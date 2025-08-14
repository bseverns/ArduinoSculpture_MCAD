# Unit 5 – Web Feeds & Network Mischief

Time to sling sensor data onto the web.

## Electrical guts

- Serial over USB still needs proper grounding between Arduino and your computer.
- Keep wires short and shielded if the signal acts haunted.

## Firmware moves

- `Serial.print()` streams data to whatever’s listening.
- A p5.js sketch slurps the serial stream and paints pixels with it.
- Mind the baud rate; both sides need to agree or you get gibberish.

The Arduino sketch pushes data, the p5 file grabs it and feeds a browser. Bend the data, break the internet (politely).
