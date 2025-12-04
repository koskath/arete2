<a id='d68c5861-e2a8-4f7f-b3e9-30c288d6ebfa'></a>

<::logo: [Unknown]
A black, five-petal flower with a white center dot and four white dots arranged around it.::>

<a id='fbcfebe8-21ea-4db5-9183-7986eea69bcb'></a>

Adafruit BMP280 Barometric Pressure +
Temperature Sensor Breakout

<a id='3493a400-cde1-4b52-b8f1-4db45ac03173'></a>

Created by lady ada

<a id='797bd3a6-cd42-4d9a-9318-dd1f62e4d513'></a>

<::An image of a BMP280 Pressure Sensor circuit board. The board is black with various surface-mount components, including chips, resistors, and capacitors. It has several gold-colored circular pads along the bottom edge for pin connections. The top of the board is labeled "BMP280 Pressure Sensor". Along the bottom edge, the pins are labeled as follows:
3Vo SCK SDI
VIN GND SDO CS
: figure::>

<a id='0124ef34-b823-47ec-9d02-5520358e520c'></a>

https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-
breakout

<a id='2268bb8d-8736-4de7-8c3b-80dc67ef487f'></a>

Last updated on 2024-06-03 01:46:24 PM EDT

<a id='c86e6ea4-4ffb-4a4f-9856-2bbd306dfe0a'></a>

© Adafruit Industries

<a id='42fadb55-a8e2-4d0c-b8ec-e273ea63f9e1'></a>

Page 1 of 34

<!-- PAGE BREAK -->

<a id='cded33c2-e422-4ce7-b84a-39aa65603822'></a>

# Table of Contents

<a id='10862d29-db64-41b2-badb-31661c0845e7'></a>

<table id="1-1">
<tr><td id="1-2">Overview</td><td id="1-3">3</td></tr>
<tr><td id="1-4">Pinouts</td><td id="1-5">6</td></tr>
<tr><td id="1-6">SPI Logic pins:</td><td id="1-7"></td></tr>
<tr><td id="1-8">Power Pins:</td><td id="1-9"></td></tr>
<tr><td id="1-a">I2C Logic pins:</td><td id="1-b"></td></tr>
</table>

<a id='be6b829c-6cad-42c2-b37e-f65fa112f771'></a>

# Assembly

---

* Prepare the header strip:
* Add the breakout board:
* And Solder!

8

<a id='81182b52-e0de-42f7-a111-80ee2d1bfb49'></a>

## Arduino Test

---

* I2C Wiring
* SPI Wiring
* Download Adafruit_BMP280 library
* Load Demo
* Library Reference

10

<a id='428b7847-929f-4185-b2ae-7a707df5e74a'></a>

# Python & CircuitPython Test

* CircuitPython Microcontroller Wiring
* Python Computer Wiring
* CircuitPython Installation of BMP280 Library
* Python Installation of BMP280 Library
* CircuitPython & Python Usage

16

<a id='9da77a0c-bf03-494b-afa4-df767f7dee71'></a>

Python Docs 23

WipperSnapper 24
* What is WipperSnapper
* Wiring
* Usage

<a id='e43ebadf-4f88-483a-ab50-bde1f5b308ee'></a>

F.A.Q.                                                                                              31

<a id='95f0b8f8-b7f7-4b2d-b521-e021a7ea6c01'></a>

## Downloads

---

*   Documents
*   Schematic - STEMMA QT version
*   Fab Print - STEMMA QT version
*   Schematic - Original version
*   Fab Print - Original version

32

<a id='f1eb5793-8cda-4e4d-93b6-6764e525e6b2'></a>

© Adafruit Industries

<a id='e067a162-72fe-4d6f-be5a-e122b81ec54a'></a>

Page 2 of 34

<!-- PAGE BREAK -->

<a id='aa73bf3d-a359-4592-98f9-ba027bd4c47e'></a>

Overview

<a id='49ed1728-306f-4eaa-9e29-a957be48e15b'></a>

<::A small rectangular gray circuit board with various electronic components. Text on the board reads "BMP280 Pressure Sensor". Along one edge, there are solder pads labeled "VIN", "3V0", "GND", "SCK", "SDO", "SDI", and "CS". There are also two mounting holes with metal grommets at opposite corners of the board.
: electronic component::>

<a id='b3754f87-e807-4b6e-ae95-b5968f5a8f50'></a>

Bosch has stepped up their game with their new BMP280 sensor, an environmental sensor with temperature, barometric pressure that is the next generation upgrade to the BMP085/BMP180/BMP183. This sensor is great for all sorts of weather sensing and can even be used in both I2C and SPI!

<a id='2b605f96-cb8f-4b66-bb9d-a92ef7baf4bf'></a>

This precision sensor from Bosch is the best low-cost, precision sensing solution for measuring barometric pressure with 1 hPa absolute accuracy, and temperature with 1.0C accuracy. Because pressure changes with altitude, and the pressure measurements are so good, you can also use it as an altimeter with 1 meter accuracy.

<a id='f060a93d-f045-490a-a4e6-7278f0d79447'></a>

© Adafruit Industries

<a id='448f7655-d520-4f2f-8079-d95ea46f6898'></a>

Page 3 of 34

<!-- PAGE BREAK -->

<a id='3531a6fd-6f16-4394-a39e-b5d1b43ff7a3'></a>

<::A close-up shot of a dark gray BMP280 Pressure Sensor module and a black 8-pin male header below it. The sensor module is rectangular with rounded corners and has various surface-mount components, traces, and text. The top left corner features a star-shaped logo and the text "BMP280 Pressure Sensor". Below this, an "on" indicator is visible. Along the bottom edge of the module, there are eight gold-plated through-holes, each labeled with white text: "VIN", "GND", "3Vo", "SCK", "SDI", "SDO", and "CS". Other markings on the board's components include "AG3P", "310", "103", "197", and "010". The 8-pin male header is positioned directly below the module, showing its black plastic housing and silver metal pins. : electronic component::>

<a id='531feb7c-aa68-41e3-a917-14ec8ab122df'></a>

The BMP280 is the next-generation of sensors from Bosch, and is the upgrade to the BMP085/BMP180/BMP183 - with a low altitude noise of 0.25m and the same fast conversion time. It has the same specifications, but can use either I2C or SPI. For simple easy wiring, go with I2C. If you want to connect a bunch of sensors without worrying about I2C address collisions, go with SPI.

<a id='847bc52e-4b8e-4cad-9127-a88c234c7d4e'></a>

<::A close-up, angled view of a small, rectangular black circuit board, likely a sensor module. The board features various surface-mounted components, including resistors, capacitors, and integrated circuits. On the left edge of the board, there is a row of six gold-plated circular pads with corresponding labels printed in white text: CS, SDI, SDO, SCK, 3V0, and GND. On the right side of the board, rotated text reads "BMP280 Pressure Sensor". A silver connector with multiple pins is visible on the top edge, and another silver connector, resembling a micro-USB port, is located on the bottom edge. The board is resting on a dark, textured surface.: figure::>

<a id='a28c8bdd-546c-4e2a-bf68-2e7d876a8364'></a>

