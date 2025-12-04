<a id='42a1c667-ebfb-4a62-8e17-23933858b506'></a>

12/4/25, 2:51 PM

<a id='8268baae-a860-46a1-a5d2-a747337e36e4'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='10afe9b6-f4ce-4c88-983d-1d46980af104'></a>

ARDUINODOCS

Search on Docs /

<a id='aed4fee2-85e5-4061-96c3-98403b86faa9'></a>

← Go Back

## Hardware

<a id='bd9a884d-2e46-40a9-98b7-63ce728b1a2a'></a>

MKR ENV Shield

Tutorials

Reading Data From the
MKR ENV Shield

<a id='b9ffe4e0-2ff3-4310-aee7-4a575f54187a'></a>

Home / Hardware / MKR ENV Shield / Reading
Data From the MKR ENV Shield

<a id='b91b466b-0d12-4ac4-a84f-2cb6c72fa976'></a>

# Reading Data From the MKR ENV Shield

Learn how to access the different sensors, such as temperature, humidity & pressure.

---

Author: Karl Söderby
Last revision: 17/07/2024

<a id='ae5695ce-6df4-423e-afc5-dbedfa20c6ff'></a>

# Introduction

In this tutorial, we will go through the requirements of getting started with the MKR ENV Shield, a shield designed to capture environmental data from your surroundings. The shield can only be used with a MKR family board, where it can be easily mounted on top.

<a id='2a03fc02-8de6-413d-819d-f8d082d3ad3b'></a>

The MKR ENV Shield is a great option for
weather projects, where we can read
temperature, humidity, light intensity &
atmospheric pressure. Additionally, it also
comes equipped with an SD card holder, that
can be used to store the data captured from
the sensors.

<a id='18c28858-ca5b-423e-808a-6a72bc3882ed'></a>

*Note: The older MKR ENV Shield version (v1) comes with a UV sensor that can capture UVA & UVB wavelengths. The newer versions (v2 and up) does not include this sensor. This can be seen in the silk on the shield, where newer versions does not have a sun symbol marked on top.*

<a id='2298cd2a-5d2c-42fe-85df-c550acb62b03'></a>

# Goals

The goals of this project are:

* Learn how to use the **Arduino_MKRENV** library.
* Capture data from all the sensors on the shield.
* Print out the data in the Serial Monitor.

<a id='a2e3c9af-3efe-485a-8a08-8064a06f6bb8'></a>

ON THIS PAGE

<a id='176913b5-0c40-4cfb-8bb1-41a895b20d85'></a>

## Introduction
- Goals
- Hardware & Software Needed
- The Different Sensors on the Shield
  - HTS221 Temperature & Humidity Sensor
  - LPS22HB Atmospheric Pressure Sensor
  - TEMT6000 Light Sensor
  - VEML6075 (Older Versions Only)
- Circuit
- Programming the Board
- Testing It Out
  - Troubleshoot
- Conclusion

<a id='290168f5-e466-4954-93dd-e594117a309f'></a>

Hardware & Software

<a id='d40eed43-dd50-4dad-be2e-e6e91ba4dfd4'></a>

Needed
file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='58311146-efe6-4d6f-9e6d-702d4ba5b8a0'></a>

Help

<a id='60bde594-4ea6-4f5b-9286-16006385a215'></a>

1/8

<!-- PAGE BREAK -->

<a id='8d75550c-22cc-4d22-85d8-3e9d2c0b2b58'></a>

12/4/25, 2:51 PM

<a id='f6b927c5-85c4-4690-8cc3-a4d1857ebba9'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='bc2a2b91-70e9-4460-a83a-5cc66a1a72ac'></a>

ARDUINODOCS

<a id='4a484926-ada1-4279-9c85-40722cb9db30'></a>

Arduino IDE (online or offline).
Arduino_MKRENV library installed.
MKR ENV Shield (link to store)
Arduino MKR family board (link to
store)

<a id='717f2559-4864-4028-a96f-ab6f71d333d1'></a>

# The Different Sensors on the Shield

Before we test out the MKR ENV Shield, let's take a look at the different sensors that come with it. In total, there are three sensors: the LPS22HB (atmospheric pressure), HTS221 (temperature & humidity) and TEMT6000 (light intensity).

<a id='b5c6d2c0-6c2b-439f-b607-997b13d98f5f'></a>

