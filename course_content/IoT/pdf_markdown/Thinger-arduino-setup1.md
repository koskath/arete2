<a id='f869e6ce-ef1b-4ee9-bbe3-2bbbbaf7b74e'></a>

<::logo: thinger.io
thinger.io
The logo features a minimalist black text "thinger.io" with a small square outline at the end, preceded by a three-line hamburger menu icon.::>

<a id='b115df92-1822-48b7-8856-c245c0eb007e'></a>

<::A magnifying glass icon within a rounded square button, centered on a white background.
: figure::>

<a id='9139cb41-92c8-4e6b-a2d2-c264002048a0'></a>

SDK SETUP

Arduino IDE

<a id='1a633e6a-dd5a-401a-8180-0bf253256145'></a>

GitHub icon Edit v

<a id='f288fb42-2d80-4ec4-8b7c-1c27ee9190f6'></a>

Arduino is widely recognized as the best framework for learning, prototyping, and even
product development. Its simplicity and the robust community of developers
continuously enhancing its capabilities make it an excellent choice.

<a id='8b5ce253-a748-4cab-946a-4bb5f93bc987'></a>

At Thinger.io, we have developed a Software Client to easily connect Arduino-based devices. This client is compatible with a wide variety of hardware and is available for Windows, macOS, and Linux distributions. It is possible to download it for free from the official Arduino website л.

<a id='8016736b-06e6-4a9b-8aae-fbf850cd27cf'></a>

The following sections will provide guidance on the installation and preparation of the
Arduino IDE to work with Thinger.io client libraries.

<a id='6cb02c97-a2ab-4975-8b44-8a3f381b5ddb'></a>

sketch_jun6a | Arduino IDE 2.3.2

✓ → ▷ ϟ Arduino UNO R4 WiFi ▾

sketch_jun6a.ino

```c
1 void setup() {
2 // put your setup code here, to run once:
3 
4 }
5 
6 void loop() {
7 // put your main code here, to run repeatedly:
8 
9 }
10 
```

indexing: 61/67 Ln 1, Col 1 Arduino UNO R4 WiFi on /dev/cu.usbmodemF412FA765E202 No Notifications

<a id='bd7a96ef-a465-428f-b2f1-98902fc23e9a'></a>

Arduino IDE

<a id='5e9a5948-9ede-433f-b6e9-5f66c3144922'></a>

1

<!-- PAGE BREAK -->

<a id='06f61ceb-d8f4-4572-9438-77fc6b174027'></a>

## Installing the Arduino IDE

To use Thinger.io with Arduino, a modern version of the Arduino IDE that supports the Library Manager and other advanced features is needed. Version 1.6.3 or later should be installed. If a compatible version is already installed, this step can be skipped.

<a id='5854cd7d-8154-4537-8c19-d272bbf31862'></a>

1. **Download the Arduino IDE:** Visit the official Arduino download page > to download the latest version suitable for any operating system (Windows, macOS, or Linux).

<a id='f866ffce-8bbd-4c45-b12a-09ecd13e9108'></a>

Follow the instructions on the website to complete the installation process.

<a id='ca83f90c-cde0-4f55-95d6-5d8991f27a2f'></a>

# Install Thinger.io from the Library Manager

Thinger.io Client libraries contain the software needed to connect Arduino-compatible devices with the Thinger.io platform. Using these libraries is the preferred method for connecting devices, as it allows leveraging all of Thinger.io's features.

<a id='6135459c-8fe0-4e5c-8102-15b02cf029db'></a>

To install the Thinger.io library from the Arduino Library Manager:

1.  **Open the Library Manager**:
    *   In the Arduino IDE, go to **Sketch > Include Library > Manage Libraries**.
2.  **Search for Thinger.io**:
    *   Use the search bar in the Library Manager to find "Thinger.io".
3.  **Install the Library**:
    *   Select the Thinger.io Client library from the search results and click **Install**.

<a id='6512e60e-8c5f-41cd-8cfe-adcec38d253c'></a>

2

<!-- PAGE BREAK -->

<a id='5978e2ed-d6ea-4d98-a56d-8faa5b6df529'></a>

sketch_jun6a | Arduino IDE 2.3.2

Arduino UNO R4 WiFi

LIBRARY MANAGER

Thinger.io

Type: All
Topic: All

thinger.io by Alvaro Luis Bustamante...
2.30.0 installed
Arduino library for IOTMP protocol used on Thinger.io IOT Platform. Thinger.io is an ope...
More info

2.30.0 REMOVE

ClimaStick by Jorge Trincado Castan...
Arduino ClimaStick v1 & v2 library for the Thinger.io Internet of Things Platform...
More info

