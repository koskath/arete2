<a id='556ffad6-dfa3-42f4-95ca-3c5337dd8efb'></a>

DEVICES

<a id='0ae866d0-5032-40b9-b2ca-b9b9bba302c9'></a>

Edit

<a id='2dc01485-97c2-4981-ab8a-6c289c205206'></a>

ARDUINO WIFI

<a id='e01f5c82-e30b-439f-aac4-c976f2130473'></a>

# Introduction
Using Arduino with WiFi is a great option for connecting the Arduino board wirelessly to the Internet in a few minutes. Connecting a device to a WiFi network is straightforward; no configuration beyond the SSID and password is needed. There are many boards with WiFi connectivity, as it provides an easy setup, without any cable requirement. There are plenty of alternatives for WiFi connectivity, including shields, devices with on-board WiFi, or external modules that can be connected to the microcontroller.

<a id='2f4af647-e544-4d2e-8c04-cb8f41961d04'></a>

In this documentation, we cover how to connect devices over WiFi by using different approaches, like Arduino Shields, external modules, and devices with embedded WiFi like Arduino Nano 33 IoT, or Arduino MKR WIFI 1010.

<a id='c860faa2-84d8-4971-99dc-2bae6a8473b5'></a>

Arduino with WiFi Shield

<a id='a805cd0c-574b-4d22-a559-04a3dc5d8c5b'></a>

1

<!-- PAGE BREAK -->

<a id='28843ca3-6ee8-43ab-b1ca-82b75de02fbd'></a>

<::An illustration of an Arduino WiFi shield, viewed from above. The shield is dark gray with various components and pin headers labeled in white text.  
  
On the top edge, from left to right, are pin headers labeled: AREF, GND, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, TX, RX. Below these, to the right, is a pin labeled INT and a header for ICSP.  
  
On the left side, there's a header labeled "WIFI Shield" vertically.  
  
At the bottom edge, from left to right, are pin headers labeled: RESET, 3V3, 5V, Gnd, 9V. Following these is a section labeled "ANALOG IN" with pins A0, 1, 2, 3, 4, A5.  
  
A large rectangular area in the bottom right is labeled "SD". There are also several indicator lights and connection points visible on the board.  
: figure::>


<a id='e201d33c-9951-4993-87c7-10983621ef81'></a>

This example will allow connecting the Arduino device with the WiFi Shield to the cloud platform in a few lines. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='b2344518-f34e-4c82-b5e4-f7b1e6faee0b'></a>

2

<!-- PAGE BREAK -->

<a id='0b4305cd-6cf9-42ac-9830-a7602ff253ab'></a>

ArduinoWiFi.ino arduino_secrets.h

<a id='c0df6105-8caf-4e4d-ae5c-e1f146478971'></a>

```cpp
#define THINGER_SERIAL_DEBUG
#define THINGER_USE_STATIC_MEMORY
#define THINGER_STATIC_MEMORY_SIZE 512

#include <WiFi.h>
#include <ThingerWifi.h>
#include "arduino_secrets.h"

ThingerWifi thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  pinMode(2, OUTPUT);

  // pin control example (i.e. turning on/off a light, a
  // relay, etc)
  thing["led"] << digitalPin(2);

  // resource output example (i.e. reading a sensor value, a
  // variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}
```

<a id='1fe5ad55-a77a-4f0d-9607-012bbe6c5922'></a>

Arduino with CC3000

<a id='8031627b-78ab-4b6c-878a-4f794f2ed231'></a>

3

<!-- PAGE BREAK -->

<a id='eff8a26c-99e3-412e-a2e1-40841915dfad'></a>

The CC3000 chip from Texas Instruments was one of the first low-cost WiFi chips that revolutionized the IoT maker ecosystem. In contrast to the other available WiFi alternatives, like the WiFi shield, the CC3000 appeared at a low cost (about 10$) for its time. It is a powerful chip as it integrates the whole TCP/IP stack and many other protocols. Some vendors, like Adadruit, started to build modules and libraries for integrating this chip with the Arduino ecosystem. Thanks to the libraries provided by Adafruit is then possible to build a connected device with a few lines of code.

<a id='7d87a658-7521-495d-a818-eeb09c58e9eb'></a>

<::A close-up photograph of a black Adafruit CC3000 WiFi module, version 1.1, on a white background. The module is rectangular with rounded corners, populated with various electronic components. A prominent metallic shield in the center has text:
Model: CC3000MOD
FCC ID: Z64-CC3000EM
IC: 4511-CC3000EM
LTC: 13430 15
R 007-AB0057

Around the edges of the board are solder pads labeled with functions. On the left side, from top to bottom, are "Adafruit CC3000 WiFi", then a series of pads labeled: "GND", "Debug", "TXD", and "RXD". On the right side, from top to bottom, are pads labeled: "IRQ", "UBEN", "CS", "MOSI", "MISO", "CLK", "UTN", "GND", and "3V3". There is also a component labeled "39AY1YM HC4050M G4". A small flower-like logo is visible on the top right corner of the board. The module is titled: Texas Instruments CC3000 WiFi module.
: figure::>

<a id='1a1104cb-622c-4d9b-99f9-db212b6a3950'></a>

For this module is required to have installed the **Adafruit CC3000 Libraries**, as they are directly used by the Thinger client. Install it directly from the Arduino Library Manager by searching `cc3000`.

<a id='d6290d1a-874d-40fa-b1fe-67b40ee00b3f'></a>

4

<!-- PAGE BREAK -->

