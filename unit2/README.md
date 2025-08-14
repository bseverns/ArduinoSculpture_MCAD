# Unit 2 – Motors & Ultrasonic Chaos

Now we make things move and scream.

## Electrical guts

- H-bridges let you flip motor direction without burning out pins.
- Motors demand real current; give them external juice and common ground.
- Ultrasonic sensors (like HC-SR04) use 5V logic; mind the wiring and timing.

## Firmware moves

- `digitalWrite()` and `analogWrite()` to control direction and speed.
- Pulse the trigger pin, listen for echo to measure distance.
- Use libraries or raw `pulseIn()` to translate echo time to centimeters.

The examples here drive motors with an H-bridge and read an ultrasonic sensor to dodge obstacles. Go wild.
