#include <Wire.h>
#include <math.h>
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
bool dataSentSuccessfully = false;
int ident = 3;

// E8:9F:6D:1F:8C:C8
// uint8_t broadcastAddress[] = {0xE8, 0x9F, 0x6D, 0x31, 0x9C, 0x44};
uint8_t broadcastAddress[] = {0xE8, 0x9F, 0x6D, 0x1F, 0x8C, 0xC8};

typedef struct struct_message {
  float la;
  int concussbool;
  int identity;
  float batteryPercentage;
} struct_message;

struct_message myData;
esp_now_peer_info_t peerInfo;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  if (status == ESP_NOW_SEND_SUCCESS) {
    Serial.println("Delivery Success");
    dataSentSuccessfully = true;
  } else {
    Serial.println("Delivery Fail");
    dataSentSuccessfully = false;
  }
}

void setup(void) {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initialzing ESP-NOW");
    return;
  }
  esp_now_register_send_cb(OnDataSent);

  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }

  while (!Serial);
  Serial.println("ADXL375 Accelerometer Test\n");

  if (!accel.begin()) {
    Serial.println("Ooops, no ADXL375 detected ... Check your wiring!");
    while (1);
  }

  // with the data rate set to 800 Hz, the accelerometer will take readings every 1.25 milliseconds.
  //        the duration of a concussion is between 2-10 milliseconds.

  accel.setDataRate(ADXL343_DATARATE_800_HZ);
  accel.printSensorDetails();

  Serial.print("Data Rate: ");
  switch (accel.getDataRate()) {
    case ADXL343_DATARATE_3200_HZ: Serial.print("3200 "); break;
    case ADXL343_DATARATE_1600_HZ: Serial.print("1600 "); break;
    case ADXL343_DATARATE_800_HZ:  Serial.print("800 ");  break;
    case ADXL343_DATARATE_400_HZ:  Serial.print("400 ");  break;
    case ADXL343_DATARATE_200_HZ:  Serial.print("200 ");  break;
    case ADXL343_DATARATE_100_HZ:  Serial.print("100 ");  break;
    case ADXL343_DATARATE_50_HZ:   Serial.print("50 ");   break;
    case ADXL343_DATARATE_25_HZ:   Serial.print("25 ");   break;
    case ADXL343_DATARATE_12_5_HZ: Serial.print("12.5 "); break;
    case ADXL343_DATARATE_6_25HZ:  Serial.print("6.25 ");  break;
    case ADXL343_DATARATE_3_13_HZ: Serial.print("3.13 ");  break;
    case ADXL343_DATARATE_1_56_HZ: Serial.print("1.56 ");  break;
    case ADXL343_DATARATE_0_78_HZ: Serial.print("0.78 ");  break;
    case ADXL343_DATARATE_0_39_HZ: Serial.print("0.39 ");  break;
    case ADXL343_DATARATE_0_20_HZ: Serial.print("0.20 ");  break;
    case ADXL343_DATARATE_0_10_HZ: Serial.print("0.10 ");  break;
    default:                       Serial.print("???? ");  break;
  }
  Serial.println(" Hz");
  Serial.println("");
}

