<a id='29f023b7-ebf7-4b07-962b-3543ec7de91e'></a>

<::logo: thinger.io
thinger.io
SDK SETUP
It features a black text logo with a gray square around the ".io" part, accompanied by a hamburger menu icon and the text "SDK SETUP" below.::>

<a id='538f1b92-b969-4e7e-98f1-3a280a4fa20a'></a>

<::A UI element featuring a search icon (magnifying glass) in a rounded square. Partially visible behind it are the GitHub Octocat logo and the text "Edit".: figure::>

<a id='2641b077-f127-47e8-a133-9d1abd160c1c'></a>

Arduino IDE

<a id='91dcf127-aa7f-4a24-a135-ef13d5bcb141'></a>

Arduino is widely recognized as the best framework for learning, prototyping, and even
product development. Its simplicity and the robust community of developers
continuously enhancing its capabilities make it an excellent choice.

<a id='7a902cee-1227-45b2-82ca-4b7319801e0f'></a>

At Thinger.io, we have developed a Software Client to easily connect Arduino-based devices. This client is compatible with a wide variety of hardware and is available for Windows, macOS, and Linux distributions. It is possible to download it for free from the official Arduino website л.

<a id='bea10989-d6b9-4b5c-ad0a-f857943dc24e'></a>

The following sections will provide guidance on the installation and preparation of the Arduino IDE to work with Thinger.io client libraries.

<a id='d30d1c9c-ef6d-4738-bed6-2d41cbf66a80'></a>

sketch_jun6a | Arduino IDE 2.3.2

Arduino UNO R4 WiFi

sketch_jun6a.ino
```cpp
1 void setup() {
2   // put your setup code here, to run once:
3 }
4
5 void loop() {
6   // put your main code here, to run repeatedly:
7 }
8
9
10
```
indexing: 61/67                                             No Notifications
Ln 1, Col 1 Arduino UNO R4 WiFi on /dev/cu.usbmodemF412FA765E202

<a id='e6500f13-8d4e-4f4e-8b53-f3f7b0e5e023'></a>

Arduino IDE

<a id='044a3c24-8ee8-4f5c-a95f-9d41ae04256a'></a>

1

<!-- PAGE BREAK -->

<a id='5b96bac6-9a12-44cb-aab8-6282c343950a'></a>

# Installing the Arduino IDE
To use Thinger.io with Arduino, a modern version of the Arduino IDE that supports the Library Manager and other advanced features is needed. Version 1.6.3 or later should be installed. If a compatible version is already installed, this step can be skipped.

<a id='e71826e6-e8bc-4c5b-b1a6-48723cdd82ec'></a>

1. **Download the Arduino IDE:** Visit the official Arduino download page > to download the latest version suitable for any operating system (Windows, macOS, or Linux).

<a id='7e0af62d-a56c-4f9c-8641-fcd3ee585280'></a>

Follow the instructions on the website to complete the installation process.

<a id='152b1a8c-1c88-48d3-bdb3-0396de0a6e19'></a>

# Install Thinger.io from the Library Manager

Thinger.io Client libraries contain the software needed to connect Arduino-compatible devices with the Thinger.io platform. Using these libraries is the preferred method for connecting devices, as it allows leveraging all of Thinger.io's features.

<a id='2da0bfa8-65f0-4ea8-a264-20e90706f3c2'></a>

To install the Thinger.io library from the Arduino Library Manager:

1.  **Open the Library Manager:**
    *   In the Arduino IDE, go to **Sketch > Include Library > Manage Libraries.**
2.  **Search for Thinger.io:**
    *   Use the search bar in the Library Manager to find "Thinger.io".
3.  **Install the Library:**
    *   Select the Thinger.io Client library from the search results and click **Install.**

<a id='d3f5a49d-c4f8-4cc7-8e03-fef5f2981130'></a>

2

<!-- PAGE BREAK -->

<a id='c8f85a3a-f15a-4b4f-9ecd-61ee0d6cba45'></a>

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

<a id='56b2a94e-3485-490c-a07f-4620a83cfcd2'></a>

Thinger.io Arduino Library

<a id='6fae7275-50bc-410d-a735-f9109292456e'></a>

# Install Thinger.io from ZIP
If there is a preference to manage the libraries manually or if the Library Manager is not working, the Thinger.io library can be installed by following these steps:

<a id='9d70b6df-8c55-4ad9-a114-f5c54cc2f933'></a>