<a id='de1bc2d6-1c97-4ab0-bf8f-3c690efcaac1'></a>

Library Manager

Type All
Topic All
cc300

**Adafruit CC3000 Library**
by Adafruit Version 1.0.4 INSTALLED
Library code for Adafruit's CC3000 WiFi breakouts. The CC3000 allows an Arduino to connect to a WiFi network and access the internet.
See more at: https://learn.adafruit.com/adafruit-cc3000-wifi/
More info

Select version
Install

**CC3000 MDNS**
by Adafruit
Simple multicast DNS name resolution library for Adafruit's CC3000 and Arduino. Simple multicast DNS name resolution library for Adafruit's CC3000 and Arduino.
More info

**PubSubClient**
by Nick O'Leary
A client library for MQTT messaging. MQTT is a lightweight messaging protocol ideal for small devices. This library allows you to send and receive MQTT messages. It supports the latest MQTT 3.1.1 protocol and can be configured to use the older MQTT 3.1 if needed. It supports all Arduino Ethernet Client compatible hardware, including the Intel Galileo/Edison, ESP8266 and TI CC3000.

Close

<a id='4857bf51-f3f7-4809-947a-d5d7de388a9c'></a>

Install CC3000 Arduino Libraries

<a id='93460115-af78-47cf-a914-f8ee32e98e2a'></a>

This example will allow connecting the Arduino device with the CC3000 module to the cloud platform in a few lines. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='0e3ad6cc-0721-482f-bc1f-7059e9100f23'></a>

5

<!-- PAGE BREAK -->

<a id='f11e690e-c39a-448c-9ffd-90df572a155f'></a>

ArduinoCC3000.ino arduino_secrets.h

<a id='dfd80ba6-731d-404a-bcb2-9ed20a6f4425'></a>

```c
#define THINGER_SERIAL_DEBUG

#include <ThingerCC3000.h>
#include "arduino_secrets.h"

ThingerCC3000 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  pinMode(2, OUTPUT);

  // pin control example (i.e. turning on/off a light, a
  // relay, etc)
  thing["led"] << digitalPin(2);

  // resource output example (i.e. reading a sensor value, a
  // variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}
```

<a id='63537f1b-2e3b-4139-91f0-cad98b8dc8a5'></a>

Arduino Yun

<a id='42a79acf-9cee-412e-a133-0e59f755f881'></a>

6

<!-- PAGE BREAK -->

<a id='b9fdafeb-1071-47bf-899d-145ef32281c0'></a>

The Arduino Yùn is a microcontroller board based on the ATmega32u4 and the Atheros AR9331. The Atheros processor supports a Linux distribution based on OpenWrt named OpenWrt-Yun. The board has built-in Ethernet and WiFi support, a USB-A port, micro-SD card slot, 20 digital input/output pins (of which 7 can be used as PWM outputs and 12 as analog inputs), a 16 MHz crystal oscillator, a micro USB connection, an ICSP header, and 3 reset buttons. This board lets the programmable ATmega32u4 communicate with the Internet by using the Bridge Library that exposes some functions running in the Linux distribution.

<a id='8fc05de7-e460-4296-9027-53bb8ad44907'></a>

<::image: An overhead view of an Arduino Yun development board. The board is dark grey/brown with various electronic components, connectors, and labels. At the top left, there's an Ethernet port block and a button labeled "RST" next to "3204". Along the top edge, there are pin headers labeled "AREF", "GND", and digital pins from "13" down to "1/TX 0/RX". In the center, there's a prominent white Arduino logo with an infinity symbol and a plus sign, above the text "Arduino™ YUN". To the left, the text "ARDUINO.CC" is visible, along with a USB host port and a button labeled "WAN-RST". On the right side, there's an "ICSP" header (a 2x3 pin array) and a column of LEDs labeled "RX", "TX", "LIN", "WAN", "ON", "WLAN", "USB", and a button labeled "YUN-RST". At the bottom edge, there are more pin headers labeled "IOREF", "RST", "3.3V", "5V", "GND", "GND", "VIN", and analog input pins "A0" through "A5". A large square integrated circuit is visible in the lower-middle section of the board.  
Arduino Yun Board::>

<a id='81baee87-961a-44a0-a64f-5ea520e100a5'></a>

This example will allow connecting an Arduino Yun to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information. Notice that it is not required to configure any network parameters in the code, as this is managed by the running Linux distribution. However, it may be necessary to connect with the Arduino Yun via WiFi to connect it to a local network.

<a id='f81080b1-1c8e-4fd6-b50e-3331c4746443'></a>

7

<!-- PAGE BREAK -->

<a id='89e241d5-6394-4f03-bd27-9e366999c902'></a>

ArduinoYun.ino arduino_secrets.h

<a id='4ba2ff29-2b2e-40a3-b905-0c2e46f52f0f'></a>

#include <ThingerYun.h>
#include "arduino_secrets.h"

<a id='21245a51-0d3a-4c08-b3c5-e83819977da8'></a>

thinger.io

<a id='b7ddb650-4ca7-49b5-9a33-b042cb6fcc4b'></a>

<::A magnifying glass icon is centered within a rounded square with a subtle shadow.: icon::>

<a id='3ba1782c-b67f-4c21-bbc8-9946de9cce75'></a>

pinMode(LED_BUILTIN, OUTPUT);

// initialize bridge
Bridge.begin();

// pin control example (i.e. turning on/off a light, a
relay, etc)
thing["led"] << digitalPin(LED_BUILTIN);

