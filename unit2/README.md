# Unit 2 – Motors, Mayhem, and the H-Bridge

Time to make stuff move and not blow the lab's breaker.

What you'll tinker with:
- Driving DC motors using an H-bridge so you can spin both ways.
- Using ultrasonic distance as a throttle in `2_hypersonic.ino`.
- Wrangling code that deals with higher current loads.

Firmware focus:
- `analogWrite` for PWM speed control.
- Reading sensors while juggling motor states.

Electrical street smarts:
- Separate motor power from logic power unless you like random resets.
- Back-EMF diodes and why inductive kickback is evil.
- Heat, current, and choosing a driver that doesn't cook itself.

Files in this folder:
- `2_hDrive_test1.ino` — test the driver.
- `2_hypersonic.ino` — drive by sonic vibes.
- `2_motor_Hyper1[MCADMOUSE].ino` — full project mashup.

Respect the amps or the amps will disrespect you.
