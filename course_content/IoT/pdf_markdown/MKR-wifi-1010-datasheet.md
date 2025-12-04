<a id='2ad38ad7-6fe1-406c-931b-263b4696f291'></a>

<::logo: Arduino
None
A teal infinity symbol is combined with a plus sign and a minus sign, forming a stylized logo.:>

<a id='68df26c6-3ee4-4009-bbda-9111d84669b2'></a>

Arduino® MKR WiFi 1010

<a id='931867a4-c94f-46be-9b40-57cc727c8443'></a>

User Manual
SKU: ABX00023

<a id='6c431ce3-cbde-48f9-9b43-de4d0f79793f'></a>

<::An overhead view of a blue Arduino MKR WiFi 1010 development board. The board is rectangular with rounded corners and features numerous electronic components. On the left side, there is a micro-USB port and a label "ON" near the top left corner, and "CHRG" near the bottom left corner. A white connector with multiple pins is located above the micro-USB port. In the center, a large square Atmel microcontroller chip is visible with the text "ATMEL SAMD21G18A". To its right, a white push button labeled "RST" is present. Towards the right side of the board, there is a u-blox module with a QR code and text "000-00-1B26 MODEL: NINA-W102" and a red "blox" logo. Above this module, the text "ARDUINO.CC" is printed. Below the module, "MKR WIFI 1010" is visible. The board has two long rows of black female pin headers running along its top and bottom edges. Various surface-mount components, such as resistors, capacitors, and integrated circuits, are distributed across the board. A prominent dark gray inductor labeled "2R2" is located near the top center.: electronic board::>

<a id='15af1d37-6d67-405a-83ee-70f1c7259c05'></a>

## Description
The Arduino® MKR WiFi 1010 is a miniature sized module containing a SAMD21G18A Processor, the Nina W102 Module and a crypto chip (the ATECC508).

<a id='51aabf34-403c-4059-8670-02cb3d014642'></a>

Target Areas
Prototyping, IoT application examples

<a id='b6787419-711a-418e-b9fa-b768759dd0c4'></a>

1/16

<a id='b78b812b-eea4-47ce-946f-d5d344dafa29'></a>

Arduino® MKR WiFi 1010

<a id='ad384664-9f8b-429b-a4f6-3e18b8ad9ce5'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='24bbdb8e-cc2a-4eee-ba27-ec36b10d0046'></a>



<a id='6d99c086-6dfe-4126-adb8-1d4095ca01de'></a>

Arduino® MKR WiFi 1010

<a id='3db4b92b-4ed9-4fec-90ea-6cb2881b74e1'></a>

## Features

- SAMD21G18A
  - Processor
    - Arm® Cortex®-M0+ at up to 48 MHz
    - 256 kB Flash
    - 32 KB SRAM
    - Power On Reset (POR) and Brown Out Detection (BOD)
  - Peripherals
    - 12 channel DMA
    - 12 channel event system
    - 5x 16 bit Timer/Counter
    - 3x 24 bit timer/counter with extended functions
    - 32 bit RTC
    - Watchdog Timer
    - CRC-32 generator
    - Full speed Host/Device USB with 8 end points
    - 6x SERCOM (USART, I2C, SPI, LIN)
    - Two channel I2S
    - 12 bit 350ksps ADC (up to 16 bit with oversampling)
    - 10 bit 350ksps DAC
    - External Interrupt Controller (up to 16 lines)
- ATECC508 Crypto Chip
  - Cryptographic co-processor with secure hardware based key storage
  - Protected storage for up to 16 keys, certificates or data
  - ECDH: FIPS SP800-56A Elliptic Curve Diffie-Hellman
  - ECDSA: FIPS186-3 Elliptic Curve Digital Signature Algorithm
  - NIST standard P256 elliptic curve support
  - SHA-256 & HMAC hash including off-chip context save/restore

<a id='6169dc8f-63c5-417e-aa37-390cdfa74b65'></a>

2 / 16

<a id='b1e72d8a-aefb-4534-bdf2-b95ee8298d37'></a>

Arduino® MKR WiFi 1010

<a id='a6aeffc4-8083-451f-87c9-0a283f24f28c'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='5529e94a-93b8-4c14-bc2b-0f95a8c7562e'></a>



<a id='35ce9272-4042-42fd-b776-dfad1709948e'></a>

Arduino® MKR WiFi 1010

<a id='54bff8c9-e158-4695-a250-4425431e5153'></a>

* Nina W102 Module
    * Dual Core Tensilica LX6 CPU at up to 240MHz
    * Wi-Fi®
        * IEEE 802.11b up to 11Mbit
        * IEEE 802.11g up to 54MBit
        * IEEE 802.11n up to 72MBit
        * 2.4 GHz, 13 channels
        * 96 dBm sensitivity
* Bluetooth® BR/EDR
    * Max 7 Clients
    * 2.4 GHz, 79 channels
    * Up to 3 Mbit/s
    * -88 dBm sensitivity
    * Bluetooth® Low Energy
    * Bluetooth® 5.0 dual mode
    * 2.4GHz 40 channels
    * -88 dBm sensitivity
    * Up to 1 Mbit/s
* BQ24125L I2C Controlled USB/Adapter Charger
    * 92% Charge Efficiency at 2 A, 90% at 4 A
    * Autonomous Battery Charging
    * 2.5-A Fast Charging

<a id='a43cb833-aef5-455b-902f-75ae5cc458bb'></a>

3 / 16

<a id='844e6328-d1d9-445d-80a9-0a6713ab0edf'></a>

Arduino® MKR WiFi 1010

