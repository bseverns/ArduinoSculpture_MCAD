# Classy Tidings
Sculpture Studio: Arduino  
SC 3082 Spring19

This repo is the playground for SC 3082 "Sculpture Studio: Arduino", Spring 2019 at the Minneapolis College of Art and Design.

## Units

We carved each chunk of the course into its own folder:

- [unit1](unit1/README.md) — make an LED blink, read some sensors, and dip a toe into OOP without selling your soul.
- [unit2](unit2/README.md) — wrestle motors with an H-bridge and learn why power supplies hate you.
- [unit4](unit4/README.md) — spot warm bodies with PIR sensors and trigger noise like a pro.
- [unit5](unit5/README.md) — sling data between Arduino, Processing, and the web without losing any bytes.

Unit numbers follow the original syllabus, so yeah, we jump from 2 to 4. We did no-code work in unit 3 where we spent an hour alone, without cell phones or media sources we could personally controll, just existing in the world and noticing it happen, considering inputs and outputs.

Check -link- soon for photo/video documentation!

## Unit kits for the roadies

Need a whole Arduino lesson in your backpack? Run the kit builder and a
fresh "Unit-Kit.zip" will pop up inside each unit folder. Crack it open and
you'll find:

- `sketches/` with cleaned copies of the code so you can flash boards without
  spelunking through git history.
- `libraries/` for any helper code a unit leans on. If the folder only contains
  a loudmouth README, it means the unit rides stock Arduino libraries.
- `docs/Unit-Guide.pdf` — a printable take on the README because sometimes the
  studio Wi-Fi ghosts out exactly when you need instructions.

Regenerate the whole pile any time you tweak a unit:

```bash
python build_kits.py
```

You can also feed it a subset if you're only remixing one or two modules:

```bash
python build_kits.py unit4 unit5
```

The script pins timestamps so rerunning it won't churn needless git diffs.
These ZIPs are generated artifacts, so the repo ignores them—sling the fresh
archives to students, but keep source control clean. Add your new content,
rebuild, and hand the kits to whoever needs them.

### CI babysitter

When a pull request hits GitHub, a workflow boots up, runs `python build_kits.py`,
and makes sure the repo doesn't get dirty in the process. That way the kit
builder stays honest, and we never merge a script that barfs on the people
depending on it. Consider it our automated roadie doing a line check before
the show.

License: [MIT](LICENSE)
