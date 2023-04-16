#include <string.h>
#include <Servo.h>

Servo servoZ;

const int en = 8;
const int switchPinX = 12;
const int switchPinY = 13;
const int pumpPin = 10;
const int stepPinX = 5;
const int dirPinX = 2;
const int stepPinY = 7;
const int dirPinY = 4;
const int servoPinZ = 11;

const float distancePerCell = 3.5; //cm
const long pulsePerRound = 200; // so xung/vong
const long distancePerRound = 4 ; //cm
const long pulsePerDistance = pulsePerRound/distancePerRound;  //pulse/cm

char Home[] = "AK";
char Term[] = "BK";
char Eat[] = "JE";

char P_start1[] = "BH";
char P_end1[] = "EH";
char is_exist1[] = "F";

char P_start2[] = "EH";
char P_end2[] = "ED";
char is_exist2[] = "T";

char P_start3[] = "BJ";
char P_end3[] = "CH";
char is_exist3[] = "F";

char P_start4[] = "CJ";
char P_end4[] = "EH";
char is_exist4[] = "F";

char P_start5[] = "AJ";
char P_end5[] = "BJ";
char is_exist5[] = "F";

String str;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  // khai bao chan
  pinMode(en, OUTPUT); // Enable
  pinMode(stepPinX, OUTPUT); // Step
  pinMode(dirPinX, OUTPUT); // Dir
  pinMode(stepPinY, OUTPUT); // Step
  pinMode(dirPinY, OUTPUT); // Dir
  pinMode(switchPinX, INPUT); //cong tac X
  pinMode(switchPinY, INPUT); //cong tac Y
  servoZ.attach(servoPinZ); //servo Z
  pinMode(pumpPin, OUTPUT); //giac hut

  //moveHome();
  
}

void loop() {
    if (Serial.available()) {
    str = Serial.readStringUntil('\r');
    Serial.println(str);
    if (str == "1") {
      robotMove(P_start1, P_end1, is_exist1);
      Serial.println("done"); 
      delay(100000000);    
    }
    if (str == "2") {
      robotMove(P_start2, P_end2, is_exist2);
      Serial.println("done"); 
      delay(100000000);    
    }
    if (str == "3") {
      robotMove(P_start3, P_end3, is_exist3);
      Serial.println("done"); 
      delay(100000000);    
    }
    // if (str == "4") {
    //   robotMove(P_start4, P_end4, is_exist4);
    //   Serial.println("done"); 
    //   delay(100000000);    
    // }
    // if (str == "5") {
    //   robotMove(P_start5, P_end5, is_exist5);
    //   Serial.println("done"); 
    //   delay(100000000);    
    // }
  }
}



void moveXY(long nStepX, int stepPinX, long nStepY, int stepPinY) {

  float nStepMax = nStepX;
  float nStepMin = nStepY;
  int stepPinMax = stepPinX;
  int stepPinMin = stepPinY;

  float current_axis_min = 0;
  long steps_axis_min = 0;
  float ratio_max_min = 0;

  if (nStepY > nStepX) {
    nStepMax = nStepY;
    nStepMin = nStepX;
    stepPinMax = stepPinY;
    stepPinMin = stepPinX;
  }

  ratio_max_min = nStepMax / nStepMin;

  for (int i = 1 ; i <= nStepMax ; i = i + 1) {
    current_axis_min = i / ratio_max_min;

    if (current_axis_min - steps_axis_min >= 1) {
      digitalWrite(stepPinMin, HIGH);
      steps_axis_min++;
    }

    digitalWrite(stepPinMax, HIGH);
    delay(3);

    digitalWrite(stepPinMax, LOW);
    digitalWrite(stepPinMin, LOW);
    delay(3);
  }
}