Nice sensor right? So we made it easy for you to get right into your next project. The surface-mount sensor is soldered onto a custom made PCB in the [STEMMA QT form factor](https://adafru.it/LBQ), making them easy to interface with. The [STEMMA QT connectors](https://adafru.it/JqB) on either side are compatible with the [SparkFun Qwiic](https://adafru.it/Fpw) I2C connectors. This allows you to make solderless connections between your development board and the BMP280 or to chain it with a

<a id='b7edc50e-95f8-4d1c-ba05-3f82474f31f3'></a>

© Adafruit Industries

<a id='f7f91e5b-bfdd-4fbe-a327-b8a83c5e608c'></a>

Page 4 of 34

<!-- PAGE BREAK -->

<a id='df8b6446-5435-4344-9787-5e162c857ab6'></a>

wide range of other sensors and accessories using a compatible cable (https:// adafru.it/JnB). We've of course broken out all the pins to standard headers and added a voltage regulator and level shifting so allow you to use it with either 3.3V or 5V systems such as the Metro M4 or Arduino Uno respectively.

<a id='e18c133f-7af3-45e1-8eca-db0e31b5c529'></a>

We even wrote up a nice tutorial with wiring diagrams, schematics, libraries and examples to get you running in 10 minutes! Make sure to check the tutorial for example code for Arduino and CircuitPython, pinouts, assembly, wiring, downloads, and more! (https://adafru.it/MbA)

<a id='ab271924-d0b1-4e4e-b8a2-4750f9fe463e'></a>

There are two versions of this board - the STEMMA QT version shown above, and the original header-only version shown below. Code works the same on both!

<a id='4f9c7553-e930-4d43-97d4-bc89e75d5d9e'></a>

<::A close-up photograph of a small, square, blue circuit board, likely a sensor module, against a dark, textured background. The board has rounded corners and several gold-plated circular pads for connections along the bottom and two larger ones at the top corners for mounting. Text on the board reads "BMP280 Pressure & Temp Sensor" at the top. Various surface-mount components are visible, including resistors (some labeled "1002"), capacitors, and integrated circuits. One IC is labeled "34F KL", another "0E8J", and a smaller one "CLr". Along the bottom edge, connection labels are visible: "VIN", "GND", "SDO", "CS" above their respective pads, and "3V0", "SCK", "SDI" below their pads. A small white star graphic is near the top right corner. The board appears to be a Bosch BMP280 barometric pressure and temperature sensor module.: figure::>

<a id='6728e4e7-cfdc-4670-988d-f1cfe270293d'></a>

©Adafruit Industries

<a id='98a078f4-220f-4ee1-a08c-b443f8ea72ad'></a>

Page 5 of 34

<!-- PAGE BREAK -->

<a id='7d0bcd4d-2491-4b8a-a74a-dad70baf45d9'></a>

Pinouts

<a id='a681e4f6-924d-458d-a139-9302c1c05652'></a>

<::A close-up, top-down view of a small, rectangular, black circuit board for a BMP280 Pressure Sensor. The board features various surface-mount components, including integrated circuits, resistors, and capacitors. At the top left, there's a star-like logo next to the text "BMP280 Pressure Sensor". There are four mounting holes, one in each corner, with gold-plated rings. Along the bottom edge of the board, there are seven gold-plated through-holes, labeled from left to right as: VIN, GND, SDO, CS. Above these pins, other labels are visible: 3Vo, SCK, SDI. Other text visible on the components and board includes: "on", "310", "103", "4G3P", "PS", "197", and "D1C".
: figure::>

<a id='6d6ae7ee-7596-4f6a-87ec-1b67d40b1687'></a>

<::Image of a small, square blue circuit board for a BMP280 Pressure & Temp Sensor. The board features various surface-mount electronic components, including resistors, capacitors, and integrated circuits. Text printed on the board includes 'BMP280 Pressure & Temp Sensor' at the top, and pin labels along the bottom edge: 'VIN', 'GND', 'SDO', 'CS', '3V0', 'SCK', 'SDI'. There are gold-plated circular pads below each pin label and mounting holes in the corners. A small white star logo is visible on the right side of the board.: figure::>

<a id='accf2302-4d07-4c86-b520-88ba4996d539'></a>

Power Pins:

*   **Vin** - this is the power pin. Since the sensor chip uses 3 VDC, we have included a voltage regulator on board that will take 3-5VDC and safely convert it down. To power the board, give it the same power as the logic level of your microcontroller - e.g. for a 5V micro like Arduino, use 5V
*   **3Vo** - this is the 3.3V output from the voltage regulator, you can grab up to 100mA from this if you like

<a id='5bd28799-c955-4ab4-9d6c-b0bc50a7b0e8'></a>

© Adafruit Industries

<a id='2efa8097-c6b5-44cb-8766-033c4fb3a814'></a>

Page 6 of 34

<!-- PAGE BREAK -->

<a id='69a1e2ed-e376-47ec-9a06-10e7cfe01a06'></a>

GND - common ground for power and logic

<a id='04634302-f960-4f10-860d-93ab047950df'></a>

# SPI Logic pins:

All pins going into the breakout have level shifting circuitry to make them 3-5V logic level safe. Use whatever logic level is on **Vin**!

* **SCK** - This is the **SPI Clock** pin, its an input to the chip
* **SDO** - this is the **Serial Data Out** / **Microcontroller In Sensor Out** pin, for data sent from the BMP280 to your processor
* **SDI** - this is the **Serial Data In** / **Microcontroller Out Sensor In** pin, for data sent from your processor to the BMP280
* **CS** - this is the **Chip Select** pin, drop it low to start an SPI transaction. Its an input to the chip

<a id='2cb36188-7dc1-428b-b7b5-11d275463f6a'></a>

If you want to connect multiple BMP280's to one microcontroller, have them share the SDI, SDO and SCK pins. Then assign each one a unique CS pin.

<a id='895cc4b5-4093-4378-a438-abcc7cd2a530'></a>

I2C Logic pins:

*   **SCK** - this is also the I2C clock pin (**SCL**), connect to your microcontroller's I2C clock line.
*   **SDI** - this is also the I2C data pin (**SDA**), connect to your microcontroller's I2C data line.

<a id='2990b196-84b2-40c2-bb23-6a983929d281'></a>

Leave the other pins disconnected

<a id='7045534b-0c88-4ac9-af82-c001fb1b796f'></a>

©Adafruit Industries

<a id='b208eb36-3183-4ce8-8aa8-831633a94d72'></a>

Page 7 of 34

<!-- PAGE BREAK -->

<a id='45679dbc-ce04-4887-9645-c653802ae978'></a>

Assembly

<a id='bf248b6c-fc12-47c5-80b6-1ac46b1666f1'></a>

<::A blue square circuit board, labeled "BMP280 Pressure & Temp Sensor", is positioned above a row of black pin headers with gold-colored pins. The circuit board has various surface-mount components, including resistors, capacitors, and an integrated circuit. Along the bottom edge of the circuit board are circular pads labeled from left to right: VIN, GND, SDO, CS, 3Vo, SCK, and SDI. There is also a small white star icon on the top right of the board. The pin header strip has 16 pins.: figure::>

<a id='51f17a5c-1557-4eb8-aa8a-1146ebe26c17'></a>

The assembly pix use the BME280 but it is identically shaped/sized as the BMP280

<::A photo showing a white breadboard with a black header strip inserted into the middle section. The header strip has 8 pins. The breadboard has numbered rows (1-30) and lettered columns (a-j for the top section, a-e for the middle, and f-j for the bottom section). The top and bottom edges of the breadboard also have power rails marked with '+' (red line) and '-' (blue line).

Prepare the header strip: Cut the strip to length if necessary. It will be easier to solder if you insert it into a breadboard - long pins down
: figure::>


<a id='0c5f451c-70a9-4709-9b60-561fcf0d3180'></a>

©Adafruit Industries

<a id='6353cea3-79f8-4994-b71b-5aa22a4b0adf'></a>

Page 8 of 34

<!-- PAGE BREAK -->

<a id='7513d9c5-58ff-4991-8322-7e5cfb2a5cfd'></a>

<::A BME280 sensor module, a small blue circuit board, is mounted on a white breadboard. The module is labeled "BME280 Pressure Temp+Humidity" at the top. Along the bottom edge, there are pin labels with corresponding gold-colored circular pads: UIN, GND, SDO, CS, 3Vo, SCK, and SDI. The breadboard has numbered rows (6 through 24) and columns.::>

<a id='0a6638fb-3054-46d9-8aa7-6657cdf242d0'></a>

<::Two images showing the process of soldering. The top image shows a close-up of hands soldering a wire to a small blue sensor module plugged into a white breadboard. A black microcontroller board (partially visible, labeled "tro") is in the background. The bottom image provides a more detailed view of the breadboard and sensor module. The breadboard has numbered rows (1-30) and lettered columns (a-j) and power rails marked with red (+) and blue (-) lines. The blue sensor module is labeled "BME280 Pressure TempHumidity" and has pins labeled "VIN", "GND", "SDO", and "SCK". A silver wire is being held by one hand, and a soldering iron is held by another hand, with its tip touching a pin on the BME280 module to solder the wire. The wire is connected to row 12, column e on the breadboard.::>

<a id='3d28bb0c-8a5b-4286-965e-1fbe94b23833'></a>

<::logo: [Unknown Brand]BME 280PressureTemp HumidityThis logo features a blue circuit board with white text and gold components.::>

<a id='adcd4ec6-118b-424e-8424-70fd08ae3c1e'></a>

# Add the breakout board:
Place the breakout board over the pins so
that the short pins poke through the
breakout pads

<a id='3bd8c176-74f5-4917-9849-bbc299ff52c3'></a>

## And Solder!
Be sure to solder all pins for reliable electrical contact.

<a id='eba11c8f-8e7f-41fc-8174-3c9c36482862'></a>

(For tips on soldering, be sure to check out our [Guide to Excellent Soldering](https://adafru.it/aTk)).

<a id='b0c06376-1955-469a-aa64-9c838b25a78d'></a>

© Adafruit Industries

<a id='b6eb15d4-295f-4008-82d7-c171048eff2f'></a>

Page 9 of 34

<!-- PAGE BREAK -->

<a id='8cfb4170-eee0-4e3a-8d67-2280252acd0f'></a>

<::A close-up photograph of a blue BME280 Pressure, Temperature, and Humidity sensor module. The module is placed on a white breadboard, with its pins inserted into the breadboard holes. The module has various components, including integrated circuits and resistors, and is labeled with "BME280", "Pressure", and "Temp+Humidity". The pins are labeled from left to right as "VIN", "3Vo", "GND", "SCK", "SDO", "SDI", and "CS".
: figure::>
You're done! Check your solder joints visually and continue onto the next steps

<a id='f021cd9a-1dfd-406f-a68c-78d97495bdb2'></a>

<::A close-up view of a small blue circuit board labeled "Temp+Humidity". The board has various surface-mount components, including resistors labeled "1002", "2001", and "2006", and an integrated circuit labeled "0133". There's also a small square component in the center that appears to be the sensor. Along the bottom edge of the board, there are solder pads with corresponding labels: "UIN", "GND", "SDO", and "CS" on the top row, and "/3Vo", "SCK/", and "SDI" on the bottom row. A small star-shaped logo is visible in the upper right corner.
: figure::>

<a id='61bf2d9b-6cfd-476b-acfc-6dcea57526bc'></a>

# Arduino Test
You can easily wire this breakout to any microcontroller, we'll be using an Arduino. For another kind of microcontroller, as long as you have 4 available pins it is possible to 'bit-bang SPI' or you can use two I2C pins, but usually those pins are fixed in hardware. Just check out the library, then port the code.

<a id='fd9f86cb-7209-4aa7-b732-2eb5bb04e684'></a>

I2C Wiring

Use this wiring if you want to connect via I2C interface

<a id='caea6a63-ef9a-496b-a1c5-b62f4a40603c'></a>

© Adafruit Industries

<a id='114a2cbe-ebac-4acf-bb85-7b51bf63798f'></a>

Page 10 of 34

<!-- PAGE BREAK -->

<a id='73558cd5-18ad-4557-83a0-dab24d972cb4'></a>

<::A photograph showing an Adafruit Metro microcontroller board connected to a white breadboard. The Metro board is black with "Metro" and "adafruit" logos. Wires (red, blue, yellow, black) connect the Metro board to a small blue sensor module on the breadboard, which is labeled with rows and columns.
: figure::>
<::A Fritzing diagram illustrating the wiring connections between an Adafruit Metro microcontroller board and a BMP280 pressure sensor module. The Metro board is black and labeled "Metro" and "adafruit". The sensor module is also black and connected to a small virtual breadboard area. Wires (yellow, blue, red, black) connect the two components.
: diagram::>
<::A Fritzing diagram, similar to the previous one, showing the wiring between an Adafruit Metro microcontroller board and a BMP280 pressure sensor. The Metro board is black with "Metro" and "adafruit" logos and pin labels like "Digital" and "Analog In". The sensor module is black and labeled "BMP280 Pressure Sensor". Wires (yellow, blue, red, black) connect the boards.
: diagram::>
fritzing

<a id='d9cb6b7f-cf20-4dd2-876b-9992a3810382'></a>

Connect Vin (**red wire on STEMMA**
version) to the power supply, 3-5V is fine.
Use the same voltage that the
microcontroller logic is based off of. For
most Arduinos, that is 5V
Connect GND (**black wire on STEMMA**
version) to common power/data ground
Connect the SCK (**yellow wire on STEMMA**
version) pin to the I2C clock **SCL** pin on
your Arduino. On an UNO & '328 based
Arduino, this is also known as **A5**, on a
Mega it is also known as **digital 21** and on
a Leonardo/Micro, **digital 3**
Connect the SDI (**blue wire on STEMMA**
version) pin to the I2C data **SDA** pin on
your Arduino. On an UNO & '328 based
Arduino, this is also known as **A4**, on a
Mega it is also known as **digital 20** and on
a Leonardo/Micro, **digital 2**

<a id='20ba5f1d-153e-48a0-be17-165d5853500f'></a>

## SPI Wiring

Since this is a SPI-capable sensor, we can use hardware or 'software' SPI. To make wiring identical on all Arduinos, we'll begin with 'software' SPI. The following pins should be used:

<a id='69eb1ca0-1279-405a-971b-9da985ede455'></a>

© Adafruit Industries

<a id='04c077d9-c482-4c65-a2ca-de02b4cdd060'></a>

Page 11 of 34

<!-- PAGE BREAK -->

<a id='4304aa11-6bf4-438b-8723-0a5d95d3e820'></a>

<:: A top-down view of a black Adafruit Metro microcontroller board connected to a white breadboard. A blue BME280 sensor module is plugged into the breadboard. Jumper wires connect the Metro board to the breadboard and the sensor module. Specifically, a red wire connects the Metro's 5V pin to the positive power rail of the breadboard, and a black wire connects the Metro's GND pin to the negative power rail. The BME280 sensor is connected to the breadboard with a red wire from the breadboard's positive rail to the sensor's VIN, a brown wire from the breadboard's negative rail to the sensor's GND, a yellow wire from the Metro's SDA pin to the sensor's SDA, a green wire from the Metro's SCL pin to the sensor's SCL, and a light blue wire from the Metro's D2 pin to the sensor's SCK. The breadboard has rows labeled 1 through 30 and columns 'a' through 'j'.
: figure::>
<:: A top-down view of a black Adafruit Metro microcontroller board connected to a smaller white breadboard. A black BME280 sensor module is plugged into the small breadboard. Jumper wires connect the Metro board to the small breadboard and the sensor module. A red wire connects the Metro's 5V pin to the sensor's VIN pin (via the breadboard), a black wire connects the Metro's GND pin to the sensor's GND pin (via the breadboard), a purple wire connects the Metro's SDA pin to the sensor's SDA pin, a green wire connects the Metro's SCL pin to the sensor's SCL pin, and a yellow wire connects the Metro's D2 pin to the sensor's SCK pin.
: figure::> 

<a id='71d18a21-9eff-4f6e-8789-6f05c07853b0'></a>

<::An image shows a blue rectangular electronic module, labeled "BMP280 Pressure Sensor" and "Adafruit Breakout", connected to a breadboard. Wires in various colors (black, red, blue, green, yellow, white) extend from the module to the breadboard, which has rows of holes for connections.::>

<a id='149d50e4-6423-4357-a048-6b5c3e04b773'></a>

Connect **Vin** to the power supply, 3V or 5V is fine. Use the same voltage that the microcontroller logic is based off of. For most Arduinos, that is 5V
Connect **GND** to common power/data ground
Connect the **SCK** pin to **Digital #13** but any pin can be used later
Connect the **SDO** pin to **Digital #12** but any pin can be used later
Connect the **SDI** pin to **Digital #11** but any pin can be used later
Connect the **CS** pin **Digital #10** but any pin can be used later

<a id='604a5c2d-e621-4165-99db-2069ce5bf0da'></a>

Later on, once we get it working, we can adjust the library to use hardware SPI if you
desire, or change the pins to other

<a id='6ae53457-434a-4e94-90fb-4ff5f8aeeb4e'></a>

# Download Adafruit_BMP280 library

To begin reading sensor data, you will need to [install the Adafruit_BMP280 library](https://adafru.it/fIK) (code on our github repository). It is available from the Arduino library manager so we recommend using that.

<a id='0c4c1ef6-d313-4eef-833a-0eb3b2b95586'></a>

From the IDE open up the library manager...<::Arduino IDE screenshot: The window title bar reads "demo | Arduino 1.8.4". The menu bar shows "File Edit Sketch Tools Help". The "Sketch" menu is open, displaying a dropdown list. The "Include Library" option is highlighted, and hovering over it reveals a sub-menu. In this sub-menu, "Manage Libraries..." is highlighted. Other options visible in the Sketch menu include: Verify/Compile Ctrl+R, Upload Ctrl+U, Upload Using Programmer Ctrl+Shift+U, Export compiled Binary Ctrl+Alt+S, Show Sketch Folder Ctrl+K, Add File.... The sub-menu for Include Library also shows: Add .ZIP Library..., Arduino libraries (header), ArduinoHttpClient, ArduinoSound, AudioZero, Bridge.::>

<a id='471525c5-09d4-4634-89d9-bc6cf9ec991a'></a>

©Adafruit Industries

<a id='65f435a8-75dc-4ea2-9d84-df1fceafb238'></a>

Page 12 of 34

<!-- PAGE BREAK -->

<a id='af7d61c0-ebe9-4e59-aae3-dd2d468361fb'></a>

#define BMP_MOSI 11
#define BMP_CS 10
Adafruit_BMP280 bmp; // I2C
//Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
//Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO, BMP_SCK);

<a id='28303d48-81be-4b45-93aa-e0ac8ff85580'></a>

Once uploaded to your Arduino, open up the serial console at 9600 baud speed to see data being printed out

<a id='5f0ee925-7d0c-44e3-b850-e77235c2ee50'></a>

COM55

[ ] Send

BMP280 test
Temperature = 25.53 *C
Pressure = 100935.02 Pa
Approx altitude = 32.52 m

Temperature = 25.54 *C
Pressure = 100937.41 Pa
Approx altitude = 32.32 m

Temperature = 25.54 *C
Pressure = 100935.35 Pa
Approx altitude = 32.49 m

Temperature = 25.65 *C
Pressure = 100939.53 Pa
Approx altitude = 32.14 m

Temperature = 26.91 *C
Pressure = 101698.37 Pa
Approx altitude = -31.04 m

Temperature = 26.73 *C
Pressure = 100944.21 Pa
Approx altitude = 31.75 m

option Autoscroll: [x]
Both NL & CR
9600 baud

<a id='872f08c8-1b60-438d-814d-b23fb887126c'></a>

**Temperature** is calculated in degrees C, you can convert this to F by using the classic
F = C * 9/5 + 32 equation.

<a id='b06b1551-dc93-41df-b5d4-3390009803f5'></a>

Pressure is returned in the SI units of **Pascals**. 100 Pascals = 1 hPa = 1 millibar. Often times barometric pressure is reported in millibar or inches-mercury. For future reference 1 pascal =0.000295333727 inches of mercury, or 1 inch Hg = 3386.39 Pascal. So if you take the pascal value of say 100734 and divide by 3389.39 you'll get

<a id='6f5f14c3-c036-40d9-ab74-11417ba7a4c8'></a>

Adafruit Industries

<a id='9e273871-6003-4aaa-98bf-22b21e15fe40'></a>

Page 14 of 34

<!-- PAGE BREAK -->

<a id='30e0b3a0-fbfe-40de-be7b-ef7596f3e402'></a>

29.72 inches-Hg.

<a id='8a3a1aaa-025e-4107-82db-2bf7d26e2562'></a>

You can also calculate Altitude. However, you can only really do a good accurate job of calculating altitude if you know the hPa pressure at sea level for your location and day! The sensor is quite precise but if you do not have the data updated for the current day then it can be difficult to get more accurate than 10 meters.

<a id='7cbdf584-6217-424e-8f40-9f3281436d7f'></a>

# Library Reference
You can start out by creating a BMP280 object with either software SPI (where all four pins can be any I/O) using

<a id='eab208a6-7ab4-492f-a134-fe98a1a7fe3a'></a>

Adafruit_BMP280 bmp(BMP_CS, BMP_MOSI, BMP_MISO, BMP_SCK);

<a id='f931c0a1-abef-468a-8ec7-e8d6fb818ccf'></a>

Or you can use hardware SPI. With hardware SPI you must use the hardware SPI pins for your Arduino - and each arduino type has different pins! Check the [SPI reference to see what pins to use.](https://adafru.it/d5h)
In this case, you can use any CS pin, but the other three pins are fixed

```
Adafruit_BMP280 bmp(BMP_CS); // hardware SPI
```

<a id='37eadafd-7f67-4029-b7d1-9da9e0eb6064'></a>

or I2C using the default I2C bus, no pins are assigned

```
Adafruit_BMP280 bmp; // I2C
```

<a id='9fd8f84b-d90f-4142-8ebe-3138c703eb8a'></a>

Once started, you can initialize the sensor with

```
if (!bmp.begin()) {
Serial.println("Could not find a valid BMP280 sensor, check wiring!");
while (1);
}
```

<a id='aff2f052-32b8-4311-bddc-926d99973f47'></a>

begin() will return True if the sensor was found, and False if not. If you get a False value back, check your wiring!

<a id='d52f1f27-12c1-4dd8-9ff0-4b9fcd137d8b'></a>

Reading temperature and pressure is easy, just call:

```
bmp.readTemperature()
bmp.readPressure()
```

<a id='0bcf86af-905f-4801-8cd6-d523ec505fe9'></a>

© Adafruit Industries

<a id='7d944b79-f040-4a08-9b44-8dbbfa881271'></a>

Page 15 of 34

<!-- PAGE BREAK -->

<a id='b7efe6af-3c5f-4f95-a720-9753b0b1513d'></a>

Temperature is always a floating point, in Centigrade. Pressure is a 32 bit integer with the pressure in Pascals. You may need to convert to a different value to match it with your weather report.

<a id='bc0a5eab-6d7b-4e5c-a197-68126e0a3964'></a>

It's also possible to turn the BMP280 into an altimeter. If you know the pressure at sea level, the library can calculate the current barometric pressure into altitude

<a id='5535ab08-0fae-4164-859b-ec5bb96a056d'></a>

# Python & CircuitPython Test
It's easy to use the BMP280 sensor with CircuitPython and the [Adafruit CircuitPython BMP280](https://adafru.it/COx) module. This module allows you to easily write Python code that reads the temperature and pressure from the sensor.

<a id='60ac3f64-f5cd-446d-97e3-acc27ba07dff'></a>

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python thanks to Adafruit_Blinka, our CircuitPython-for-Python compatibility library (https://adafru.it/BSN).

<a id='9d15f5b0-69a0-4235-87a1-d03467479982'></a>

# CircuitPython Microcontroller Wiring

First wire up a BMP280 to your board exactly as shown on the previous pages for Arduino. You can use either I2C or SPI wiring, although it's recommended to use I2C for simplicity. Here's an example of wiring a Feather to the sensor with I2C:

<a id='73259469-4db1-4c49-ac34-29d2d125adbc'></a>

©Adafruit Industries

<a id='96ed7b0f-4c5a-40de-9089-18f8d28ebc46'></a>

Page 16 of 34

<!-- PAGE BREAK -->

<a id='ef777c82-e488-4ac6-ab16-bac1ca8dc035'></a>

<::logo: fritzing
fritzing
The logo is a stylized wordmark in a sans-serif font, rendered in a dark gray color.::>

<a id='7fddba88-64c3-4bcf-a4c2-40535af35cd3'></a>

<::A Fritzing-style diagram shows an electronic circuit assembled on a white breadboard. Two main components are visible: an Adafruit Feather M4 Express microcontroller board on the left and a BMP280 Pressure Sensor board on the right. Both boards are black PCBs. The breadboard has red and blue power rails along the top and bottom edges, indicating positive and negative voltage lines, respectively. The Feather M4 Express board is labeled "Adafruit Feather M4 Express" and has a USB port on its left side. Key pins on the Feather M4 board include "Bat", "En", "USB", digital pins 13 through 5, "SCL", "SDA", "3V", "Gnd", analog pins A0 through A5, "SCK", "MO", "MI", "RX", "TX", and "D4". The BMP280 Pressure Sensor board is labeled "BMP280 Pressure Sensor" and has pins for "VIN", "GND", "SCL", "SDA", "CSB", and "SDO". Connections are made with jumper wires: A red wire connects the "3V" pin of the Feather M4 to the bottom red power rail of the breadboard. A black wire connects the "Gnd" pin of the Feather M4 to the bottom blue power rail. The BMP280 sensor's "VIN" pin is connected to the bottom red power rail, and its "GND" pin is connected to the bottom blue power rail. A yellow wire connects the "SDA" pin of the Feather M4 to the "SDA" pin of the BMP280. A blue wire connects the "SCL" pin of the Feather M4 to the "SCL" pin of the BMP280. This setup demonstrates an I2C communication connection between the Feather M4 and the BMP280 sensor, powered via the breadboard's rails.: circuit diagram::>

<a id='666e9974-16aa-4aff-82a7-d093287a9168'></a>

Board 3V to sensor VIN (red wire on
STEMMA version)
Board GND to sensor GND (black wire on
STEMMA version)
Board SCL to sensor SCK (yellow wire on
STEMMA version)
Board SDA to sensor SDI (blue wire on
STEMMA version)

<a id='b04aab38-49b9-4f3d-8341-ce69c18bab1d'></a>

<::A diagram showing two electronic boards connected by colored wires. On the left is a rectangular board labeled "BMP280 Pressure Sensor" with pins labeled VIN, GND, SDO, SCK, SDA, and CS. On the right is a larger rectangular board labeled "Feather M4 Express" by Adafruit. This board has a USB port, a reset button, and numerous pins labeled from 3V, Aref, Gnd, A0 to A5, SCK, MOSI, MISO, RX, TX, and D4, as well as digital pins 13 down to 5, SCL, and SDA. A black wire connects the GND pin of the sensor to a GND pin on the Feather M4. A red wire connects the VIN pin of the sensor to a 3V pin on the Feather M4. A blue wire connects the SDA pin of the sensor to the SDA pin on the Feather M4. A yellow wire connects the SCK pin of the sensor to the SCL pin on the Feather M4. The text "fritzing" is visible in the bottom right corner of the image.: diagram::>
fritzing

<a id='168e2b05-88ba-435f-9d61-ee2e1445e3cd'></a>

And an example of a Feather M0 wired with hardware SPI:

<a id='cb6dd0b7-e802-404c-95a6-da31c2ae689b'></a>

Adafruit Industries

<a id='d30732ef-025c-4671-92a8-9e5ec64691d0'></a>

Page 17 of 34

<!-- PAGE BREAK -->

<a id='d19949b9-4bad-4343-9b8b-a3665a0d6882'></a>

<::A circuit diagram showing a black Adafruit Feather M4 Express microcontroller board connected to a blue BMP280 Pressure & Temp Sensor module via a breadboard. The Feather M4 Express has a USB port at the bottom and multiple pin headers along its sides. The BMP280 sensor module is labeled "BMP280 Pressure & Temp Sensor" and has six pins labeled VIN, GND, SCL, SDA, 3V3, and SDO. The components are interconnected with various colored jumper wires: a green wire connects a pin on the Feather to a pin on the breadboard, a yellow wire connects from the Feather to the SCL pin of the sensor, a blue wire connects from the Feather to the SDA pin of the sensor, an orange wire connects from the Feather to the 3V3 pin of the sensor, a red wire connects from the Feather to the GND pin of the sensor, a black wire connects from the Feather to the VIN pin of the sensor, and another green wire connects from the Feather to a pin on the breadboard near the sensor. The breadboard has numbered rows and columns. The "fritzing" logo is visible in the bottom right corner of the image.
: figure::>

<a id='55af49da-b47c-4e01-aaf0-39c3b3b3fc2e'></a>

Board **3V** to sensor **VIN**
Board **GND** to sensor **GND**
Board **SCK** to sensor **SCK**
Board **MOSI** to sensor **SDI**
Board **MISO** to sensor **SDO**
Board **D5** to sensor **CS** (or use any other free digital I/O pin)

<a id='3708a84f-062e-4009-9c22-aea78057acf3'></a>

<::The image displays a circuit setup on a white breadboard. Two main electronic components are visible: an Adafruit Feather M4 microcontroller board and a BMP280 pressure sensor module. The breadboard features horizontal power rails at the top and bottom (indicated by red and blue lines) and a central prototyping area with numbered columns and lettered rows.  The Feather M4 board, positioned on the left, is a black PCB with a USB port on its left side. Its pins are labeled as follows:  - Top row (left to right): Bat, En, USB, 13, 12, 11, 10, 9, 6, 5, SCL, SDA, 3V, GND.  - Bottom row (left to right): 3V, Aref, Gnd, A0, A1, A2, A3, A4, A5, SCK, MISO, MOSI, RX, TX, D4.  The BMP280 Pressure Sensor module, located on the right side of the breadboard, is also a black PCB. Its bottom pins are labeled (from left to right): Vin, Gnd, SCL, SDA, CS, SD0.  Several colored jumper wires connect the two modules on the breadboard:  - A green wire connects the '3V' pin on the bottom row of the Feather M4 to the 'Vin' pin of the BMP280.  - A black wire connects the 'Gnd' pin on the bottom row of the Feather M4 to the 'Gnd' pin of the BMP280.  - A blue wire connects the 'SCL' pin on the bottom row of the Feather M4 to the 'SCL' pin of the BMP280.  - A purple wire connects the 'SDA' pin on the bottom row of the Feather M4 to the 'SDA' pin of the BMP280.  - Additionally, two green wires connect the Feather M4's '3V' and 'GND' pins (from its top row) to the breadboard's power rails.  The overall image shows a complete wiring diagram for connecting a BMP280 pressure sensor to an Adafruit Feather M4 microcontroller on a breadboard.::>

<a id='7a1bca69-22bf-4588-9bb6-72bce8caed72'></a>

## Python Computer Wiring

Since there's dozens of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://adafru.it/BSN).

<a id='1cb4697b-e12b-43c7-a778-e0438a8da723'></a>

Here's the Raspberry Pi wired with I2C:

<a id='1e6611ad-02f5-47b7-8354-38e82e9c60bb'></a>

©Adafruit Industries

<a id='d6863ac4-11fc-4999-b593-d53f823e5045'></a>

Page 18 of 34

<!-- PAGE BREAK -->

<a id='b79ea790-4b56-4021-aedf-4443b16af3c0'></a>

<::diagram: A Fritzing diagram showing a green Raspberry Pi board connected to a blue BME280 sensor module on a white breadboard via jumper wires. The Pi has various ports including USB, Ethernet, and HDMI, and its GPIO pins are connected to the breadboard, which in turn connects to the sensor module.:>

<::diagram: A Fritzing diagram depicting a green Raspberry Pi board connected to a black VPP280 sensor module mounted on a white breadboard. Jumper wires connect the Pi's GPIO pins to the sensor module via the breadboard. The associated wiring instructions are:
Pi 3V3 to sensor VIN (red wire on STEMMA version)
Pi GND to sensor GND (black wire on STEMMA version)
Pi SCL to sensor SCK (yellow wire on STEMMA version)
Pi SDA to sensor SDI (blue wire on STEMMA version):>

<::diagram: A Fritzing diagram showing a green Raspberry Pi board directly connected to a black VPP280 sensor module using jumper wires. The sensor module is attached directly to the Pi's GPIO pins without a breadboard.:>

And an example on the Raspberry Pi 3 Model B wired with SPI: 

<a id='30a2247c-9387-45c6-86a7-da5cd43b36c0'></a>

© Adafruit Industries

<a id='5dd5eae6-e599-4c55-b68a-0601cbc091d7'></a>

Page 19 of 34

<!-- PAGE BREAK -->

<a id='dadc5963-43fb-4661-9b44-5016cce95cd1'></a>

<::Fritzing diagram showing a top-down view of a Raspberry Pi 3 Model B v1.2 (© Raspberry Pi 2015) connected to a blue BME280 Pressure Temperature Humidity sensor module on a breadboard. The Raspberry Pi has various ports labeled: Power, DSI (DISPLAY), HDMI, CSI (CAMERA), Audio, Ethernet, and four USB 2.0 ports. Wires connect the Raspberry Pi's GPIO pins to the breadboard and then to the BME280 sensor module. The wires are colored red, black, orange, yellow, blue, and green.fritzing
: circuit diagram::>
<::Fritzing diagram showing a bottom-up view of a Raspberry Pi 3 Model B v1.2 (© Raspberry Pi 2015) connected to a black BME280 Pressure Sensor module on a breadboard. The Raspberry Pi has various ports labeled: Power, DSI (DISPLAY), HDMI, CSI (CAMERA), Audio, Ethernet, and four USB 2.0 ports. Wires connect the Raspberry Pi's GPIO pins to the breadboard and then to the BME280 sensor module. The wires are colored red, black, blue, purple, yellow, and green.
: circuit diagram::>

<a id='11fbaf88-77f1-4b8e-aeeb-94171aef3503'></a>

Pi **3V3** to sensor **VIN**
Pi **GND** to sensor **GND**
Pi **MOSI** to sensor **SDI**
Pi **MISO** to sensor **SDO**
Pi **SCLK** to sensor **SCK**
Pi **#5** to sensor **CS** (or use any other free
GPIO pin)

<a id='c616aff4-68f5-427a-b1bf-dd7981d4238d'></a>

CircuitPython Installation of BMP280
Library

<a id='85279730-1e4b-4d8a-af44-29674cdb59b2'></a>

You'll need to install the [Adafruit CircuitPython BMP280](https://adafru.it/COx) library on your CircuitPython board.

<a id='892bf10a-be54-40bd-8c2a-459483e4a933'></a>

First make sure you are running the [latest version of Adafruit CircuitPython](https://adafru.it/Amd) for your board.

<a id='447cef56-a7cc-4b52-bec7-62c4a65b04d7'></a>

Next you'll need to install the necessary libraries to use the hardware--carefully follow the steps to find and install these libraries from [Adafruit's CircuitPython library bundle](https://adafru.it/uap). Our CircuitPython starter guide has a [great page on how to install the library bundle](https://adafru.it/ABU).

<a id='1c16d637-2b6a-4f37-8558-d1113587636c'></a>

© Adafruit Industries

<a id='ab385b29-787a-4a54-b80f-0652dbf719db'></a>

Page 20 of 34

<!-- PAGE BREAK -->

<a id='3b5548e3-7bb1-46ef-8790-eeb0b4ca3bd6'></a>

For non-express boards like the Trinket MO or Gemma MO, you'll need to manually install the necessary libraries from the bundle:

<a id='6c00bcbb-af74-4fe6-88f2-0d090536ca07'></a>

* adafruit_bmp280.mpy
* adafruit_bus_device

<a id='80b758c9-418d-40f5-b20a-54ec760044e5'></a>

Before continuing make sure your board's lib folder or root filesystem has the `adafruit_bmp280.mpy`, and `adafruit_bus_device` files and folders copied over.

<a id='eb5e6912-e579-4866-b935-61d8340d3f0f'></a>

Next [connect to the board's serial REPL](https://adafru.it/Awz) so you are at the CircuitPython >>> prompt.

<a id='db5e8b52-c047-4501-a2c4-dec43e068b23'></a>

# Python Installation of BMP280 Library
You'll need to install the Adafruit_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready (https://adafru.it/BSN)!

<a id='56c06d12-9164-459f-9b17-34fca9881e1d'></a>

Once that's done, from your command line run the following command:

<a id='6baa7ae1-d4ed-49e0-900a-1a73b6a517c0'></a>

- sudo pip3 install adafruit-circuitpython-bmp280

<a id='f2cf09e1-e466-4137-a272-73a38b3be14b'></a>

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

<a id='4b790296-8a3f-451a-a13c-7493ab76a75d'></a>

CircuitPython & Python Usage

<a id='acdb3112-6441-4dd9-95ce-f5a8ca575d0f'></a>

To demonstrate the usage of the sensor we'll initialize it and read the temperature,
humidity, and more from the board's Python REPL.

<a id='60d82fc5-98e2-44e0-b114-d254d569252b'></a>

If you're using an I2C connection run the following code to import the necessary modules and initialize the I2C connection with the sensor:

<a id='ac3c840f-bd8c-4611-8225-6d38ab9cc751'></a>

```python
import board
import adafruit_bmp280
i2c = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
```

<a id='14d07aa1-a5b5-47cf-a4bc-f42e93b1d829'></a>

© Adafruit Industries

<a id='02c42120-8c76-4934-a229-39bb0b7e3a4d'></a>

Page 21 of 34

<!-- PAGE BREAK -->

<a id='d2f7a562-a012-4057-a25e-6acdcc30473c'></a>

Or if you're using a SPI connection run this code instead to setup the SPI connection
and sensor:

```
import board
import digitalio
import adafruit_bmp280
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)
sensor = adafruit_bmp280.Adafruit_BMP280_SPI(spi, cs)
```

<a id='73a58dc7-65ee-4ecf-99bb-e1da3728b44e'></a>

Now you're ready to read values from the sensor using any of these properties:

<a id='d7d367c0-d735-43c4-966d-def094ee2dcc'></a>

* **temperature** - The sensor temperature in degrees Celsius.
* **pressure** - The pressure in hPa.
* **altitude** - The altitude in meters.

<a id='07edf083-883d-467a-885f-4ed58c33773a'></a>

For example to print temperature and pressure:

<a id='b3b93fba-44d3-43e9-b119-3505d91e98ff'></a>

```python
print('Temperature: {} degrees C'.format(sensor.temperature))
print('Pressure: {}hPa'.format(sensor.pressure))
```

<a id='c239f983-e00b-4af8-851b-a96e3b0cedde'></a>

```
>>> print('Temperature: {} degrees C'.format(sensor.temperature))
Temperature: 21.0874 degrees C
>>> print('Pressure: {}hPa'.format(sensor.pressure))
Pressure: 1012.32hPa
>>>
```

<a id='381b2af2-0069-4cf2-9e73-816fef1c042c'></a>

For altitude you'll want to set the pressure at sea level for your location to get the most accurate measure (remember these sensors can only infer altitude based on pressure and need a set calibration point). Look at your local weather report for a pressure at sea level reading and set the **seaLevelhPA** property:

<a id='00d764b5-8ebb-4f60-b6f8-6ce613c38268'></a>

```
sensor.sea_level_pressure = 1013.25
```

<a id='456a272e-6b22-4074-9c10-6f51a2a84bb1'></a>

Then read the altitude property for a more accurate altitude reading (but remember this altitude will fluctuate based on atmospheric pressure changes!):

<a id='f2031896-f1e5-497f-a400-dc703bcfa12c'></a>

```python
print('Altitude: {} meters'.format(sensor.altitude))
```

<a id='784ac68f-e7aa-4ffb-af4c-add35ff18efd'></a>

<::A screenshot of a PuTTY terminal window titled "COM11 - PuTTY". The terminal displays Python code execution and its output. The content shown is:

>>>
>>> sensor.sea_level_pressure = 1013.25
>>> print('Altitude: {} meters'.format(sensor.altitude))
Altitude: 65.8983 meters
>>>
: terminal::>

<a id='5725a28d-ef58-4621-802f-4e112e03afc4'></a>

That's all there is to using the BMP280 sensor with CircuitPython!

<a id='852be16f-505f-4528-a599-84277e33bc34'></a>

© Adafruit Industries

<a id='f4b5dec2-4379-41c6-ba33-dd1933eae22b'></a>

Page 22 of 34

<!-- PAGE BREAK -->

<a id='16d24f0c-fa97-4443-a89a-3dffb6729dc4'></a>

Here's a starting example that will print out the temperature, pressure and altitude every 2 seconds:

<a id='9a6a0536-8b99-4910-b86e-1767fa1b03a5'></a>

# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simpletest Example that shows how to get temperature,
pressure, and altitude readings from a BMP280"""
import time
import board

# import digitalio # For use with SPI
import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a
# microcontroller
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# OR Create sensor object, communicating over the board's default SPI bus
# spi = board.SPI()
# bmp_cs = digitalio.DigitalInOut(board.D10)
# bmp280 = adafruit_bmp280.Adafruit_BMP280_SPI(spi, bmp_cs)

# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    time.sleep(2)

<a id='a8a582af-d44e-44b3-acfa-84ddf4486354'></a>

Python Docs

<a id='033b2137-1235-4d6b-aa27-fc0458da9ee3'></a>

[Python Docs](https://adafru.it/C0B)

<a id='fbed7686-b689-4e9d-8bbb-c053dda72b83'></a>

© Adafruit Industries

<a id='3d585c5d-7b1d-4255-b558-18506bc5ec7f'></a>

Page 23 of 34

<!-- PAGE BREAK -->

<a id='b6ffdaa8-3bf9-4445-b5b7-9ed343d07105'></a>

WipperSnapper

<a id='a8a8b2d8-7405-4fe1-a19d-711dafbd153e'></a>

Shop Learn Blog Forums LIVE! AdaBox IO

adafruit Devices Feeds Dashboards Actions Power-Ups

Hi, Tyeth Gundry | Account 0

New Device

tyeth_demo / Devices

Help

option New Device: [x]

<::transcription of the content
: image::>

Adafruit Feather ESP32 V2
by Adafruit
option Online: [x]
option v1.0.0-beta.69: [x]
option Docs: [ ]
option Purchase: [ ]

+

Get Help
Quick Guides
API Documentation

Learn
IO Plus
News

Connection: Adafruit Feather ESP32 V2

<a id='7a435d7a-ad91-483b-ab9c-84bb3e6bd309'></a>

# What is WipperSnapper
WipperSnapper is a firmware designed to turn any WiFi-capable board into an Internet-of-Things device without programming a single line of code. WipperSnapper connects to [Adafruit IO](https://adafru.it/fsU), a web platform designed (by [Adafruit!](https://adafru.it/Bo5)) to display, respond, and interact with your project's data.

<a id='a0159488-14c9-43be-96fd-293ea2ce3e81'></a>

Simply load the WipperSnapper firmware onto your board, add credentials, and plug it into power. Your board will automatically register itself with your Adafruit IO account.

<a id='62b021b7-fa3d-4daa-b41e-33cb1b549bf4'></a>

From there, you can add components to your board such as buttons, switches, potentiometers, sensors, and more! Components are dynamically added to hardware, so you can immediately start interacting, logging, and streaming the data your projects produce without writing code.

<a id='dbff3046-22cb-4ed5-af10-c74bb36bf1cd'></a>

If you've never used WipperSnapper, click below to read through the quick start guide before continuing.

<a id='014d9b9f-3c2d-4cc4-8803-2d84ab87dadc'></a>

Quickstart: Adafruit IO WipperSnapper

https://adafru.it/Vfd

<a id='10f1e64d-b274-4deb-9ff1-15f1a8a53343'></a>

© Adafruit Industries

<a id='0debbef2-f312-41ea-aef9-6b3448b89910'></a>

Page 24 of 34

<!-- PAGE BREAK -->

<a id='920a7e29-e78a-4039-b1a8-ffaa4ae5379e'></a>

Wiring

<a id='e7f4ae3f-f848-4ed9-a48c-f4f7d5412a77'></a>

First, wire up a BMP280 to your board exactly as follows. Here is an example of the
BMP280 wired to an [Adafruit ESP32 Feather V2](http://adafru.it/5400) using I2C with
a [STEMMA QT cable (no soldering required)](http://adafru.it/4210)

<a id='acae752b-3b51-44fe-9eed-82bce3d7157f'></a>

<::logo: fritzing
fritzing
The logo is a stylized wordmark in a sans-serif font.::>

<a id='c1c47490-73a0-495e-b9c0-8bb59c303b84'></a>

<::A Fritzing diagram showing an electronic circuit on a breadboard. A purple Adafruit ESP32 Huzzah v2 microcontroller board is connected to the breadboard. A black BMP280 Pressure Sensor module is also connected to the breadboard. Jumper wires connect the ESP32 Huzzah v2 board to the breadboard, and the BMP280 sensor to both the breadboard and the ESP32 Huzzah v2 board. The text "fritzing" is at the bottom right of the image.
: circuit diagram::>
fritzing

<a id='515fed8b-52e8-487c-88a1-00b9ee10b97c'></a>

Board 3V to sensor VIN (red wire on
STEMMA QT)
Board GND to sensor GND (black wire on
STEMMA QT)
Board SCL to sensor SCK (yellow wire on
STEMMA QT)
Board SDA to sensor SDI (blue wire on
STEMMA QT)

<a id='7a48a725-1cb9-4bae-af23-f100449bea13'></a>

## Usage

Connect your board to Adafruit IO Wippersnapper and navigate to the [WipperSnapper board list](https://adafru.it/TAu).

<a id='d323e8f9-df5f-4c78-a292-d1ce38880a9e'></a>

On this page, **select the WipperSnapper board you're using** to be brought to the board's interface page.

<a id='b9192a7f-de1b-48b4-a167-0a1c4a05aefd'></a>

©Adafruit Industries

<a id='f4ecb328-9aaf-4583-9071-5d345982e447'></a>

Page 25 of 34

<!-- PAGE BREAK -->

<a id='9c5d021f-89d8-438e-9ef6-1f345fcd10a9'></a>

Shop Learn Blog Forums LIVE! AdaBox IO

Hi, Tyeth Gundry | Account v

0

adafruit Devices Feeds Dashboards Actions Power-Ups New Device

tyeth_demo / Devices

Help

New Device

<::transcription of the content
: figure::>

Adafruit Feather ESP32 V2
by Adafruit
option Online: [x]
option v1.0.0-beta.71: [x]
option Docs: [ ]
option Purchase: [ ]

+


<a id='272c1301-aa21-4509-96f1-98f2eac7de5b'></a>

If you do not see your board listed here - you need [to connect your board to Adafruit IO](https://adafru.it/Vfd) first.

<a id='bb787611-157a-4d02-ba32-5ec0cf3d7b52'></a>

Adafruit Feather ESP32 V2
by Adafruit

Online
v1.0.0-beta.69
Docs
Purchase

<a id='0778a76e-76ff-4544-a598-5499a0178a44'></a>

On the device page, quickly check that
you're running the latest version of the
WipperSnapper firmware.

<a id='0aa6e6be-1047-4076-879b-fda119986c69'></a>

The device tile on the left indicates the version number of the firmware running on the connected board.

<a id='e00be180-ef77-40a3-83a1-12049b9fadb3'></a>

Adafruit Feather ESP32
V2
by Adafruit

Online
v1.0.0-beta.68 Update
Docs
$ Purchase

<a id='336a3ccd-96c4-440a-ba9c-2c22d2b3b524'></a>

If the firmware version is green with a checkmark - continue with this guide.
If the firmware version is red with an exclamation mark "!" - update to the latest WipperSnapper firmware (https://adafru.it/Vfd) on your board before continuing.

<a id='f3ec7bb9-eca3-41ae-a86c-6abed8c89972'></a>

Next, make sure the sensor is plugged into your board and click the **I2C Scan** button.

<a id='f7d07c29-5da2-484a-b1f5-f1c5d27b00e8'></a>

© Adafruit Industries

<a id='82595b65-b738-483e-99b6-eefbf4a99df2'></a>

Page 26 of 34

<!-- PAGE BREAK -->

<a id='2b9d76de-b7b8-4ec7-a3fc-64534a69d347'></a>

adafruit Devices Feeds Dashboards Actions Power-Ups

brubell / Devices / Adafruit Feather ESP32 V2

option New Component: [ ]
option I2C Scan: [ ]
option Device Settings: [ ]

<::transcription of the content
: figure::>

Adafruit Feather ESP32...
Adafruit Feather ESP32 V2 by Adafruit

<a id='3c805601-505d-49d0-94fa-c350c589d8c3'></a>

You should see the BMP280's default I2C address of 0x77 pop-up in the I2C scan list.

<a id='45f73a6c-bf7f-4bf6-91ba-4bf30e683d68'></a>

I2C Scan Complete

<table><thead><tr><th></th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>a</th><th>b</th><th>c</th><th>d</th><th>e</th><th>f</th></tr></thead><tbody><tr><td>00</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td></td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>10</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>20</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>30</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>40</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>50</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>60</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td></tr><tr><td>70</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>--</td><td>77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

Close Scan Again

<a id='9a358ee8-d435-40e9-bf82-520152c4bba8'></a>

---

## I don't see the sensor's I2C address listed!

First, double-check the connection and/or wiring between the sensor and the board.

Then, reset the board and let it re-connect to Adafruit IO WipperSnapper.

---

<a id='739cd844-bc8a-45fe-b36e-81438dd33a22'></a>

With the sensor detected in an I2C scan, you're ready to add the sensor to your
board.

<a id='4abd7ec4-6167-40f5-aceb-c8e8c1336884'></a>

Click the New Component button or the + button to bring up the component picker.

<a id='b8c2c56a-b342-4b54-94cb-4bcbe64976c3'></a>

© Adafruit Industries

<a id='c0a1bf7b-7a7b-4f43-a174-ac20aa10159e'></a>

Page 27 of 34

<!-- PAGE BREAK -->

<a id='9f4b5146-4d82-49a1-b7f9-5c58022bcb17'></a>

tyeth_demo / Devices / Adafruit Feather ESP32 V2                                            ? Help
                                                                                            ⚙️ Settings
➕ New Component   ✨ Auto-Config   I2C Scan

<::Image of a purple Adafruit Feather ESP32 V2 development board with a USB-C port, a WiFi antenna, and various pins. To its right, a large rectangular box with a blue border and a blue circle containing a white plus sign in the center, indicating an empty slot for a new component. A red arrow points from the "New Component" button to the card containing the Adafruit Feather board. Another red arrow points from the center of the large rectangular box with the plus sign to the "New Component" button: diagram::>

Adafruit Feather
ESP32 V2
by Adafruit
✔️ Online
✔️ v1.0.0-beta.69
 Docs
 Purchase

<a id='78179f2c-6ae6-4f40-998b-d9ab6b498c02'></a>

Adafruit IO supports a large amount of components. To quickly find your sensor, type BMP280 into the search bar, then select the **BMP280** component.

<a id='f0c52daf-f00e-45d6-9b81-02d4078c9665'></a>

New Component

Which component would you like to set up?

X BMP280

Displaying 1 matching Components.

<::transcription of the content
: figure::>

<::transcription of the content
: figure::>

<::transcription of the content
: figure::>

ambient-temp
ambient-temp-fahrenheit
pressure
altitude

i2c
BMP280
This little sensor contains
temperature, pressure, and
altitude sensing capabilities.

Product Page
Documentation

Cancel

<a id='937a1fcb-7e76-4b87-bd5a-7d48ef04a43f'></a>

On the component configuration page, the BMP280's sensor address should be listed along with the sensor's settings.

<a id='af88636f-667e-4cf2-b5d1-1c328ea9a2e9'></a>

The **Send Every** option is specific to each sensor's measurements. This option will tell the Feather how often it should read from the **BMP280**'s sensors and send the data to Adafruit IO. Measurements can range from every 30 seconds to every 24 hours.

<a id='90e6d1f5-69a3-441b-9a90-8feab3f5010d'></a>

© Adafruit Industries

<a id='0b45de8e-e2b6-40d9-a5b2-50dedcd6dbd2'></a>

Page 28 of 34

<!-- PAGE BREAK -->

<a id='035282c3-7318-44c2-b6e9-48bc0cff62cf'></a>

For this example, set the **Send Every** interval to every 30 seconds. Don't forget to scroll down as there are 4 sensor metrics / feeds to select. On a small screen you may only see the first 3 and then wonder why altitude isn't updating (it will still be set to the default of every 15 minutes)

<a id='4a308740-c554-4a36-92c8-dfcd9318a43f'></a>

Create BMP280 Component X

Select I2C Address:
0x77

option Enable BMP280: Temperature Sensor (°C)?: [x]
Name:
BMP280: Temperature Sensor (°C)
Send Every:
Every 30 seconds

option Enable BMP280: Temperature Sensor (°F)?: [x]
Name:
BMP280: Temperature Sensor (°F)
Send Every:
Every 30 seconds

option Enable BMP280: Pressure Sensor?: [x]
Name:
BMP280: Pressure Sensor
Send Every:
Every 30 seconds

option Enable BMP280: Altitude (Relative)?: [x]
Name:

<::transcription of the content
: figure::>

← Back to Component Type

Create Component

<a id='f53e15da-a877-44a3-85f5-9c0b8911e665'></a>

Your device interface should now show the sensor components you created. After the interval you configured elapses, WipperSnapper will automatically read values from the sensor(s) and send them to Adafruit IO.

<a id='9b44afb3-7db3-4f75-9109-12333f46f5dc'></a>

©Adafruit Industries

<a id='b709ff47-f46b-4667-9284-c4a8801c6c31'></a>

Page 29 of 34

<!-- PAGE BREAK -->

<a id='35ae41a3-8442-477e-96af-9434108c1cba'></a>

adafruit Devices Feeds Dashboards Actions Power-Ups
New Device

tyeth_demo / Devices / Adafruit Feather ESP32 V2

Help
Settings

option New Component: [x] Auto-Config I2C Scan

<::transcription of the content
: figure::>

BMP280: Altitude (Relative) bmp280:altitude

-32.35m

Create Action I Add to Dashboard

BMP280: Pressure Sensor bmp280:pressure

1017.14hPa

Create Action I Add to Dashboard

Adafruit Feather
ESP32 V2
by Adafruit

BMP280: Temperature Sensor (°C) bmp280:ambient-temp

option Online: [x]
option v1.0.0-beta.70: [x]
Docs
Purchase

26.32°C

Create Action I Add to Dashboard

Report Bugs

BMP280: Temperature Sensor (°F) bmp280:ambient-temp-fahrenheit

79.38°F

Create Action I Add to Dashboard

<a id='c47e795c-a30e-4481-955c-fe99d89f9a85'></a>

To view the data that has been logged from the sensor, click on the graph next to the sensor name.

<a id='79b5245b-6b33-45a3-8cbe-8f249cd0b4ee'></a>

adafruit

Devices Feeds Dashboards Actions Power-Ups

New Device

tyeth_demo/Devices / Adafruit Feather ESP32 V2

Help

New Component Auto-Config I2C Scan

Settings

BMP280: Altitude (Relative) bmp280:altitude

-32.35m

Create Action I Add to Dashboard

BMP280: Pressure Sensor bmp280:pressure

Adafruit Feather
ESP32 V2
by Adafruit

1017.14hPa

Create Action I Add to Dashboard

option Online: [x]
option v1.0.0-beta.70: [x]
option Docs: [x]
option Purchase: [ ]

BMP280: Temperature Sensor (°C) bmp280:ambient-temp

0°
26.34°C

Create Action I Add to Dashboard

Report Bugs

BMP280: Temperature Sensor (°F) bmp280:ambient-temp-fahrenheit

0°
79.41°F

Create Action I Add to Dashboard

<a id='ff84a2bd-458d-44e7-bf21-ea87c46a0e37'></a>

Here you can see the feed history and edit things about the feed such as the name, privacy, webhooks associated with the feed and more. If you want to learn more about how feeds work, [check out this page](https://adafru.it/10aZ).

<a id='34c26e87-5c9c-41f6-9513-391c65fa281a'></a>

© Adafruit Industries

<a id='f9a7eca6-c619-489e-9a29-e08ecf32e3c3'></a>

Page 30 of 34

<!-- PAGE BREAK -->

<a id='ec79fe68-1226-44c3-9b8a-42b53059c438'></a>

<::Logo: adafruit logo::> adafruit Devices Feeds Dashboards Actions Power-Ups <::Button: New Device button with a plus icon::> New Device tyeth_demo / Feeds / BMP280: Pressure Sensor <::Button: Help button with a question mark icon::> <::Line chart: A line chart displaying 'BMP280: Pressure Sensor' data over time. The y-axis ranges from 1,017.125 to 1,017.165. A specific data point is highlighted with a tooltip showing "August 22nd 2023, 6:44:43PM BMP280: Pressure Sensor 1017.14". The legend at the bottom shows a blue square labeled "BMP280: Pressure Sensor".::> <::Icon: Info icon::> Feed Info <::Icon: Gear icon::> Manage feed name, key, description, and tags. <::Icon: Lock icon::> Privacy <::Icon: Gear icon::> This feed is: private. Only you can see it. <::Icon: Share icon::> Sharing <::Icon: Gear icon::> Not shared yet <::Icon: History icon::> Feed History <::Icon: Gear icon::> Feed history is ON Value size is limited to 1KB You have 8 data points from August 22nd 2023, 6:44PM to August 22nd 2023, 6:47PM. + Add Data <::Button: Download All Data button with a download icon and a filter dropdown icon::> Download All Data ▼ Filter < Prev First page 1 of 1 Next > Created at Value Location 2023/08/22 06:48:13PM 1017.166259765625 <::Icon: Red 'X' icon::> 2023/08/22 06:47:43PM 1017.1484985351562 <::Icon: Red 'X' icon::> 2023/08/22 06:47:13PM 1017.1607666015625 <::Icon: Red 'X' icon::> 2023/08/22 06:46:43PM 1017.1490478515625 <::Icon: Red 'X' icon::> <::Icon: Bell icon::> Notifications <::Icon: Gear icon::> This feed is Online You have no notifications active for this feed.

<a id='1fa402d1-27e9-454e-af7f-150d0d299576'></a>

F.A.Q.

---

How come the altitude calculation is wrong? Is my sensor broken?

<a id='c2ca850c-25ab-48d6-95bd-e2d21d815c84'></a>

No, your sensor is likely just fine. The altitude calculation depends on knowing the barometric pressure at sea level

<a id='4ac79cd1-6849-4f3b-9a58-b34b492e9c70'></a>

If you do not set the correct sea level pressure for your location FOR THE CURRENT DAY it will not be able to calculate the altitude accurately

<a id='27939518-8e90-4106-9cbf-6d0edfca4bc4'></a>

Barometric pressure at sea level changes daily based on the weather!

<a id='94a59918-1aed-4d32-be0d-39c55423f5e4'></a>

If I have long delays between reads, the first data read seems wrong?

<a id='e7260af3-b04d-4890-b86a-23db45dad2fe'></a>

The BMx280 'saves' the last reading in memory for you to query. Just read twice in
a row and toss out the first reading!

<a id='259909f9-15f9-4790-8716-77679c754110'></a>

© Adafruit Industries

<a id='8df25a27-524c-474e-a30c-826f056b84e9'></a>

Page 31 of 34

<!-- PAGE BREAK -->

<a id='6947800f-2384-453e-9233-2290c5d581ed'></a>

Downloads

<a id='568369a2-6973-4a03-a9b6-481725f5e40e'></a>

# Documents

* Datasheet for the BMP280 sensor used in the breakout (https://adafru.it/fIO)
* Arduino BMP280 Driver (https://adafru.it/fIK)
* Fritzing object in the Adafruit Fritzing Library (https://adafru.it/Mbx)
* EagleCAD PCB files on GitHub (https://adafru.it/rDq)

<a id='6a3c6cf9-a7f7-41e0-84c5-c22f5e013add'></a>

Schematic - STEMMA QT version

<a id='cd4fc05c-b060-4ef5-94d6-d9e2d5408654'></a>

<::Schematic diagram: schematic::>
### Power supply
*   **Voltage Regulator**: MIC5219-3.3, 3.3V output, with input and output capacitors.
*   **Input/Output Pins**: VCC, GND, IN, OUT, EN, GND, P4.

### ON LED
*   **LED Circuit**: An LED with a current-limiting resistor (100 Ohm) connected to 3.3V and GND.

### I2C Pullups & Shift
*   **Level Shifting**: Two MOSFETs (BSS138) for level shifting SDA and SCL lines between 3.3V and a higher voltage (indicated by VCC).
*   **Pull-up Resistors**: Resistors pulling up SCL/SDA and SCK_3V lines to 3.3V.

### STEMMA/I2C Headers
*   **Connectors**: Two connectors (CONN051 and CONN041) with pins labeled GND, VCC, SDA, SCL, and STEMMA_I2C_QT.

### I2C Pullups
*   **Pull-up Resistors**: Resistors pulling up CS_3V, SDO/ADO, and SCL/SDA lines to 3.3V.

### BMP280 Digital Pressure Sensor
*   **Component**: BMP280 Digital Pressure Sensor with pins VDD, VIO, GND, CSB, SDO, SDI, SCL, SDA.
*   **Capacitors**: Decoupling capacitors (C19, C18).
*   **Temperature Range**: -40°C ~ +85°C.

### Additional Connector
*   **Connector J1**: Pins for VCC, SDA, SCL, SDO/ADO, CS.
<::

<::Schematic Title Block: table::>
| BMP280 rev C |
| :--- |
| **Date**: 1/15/20 13:09 |
| **Drawing**: >AUTHOR |
| **Sheet**: 1/1 |
| **Company**: Adafruit Industries |
| **Logo**: Adafruit logo (a stylized flower) |
<::

<a id='f56eae2e-6dcb-4f5d-929a-c51e44427501'></a>

© Adafruit Industries

<a id='49e6dce2-81ba-42d9-8a4f-cab9ea9aa909'></a>

Page 32 of 34

<!-- PAGE BREAK -->

<a id='f3fb1a64-ee98-4a00-a0d5-5be8650da304'></a>

Fab Print - STEMMA QT version

<a id='88b11199-0267-41dd-ad6b-2011f966beb0'></a>

<::A circuit board layout with dimensions. The board is rectangular with rounded corners. Various components and traces are visible in red, blue, and magenta. Several labels are printed on the board, some of which are mirrored. Around the board, dimension lines indicate measurements. The top dimension is 0.80. The left vertical dimension is 0.10. The right vertical dimensions are 0.50 and 0.70. The bottom horizontal dimension is 1.00. Labels on the board include: P$1 (twice), mirrored "BMP580", mirrored "temperature sensor", mirrored "I2C addr 0x76", mirrored "I2C addr 0x77", mirrored "VDDIO ACC 3-5VDC", and pin labels such as SCL, SDA, CSB, SDO, GND, VCC. There are also labels "16Mhz" on the right side and "2" on the left side.: figure::>

<a id='0cc09a8c-c80c-412c-9da5-6522796722d1'></a>

Schematic - Original version

<a id='4b5a36de-e5c2-4fa2-80f0-b8bd2e0152fc'></a>

Click to enlarge. BMP280 shares the same package & pinout as the BME280 so the schematic is the same

<a id='097cef43-a138-4309-8e43-d7e9d1dd5fb5'></a>

LEVEL SHIFTING (5U <--> 3U)
<::A schematic diagram showing level shifting and a voltage regulator.
- **Level Shifting Circuit:**
  - Two channels for level shifting between 3.3V and 5V. Each channel uses two pull-up resistors (to 3.3V and 5V respectively) and a BSS138 MOSFET.
  - The first channel connects "SCK/SCL 3V" to "SCK/SCL 5V".
  - The second channel connects "SDI/SDA 3V" to "SDI/SDA 5V".
  - There are also connections for "SDO/ADR 3V" and "CSB 3V" to "SDO/ADR 5V" and "CSB 5V" respectively, through pull-up resistors.
- **Voltage Regulator (U2):**
  - A MIC5225-3.3 voltage regulator with 5V input (IN) and 3.3V output (OUT).
  - The enable (EN) pin is connected to 5V.
  - Input and output capacitors are connected to ground (GND).
: schematic diagram::>
For SPI set CSB lou at startup
SDO=MISO, SDI=MOSI, SCK=SCK, CSB=CS/SSEL
For I2C leave CSB pulled high (default value)
SDI=SDA, SCK=SCL

<::A schematic diagram showing a BME280 sensor, a pin header, and document information.
- **BME280 Digital Environment Sensor (U1):**
  - Pins: VDD (connected to 3.3V), SDO (connected to SDO/ADR 3V), CSB (connected to CSB 3V), SCK (connected to SCK 3V), SDI (connected to SDI 3V), and GND.
  - Operating temperature range: -40°C to 85°C.
- **8-pin Header (JP2):**
  - Pins 1-8 are connected to 3.3V, 5V, SDO/ADR 3V, SCK/SCL 3V, SDI/SDA 3V, CSB 3V, and GND.
- **Document Footer:**
  - Logo: Adafruit
  - Filename: Adafruit_BME280_SPI_REU-B
  - Date/Time: 6/21/2015 2:19:58 PM
  - Sheet: 1/1
  - Drawing: >AUTHOR
  - Company: Adafruit Industries
: schematic diagram::>

<a id='dc1fb7b3-0fb2-4af5-97a7-0c7b6870086e'></a>

<::logo: Adafruit
adafruit
The logo features a stylized red flower symbol next to the word "adafruit" in a sans-serif font.::>

<a id='6cc22c7c-2869-44af-8d26-d9aad6daad9a'></a>

©Adafruit Industries

<a id='1fc2ea80-9d5a-4e93-8a3e-7951934f6582'></a>

Page 33 of 34

<!-- PAGE BREAK -->

<a id='70cbeba7-b7f2-4e3d-b708-564deb1787f9'></a>

## Fab Print - Original version

In inches. BMP280 shares the same package & pinout as the BME280 so the layout is the same

<a id='5328d105-2ec1-4950-8ff8-5247c04fcca3'></a>

<::Diagram of a BME280 Pressure, Temperature, and Humidity sensor module with dimensions. The module is rectangular with four mounting holes, one at each corner. The top surface of the module has the text "BME280 Pressure Temp+Humidity" and various electronic traces and components visible. Along the bottom edge, there are solder pads labeled: VIN, GND, SDO, CS, 3Vo, SCK, SDI.  Dimensions are indicated around the module:
- Overall width: 0.7
- Width between mounting holes: 0.5
- Overall height: 0.75
- Height between mounting holes: 0.65
- Edge spacing for mounting holes (top left): 0.08
- Edge spacing for mounting holes (bottom left): 0.1
: diagram::>

<a id='706fc170-1535-46fb-ba18-6d301849b8d1'></a>

© Adafruit Industries

<a id='03bd7ddc-1365-4e41-bf1b-e789b4376aa2'></a>

Page 34 of 34