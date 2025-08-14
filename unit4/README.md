# Unit 4 – PIRs and Other Ghost Stories

Motion sensing without cameras, just warm bodies and cheap sensors.

Learn to:
- Read PIR (Passive Infrared) sensors to detect movement.
- Gate audio or other outputs when something moves.
- Wrap sensor logic in C++ classes for reuse.

Firmware bits:
- `digitalRead`, debouncing, timers for ignoring sensor noise.
- Using simple state machines to decide when to trigger.

Electrical truths:
- PIR modules like 5V and spit out a clean digital signal.
- Give them a minute to warm up or they'll lie to you.
- Use a pull-down resistor if your module doesn't include one.

Files:
- `4_PIRsimpler.ino` — bare minimum to trip on motion.
- `4_PIRlittlesoundie.ino` — fire off a tune when someone walks by.
- `4_OOP_PIR.ino` — same deal, now in class form.

Keep it creepy, keep it stable.
