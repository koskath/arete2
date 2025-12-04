<a id='535e2acd-40ba-4b9b-8d21-55271da4aa1d'></a>

<::logo: [Unknown] [No readable text] A black five-petal flower with white circular centers.::>

<a id='9db75b1e-1e78-426a-9f2d-5e7f9bc8b834'></a>

Adafruit MMA8451 Accelerometer
Breakout

<a id='02ba2b68-9276-417d-9d99-12175432d808'></a>

Created by lady ada

<a id='fcbd330c-caa6-4f81-ae08-944d6b5166a5'></a>

<::A close-up photograph of an Adafruit MMA8451 accelerometer breakout board. The board is a small, square blue PCB with gold-plated circular pads for connections. The top surface of the board shows various surface-mount components, including a central black integrated circuit (IC) labeled "263", "8451", and "3CZR". Around the IC are several smaller black components labeled "1002" and "2001", as well as tan-colored capacitors. White silkscreen text on the board includes "MMA8451" prominently, along with an X-Y-Z axis indicator with a star symbol. Connection labels visible are "VIN", "GND", "3V0", "I1", "I2", "SDA", and "SCL". The board is set against a dark, textured background. https://learn.adafruit.com/adafruit-mma8451-accelerometer-breakout
: figure::>

<a id='7f8ecc55-68e4-43be-8e42-c17f773382a3'></a>

Last updated on 2024-09-26 02:04:40 PM EDT

<a id='b1b2a99c-4935-41c8-99db-fe2b22ffab5c'></a>

© Adafruit Industries

<a id='a36a9f3f-8797-436d-bd0b-e9abdb83a950'></a>

Page 1 of 21

<!-- PAGE BREAK -->

<a id='8276e374-eaa6-4951-9e6b-8f3199f3168f'></a>

# Table of Contents

<a id='f2ca0120-f8eb-4494-bbba-e0acff9f14c1'></a>

<table id="1-1">
<tr><td id="1-2">Overview</td><td id="1-3">3</td></tr>
<tr><td id="1-4">Pinouts</td><td id="1-5">5</td></tr>
<tr><td id="1-6">• Power Pins</td><td id="1-7"></td></tr>
<tr><td id="1-8">• I2C Pins</td><td id="1-9"></td></tr>
<tr><td id="1-a">• INT and ADDR Pins</td><td id="1-b"></td></tr>
</table>

<a id='40932434-6ee0-4a5c-89bd-85a81cc6da48'></a>

## Assembly

---
*   Prepare the header strip:
*   Add the breakout board:
*   And Solder!

6

<a id='5f5d023d-83c7-4022-a4c6-e3c191c2cef8'></a>

# Arduino Code

*   Download Libraries
*   Load Demo
*   Library Reference
*   Set & Get Range
*   Read Raw Count Data
*   Reading Normalized Adafruit_Sensor data
*   Read Orientation

9

<a id='bdcc6076-37a6-4c8f-a085-1be35eb4d9ae'></a>

# Python & CircuitPython

* CircuitPython Microcontroller Wiring
* Python Computer Wiring
* CircuitPython Installation of MMA8451 Library
* Python Installation of MMA8451 Library
* CircuitPython & Python Usage
* Full Example Code

15

<a id='7a243c17-d485-477a-82a5-1bae1c690676'></a>

Python Docs 20
---


<a id='b28f61ca-e2a7-4158-8493-7b652efeac7a'></a>

20

---

## Downloads

*   Datasheet & Files
*   Schematics
*   Fabrication print

<a id='29447ae0-ca4f-411d-a24c-1a27f24fb6f6'></a>

©Adafruit Industries

<a id='c22fbeec-8809-446f-a1ce-03101a9efc97'></a>

Page 2 of 21

<!-- PAGE BREAK -->

<a id='37337ca8-c52a-457d-ac64-291ebcc3fc1d'></a>

Overview

<a id='6e547731-f5d0-4e2e-86ae-eb942e2024a9'></a>

<::A close-up, angled view of a small blue square circuit board (PCB) labeled "MMA8451". The board features several surface-mount components, including a central integrated circuit (IC) marked "261", "8451", and "3CZR". Around the IC, there are multiple resistors or capacitors marked "1002" and "2001".

Along the edges of the board, there are several through-hole pads labeled with functions: "VIN", "GND", "3V0", "I1", "I2", "SDA", "SCL", and "A". In the top right corner of the board, there is a silkscreened symbol indicating X, Y, and Z axes.
: figure::>

<a id='72571bb3-461e-48e4-903f-16059a1e27a0'></a>

You can detect motion, tilt and basic orientation with a digital accelerometer - and the
MMA8451 is a great accelerometer to start with. It's low cost, but high precision with
14-bit ADC. It has a wide usage range, from +-2g up to +-8g yet is easy to use with
Arduino or another microcontroller

<a id='66cbbcbe-1c88-4284-bca3-dc8ded951f18'></a>

The MMA8451 is a miniature little accelerometer from Freescale, who are (by this point) masters at the accelerometer-design game. It's designed for use in phones, tablets, smart watches, and more, but works just as well in your Arduino project. Of the MMA8451/MMA8452/MMA8453 family, the MMA8451 is the most precise with a built in 14-bit ADC. The accelerometer also has built in tilt/orientation detection so i can tell you whether your project is being held in landscape or portrait mode, and whether it is tilted forward or back

<a id='87a13a24-606d-4144-8584-10984e0e9af8'></a>

©Adafruit Industries

<a id='6337dc30-8ccd-43b2-972f-a16dd4747121'></a>

Page 3 of 21

<!-- PAGE BREAK -->

<a id='7aaa2926-f4a4-4d80-a9a9-d4cb232dee6f'></a>

<::A blue rectangular PCB (Printed Circuit Board) with various electronic components, labeled "MMA8451", "VIN", "3V0", "I1", "SDA", "GND", "I2", "SCL", and "A". It also shows x, y, z axis labels. Next to it is an 8-pin male header.
: figure::>

<a id='a66fb004-be97-4cb3-a359-6d3e8453fb15'></a>

<::A close-up image of a small blue circuit board, labeled 'MMA8451' prominently in white text near the top center. The board features various surface-mount components, including an integrated circuit chip in the center with text that appears to be '451J'. Around the chip are several smaller rectangular components, some labeled '1002'. In the top right corner, there is a white graphic indicating X, Y, and Z axes with arrows. Along the bottom edge of the board, there are solder pads or pin headers labeled from left to right: 'GND', 'VIN', '3V3', 'I1', 'I2', 'SDA', 'SCL', and 'A'. There are also mounting holes in each corner of the board.
: figure::>

<a id='3c80d188-ccdb-4e73-8359-e8fad4617512'></a>