HTS221 Temperature & Humidity
Sensor

<a id='89d494bf-1138-4cdf-9839-3dd9acdd3aad'></a>

<::An image showing a blue circuit board (possibly an Arduino-compatible board) with a small, rectangular component highlighted in blue. A dark grey label box with white text "HTS221" is positioned above the highlighted component, indicating it as the HTS221 sensor.
: figure::>
The HTS221 sensor.

<a id='906aaa48-671c-4699-8be4-5fc15ab9c6d9'></a>

This sensor's range and accuracy make it
suitable for many interesting experimental
settings. There are two different functions
that we can call upon:

<a id='bdc01f26-b9c5-4b7a-b969-ae8c68cbcca5'></a>

`readTemperature()`
and
`readHumidity()`
. The return values are in
**Celsius**
and relative humidity, but we can also use the
command
`readTemperature(FAHRENHEIT)`
if we want to get our values in
**Fahrenheit**

<a id='fe3d9fe2-e7f0-440e-a560-9f871321655f'></a>

The temperature range goes between
-40 and +120 (C) and the accuracy is 
0.5 C in the range of 15 to +40 C.
The humidity range goes between 
3.5% rH (relative humidity), at 20 (C) to
+80% rH. The rH sensitivity is 0.004%
rH.

<a id='a5a7f638-969b-4999-97c8-da91ed9d4413'></a>

You can find more information about this file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='cffeef90-c353-43ba-aca2-d7a073e67b31'></a>

2/8

<!-- PAGE BREAK -->

<a id='3bbdc50f-6da1-4779-9b31-ac256a4246ec'></a>

12/4/25, 2:51 PM

<a id='3b13d1e4-23d1-4f9f-82fb-52fea7f62b74'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='e9adeaeb-30e5-4bf4-872c-9694d03e5a57'></a>

ARDUINODOCS

<a id='39735172-607b-4f9a-8d6e-14a69bb20a8b'></a>

LPS22HB Atmospheric Pressure
Sensor

<a id='4112b6ae-f4ac-4e01-bad5-1731dbe2cbce'></a>

<::An image shows a circuit board with a small, dark blue rectangular component labeled "LPS22HB" in a callout box. The circuit board has various pins and other components. Below the image, the caption reads: The LPS22HB sensor.
: figure::>

<a id='3221962b-c812-4161-9cad-ee2438ea91cf'></a>

The atmospheric pressure can be read using
the command

<a id='e85bd8f8-d26c-4306-97b9-efa0f8388bb1'></a>

`readPressure()`
, which can take either no parameters or one
of the following three, which will determine
the units in which pressure will be expressed:

<a id='ee310ea9-8e86-4c6d-a61c-24b829c0f37a'></a>

PSI - the sensor returns data in pounds
per square inch.

<a id='3f046e78-be17-455f-9125-ab676a4e092a'></a>

MILLIBAR - the sensor returns data in millibars. Millibars are exactly the same as hectopascal, a unit that is more commonly used by meteorologists for weather reports.

<a id='05bd680c-4fff-49cb-a92a-827c767890db'></a>

KILOPASCAL - the sensor returns data in kilopascals - this is the default option.

<a id='e0d82c13-1505-4055-9611-6f784d2d930e'></a>

Take a look at the table below. Here, we can
see that hectopascal and millibars are exactly
the same, and that PSI is entirely different, as
it follows the imperial unit system.

<a id='7aae439d-835a-4206-bf79-ced36e763f5c'></a>

<table id="2-1">
<tr><td id="2-2">Kilopascal (kPa)</td><td id="2-3">Hectopascal (hPa)</td><td id="2-4">Millibar</td><td id="2-5">PSI</td></tr>
<tr><td id="2-6">1</td><td id="2-7">10</td><td id="2-8">10</td><td id="2-9">0.145038</td></tr>
<tr><td id="2-a">10</td><td id="2-b">100</td><td id="2-c">100</td><td id="2-d">1.45038</td></tr>
<tr><td id="2-e">25</td><td id="2-f">250</td><td id="2-g">250</td><td id="2-h">3.62594</td></tr>
</table>

<a id='6830e9e9-bfa6-4b94-b2f7-986e8d0e5401'></a>

