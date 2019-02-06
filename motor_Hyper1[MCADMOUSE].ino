//Set up motor

//define the two direction logic pins and the speed / PWM pin
const int m1DIR_A = 5;
const int m1DIR_B = 4;
const int PWM1 = 6;

const int m2DIR_A=8;
const int m2DIR_B=7;
const int PWM2 =9;

const int trigPin = 13;
const int echoPin = 12;
const int led = 11;
const int led2 = 10;

void setup() {
  Serial.begin (9600); //need to add this if you want to see communication back-forth with your board. much encourage
  
  //sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  //led pins
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);

  //motor1
  pinMode(m1DIR_A, OUTPUT);
  pinMode(m1DIR_B, OUTPUT);
  pinMode(PWM1, OUTPUT);
  //motor2
  pinMode(m2DIR_A, OUTPUT);
  pinMode(m2DIR_B, OUTPUT);
  pinMode(PWM2, OUTPUT);
  
  //triple check the serial thing is doing
  Serial.println("setup");
}

void loop() {
///This next stuff is for finding out where we are in relation to stuff
  long duration, distance; //variables to measure things
  digitalWrite(trigPin, LOW);  // pulse off
  delayMicroseconds(2); // quick pause
  digitalWrite(trigPin, HIGH); //pulse on
  delayMicroseconds(10); // pause
  digitalWrite(trigPin, LOW); //pulse off
  duration = pulseIn(echoPin, HIGH); //duration determined bu how long/often the echoPin reads HIGH
  distance = (duration / 2) / 29.1; //how long the pulse took to hear divided by the speed of sound

  /*
     Below this zone is where you manipulate the motors!!!!
try setting timing to control how much the mouse turns
     !!!!!!!
  */

  if (distance < 5) {  
    
    // This is where the LED On/Off happens
    //add more variance here- play with those patterns &&the timer library to give us a show while the motors do their thing
    //&&the sensors does its thing
    
    digitalWrite(led, HIGH); // When the Red condition is met, the Green LED should turn off or whatever
    digitalWrite(led2, LOW);

    //MOTORS - check the chart posted on the git wiki for HIGH/LOW patterns
    //forward
    digitalWrite(m1DIR_A, HIGH); //on
    digitalWrite(m1DIR_B, LOW); //off
    analogWrite(PWM1, 255); //on [range of 0-255, on-off]
    
    digitalWrite(m2DIR_A, HIGH);
    digitalWrite(m2DIR_B, LOW);
    analogWrite(PWM2, 255);
    
    Serial.print("FORWARD!!!");
  }
  else {
    //lights
    digitalWrite(led, LOW);
    digitalWrite(led2, HIGH);

    //turn in a direction
    digitalWrite(m1DIR_A, LOW);
    digitalWrite(m1DIR_B, HIGH);
    analogWrite(PWM, 255);
    
    digitalWrite(m2DIR_A, HIGH);
    digitalWrite(m2DIR_B, LOW);
    analogWrite(PWM1, 255);
    
    Serial.print("TURN!!!");
  }
///////////////////////////////////////////////////////////////////


  if (distance >= 200 || distance <= 0) { //too far? try changing these numbers, like the 200
    Serial.println("Out of range");
  }
  else {
    Serial.print(distance);
    Serial.println(" cm");
  }
  delay(500); //maybe delete this thing?
}
