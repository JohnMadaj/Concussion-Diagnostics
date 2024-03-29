#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL375.h>
#include <esp_now.h>
#include <WiFi.h>

#define ADXL375_SCK 13
#define ADXL375_MISO 12
#define ADXL375_MOSI 11
#define ADXL375_CS 10

Adafruit_ADXL375 accel = Adafruit_ADXL375(12345);

int concussed_status = 1;
int good_status = 0;
float tolerance_severity = 0.5; //g //arbitrary

void displayDataRate(void)
{
  Serial.print  ("Data Rate:    ");

  switch(accel.getDataRate())
  {
    case ADXL343_DATARATE_3200_HZ:
      Serial.print  ("3200 ");
      break;
    case ADXL343_DATARATE_1600_HZ:
      Serial.print  ("1600 ");
      break;
    case ADXL343_DATARATE_800_HZ:
      Serial.print  ("800 ");
      break;
    case ADXL343_DATARATE_400_HZ:
      Serial.print  ("400 ");
      break;
    case ADXL343_DATARATE_200_HZ:
      Serial.print  ("200 ");
      break;
    case ADXL343_DATARATE_100_HZ:
      Serial.print  ("100 ");
      break;
    case ADXL343_DATARATE_50_HZ:
      Serial.print  ("50 ");
      break;
    case ADXL343_DATARATE_25_HZ:
      Serial.print  ("25 ");
      break;
    case ADXL343_DATARATE_12_5_HZ:
      Serial.print  ("12.5 ");
      break;
    case ADXL343_DATARATE_6_25HZ:
      Serial.print  ("6.25 ");
      break;
    case ADXL343_DATARATE_3_13_HZ:
      Serial.print  ("3.13 ");
      break;
    case ADXL343_DATARATE_1_56_HZ:
      Serial.print  ("1.56 ");
      break;
    case ADXL343_DATARATE_0_78_HZ:
      Serial.print  ("0.78 ");
      break;
    case ADXL343_DATARATE_0_39_HZ:
      Serial.print  ("0.39 ");
      break;
    case ADXL343_DATARATE_0_20_HZ:
      Serial.print  ("0.20 ");
      break;
    case ADXL343_DATARATE_0_10_HZ:
      Serial.print  ("0.10 ");
      break;
    default:
      Serial.print  ("???? ");
      break;
  }
  Serial.println(" Hz");
}

// Integer for identification (unique for each transmitter)
int ident = 3;

//E8:9F:6D:1F:8C:C8
//uint8_t broadcastAddress[] = {0x94, 0xE6, 0x86, 0x49, 0x01, 0xE0};
uint8_t broadcastAddress[] = {0xE8, 0x9F, 0x6D, 0x1F, 0x8C, 0xC8};

// Define a data structure
typedef struct struct_message{
  float la;
  int concussbool;
  int identity;
  float batteryPercentage; 
  //int issr;
} struct_message;

// create a structured object
struct_message myData;

// peer info
esp_now_peer_info_t peerInfo;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status){
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status==ESP_NOW_SEND_SUCCESS ? "Delivery Success":"Delivery Fail");
}


void setup(void)
{
  Serial.begin(115200);

  // initialize esp-now
  WiFi.mode(WIFI_STA);

  //initialize ESP-NOW
  if (esp_now_init() != ESP_OK){
    Serial.println("Error initialzing ESP-NOW");
    return;
  }
  // Register the send callback
  esp_now_register_send_cb(OnDataSent);

  // Register peer
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  // Add peer
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }

  while (!Serial);
  Serial.println("ADXL375 Accelerometer Test"); Serial.println("");

  /* Initialise the sensor */
  if(!accel.begin())
  {
    /* There was a problem detecting the ADXL375 ... check your connections */
    Serial.println("Ooops, no ADXL375 detected ... Check your wiring!");
    while(1);
  }

  // Range is fixed at +-200g
  accel.setDataRate(ADXL343_DATARATE_3200_HZ);
  /* Display some basic information on this sensor */
  accel.printSensorDetails();
  displayDataRate();
  Serial.println("");
}