The barometric pressure sensor functions as a digital output barometer; it processes the data collected from the movement of a suspended silicon membrane. The change of pressure on the membrane affects a Wheatstone bridge, where piezo resistances are measured with an analog-to-digital converter and processed digitally.

<a id='1b330470-1518-4f1f-ad63-275d846fedc3'></a>

The sensor's range and accuracy make it suitable for a wide range of scientific experiments. The pressure range measures between 260 and 1260 hPa, with an accuracy

<a id='074ed96a-c3bb-4fcd-8a85-ae1da7a9dea3'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='0d9b2a61-2cf5-433a-85ee-671646925184'></a>

3/8

<!-- PAGE BREAK -->

<a id='fce34620-3587-4c73-a33c-653e3fc33c34'></a>

12/4/25, 2:51 PM

<a id='5334e292-6edc-4465-bd66-6042537dcdde'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='29ff40b9-f0e6-4f26-8bc8-1ca846afb9ec'></a>

ARDUINODOCS

<a id='67b7ac35-8450-491d-aa71-1a0e87805a10'></a>

operate with a more constrained pressure
range between the extended temperature
range from -40 C to +85 C.

<a id='8e5610f3-4349-44d0-a8b1-7da95242e0e0'></a>

You can find more information about this sensor by reading it's datasheet.

<a id='5ed5c21e-83a4-4e46-aaf7-25d845a55296'></a>

TEMT6000 Light Sensor

<a id='1d87d72e-f2f9-40c5-a6fd-0f0cf6bc4758'></a>

<::image: An electronic development board (likely an Arduino Nano Every or similar) with various components, pins, and a micro-SD card slot. A specific component on the board, a light sensor, is highlighted with a blue glow and has a label "TEMT6000" pointing to it. The TEMT6000 sensor.::>

<a id='c4c4530a-d1e2-4549-9026-ce715c3117fa'></a>

The TEMT6000 sensor is a phototransistor, a component that will allow electrons to flow differently based on the amount of light shining on it. It has been calculated to be adapted to the human eye sensitivity. In other words, this sensor is telling you how intense light is for your eyes.

<a id='9da9d2bf-6172-4052-a920-147fc5e1fa36'></a>

The sensor's range and accuracy makes is suitable for a lot of scientific experiments. The sensor's opening angle is 60, and while it peaks up at 570 nm, it is detecting light in the range from 440 nm to 800 nm, in the temperature range from -40 C to +100 C.

<a id='a8ac93e1-1aae-4287-8bc6-bc98cb368df2'></a>

Using the command
`readIlluminance()`
will by default return a value measured in
`LUX`
. This unit represents one lumen per square meter. Unlike a measurement of Watts per square meter, which weights the power of signals in different frequencies of the spectrum differently, the lumens are calculated by looking at the mathematical response of the human eye to different wavelengths. In that way, LUX comes to be a measurement of how intense the light is for the human eye.

<a id='b8efab35-12e1-404a-9f9e-07a76bfde726'></a>

You can find more information about this sensor by reading it's datasheet.

<a id='cf67301b-ac08-412b-9347-8bd89ff4bc88'></a>

VEML6075 (Older Versions Only)

<a id='a87794c0-cfbb-469d-8775-6042fe2d9a1f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='b05ba20c-56cf-4555-80ab-fab225df30e1'></a>

4/8

<!-- PAGE BREAK -->

<a id='30b42970-56d7-496f-a790-353f633866db'></a>

12/4/25, 2:51 PM

<a id='a82064a0-a4de-4a82-8c5e-a5e3bececc28'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='daac1032-7562-4861-b8ad-b015f490d57a'></a>

ARDUINODOCS

<a id='058f9a28-2561-48a9-8a0c-bfba971d4957'></a>

<::An image of a circuit board (likely a development board or shield) with various electronic components. A label points to a specific component on the board, indicating "VEML6075 (OLDER VERSIONS)". The board has multiple rows of pin headers along its long edges, and a smaller header or connector on one short edge. There's also what appears to be an SD card slot on the left side. The overall color scheme is blue for the PCB and grey for the background.: figure::>
The VEML6075 sensor.

<a id='c80c9221-c17c-40b2-9f10-fa76e656a939'></a>

The older versions of the MKR ENV Shields also has a UV sensor that can detect UVA and UVB wavelengths. The sensors can be read through the

`readUVA()`

and

`readUVB()`

commands. We can also use

`readUVIndex()`
to calculate the UV index.