1.  **Download the ZIP Library:**
    *   Obtain the `.zip` library file from the official [Thinger.io project GitHub repository](https://github.com/thinger-io/Arduino-Library)
    *   Click on CODE and download the ZIP named `Arduino-Library-master.zip`
2.  **Rename the ZIP File:**
    *   Rename `Arduino-Library-master.zip` to something more relevant, such as `thinger.zip` .
3.  **Import the ZIP Library in Arduino IDE:**
    *   Open the Arduino IDE.
    *   Go to **Sketch > Include Library > Add .ZIP Library....**

<a id='03725fb6-feb6-404d-bcf4-00b6c0e26a89'></a>

3

<!-- PAGE BREAK -->

<a id='49aadab4-3dc9-4c71-bd36-e1006a6fe046'></a>

* Navigate to and select the `thinger.zip` file.
* The Arduino IDE will uncompress and copy the zip library into the Arduino libraries folder, typically located under the Documents folder.

<a id='1a519594-1286-47f9-b2fb-d34ea9b328b5'></a>

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

<a id='3659099a-a5fe-4d2e-a5b0-d150d9c188e6'></a>

# Starting a Project

Once the Thinger.io Library has been installed, start a new project using one of the default examples provided. There are examples tailored for different boards, so choose the one that matches the device.

<a id='7e1a00bd-808b-4b56-bad2-505decd76ea4'></a>

1. Open Example Project:
   * In the Arduino IDE, go to **File** > **Examples** > **thinger.io**.
   * Select an example that corresponds to the device.

<a id='73283d57-6617-4ce2-a488-1c16e59f0e7d'></a>

This will load the example code, which can then be modified to suit specific needs.

<a id='9869d612-78f3-43ba-afd0-30a22528f35f'></a>

4

<!-- PAGE BREAK -->

<a id='5bb11cc9-5cfb-477b-b915-ae22b0bcb64f'></a>

<::Menu Structure:menu::>
OPAMP >
OTAUpdate >
Preferences >
RTC >
SD >
SDU >
Servo >
SoftwareATSE >
SoftwareSerial >
Stepper >
TFT >
WDT >
WiFiS3 >

Examples from Custom Libraries
  Arduino_Portenta_OTA >
  MKRNB >
  thinger.io >
  WIFININA >

                                 Arduino >
                                 EnergiaCC3200 >
                                 ESP32 >
                                 ESP8266 >
                                 LinkItOne >
                                 Sonoff >
                                                 ArduinoCC3000
                                                 ArduinoENC28J60
                                                 ArduinoEthernet
                                                 ArduinoGSM1400
                                                 ArduinoMKR1000
                                                 ArduinoMKR1010
                                                 ArduinoMKRNB1500
                                                 ArduinoNano33IOT
                                                 ArduinoNanoRP2040
                                                 ArduinoOptaEthernet
                                                 ArduinoOptaWiFi
                                                 ArduinoPortentaH7
                                                 ArduinoPortentaH7Ethernet
                                                 ArduinoR4Wifi
                                                 ArduinoTinyGSM
                                                 ArduinoWifi
                                                 ArduinoYun
                                 Ln 10
Thinger.io Arduino Examples
<::

<a id='d7c33f85-a421-47d9-95ce-a33c05cb2ee8'></a>

A basic example for an ESP32 device:

<a id='cf250073-b10f-422e-b0d3-444e9c221e95'></a>

ESP32.ino arduino_secrets.h

```
#define USERNAME "your_user_name"
#define DEVICE_ID "your_device_id"
#define DEVICE_CREDENTIAL "your_device_credential"

#define SSID "your_wifi_ssid"
#define SSID_PASSWORD "your_wifi_ssid_password"
```

<a id='22e299df-3b05-448c-ab48-66bf20505ce2'></a>

Previous
SDK SETUP

<a id='f068a9f3-780c-4097-ac39-9445509c73cb'></a>

Next
Visual Studio Code

<a id='aaf7359f-672e-47fb-817f-86bee1206379'></a>

Last updated 5 months ago

<a id='a675b7ce-9627-4bf1-9c26-e415a44d2d22'></a>

Was this helpful?
option happy: [ ]
option neutral: [ ]
option sad: [ ]

<a id='e757f72c-04cb-48af-889a-b1b36e68554d'></a>

5

<!-- PAGE BREAK -->

<a id='404d6c6d-2469-4bb8-9c05-7ea9ab7f0bd3'></a>

option sun icon: [ ]
option monitor icon: [x]
option moon icon: [ ]

<a id='18e46c6b-400a-4aad-99dc-4eeb6ea5af0f'></a>

6