// resource output example (i.e. reading a sensor value, a
variable, etc)

// more details at http://docs.thinger.io/arduino/
}

void loop() {
thing.handle();
}

<a id='3e736aa2-5e91-4926-8733-cde356d93dd0'></a>

i For using Arduino Yun, the device must be connected to a network with Internet, just via Ethernet or a Wifi connection. It can be configured in the Arduino Yun web configuration.

<a id='73a40e04-3f30-4f51-a611-6790145e4ac9'></a>

8

<!-- PAGE BREAK -->

<a id='c20785b0-7009-4a39-91e9-4d227efb8522'></a>

<::logo: Arduino
ARDUINO YÚN
This logo features a white infinity symbol with a minus sign on the left and a plus sign on the right, above the word "ARDUINO" and then "YÚN", all on a dark grey background.::>

<a id='fe43c76f-dcf4-4c3e-8917-682cf7ed296e'></a>

For more advanced network configuration features, see the advanced configuration panel (luci)

<a id='f5b71d19-5e80-491b-887b-6ebf6951f2ac'></a>

YÚN BOARD CONFIGURATION ⓘ

YÚN NAME *: Arduino

PASSWORD:

CONFIRM PASSWORD:

TIMEZONE *: Europe/Madrid ▾

<a id='59896de1-ed44-454b-81da-601a5cb12e0b'></a>

## WIRELESS PARAMETERS

option CONFIGURE A WIRELESS NETWORK: [x]

DETECTED WIRELESS NETWORKS: Thinger.io (WPA2, quality 80%) Refresh

WIRELESS NAME *: Thinger.io

SECURITY: WPA2

PASSWORD *: .......... (eye icon)

<a id='d65f7e69-d260-4cd9-b8ca-8e679def3302'></a>

DISCARD
CONFIGURE & RESTART

<a id='d0b3c9ca-8a98-4fc2-92b0-cc6c6cc49f97'></a>

Arduino Yun network configuration

<a id='c2d44ddc-92e0-4985-865f-984e77260930'></a>

# Arduino MKR1000
The Arduino MKR1000 is a microcontroller based on the Atmel ATSAMW25 SoC (System on Chip), which is part of the SmartConnect family of Atmel Wireless devices, specifically designed for IoT projects and devices. A good 32-bit computational power similar to the Zero board, the usual rich set of I/O interfaces, low-power WiFi with a Cryptochip for secure communication, and the ease of use of the Arduino Software (IDE) for code development and programming. All these features make this board the preferred choice for the emerging IoT battery-powered projects in a compact form factor.

<a id='7dd30eb7-e1c7-4def-836f-09a1bb697989'></a>

9

<!-- PAGE BREAK -->

<a id='8982f286-8030-4dd6-9328-d48e852c0d7a'></a>

<::An overhead view of a dark gray circuit board, likely a development board or microcontroller. The board is rectangular with rounded corners and features four mounting holes, one in each corner. On the left side, there is a USB connector. The board is populated with numerous surface-mount components, including integrated circuits, resistors, and capacitors. In the center-right, a large rectangular module is visible, which appears to be a wireless communication module, possibly with an integrated antenna pattern on its right edge. Below this module, along the bottom edge of the board, there is a row of labeled pins from left to right: AREF, DAC0/A0, A1, A2, A3, A4, A5, A6, 0, 1, ~2, ~3, ~4, ~5. Along the top right edge of the board, another row of pins is labeled vertically from left to right: 5V, VIN, VCC, GND, RESET, 14 TX, 13 RX, 12 SCL, 11 SDA, 10 MISO, 9 SCK, 8 MOSI, 7, 6. A small push button and a multi-pin header are also visible in the central-left area of the board.: circuit board::>

<a id='beffc65c-8ccf-41d7-87a7-5e887e3f7217'></a>

This example will allow connecting the MKR1000 device to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='f148a9dc-9214-4f46-b7c1-132380208ed1'></a>

10

<!-- PAGE BREAK -->

<a id='2cd07a6f-e79e-452f-978f-50d3c5b18ce8'></a>

C++ arduino_secrets.h

<a id='4b704de2-444c-4aac-a30f-24ba9f26f701'></a>

#define THINGER_SERIAL_DEBUG
#include <ThingerWifi101.h>
#include "arduino_secrets.h"

// cannot connect? Update WiFi101 firmware and add
iot.thinger.io SSL Certificate
// https://support.arduino.cc/hc/en-us/articles/360016119219

ThingerWifi101 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
// open serial for debugging
Serial.begin(115200);

// configure wifi network
thing.add_wifi(SSID, SSID_PASSWORD);

pinMode(LED_BUILTIN, OUTPUT);

// pin control example (i.e. turning on/off a light, a
relay, etc)
thing["led"] << digitalPin(LED_BUILTIN);

// resource output example (i.e. reading a sensor value, a
variable, etc)
thing["millis"] >> outputValue(millis());

// more details at http://docs.thinger.io/arduino/
}

void loop() {
thing.handle();
}

<a id='556d6d93-7b3a-46f2-a7db-0d944da1546f'></a>

ⅰ For using MKR1000 over the default TLS/SSL connection, it is required to install the Thinger.io server certificate on the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='d9387c9a-dc6a-4bb9-9c3b-1f3fee248d18'></a>

11

<!-- PAGE BREAK -->

<a id='fc9d2fdd-5247-45b3-982a-c5c14edde848'></a>

WiFi101 Firmware/Certificates Updater

1. Select port of the WiFi module
If the port is not listed click "Refresh list" button to regenerate the list