<a id='387e55a1-eba5-48b4-a5a0-8c242ec22369'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='11d2b24e-4322-42ef-a803-db1f31e7b230'></a>

<::logo: Arduino
No text present
A teal infinity symbol is combined with a plus sign, forming a stylized "A" shape.::>

<a id='9935533e-cf5b-45dc-acda-a817f2616478'></a>

Arduino MKR WiFi 1010

<a id='07ccf241-6cec-46a9-adbf-c45516300363'></a>

# Contents

1 The Board
    1.1 Application Examples
2 Ratings
    2.1 Recommended Operating Conditions
    2.2 Power Consumption
3 Functional Overview
    3.1 Processor
    3.2 Wi-Fi® Module
    3.3 Wi-Fi®/Bluetooth® Communication Module
    3.4 Crypto Chips
    3.5 Power Tree
4 Board Operation
    4.1 Getting Started - IDE
    4.2 Getting Started - Arduino Cloud Editor
    4.3 Getting Started - Arduino Cloud
    4.4 Arduino Forum
    4.5 Online Resources
    4.6 Board Recovery
5 Connector Pinouts
    5.1 USB
    5.2 Headers
    5.3 Debug
6 Mechanical Information
    6.1 Board Outline
    6.2 Mounting Holes
    6.3 Connector Positions
7 Certifications
    7.1 Declaration of Conformity CE DoC (EU)
    7.2 Declaration of Conformity to EU RoHS & REACH 211 01/19/2021
    7.3 Conflict Minerals Declaration
    7.4 FCC Caution
8 Company Information
9 Reference Documentation


6
6
6
6
7
7
7
8
8
8
8
9
9
9
9
9
9
9
10
10
10
11
11
11
12
12
13
13
13
14
14
15
15

<a id='0780f183-7927-494c-b51b-c820e6d01206'></a>

4 / 16

<a id='76a46a53-a5b1-4443-b711-153b80cc9d67'></a>

Arduino® MKR WiFi 1010

<a id='56606510-20af-43f5-a8f8-b794e540ca01'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='54d99972-0aac-4f1d-a60f-b2a0663043d4'></a>

<::logo: Arduino
A teal infinity symbol with a plus sign on the right side.::>

<a id='b254bb02-766e-497a-830f-efa271f165c8'></a>

Arduino® MKR WiFi 1010

<a id='5ede792a-e30b-443e-9730-dbb9e807f0eb'></a>

10 Revision History

<a id='b6660674-aa36-47c1-91ba-f86026ece11b'></a>

16

<a id='4f4f391e-b228-4e83-b3a4-578c7621d1f5'></a>

5 / 16

<a id='41b37936-0fc5-4bff-b10e-92542e952331'></a>

Arduino® MKR WiFi 1010

<a id='547e39a0-3388-48fe-8b9c-2f07a54c3ea4'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='89c7e229-e9e4-40c5-b0a2-01aa43facdfc'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='22a7e4af-00cc-42c7-9434-8a92fa7e227d'></a>

Arduino® MKR WiFi 1010

<a id='8eacf2fa-52d0-4dd9-ae92-32a621a2776c'></a>

## 1 The Board
Like most Arduino MKR form factor boards the MKR WiFi 1010 can be powered via USB, via headers or connecting a Lithium or Lithium Polymer battery to the embedded battery charger (the BQ24195L).

<a id='303ac56a-4161-48a8-afc8-29668aab7a93'></a>

NOTE: MKR WiFi 1010 battery charger has a minimum of 512 mA charge current. Please ensure this charging is compatible with the battery you will be using.

<a id='12619cb3-f556-472c-b4f8-da5336d65d77'></a>

NOTE: MKR WiFi 1010 only supports 3.3 V I/Os and is NOT 5 V tolerant.

<a id='a0e1eff5-b58f-40d2-b426-ff9f290a968f'></a>

Please make sure you are not directly connecting 5 V signals to this board, or it will be damaged.

<a id='1f38d9df-53c5-4363-b9d8-36258d38945b'></a>

Also the 5V pin does NOT supply voltage but is rather connected, through a jumper, to the USB power input.

<a id='735b977c-8638-490c-a099-d6011fb4c7ca'></a>

## 1.1 Application Examples

**Bluetooth®:** The communications chipset on the MKR WiFi 1010 is something pretty unique in the world of microcontroller platforms, since this can be both a Bluetooth® LE and Bluetooth® client and host device.

<a id='928fcc08-8733-4662-a9d9-26ede4dab6c3'></a>

Wi-Fi®: The Wi-Fi® connectivity is performed with a module from u-blox®, the NINA-W10, a low power chipset operating in the 2.4GHz range.

<a id='c6319634-158a-4d70-966b-e6d9890ae884'></a>

IoT: Whether you are looking at building a sensor network connected to your office or home router, or if you want to create a BLE device sending data to a cell phone, the MKR WiFi 1010 is your one-stop-solution for many of the basic IoT application scenarios.

<a id='71b73a0e-e972-4cb2-88f6-520dfb40c1be'></a>

2 Ratings
\
2.1 Recommended Operating Conditions
\
<table id="5-1">
<tr><td id="5-2">Symbol</td><td id="5-3">Description</td><td id="5-4">Min</td><td id="5-5">Max</td></tr>
<tr><td id="5-6"></td><td id="5-7">Conservative thermal limits for the whole board:</td><td id="5-8">-40 °C</td><td id="5-9">85 °C</td></tr>
</table>

<a id='01d1bd4c-4d7e-41ca-bb6b-5fd5d3a4973b'></a>

6 / 16

<a id='ec7c1586-dee5-49ae-9f00-74a0debcf941'></a>

Arduino® MKR WiFi 1010

