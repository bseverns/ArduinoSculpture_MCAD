#!/usr/bin/env python3
"""Build reproducible kit archives for every teaching unit.

The script creates a `Unit-Kit.zip` alongside each unit directory. The kit is
self-contained and holds:
  * `sketches/` — cleaned copies of every sketch or code artifact.
  * `libraries/` — any Arduino libraries the unit ships with (or a note if none
    are needed).
  * `docs/Unit-Guide.pdf` — a quick-and-dirty PDF render of the unit README so
    folks can print or share it without futzing with Markdown viewers.

Run this from the repository root after you tweak unit content to refresh the
kits.
"""

from __future__ import annotations

import argparse
import os
import shutil
import textwrap
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List, Sequence

BASE_DIR = Path(__file__).resolve().parent

PDF_PAGE_WIDTH = 612  # 8.5 inches * 72 points per inch
PDF_PAGE_HEIGHT = 792  # 11 inches * 72 points per inch
PDF_MARGIN_LEFT = 72
PDF_MARGIN_TOP = 720
PDF_LINE_HEIGHT = 14
PDF_FONT_NAME = "F1"
PDF_FONT_SIZE = 12
PDF_MAX_LINES = 45  # keeps us comfortably on the page
ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def build_all_kits(units: Sequence[Path]) -> None:
    for unit in units:
        build_single_kit(unit)


def build_single_kit(unit_dir: Path) -> None:
    kit_zip_path = unit_dir / "Unit-Kit.zip"
    if kit_zip_path.exists():
        kit_zip_path.unlink()

    with TemporaryDirectory() as temp_dir:
        staging_root = Path(temp_dir) / "kit"
        docs_dir = staging_root / "docs"
        libraries_dir = staging_root / "libraries"
        sketches_dir = staging_root / "sketches"

        for folder in (docs_dir, libraries_dir, sketches_dir):
            folder.mkdir(parents=True, exist_ok=True)

        pdf_path = docs_dir / "Unit-Guide.pdf"
        create_pdf_from_readme(unit_dir, pdf_path)

        copy_libraries(unit_dir, libraries_dir)
        copy_sketches(unit_dir, sketches_dir)

        write_zip_from_directory(staging_root, kit_zip_path)


def create_pdf_from_readme(unit_dir: Path, pdf_path: Path) -> None:
    readme_path = unit_dir / "README.md"
    if readme_path.exists():
        text = readme_path.read_text(encoding="utf-8")
    else:
        text = (
            "This unit currently ships without a README.\n\n"
            "Drop some knowledge in README.md so future builders aren't flying blind."
        )

    lines = prepare_pdf_lines(text)
    pages = [lines[i : i + PDF_MAX_LINES] for i in range(0, len(lines), PDF_MAX_LINES)]
    if not pages:
        pages = [["(intentionally blank)"]]

    pdf_bytes = render_simple_pdf(pages)
    pdf_path.write_bytes(pdf_bytes)


def prepare_pdf_lines(markdown_text: str) -> List[str]:
    wrapper = textwrap.TextWrapper(width=90, replace_whitespace=False, drop_whitespace=False)
    lines: List[str] = []

    for raw_line in markdown_text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            if lines and lines[-1] != "":
                lines.append("")
            continue

        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            if lines and lines[-1] != "":
                lines.append("")
            heading_text = heading.upper()
            lines.append(heading_text)
            lines.append("-" * min(len(heading_text), 90))
            continue

        if stripped.startswith(('-', '*')):
            content = stripped.lstrip('-*').strip()
            bullet = f"• {content}" if content else "•"
            wrapped = wrapper.wrap(bullet) or [bullet]
            lines.extend(wrapped)
            continue

        wrapped_body = wrapper.wrap(stripped) or [stripped]
        lines.extend(wrapped_body)

    if not lines:
        lines.append("This README was empty when we made the kit.")

    # Trim trailing blank lines to avoid empty pages.
    while lines and lines[-1] == "":
        lines.pop()

    return lines


def render_simple_pdf(pages: Sequence[Sequence[str]]) -> bytes:
    objects: List[str] = []

    font_obj_id = append_object(objects, "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")

    page_object_indices = []
    content_object_ids: List[int] = []

    for page_lines in pages:
        content_stream = build_content_stream(page_lines)
        content_obj = (
            f"<< /Length {len(content_stream.encode('utf-8'))} >>\n"
            f"stream\n{content_stream}endstream"
        )
        content_obj_id = append_object(objects, content_obj)
        content_object_ids.append(content_obj_id)
        page_object_indices.append(len(objects))  # placeholder index for later substitution
        objects.append("__PAGE_PLACEHOLDER__")

    pages_obj_id = len(objects) + 1

    for idx, content_obj_id in zip(page_object_indices, content_object_ids):
        page_obj = (
            "<< /Type /Page /Parent {pages_obj_id} 0 R "
            f"/MediaBox [0 0 {PDF_PAGE_WIDTH} {PDF_PAGE_HEIGHT}] "
            f"/Contents {content_obj_id} 0 R "
            f"/Resources << /Font << /{PDF_FONT_NAME} {font_obj_id} 0 R >> >> >>"
        )
        objects[idx] = page_obj

    kids_refs = " ".join(f"{idx + 1} 0 R" for idx in page_object_indices)
    pages_obj = f"<< /Type /Pages /Kids [{kids_refs}] /Count {len(page_object_indices)} >>"
    pages_obj_id = append_object(objects, pages_obj)

    catalog_obj = f"<< /Type /Catalog /Pages {pages_obj_id} 0 R >>"
    catalog_obj_id = append_object(objects, catalog_obj)

    return assemble_pdf_bytes(objects, catalog_obj_id)