float instant_acceleration_magnitude() {
  bool measure_in_Gs = true;
  sensors_event_t event;
  accel.getEvent(&event);

  if (measure_in_Gs == true) {
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

// void calculate_momentary_threshold(float acceleration, float previous_acceleration, float initial_threshold) {
//   float duration = 0;
//   float momentary_acceleration = 0;

//   for (int i = 0; i < len; i++) {
//     float timestamp = millis();
//     float acceleration = acceleration;

//     if (acceleration >= previous_acceleration) {
//       duration += (i > 0) ? (timestamp - timestamps[i - 1]) : 0;
//       duration +=
//       momentary_acceleration = acceleration;
//     }
//     else {
//       momentary_acceleration = acceleration;
//       duration = 0;
//     }


//     float momentary_threshold;
//     if (momentary_acceleration > 0.2 * initial_threshold) {
//       momentary_threshold = initial_threshold * exp(-duration * 1.3 / momentary_acceleration);
//     }
//     else {
//       momentary_threshold = initial_threshold;
//     }

//     return momentary_threshold;
//   }
// }


// float tolerance_curve(float acceleration, float duration, float initialThreshold) {
//     // Define the initial threshold and the time constant for the logarithmic decrease
// 	float decay_rate = 100; //arbitrary
// 	float timeConstant = decay_rate / acceleration;
//     // Calculate the threshold using the formula: threshold = initialThreshold * exp(-duration/timeConstant)
//     float threshold = initialThreshold * exp(-duration/timeConstant);
//     // Return the maximum of the calculated threshold and the input acceleration
//     //return fmax(threshold, acceleration);
// 	//return fmin(threshold, acceleration);
// 	return threshold;
// }

// bool DiagnosticAlgorithm(float first_measurement, float initial_threshold, float tolerance_severity){

// 	float momentary_threshold = initial_threshold;

// 	// Simple case: measurement is less than severity of tolerance threshold, so don't bother testing
// 	if (first_measurement < tolerance_severity * momentary_threshold)
// 		return good_status;

// 	// Impact case: measurement warrants inspection using tolerance curve
// 	float start_time = millis(); //initial time from first measurement
// 	float current_time = millis();
//   float threshold = initial_threshold;
//   float new_measurement_acceleration;

// 	while (current_time - start_time <= 15.0){

// 		//float new_measurement_acceleration = perform_measurement;//TODO
// 		new_measurement_acceleration = myData.la;

// 		current_time = millis();

// 		if (new_measurement_acceleration < first_measurement) //acceleration decreased, so just measure once and be done with it
// 			return Status(new_measurement_acceleration, threshold);

// 		threshold = tolerance_curve(new_measurement_acceleration, current_time, initial_threshold);
// 	}
// 	return Status(new_measurement_acceleration, threshold);
// }

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

// void loop(void) {
//   float acceleration = instant_acceleration_magnitude();
//   // float threshold = calculate_momentary_threshold(acceleration, previous_acceleration_measurement, generic_threshold);

//float filtered_acceleration = 0;

float lowPassFilter(float raw_acceleration, float filtered_acceleration, float cutoff_frequency, float delta_time) {
  float RC = 1.0 / (2 * PI * cutoff_frequency);
  float alpha = delta_time / (RC + delta_time);
  return (alpha * raw_acceleration) + ((1 - alpha) * filtered_acceleration);
}

float generic_threshold = 50.0;

unsigned long window_start_time = millis();
float max_acceleration = 0;
float previous_acceleration_measurement = 0;
int max_concuss_status = good_status;

float concussed_acceleration;

void loop(void) {
  float acceleration = instant_acceleration_magnitude();

  // Apply low-pass filter
  float current_time = millis();
  static float prev_time = current_time;
  float delta_time = (current_time - prev_time) / 1000.0; // Convert to seconds
  static float filtered_acceleration = 0; // Declare it here as a static variable
  filtered_acceleration = lowPassFilter(acceleration, filtered_acceleration, 100, delta_time); // 100 Hz cutoff frequency
  prev_time = current_time;

  int concuss_status = Status(filtered_acceleration, generic_threshold);
  if (concuss_status > 0)
    concussed_acceleration = filtered_acceleration;

  previous_acceleration_measurement = filtered_acceleration;

  // Store the highest acceleration and corresponding concussion status
  if (concuss_status > max_concuss_status){
    max_concuss_status = concuss_status;
  }

  if (millis() - window_start_time >= 250) {
    // Transmit the highest acceleration and corresponding concussion status in the window
    myData.la = max(concussed_acceleration, filtered_acceleration);
    myData.concussbool = max_concuss_status;
    myData.identity = ident;
    myData.batteryPercentage = readBatteryPercentage();

//     // bool data_sent = false;
//     // while (!data_sent) {
//     //   // Send message via ESP-NOW
//     //   esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *)&myData, sizeof(myData));

//     //   if (result == ESP_OK) {
//     //     Serial.println("Sending confirmed");
//     //     data_sent = true;
//     //   } else {
//     //     Serial.println("Sending Error");
//     //   }

    // Send message via ESP-NOW
    esp_err_t result = esp_now_send(broadcastAddress, (uint8_t *)&myData, sizeof(myData));

    if (result == ESP_OK) {
      Serial.println("Sending confirmed");
    } else {
      Serial.println("Sending Error");
    }

    // Display the results
    Serial.print(myData.identity);
    Serial.print(myData.la);
    Serial.println(myData.concussbool);

    // Reset the highest acceleration and concussion status for the next window
    concussed_acceleration = 0;
    max_concuss_status = good_status;
    window_start_time = millis();
  }
}