/dev/cu.SOC
/dev/cu.MALS
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1442211
/dev/cu.usbmodem1442311

Refresh list
Test connection

2. Update firmware
Select the firmware from the dropdown box below
WINC1501 Model B (19.5.2)

Update Firmware

3. Update SSL root certificates
Add domains in the list below using "Add domain" button

arduino.cc:443
thinger.io:443

Add domain
Remove domain

Upload Certificates to WiFi module

<a id='c5487f2c-75b3-4c0b-b798-ba94e8004caf'></a>

WiFi 101 Certificates Updater

<a id='952475fc-0c1e-48a3-af0d-a84e93e2c22b'></a>

# Arduino MKR1010

The Arduino MKR WiFi 1010 serves as an accessible entry point for basic IoT and pico-network application design. It is a comprehensive solution for many fundamental IoT application scenarios, whether building a sensor network connected to an office or home router, or creating a BLE device that sends data to a cellphone. The board's primary processor is a low-power Arm® Cortex®-M0 32-bit SAMD21, consistent with other boards in the Arduino MKR family. WiFi and Bluetooth® connectivity are handled by the u-blox NINA-W10 module, a low-power chipset operating in the 2.4GHz range. Additionally, the Microchip® ECC508 crypto chip ensures secure communication. The board also features a battery charger and a directional RGB LED.

<a id='2d641447-d247-49ba-b7c8-b82342117fa6'></a>

12

<!-- PAGE BREAK -->

<a id='cae922d5-a348-45ac-9a56-1a8c06d8b30e'></a>

<::A top-down view of a black electronic circuit board, likely a microcontroller board. The board has various surface-mount components, including integrated circuits, resistors, and capacitors. On the left side, there is a micro-USB port and a label "CHRG". A white connector is visible at the bottom left. Pin headers run along the top and bottom edges of the board. A button labeled "RST" is near the center. A large integrated circuit with the text "Atmel" is prominent. Towards the right, there is a module labeled "blox" which also displays a QR code, the text "008-001851", and "MODEL:NINA-W102". The top right corner of the board has the text "ARDUINO.CC", and the bottom right corner shows "MKR WIFI 1010". Other small labels like "ON" and "2R2" are also visible.: figure::>

<a id='9eaf7f93-84bf-45b4-a513-e1a1ee470652'></a>

Arduino MKR1010

<a id='3644fdf2-9cac-49a3-9c71-e909acdb6732'></a>

This example will allow connecting the MKR1010 device to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='9afaaa4f-754e-43c3-b3a5-2bd45b8b7273'></a>

The integration with Thinger.io requires downloading an additional library called "Arduino WiFININA" that allows communicating with the U-BLOX WiFi module.

<a id='17276060-4234-4579-ba7b-c80d3302100b'></a>

13

<!-- PAGE BREAK -->

<a id='44849048-87db-4999-9c7a-55688a6cb075'></a>

ArduinoMKR1010.ino arduino_secrets.h

<a id='9af2c55c-1453-4896-81a6-ea333163bae6'></a>

#define THINGER_SERIAL_DEBUG
#include <ThingerWiFiNINA.h>
#include "arduino_secrets.h"

// cannot connect? Update WiFiNINA and add iot.thinger.io SSL
// Certificate
// https://support.arduino.cc/hc/en-us/articles/360016119219

ThingerWiFiNINA thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // configure LED_BUILTIN for output
  pinMode(LED_BUILTIN, OUTPUT);

  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  // pin control example (i.e. turning on/off a light, a
  // relay, etc)
  thing["led"] << digitalPin(LED_BUILTIN);

  // resource output example (i.e. reading a sensor value, a
  // variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}

<a id='f2f74bc2-8f9c-44d8-98cd-6c27df2d512b'></a>

For using MKR1010 over the default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='b86f6f47-e966-4d92-bba3-f756d00f2fd4'></a>

14

<!-- PAGE BREAK -->

<a id='f3721cd4-f61d-49c2-9b9a-144cc2473ff7'></a>

WiFi101 Firmware/Certificates Updater

1. Select port of the WiFi module
If the port is not listed click "Refresh list" button to regenerate the list

/dev/cu.SOC
/dev/cu.MALS
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1442211
/dev/cu.usbmodem1442311

Refresh list
Test connection

2. Update firmware
Select the firmware from the dropdown box below
WINC1501 Model B (19.5.2)

Update Firmware

3. Update SSL root certificates
Add domains in the list below using "Add domain" button

arduino.cc:443
thinger.io:443

Add domain
Remove domain

Upload Certificates to WiFi module

<a id='d9f3ca28-bf56-4cba-87fb-135171655397'></a>

WiFiNINA Certificates Updater

<a id='fd5bd53c-0e4c-4db1-be5d-ed5d8472f75b'></a>

# Arduino Nano 33 IoT

In the same iconic size as the Arduino Nano, the Arduino Nano 33 IoT hosts an Arm Cortex-M0+ SAMD21 processor, a WiFi and Bluetooth module based on ESP32, a 6-axis Inertial Measurement Unit (IMU) and a crypto chip which can securely store certificates and pre-shared keys.

<a id='30747324-9c57-4522-aa2b-aca10d130ded'></a>

15

<!-- PAGE BREAK -->

<a id='a1972462-c177-4f23-87d5-631203c569be'></a>