<a id='13b76f59-2021-4d7a-a0a4-6c52eba22629'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='bf5df314-9e8e-4070-b557-65c6a2c3b553'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='5f871c12-e38c-473d-a07e-d1c58daf5df6'></a>

Arduino® MKR WiFi 1010

<a id='1fc78b9c-6631-4ca1-bc80-b5fa186312a6'></a>

2.2 Power Consumption
<table id="6-1">
<tr><td id="6-2">Symbol</td><td id="6-3">Description</td><td id="6-4">Min</td><td id="6-5">Typ</td><td id="6-6">Max</td><td id="6-7">Unit</td></tr>
<tr><td id="6-8">$VIN_{Max}$</td><td id="6-9">Maximum input voltage from VIN pad</td><td id="6-a">-0.3</td><td id="6-b"></td><td id="6-c">5.5</td><td id="6-d">V</td></tr>
<tr><td id="6-e">$VUSB_{Max}$</td><td id="6-f">Maximum input voltage from USB connector</td><td id="6-g">-0.3</td><td id="6-h"></td><td id="6-i">5.5</td><td id="6-j">V</td></tr>
<tr><td id="6-k">$P_{Max}$</td><td id="6-l">Maximum power consumption</td><td id="6-m"></td><td id="6-n"></td><td id="6-o">TBC</td><td id="6-p">mW</td></tr>
</table>

<a id='4a1643a0-4d88-4869-ab49-eb9a97a2ed77'></a>

## 3 Functional Overview

<a id='494808da-3a0b-4688-b5ac-5469e094de39'></a>

## 3.1 Processor
The Main Processor is a Arm® Cortex®-M0+ running at up to 48 MHz.

<a id='4100ed2a-4eb6-44ba-90f0-e0472d4932c3'></a>

Most of its pins are connected to the external headers, however some are reserved for internal communication to the communication module and to the internal SPI and I2C peripherals (Crypto). Communication with NINA Module W102 happens through UART and SPI through the following pins.

<a id='10e2db3b-befb-4d05-b893-9b5ace3e9d7e'></a>

<table id="6-q">
<tr><td id="6-r">Pin</td><td id="6-s">Acronym</td><td id="6-t">NINA Pin</td><td id="6-u">Acronym</td><td id="6-v">Description</td></tr>
<tr><td id="6-w">21</td><td id="6-x">PA12</td><td id="6-y">36</td><td id="6-z">GPIO12</td><td id="6-A">SPI MOSI</td></tr>
<tr><td id="6-B">22</td><td id="6-C">PA13</td><td id="6-D">21</td><td id="6-E">SPIV_DI</td><td id="6-F">NINA_MISO</td></tr>
<tr><td id="6-G">23</td><td id="6-H">PA14</td><td id="6-I">28</td><td id="6-J">SPIV_CS</td><td id="6-K">SPI CS</td></tr>
<tr><td id="6-L">24</td><td id="6-M">PA15</td><td id="6-N">29</td><td id="6-O">SPIV_CLK</td><td id="6-P">SPI CLK</td></tr>
<tr><td id="6-Q">39</td><td id="6-R">PA27</td><td id="6-S">27</td><td id="6-T">GPIOO</td><td id="6-U">NINA_GPIOO</td></tr>
<tr><td id="6-V">7</td><td id="6-W">PB08</td><td id="6-X">19</td><td id="6-Y">RESET</td><td id="6-Z">NINA RESET</td></tr>
<tr><td id="6-10">41</td><td id="6-11">PA28</td><td id="6-12">7</td><td id="6-13">GPIO_33</td><td id="6-14">NINA_ACK</td></tr>
<tr><td id="6-15">23</td><td id="6-16">PA14</td><td id="6-17">21</td><td id="6-18">UART_CTS</td><td id="6-19">NINA_CS</td></tr>
<tr><td id="6-1a">24</td><td id="6-1b">PA15</td><td id="6-1c">20</td><td id="6-1d">UART_CTS</td><td id="6-1e">NINA_SCK</td></tr>
<tr><td id="6-1f">38</td><td id="6-1g">PB23</td><td id="6-1h">22</td><td id="6-1i">UART_RXD</td><td id="6-1j">Serial1_RX</td></tr>
<tr><td id="6-1k">37</td><td id="6-1l">PA22</td><td id="6-1m">23</td><td id="6-1n">UART_TXD</td><td id="6-1o">Serial1_TX</td></tr>
</table>

<a id='11b37c77-01aa-40d8-83d8-770ce33455a4'></a>

7 / 16

<a id='82b70c2e-f065-4318-b936-4b9f7f79acbd'></a>

Arduino® MKR WiFi 1010

<a id='a952d87f-d6db-484c-9bd9-15c808497640'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='1ce2326c-dd2f-491b-b768-8bf193c694f7'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='4757d89d-78f0-40ac-91d3-7c89b6391e01'></a>

Arduino® MKR WiFi 1010

<a id='9149d2d0-8316-4204-9fa2-d3c58a2a95e6'></a>

3.2 Wi-Fi® Module

3.3 Wi-Fi®/Bluetooth® Communication Module

<a id='a2ae7a3e-c4a7-4765-86ab-ee8772c66d22'></a>

Nina W102 is based on ESP32 and is delivered with a pre-certified software stack from Arduino. Source code for the firmware is available [1].

<a id='fbea2c84-17f7-4ccf-a397-dced14b42cc6'></a>

NOTE: Reprogramming the wireless module's firmware with a custom one will invalidate compliance with radio standards as certified by Arduino, hence this is not recommended unless the application is used in private laboratories far from other electronic equipment and people. Usage of custom firmware on radio modules is the sole responsibility of the user.

