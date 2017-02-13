#define ML 0
#define MR 0
#define L1 0
#define L2 0
#define R1 0
#define R2 0
#define pulsed 1000

String req = "";
 

void setup()
{
  // pinMode() and Serial.begin()
  pinMode(MR, OUTPUT);
  pinMode(ML, OUTPUT);
  pinMode(L1, OUTPUT);
  pinMode(L2, OUTPUT);
  pinMode(R1, OUTPUT);
  pinMode(R2, OUTPUT);
  Serial.println("0"); //port opened
}

void loop()
{
  if(Serial.available() > 0) { req = Serial.read(); }

  if (req == "0")
  {
    // return ADC output from the pins, Serial.println()
    // AnalogPin = 0, 1
    Serial.println(String(analogRead(0)) + "." + String(analogRead(1)) +"." + String(analogRead(2)));
  }

  else
  {
    // read from the string DLLLLLRRRRR
    motor(req.substring(0,1), req.substring(1,7).toFloat(), req.substring(7).toFloat());
    Serial.println("spin complete");
  }
}

bool motor(bool fw, float dutyL, float dutyR)
{

  if (fw) {
    analogWrite(ML, int(dutyL * 255));
    analogWrite(MR, int(dutyR * 255));
    digitalWrite(L1, HIGH);
    digitalWrite(L2, LOW);
    digitalWrite(R1, HIGH);
    digitalWrite(R2, LOW);
    delay(pulsed);
    digitalWrite(ML, LOW);
    digitalWrite(MR, LOW);
  }
  
  else {
    analogWrite(ML, int(dutyL * 255));
    analogWrite(MR, int(dutyR * 255));
    digitalWrite(L1, LOW);
    digitalWrite(L2, HIGH);
    digitalWrite(R1, LOW);
    digitalWrite(R2, HIGH);
    delay(pulsed);
    digitalWrite(ML, LOW);
    digitalWrite(MR, LOW);
  }
}