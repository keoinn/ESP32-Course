// Requirement: PWMOutESP32
#include <PWMOutESP32.h>

int redPin = 15;    // R 紅色LED控制腳 連接到ESP32的 GPIO15
int greenPin = 17;  // G 綠色LED控制腳 連接到ESP32的 GPIO17
int bluePin = 16;   // B 藍色LED控制腳 連接到ESP32的 GPIO16 
void setup()    
{   
	pinMode(redPin, OUTPUT);   //設置redPin對應的管腳GPIO15為輸出
	pinMode(greenPin, OUTPUT); //設置greenPin對應的管腳GPIO17為輸出
	pinMode(bluePin, OUTPUT);  //設置bluePin對應的管腳GPIO16為輸出
}    
      
void loop()  
{    
     
    // Basic colors:  
    color(255, 0, 0); // 红色亮
    delay(1000); //延時一秒 
    color(0,255, 0); //綠色亮
    delay(1000); //延時一秒
    color(0, 0, 255); //藍色亮  
    delay(1000); //延時一秒

    // Example blended colors:  
    color(255,255,0); // 黄色亮
    delay(1000); //延時一秒      
    color(128,0,255); // 紫色亮  
    delay(1000); //延時一秒
    color(255,255,255); // 白色亮  
    delay(1000); //延時一秒
    color(0,0,0); // 關閉led  
    delay(1000); //延時一秒  
        
}  

//顏色控制函數
void color (unsigned char red, unsigned char green, unsigned char blue)
{    
  PWMOutESP32 pwm;
  pwm.analogWrite(redPin, red);   
  pwm.analogWrite(greenPin,green); 
  pwm.analogWrite(bluePin, blue); 
} 