The UV sensor's range and accuracy makes is suitable for a lot of scientific experiments. The temperature range of operation goes from -40 °C to +85 °C.

You can find more information about this sensor by reading it's [datasheet](https://example.com/datasheet).

<a id='488a9ce3-c738-4e54-a8a2-84de87cdb21a'></a>

# Circuit

The circuit in this tutorial is very simple. Just
attach the MKR ENV Shield on top of a MKR
family board (shown below is the MKR WiFi
1010 board).

<a id='c07e40b1-fd9f-4a06-9ce7-1c6addad3782'></a>

<::logo: [MKR ENV Shield / MKR Family Board] MKR ENV SHIELD, MKR FAMILY BOARD. The logo features two circuit boards, one labeled "MKR ENV SHIELD" and the other "MKR FAMILY BOARD," with arrows indicating a connection or placement from the shield to the board.::>

<a id='0ddb8f13-3942-452f-adf0-16a25c314bb6'></a>

# Programming the Board

We will now get to the programming part of
this tutorial.

1. First, let's make sure we have the drivers
installed for the board we are using. If we are
using the Cloud Editor, we do not need to
install anything. If we are using an offline
editor. we need to install it manually. This

<a id='ba8bfa56-2c95-4c99-a4ea-2b8f1a08aa81'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='37fdee61-6591-4535-b947-0c168e99c55a'></a>

5/8

<!-- PAGE BREAK -->

<a id='664d646c-672f-4c78-bacf-60af8e9c0c6c'></a>

12/4/25, 2:51 PM

<a id='fdec619b-d5dd-4574-9d97-56714b8c0320'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='22709aed-1af0-4176-b3ef-2c67f59f98b4'></a>

ARDUINODOCS

<a id='9410bd0c-a306-4a1d-82e6-0689cb7665fc'></a>

the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it.

2. Now, we need to install the libraries needed. If we are using the Cloud Editor, there is no need to install anything. If we are using an offline editor, simply go to **Tools** > **Manage libraries**.., and search for **Arduino_MKRENV** and install it.

<a id='dc31e536-43ea-48f5-9005-0ef143b02dbb'></a>

3. We can now take a look at some of the core functions of this sketch:
`ENV.begin()` - initializes the library.
`ENV.readTemperature()` - returns temperature.
`ENV.readHumidity()` - returns relative humidity.
`ENV.readPressure()` - returns atmospheric pressure.
`ENV.readIlluminance()` - returns LUX.
`ENV.readUVA()` - returns UVA (only for older versions).
`ENV.readUVB()` - returns UVB (only for older versions).
`ENV.readUVIndex()` - calculates UV index (only for older versions).

<a id='49a54d30-c309-4471-99a6-7f8992235ba6'></a>

The sketch can be found in the snippet
below, or in the **Arduino_MKRENV** library, in
**File > Examples > Arduino_MKRENV >
ReadSensors**. Then, upload the code to the
board.

<a id='f72db4db-deb3-49cb-bb1f-1d2f76392c3e'></a>

Note: If you are using imperial units, e.g.
Fahrenheit, there is a sketch called
ReadSensorsImperial that is better suited.

<a id='22ab5578-f640-42be-b582-de35b2c88117'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='5d37a173-60fe-4f90-b202-2fec83a7dd72'></a>

6/8

<!-- PAGE BREAK -->

<a id='836a95bd-baae-45a2-ae93-69109d443497'></a>

12/4/25, 2:51 PM

<a id='794744d9-05a8-40e9-94d9-555d35b2be9e'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='e9083aa1-ff3c-4512-8c69-c205f8bf1da9'></a>

ARDUINODOCS

<a id='27f77521-6e2d-4142-aa32-c81bf4b77a83'></a>

```cpp
1 #include <Arduino_MKRENV.h>
2 
3 void setup() {
4   Serial.begin(9600);
5   while (!Serial);
6 
7   if (!ENV.begin()) {
8     Serial.println("Failed to initialize ENV sensor!");
9     while (1);
10   }
11 }
12 
13 void loop() {
14   // read all the sensor value
15   float temperature = ENV.readTemperature();
16   float humidity    = ENV.readHumidity();
17   float pressure    = ENV.readPressure();
18   float illuminance = ENV.readIlluminance();
19   float uva         = ENV.readUVA();
20   float uvb         = ENV.readUVB();
21   float uvIndex     = ENV.readUVIndex();
22 
23   // print each of the sensor
24   Serial.print("Temperature = ");
25   Serial.print(temperature);
26   Serial.println(" °C");
27 
28   Serial.print("Humidity    = ");
29   Serial.print(humidity);
```