<::A close-up photograph of a small, black circuit board, likely a microcontroller board, with various electronic components. The board features a row of through-hole pins along its top and bottom edges. On the left side, there is a silver micro-USB connector. Above the USB connector, the word "ON" is visible. Towards the center-left, there is a small, round reset button labeled "RST". Along the top edge, the text "ARDUINO.CC" is printed. The central component is a large, square integrated circuit chip labeled "Atmel ATSAMD21 G18A-U 1838". To the right of the Atmel chip, there is a rectangular module with a white label. This module has a QR code and text that reads "ublox" at the bottom, and vertically oriented text "008-0019/10 MODEL:NINA-W102" along its right side. Other smaller surface-mount components, such as resistors, capacitors, and smaller integrated circuits, are scattered across the board.: figure::>

<a id='dea14bc0-b2e1-4f7c-bdfe-e8d8f8f0d6b7'></a>

! The integration with Thinger.io requires downloading an additional library called "Arduino WIFININA" that allows communicating with the U-BLOX WiFi module.

<a id='2d028935-e5aa-4f3a-af8d-9627bcfde256'></a>

This example will allow connecting the Arduino Nano 33 IoT device to the cloud
platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just
needs to be modified with the relevant information.

<a id='fa6a669b-2d8c-484d-8201-19fc8731db06'></a>

ArduinoNano33IoT.ino arduino_secrets.h
#define USERNAME "your_user_name"
#define DEVICE_ID "your_device_id"
#define DEVICE_CREDENTIAL "your_device_credential"

#define SSID "your_wifi_ssid"
#define SSID_PASSWORD "your_wifi_ssid_password"

<a id='ed7f9310-679e-4957-b998-9a26427fbf5a'></a>

i For using Arduino 33 IoT over the default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='6cc6eb71-ba32-452b-9afb-57869232c55f'></a>

16

<!-- PAGE BREAK -->

<a id='a9f09eae-6e05-4cf1-bc5a-61253d16182d'></a>

<::Screenshot of a WiFi101 Firmware/Certificates Updater application window.

WiFi101 Firmware/Certificates Updater

1. Select port of the WiFi module
If the port is not listed click "Refresh list" button to regenerate the list
/dev/cu.SOC
/dev/cu.MALS
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1442211
/dev/cu.usbmodem1442311
Button: Refresh list
Button: Test connection

2. Update firmware
Select the firmware from the dropdown box below
Dropdown selection: WINC1501 Model B (19.5.2)
Button: Update Firmware

3. Update SSL root certificates
Add domains in the list below using "Add domain" button
List item: arduino.cc:443
List item: thinger.io:443
Text input field
Button: Add domain
Button: Remove domain
Button: Upload Certificates to WiFi module
: GUI::>

<a id='c23e0e64-cfb8-40f7-8042-ae2b52d7c8c0'></a>

WiFiNINA Certificates Updater

<a id='bad60a01-6139-4cd6-9480-fe86b57b07b3'></a>

# Arduino Nano RP2040

The brain of the board is the Raspberry Pi RP2040 silicon, a dual-core Arm Cortex M0+ running at 133MHz. It has 264KB of SRAM, and the 16MB of flash memory is off-chip to give extra storage. But what's really exciting is the onboard connectivity options. The hugely popular and highly adaptable u-blox NINA-W102 radio module is on there to make this a true IoT champion. It has on-board, built-in sensors to turn builds into powerhouse projects as well. Microphone and motion sensing add a depth of possibilities that's almost impossible to find in a board of this size. The Arduino Nano RP2040 Connect is the premium choice for RP2040 devices and the perfect option for upgrading projects and unlocking the potential of new ones.

<a id='270c70ed-f877-4a1b-8f3c-d6dc41bd0139'></a>

17

<!-- PAGE BREAK -->

<a id='f4d69b5d-4e0b-4cdf-8cd6-54f2cf51ab5a'></a>

<::An overhead, slightly angled view of a compact microcontroller board, likely an Arduino Nano RP2040 Connect. The board features a USB-C port on one end, a small white push button, and various surface-mount components. Prominently visible are two main chips: one with "RP2040" and "2140" markings, and another larger chip with the Arduino infinity logo (a horizontal figure-eight with a plus sign on the left and a minus sign on the right) on a metallic housing. Pin headers line both long edges of the board. A metal bracket with the number "2037" is visible near the Arduino chip.: figure::>

<a id='e1d01fce-17f3-4058-a561-28aaae0d20ee'></a>

Arduino Nano RP2040

<a id='5f5324de-d4b6-4220-9582-697979884688'></a>

The integration with Thinger.io requires downloading an additional library called "Arduino WiFININA" that allows communicating with the U-BLOX WiFi module.

<a id='e0891514-ec71-46d0-a6eb-4bad80c417e5'></a>

This example will allow connecting the Arduino Nano RP2040 device to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='02979c87-f40f-4aeb-98e4-2a0ba40d2d3e'></a>

18

<!-- PAGE BREAK -->

<a id='a01a60d5-5b88-40cb-b1c7-9404c3888aa3'></a>

ArduinoNanoRP2040.ino arduino_secrets.h

<a id='0f1240c1-e03c-4abc-8e94-893428d1eda6'></a>

#define USERNAME "your_user_name"
#define DEVICE_ID "your_device_id"
#define DEVICE_CREDENTIAL "your_device_credential"

#define SSID "your_wifi_ssid"
#define SSID_PASSWORD "your_wifi_ssid_password"

<a id='1924dc24-b542-4b54-be11-dcb739edafe5'></a>

For using Arduino Nano RP2040 over the default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='ad0e87e6-e845-4e06-a682-7a45a2283511'></a>