1.3.1 INSTALL

sketch_jun6a.ino

```arduino
1 void setup() {
2 // put your setup code here, to run once:
3
4 }
5
6 void loop() {
7 // put your main code here, to run repeatedly:
8
9 }
10
```

Ln 10, Col 1 Arduino UNO R4 WiFi on /dev/cu.usbmodemF412FA765E202

<a id='4adb04a5-13da-4f42-8012-179c91abac31'></a>

Thinger.io Arduino Library

<a id='672c90db-4b92-42ad-a256-928a21186f52'></a>

## Install Thinger.io from ZIP

If there is a preference to manage the libraries manually or if the Library Manager is not working, the Thinger.io library can be installed by following these steps:

<a id='069bf8c0-e5dc-4b9f-8bd2-4a7446e4234a'></a>

1.  **Download the ZIP Library:**
    *   Obtain the .zip library file from the official Thinger.io project GitHub repository.
    *   Click on CODE and download the ZIP named `Arduino-Library-master.zip`.
2.  **Rename the ZIP File:**
    *   Rename `Arduino-Library-master.zip` to something more relevant, such as `thinger.zip`.
3.  **Import the ZIP Library in Arduino IDE:**
    *   Open the Arduino IDE.
    *   Go to **Sketch > Include Library > Add .ZIP Library....**

<a id='8bfb33c0-0f32-417f-aa30-2e9246a4bf1a'></a>

3

<!-- PAGE BREAK -->

<a id='a85250e5-1711-4f3d-89f3-e2b8b147f501'></a>

<ul><li>Navigate to and select the `thinger.zip` file.</li><li>The Arduino IDE will uncompress and copy the zip library into the Arduino libraries folder, typically located under the Documents folder.</li></ul>

<a id='50d3c55d-ab79-4fdf-a1c8-bedb60b8633f'></a>

<table id="3-1">
<tr><td id="3-2" colspan="3">ESP8266 | Arduino IDE 2.3.6</td></tr>
<tr><td id="3-3">File Edit</td><td id="3-4" colspan="2">Sketch Tools Help</td></tr>
<tr><td id="3-5" rowspan="6">A grey box with a checkmark, a folder, and a box with a curved arrow</td><td id="3-6">Verify/Compile</td><td id="3-7">Ctrl + R</td></tr>
<tr><td id="3-8">Upload</td><td id="3-9">Ctrl + U</td></tr>
<tr><td id="3-a">Configure and Upload</td><td id="3-b"></td></tr>
<tr><td id="3-c">Upload Using Programmer</td><td id="3-d">Ctrl + Mayús + U</td></tr>
<tr><td id="3-e">Export Compiled Binary</td><td id="3-f">Alt + Ctrl + S</td></tr>
<tr><td id="3-g">Optimize for Debugging</td><td id="3-h"></td></tr>
<tr><td id="3-i" rowspan="3">Two books and a lightbulb icon</td><td id="3-j">Show Sketch Folder</td><td id="3-k">Alt + Ctrl + K</td></tr>
<tr><td id="3-l">Include Library</td><td id="3-m">&gt; (image of an arrow)</td></tr>
<tr><td id="3-n">Add File...</td><td id="3-o"></td></tr>
</table>

<a id='cfc95f20-dad8-46df-b24b-d8838e875c35'></a>

## Starting a Project

Once the Thinger.io Library has been installed, start a new project using one of the default examples provided. There are examples tailored for different boards, so choose the one that matches the device.

<a id='85c2e2dd-9c32-41df-833a-651ac385c6db'></a>

1. Open Example Project:
    * In the Arduino IDE, go to **File** > **Examples** > **thinger.io**.
    * Select an example that corresponds to the device.

<a id='6aa51d88-147e-4d9a-96c4-2a6905493583'></a>

This will load the example code, which can then be modified to suit specific needs.

<a id='f92cdc65-3e3e-41a0-9f18-f2bd0df053e1'></a>

4

<!-- PAGE BREAK -->

<a id='1e7a2563-f1b4-4f53-9b59-5c6ee202e4d3'></a>

