int MOTION_PIN = 2;

int GREEN = 13;
int YELLOW = 12;
int RED = 11;

void setup() {
  pinMode(GREEN, OUTPUT); //LED pin
  pinMode(YELLOW, OUTPUT); //LED pin
  pinMode(RED, OUTPUT); //LED pin

  pinMode(MOTION_PIN, INPUT_PULLUP); //PIR sensor
}

// the loop function runs over and over again forever
void loop() {
  int proximity = digitalRead(MOTION_PIN); //turning the LOW/HIGH into a number because numbers are good

  if (proximity == 0) {
    digitalWrite(GREEN, HIGH);//GREEN ON
    delay(250);
    digitalWrite(GREEN, LOW); //GREEN OFF
    delay(500);
    digitalWrite(YELLOW, HIGH); //YELLOW ON
    delay(250);
    digitalWrite(YELLOW, LOW); //YELLOW OFF
    delay(250);
    digitalWrite(RED, HIGH); //RED ON
    delay(1000);
    digitalWrite(RED, LOW); //RED OFF

  }
}