WiFi101 Firmware/Certificates Updater

1. Select port of the WiFi module
If the port is not listed click "Refresh list" button to regenerate the list

/dev/cu.SOC
/dev/cu.MALS
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1442211
/dev/cu.usbmodem1442311

Refresh list
Test connection

2. Update firmware
Select the firmware from the dropdown box below
WINC1501 Model B (19.5.2)

Update Firmware

3. Update SSL root certificates
Add domains in the list below using "Add domain" button

arduino.cc:443
thinger.io:443

Add domain
Remove domain

Upload Certificates to WiFi module

<a id='7e54a96d-d560-49fa-bed6-36cba7fb2b88'></a>

WiFiNINA Certificates Updater

<a id='4f71f11e-6ac9-4aa6-81b1-6eee8f81e69f'></a>

19

<!-- PAGE BREAK -->

<a id='e78728b8-3ad2-409f-9f63-eebdba6cf989'></a>

# Arduino Portenta H7

Portenta H7 simultaneously runs high-level code along with real-time tasks. The design includes two processors that can run tasks in parallel. For example, it is possible to execute Arduino compiled code along with MicroPython code, and have both cores communicate with one another. The Portenta functionality is two-fold, it can either be running like any other embedded microcontroller board or as the main processor of an embedded computer.

<a id='60897e32-0495-420d-81d1-66e60daf4c99'></a>

H7's main processor is the dual-core STM32H747, including a Cortex® M7 running at 480 MHz and a Cortex® M4 running at 240 MHz. The two cores communicate via a _Remote Procedure Call_ mechanism that allows calling functions on the other processor seamlessly.

<a id='d4ffa1bf-dbd4-4753-86ff-5d441823d03a'></a>

<::A black Arduino circuit board, rectangular in shape, densely packed with various electronic components. The board features multiple integrated circuits (ICs), resistors, capacitors, and connectors. Prominently centered is a large black IC labeled "ARDUINO" in white, with "DESIGNED AND ASSEMBLED IN ITALY" written vertically next to it. Other visible text on smaller chips includes "SS9006002", "1DX", "41ACAM195E-081N", and "B80816". The board has an Arduino logo (infinity symbol with a plus and minus) near the top left corner. A USB-C port is located on the right edge, and a microSD card slot is visible near the top right. A small push button switch is also present. Along the top and bottom edges are rows of circular through-holes for pin headers.: electronic circuit board::>

<a id='dfb1e12d-031f-4918-bd92-9210f4c8e185'></a>

Arduino Portenta H7

<a id='cecec0ea-51fb-45bc-8dea-066968582ed3'></a>

20

<!-- PAGE BREAK -->

<a id='983590ef-52d5-45d0-97b8-274cebe1a2d3'></a>

ArduinoPortentaH7.ino
arduino_secrets.h

<a id='2bcc025d-c337-4477-8e73-13d15168d3ce'></a>

```cpp
#define THINGER_SERIAL_DEBUG

#include <ThingerMbed.h>
#include "arduino_secrets.h"

ThingerMbed thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // configure LED_BUILTIN for output
  pinMode(LED_BUILTIN, OUTPUT);

  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  // pin control example (i.e. turning on/off a light, a
  // relay, etc)
  thing["led"] << digitalPin(LED_BUILTIN);

  // resource output example (i.e. reading a sensor value, a
  // variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}
```

<a id='99be46d8-a5b4-41f9-93c0-2d0ae069cb1a'></a>

In case of problems when connecting over secure TLS connections, try updating the WiFi firmware by flashing the WiFiFirmwareUpdater example sketch.

<a id='b204aa02-bab0-4a3e-b181-c4d844c67b48'></a>

<::Menu displaying a list of options. The first column shows main categories, and selecting one (indicated by '>') reveals a sub-menu in the second column. The "STM32H747_System" option is highlighted, and its sub-menu is visible.

Left Menu:
- STM32H747_System >
- TFT >
- ThreadDebug >
- USB Mass Storage >
- USBHID >
- USBHOST >

Right Sub-Menu (for STM32H747_System):
- QSPIFormat
- QSPIFReadPartitions
- STM32H747_getBootloaderinfo
- STM32H747_getResetReason
- STM32H747_manageBootloader
- WiFiFirmwareUpdater (highlighted)
: menu::>

<a id='eafddcaa-c9b4-46d5-971c-7cc203a7305e'></a>

21

<!-- PAGE BREAK -->

<a id='2de43259-a956-48e2-b7f0-7309483180d1'></a>

# Arduino Opta Wifi

The Arduino Opta is designed for industrial automation, offering robust performance and reliability. It features a dual-core STM32H747 microcontroller, which includes a Cortex® M7 running at 480 MHz and a Cortex® M4 running at 240 MHz. This configuration enables Opta to handle complex real-time tasks and high-level code execution concurrently.

<a id='a60cb20c-ccdc-47f7-9d48-16888edac265'></a>

With its versatile architecture, the Opta supports running Arduino sketches alongside MicroPython, allowing developers to leverage the strengths of both programming environments. The dual-core setup facilitates inter-core communication via Remote Procedure Call, ensuring smooth and efficient coordination between the two processors. This capability makes the Arduino Opta ideal for advanced automation systems, where precise control and rapid response are crucial.

<a id='94fd058b-fa9b-4591-a87d-d63544405501'></a>

