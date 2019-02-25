const int SensorSignal = 2; // PIR on digital pin 2
const int soundC1 = 7; //00 soundie digital pin 7
const int soundC2 = 6;// 01 soundie digital pin 6
int sensorValue = 0; //
int pcount = 0; // number of loops

void setup() {
  pinMode(SensorSignal, INPUT); // declare digital pin 2 as input, this is where you connect the S output from your sensor, this can be any digital pin
  pinMode(soundC1, OUTPUT);
  pinMode(soundC2, OUTPUT);
}

void loop() {
  sensorValue = digitalRead(SensorSignal); // read the value of pin 2, should be high or low
  if (sensorValue == HIGH) {
    //play sound
    if (pcount < 50) {
      for (i = 0; i < 50; i++) {
        digitalWrite(soundC1, HIGH);
        pcount++;
        delay(2);
      }
    } else if (pcount < 100) {
      for (i = 0; i < 50; i++) {
        digitalWrite(soundC2, HIGH);
        pcount++;
        delay(2);
      }
    } else {
      for (i = 0; i < 50; i++) {
        digitalWrite(soundC1, HIGH);
        digitalWrite(soundC2, HIGH);
        pcount++;
        delay(2);
      }
    } else {
      digitalWrite(ledPin, LOW);
    }

    if (pcount > 149) {
      pcount == 0;
    }
  }
  //code End