This sensor communicates over I2C so you can share it with a bunch of other sensors on the same two I2C pins. There's an address selection pin so you can have accelerometers share an I2C bus. Please note this chip requires repeated-start I2C support (in case you are looking to port this to another processor)

<a id='98d736db-5dbe-49e8-83e0-e82dee62ebf7'></a>

<::A small blue circuit board, labeled "adafruit! 3-Axis 14-Bit Accelerometer", with specifications "±2/±4/±8g" and "5V Safe". It has two mounting holes at the top and eight circular solder pads at the bottom. The circuit board is placed next to a US quarter coin, showing the obverse side with George Washington's profile, and the text "LIBERTY", "IN GOD WE TRUST", "1998", and "P" (mint mark). This visual compares the size of the accelerometer to the quarter.
: figure::>

<a id='20c6a992-d426-4d18-9a7e-53c3653a0543'></a>

<::A blue circuit board with white text and gold-colored circular pads.The text reads:adafruit!3-Axis 14-BitAccelerometer±2/±4/±8g5V SafeThere are 8 circular pads along the bottom edge and two larger circular pads near the top corners.: figure::>

<a id='b9d88452-7928-43cb-9536-b51c7eb135d6'></a>

To get you going fast, we spun up a breakout board for this little guy. Since it's a 3V sensor, we add a low-dropout 3.3V regulator and level shifting circuitry on board. That means its perfectly safe for use with 3V or 5V power and logic.

<a id='68195183-fdcc-44db-ab6a-de8f1cadcfef'></a>

© Adafruit Industries

<a id='e330803e-b1b1-463b-9d93-e8a6d32f3b18'></a>

Page 4 of 21

<!-- PAGE BREAK -->

<a id='e040f59b-ee31-4b73-bfad-fcef653fd455'></a>

Pinouts

<a id='37f12efa-4235-4be9-bf4b-724f8b792555'></a>

<::A close-up overhead view of a small, rectangular blue circuit board, likely an accelerometer breakout board. The board features several surface-mount components, including a central integrated circuit, various resistors (some labeled "1002"), and capacitors. Along the bottom and left edges, there are gold-plated through-holes for connecting wires, labeled with functions: "VIN", "GND", "3V0", "I1", "I2", "SCL", "SDA", and "A". In the top center, the model number "MMA8451" is printed in white text, along with a star-shaped logo. To the right of the model number, an orthogonal coordinate system with arrows indicates the X, Y, and Z axes. There are two larger, gold-plated mounting holes in the top left and top right corners of the board. The background is a dark, textured surface.: circuit board::>

<a id='a6fe834e-a909-4e56-835b-b9e0fdde1fc3'></a>

The little chip in the middle of the PCB is the actual MMA8451 sensor that does all the motion sensing. We add all the extra components you need to get started, and 'break out' all the other pins you may want to connect to onto the PCB. For more details you can check out the schematics in the Downloads page.

<a id='f60e80e2-4ee4-48dc-9bd9-9b993ec1bef4'></a>

# Power Pins
The sensor on the breakout requires 3V power. Since many customers have 5V microcontrollers like Arduino, we tossed a 3.3V regulator on the board. Its ultra-low dropout so you can power it from 3.3V-5V just fine.
*   **Vin** - this is the power pin. Since the chip uses 3 VDC, we have included a voltage regulator on board that will take 3-5VDC and safely convert it down. To power the board, give it the same power as the logic level of your microcontroller - e.g. for a 5V micro like Arduino, use 5V
*   **3Vo** - this is the 3.3V output from the voltage regulator, you can grab up to 100mA from this if you like
*   **GND** - common ground for power and logic

<a id='326cd89a-9935-498e-893f-194c4fd19874'></a>

# I2C Pins

* SCL - I2C clock pin, connect to your microcontrollers I2C clock line.
* SDA - I2C data pin, connect to your microcontrollers I2C data line.

<a id='33b672a7-3ab6-4c86-832d-925aa07dabaa'></a>

© Adafruit Industries

<a id='88bada5a-76e7-4b41-83ac-bacfea81e43b'></a>

Page 5 of 21

<!-- PAGE BREAK -->

<a id='9e79289c-7612-46a1-b391-594a22455629'></a>

## INT and ADDR Pins

*   A is the I2C Address select pin. By default this is pulled up to 3.3V with a 10K resistor, for an I2C address of 0x1D. You can also connect it to the GND pin for an address of 0x1C
*   I1 and I2 are the Interrupt #1 and #2 signal pins. These pins are for more advanced usage, where you want to be alerted by the chip say when data is ready to read, or if it detects a large motion. We don't have direct support in the example Arduino library for these pins, so please check the datasheet for the I2C commands

<a id='d8b876ed-32eb-4d45-b340-a374029569a2'></a>

Assembly
<::A top-down view of a small, square, blue circuit board (MMA8451) and a separate 8-pin male header. The circuit board has various surface-mount components, an integrated circuit, and through-hole pads labeled "VIN", "GND", "3V0", "I1", "I2", "SDA", "SCL", and "A". An X, Y, and Z axis indicator is present near the top right of the board. The pin header has eight gold-colored pins extending from a black plastic base. Both components are displayed on a dark grey background.: figure::>

<a id='054443c8-4bbc-4d50-983c-ef05c0b85a4f'></a>

<::A small, blue square circuit board with various electronic components. In the center, a black integrated circuit is visible. Several smaller components, including resistors and capacitors, are scattered across the board. Along the bottom edge, there are solder pads labeled "VIN", "3V0", "I1", "SDA", "GND", "I2", "SCL", and "A". Two mounting holes are present in the top corners. Near the top center, the text "MMA8451" is printed, accompanied by a star logo and a coordinate system with X, Y, and Z axes. The components have markings such as "1002" and "200T".: circuit board::>

<a id='33f2d908-fc6d-4b0b-a6db-3b49d549d6c1'></a>

<::A white breadboard is shown, viewed from slightly above. The breadboard has two main sections, separated by a central channel. Both the top and bottom sections feature power rails running horizontally along their edges. The top section has a red line marked with a '+' and a blue line marked with a '-' on the upper edge, and similar red and blue lines on the lower edge. The main prototyping area in both sections is marked with columns labeled 'a' through 'e' on the left side and 'f' through 'j' on the right side, with rows numbered 1 through 30 running vertically down the center. In the central channel of the breadboard, a black, 8-pin male header or integrated circuit is inserted into the holes. The numbers on the breadboard are arranged such that 1-30 are visible along the central channel, and the lettered columns are on the outer edges. The positive and negative rails are clearly marked with red and blue lines respectively, and plus and minus signs.::>

<a id='1c85103e-6c3d-4443-8d8e-a5a795e9f9df'></a>

