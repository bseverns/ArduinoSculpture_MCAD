# Unit 5 – The Lamp That Reads the Web

Mash up the internet, Processing, and Arduino to make light react to headlines.

Here's the game plan:
- Processing sketch (`5_WebFeed_p5`) fetches a feed and parses words.
- Arduino sketch (`5_WebFeed_ardu`) streams sensor data and listens for RGB values.
- Serial protocol mania: sending `#RRGGBB` strings and reading analog sensors.

Firmware nuts and bolts:
- `Serial.begin`, `Serial.read`, `analogWrite`, and converting hex to bytes.

Electrical angles:
- Driving an RGB LED with three PWM pins and appropriate resistors.
- Sharing ground between computer, Arduino, and any external power.

Files:
- `5_WebFeed_ardu` — Arduino side.
- `5_WebFeed_p5` — Processing side.

When the net says “love” or “arduino,” your lamp screams it in color. Rock on.
