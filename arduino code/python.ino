int a=8,b=4,pwm=5,test=0;
bool i=0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(a,OUTPUT);
pinMode(b,OUTPUT);
pinMode(pwm,OUTPUT);  
pinMode(4,OUTPUT);
digitalWrite(3,LOW);
  
  // put your main code here, to run repeatedly:
  while(1){
    Serial.print("2")   ;
 if(Serial.read()=='a'){
digitalWrite(a,LOW);
digitalWrite(b,HIGH);
digitalWrite(5,HIGH);
digitalWrite(3,HIGH);
Serial.print("1");}
else
{
digitalWrite(3,LOW);  
analogWrite(pwm,0);
}
}
}
void loop(){
 
}

  
  