Prepare the header strip:
Cut the strip to length if necessary. It will
be easier to solder if you insert it into a
breadboard - **long pins down**

<a id='6fef3dad-2c84-4d1f-934d-7592628d4323'></a>

©Adafruit Industries

<a id='95705c0a-2d14-486e-8bff-f5daf7d9302d'></a>

Page 6 of 21

<!-- PAGE BREAK -->

<a id='ee9e36ca-0b2a-4616-b718-23a92350afd1'></a>

<::A close-up photograph shows a small, rectangular blue circuit board, labeled "MMA8451", resting on a white breadboard. The circuit board features a central integrated circuit (IC) chip surrounded by numerous smaller surface-mount components like resistors and capacitors. Along one edge of the board, there are eight gold-plated circular pads, labeled from left to right as "VIN", "GND", "3V0", "I1", "I2", "SDA", "SCL", and "A". Above the "MMA8451" text, there is a star logo and an arrow diagram indicating X, Y, and Z axes. The breadboard beneath has rows and columns of connection holes, with numbers visible along its edges, ranging from "6" to "23" vertically and horizontally, suggesting its grid layout.: figure::>

<a id='f1476b11-f1f2-4c46-8ebc-583898d3a1fc'></a>

<::A close-up image of a blue printed circuit board (PCB) for an MMA8451 accelerometer module. The board features several surface-mount components, including the main MMA8451 chip in the center. At the top, there's a star logo and the text "MMA8451", along with an arrow diagram indicating X, Y, and Z axes. Along the bottom edge, there are gold-plated through-hole pins labeled from left to right as: VIN, GND, 3V3, I2, SDA, SCL, and A. Other smaller components like resistors and capacitors are visible across the board.: figure::>

<a id='004e1197-21e7-430e-a1c2-9dc8145e5703'></a>

Add the breakout board:
Place the breakout board over the pins so
that the short pins poke through the
breakout pads

<a id='3917ef93-fcff-480c-9967-6b964b8e3c64'></a>

© Adafruit Industries

<a id='2096a5f1-30dd-44f3-84b2-6471e5b00cb0'></a>

Page 7 of 21

<!-- PAGE BREAK -->

<a id='430b149e-5c96-40ed-871e-52f7c014ba7b'></a>

<::A hand holds a wire, and a soldering iron is applied to connect the wire to the SCL pin of a blue MMA8451 sensor module, which is inserted into a white breadboard. The breadboard has rows labeled 1-30 and columns a-e and f-j.: figure::>
<::A close-up of the blue MMA8451 sensor module mounted on a breadboard. The module is labeled 'MMA8451' with X, Y, Z axes indicators, and pins labeled 'UIN', 'GND', 'I2', 'I1', 'SDA', 'SCL', and 'A'. A wire is connected to the 'SCL' pin, with a soldering iron tip visible near the connection point.: figure::>
<::A hand is shown connecting a wire to the SCL pin of the MMA8451 sensor module on a breadboard, using a soldering iron to secure the connection.: figure::>

<a id='e302d562-9a99-4d53-baf8-9a29a517e626'></a>

<::logo: [Unknown]MMA8451This logo features a small blue circuit board with various electronic components, including a central black chip and several smaller resistors and capacitors.::>

<a id='d2f5e62c-55a4-4302-8089-660f7326bb42'></a>

# And Solder!

Be sure to solder all pins for reliable electrical contact.

<a id='6cf3388b-941a-44b4-a4d8-ac180bb188d7'></a>

