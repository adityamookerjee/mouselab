#include "HX711.h"

#define DOUT  3
#define CLK  2
unsigned long time = 0;
HX711 scale(DOUT, CLK);

float calibration_factor = -1050.0; 
  
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  weight = scale.get_units();
}

void loop() {
  while (weight <-5) {
    time=millis();
    Serial.print(time);
    Serial.print( , ); 
    Serial.println(weight,2);
  }
  
  // put your main code here, to run repeatedly:

}
