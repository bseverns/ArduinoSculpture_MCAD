/*
 * LED Example
 * Sensor will turn on and off the lights.
 */

float sensorState  = 0; //Switches when sensor is activated
const int SENSOR = 5; //const means unchangeable int pin for sensor
int ledState = LOW;  //State of LED lights (on/off) defaulting setting state as off
 
const int RED_LED = 7; //RED Led PIN
const int BLUE_LED = 6; //BLUE LED PIN

void setup() {
  // put your setup code here, to run once:
 pinMode(RED_LED, OUTPUT );  
 pinMode(BLUE_LED, OUTPUT);
 pinMode(SENSOR, INPUT);
 Serial.begin(9600);         //a set up for data on serial monitor( MONITOR is the cirle, TOP RIGHT OF PAGE)
 
} 

void loop() {
  // put your main code here, to run repeatedly:
  sensorState = digitalRead(SENSOR);
  Serial.println(sensorState);          //Printed data on serial monitor from sensor
  
  if (sensorState == HIGH) {            //if in range of sensor
    if (ledState == HIGH) {             //and LED is ON
      ledState = LOW;                   //then change LED to OFF
      digitalWrite(RED_LED, ledState );   //changes RED LED to OFF state
      digitalWrite(BLUE_LED, ledState );  //changes BLUE LED to OFF state
      delay(500);
      
    } else if (ledState == LOW) {         //if LED is OFF
      ledState = HIGH;                    //change LED ON when in range
      digitalWrite(RED_LED, ledState );   //changes RED LED to ON state
      digitalWrite(BLUE_LED, ledState );  //changes BLUE LED to ON state
      delay(500);
    }
    
  }
                 
}
