# Unit 1 – Blink Like You Mean It

Welcome to the crash course in forcing electrons to dance. In this unit you learn to drive an LED with digital pins, respect Ohm's law, and sample simple sensors.

## Electrical guts

- Use current-limiting resistors so you don't fry the LED or the board.
- Understand the difference between digital outputs and analog inputs.
- Wire sensors with power, ground, and a signal line that feeds into `A0` or any other analog pin.

## Firmware moves

- `digitalWrite()` to slam a pin HIGH or LOW.
- `pinMode()` is the handshake between your code and the hardware.
- `analogRead()` lets you peek at sensor values and map them to LED brightness.

The sketches in this folder show a basic blink, an object-oriented spin on it, and a simple sensor-controlled LED. Hack them, break them, learn.
