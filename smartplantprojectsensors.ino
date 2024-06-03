//Library for sending http requests
#include "HttpClient.h"

//Light sensor library
#include "BH1750.h"

//Temperature and humidity sensor library
#include <Adafruit_DHT_Particle.h>

//Temperature and humidity sensor define pin and sensor type
#define DHTPIN D5
#define DHTTYPE DHT11		

//Declaring temperature and humidity sensor
DHT tempHumidSensor(DHTPIN, DHTTYPE);

//Declaring light sensor
BH1750 lightSensor(0x23, Wire);

//Variables to store sensed values
float lightLevel;
float tempLevel;
float humidLevel;
int moistureLevel;
int numReadings;

//Setting up http 
HttpClient http;
http_header_t headers[] = {
    { "Content-Type", "application/json" },
    { NULL, NULL }
};

http_request_t request;
http_response_t response;

void setup()
{
    //Light sensor initialise
    lightSensor.begin();
    lightSensor.set_sensor_mode(BH1750::forced_mode_high_res2);
    
    //Temperature and humidity sensor initialise
    pinMode(D5, OUTPUT);
	tempHumidSensor.begin();
	
	numReadings = 10;
	
	Serial.begin(9600);
}

void loop()
{
    lightLevel = getLightLevel();
    tempLevel = validTempValue();
    humidLevel = validHumidValue();
    moistureLevel = validMoistureValue();
    
    Serial.print(lightLevel);
    Serial.print(", ");
    Serial.print(tempLevel);
    Serial.print(", ");
    Serial.print(humidLevel);
    Serial.print(", ");
    Serial.print(moistureLevel);
    
    sendSensorData(lightLevel, tempLevel, humidLevel, moistureLevel);
    
    Serial.print("Status code: ");
    Serial.println(response.status);
    Serial.print("Response: ");
    Serial.println(response.body);
    
    delay(5000);
}

//Function to convert soil moisture reading to a %
long map(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void sendSensorData(float light, float temp, float humid, int moisture)
{
    request.hostname = "192.9.200.32";
    request.port = 5000;
    request.path = "/sensor-data";
    
    char payload[256];
    snprintf(payload, sizeof(payload), "{\"light\": %.2f, \"temp\": %.2f, \"humid\": %f, \"moisture\": %d}", light, temp, humid, moisture);
    
    request.body = payload;
    
    http.post(request, response, headers);
}

float getLightLevel()
{
    lightSensor.make_forced_measurement();
    
    return lightSensor.get_light_level();
}

float getTempLevel()
{
    float t = tempHumidSensor.getTempCelcius();
    
    if (isnan(t))
    {
        t = 0;
    }
    
    return t;
}

float getHumidLevel()
{
    return tempHumidSensor.getHumidity();
}

int getMoistureLevel()
{
    int sensorValue = analogRead(A3);
    
    int percentage = map(sensorValue, 0, 2610, 0, 100);
    
    return percentage;
}

float validTempValue()
{
    float temp = 0;
    
    temp = getTempLevel();
    
    while (temp == 0)
    {
        temp = getTempLevel();
    }
    
    return temp;
}

float validHumidValue()
{
    float humid = 0;
    
    humid = getHumidLevel();
    
    while (humid > 100)
    {
        humid = getHumidLevel();
    }
    
    return humid;
}

int validMoistureValue()
{
    int moisture = 0;
    
    moisture = getMoistureLevel();
    
    while (moisture > 100)
    {
        moisture = getMoistureLevel();
    }
    
    return moisture;
}
