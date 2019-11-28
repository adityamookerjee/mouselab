#include "HX711.h"

#define calibration_factor -1050.0 //This value is obtained using the SparkFun_HX711_Calibration sketch

#define DOUT  3
#define CLK  2
unsigned long time;
HX711 scale(DOUT, CLK);
void setup() {
  Serial.begin(9600);
  Serial.println("HX711 scale demo");

  scale.set_scale(calibration_factor); 
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0


  Serial.println(time);
}

void loop() {
  
  time = millis();
  Serial.println(time);
  Serial.println(scale.get_units(), 2); //scale.get_units() returns a float 
  Serial.println();
}
