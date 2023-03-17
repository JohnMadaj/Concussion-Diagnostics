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
// Received Signal Strength Indicatior
//int rssi = WiFi.RSSI();

uint8_t broadcastAddress[] = {0xE8, 0x31, 0xCD, 0x63, 0x4E, 0x58};

// Define a data structure
typedef struct struct_message{
  float la;
  int concussbool;
  int identity;
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

  /* Display some basic information on this sensor */
  accel.printSensorDetails();
  displayDataRate();
  Serial.println("");
}

bool DiagnosticAlgorithm(float la, float la_threshold)
{
    if (la > la_threshold)
        return 1
    return 0
}
// TODO IMPLEMENT
// Function to calculate the acceleration threshold based on duration
float calculateThreshold(float acceleration, float duration, float initialThreshold) {
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


void loop(void)
{
  /* Get a new sensor event */
  sensors_event_t event;
  accel.getEvent(&event);

  myData.la = sqrt((event.acceleration.x*event.acceleration.x)+(event.acceleration.y*event.acceleration.y)+(event.acceleration.z*event.acceleration.z));

  myData.concussbool = DiagnosticAlgorithm(myData.la, 80);


  myData.identity = ident;
  //myData.issr = rssi;

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

  delay(100);
}