Additionally, the Arduino Opta is equipped with industrial-grade features, such as enhanced I/O capabilities and robust connectivity options. It can be seamlessly integrated into existing industrial networks, providing a reliable solution for monitoring and control applications. Whether used as a standalone microcontroller or as part of a larger embedded system, the Opta's performance and versatility make it a valuable asset in any industrial setting.

<a id='d7b9f6d8-5c98-420a-8ba9-734834fb92ba'></a>

22

<!-- PAGE BREAK -->

<a id='38b07905-dfa6-4c57-8d27-b1ad1a3c9538'></a>

<::An image of a black electronic device, possibly a programmable logic controller or industrial relay, shown from a slightly elevated, angled perspective. The device has multiple labels, indicators, and ports. The top surface displays the "OPTA" logo prominently, along with "RESET" and "USER" buttons, each with an associated indicator light. A "STATUS" section shows four indicator lights labeled "1 2 3 4", with the first light appearing illuminated. Certification marks "cULus LISTED Prog. Cntlr. E528578" are visible. Further on the top surface are the "finder" and "ARDUINO PRO" logos. There's a "LAN" indicator, an "EC15" symbol, and the model number "8A.04.9.024.8320". One side of the device features a "USB" port, a warning symbol (triangle with exclamation mark), and a ground symbol. The bottom section of the device has two sets of screw terminals labeled "OUTPUT 10A" with individual terminals marked "1", "2", "3", and "4". Another side shows an "ETH RJ45" port.: figure::>

<a id='468516d5-4cc0-43d2-8959-de8de160d4fd'></a>

Arduino Opta Wifi

<a id='c292a5cf-795b-462d-87b8-4b4acca31fe5'></a>

23

<!-- PAGE BREAK -->

<a id='72bdb80f-538a-4653-b9e3-6b332ead8b8b'></a>

ArduinoOptaWifi.ino

<a id='89c2685c-b4d9-4a7f-990f-fc7c8eaedb71'></a>

arduino_secrets.h

<a id='348379f3-6437-4d45-99b7-30bfe8ab0fcf'></a>

24

<!-- PAGE BREAK -->

<a id='8e24d866-9532-4a0f-9219-9fef29b16771'></a>

25

<!-- PAGE BREAK -->

<a id='2c3e0620-176d-4d8b-8a96-696fc18376d5'></a>

#define THINGER_SERIAL_DEBUG

<a id='4c7e4eb2-21a2-4bd1-9707-33e36c6d7228'></a>

#include <ThingerMbed.h>
#include <ThingerPortentaOTA.h>
#include "arduino_secrets.h"

<a id='87748d35-1871-4bc4-a40b-3260cbd01378'></a>

ThingerMbed thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);
ThingerPortentaOTA ota(thing);

<a id='c49ecdfa-52ef-4a37-9f26-c9899d38de24'></a>

void setup() {
// open serial for debugging
Serial.begin(115200);
}

<a id='be852785-9411-462b-a854-1561abd3c25f'></a>

```
// configure leds for output
pinMode(LED_D0, OUTPUT);
pinMode(LED_D1, OUTPUT);
pinMode(LED_D2, OUTPUT);
pinMode(LED_D3, OUTPUT);
pinMode(LEDR, OUTPUT);
pinMode(LED_BUILTIN, OUTPUT);
```

<a id='3b5e6d49-ba36-47b6-b6f6-7fae4348581a'></a>

```
// configure relays for output
pinMode (D0, OUTPUT);
pinMode (D1, OUTPUT);
pinMode (D2, OUTPUT);
pinMode (D3, OUTPUT);
```

<a id='e8aa347a-2460-4796-bf03-c5aabdec8e17'></a>

// example for controlling relays and status LED
thing["relay_d0"] << [](pson& in) {
    if(in.is_empty()) {
        in = (bool) digitalRead(D0);
    }else{
        digitalWrite(D0, in? HIGH : LOW);
        digitalWrite(LED_D0, in? HIGH : LOW);
    }
};

<a id='6490ff27-af1f-4bd2-bf57-322f560b0136'></a>

```
thing["relay_d1"] << [] (pson& in){
  if(in.is_empty()){
    in = (bool) digitalRead(D1);
  }else{
    digitalWrite(D1, in ? HIGH : LOW);
    digitalWrite(LED_D1, in ? HIGH : LOW);
  }
};
```

<a id='bfe32285-01f5-4438-b0f2-236954401cd1'></a>