(For tips on soldering, be sure to check out our [Guide to Excellent Soldering](https://adafru.it/aTk)).

<a id='99dbc2b4-45ce-41dd-a3fe-36ef3cbabbb8'></a>

©Adafruit Industries

<a id='15ad0d5f-ca7a-43e4-89a9-9ed7614ce9b3'></a>

Page 8 of 21

<!-- PAGE BREAK -->

<a id='d2b48cec-c662-4bb2-8012-d885eea3430d'></a>

<::A blue MMA8451 accelerometer module circuit board is mounted on a white breadboard. The board has various surface-mount components, including an integrated circuit in the center. Markings on the board include "MMA8451", an arrow indicating X, Y, and Z axes, a star symbol, and several pin labels along the bottom edge: VIN, GND, I1, I2, SDA, SCL, and A. Other visible markings include "1002" on some components and "3Uo". There are two gold-colored mounting holes on the top corners of the board.
: figure::>

<a id='acdc07b9-3971-47b9-b510-755bce8e29af'></a>

<::A close-up image of a blue circuit board with various electronic components. Several integrated circuits (ICs), resistors, and capacitors are visible. Along the bottom edge of the board, there are solder points labeled from left to right: "VIN", "GND", "3V0", "I1", "I2", "SDA", "SCL", and "A". Some resistors have "1002" printed on them. There is a central black IC and smaller black ICs and other components scattered across the board.
: figure::>

<a id='c42f2496-3515-4f42-ba31-16a7b726008c'></a>

You're done! Check your solder joints visually and continue onto the next steps

<a id='684e3e7e-2bdb-45f2-9d66-c9d117078760'></a>

# Arduino Code
You can easily wire this breakout to any microcontroller, we'll be using an Arduino. For another kind of microcontroller, just make sure it has I2C with **repeated-start support**, then port the code - its pretty simple stuff!

<a id='0c1f4bea-da07-4950-879c-b76d4ebc6680'></a>

<::An image showing an Arduino Uno board connected to a white breadboard with an MMA8451 sensor module. The Arduino Uno is a blue circuit board with various components, including a USB-B port, a power jack, a large microcontroller chip, and several pin headers labeled 'DIGITAL (PWM~)', 'ANALOG IN', 'POWER', 'IOREF', and 'RESET'. The digital pins are numbered 0 through 13, and analog pins A0 through A5. Power pins include 5V, GND, and Vin. The breadboard has numbered rows from 1 to 30 and lettered columns from a to j, with power rails marked with '+' and '-' symbols along the long edges. The MMA8451 sensor module is a small blue PCB located on the breadboard, connected across rows 13 to 20 and columns f to j. It has pins labeled VIN, GND, SCL, SDA, 3V3, INT1, and INT2. The wiring connections are as follows: A red wire connects the Arduino's 5V pin to the positive power rail of the breadboard (around row 17). A black wire connects the Arduino's GND pin to the negative power rail of the breadboard (around row 18). Another red wire connects the breadboard's positive power rail (row 21) to the VIN pin of the MMA8451 module (row 20, column f). Another black wire connects the breadboard's negative power rail (row 21) to the GND pin of the MMA8451 module (row 19, column f). A green wire connects the Arduino's A4 (SDA) pin to the SDA pin of the MMA8451 module (row 14, column f). A blue wire connects the Arduino's A5 (SCL) pin to the SCL pin of the MMA8451 module (row 15, column f).: figure::>

<a id='914a5093-1e97-4648-8dc9-6d410963b74f'></a>

* Connect **Vin** to the power supply, 3-5V is fine. Use the same voltage that the microcontroller logic is based off of. For most Arduinos, that is 5V
* Connect **GND** to common power/data ground
* Connect the **SCL** pin to the I2C clock **SCL** pin on your Arduino. On an UNO & '328 based Arduino, this is also known as **A5**, on a Mega it is also known as **digital 21** and on a Leonardo/Micro, **digital 3**

<a id='e9c7bcae-9c01-4bdf-87a4-5026945d5b39'></a>

© Adafruit Industries

<a id='1957814d-5b4f-4441-a2ba-8d413681453b'></a>

Page 9 of 21

<!-- PAGE BREAK -->

<a id='7e4192d3-73b6-4b03-8b56-635cbc8a0e33'></a>

• Connect the **SDA** pin to the I2C data **SDA** pin on your Arduino. On an UNO &
'328 based Arduino, this is also known as **A4**, on a Mega it is also known as
digital **20** and on a Leonardo/Micro, digital **2**

<a id='730b6ad9-9c87-41f3-8f0f-611ef78b9e9e'></a>

The MMA8451 has a default I2C address of **0x1D** and can be changed to 0x1C by tying the **A** pin to GND

<a id='b0159450-72b0-4b5d-b523-282cfcbaa8a4'></a>

## Download Libraries
To begin reading sensor data, you will need to download the Adafruit_MMA8451 library and the Adafruit_Sensor library from the Arduino library manager.

<a id='67c78e06-298a-4a06-99dc-9e1f0b9d29a8'></a>

Open up the Arduino library manager: <::A screenshot of the Arduino IDE (version 1.8.4) titled "demo". The menu bar shows File, Edit, Sketch, Tools, and Help. The "Sketch" menu is open, displaying options such as "Verify/Compile", "Upload", "Upload Using Programmer", "Export compiled Binary", "Show Sketch Folder", "Include Library", and "Add File...". The "Include Library" option has a sub-menu open to its right, showing "Manage Libraries..." highlighted, followed by "Add .ZIP Library...", a header "Arduino libraries", and then a list of libraries including "ArduinoHttpClient", "ArduinoSound", "AudioZero", and "Bridge". This visual demonstrates the steps to access the library manager by selecting "Sketch" > "Include Library" > "Manage Libraries...".: figure::>

<a id='88487957-a3a7-40cc-ba3c-a775342a60e1'></a>

Search for the **Adafruit MMA8451** library and install it

<a id='022e90cd-309e-4718-be3c-0ce55cf530e5'></a>

Type All Topic All adafruit mma8451

Adafruit MMA8451 Library by Adafruit

Arduino library for the MMA8451 Accelerometer sensors in the Adafruit shop

More info

Version 1.... Install

<a id='063df122-38c7-4267-b4b0-75f8014b21fa'></a>

Search for the **Adafruit Sensor** library and install it

<a id='5ce1f4e6-3ea9-49fd-b0a0-3a5465f1c992'></a>

Library Manager

Type All
Topic All
Adafruit_Sensor

Adafruit Unified Sensor by Adafruit Version 1.0.2 INSTALLED
Required for all Adafruit Unified Sensor based libraries. A unified sensor abstraction layer used by many Adafruit sensor libraries.
More info

<a id='8178dae0-1aad-43f4-b106-fdc90cc786de'></a>

We also have a great tutorial on Arduino library installation at:
http://learn.adafruit.com/adafruit-all-about-arduino-libraries-install-use (https://
adafru.it/aYM)

<a id='4882cae6-fe34-40df-afef-ad048d23b4f0'></a>

© Adafruit Industries

<a id='cfbfa48d-91d8-4552-bf69-b15e412252ed'></a>

Page 10 of 21

<!-- PAGE BREAK -->

<a id='d674b632-e760-4801-b8ed-0a153c1715cd'></a>

# Load Demo
Open up File->Examples->Adafruit_MMA8451->MMA8451demo and upload to your Arduino wired up to the sensor

<a id='e3ef445b-6418-4977-90d8-5fb2e188f4f6'></a>

MMA8451demo | Arduino 1.0.5 File Edit Sketch Tools Help New Ctrl+N Open... Ctrl+O Sketchbook Examples Close Ctrl+W Save Ctrl+S Save As... Ctrl+Shift+S Upload Ctrl+U Upload Using Programmer Ctrl+Shift+U Page Setup Ctrl+Shift+P Print Ctrl+P Preferences Ctrl+Comma Quit Ctrl+Q <::A dropdown menu is shown, with 'Examples' highlighted. To the right of 'Examples', a second-level dropdown menu displays a list of Adafruit libraries. The option 'Adafruit_MMA8451' is highlighted in this second menu. To the right of 'Adafruit_MMA8451', a third-level dropdown menu is open, showing 'MMA8451demo'. Above this, next to 'Adafruit_MAX21000', there is a truncated snippet that looks like a code comment, '***********/' : dropdown_menu::> Adafruit_LSM9DS0 > Adafruit_MAX21000 ***********/ > Adafruit_MAX21100 > Adafruit_MAX31855 > Adafruit_MCP23008 > Adafruit_MCP23017 > Adafruit_MCP4725 > Adafruit_MCP9808 > Adafruit_MiniMLX9014 > Adafruit_MLX9014 > Adafruit_MMA8451 MMA8451demo > Adafruit_MotorShield > Adafruit_MPL115A2 ce code, > Adafruit_MPL3115A2 ng > Adafruit_MPR121 > Adafruit_MPU9150 > Adafruit_NECremote

<a id='d0ff6e49-2288-469e-9e77-27c657cbd0f4'></a>

(https://adafru.it/dLL)
Thats it! Now open up the serial terminal window at 9600 speed to begin the test.

<a id='b4de92ca-1dbb-4929-8da2-bd1d0dd1912c'></a>

© Adafruit Industries

<a id='8563cbde-0527-4172-a0d1-8472961616b1'></a>

Page 11 of 21

<!-- PAGE BREAK -->

<a id='7458bfba-dbbc-47a1-a19b-23420682f7fa'></a>

COM70
Send

Adafruit MMA8451 test!
MMA8451 found!
Range = 8G
X: 45 Y: -672 Z: 734
X: 0.05 Y: -0.65 Z: 0.71 m/s^2
Portrait Up Front

X: 86 Y: -807 Z: 646
X: 0.07 Y: -0.77 Z: 0.62 m/s^2
Portrait Up Front

X: -767 Y: 75 Z: 656
X: -0.75 Y: 0.07 Z: 0.64 m/s^2
Landscape Left Front

X: -862 Y: 266 Z: 545
X: -0.85 Y: 0.26 Z: 0.54 m/s^2
Landscape Left Front

X: -880 Y: -268 Z: 10
X: -0.88 Y: -0.25 Z: 0.01 m/s^2
Landscape Left Front

X: 136 Y: -171 Z: -881
X: 0.14 Y: -0.17 Z: -0.88 m/s^2
Landscape Left Back

X: 536 Y: -96 Z: -805
X: 0.53 Y: -0.10 Z: -0.79 m/s^2
Landscape Right Back

X: 732 Y: 1107 Z: -161
X: 0.70 Y: 1.19 Z: -0.13 m/s^2
Portrait Down Back

option Autoscroll: [x]
option No line ending: [x]
option 9600 baud: [x]

<a id='eb0a1157-e310-4318-a218-7c173a5705c6'></a>

There's three lines of output from the sensor.

<a id='d0d89f7c-c02c-45ef-a6ef-abffa79ce4c0'></a>

Example for line 1:

<a id='6cc6b37a-670c-4e78-8af4-c2a55272f8ab'></a>

X: 45 Y: -672 Z: 734

<a id='8a754178-c418-434d-ab72-8efcf3efd0e7'></a>

This is the "raw count" data from the sensor, its a number from -8192 to 8191 (14 bits)
that measures over the set range. The range can be set to 2G, 4G or 8G

<a id='e74f65cb-7cdc-4180-ae38-10459f86e7d9'></a>

Example for line 2:
X: -0.07 Y: 0.09 Z: 9.8 m/s^2

<a id='4ea06c18-a0fb-4b9c-84a8-0d61c92b6a47'></a>

This is the Adafruit_Sensor'ified nice output which is in m/s*s, the SI units for measuring acceleration. No matter what the range is set to, it will give you the same units, so its nice to use this instead of mucking with the raw counts. (Note that the screenshot above has the m/s^2 divided by 10, you can ignore that typo :)

<a id='1d897519-4040-44f5-81f2-a0dc47de4535'></a>

 Adafruit Industries

<a id='4403bc10-d7d6-4f13-b748-5e3aef678a4f'></a>

Page 12 of 21

<!-- PAGE BREAK -->

<a id='a3332959-f0eb-4853-9844-15eb6a4983b3'></a>

Example for line 3:

Portrait Up Front

<a id='226f77fe-082d-4686-8b90-372af7565630'></a>

This is the output of the orientation detection inside the chip. Since inexpensive accelerometers are often used to detect orientation and tilt, this sensor has it built in. The orientation can be Portrait or Landscape, then Up/Down or Left/Right and finally tilted forward or tilted back. Note that if the sensor is tilted less than 30 degrees it cannot determine the forward/back orientation. If you play with twisting the board around you'll get the hang of it.

<a id='d0860328-60cf-47cb-bbe3-9268b3df9888'></a>

Library Reference
The library we have is simple and easy to use

<a id='ed4eac47-8378-4f01-85a1-4519c0b3217d'></a>

You can create the **Adafruit_MMA8451** object with:
```
Adafruit_MMA8451 mma = Adafruit_MMA8451();
```
There are no pins to set since you must use the I2C bus!

<a id='22a284c3-fea0-4cdf-a5dc-b2609b1560d5'></a>

Then initialize the sensor with:

```
mma.begin()
```

<a id='1369a757-ed36-41dc-9e41-bfe92d344685'></a>

this function returns **True** if the sensor was found and responded correctly and **False** if it was not found. We suggest something like this:

```
if (! mma.begin()) {
Serial.println("Couldnt start")
while (1);
}
Serial.println("MMA8451 found!");
```

<a id='6e39bee1-f0ef-4eec-9cc2-ddbf2c24b20e'></a>

Set & Get Range
You can set the accelerometer max range to 2g, 4g or 8g with

<a id='69e5c8c8-408a-4a0a-a63e-e093fee3c3bf'></a>

<table id="12-1">
<tr><td id="12-2">mma.setRange(MMA8451 RANGE 2 G);</td><td id="12-3"></td></tr>
<tr><td id="12-4">mma.setRange(MMA8451 RANGE 4 G);</td><td id="12-5"></td></tr>
<tr><td id="12-6">mma.setRange(MMA8451 RANGE 8 G);</td><td id="12-7"></td></tr>
</table>

<a id='51def107-119d-4b9b-961f-70fc86fffeb7'></a>

And read what the current range is with

<a id='32708e44-6774-472c-a6ba-1aa761a3d693'></a>

© Adafruit Industries

<a id='bb9ada82-640b-4c17-af71-5220f6d0d6f7'></a>

Page 13 of 21

<!-- PAGE BREAK -->

<a id='c6b14f04-cfac-4966-854b-f1f88b6dbb6e'></a>

mma.getRange()

<a id='a0e42bfb-d042-45dd-a10a-711aba543248'></a>

Which returns 1 for ±2g, 2 for ±4g and 3 for ±8g

<a id='d7eacc58-a295-4afa-b629-a1c513a80e37'></a>

Read Raw Count Data
You can read the raw counts data with

<a id='648eebb8-a89f-466c-9750-65f83cd5d72e'></a>

```
mma.read();
```

<a id='9984c523-9da1-4cbb-b418-870d574bde8f'></a>

The x, y and z data is then available in **mma.x**, **mma.y** and **mma.z**
All three are read in one transaction.

<a id='3fe55a4e-288d-477f-a409-414ec8175fc1'></a>

Reading Normalized Adafruit_Sensor data
We recommend using the Adafruit_Sensor interface which allows reading into an
event structure. First create a new event structure

<a id='78091f38-0344-46d4-9ad0-3cec2809e925'></a>

sensors_event_t event;

<a id='ac0ae868-e9f9-4646-b3e4-de365618d754'></a>

Then read the event whenever you want

```
mma.getEvent(&amp;event);
```

<a id='2ab87a4b-b881-46be-9158-52218b553c71'></a>

The normalized SI unit data is available in `event.acceleration.x`, `event.acceleration.y` and `event.acceleration.z`

<a id='7b8fb58b-5310-4efd-8e94-9f49979f7637'></a>

## Read Orientation

The sensor has built in tilt/orientation detection. You can read the current orientation with

```
mma.getOrientation();
```

<a id='396108dd-ab54-4854-8aa8-10c6eab9c269'></a>

The return value ranges from 0 to 7
* 0: Portrait Up Front
* 1: Portrait Up Back
* 2: Portrait Down Front
* 3: Portrait Down Back
* 4: Landscape Right Front
* 5: Landscape Right Back
* 6: Landscape Left Front
* 7: Landscape Left Back

<a id='b2993155-e912-4c01-b0c1-ff60d577e29a'></a>

© Adafruit Industries

<a id='28024783-d857-47fd-be23-1ec49dc89590'></a>

Page 14 of 21

<!-- PAGE BREAK -->

<a id='cb6269e2-eee7-4dd2-a126-66c2cdff15a0'></a>

<::Screenshot of a "Library Manager" software window. The window features standard macOS traffic light buttons (red, yellow, green) in the top left corner. The title bar reads "Library Manager". Below the title bar, there are filter fields: "Type" with a dropdown displaying "All", "Topic" with a dropdown displaying "All", and a search input field containing the text "Adafruit_Sensor". Below these controls, a display area shows details for "Adafruit Unified Sensor by Adafruit Version 1.0.2 INSTALLED". A description reads: "Required for all Adafruit Unified Sensor based libraries. A unified sensor abstraction layer used by many Adafruit sensor libraries." At the bottom of this entry, there is a link labeled "More info".: screenshot::>

<a id='57192a38-3b08-4e09-91fe-97b57ac89478'></a>

# Python & CircuitPython
It's easy to use the MMA8451 sensor with Python or CircuitPython, and the [Adafruit CircuitPython MMA8451](https://adafru.it/C5g) module. This module allows you to easily write Python code that reads the acceleration and more from the sensor.

<a id='99c37fb4-8dec-4353-882b-651115eef4fc'></a>

You can use this sensor with any CircuitPython microcontroller board or with a computer that has GPIO and Python thanks to Adafruit_Blinka, our [CircuitPython-for-Python compatibility library](https://adafru.it/BSN).

<a id='36f50215-be1f-46b6-9635-3e6cd74adb10'></a>

# CircuitPython Microcontroller Wiring

First wire up a MMA8451 to your board exactly as shown on the previous pages for Arduino using an I2C connection. Here's an example of wiring a Feather MO to the sensor with I2C:

<a id='3acb978d-8bcc-4e9e-b750-9a9520179791'></a>

<::logo: fritzing
fritzing
The logo is a simple wordmark in a sans-serif font, all in lowercase, in a gray color.::>

<a id='50012389-19da-4911-82a1-f353e4c68d5e'></a>

Board 3V to sensor VIN
Board GND to sensor GND
Board SCL to sensor SCL
Board SDA to sensor SDA

<a id='9f25bbc8-546f-42e0-86fa-f25e7d990d9b'></a>

# Python Computer Wiring

Since there's dozens of Linux computers/boards you can use we will show wiring for Raspberry Pi. For other platforms, [please visit the guide for CircuitPython on Linux to see whether your platform is supported](https://adafru.it/BSN).

<a id='de00160a-e28e-4621-a124-dcf46d6415af'></a>

Here's the Raspberry Pi wired with I2C:

<a id='d1510e09-7350-441f-a886-dd7e445be3dc'></a>

© Adafruit Industries

<a id='2e3d3080-6d27-41c8-ab26-79fb320f862b'></a>

Page 15 of 21

<!-- PAGE BREAK -->

<a id='0525d496-cd15-4933-ba3a-511d276d8305'></a>

<::A diagram illustrating the wiring connections between a Raspberry Pi and a sensor module on a breadboard. The green Raspberry Pi board is on the left, featuring various ports such as Power, DSI (Display), HDMI, CSI (Camera), Audio, Ethernet, and two USB 2x ports. A 40-pin GPIO header is visible on the right side of the Raspberry Pi. On the right, a blue sensor module, labeled "MMA8453", is plugged into a white breadboard. Four jumper wires connect the Raspberry Pi's GPIO pins to the sensor module:
Pi 3V3 to sensor VIN
Pi GND to sensor GND
Pi SCL to sensor SCL
Pi SDA to sensor SDA
: figure::>

<a id='396069a4-8751-48d0-9fd9-a429193ef937'></a>

Older versions of the Raspberry Pi firmware do not have I2C clock stretching support so they don't work well with the MMA. Please ensure your firmware is updated to the latest version before continuing and slow down the I2C as explained here https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/i2c-clock-stretching

<a id='7c3e1bea-f3f0-4468-a8ad-369e4992c530'></a>

# CircuitPython Installation of MMA8451 Library

Next you'll need to install the [Adafruit CircuitPython MMA8451](https://adafru.it/C5g) library on your CircuitPython board.

<a id='591b005f-226b-4428-b693-e766c886b489'></a>

First make sure you are running the [latest version of Adafruit CircuitPython](https://adafru.it/Amd) for your board.

<a id='b5389689-8ff9-4bf5-9953-e606487ccd4b'></a>

Next you'll need to install the necessary libraries to use the hardware--carefully follow the steps to find and install these libraries from [Adafruit's CircuitPython library bundle](https://adafru.it/zdx). Our introduction guide has a [great page on how to install the library bundle](https://adafru.it/ABU) for both express and non-express boards.

<a id='aebc4452-7a80-47a3-a2ab-d929c59dbb0b'></a>

Remember for non-express boards like the, you'll need to manually install the necessary libraries from the bundle:

<a id='265dab5a-a066-4d12-87b2-980959d43ddb'></a>

* adafruit_mma8451.mpy
* adafruit_bus_device

<a id='2fdcf8e3-7989-4959-8760-13d77a006d92'></a>

Before continuing make sure your board's lib folder or root filesystem has the `adafruit_mma8451.mpy`, and `adafruit_bus_device` files and folders copied over.

<a id='37566a7d-88e7-4f22-b683-7c6341ee9c2d'></a>

© Adafruit Industries

<a id='a71e1d96-252d-4ef8-9695-16bc88866b1c'></a>

Page 16 of 21

<!-- PAGE BREAK -->

<a id='96dd07c5-2a21-4bf4-98d2-8daa3996b512'></a>

Next connect to the board's serial REPL (https://adafru.it/Awz) so you are at the
CircuitPython >>> prompt.

<a id='1c3f95f3-e117-4c0c-aa50-58cbad50ef5e'></a>

# Python Installation of MMA8451 Library

You'll need to install the Adafruit_Blinka library that provides the CircuitPython support in Python. This may also require enabling I2C on your platform and verifying you are running Python 3. Since each platform is a little different, and Linux changes often, please visit the CircuitPython on Linux guide to get your computer ready (https://adafru.it/BSN)!

<a id='52c46285-135d-4244-91e5-5b1a75f71656'></a>

Once that's done, from your command line run the following command:

* `sudo pip3 install adafruit-circuitpython-mma8451`

<a id='ac36c891-2fab-4772-bd5a-437bc3659aa4'></a>

If your default Python is version 3 you may need to run 'pip' instead. Just make sure you aren't trying to use CircuitPython on Python 2.x, it isn't supported!

<a id='f1d922cf-fdef-4718-8263-653233461096'></a>

# CircuitPython & Python Usage
To demonstrate the usage of the sensor we'll initialize it and read the acceleration from the board's Python REPL. Run the following code to import the necessary modules and initialize the I2C connection with the sensor:

<a id='a83be39d-79cf-4a6f-9f1a-6531742c413b'></a>

```python
import board
import adafruit_mma8451
i2c = board.I2C()
sensor = adafruit_mma8451.MMA8451(i2c)
```

<a id='d67de593-97cc-4130-8ed6-b19cf689f960'></a>

Now you're ready to read values from the sensor using any of these properties:

*   **acceleration** - This returns a 3-tuple of X, Y, Z acceleration values in meters per second squared (i.e. 9.8m/s^2 is the force of gravity on the surface of the earth).
*   **orientation** - This is a value the MMA8451 calculates to help you understand what orientation the sensor is in, kind of like how a smartphone detects if its landscape or portrait orientation. This will return one of the following values:
    *   `adafruit_mma8451.PL_PUF`: Portrait, up, front
    *   `adafruit_mma8451.PL_PUB`: Portrait, up, back
    *   `adafruit_mma8451.PL_PDF`: Portrait, down, front
    *   `adafruit_mma8451.PL_PDB`: Portrait, down, back
    *   `adafruit_mma8451.PL_LRF`: Landscape, right, front
    *   `adafruit_mma8451.PL_LRB`: Landscape, right, back

<a id='65c061f7-d9a7-4cf7-9348-f585235a806d'></a>

©Adafruit Industries

<a id='3beb7b44-35f4-4367-aa8b-4ab582cbb0a7'></a>

Page 17 of 21

<!-- PAGE BREAK -->

<a id='eb05be8d-72f1-4ee7-adf9-fbba85932217'></a>

* adafruit_mma8451.PL_LLF: Landscape, left, front
* adafruit_mma8451.PL_LLB: Landscape, left, back

<a id='46252fc0-4a26-4f32-baa8-11d3190a662c'></a>

```
x, y, z = sensor.acceleration
print('Acceleration: x={0:0.3f} m/s^2 y={1:0.3f} m/s^2 z={2:0.3f} m/s^2'.format(x,
y, z))
orientation = sensor.orientation
print('Orientation: {0}'.format(orientation))
```

<a id='90638ca5-6aa9-471c-ab77-e2349628baf5'></a>

```
>>> x, y, z = sensor.acceleration
>>> print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
Acceleration: x=-1.475m/s^2 y=-1.820m/s^2 z=9.357m/s^2
>>> orientation = sensor.orientation
>>> print('Orientation: {0}'.format(orientation))
Orientation: 0
>>>
```

<a id='54f4399f-7274-4c49-b509-43c6089c658d'></a>

In addition there are a few properties you can read and write to change the behavior of the sensor:

<a id='7c51c616-95a5-45e5-b0a9-5455091239fa'></a>

- range - The range of the accelerometer measurements. This must be a value of:
  * adafruit_mma8451.RANGE_2G: +/- 2G range
  * adafruit_mma8451.RANGE_4G: +/- 4G range (the default)
  * adafruit_mma8451.RANGE_8G: +/- 8G range
- data_rate - The rate at which the sensor measures acceleration data. This must be a value of:
  * adafruit_mma8451.DATARATE_800HZ: 800hz
  * adafruit_mma8451.DATARATE_400HZ: 400hz
  * adafruit_mma8451.DATARATE_200HZ: 200hz
  * adafruit_mma8451.DATARATE_100HZ: 100hz
  * adafruit_mma8451.DATARATE_50HZ: 50hz
  * adafruit_mma8451.DATARATE_12_5HZ: 12.5hz
  * adafruit_mma8451.DATARATE_6_25HZ: 6.25hz
  * adafruit_mma8451.DATARATE_1_56HZ: 1.56hz

<a id='047ee490-df08-4400-9abd-788143193270'></a>

sensor.range = adafruit_mma8451.RANGE_8G
sensor.data_rate = adafruit_mma8451.DATARATE_400HZ

<a id='30075db3-7b28-4402-9da1-74548893c6e1'></a>

>>> sensor.range = adafruit_mma8451.RANGE_8G
>>> sensor.data_rate = adafruit_mma8451.DATARATE_400HZ
>>> x, y, z = sensor.acceleration
>>> print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
Acceleration: x=-1.456m/s^2 y=-1.810m/s^2 z=9.385m/s^2
>>> orientation = sensor.orientation
>>> print('Orientation: {0}'.format(orientation))
Orientation: 0
>>>

<a id='43938730-72bc-40ff-9d36-f640cc607da2'></a>

That's all there is to using the MMA8451 with CircuitPython!

<a id='700704f1-2540-4f0c-ae70-a101d28f9cb3'></a>

© Adafruit Industries

<a id='7013d550-f2a5-4927-a7c2-15239ff938f0'></a>

Page 18 of 21

<!-- PAGE BREAK -->

<a id='14a61527-a503-44a7-9561-946e08129e0c'></a>

The following is a complete example that will print the orientation and acceleration of the sensor every second. Save this as **code.py** on your board and open the REPL to see the output.

<a id='ac3fb886-d1b3-47ec-94df-afe687ce83cc'></a>

Full Example Code

<a id='422eb9e8-c566-4ddf-afb9-79590243df7e'></a>

# SPDX-FileCopyrightText: 2018 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

<a id='933d3b4f-ee65-4243-966f-1459526aa43b'></a>

# Simple demo of reading the MMA8451 orientation every second.import timeimport boardimport adafruit_mma8451

<a id='ef5bb1ce-1391-4edd-a61f-7700f229e8dc'></a>

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C() # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C() # For using the built-in STEMMA QT connector on a
microcontroller

# Initialize MMA8451 module.
sensor = adafruit_mma8451.MMA8451(i2c)
# Optionally change the address if it's not the default:
# sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)

# Optionally change the range from its default of +/-4G:
# sensor.range = adafruit_mma8451.RANGE_2G # +/- 2G
# sensor.range = adafruit_mma8451.RANGE_4G # +/- 4G (default)
# sensor.range = adafruit_mma8451.RANGE_8G # +/- 8G

# Optionally change the data rate from its default of 800hz:
# sensor.data_rate = adafruit_mma8451.DATARATE_800HZ # 800Hz (default)
# sensor.data_rate = adafruit_mma8451.DATARATE_400HZ # 400Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_200HZ # 200Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_100HZ # 100Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_50HZ # 50Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_12_5HZ # 12.5Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_6_25HZ # 6.25Hz
# sensor.data_rate = adafruit_mma8451.DATARATE_1_56HZ # 1.56Hz

<a id='4d4d4872-54b9-4795-a8b9-41d1ca10d924'></a>

```python
# Main loop to print the acceleration and orientation every second.
while True:
    x, y, z = sensor.acceleration
    print(
        "Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2".format(x, y,
        z)
    )
```

<a id='d9ed96ed-0b41-4796-ac58-1168a20bedda'></a>

orientation = sensor.orientation
# Orientation is one of these values:
# - PL_PUF: Portrait, up, front
# - PL_PUB: Portrait, up, back
# - PL_PDF: Portrait, down, front
# - PL_PDB: Portrait, down, back
# - PL_LRF: Landscape, right, front
# - PL_LRB: Landscape, right, back
# - PL_LLF: Landscape, left, front
# - PL_LLB: Landscape, left, back
print("Orientation: ", end="")
if orientation == adafruit_mma8451.PL_PUF:
    print("Portrait, up, front")
elif orientation == adafruit_mma8451.PL_PUB:
    print("Portrait, up, back")
elif orientation == adafruit_mma8451.PL_PDF:

<a id='77018818-3958-4ad5-9b27-00383319e64a'></a>

Adafruit Industries

<a id='0cc896fc-cd3a-4e4a-922d-d455fc9364a5'></a>

Page 19 of 21

<!-- PAGE BREAK -->

<a id='47a2024d-05d0-4174-97e3-4f7e4656d87c'></a>

print("Portrait, down, front")
elif orientation == adafruit_mma8451.PL_PDB:
    print("Portrait, down, back")
elif orientation == adafruit_mma8451.PL_LRF:
    print("Landscape, right, front")
elif orientation == adafruit_mma8451.PL_LRB:
    print("Landscape, right, back")
elif orientation == adafruit_mma8451.PL_LLF:
    print("Landscape, left, front")
elif orientation == adafruit_mma8451.PL_LLB:
    print("Landscape, left, back")
time.sleep(1.0)

<a id='999c17c6-8fe7-4f7d-85a6-76069d5fdc4e'></a>

# Python Docs

[Python Docs](https://adafru.it/C5i)

<a id='d70d5627-dc7e-44dc-8602-0b0a7aad8db7'></a>

# Downloads

## Datasheet & Files

* [MMA8451-Q Datasheet](https://adafru.it/dLO)
* [Fritzing object in Adafruit Fritzing library](https://adafru.it/aP3)
* [EagleCAD PCB files on GitHub](https://adafru.it/pIF)

<a id='6df27988-5065-47d3-9f3b-a15136eb3166'></a>

Schematics
<::
```schematic
U2 Voltage Regulator (MEC5225-3.3)
- Input (+5V) to IN and EN pins, with 10uF capacitor (C1) to GND.
- Output (+3V3) from OUT pin, with 10uF capacitor (C2) to GND.
- GND pin connected to ground.

Level Shifters (88128)
- Two identical level shifters.
- Each shifter has +3V3, SCL 3.3V, SDA 3.3V, and GND on one side.
- Each shifter has +5V, SCL 5.0V, SDA 5.0V, and GND on the other side.
- SCL 3.3V and SDA 3.3V from the level shifters connect to U1.
- SCL 5.0V and SDA 5.0V from the level shifters connect to JP1.

U1 MMA845x Accelerometer
- VDD and VDDD connected to +3V3, with 0.1uF capacitor (C3) from +3V3 to GND.
- GND connected to ground.
- SCL and SDA connected to the SCL 3.3V and SDA 3.3V lines from the level shifters.
- INT1 and INT2 pins are connected to each other and to JP1.
- BYP pin connected to GND via a capacitor (C4).
- NC pins are not connected.
- VDD 2-3.6V is noted.

JP1 Header
- Pins for SDA, SCL, INT1, INT2, +5V, and GND.
- SDA and SCL pins connected to the SCL 5.0V and SDA 5.0V lines from the level shifters.
- INT1 and INT2 pins connected to the INT1/INT2 lines from U1.
- +5V and GND pins are available.
```
: schematic::>
ISSUE
DRAUN
KTOWN
CHECKED
>CHECKED
DATE
>DATE
ADAFRUIT INDUSTRIES
TITLE
DATE
not saved!
FILE: MMA845_REV-B
2013
REV
A
DRG NO
>DRGNO
PAGE: 1/1

<a id='0f655fb3-9861-4d92-8791-0c9b1118c14d'></a>

<table id="19-1">
<tr><td id="19-2"></td><td id="19-3"></td><td id="19-4">(red abstract pattern)</td><td id="19-5">(red abstract pattern)</td></tr>
<tr><td id="19-6"></td><td id="19-7"></td><td id="19-8">(red circular pattern)</td><td id="19-9">(red circular pattern)</td></tr>
<tr><td id="19-a">ISSUE</td><td id="19-b">ADAFRUIT INDUSTRIES</td><td id="19-c" colspan="2">2013 (icon)</td></tr>
</table>
<table id="19-d">
<tr><td id="19-e">DRALN KTOWN</td><td id="19-f" rowspan="3" colspan="2">TITLE REV A DATE not saved! DRG NO &gt;DRGNO</td></tr>
<tr><td id="19-g">CHECKED &gt;CHECKED</td></tr>
<tr><td id="19-h" rowspan="2">DATE &gt;DATE</td></tr>
<tr><td id="19-i">FILE: MMA845_REV-B</td><td id="19-j">PAGE: 1/1</td></tr>
</table>

<a id='bf8d096e-bd51-4fa4-a4c5-2ec943a29f72'></a>

Fabrication print
Dimensions are in Inches

<a id='f639dd57-d9b2-4a82-901c-2fbc7c8c68f0'></a>

© Adafruit Industries

<a id='7106f12b-1a20-4420-88ce-af9691ebdac9'></a>

Page 20 of 21

<!-- PAGE BREAK -->

<a id='0c394ddf-df64-4571-8197-675fcfc1fa4d'></a>

<::Technical drawing of a PCB (Printed Circuit Board) layout for an MMA8451 sensor. The board is rectangular with various electronic components and traces visible. There are labeled pads along the bottom edge: UIN, GND, 3V0, I1, I2, SCL, SDA, and A. The top center of the board has the label "MMA8451" with a small star icon and an indicated coordinate system (x, y, z axes). The drawing includes external dimensions: a total width of 0.8 units, with a segment of 0.6 units marked within it. The total height on the right side is 1.1 units, with a segment of 0.1 units indicated. The height on the left side is 0.7 units.
: technical drawing::>

<a id='4796d0ec-8a45-49f6-843f-cf4f42a3dc18'></a>

©Adafruit Industries

<a id='a708c511-7a39-4288-bc57-31e65b0fd3f1'></a>

Page 21 of 21