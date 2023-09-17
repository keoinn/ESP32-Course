// Requirement: PWMOutESP32
#include <PWMOutESP32.h>

int redPin = 15;    // R 紅色LED控制腳 連接到ESP32的 GPIO15
int greenPin = 17;  // G 綠色LED控制腳 連接到ESP32的 GPIO17
int bluePin = 16;   // B 藍色LED控制腳 連接到ESP32的 GPIO16 
#define FADESPEED 50     // 速度
#define MAXIMUM_LIMIT 10
#define MINIMUM_LIMIT 0
int START_MAXIMUM = MAXIMUM_LIMIT -1;


void setup()    
{   
  pinMode(redPin, OUTPUT);   //設置redPin對應的管腳GPIO15為輸出
  pinMode(greenPin, OUTPUT); //設置greenPin對應的管腳GPIO17為輸出
  pinMode(bluePin, OUTPUT);  //設置bluePin對應的管腳GPIO16為輸出
}    


void loop() {
  int r, g, b;
  PWMOutESP32 pwm;
  // 由藍到紫
  for (r = MINIMUM_LIMIT; r < MAXIMUM_LIMIT; r++) { 
    pwm.analogWrite(redPin, r);
    delay(FADESPEED);
  } 
  // 由紫到紅
  for ( b = START_MAXIMUM; b > MINIMUM_LIMIT; b--) { 
    pwm.analogWrite(bluePin, b);
    delay(FADESPEED);
  } 
  // 由紅到黃
  for (g = MINIMUM_LIMIT; g < MAXIMUM_LIMIT; g++) { 
    pwm.analogWrite(greenPin, g);
    delay(FADESPEED);
  } 
  // 由黃到綠
  for (r = START_MAXIMUM; r > MINIMUM_LIMIT; r--) { 
    pwm.analogWrite(redPin, r);
    delay(FADESPEED);
  } 
  // 由綠到藍綠色
  for (b = MINIMUM_LIMIT; b < MAXIMUM_LIMIT; b++) { 
    pwm.analogWrite(bluePin, b);
    delay(FADESPEED);
  } 
  // 由藍綠色到藍色
  for (g = START_MAXIMUM; g > MINIMUM_LIMIT; g--) { 
    pwm.analogWrite(greenPin, g);
    delay(FADESPEED);
  }
}
