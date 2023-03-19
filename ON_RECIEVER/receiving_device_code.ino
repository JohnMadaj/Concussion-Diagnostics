
/*
 * ESP-NOW Demo - Recieve
 * Reads data from Initiator
 */

// Include libraries
#include <esp_now.h>
#include <WiFi.h>

// Define a data structure
typedef struct struct_message{
  float la;
  int concussbool;
  int identity;
  float batteryPercentage;
} struct_message;

// Create a structured object
struct_message myData;

// Callback function executed when data is recieved
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len){
  memcpy(&myData, incomingData, sizeof(myData));

  Serial.print(myData.identity);
  Serial.print(": ");
  Serial.print(myData.la);
  Serial.print(": ");
  Serial.println(myData.concussbool);
  Serial.println("");
  // Serial.print(": ");
  // Serial.println(myData.batteryPercentage);
  
}

void setup() {
  // Set up Serial Monitor
  Serial.begin(115200);

  // Set up ESP32 as a wifi station
  WiFi.mode(WIFI_STA);

  //Initialize ESP-NOW
  if (esp_now_init() != ESP_OK) {
    Serial.println("Error Initializing ESP-NOW");
    return;
  }
  // Register callback function
  esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
  // put your main code here, to run repeatedly:

}

