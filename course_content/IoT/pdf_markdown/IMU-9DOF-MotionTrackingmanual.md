<a id='b4e4bacd-411a-472d-b6fb-928b860fd1ed'></a>

7/23/22, 9:09 PM

<a id='411d8765-1e67-4554-85bd-da4331740efb'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='f36640f6-e3f2-477b-82a7-72efaa9a8a12'></a>

Grove - IMU
9DOF(Icm20600+AK09918)

<a id='f8db9842-03ea-48cb-8711-4e4f7ed342b5'></a>

<::An image of a blue printed circuit board (PCB) with various electronic components. The board features a white 4-pin connector on the right side. The pins are labeled from top to bottom as SCL, SDA, VCC, and GND. Numerous surface-mount devices (SMDs) such as resistors, capacitors, and integrated circuits (ICs) are visible across the board. On the left side of the PCB, a coordinate system with labeled X, Y, and Z axes is printed. Another IC is located near this coordinate system. The board has mounting holes in each corner and a notched edge on the bottom.: figure::>

<a id='743b2531-e98d-4758-aaf7-87f360f74bee'></a>

The Grove - IMU 9DOF (Icm20600+AK09918) is a 9 Degrees of Freedom IMU
[Inertial measurement unit](https://en.wikipedia.org/wiki/Inertial_measurement_unit) which combines gyroscope, accelerometer and

<a id='6a6f0e3d-136b-4a10-be77-844386ece3eb'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='6620c1ef-9cbe-458a-a9a0-7b7f13b35aa0'></a>

1/23

<!-- PAGE BREAK -->

<a id='f6cf4017-3d5b-408e-98ce-3909277c5a3a'></a>

7/23/22, 9:09 PM

<a id='9e9f6748-bd4f-4914-944e-4d58625efb77'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='1dcfbf38-c3b9-44a9-9c4a-816e6a70cc1c'></a>

electronic compass. We use two chips LCM20600+AK09918 to
implement those 3 functions.

<a id='1ee768b6-63f1-4720-ae60-1ea359abf335'></a>

The LCM20600 is a 6-axis MotionTracking device that combines a 3-axis gyroscope, 3-axis accelerometer. Gyroscope [https://en.wikipedia.org/wiki/Gyroscope] is a device used for measuring or maintaining orientation and angular velocity, normally, we use it to measure spin and twist. Accelerometer [https://en.wikipedia.org/wiki/Accelerometer] is a device that measures proper acceleration.

<a id='240b664a-109b-4811-8f80-45583c159a3a'></a>

The AK09918 is a 3-axis electronic compass
[https://en.wikipedia.org/wiki/Magnetometer] IC with high sensitive
Hall sensor technology. We use an electronic compass to measure
the magnetic force, which can provide us with the direction
information.

<a id='f29b4694-a018-4317-8cff-c8f4896d956b'></a>

As its name suggests just use this single small module and you can
measure 9 Degrees of Freedom: angular rotation in x/y/z axis,
acceleration in x/y/z axis, and magnetic force in x/y/z axis.

<a id='a22708a4-99d3-434b-922a-917f951610f6'></a>

What an amazing module! Just use this module to build your own motion and orientation system 😁

<a id='ffdea2c9-453f-498b-a9b2-c12456556aa9'></a>

Get One Now
[https://www.seeedstudio.com/Grove-IMU-9DOF-%28lcm20600%2BAK09918%29-p-3157.html]

<a id='6e21cf8e-b58e-4172-930f-609e685bf1e3'></a>

Features

<a id='6090c921-bc05-46d9-a677-20f3e56a627b'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='756281a2-e323-4044-8a3f-1112f0513ca1'></a>

2/23

<!-- PAGE BREAK -->

<a id='3776ca9f-3203-4cc1-8df3-86d93ab65b81'></a>

7/23/22, 9:09 PM

<a id='66e9bd0d-7b24-4cca-8d69-fe09933d4043'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='a620c0bf-c354-4f4d-a721-b5fdd05750e8'></a>

* 3-Axis Gyroscope with Programmable FSR of 250 dps, 500 dps, 1000 dps, and 2000 dps
* 3-Axis Accelerometer with Programmable FSR of 2g, 4g, 8g, and 16g
* 3-Axis Electronic Compass with 0.15 T/LSB (typ.) sensitivity
* User-programmable interrupts
* 16-bit ADC resolution and Programmable Filters for acceleration measurements
* 16-bit ADC resolution for magnetic measurements
* 1 KB FIFO buffer enables the applications processor to read the data in bursts(LCM20600)
* Embedded temperature sensor
* Magnetic sensor overflow monitor function
* Built-in oscillator for internal clock source

<a id='7e1e6a84-c78e-4dc1-bc5a-0cb8e906209b'></a>

Specification

<a id='832e3195-e773-4446-98f3-5efd3551acc5'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='6a8aa2d2-5d57-4848-82f1-802a193ddbc1'></a>

3/23

<!-- PAGE BREAK -->

<a id='26266e62-15c8-4b30-83bc-cd27d3558538'></a>

7/23/22, 9:09 PM

<a id='092e7df7-2e5a-46d8-85bf-8e147e7c497c'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='b244c09f-3223-4c10-af12-d062d913d537'></a>

<table id="3-1">
<tr><td id="3-2">Item</td><td id="3-3">Value</td></tr>
<tr><td id="3-4">Operating voltage</td><td id="3-5">3.3V / 5V</td></tr>
<tr><td id="3-6">Operating temperature</td><td id="3-7">-30°C to +85°C</td></tr>
<tr><td id="3-8">Gyroscope Full-Scale Range</td><td id="3-9">±250 dps, ±500 dps, ±1000 dps, ±2000 dps</td></tr>
<tr><td id="3-a">Gyroscope Sensitivity Scale Factor</td><td id="3-b">131 LSB/(dps)@±250 dps 65.5 LSB/(dps)@±500 dps 32.8 LSB/(dps)@±1000 dps 16.4 LSB/(dps)@±2000 dps</td></tr>
<tr><td id="3-c">Accelerometer Full-Scale Range</td><td id="3-d">±2g, ±4g, ±8g, ±16g</td></tr>
<tr><td id="3-e">Accelerometer Sensitivity Scale Factor</td><td id="3-f">16384 LSB/g@±2g 8192 LSB/g@±4g 4096 LSB/g@±8g 2048 LSB/g@±16g</td></tr>
<tr><td id="3-g">Magnetic sensor measurement range</td><td id="3-h">±4912µT (typical)</td></tr>
<tr><td id="3-i">Magnetic sensor sensitivity</td><td id="3-j">0.15µT (typical)</td></tr>
<tr><td id="3-k">Interface</td><td id="3-l">I²C</td></tr>
<tr><td id="3-m">I²C Address</td><td id="3-n">LCM20600 0x69(default) 0x68(optional) AK09918 0x0C</td></tr>
</table>

<a id='25346971-b340-4620-b922-fe81bed21e74'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='60a7d5d8-ba61-4676-ba7c-a9d76a787bee'></a>

4/23

<!-- PAGE BREAK -->

<a id='2b6f6016-c339-4b5a-8838-50703a9a91c1'></a>

7/23/22, 9:09 PM

<a id='5b0f22f0-27e5-46a7-a1b2-32a9a7af9100'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='1a608ae6-d874-4a47-b703-ce11046ed18e'></a>

Applications

* Smartphones and Tablets
* Wearable Sensors

<a id='52b7aa99-07ee-45de-ad1a-b6e4b1af2b98'></a>

Hardware Overview

<a id='a1aff9a2-aeb5-4d08-94a5-97afdf72fa33'></a>

Pin Out

<a id='a1c5968d-d21f-421b-9b73-ff958fb2f62b'></a>

<::A blue circuit board module with a 4-pin connector on the left side. The pins are labeled GND, VCC, SDA, and SCL from top to bottom. Numbered circles with dashed lines point to each pin:
4 points to GND
3 points to VCC
2 points to SDA
1 points to SCL
On the right side of the board, an X, Y, Z axis diagram is present.

Legend:
4 GND: connect this module to the system GND
3 VCC: you can use 5V or 3.3V for this module
2 SDA: I²C serial data
1 SCL: I²C serial clock
: figure::>

<a id='08a0d135-6e03-46a9-a673-07a8eda76d62'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='4b9796cf-9f48-4a4c-87f4-13873d30fad0'></a>

5/23

<!-- PAGE BREAK -->

<a id='c6d092fc-0851-4efc-ac38-07e9e9e62884'></a>

7/23/22, 9:09 PM

<a id='b17df039-17e9-448c-898c-f04c656cbbc4'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='cdb2f59d-f980-4719-8bda-55e62e0e54e8'></a>

ICM Address<::A diagram illustrating jumper settings for ICM Address. The first configuration shows a jumper connecting the middle (grey) and right (black) pins, indicating address 0x68. The second configuration shows a jumper connecting the left (red) and middle (grey) pins, indicating address 0x69 Default. Below this, a blue circuit board is shown with various labels. A jumper block on the board is labeled "High" and "Low" with "AD(ICM20600)". Other text on the board includes "IMU 9DOF (ICM20600 & AK09918) v1.0", "address(icm20600) 0x69", and "address(ak09918C) 0x0c.". Numbered circles (5, 6, 7, 8) point to specific pins or areas on the board, corresponding to the descriptions below.: figure::>5 INT2: Interrupt digital output (totem pole or open-drain)6 INT1: Interrupt digital output (totem pole or open-drain)7 FSYNC: Frame synchronization digital input or No Connect8 VCC_1.8V: Provide 1.8V for ICM20600 and AK09918

<a id='943d085b-ff84-4669-859b-5db0a3d5fd22'></a>

**Danger**
The default I2C address of LCM20600 is 0x69, you can change it to 0x68.
The central pad is connected to the address wire, you can change the I2C
address by cutting the wire and re-welding it. For the safety of you and
others, please be careful with knife or welding gun you may use.

<a id='96049d48-8754-40f9-9b0f-b284af6042c7'></a>

Schematic

Power

<a id='0fa33023-e8d3-4537-9427-67c76a195f07'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='9fe8c67c-6d20-40c9-a2c9-e3420ef68895'></a>

6/23

<!-- PAGE BREAK -->

<a id='fecf1f89-2389-41b7-953d-8f0bd8fd57d0'></a>

7/23/22, 9:09 PM

<a id='28faafbe-8a9b-42ce-9ae4-a512ab6defb3'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='34ae9661-0d69-4086-8922-c4efe711a775'></a>

<::An electronic circuit diagram for a voltage regulator. The main component is an IC labeled U5, XC6206P182MR, which has pins VIN, VSS, and VOUT. Pin 3 is VIN, pin 1 is VSS, and pin 2 is VOUT. The input voltage, labeled VCC, is connected to the VIN pin. In parallel with the VIN input, there are two capacitors, C2 (100nF) and C1 (10uF), connected to ground. The VOUT pin is connected to an output labeled 1V8. In parallel with the VOUT output, there are two capacitors, C11 (100nF) and C10 (10uF), connected to ground. A test point, TP7+, is also connected to the VOUT line. The VSS pin of the IC is connected directly to ground.: circuit diagram::>

<a id='df0d9da6-effb-40b3-87f6-e221ac8da153'></a>

Since the operating voltage range of LCM20600 is 1.71V to 3.45V, and the operating voltage range of AK09918 is 1.65V to 1.95V, we use a power conversion chip **XC6206P182MR** to provide a stable 1.8V for both chips.

<a id='7b1b07a5-953c-4e70-bbdd-b95ed371a015'></a>

Bi-directional level shifter circuit
<::circuit diagram
: The diagram shows a bi-directional level shifter circuit. It features two identical sections, one for SDA and one for SCL, each using an N-channel MOSFET (CJ2102) for level shifting.

Top section (SDA):
- An input labeled "SDA_1V8" is connected through a 4.7K resistor (R3) to the source of MOSFET Q1 (CJ2102).
- The gate of Q1 is connected to a 1V8 rail.
- The drain of Q1 is connected to an output labeled "SDA_VCC" and also through a 4.7K resistor (R4) to a VCC rail.
- The 1V8 rail is also connected to the source side of Q1 via a direct connection.

Bottom section (SCL):
- An input labeled "SCL_1V8" is connected through a 4.7K resistor (R5) to the source of MOSFET Q2 (CJ2102).
- The gate of Q2 is connected to the same 1V8 rail.
- The drain of Q2 is connected to an output labeled "SCL_VCC" and also through a 4.7K resistor (R2) to the same VCC rail.
- The 1V8 rail is also connected to the source side of Q2 via a direct connection.

Both MOSFETs, Q1 and Q2, are depicted with their internal body diodes.::>

<a id='8c17a49f-6fad-4ac6-8cb7-8fbe739a68e4'></a>

This is a typical Bi-directional level shifter circuit to connect two different voltage section of an I²C bus. The I²C bus of two chips use 1.8V, if the I²C bus of the Arduino use 5V or 3.3V, this circuit will be needed. In the schematic above, **Q1** and **Q2** are N-Channel MOSFET CJ2102 [https://files.seeedstudio.com/wiki/Grove-IMU_9DOF-Icm20600_AK09918/res/CJ2102.pdf], which act as a

<a id='e227ef4f-ea04-4f99-af21-e3a0c9f43c04'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='e67be9d4-b5a1-4bd2-a0f9-9960bee962de'></a>

7/23

<!-- PAGE BREAK -->

<a id='55a83ba6-6c5d-43aa-a43c-cd0b26dd144d'></a>

7/23/22, 9:09 PM

<a id='633ea678-92da-42c6-a47e-6c1d7275a2ae'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='66fa4577-3ca5-4c0f-a661-32f987ee2cf3'></a>

bidirectional switch. In order to better understand this part, you can refer to the AN10441 [https://files.seeedstudio.com/wiki/Grove-I2C_High_Accuracy_Temperature_Sensor-MCP9808/res/AN10441.pdf]

<a id='48741771-2349-4fda-8728-db084d279322'></a>

Platforms Supported

<a id='a6589a41-5585-469b-83d6-fe6477aa76b4'></a>

<table><thead><tr><th>Arduino</th><th>Raspberry<br>Pi</th><th></th><th></th></tr></thead><tbody><tr><td><::Arduino logo: illustration::></td><td><::Raspberry Pi logo with a red "TO DO" badge: illustration::></td><td></td><td></td></tr></tbody></table>

<a id='3906dd3a-e674-430f-aa96-ac8c4eec6531'></a>

Caution
The platforms mentioned above as supported is/are an indication of the module's software or theoritical compatibility. We only provide software library or code examples for Arduino platform in most cases. It is not possible to provide software library / demo code for all possible MCU platforms. Hence, users have to write their own software library.

<a id='95e616d6-bb66-4883-a9b8-f084e9c7f41d'></a>

# Getting Started

Play With Arduino

### Hardware

Materials required

<a id='9da0f100-669b-46f2-a125-fd78a36684ef'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='eeec2a83-b728-4ac6-b587-901ff2d34533'></a>

8/23

<!-- PAGE BREAK -->

<a id='1c23de68-a7a4-4a4f-8da5-abe0cd6c767c'></a>

7/23/22, 9:09 PM

<a id='24c0ad9d-7a59-477d-9dba-dbc2a6cb65bc'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='706e2625-b6a0-4950-a3ae-4135e7e6a6fb'></a>

Seeeduino V4.2 Base Shield <::A red Seeeduino V4.2 circuit board with yellow pin headers, featuring various electronic components, a micro USB port, a DC barrel jack, and white 3-pin connectors.: figure::> <::A black Base Shield circuit board with blue pin headers, featuring a grid of white 3-pin Grove connectors, a green LED, and labels such as I2C, 5V, 3V3, A0, A1, A2, and A3.: figure::>

<a id='6e9af001-f806-451d-8b0e-e680b192b63a'></a>

Get One Now
[https://www.seeedstudio.com/Seeeduino-
V4.2-p-2517.html]

Get One Now
[https://www.seeedstudio.com/Base
Shield-V2-p-1378.html]

<a id='140fb04c-14d3-43ab-9485-612a2e93054d'></a>

Note

1.  Please plug the USB cable gently, otherwise you may damage the port. Please use the USB cable with 4 wires inside, the 2 wires cable can't transfer data. If you are not sure about the wire you have, you can click [here](https://www.seeedstudio.com/Micro-USB-Cable-48cm-p-1475.html) to buy.
2.  Each Grove module comes with a Grove cable when you buy. In case you lose the Grove cable, you can click [here](https://www.seeedstudio.com/Grove-Universal-4-Pin-Buckled-20cm-Cable-%285-PCs-pack%29-p-936.html) to buy.

<a id='a34e9940-756a-47df-a393-1d7399667c69'></a>

*   **Step 1.** Connect the Grove - IMU 9DOF (Icm20600+AK09918) to port I²C of Grove-Base Shield.
*   **Step 2.** Plug Grove - Base Shield into Seeeduino.
*   **Step 3.** Connect Seeeduino to PC via a USB cable.

<a id='c002f8a5-4fc2-4241-80ee-233582d83e5b'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='d9cba65c-d238-4330-b299-a3980ba84401'></a>

9/23

<!-- PAGE BREAK -->

<a id='b244cb16-860b-4a20-9368-46403172ba46'></a>

7/23/22, 9:09 PM

<a id='21e36809-b2f7-4b67-aadb-5e088a6675fc'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='8ab4d550-e28a-40c0-b3b0-58007f872bef'></a>

<::An electronic assembly consisting of multiple circuit boards stacked together, with a black cable connected to the top left. The assembly includes a base board (red/brown), a middle board with blue female headers and a green LED, and a top board with white female headers. A smaller blue sensor module is connected to the right side of the stack via a white connector and a bundle of red, black, yellow, and white wires. The blue module has various small components and labels such as VCC, GND, SCL, SDA, and X, Y, Z axes markings.: figure::>

<a id='65755388-5a74-45bb-aabb-2a3876de69bf'></a>

**Note**
If we don't have Grove Base Shield, We also can directly connect this
module to Seeeduino as below.

<a id='5f7467a7-8568-48f9-9019-6bfb22e2f741'></a>

<table id="9-1">
<tr><td id="9-2">Seeeduino</td><td id="9-3">Grove - IMU 9DOF</td></tr>
<tr><td id="9-4">5V</td><td id="9-5">Red</td></tr>
<tr><td id="9-6">GND</td><td id="9-7">Black</td></tr>
<tr><td id="9-8">SDA</td><td id="9-9">White</td></tr>
<tr><td id="9-a">SCL</td><td id="9-b">Yellow</td></tr>
</table>

<a id='3095eb59-085f-47d6-bc37-e02a32c95101'></a>

Software

<::pencil icon::> Note

<a id='869303aa-9948-4c38-ad02-f8b17548756a'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='c1994efe-a2b7-46bd-ac8c-a792c86ec186'></a>

10/23

<!-- PAGE BREAK -->

<a id='0c313679-9083-4814-930f-135ac17a1f2b'></a>

7/23/22, 9:09 PM

<a id='80d394b1-55f0-49a4-bd59-cac4437954b9'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='0fc6f515-3425-47cb-9d58-8c9fbbf4047f'></a>

If this is the first time you work with Arduino, we strongly recommend you to see Getting Started with Arduino [https://wiki.seeedstudio.com/Getting_Started_with_Arduino/] before the start.

<a id='f4b48a4d-e9bf-4b67-ae3f-6c1819dae370'></a>

- **Step 1.** Download the Grove - IMU 9DOF (Icm20600+AK09918) [https://github.com/Seeed-Studio/Seeed_ICM20600_AK09918] Library from Github.
- **Step 2.** Refer to How to install library [https://wiki.seeedstudio.com/How_to_install_Arduino_Library] to install library for Arduino.
- **Step 3.** Restart the Arduino IDE. Open the example, you can open it in the following three ways:

<a id='3601ff50-83d0-4fcb-9aec-7c47367cf875'></a>

a. Open it directly in the Arduino IDE via the path: **File** → **Examples** → Grove IMU 9DOF ICM20600 AK09918 →

<a id='8f94023c-fe7b-435d-ae89-14f61fdd2a3f'></a>

compass.

File Edit Sketch Tools Help

New Ctrl+N
Open... Ctrl+O
Open Recent >
Sketchbook >
Examples >
Close Ctrl+W
Save Ctrl+S
Save As... Ctrl+Shift+S
Page Setup Ctrl+Shift+P
Print Ctrl+P
Preferences Ctrl+Comma
Quit Ctrl+Q

GSM >
LiquidCrystal >
PN532 >
Radio >
Robot Control >
Robot Motor >
SD >
Servo >
SpacebrewYun >
...

delay(100);
err = ak09918.isDataRes
}

Grove - LED Matrix Driver (HT16K33 with 8x8 LED Matrix) >
Grove IMU 9DOF ICM20600 AK09918
  compass
  test_6axis
  test_magnet
Grove Multiple Switch library
Grove Temper Humidity TH02

<a id='f8b3e313-ef51-4e42-8d24-4cd434603b0d'></a>

b. Open it in your computer by click the **compass.ino** which
you can find in the folder
XXXX\Arduino\libraries\Seeed_ICM20600_AK09918-

<a id='45e71c54-c515-4102-99c1-056150267bab'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='4b86f312-455f-4275-974e-196fee0bd5b3'></a>

11/23

<!-- PAGE BREAK -->

<a id='55cb16a1-1dc1-4967-9d80-510de4c647e8'></a>

7/23/22, 9:09 PM

<a id='57c20c87-bc72-4e59-b583-faedae2d6cba'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='015abf54-2e89-49c8-bcf7-da6b8486a312'></a>

master\examples\compass, XXXX is the location you installed the Arduino IDE.

<a id='b06a3a2f-02a2-497a-b6b8-e2ac0e8337f4'></a>

is
> This PC > Core (C:) > Users > seeed > Documents > Arduino > libraries > Seeed_ICM20600_AK09918-master > examples > compass

<table><thead><tr><th>Name</th><th>Date modified</th><th>Type</th><th>Size</th></tr></thead><tbody><tr><td>compass.ino</td><td>9/13/2018 9:05 AM</td><td>INO File</td><td>5 KB</td></tr></tbody></table>

<a id='496dbdf3-c7c7-4c99-b4c2-12125e6e99c7'></a>

c. Or, you can just click the icon \u2398 in upper right corner of the code block to copy the following code into a new sketch in the Arduino IDE.

<a id='d3665f06-3638-4ce5-9d08-0117d8f86856'></a>

1 #include "AK09918.h"
2 #include "ICM20600.h"
3 #include <Wire.h>
4 
5 AK09918_err_type_t err;
6 int32_t x, y, z;
7 AK09918 ak09918;
8 ICM20600 icm20600(true);
9 int16_t acc_x, acc_y, acc_z;
10 int32_t offset_x, offset_y, offset_z;
11 double roll, pitch;
12 // Find the magnetic declination at your Location
13 // http://www.magnetic-declination.com/
14 double declination_shenzhen = -2.2;
15 
16 void setup()
17 {
18 // join I2C bus (I2Cdev library doesn't do this aut
19 Wire.begin();
20 
21 err = ak09918.initialize();
22 icm20600.initialize();
23 ak09918.switchMode (AK09918_POWER_DOWN);
24 ak09918.switchMode(AK09918_CONTINUOUS_100HZ);
25 Serial.begin(9600);
26 
27 err = ak09918.isDataReady();
28 while (err != AK09918_ERR_OK)
29 {

<a id='05e65eb1-8981-4cd6-b6e5-0ef90cb4efa7'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='19faeee2-0e7f-4347-a6d3-9ad731704c95'></a>

12/23

<!-- PAGE BREAK -->

<a id='ba4213a7-dda7-453f-88dd-567638871d62'></a>

7/23/22, 9:09 PM

<a id='905ec715-e343-4898-bc60-82aae694b94d'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='be45e058-0408-4788-a578-61f9f3dc9103'></a>

```cpp
Serial.println("Waiting Sensor");
delay(100);
err = ak09918.isDataReady();
}

Serial.println("Start figure-8 calibration after 2");
delay(2000);
calibrate(10000, &offset_x, &offset_y, &offset_z);
Serial.println("");
}

void loop() {
  // get acceleration
  acc_x = icm20600.getAccelerationX();
  acc_y = icm20600.getAccelerationY();
  acc_z = icm20600.getAccelerationZ();

  Serial.print("A: ");
  Serial.print(acc_x);
  Serial.print(", ");
  Serial.print(acc_y);
  Serial.print(", ");
  Serial.print(acc_z);
  Serial.println(" mg");

  Serial.print("G: ");
  Serial.print(icm20600.getGyroscopeX());
  Serial.print(", ");
  Serial.print(icm20600.getGyroscopeY());
  Serial.print(", ");
  Serial.print(icm20600.getGyroscopeZ());
  Serial.println(" dps");

  ak09918.getData(&x, &y, &z);
  x = x - offset_x;
  y = y - offset_y;
  z = z - offset_z;

  Serial.print("M: ");
  Serial.print(x);
```

<a id='29e13344-a04d-4573-9dbb-9414f98b8535'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='03d7ce34-5ee1-4ae9-85a9-ddf8caa394aa'></a>

13/23

<!-- PAGE BREAK -->

<a id='df1b962b-395c-4731-9439-60da4eb4226e'></a>

7/23/22, 9:09 PM

<a id='52419da6-0e26-44a7-b6c5-f6fc8378a735'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='7ebce823-d715-4e1e-b4b7-bdbef6d57eb2'></a>

71 Serial.print(", ");
72 Serial.print(y);
73 Serial.print(",");
74 Serial.print(z);
75 Serial.println(" uT");
76
77 // roll/pitch in radian
78 roll = atan2((float)acc_y, (float)acc_z);
79 pitch = atan2(-(float)acc_x, sqrt((float)acc_y*acc_
80 Serial.print("Roll: ");
81 Serial.println(roll*57.3);
82 Serial.print("Pitch: ");
83 Serial.println(pitch*57.3);
84
85 double Xheading = x * cos(pitch) + y * sin(roll) *
86 double Yheading = y * cos(roll) - z * sin(pitch);
87
88
89 double heading = 180 + 57.3*atan2(Yheading, Xheadin;
90
91 Serial.print("Heading: ");
92 Serial.println(heading);
93 Serial.println("---------------------------------");
94
95 delay(500);
96
97 }
98
99 void calibrate(uint32_t timeout, int32_t *offsetx, int3
100 {
101 int32_t value_x_min = 0;
102 int32_t value_x_max = 0;
103 int32_t value_y_min = 0;
104 int32_t value_y_max = 0;
105 int32_t value_z_min = 0;
106 int32_t value_z_max = 0;
107 uint32_t timeStart = 0;
108
109 ak09918.getData(&x, &y, &z);
110
111 value_x_min = x;

<a id='7a30ecdb-1f33-4133-92a2-2b90729fb6b0'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='124b70c9-16a3-4b89-bd80-9e1adaada8c3'></a>

14/23

<!-- PAGE BREAK -->

<a id='9d0887e9-b4b4-42b4-bb24-5a21fb6265f2'></a>

7/23/22, 9:09 PM

<a id='2da66da1-4e43-45f2-9e37-6130fbc7c364'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='afbdb56b-6d93-4771-b73a-7b425ead4e35'></a>

```c
112 value_x_max = x;
113 value_y_min = y;
114 value_y_max = y;
115 value_z_min = z;
116 value_z_max = z;
117 delay(100);
118 
119 timeStart = millis();
120 
121 while((millis() - timeStart) < timeout)
122 {
123 ak09918.getData(&x, &y,&z);
124 
125 /* Update x-Axis max/min value */
126 if(value_x_min > x)
127 {
128 value_x_min = x;
129 // Serial.print("Update value_x_min: ");
130 // Serial.println(value_x_min);
131 
132 }
133 else if(value_x_max < x)
134 {
135 value_x_max = x;
136 // Serial.print("update value_x_max: ");
137 // Serial.println(value_x_max);
138 }
139 
140 /* Update y-Axis max/min value */
141 if(value_y_min > y)
142 {
143 value_y_min = y;
144 // Serial.print("Update value_y_min: ");
145 // Serial.println(value_y_min);
146 
147 }
148 else if(value_y_max < y)
149 {
150 value_y_max = y;
151 // Serial.print("update value_y_max: ");
152 // Serial.println(value_y_max);
```

<a id='258f414a-74ae-4165-a6d5-d6e5d34bfdfc'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='8b2bb639-8296-4bcd-9552-ee25dcb2573c'></a>

15/23

<!-- PAGE BREAK -->

<a id='26b1f43c-689a-4fd4-a602-f27413235f9e'></a>

7/23/22, 9:09 PM

<a id='3c443e11-edc1-42c1-8848-491674973200'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='f75489af-c881-43c3-8be1-997bfefa4962'></a>

```
}

/* Update z-Axis max/min value */
if(value_z_min > z)
{
  value_z_min = z;
  // Serial.print("Update value_z_min: ");
  // Serial.println(value_z_min);
}
else if(value_z_max < z)
{
  value_z_max = z;
  // Serial.print("update value_z_max: ");
  // Serial.println(value_z_max);
}

Serial.print(".");
delay(100);
}

*offsetx = value_x_min + (value_x_max - value_x_min)/
*offsety = value_y_min + (value_y_max - value_y_min)/
*offsetz = value_z_min + (value_z_max - value_z_min)/
}
```

<a id='00bc67e8-ff0e-484e-a87a-c98aa1b82dc1'></a>

## Note
There are 3 demos in the library:

**test_6axis**
> This example shows how to get gyroscope and acceleration data from ICM20600.

**test_magnet**
> This example shows how to get magnetic data from AK09918.

**compass**

<a id='b91c25a2-31a5-483b-86ff-ca03931c7b78'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='a7906553-7bb7-4326-a1da-3b1d72f06854'></a>

16/23

<!-- PAGE BREAK -->

<a id='bd02dc04-fea6-4726-9f21-168bf3bfd7e3'></a>

7/23/22, 9:09 PM

<a id='68b8b952-ae92-42c8-8236-984f5f96cd12'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='355649c3-29b8-4a47-bd9b-2e35689e8931'></a>

This example gets magnetic data and acceleration data, to count pitch and roll, and make a compass application.

<a id='990d6a2f-5473-4516-8c7e-a7f70f17b936'></a>

- **Step 4.** Upload the demo. If you do not know how to upload the code, please check [How to upload code](https://wiki.seeedstudio.com/Upload_Code/).
- **Step 5.** Open the **Serial Monitor** of Arduino IDE by click **Tool**->**Serial Monitor**. Or tap the Ctrl + Shift + M key at the same time. Set the baud rate to **9600**.

<a id='f5930aa6-a293-4542-a098-78493bea5ae4'></a>

Success
If every thing goes well, when you open the Serial Monitor, the notice will pop up--*Start figure-8 calibration after 2 seconds*. Which means in order to calibrate this module, you should move it and draw the number 8 trajectory in the air. When the "..." appears, you can start your calibration.

<a id='50240cbe-bec8-405f-a9ed-55b70f19080f'></a>

Start figure-8 calibration after 2 seconds.
...
A: -362, -205, 738 mg
G: -45, 12, -1 dps
M: -6, -23, -33 uT
Roll: -15.53
Pitch: 25.30
Heading: 23.99
---
A: -269, 583, 61 mg
G: 102, 377, -2 dps
M: 18, -21, -18 uT
Roll: 84.03
Pitch: 24.65
Heading: 215.58
---
A: -495, 229, 37 mg
G: -43, -231, 201 dps
M: 7, -30, 6 uT

<a id='19519c2c-0d60-4750-af54-06c3085d1ab8'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='99bae08d-c889-4e4b-a19a-cb4e71c3247d'></a>

17/23

<!-- PAGE BREAK -->

<a id='90bebc64-1778-45bf-a62e-2fb09b2eb45d'></a>

7/23/22, 9:09 PM

<a id='5b385715-0fe1-4e06-9d81-d8b15e5cc2bc'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='ce16a879-2ebf-4594-a725-5a18bbc4cfb2'></a>

20 Roll: 80.83
21 Pitch: 64.90
22 Heading: 21.76
23 ---

<a id='7764ba17-52dc-475c-99b3-b8cdd37afabe'></a>

Note
As you can see, the result of compass example includes three parameter:
roll, pitch and Heading. There are the terminology of Euler angles
[https://en.wikipedia.org/wiki/Euler_angles](click to check more
information).

<a id='c7bb5de6-ac11-4969-9786-e4d5ef02903e'></a>

Fuction table
<table id="17-1">
<tr><td id="17-2">Function</td><td id="17-3">Description</td></tr>
<tr><td id="17-4">ICM20600</td><td id="17-5"></td></tr>
<tr><td id="17-6">initialize()</td><td id="17-7">Initialize the chip LCM20600, by default: the measurement range of gyroscope is ± dps the measurement range of accelerometer</td></tr>
<tr><td id="17-8">setGyroScaleRange(gyro_scale_type_t range)</td><td id="17-9">After the initialization, you can set the gyr range to meet your own needs, the param gyro_scale_type_t range list: RANGE_250_DPS RANGE_500_DPS RANGE_1K_DPS RANGE_2K_DPS e.g. icm20600.setGyroScaleRange(RANGE_1 this code line will change the gyroscope measurement range to ±1000dps</td></tr>
<tr><td id="17-a">Function setAccScaleRange(acc_scale_type_t</td><td id="17-b">Description After the initialization, you can set the</td></tr>
</table>

<a id='2bca5fda-234f-477a-8129-b6ce55286b8f'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='8c1d78a1-2432-4ac5-80dd-afd91d47d1af'></a>

18/23

<!-- PAGE BREAK -->

<a id='9b7933a0-9657-4de5-906d-adad0be8ad6e'></a>

7/23/22, 9:09 PM

<a id='3ee3aed5-f7ba-4cc8-b945-30860ed0940e'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='bd0352f6-cfbf-4c07-9ab9-76356bb89609'></a>

<table id="18-1">
<tr><td id="18-2">range)</td><td id="18-3">accelerometer range to meet your own ne parameter acc_scale_type_t range list: RANGE_2G RANGE_4G RANGE_8G RANGE_16G e.g. icm20600.setAccScaleRange(RANGE_80 this code line will change the accelerome measurement range to ±8g</td></tr>
<tr><td id="18-4">getGyroscope(int16_t* x, int16_t* y, int16_t* z))</td><td id="18-5">You can use this function to get the gyros X/Y/Z 3-axis data at the same time, and t of the data is dps</td></tr>
<tr><td id="18-6">getGyroscopeX(void) getGyroscopeY(void) getGyroscopeZ(void)</td><td id="18-7">Or, you can get the gyroscope X/Y/Z 3-axi separately by using those three functions the unit of the data is dps</td></tr>
<tr><td id="18-8">getRawGyroscopeX(void) getRawGyroscopeX(void) getRawGyroscopeX(void)</td><td id="18-9">Those three functions get the raw data di from the register of ICM20600 without co the data unit to dps</td></tr>
<tr><td id="18-a">getAcceleration(int16_t* x, int16_t* y, int16_t* z)</td><td id="18-b">You can use this function to get the X/Y/Z acceleration at the same time, and the un data is mg</td></tr>
<tr><td id="18-c">getAccelerationX(void) getAccelerationY(void) getAccelerationZ(void)</td><td id="18-d">Or, you can get the X/Y/Z 3-axis accelerat separately by using those three functions the unit of the data is mg</td></tr>
<tr><td id="18-e">getRawAccelerationX(void) getRawAccelerationY(void) getRawAccelerationZ(void)</td><td id="18-f">Those three functions get the raw data di from the register of ICM20600 without co the data unit to mg</td></tr>
<tr><td id="18-g">getTemperature(void) Function</td><td id="18-h">You ca use this function to get the tempe Description</td></tr>
<tr><td id="18-i"></td><td id="18-j"></td></tr>
</table>

<a id='f02e06a6-98f8-46c5-9fdc-584a32163a9e'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='3d0b1c93-a499-4d67-9cc7-4bb2541cbb7f'></a>

19/23

<!-- PAGE BREAK -->

<a id='71e3a01f-6b07-4d31-b777-75f97b1389ff'></a>

7/23/22, 9:09 PM

<a id='e24885dd-f40e-4836-949f-495a7577cc5d'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='28abbbdd-02d5-4bb5-9184-ac8999d7d4b7'></a>

<table><thead><tr><th>AK09918</th><th></th></tr></thead><tbody><tr><td>getData(int32_t *axis_x, int32_t<br>*axis_y, int32_t *axis_z)</td><td>You can use this function to get the magr<br>force of 3-axis.</td></tr></tbody></table>

<a id='a37da718-1124-4cc2-a237-9efde294a70c'></a>

<::logo: [Not discernible]
[No text discernible]
A light gray square with a darker gray left-pointing triangular arrow in the center.::>

<a id='c02469ca-d8aa-4cbb-be19-5cb1a29f334f'></a>

<::logo: [Unknown]
[No readable text]
The logo features a dark gray play icon within a light gray square with rounded corners.:>

<a id='7cdb1668-0d2f-411b-a9c7-1b15f3012d81'></a>

Schematic Online Viewer

<a id='34c0d11d-00ca-4a8f-84bc-0f93f7b593d9'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='3f70952c-9d0a-4b0d-8318-e3812d444cf0'></a>

20/23

<!-- PAGE BREAK -->

<a id='af83df5c-0019-4cf4-83e4-4c5a42bb7623'></a>

7/23/22, 9:09 PM

<a id='ac98f10c-e4e4-4f3d-a8d8-0adfbc0e7e2e'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='c3fc5c74-67c2-4cb7-b36d-1c51d40a23cf'></a>

Resources

*   **[Zip]** Grove - IMU 9DOF (Icm20600+AK09918) Eagle Files
    [https://files.seeedstudio.com/wiki/Grove-IMU_9DOF-Icm20600_AK09918/res/Grove%20-%20IMU%209DOF%20(ICM20600%20%26%20AK09918).zip]
*   **[Zip]** Seeed ICM20600+AK09918 Library
    [https://github.com/Seeed-Studio/Seeed_ICM20600_AK09918/archive/master.zip]
*   **[PDF]** Datasheet of ICM-20600
    [https://files.seeedstudio.com/wiki/Grove-IMU_9DOF-Icm20600_AK09918/res/ICM-20600.pdf]
*   **[PDF]** Datasheet of AK09918
    [https://files.seeedstudio.com/wiki/Grove-IMU_9DOF-Icm20600_AK09918/res/AK09918.pdf]
*   **[PDF]** Datasheet of CJ2102
    [https://files.seeedstudio.com/wiki/Grove-IMU_9DOF-Icm20600_AK09918/res/CJ2102.pdf]

<a id='231e92a4-341f-45e3-a779-47818a07437a'></a>

# Project
This is the introduction Video of this product, simple demos, you can have a try.

<a id='0ef7a673-b735-459e-9c75-7fbf239f3d66'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='9e4f260f-92b5-4663-9579-6dc6e88cfb65'></a>

21/23

<!-- PAGE BREAK -->

<a id='260dcf47-1500-4f58-9db5-0f83972a7f5e'></a>

7/23/22, 9:09 PM

<a id='2bac350d-4803-4c92-be57-deda1e962f19'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='efa4245f-3f54-43ea-8376-305e24d934b4'></a>

All new Grove - Motion Sens...

<::A gray YouTube play button icon, centered on a white background, indicating a video placeholder.
: video_placeholder::>

<a id='3f77e561-c97e-44b8-b3aa-63035cbb701f'></a>

Tech Support

<a id='9da3eb26-5dca-4815-95b4-4edead29201d'></a>

Please do not hesitate to submit the issue into our forum
[https://forum.seeedstudio.com/].

<a id='ec872705-9960-4b8c-a2bb-93d0fdb47da8'></a>

<::image: A marketing banner featuring the "seeed studio" logo and the text "The IoT Hardware Enabler" and "New Products" on a dark teal background. On the right side, against a white background, are several electronic hardware products including two white industrial-style computers, a black and silver portable device, a red and black square mini PC, a blue sensor module, a small development board (like an Arduino Nano), and a green single-board computer (like a Raspberry Pi)::>

[https://www.seeedstudio.com/act-4.html?utm_source=wiki&utm_medium=wikibanner&utm_campaign=newproducts]

<a id='05f6dbd3-de04-44b1-bc8d-65183492dab6'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='882054ee-0ef4-4a09-8e2b-847b290c5b84'></a>

22/23

<!-- PAGE BREAK -->

<a id='97bb7d56-8185-48fc-ae30-b07d807865d9'></a>

7/23/22, 9:09 PM

<a id='880727f1-a996-4545-8480-253df27b2d0a'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='2c977bc6-7b52-4106-9000-8ccd2838c809'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='4119eb12-18bd-490a-a480-56c409a81a94'></a>

23/23