void movePtoP(char P_start[], char P_end[]) {
  if ((int)P_start[0] < (int)P_end[0]){
    int dis_X = (int)P_end[0] - (int)P_start[0];
    // Serial.print(stepX);
    // Serial.println(" buoc cung chieu X");
    if ((int)P_start[1] < (int)P_end[1]) {
      int dis_Y = (int)P_end[1] - (int)P_start[1];
      digitalWrite(dirPinX, LOW); // Set Enable low
      digitalWrite(dirPinY, LOW);
      moveXY(dis_X * pulsePerDistance * distancePerCell, stepPinX, dis_Y * pulsePerDistance * distancePerCell, stepPinY);
      // Serial.print(stepY);
      // Serial.println(" buoc cung chieu Y");
    }
    else {
      int dis_Y = (int)P_start[1] - (int)P_end[1];
      digitalWrite(dirPinX, LOW); // Set Enable low
      digitalWrite(dirPinY, HIGH);
      moveXY(dis_X * pulsePerDistance * distancePerCell, stepPinX, dis_Y * pulsePerDistance * distancePerCell, stepPinY);
      // Serial.print(stepY);
      // Serial.println(" buoc nguoc chieu Y");
    }
  }
  else {
    int dis_X = (int)P_start[0] - (int)P_end[0];
    // Serial.print(stepX);
    // Serial.println(" buoc nguoc chieu X");
    if ((int)P_start[1] < (int)P_end[1]) {
      int dis_Y = (int)P_end[1] - (int)P_start[1];
      digitalWrite(dirPinX, HIGH); // Set Enable low
      digitalWrite(dirPinY, LOW);
      moveXY(dis_X * pulsePerDistance * distancePerCell, stepPinX, dis_Y * pulsePerDistance * distancePerCell, stepPinY);
      // Serial.print(stepY);
      // Serial.println(" buoc cung chieu Y");
    }
    else {
      int dis_Y = (int)P_start[1] - (int)P_end[1];
      digitalWrite(dirPinX, HIGH); // Set Enable low
      digitalWrite(dirPinY, HIGH);
      moveXY(dis_X * pulsePerDistance * distancePerCell, stepPinX, dis_Y * pulsePerDistance * distancePerCell, stepPinY);
      // Serial.print(stepY);
      // Serial.println(" buoc nguoc chieu Y");
    }
  }
}

void moveHome() {
  int switch_valX = digitalRead(switchPinX);
  int switch_valY = digitalRead(switchPinY);
  while (switch_valY == 1) {
    digitalWrite(dirPinY, LOW);
    digitalWrite(stepPinY, HIGH);
    delay(3);
    digitalWrite(stepPinY, LOW);
    delay(3);
    switch_valY = digitalRead(switchPinY);
  }
  while (switch_valX == 1) {
    digitalWrite(dirPinX, HIGH);
    digitalWrite(stepPinX, HIGH);
    delay(3);
    digitalWrite(stepPinX, LOW);
    delay(3);
    switch_valX = digitalRead(switchPinX);
  }
}

void pump() {
  int pos = 0;
  // servo xuong
  for (pos = 0; pos <= 180; pos += 5) { 
    servoZ.write(pos);
    delay(50);
  }
  digitalWrite(pumpPin, HIGH);
  delay(100);
  // servo len
  for (pos = 180; pos >=0; pos -= 5) { 
    servoZ.write(pos);
    delay(50);
  }
}

void release() {
  int pos = 0;
  // servo xuong
  for (pos = 0; pos <= 120; pos += 5) { 
    servoZ.write(pos);
    delay(50);
  }
  digitalWrite(pumpPin, LOW);
  delay(100);
  //servo len
  for (pos = 120; pos >=0; pos -= 5) { 
    servoZ.write(pos);
    delay(50);
  }
}

void robotMove(char P_start[], char P_end[], char is_exist[]) {
  int switch_valX = digitalRead(switchPinX);
  int switch_valY = digitalRead(switchPinY);
  if (is_exist[0] == 'F') {
    moveHome();
    delay(100);
    movePtoP(Home, P_start);
    delay(100);
    pump();
    delay(100);
    movePtoP(P_start, P_end);
    delay(100);
    release();
    delay(100);
    moveHome();
    delay(100);
    movePtoP(Home, Term);
  }
  if (is_exist[0] == 'T') {
    moveHome();
    delay(100);
    movePtoP(Home, P_end);
    delay(100);
    pump();
    delay(100);
    moveHome();
    delay(100);
    release();
    movePtoP(Home, P_start);
    delay(100);
    pump();
    delay(100);
    movePtoP(P_start, P_end);
    delay(100);
    release();
    delay(100);
    moveHome();
    delay(100);
    movePtoP(Home, Term);
  }
}






