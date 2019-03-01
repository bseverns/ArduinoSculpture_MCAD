const int SensorSignal = 2; // PIR on digital pin 2
const int soundC1 = 7; //00 soundie digital pin 7
const int soundC2 = 6;// 01 soundie digital pin 6
int sensorValue = 0; //PIR sensor value
int pcount = 0; // number of loops

void setup() {
  pinMode(SensorSignal, INPUT); // declare digital pin 2 as input, this is where you connect the S output from your sensor, this can be any digital pin
  pinMode(soundC1, OUTPUT); //0 on the soundie
  pinMode(soundC2, OUTPUT); //1 on the soundie
  Serial.begin(9600); //for checking
}

void loop() {
  sensorValue = digitalRead(SensorSignal); // read the value of pin 2, should be high or low
  if (sensorValue == HIGH) { //if motion
    //play sound
    if (pcount < 50) {
      for (i = 0; i < 50; i++) {
        digitalWrite(soundC1, HIGH); //on
        pcount++; //add one to pcount
        delay(2);
        Serial.println("1");
        digitalWrite(soundC1, LOW); //off
      }
    } else if (pcount < 100) {
      for (i = 0; i < 50; i++) {
        digitalWrite(soundC2, HIGH);//on
        pcount++; //add one to pcount
        delay(2);
        digitalWrite(soundC2, LOW);//low
      }
    } else if ({
    for (i = 0; i < 50; i++) {
        digitalWrite(soundC1, HIGH);//on
        digitalWrite(soundC2, HIGH);//on
        pcount++; //add one to pcount
        delay(2);
        digitalWrite(soundC1, LOW);//off
        digitalWrite(soundC2, LOW);//off
      }

    } else {
      digitalWrite(soundC1, LOW);//off
      digitalWrite(soundC2, LOW);//off
    }

    if (pcount > 149) {//reset
    pcount == 0;
  }
}
//code End