thing["relay_d2"] << [] (pson& in){
if(in.is_empty()){


<a id='2e522097-ae45-4479-8bda-c3fd10b9a2f2'></a>

26

<!-- PAGE BREAK -->

<a id='c2844b47-4b61-4267-bb13-913915be508d'></a>

```
in = (bool) digitalRead (D2);
}else{
    digitalWrite(D2, in? HIGH: LOW);
    digitalWrite(LED_D2, in ? HIGH : LOW);
}
```

<a id='51540ba3-60a9-4833-99fb-09b18c2679d5'></a>

```
};
thing["relay_d3"] << [](pson& in){
  if(in.is_empty()){
    in = (bool) digitalRead(D3);
  }else{
    digitalWrite(D3, in ? HIGH : LOW);
    digitalWrite(LED_D3, in ? HIGH : LOW);
  }
};
```

<a id='1515a5a9-214b-41f3-b79c-8227f177dee6'></a>

// example for controlling the LED
thing["led"] << digitalPin(LED_BUILTIN);
thing["led_r"] << digitalPin(LEDR);

<a id='c8739503-ee81-46ac-bb3e-e73579e0175f'></a>

// resource output example (i.e. reading a sensor value, a
variable, etc)
thing["millis"] >> outputValue(millis());

<a id='bcde49ab-2b09-4097-8e0f-b4f9f7b41a95'></a>

// start thinger on its own task
thing.start();

// more details at http://docs.thinger.io/arduino/

<a id='dce055df-9fd0-48a3-a2e8-1c0c2c6ea27c'></a>

}
void loop() {
// use loop as in normal Arduino Sketch
// use thing.lock() thing.unlock() when using/modifying
variables exposed on thinger resources
delay(1000);


<a id='ae1f365f-1754-4f0c-9ac2-b787d5161110'></a>

option : [x] In case of problems when connecting over secure TLS connections, try updating the WiFi firmware by flashing the WiFiFirmwareUpdater example sketch.

<a id='109aaced-6641-40f2-8134-79017aa0aa46'></a>

<::A menu interface is displayed. The menu has two columns. The left column lists main options, and the right column shows sub-options or actions associated with the selected main option. The 'USBHOST' option in the left column is selected, and its corresponding action 'WiFiFirmwareUpdater' in the right column is highlighted, indicating it is the active selection. The full list of options and their associated actions are:
- STM32H747_System > QSPIFormat
- TFT > QSPIFReadPartitions
- ThreadDebug > STM32H747_getBootloaderinfo
- USB Mass Storage > STM32H747_getResetReason
- USBHID > STM32H747_manageBootloader
- USBHOST > WiFiFirmwareUpdater
- USBLIB
: menu::>

<a id='a55af4f0-264f-46bd-856f-87d3ce129bf5'></a>

27

<!-- PAGE BREAK -->

<a id='a52e260f-e2a5-4b8b-9305-359454538c62'></a>

# Arduino Uno WiFi Rev2

The Arduino Uno WiFi is functionally the same as the Arduino Uno Rev3, but with the addition of WiFi and some other enhancements. It incorporates a brand new 8-bit microprocessor from Microchip and has an onboard IMU (Inertial Measurement Unit). The WiFi Module is a self-contained SoC with an integrated TCP/IP protocol stack that can provide access to a WiFi network or act as an access point.

<a id='3f240e34-7a0d-48ff-8f6c-9fdaca60fb66'></a>

The integration with Thinger.io requires downloading an additional library called "Arduino WiFININA" that allows communicating with the U-BLOX WiFi module.

<a id='04ab3755-8b44-4033-a0be-bccc38a45642'></a>

This example will allow connecting the Arduino Uno WiFi Rev2 device to the cloud platform in a few lines using the WiFi interface. The `arduino_secrets.h` file just needs to be modified with the relevant information.

<a id='5d290c55-7376-4ec5-9aaa-b55708e5291d'></a>

28

<!-- PAGE BREAK -->

<a id='35163c68-d6e2-48e6-bb6e-9b76eef5387d'></a>

ArduinoUnoWiFiRev2.ino arduino_secrets.h

<a id='95e70972-9135-49b2-b70e-4308288c7889'></a>

#define THINGER_SERIAL_DEBUG

#include <ThingerWiFiNINA.h>
#include "arduino_secrets.h"

// cannot connect? Update WiFiNiNA and add iot.thinger.io SSL
Certificate
// https://support.arduino.cc/hc/en-us/articles/360016119219

ThingerWiFiNINA thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // configure LED_BUILTIN for output
  pinMode(LED_BUILTIN, OUTPUT);

  // open serial for debugging
  Serial.begin(115200);

  // configure wifi network
  thing.add_wifi(SSID, SSID_PASSWORD);

  // pin control example (i.e. turning on/off a light, a
  relay, etc)
  thing["led"] << digitalPin(LED_BUILTIN);

  // resource output example (i.e. reading a sensor value, a
  variable, etc)
  thing["millis"] >> outputValue(millis());

  // more details at http://docs.thinger.io/arduino/
}

void loop() {
  thing.handle();
}

<a id='0a024af8-06ed-4276-9116-b9ab9831dd16'></a>

For using this board with he default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='1f49e096-af0c-4041-8786-ea5b65038437'></a>

29

<!-- PAGE BREAK -->

<a id='28d85292-edd1-483b-8fd9-e8a90356977c'></a>

WiFi101 Firmware/Certificates Updater

1. Select port of the WiFi module
If the port is not listed click "Refresh list" button to regenerate the list
/dev/cu.SOC
/dev/cu.MALS
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1442211
/dev/cu.usbmodem1442311
Refresh list
Test connection

2. Update firmware
Select the firmware from the dropdown box below
option WINC1501 Model B (19.5.2): [x]
Update Firmware

3. Update SSL root certificates
Add domains in the list below using "Add domain" button
arduino.cc:443
thinger.io:443
Add domain
Remove domain (inactive)
Upload Certificates to WiFi module

<a id='15941c78-b577-4520-8e5b-d9cf70cbf703'></a>

Previous
ARDUINO ETHERNET

Next
ARDUINO GSM

<a id='2a85d70d-8bbf-4083-8386-6d8c5755f5a5'></a>

Last updated 5 months ago

<a id='8bd54375-d81c-498b-837a-804de2c645ae'></a>

Was this helpful?

option happy_face: [ ]
option neutral_face: [ ]
option sad_face: [ ]

<a id='69686725-ba9c-4665-a2cd-64afa23a9bac'></a>

<::Three icons: a sun, a computer monitor with a light gray background (indicating selection), and a crescent moon.: figure::>

<a id='ac329e5e-dbd3-48c2-a6cf-f98e3a364a07'></a>

30