<a id='419760e7-0063-456c-a68f-1282daa147d5'></a>

> Note: If you are using a newer version of
> the MKR ENV shield, you will not be able to
> use the
> `readUVA()`, `readUVB()` and
> `readUVindex()` commands.

<a id='46e43495-55d6-4c14-a879-a6898ede03e1'></a>

# Testing It Out

The code that we have now uploaded is very simple. First, we do a reading of all the sensors, then we simply print them in the Serial Monitor, with an interval of one second.

<a id='1eeb1e05-6db4-4dd0-95e5-9ed8f709ab49'></a>

We can test that it is working, by opening the
Serial Monitor. If everything is working
properly, we should now see the values
being printed in the Serial Monitor.

<a id='cfb5e9c5-b6a6-4343-a244-6fb172361284'></a>

<::Arduino IDE window and Serial Monitor window: figure::>
<::Arduino IDE window titled "Arduino.ino - Arduino 1.8.19">
Menu: File, Edit, Sketch, Tools, Help
Toolbar icons: Verify, Upload, New, Open, Save, Serial Monitor
Code editor content:
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  float hif = dht.computeHeatIndex(f, h);
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print(" %\t");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.print(" *C ");
  Serial.print(f);
  Serial.print(" *F\t");
  Serial.print("Heat index: ");
  Serial.print(hic);
  Serial.print(" *C ");
  Serial.print(hif);
  Serial.println(" *F");
  delay(2000);
}
```
<::Serial Monitor window titled "Serial Monitor">
Output content:
```
Temperature = 25.17 %
Humidity = 75.99 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24

Temperature = 25.43 %
Humidity = 76.24 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24

Temperature = 25.64 %
Humidity = 76.45 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24

Temperature = 25.93 %
Humidity = 76.71 %
Distance = 277.42 cm
Heat Index = -1.00
UV Index = 0.24
```

<a id='a32b2671-8155-4bc0-a845-9acdaea1ba83'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='18f40449-da01-46f5-bb94-aead746248ef'></a>

7/8

<!-- PAGE BREAK -->

<a id='1837ec62-e038-4435-be33-e689c8a86b92'></a>

12/4/25, 2:51 PM

<a id='4aee103d-74e1-4369-856f-0822cfa6ea97'></a>

Reading Data From the MKR ENV Shield | Arduino Documentation

<a id='08fd9324-2c7c-4cec-ba99-cda4d737521f'></a>

ARDUINODOCS

<a id='b139b016-43f8-4fe4-ab91-2fdf22d83980'></a>

## Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- We have not mounted the MKR ENV Shield on top of the board.
- We have not installed the **Arduino_MKRENV** library.

<a id='1632e5b3-81bb-4017-9202-67d2580a76db'></a>

## Conclusion

In this tutorial, we have learned how to access the different sensors on the MKR ENV Shield, and print them in the Serial Monitor. Now with some basic knowledge on how the shield works, you can start creating your own projects, such as mini weather station, or an indoor temperature control device.

<a id='2f4e9d53-8c2f-4d44-b4ea-e95fb9e31dd8'></a>

Feel free to explore the Arduino_MKRENV
library further, and try out some of the many
cool functions.

<a id='1617c195-761d-41f9-aee9-543f4608bf29'></a>

| Suggest changes | Need support? | License |
|---|---|---|
| The content on docs.arduino.cc is facilitated through a public GitHub repository. If you see anything wrong, you can edit this page here. | Help Center<br>Ask the Arduino Forum<br>Discover Arduino<br>Discord | The Arduino documentation is licensed under the Creative Commons Attribution-Share Alike 4.0 license. |

<a id='dae16e49-57f5-40f9-991a-4145338347ec'></a>

Was this article helpful?

---

option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='90b710d2-e74e-4244-84c4-dc0472d74b19'></a>

&copy; 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='768d24d6-cc00-49a9-abac-fef1cdd7022b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-userManual.html

<a id='dd00833e-e0e3-4ddc-8bf0-7afccf526075'></a>

8/8