// concussed_status = 1;
// good_status = 0;
// tolerance_severity = 0.5; //g //arbitrary

float instant_acceleration_magnitude(){
  bool measure_in_Gs = true;

	/* Get a new sensor event */
  sensors_event_t event;
  accel.getEvent(&event);
  
  if (measure_in_Gs == true){
	event.acceleration.x /= 9.8;
	event.acceleration.y /= 9.8;
	event.acceleration.z /= 9.8;
  }
  return sqrt((event.acceleration.x*event.acceleration.x)+(event.acceleration.y*event.acceleration.y)+(event.acceleration.z*event.acceleration.z));
}

bool Status(float la, float la_threshold)
{
    if (la > la_threshold)
        return concussed_status;
    return good_status;
}
 
float tolerance_curve(float acceleration, float duration, float initialThreshold) {
    // Define the initial threshold and the time constant for the logarithmic decrease
	float decay_rate = 100; //arbitrary
	float timeConstant = decay_rate / acceleration;
    // Calculate the threshold using the formula: threshold = initialThreshold * exp(-duration/timeConstant)
    float threshold = initialThreshold * exp(-duration/timeConstant);
    // Return the maximum of the calculated threshold and the input acceleration
    //return fmax(threshold, acceleration);
	//return fmin(threshold, acceleration);
	return threshold;
}

bool DiagnosticAlgorithm(float first_measurement, float initial_threshold, float tolerance_severity){
	
	float momentary_threshold = initial_threshold;
	
	// Simple case: measurement is less than severity of tolerance threshold, so don't bother testing
	if (first_measurement < tolerance_severity * momentary_threshold)
		return good_status;
	
	// Impact case: measurement warrants inspection using tolerance curve
	float start_time = millis(); //initial time from first measurement
	float current_time = millis();
  float threshold = initial_threshold;
  float new_measurement_acceleration;

	while (current_time - start_time <= 15.0){
		
		//float new_measurement_acceleration = perform_measurement;//TODO
		new_measurement_acceleration = myData.la;
		
		current_time = millis();
		
		if (new_measurement_acceleration < first_measurement) //acceleration decreased, so just measure once and be done with it
			return Status(new_measurement_acceleration, threshold);
		
		threshold = tolerance_curve(new_measurement_acceleration, current_time, initial_threshold);
	}
	return Status(new_measurement_acceleration, threshold);
}

float readBatteryPercentage() {
  const int batteryPin = A13;
  const float voltageDivider = 2.0; // Assuming a 2:1 voltage divider (2x 100k resistors)
  const int adcResolution = 4095;
  const float Vref = 3.3;

  const float Vbat_min = 3.0;
  const float Vbat_max = 4.2;

  int rawADC = analogRead(batteryPin);
  float voltage = (rawADC * Vref / adcResolution) * voltageDivider;

  float batteryPercentage = (voltage - Vbat_min) / (Vbat_max - Vbat_min) * 100;
  batteryPercentage = constrain(batteryPercentage, 0, 100); // Limit the percentage to the 0-100 range

  return batteryPercentage;
}

float generic_threshold = 50.0;
//cd 
void loop(void)
{
  myData.la = instant_acceleration_magnitude();
	
  myData.concussbool = DiagnosticAlgorithm(myData.la, generic_threshold, tolerance_severity);

  myData.identity = ident;
  myData.batteryPercentage = readBatteryPercentage();

  // Send message via ESP-NOW
  esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));

  if (result == ESP_OK){
    Serial.println("Sending confirmed");
  }
  else {
    Serial.println("Sending Error");
  }

  /* Display the results (acceleration is measured in m/s^2) */
 // Serial.print(myData.issr);
  Serial.print(myData.identity);
  Serial.print(myData.la);
  Serial.println(myData.concussbool);

  delay(250);
}