<a id='80aeecab-efd2-4197-96e2-7137bacfcdc7'></a>

3.4 Crypto Chips

The crypto chip in Arduino IoT boards is what makes the difference with other less secure boards as it provides a secure way to store secrets such as certificates and it also allows accelerating secure protocols while never exposing secrets in plain text.

<a id='426631a3-b699-4aa5-a423-f31536a2f924'></a>

3.5 Power Tree <::flowchart:Inputs: - V USB (MOSFET) - VIN (DIODE) Both inputs connect to V CHRG. From V CHRG, power flows to 3V8 (BQ24195L). From 3V8, power flows to 3V3 (LDO, 600mA). From 3V3, power splits to: - SAMD21G18 (30mA) - NINA W102 (320mA) - ECC508 (16mA) - User application (600mA) Legend: - Component: (represented by a white rectangle) - Power Rail: (represented by a red outlined rectangle) - Power I/O: (represented by a grey circle) - Max Current: (represented by a red circle) - Conversion Type: (represented by a teal circle): flowchart::> MKR WiFi 1010 Power Tree

<a id='bb2f6a87-362e-46bb-807c-8b76b762d68f'></a>

8 / 16

<a id='fdd1d170-89e5-4cff-96b3-c2a5973ef091'></a>

Arduino® MKR WiFi 1010

<a id='f48c5407-c760-4896-bfbf-9adde4a7dbef'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='ccd85fdc-055b-4517-a899-96bd804a7c20'></a>



<a id='decfd539-2406-4958-ac7b-d3ef2025d31e'></a>

Arduino® MKR WiFi 1010

<a id='f87e246e-50a0-4280-8bda-d301ce22d2af'></a>

# 4 Board Operation

## 4.1 Getting Started - IDE

If you want to program your MKR WiFi 1010 while offline you need to install the Arduino Desktop IDE [2] To connect the MKR WiFi 1010 to your computer, you'll need a micro-B USB cable. This also provides power to the board, as indicated by the LED.

<a id='b2783604-b802-4e7f-b407-c3f97eb742ff'></a>

4.2 Getting Started - Arduino Cloud Editor

<a id='7819052d-919a-467e-85d1-d094bd92de8a'></a>

All Arduino boards, including this one, work out-of-the-box on the Arduino Cloud Editor [3], by just installing a simple plugin.

<a id='02f687ad-3960-495a-94a8-f3538333089d'></a>

The Arduino Cloud Editor is hosted online, therefore it will always be up-to-date with the latest features and support for all boards. Follow [4] to start coding on the browser and upload your sketches onto your board.

<a id='f886daec-67cd-43af-8a3d-c51991c8bc55'></a>

4.3 Getting Started - Arduino Cloud

<a id='f4abd87a-6284-42b6-a98a-86fe79af42cb'></a>

All Arduino IoT enabled products are supported on Arduino Cloud which allows you to Log, graph and analyze sensor data, trigger events, and automate your home or business.

<a id='3b46a0d2-55e1-463c-98b6-c4a0c258d021'></a>

4.4 Arduino Forum

<a id='ffda6fe5-63c3-47cd-a711-19239105a893'></a>

Discussions and ideas for the MKR WiFi 1010 can be found in the Arduino Forum [5].

<a id='5fbcbdc7-2731-4932-8311-8012ac59ccdb'></a>

## 4.5 Online Resources
Now that you have gone through the basics of what you can do with the board you can explore the endless possibilities it provides by checking exciting projects on Arduino Project Hub [6], the Arduino Library Reference [7] and the online store [8] where you will be able to complement your board with sensors, actuators and more.

<a id='57fa30d1-d95a-4b1a-82a5-69624b768d65'></a>

## 4.6 Board Recovery

All Arduino boards have a built-in bootloader which allows flashing the board via USB. In case a sketch locks up the processor and the board is not reachable anymore via USB it is possible to enter bootloader mode by double-tapping the reset button right after power up.

<a id='28237e65-95c9-4a7f-ad5a-9247ac4f8df1'></a>

9 / 16

<a id='abde6b5e-bade-4665-9992-7d61f421adad'></a>

Arduino® MKR WiFi 1010

<a id='042918fa-7e8f-4b6f-ad5e-97104dcd6d26'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='7c0336d4-ba0f-4543-b6b0-a2f225cb31cc'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='341bd3f8-ed97-4c32-8906-84e29ef006cd'></a>

Arduino® MKR WiFi 1010

<a id='ca124b68-cfe9-41c1-bf7f-89706ea2f0fd'></a>

5 Connector Pinouts

<a id='8a8f328c-130e-437b-9915-e723d99e2fa6'></a>

5.1 USB
<table id="9-1">
<tr><td id="9-2">Pin</td><td id="9-3">Function</td><td id="9-4">Type</td><td id="9-5">Description</td></tr>
<tr><td id="9-6">1</td><td id="9-7">VUSB</td><td id="9-8">Power</td><td id="9-9">Power Supply Input. Output is powered via VUSB from header</td></tr>
<tr><td id="9-a">2</td><td id="9-b">D-</td><td id="9-c">Differential</td><td id="9-d">USB differential data -</td></tr>
<tr><td id="9-e">3</td><td id="9-f">D+</td><td id="9-g">Differential</td><td id="9-h">USB differential data +</td></tr>
<tr><td id="9-i">4</td><td id="9-j">ID</td><td id="9-k">Analog</td><td id="9-l">Selects Host/Device functionality</td></tr>
<tr><td id="9-m">5</td><td id="9-n">GND</td><td id="9-o">Power</td><td id="9-p">Supply Ground</td></tr>
</table>

