#include <SoftwareSerial.h>
  
SoftwareSerial mySerial(11,10);// RX,TX 38400

int btState = 12;
const int pinLED = 13;

// Here Led Variables
int led_left = 4;
int led_right = 2;
int led_center = 3;

int button =  6;
boolean button_pas = true;

char DATO = '4';

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
  Serial.println("Start"); 
  
  pinMode(button,INPUT); 

  // PinMode Leds
  pinMode(led_left, OUTPUT);
  pinMode(led_right, OUTPUT);
  pinMode(led_center, OUTPUT);  

  pinMode(btState,INPUT);
  pinMode(pinLED, OUTPUT);

  //buzzer pin
  pinMode(A0,OUTPUT);
}

void loop() {
  if(mySerial.available() > 0){
      DATO = mySerial.read();
  }

  //According to the byte, a different led turns on 
  if(DATO == '1') {
    
    Serial.println("neutro");
    digitalWrite(led_center, HIGH);
    digitalWrite(led_left, LOW);
    digitalWrite(led_right, LOW);
    
    if(button_pas){
      noTone(A0);
    }
    
   }else if (DATO == '2') {
    
    Serial.println("left");
    digitalWrite(led_left, HIGH);
    digitalWrite(led_center, LOW);
    digitalWrite(led_right, LOW);

    if(button_pas){
      noTone(A0);
    }
         
   }else if (DATO == '3') {
    
    Serial.println("right");
    digitalWrite(led_right, HIGH);
    digitalWrite(led_center, LOW);
    digitalWrite(led_left, LOW);

    if(button_pas){
      noTone(A0);
    }
         
   }else if (DATO == '0') {
    
    Serial.println("blink");
    digitalWrite(led_left, HIGH);
    digitalWrite(led_right, HIGH);
    digitalWrite(led_center, HIGH);

    tone(A0, 440);
    button_pas = false;
          
   }else if(DATO == '4'){
    
    // Turn off all the lights
    digitalWrite(led_left, LOW);
    digitalWrite(led_right, LOW);
    digitalWrite(led_center, LOW);
    Serial.println("nada");

    if(button_pas){
      noTone(A0);
    }
   }

  if(digitalRead(btState)==LOW){
     digitalWrite(pinLED, LOW);
   }else{
     digitalWrite(pinLED, HIGH);
   }


   if(digitalRead(button)==HIGH){

    //insert comment
    button_pas = true;
    
  }

}