def build_content_stream(lines: Sequence[str]) -> str:
    def escape(text: str) -> str:
        return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    commands = [
        "BT",
        f"/{PDF_FONT_NAME} {PDF_FONT_SIZE} Tf",
        f"{PDF_LINE_HEIGHT} TL",
        f"{PDF_MARGIN_LEFT} {PDF_MARGIN_TOP} Td",
    ]

    first_line = True
    for line in lines:
        safe_line = escape(line)
        if first_line:
            commands.append(f"({safe_line}) Tj")
            first_line = False
        else:
            commands.append("T*")
            commands.append(f"({safe_line}) Tj")

    if first_line:
        # We never printed anything; drop a placeholder so the PDF isn't empty.
        commands.append("() Tj")

    commands.append("ET\n")
    return "\n".join(commands) + "\n"


def append_object(objects: List[str], obj_str: str) -> int:
    objects.append(obj_str)
    return len(objects)


def assemble_pdf_bytes(objects: Sequence[str], catalog_obj_id: int) -> bytes:
    pdf_bytes = bytearray(b"%PDF-1.4\n")
    offsets: List[int] = []

    for obj_number, obj_content in enumerate(objects, start=1):
        offsets.append(len(pdf_bytes))
        obj_bytes = f"{obj_number} 0 obj\n{obj_content}\nendobj\n".encode("utf-8")
        pdf_bytes.extend(obj_bytes)

    xref_offset = len(pdf_bytes)
    pdf_bytes.extend(f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n".encode("ascii"))
    for offset in offsets:
        pdf_bytes.extend(f"{offset:010d} 00000 n \n".encode("ascii"))

    trailer = f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_obj_id} 0 R >>\n"
    pdf_bytes.extend(trailer.encode("ascii"))
    pdf_bytes.extend(f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii"))
    return bytes(pdf_bytes)


def copy_libraries(unit_dir: Path, libraries_dir: Path) -> None:
    candidate_dirs = sorted(
        {p for p in unit_dir.iterdir() if p.is_dir() and "lib" in p.name.lower()}
    )

    additional_library_dirs = sorted({p for p in unit_dir.rglob("*") if p.is_dir() and p.name.lower() == "libraries"})
    for extra in additional_library_dirs:
        if extra not in candidate_dirs:
            candidate_dirs.append(extra)

    if not candidate_dirs:
        placeholder = libraries_dir / "README.txt"
        placeholder.write_text(
            "No external Arduino libraries needed for this unit.\n"
            "If you add some later, drop them in alongside this note before rerunning build_kits.py.\n",
            encoding="utf-8",
        )
        return

    for source_dir in candidate_dirs:
        destination = libraries_dir / source_dir.name
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source_dir, destination)


def copy_sketches(unit_dir: Path, sketches_dir: Path) -> None:
    ignored = {"README.md", "Unit-Kit.zip"}
    for item in sorted(unit_dir.iterdir()):
        if item.name in ignored:
            continue
        if item.name.startswith('.'):  # skip hidden clutter
            continue
        if item.is_dir():
            # Directories that weren't recognized as libraries are skipped here; if they
            # contain sketches they should be nested under a library folder or copied
            # explicitly into the unit directory.
            continue
        if not item.is_file():
            continue

        destination_name = classify_sketch_filename(item)
        destination_path = sketches_dir / destination_name
        destination_path.write_bytes(item.read_bytes())


def classify_sketch_filename(path: Path) -> str:
    name = path.name
    suffix = path.suffix.lower()
    if suffix:
        return name

    try:
        sample = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return name

    lowered = sample.lower()
    if "void setup" in lowered and "void loop" in lowered:
        return f"{name}.ino"
    if "void setup" in lowered and "void draw" in lowered:
        return f"{name}.pde"
    if "function setup" in lowered and "createcanvas" in lowered:
        return f"{name}.js"
    return name


def write_zip_from_directory(source_dir: Path, zip_path: Path) -> None:
    files_to_write = []
    dirs_to_write = set()

    for root, dirs, files in os.walk(source_dir):
        dirs.sort()
        rel_root = Path(root).relative_to(source_dir)
        if rel_root != Path('.'):
            dirs_to_write.add(str(rel_root).replace(os.sep, '/') + '/')
        for file_name in sorted(files):
            file_path = Path(root) / file_name
            rel_path = rel_root / file_name
            rel_path_str = str(rel_path).replace(os.sep, '/')
            files_to_write.append((rel_path_str, file_path.read_bytes()))

    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for directory in sorted(dirs_to_write):
            info = zipfile.ZipInfo(directory)
            info.date_time = ZIP_TIMESTAMP
            info.external_attr = 0o755 << 16
            zip_file.writestr(info, b"")
        for rel_path, data in files_to_write:
            info = zipfile.ZipInfo(rel_path)
            info.date_time = ZIP_TIMESTAMP
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zip_file.writestr(info, data)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rebuild every Unit-Kit.zip archive.")
    parser.add_argument(
        "units",
        nargs="*",
        help="Specific unit directories to rebuild (defaults to every unit*/ folder).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.units:
        units = [BASE_DIR / unit for unit in args.units]
    else:
        units = sorted(p for p in BASE_DIR.iterdir() if p.is_dir() and p.name.startswith("unit"))

    missing = [p for p in units if not p.exists()]
    if missing:
        names = ", ".join(str(m) for m in missing)
        raise SystemExit(f"Could not find the requested unit directories: {names}")

    build_all_kits(units)
    print(f"Generated {len(units)} kit(s).")


if __name__ == "__main__":
    main()