<a id='271c4a86-16e5-423b-ab23-6a9b536ab8bc'></a>

NOTE: This board can support USB host mode only if powered via the VUSB pin and if the jumper close to the VUSB pin is shorted.

<a id='c1fb7ce4-ea2b-4207-ab73-25256b06c9d3'></a>

5.2 Headers

<a id='6de7e03a-1bbe-4d31-bfd1-13841cccee58'></a>

Board exposes two 28 pin connectors assembled with pin headers.
<table id="9-q">
<tr><td id="9-r">Pin</td><td id="9-s">Function</td><td id="9-t">Type</td><td id="9-u">Description</td></tr>
<tr><td id="9-v">1</td><td id="9-w">AREF</td><td id="9-x">Analog</td><td id="9-y">Analog Reference.</td></tr>
<tr><td id="9-z">2</td><td id="9-A">A0/DACO</td><td id="9-B">Analog</td><td id="9-C">ADC in/DAC out, Can be used as GPIO</td></tr>
<tr><td id="9-D">3</td><td id="9-E">A1</td><td id="9-F">Analog</td><td id="9-G">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-H">4</td><td id="9-I">A2</td><td id="9-J">Analog</td><td id="9-K">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-L">5</td><td id="9-M">A3</td><td id="9-N">Analog</td><td id="9-O">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-P">6</td><td id="9-Q">A4/SDA</td><td id="9-R">Analog</td><td id="9-S">ADC in, I2C SDA, Can be used as GPIO</td></tr>
<tr><td id="9-T">7</td><td id="9-U">A5/SCL</td><td id="9-V">Analog</td><td id="9-W">ADC in, I2C SCL, Can be used as GPIO</td></tr>
<tr><td id="9-X">8</td><td id="9-Y">A6</td><td id="9-Z">Analog</td><td id="9-10">ADC in, Can be used as GPIO</td></tr>
<tr><td id="9-11">9</td><td id="9-12">D0</td><td id="9-13">Digital</td><td id="9-14">GPIO, can be used as PWM</td></tr>
<tr><td id="9-15">10</td><td id="9-16">D1</td><td id="9-17"></td><td id="9-18">GPIO, can be used as PWM</td></tr>
<tr><td id="9-19">11</td><td id="9-1a">D2/PWM</td><td id="9-1b">Digital</td><td id="9-1c">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1d">12</td><td id="9-1e">D3/PWM</td><td id="9-1f">Digital</td><td id="9-1g">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1h">13</td><td id="9-1i">D4/PWM</td><td id="9-1j">Digital</td><td id="9-1k">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1l">14</td><td id="9-1m">D5/PWM</td><td id="9-1n">Digital</td><td id="9-1o">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1p">15</td><td id="9-1q">D6</td><td id="9-1r">Digital</td><td id="9-1s">GPIO, can be used as PWM</td></tr>
<tr><td id="9-1t">16</td><td id="9-1u">D7</td><td id="9-1v">Digital</td><td id="9-1w">GPIO can be used as PWM</td></tr>
<tr><td id="9-1x">17</td><td id="9-1y">D8/MOSI</td><td id="9-1z">Digital</td><td id="9-1A">SPI MOSI, can be used as GPIO, can be used as PWM</td></tr>
<tr><td id="9-1B">18</td><td id="9-1C">D9/SCK</td><td id="9-1D">Digital</td><td id="9-1E">SPI SCK, can be used as GPIO, can be used as PWM</td></tr>
<tr><td id="9-1F">19</td><td id="9-1G">D10/MISO</td><td id="9-1H">Digital</td><td id="9-1I">SPI MISO, can be used as GPIO</td></tr>
<tr><td id="9-1J">20</td><td id="9-1K">D11/SDA</td><td id="9-1L">Digital</td><td id="9-1M">I2C SDA, can be used as GPIO</td></tr>
<tr><td id="9-1N">21</td><td id="9-1O">D12/SCL</td><td id="9-1P">Digital</td><td id="9-1Q">I2C SCL, can be used as GPIO</td></tr>
<tr><td id="9-1R">22</td><td id="9-1S">D13/RX</td><td id="9-1T">Digital</td><td id="9-1U">USART RX, can be used as GPIO</td></tr>
<tr><td id="9-1V">23</td><td id="9-1W">D14/TX</td><td id="9-1X">Digital</td><td id="9-1Y">USART TX, can be used as GPIO</td></tr>
<tr><td id="9-1Z">24</td><td id="9-20">RESETN</td><td id="9-21">Digital</td><td id="9-22">Reset input</td></tr>
<tr><td id="9-23">25</td><td id="9-24">GND</td><td id="9-25">Power</td><td id="9-26">Power Ground</td></tr>
<tr><td id="9-27">26</td><td id="9-28">+3V3</td><td id="9-29">Power Out</td><td id="9-2a"></td></tr>
</table>

<a id='d44687f5-c075-4086-a293-3d0e5258f41f'></a>

10 / 16

<a id='f69acb5b-163a-4343-95cd-aaa21cc9d194'></a>

Arduino® MKR WiFi 1010

<a id='bad0f957-88ee-4b77-ab0d-f8ee1d265af2'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='ae637989-65f3-4a3e-8645-57c87e385ba2'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='b758a97f-c338-4991-b2aa-e945cf47b1f3'></a>

Arduino® MKR WiFi 1010

<a id='49184ae0-d6ae-412e-af34-48155de9ba5d'></a>