<table id="4-1">
<tr><td id="4-2">OPAMP</td><td id="4-3">(arrow pointing right)</td><td id="4-4"></td><td id="4-5"></td></tr>
<tr><td id="4-6">OTAUpdate</td><td id="4-7">(arrow pointing right)</td><td id="4-8"></td><td id="4-9" rowspan="2">ArduinoCC3000</td></tr>
<tr><td id="4-a">Preferences</td><td id="4-b">(arrow pointing right)</td><td id="4-c"></td></tr>
<tr><td id="4-d">RTC</td><td id="4-e">(arrow pointing right)</td><td id="4-f"></td><td id="4-g">ArduinoENC28J60</td></tr>
<tr><td id="4-h">SD</td><td id="4-i">(arrow pointing right)</td><td id="4-j"></td><td id="4-k">ArduinoEthernet</td></tr>
<tr><td id="4-l">SDU</td><td id="4-m">(arrow right)</td><td id="4-n"></td><td id="4-o">ArduinoGSM1400</td></tr>
<tr><td id="4-p">Servo</td><td id="4-q">(arrow right)</td><td id="4-r"></td><td id="4-s" rowspan="3">ArduinoMKR1000 ArduinoMKR1010 ArduinoMKRNB1500</td></tr>
<tr><td id="4-t">SoftwareATSE</td><td id="4-u">(arrow right)</td><td id="4-v"></td></tr>
<tr><td id="4-w">SoftwareSerial</td><td id="4-x">(arrow right)</td><td id="4-y"></td></tr>
<tr><td id="4-z">Stepper</td><td id="4-A">(arrow right)</td><td id="4-B"></td><td id="4-C" rowspan="3">ArduinoNano33IOT ArduinoNanoRP2040 ArduinoOptaEthernet ArduinoOptaWiFi</td></tr>
<tr><td id="4-D">TFT</td><td id="4-E">&gt; (image)</td><td id="4-F">Ln 10</td></tr>
<tr><td id="4-G">WDT</td><td id="4-H">&gt; (image)</td><td id="4-I"></td></tr>
<tr><td id="4-J">WiFiS3</td><td id="4-K">&gt; (image)</td><td id="4-L">Arduino</td><td id="4-M">Arduino PortentaH7</td></tr>
<tr><td id="4-N">Examples from Custom Libraries</td><td id="4-O"></td><td id="4-P">EnergiaCC3200</td><td id="4-Q">Arduino PortentaH7Ethernet</td></tr>
<tr><td id="4-R">Arduino_Portenta_OTA</td><td id="4-S">&gt; (image)</td><td id="4-T">ESP32</td><td id="4-U">ArduinoR4Wifi</td></tr>
<tr><td id="4-V">MKRNB</td><td id="4-W">&gt;</td><td id="4-X">ESP8266</td><td id="4-Y">ArduinoTinyGSM</td></tr>
<tr><td id="4-Z">thinger.io</td><td id="4-10">&gt;</td><td id="4-11">LinkItOne</td><td id="4-12">ArduinoWifi</td></tr>
<tr><td id="4-13">WIFININA</td><td id="4-14">&gt;</td><td id="4-15">Sonoff</td><td id="4-16">ArduinoYun</td></tr>
</table>
Thinger.io Arduino Examples

<a id='bc05a67d-31bc-4414-ad72-668487297d8c'></a>

A basic example for an ESP32 device:

<a id='b641a8df-2d24-403f-bd54-9c9a36560b24'></a>

5

<!-- PAGE BREAK -->

<a id='86dfad77-878e-47ed-aaeb-ebb7cc4a018d'></a>

ESP32.ino arduino_secrets.h

#define THINGER_SERIAL_DEBUG
#include <ThingerESP32.h>
#include "arduino_secrets.h"

ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
// open serial for debugging
Serial.begin(115200);

pinMode(16, OUTPUT);

thing.add_wifi(SSID, SSID_PASSWORD);

// digital pin control example (i.e. turning on/off a light,
a relay, configuring a parameter, etc)
thing["GPIO_16"] << digitalPin(16);

// resource output example (i.e. reading a sensor value)
thing["millis"] >> outputValue(millis());

// more details at http://docs.thinger.io/arduino/
}

void loop() {
thing.handle();
}

<a id='a83e8c1d-5b6c-418f-9a79-c3bc2d1abc7c'></a>

Previous
SDK SETUP

Next
Visual Studio Code

<a id='19db7669-9015-4a4f-b71d-876d4ea6ad37'></a>

Last updated 5 months ago

Was this helpful?
option :) : [ ]
option :| : [ ]
option :( : [ ]

<a id='03f7c641-24d6-4b6a-be50-e4123a6a1a43'></a>

6

<!-- PAGE BREAK -->

<a id='ceb8ccbe-8895-4ed9-b45c-85a560a1a9b5'></a>

<::Three icons are displayed horizontally. From left to right, they are a sun icon, a computer monitor icon, and a moon icon. The computer monitor icon is highlighted with a light grey background and a border, indicating it is selected.: figure::>

<a id='ac7910f7-623a-4192-8afe-262a563e84ee'></a>

7