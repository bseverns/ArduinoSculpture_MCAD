# Unit 4 – PIR Patrol & OOP

Motion sensing meets object-oriented flair.

## Electrical guts

- PIR sensors spit out a digital HIGH when they see warm bodies.
- Give them 5V, ground, and wait for the calibration swagger.
- They’re noisy; debounce or add delay if your sculpture freaks out.

## Firmware moves

- Wrap sensor logic in classes so your code stays clean and mean.
- Use `millis()` instead of delay to keep things responsive.
- Trigger sounds or animations when the sensor trips.

Three sketches show vanilla PIR use, a tiny sound-trigger version, and an OOP approach. Customize to taste.