<table id="10-1">
<tr><td id="10-2">Pin</td><td id="10-3">Function</td><td id="10-4">Type</td><td id="10-5">Description</td></tr>
<tr><td id="10-6">27</td><td id="10-7">VIN</td><td id="10-8">Power In</td><td id="10-9">Vin Power input</td></tr>
<tr><td id="10-a">28</td><td id="10-b">+5V</td><td id="10-c">Power Out</td><td id="10-d"></td></tr>
</table>

<a id='e69124bb-b048-44ee-9f01-6a3a48466c93'></a>

5.3 Debug
<table id="10-e">
<tr><td id="10-f">Pin</td><td id="10-g">Function</td><td id="10-h">Type</td><td id="10-i">Description</td></tr>
<tr><td id="10-j">1</td><td id="10-k">+3V3</td><td id="10-l">Power Out</td><td id="10-m"></td></tr>
<tr><td id="10-n">2</td><td id="10-o">SWD</td><td id="10-p">Digital</td><td id="10-q">Single Wire Debug Data</td></tr>
<tr><td id="10-r">3</td><td id="10-s">RESETN</td><td id="10-t">Digital In</td><td id="10-u">Processor Reset</td></tr>
<tr><td id="10-v">4</td><td id="10-w">SWCLK</td><td id="10-x">Digital In</td><td id="10-y">Single Wire Debug Clock</td></tr>
<tr><td id="10-z">5</td><td id="10-A">GND</td><td id="10-B">Power</td><td id="10-C"></td></tr>
</table>

<a id='68c8a114-73f2-4d06-a1da-de42accb5965'></a>

## 6 Mechanical Information

Board measures are mixed between metric and imperial. Metric measures are used to maintain 100 mil pitch grid between pin rows to allow them to fit in a breadboard.

<a id='7e9ac750-3c20-4978-ac55-a35d2d11cecc'></a>

6.1 Board Outline
<::technical drawing
: An outline diagram of the MKR WiFi 1010 board, showing its dimensions. The board has a width of 61.50mm [2421mil] and a height of 25.00mm [984mil]. Various components are indicated in outline, including a USB port on the left, a large central chip, and pin headers along the top and bottom edges. A component is labeled "3R3".
MKR WiFi 1010 Board Outline::>

<a id='4da56f08-b100-4bbc-9dc6-8627c563c141'></a>

11 / 16

<a id='e452d0dc-aff5-418f-8399-ba615b9d26d3'></a>

Arduino® MKR WiFi 1010

<a id='83b6581a-d435-4a95-8a16-b70802b0a4b9'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='98b87e08-99ba-4bde-aeba-875285d6d4be'></a>



<a id='cf083e04-b06c-4759-af2d-153d8098bd86'></a>

Arduino® MKR WiFi 1010

<a id='bb06f055-e02c-44aa-996b-5bb3dd2b100c'></a>

6.2 Mounting Holes

<a id='b7fc8f79-7c59-4940-8f0d-673055a3b89c'></a>

<::A diagram of the MKR WiFi 1010 circuit board, viewed from the top, showing its layout and mounting hole dimensions. The board has a rectangular shape with rounded corners, and various electronic components are depicted on its surface. There are four circular mounting holes, one in each corner. Dimensions are indicated for the mounting holes: - The diameter of a mounting hole is Ø2.25mm ([Ø89mil]), as shown for the top-left hole. - The distance from the top edge to the center of the top-right mounting hole is 2.31mm ([91mil]). - The distance from the right edge to the center of the top-right mounting hole is 2.31mm ([91mil]). Other visible labels include "3R3" and "FD2". MKR WiFi 1010 Mounting Holes: diagram::>

<a id='832cd464-2fa5-4ded-a510-b1955ab11da1'></a>

6.3 Connector Positions<::diagram: A technical diagram of the MKR WiFi 1010 board showing connector positions and dimensions. The board is rectangular with rounded corners. Key connectors and components are labeled:
- J1 is on the left side.
- J4 is on the top left.
- JDIGITAL is a long connector along the top edge.
- J7 is near the center, below J4.
- JANALOG is a long connector along the bottom edge.

Dimensions are indicated with arrows and numerical values:
- Vertical dimension on the left for J1: [490mil] 12.44mm
- Horizontal dimension from the left edge to J4: [374mil] 9.50mm
- Horizontal dimension from the left edge to the right edge of JDIGITAL: [1513mil] 38.43mm
- Vertical dimension on the right for JDIGITAL: [96mil] 2.44mm
- Horizontal dimension from the left edge to J7: [611mil] 15.51mm

Other smaller labels include D3, PB1, Q2, D2, and various small component outlines.::>MKR WiFi 1010 Connector Positions

<a id='8013feaf-affe-4725-b776-cd1bd218c70d'></a>

12 / 16

<a id='b28afc04-6154-4353-8fca-4a9dc4c950bd'></a>

Arduino® MKR WiFi 1010

<a id='37be4213-24f6-4a1b-8e5d-42129df5934e'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='73ca83cc-81ff-4355-bd1c-21c89487404c'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='928b4337-c889-4f05-a3bb-c6016c8e68de'></a>

Arduino® MKR WiFi 1010

<a id='b7737c8d-ae44-41a6-9ebb-ef98ef397fe3'></a>

7 Certifications

<a id='22200e15-92a3-4e91-93c8-67eeffc518aa'></a>

## 7.1 Declaration of Conformity CE DoC (EU)

We declare under our sole responsibility that the products above are in conformity with the essential requirements of the following EU Directives and therefore qualify for free movement within markets comprising the European Union (EU) and European Economic Area (EEA).

<a id='7e67372b-84d5-4db9-babc-45ac0f590768'></a>

ROHS 2 Directive 2011/65/EU Conforms to: EN50581:2012
Directive 2014/35/EU. (LVD) Conforms to: EN 60950-1:2006/A11:2009/A1:2010/A12:2011/AC:2011

