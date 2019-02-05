//how would multiple sensors and multiple stop lights end up working together?
//could you think of a logical-if/then/else solution?

#include <millisDelay.h> //millisDelay library - rather handy

millisDelay ledDelay;

int MOTION_PIN = 2;
int GREEN = 13;
int YELLOW = 12;
int RED = 11;

void setup() {
  ledDelay.start(5); //initialize the timer library
  pinMode(GREEN, OUTPUT); //LED pin
  pinMode(YELLOW, OUTPUT); //LED pin
  pinMode(RED, OUTPUT); //LED pin
  pinMode(MOTION_PIN, INPUT_PULLUP); //PIR sensor
}

void loop() {
  int proximity = digitalRead(MOTION_PIN); //turning the LOW/HIGH into a number because numbers are good
  if (ledDelay.isFinished()) { //if we aren't timing something else
    if (proximity > 0) { //if proximity is LOW - remember my sensor pulls low when it detects motion
      ledDelay.start(5000);  // start a 5sec delay
      green(); //green light configuration
      Serial.println("GREEN MEANS GO");
    } else {
      yellow(); //stopping mechanism
    }
  }
}


void green() {
  digitalWrite(GREEN, HIGH);//GREEN ON
  digitalWrite(YELLOW, LOW); //YELLOW OFF
  digitalWrite(RED, LOW); //RED OFF
}

void yellow() {
  Serial.println("WHOA BUCKEROO!!!");
  digitalWrite(YELLOW, HIGH); //YELLOW ON
  digitalWrite(GREEN, LOW);//GREEN OFF
  digitalWrite(RED, LOW); //RED OFF
  delay(1000); //a little barbaric, but gets the job done in a way that makes sense with the stop light
  red(); //you should quit it now
}

void red() {
  digitalWrite(RED, HIGH); //RED ON
  digitalWrite(GREEN, LOW);//GREEN OFF
  digitalWrite(YELLOW, LOW); //YELLOW OFF
  Serial.println("STOPSTOPSTOPIT");
}