<a id='a68f1d1d-687c-42ee-b8d2-9b37941c14cb'></a>

Directive 2004/40/EC & 2008/46/EC & 2013/35/EU, EMF Conforms to: EN 62311:2008

<a id='ee61da77-7616-49bf-8dff-717203e9bf75'></a>

7.2 Declaration of Conformity to EU RoHS & REACH 211 01/19/2021

<a id='208c6c21-5404-42f6-b18f-e02e99a4494c'></a>

Arduino boards are in compliance with RoHS 2 Directive 2011/65/EU of the European Parliament and RoHS 3 Directive 2015/863/EU of the Council of 4 June 2015 on the restriction of the use of certain hazardous substances in electrical and electronic equipment.

<a id='067bb7f6-70f2-4ff1-91bc-6f234349e1b6'></a>

<table id="12-1">
<tr><td id="12-2">Substance</td><td id="12-3">Maximum Limit (ppm)</td></tr>
<tr><td id="12-4">Lead (Pb)</td><td id="12-5">1000</td></tr>
<tr><td id="12-6">Cadmium (Cd)</td><td id="12-7">100</td></tr>
<tr><td id="12-8">Mercury (Hg)</td><td id="12-9">1000</td></tr>
<tr><td id="12-a">Hexavalent Chromium (Cr6+)</td><td id="12-b">1000</td></tr>
<tr><td id="12-c">Poly Brominated Biphenyls (PBB)</td><td id="12-d">1000</td></tr>
<tr><td id="12-e">Poly Brominated Diphenyl ethers (PBDE)</td><td id="12-f">1000</td></tr>
<tr><td id="12-g">Bis(2-Ethylhexyl) phthalate (DEHP)</td><td id="12-h">1000</td></tr>
<tr><td id="12-i">Benzyl butyl phthalate (BBP)</td><td id="12-j">1000</td></tr>
<tr><td id="12-k">Dibutyl phthalate (DBP)</td><td id="12-l">1000</td></tr>
<tr><td id="12-m">Diisobutyl phthalate (DIBP)</td><td id="12-n">1000</td></tr>
</table>

<a id='ce264e66-6a50-4be7-be7b-141471ff567f'></a>

Exemptions : No exemptions are claimed.

<a id='785cda5e-a9fc-4dd3-a7d4-dd8f290cecb5'></a>

Arduino Boards are fully compliant with the related requirements of European Union Regulation (EC) 1907/2006 concerning the Registration, Evaluation, Authorization and Restriction of Chemicals (REACH). We declare none of the SVHCs (https://echa.europa.eu/web/guest/candidate-list-table), the Candidate List of Substances of Very High Concern for authorization currently released by ECHA, is present in all products (and also package) in quantities totaling in a concentration equal or above 0.1%. To the best of our knowledge, we also declare that our products do not contain any of the substances listed on the "Authorization List" (Annex XIV of the REACH regulations) and Substances of Very High Concern (SVHC) in any significant amounts as specified by the Annex XVII of Candidate list published by ECHA (European Chemical Agency) 1907/2006/EC.

<a id='36b8b2af-c349-4373-aee9-99a2db6e5e87'></a>

13 / 16

<a id='9e3ff553-3dee-4bf7-9e6c-7d9f9e1315f2'></a>

Arduino® MKR WiFi 1010

<a id='b275db21-e4b0-408c-b0c0-f0221a742bef'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='3b9a46dc-65c3-443d-9393-662a0332e832'></a>



<a id='190a62bc-e0bf-4386-bc34-5079d204562c'></a>

Arduino® MKR WiFi 1010

<a id='4555fe70-cc00-46d9-b611-b1b99a0914f8'></a>

## 7.3 Conflict Minerals Declaration

As a global supplier of electronic and electrical components, Arduino is aware of our obligations with regards to laws and regulations regarding Conflict Minerals, specifically the Dodd-Frank Wall Street Reform and Consumer Protection Act, Section 1502. Arduino does not directly source or process conflict minerals such as Tin, Tantalum, Tungsten, or Gold. Conflict minerals are contained in our products in the form of solder, or as a component in metal alloys. As part of our reasonable due diligence Arduino has contacted component suppliers within our supply chain to verify their continued compliance with the regulations. Based on the information received thus far we declare that our products contain Conflict Minerals sourced from conflict-free areas.

<a id='4cb2acea-131f-46c4-a67a-65a598955c82'></a>

7.4 FCC Caution

Any Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions:
1. This device may not cause harmful interference
2. This device must accept any interference received, including interference that may cause undesired operation.

<a id='07b979a3-9f3e-4462-9d33-98774987f67f'></a>

**FCC RF Radiation Exposure Statement:**
1. This Transmitter must not be co-located or operating in conjunction with any other antenna or transmitter.
2. This equipment complies with RF radiation exposure limits set forth for an uncontrolled environment.
3. This equipment should be installed and operated with minimum distance 20cm between the radiator & your body.

<a id='1bcfe28e-511c-451b-ad00-01b6a18d8ad8'></a>

English: User manuals for license-exempt radio apparatus shall contain the following or equivalent notice in a conspicuous location in the user manual or alternatively on the device or both. This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions:

1.  this device may not cause interference
2.  this device must accept any interference, including interference that may cause undesired operation of the device.

French: Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes :

1.  l' appareil nedoit pas produire de brouillage
2.  l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

<a id='91a0f4de-fac6-4714-ad71-71c17b2750b1'></a>

IC SAR Warning:
English This equipment should be installed and operated with minimum distance 20 cm between the radiator and
your body.

<a id='5dc2333a-033f-4909-b4fa-5e2444e8d89f'></a>

French: Lors de l' installation et de l' exploitation de ce dispositif, la distance entre le radiateur et le corps est d'au moins 20 cm.

<a id='3c3073c6-4aa3-4d24-9f20-73ceb022e5d8'></a>

14 / 16

<a id='20b8903c-8514-47f8-b364-cc402e6b160e'></a>

Arduino® MKR WiFi 1010

<a id='2c3c248a-bc89-4dad-bd02-f9a4ef3ebe05'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='80092d71-eb57-4100-a564-d2fd491a76c1'></a>

<::logo: Arduino
None
A teal infinity symbol is combined with a plus sign and a minus sign, forming a stylized logo.:>

<a id='b9b651c2-03c6-4898-aa04-856ad7d646a9'></a>

Arduino® MKR WiFi 1010

<a id='b0ccf02b-ecc0-4a73-b2b3-952338973c14'></a>

**Important:** The operating temperature of the EUT can't exceed 80C and shouldn't be lower than -20C.

<a id='eb339856-4d1f-428e-95e9-a68c8a5b6bef'></a>

Hereby, Arduino S.r.l. declares that this product is in compliance with essential requirements and other relevant provisions of Directive 2014/53/EU. This product is allowed to be used in all EU member states.

<a id='d7e1b941-5554-4535-877b-5db82acf6331'></a>

<table id="14-1">
<tr><td id="14-2">Frequency bands</td><td id="14-3">Maximum output power (EIRP)</td></tr>
<tr><td id="14-4">WiFi(2412-2472MHz)</td><td id="14-5">14.49 dBm</td></tr>
<tr><td id="14-6">BT EDR(2402-2480 MHz)</td><td id="14-7">2.16 dBm</td></tr>
<tr><td id="14-8">BT BLE(2402-2480 MHz)</td><td id="14-9">1.24 dBm</td></tr>
</table>

<a id='1e4a38d0-d080-4a49-b207-597bad3a0eb2'></a>

8 Company Information
<table id="14-a">
<tr><td id="14-b">Company name</td><td id="14-c">Arduino S.r.l.</td></tr>
<tr><td id="14-d">Company Address</td><td id="14-e">Via Andrea Appiani 25, 20900 MONZA, Italy</td></tr>
</table>

<a id='64618542-e249-4053-ab18-3747fb00596b'></a>

9 Reference Documentation
<table id="14-f">
<tr><td id="14-g">Ref</td><td id="14-h">Link</td></tr>
<tr><td id="14-i">NINA Firmware</td><td id="14-j">https://github.com/arduino/nina-fw</td></tr>
<tr><td id="14-k">Arduino IDE (Desktop)</td><td id="14-l">https://www.arduino.cc/en/software</td></tr>
<tr><td id="14-m">Arduino Cloud Editor</td><td id="14-n">https://create.arduino.cc/editor</td></tr>
<tr><td id="14-o">Arduino Cloud Editor - Getting Started</td><td id="14-p">https://docs.arduino.cc/arduino-cloud/guides/editor/</td></tr>
<tr><td id="14-q">Arduino Documentation</td><td id="14-r">https://docs.arduino.cc/hardware/mkr-wifi-1010</td></tr>
<tr><td id="14-s">Arduino Project Hub</td><td id="14-t">https://create.arduino.cc/projecthub?by=part&amp;part_id=11332&amp;sort=trending</td></tr>
<tr><td id="14-u">Library Reference</td><td id="14-v">https://www.arduino.cc/reference/en/libraries/</td></tr>
<tr><td id="14-w">Online Store</td><td id="14-x">https://store.arduino.cc/</td></tr>
</table>

<a id='0fa925d5-9066-441e-bb1b-d9ee1e391940'></a>

15 / 16

<a id='2110e812-0cdb-44b1-ad01-282955e1c4e4'></a>

Arduino® MKR WiFi 1010

<a id='119a389d-5152-4d00-910b-03e53910aa07'></a>

Modified: 05/11/2025

<!-- PAGE BREAK -->

<a id='4ab2d4ef-18ae-4497-8ac6-033f63c14153'></a>

<::logo: Arduino
An infinity symbol with a plus sign on the right side and a minus sign on the left side, all in teal blue.::>

<a id='af753180-caad-4053-a665-128c809f9806'></a>

Arduino® MKR WiFi 1010

<a id='be776f49-4386-4557-9c8f-cac57a0ca481'></a>

10 Revision History
<table id="15-1">
<tr><td id="15-2">Date</td><td id="15-3">Revision</td><td id="15-4">Changes</td></tr>
<tr><td id="15-5">25/04/2024</td><td id="15-6">5</td><td id="15-7">Updated Wi-Fi module information</td></tr>
<tr><td id="15-8">25/04/2024</td><td id="15-9">4</td><td id="15-a">Updated link to new Cloud Editor</td></tr>
<tr><td id="15-b">27/09/2022</td><td id="15-c">3</td><td id="15-d">Rendering problems fixed</td></tr>
<tr><td id="15-e">20/09/2022</td><td id="15-f">2</td><td id="15-g">Migration to Markdown, links updated, small typos fixed</td></tr>
<tr><td id="15-h">22/03/2021</td><td id="15-i">1</td><td id="15-j">First Release</td></tr>
</table>

<a id='54253ea8-0b19-4df3-81d0-1e5eca83c2da'></a>

16 / 16

<a id='fcffff7c-4343-47cb-9840-26d2d35475a4'></a>

Arduino® MKR WiFi 1010

<a id='d1177c3e-d604-48be-a6d9-5f7178c20e76'></a>

Modified: 05/11/2025