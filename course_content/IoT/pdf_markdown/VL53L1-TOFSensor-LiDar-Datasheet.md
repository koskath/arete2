<a id='349adabc-33cc-4bc4-8950-835ca09e8f96'></a>

<::logo: STMicroelectronics
life.augmented
The logo features the letters "ST" in a stylized, metallic blue font, with "life.augmented" in a smaller, lighter blue text next to it::>

<a id='fc7311fd-bd06-4eb0-8960-e6edd1b3969f'></a>

VL53L1X

<a id='6784e47b-165c-461a-9df2-378c6ac05cd5'></a>

A new generation, long distance ranging Time-of-Flight sensor
based on ST's FlightSense™ technology

<a id='2f69c9fc-cc48-4dab-a745-b488342d39dc'></a>

Datasheet - production data

<a id='ccf1b723-4626-42f8-be86-aef739a02318'></a>

<::An image displaying two electronic components. On the left is a black module with two distinct yellow square-shaped sensors or lenses. On the right, slightly behind and angled, is a green circuit board with golden rectangular contact pads arranged in a grid. The circuit board has the "ST" logo and the text "VL53L1X" printed in white.: figure::>

<a id='f0b0a260-2de0-4e25-b078-436d53eeff41'></a>

# Features
* Fully integrated miniature module
  - Size: 4.9x2.5x1.56 mm
  - Emitter: 940 nm invisible laser (Class1)
  - SPAD (single photon avalanche diode) receiving array with integrated lens
  - Low-power microcontroller running advanced digital firmware
* Pin-to-pin compatible with the VL53L0X FlightSense™ ranging sensor
* Fast and accurate long distance ranging
  - Up to 400 cm distance measurement
  - Up to 50 Hz ranging frequency
* Typical full field-of-view (FoV): 27 °
* Programmable region-of-interest (ROI) size on the receiving array, allowing the sensor FoV to be reduced
* Programmable ROI position on the receiving array, providing multizone operation control from the host
* Easy integration
  - Single reflowable component
  - Can be hidden behind many cover window materials
  - Software driver and code examples for turnkey ranging
  - Single power supply (2v8)
  - I²C interface (up to 400 kHz)
  - Shutdown and interrupt pins

<a id='63b4bff9-5174-419e-9a43-dcb1a3efb350'></a>

# Applications

* User detection (Autonomous low-power mode) to power on/off and lock/unlock devices like personal computers/laptops and the IoT
* Service robots and vacuum cleaners (long distance and fast obstacle detection)
* Drones (landing assistance, hovering, ceiling detection)
* Smart shelves and vending machines (goods inventory monitoring)
* Sanitary (robust user detection whatever the target reflectance)
* Smart building and smart lighting (people detection, gesture control)
* 1 D gesture recognition
* Laser assisted autofocus which enhances the camera autofocus system speed and robustness, especially in difficult scenes (low light and low contrast) and video focus tracking assistance

<a id='323c5859-6d8f-4e33-99c3-8506d3430113'></a>

# Description
The VL53L1X is a state-of-the-art, Time-of-Flight (ToF), laser-ranging sensor, enhancing the ST FlightSense™ product family. It is the fastest miniature ToF sensor on the market with accurate ranging up to 4 m and fast ranging frequency up to 50 Hz

<a id='d58a4f80-2619-49be-a4ba-d3038409505c'></a>

Housed in a miniature and reflowable package, it
integrates a SPAD receiving array, a 940 nm
invisible Class1 laser emitter, physical infrared
filters, and optics to achieve the best ranging
performance in various ambient lighting conditions
with a range of cover window options.

<a id='b54c201d-f181-4917-9d54-794cfdc9974c'></a>

Unlike conventional IR sensors, the VL53L1X uses ST's latest generation ToF technology which allows absolute distance measurement whatever the target color and reflectance.

<a id='6b0885c6-7a56-457f-ac4e-ba840d642e70'></a>

It is also possible to program the size of the ROI on the receiving array, allowing the sensor FoV to be reduced.

<a id='fd744008-2b44-4443-9c52-78a1769d343c'></a>

November 2018

<a id='96c3c235-28c2-49f4-9d7a-3eb69f45913b'></a>

DocID031281 Rev 3

<a id='9251e99a-4332-4a7b-97f5-5a86493a18d1'></a>

1/35

<a id='7bf754a8-fc46-4f2f-8de9-a4ff78587945'></a>

This is information on a product in full production.

<a id='3455e07f-6b60-42dd-aadc-015ea0be97d2'></a>

www.st.com

<!-- PAGE BREAK -->

<a id='6cbc0f38-2b77-4722-aff1-ea35cdde21fa'></a>

Contents

<a id='c2e67bf6-f9ea-4f44-b143-bb84c81896ef'></a>

VL53L1X

<a id='f33f3751-4a3e-4ada-a081-ab1414f87b19'></a>

Contents
<table id="1-1">
<tr><td id="1-2">1</td><td id="1-3" colspan="2">&lt;MISSING CELL VALUE&gt;</td></tr>
<tr><td id="1-4"></td><td id="1-5">1.1</td><td id="1-6">Technical specification ........................ 4</td></tr>
<tr><td id="1-7"></td><td id="1-8">1.2</td><td id="1-9">System block diagram .......................... 4</td></tr>
<tr><td id="1-a"></td><td id="1-b">1.3</td><td id="1-c">Device pinout ..................................... 5</td></tr>
<tr><td id="1-d"></td><td id="1-e">1.4</td><td id="1-f">Application schematic ........................... 6</td></tr>
<tr><td id="1-g">2</td><td id="1-h" colspan="2">&lt;MISSING CELL VALUE&gt;</td></tr>
<tr><td id="1-i"></td><td id="1-j">2.1</td><td id="1-k">System functional description ...................... 7</td></tr>
<tr><td id="1-l"></td><td id="1-m">2.2</td><td id="1-n">System state machine description .................. 8</td></tr>
<tr><td id="1-o"></td><td id="1-p">2.3</td><td id="1-q">Customer manufacturing calibration flow ............ 9</td></tr>
<tr><td id="1-r"></td><td id="1-s">2.4</td><td id="1-t">Ranging description ............................... 9</td></tr>
<tr><td id="1-u"></td><td id="1-v">2.5</td><td id="1-w">Key parameters .......................................... 10</td></tr>
<tr><td id="1-x"></td><td id="1-y"></td><td id="1-z">2.5.1 Distance mode .................................... 10</td></tr>
<tr><td id="1-A"></td><td id="1-B"></td><td id="1-C">2.5.2 Timing budget (TB) ................................ 11</td></tr>
<tr><td id="1-D"></td><td id="1-E">2.6</td><td id="1-F">Power sequence .......................................... 12</td></tr>
<tr><td id="1-G"></td><td id="1-H"></td><td id="1-I">2.6.1 Power up and boot sequence ........................ 12</td></tr>
<tr><td id="1-J"></td><td id="1-K">2.7</td><td id="1-L">Ranging sequences ........................................ 13</td></tr>
<tr><td id="1-M"></td><td id="1-N">2.8</td><td id="1-O">Sensing array optical center .................................... 14</td></tr>
<tr><td id="1-P">3</td><td id="1-Q" colspan="2">&lt;MISSING CELL VALUE&gt;</td></tr>
<tr><td id="1-R"></td><td id="1-S">3.1</td><td id="1-T">Test conditions ............................................. 15</td></tr>
<tr><td id="1-U"></td><td id="1-V">3.2</td><td id="1-W">Accuracy, repeatability, and ranging error definitions ................ 16</td></tr>
<tr><td id="1-X"></td><td id="1-Y"></td><td id="1-Z">3.2.1 Accuracy definition ................................. 16</td></tr>
<tr><td id="1-10"></td><td id="1-11"></td><td id="1-12">3.2.2 Repeatability definition ............................ 16</td></tr>
<tr><td id="1-13"></td><td id="1-14"></td><td id="1-15">3.2.3 Ranging error definition ............................ 16</td></tr>
<tr><td id="1-16"></td><td id="1-17">3.3</td><td id="1-18">Minimum ranging distance ................................ 16</td></tr>
<tr><td id="1-19"></td><td id="1-1a">3.4</td><td id="1-1b">Performances in dark conditions ......................... 16</td></tr>
<tr><td id="1-1c"></td><td id="1-1d">3.5</td><td id="1-1e">Performances in ambient light conditions . . . . . . . . . . . . . . . . 17</td></tr>
<tr><td id="1-1f"></td><td id="1-1g"></td><td id="1-1h">3.5.1 Long distance mode . . . . . . . . . . . . . . . . . . . . . . . . 17</td></tr>
<tr><td id="1-1i"></td><td id="1-1j"></td><td id="1-1k">3.5.2 Short distance mode . . . . . . . . . . . . . . . . . . . . . . . . 17</td></tr>
<tr><td id="1-1l"></td><td id="1-1m">3.6</td><td id="1-1n">Performances in partial ROI in dark conditions . . . . . . . . . . . 18</td></tr>
</table>

<a id='94a7c296-aace-4dbb-bafb-ba7c3263f905'></a>

2/35

<a id='26c5ed0e-28ba-4238-807f-711fdfdd214d'></a>

DocID031281 Rev 3

<a id='c4262e39-e8cf-41a4-bce0-aad46418a995'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<!-- PAGE BREAK -->

<a id='c087ca6d-1b7c-4ca6-b371-5bc221685311'></a>

<table id="2-1">
<tr><td id="2-2" colspan="3">VL53L1X</td></tr>
<tr><td id="2-3">4</td><td id="2-4">Control interface</td><td id="2-5">19</td></tr>
<tr><td id="2-6"></td><td id="2-7">4.1 I2C interface - timing characteristics</td><td id="2-8">21</td></tr>
<tr><td id="2-9"></td><td id="2-a">4.2 I2C interface - reference registers</td><td id="2-b">22</td></tr>
<tr><td id="2-c">5</td><td id="2-d">Electrical characteristics</td><td id="2-e">23</td></tr>
<tr><td id="2-f"></td><td id="2-g">5.1 Absolute maximum ratings</td><td id="2-h">23</td></tr>
<tr><td id="2-i"></td><td id="2-j">5.2 Recommended operating conditions</td><td id="2-k">23</td></tr>
<tr><td id="2-l"></td><td id="2-m">5.3 ESD</td><td id="2-n">23</td></tr>
<tr><td id="2-o"></td><td id="2-p">5.4 Current consumption</td><td id="2-q">24</td></tr>
<tr><td id="2-r"></td><td id="2-s">5.5 Digital I/O electrical characteristics</td><td id="2-t">24</td></tr>
<tr><td id="2-u">6</td><td id="2-v">Outline drawing</td><td id="2-w">25</td></tr>
<tr><td id="2-x">7</td><td id="2-y">Laser safety considerations</td><td id="2-z">28</td></tr>
<tr><td id="2-A">8</td><td id="2-B">Packaging and labeling</td><td id="2-C">29</td></tr>
<tr><td id="2-D"></td><td id="2-E">8.1 Product marking</td><td id="2-F">29</td></tr>
<tr><td id="2-G"></td><td id="2-H">8.2 Inner box labeling</td><td id="2-I">29</td></tr>
<tr><td id="2-J"></td><td id="2-K">8.3 Packing</td><td id="2-L">29</td></tr>
<tr><td id="2-M"></td><td id="2-N">8.4 Tape outline drawing</td><td id="2-O">30</td></tr>
<tr><td id="2-P"></td><td id="2-Q">8.5 Pb-free solder reflow process</td><td id="2-R">31</td></tr>
<tr><td id="2-S"></td><td id="2-T">8.6 Handling and storage precautions</td><td id="2-U">32</td></tr>
<tr><td id="2-V"></td><td id="2-W">8.6.1 Shock precaution</td><td id="2-X">32</td></tr>
<tr><td id="2-Y"></td><td id="2-Z">8.6.2 Part handling</td><td id="2-10">32</td></tr>
<tr><td id="2-11"></td><td id="2-12">8.6.3 Compression force</td><td id="2-13">32</td></tr>
<tr><td id="2-14"></td><td id="2-15">8.6.4 Moisture sensitivity level</td><td id="2-16">32</td></tr>
<tr><td id="2-17"></td><td id="2-18">8.7 Storage temperature conditions</td><td id="2-19">32</td></tr>
<tr><td id="2-1a">9</td><td id="2-1b">Ordering information</td><td id="2-1c">33</td></tr>
<tr><td id="2-1d">10</td><td id="2-1e">Acronyms and abbreviations</td><td id="2-1f">33</td></tr>
<tr><td id="2-1g">11</td><td id="2-1h">ECOPACK®</td><td id="2-1i">33</td></tr>
<tr><td id="2-1j">12</td><td id="2-1k">Revision history</td><td id="2-1l">34</td></tr>
</table>

<a id='47692a11-1dfb-4274-87d3-3034945e46bb'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='0ff7181b-0b67-44f1-9dcc-77a1d0a48f84'></a>

DocID031281 Rev 3

<a id='9617ae52-7e0e-4cae-b298-87828f1a971e'></a>

3/35

<!-- PAGE BREAK -->

<a id='ae2e2214-c154-4ecf-b095-30f52f1e7245'></a>

## Product overview

<a id='11f48951-87f9-4c42-b60a-d7acb0c73a9f'></a>

VL53L1X

<a id='f5ed8d75-442e-422e-adf9-c07e5d592784'></a>

1 Product overview

<a id='ec8cb55d-5510-441d-ac40-e3e8e66d3175'></a>

1.1 Technical specification
Table 1. Technical specification
<table id="3-1">
<tr><td id="3-2">Feature</td><td id="3-3">Detail</td></tr>
<tr><td id="3-4">Package</td><td id="3-5">Optical LGA12</td></tr>
<tr><td id="3-6">Size</td><td id="3-7">4.9 x 2.5 x 1.56 mm</td></tr>
<tr><td id="3-8">Operating voltage</td><td id="3-9">2.6 to 3.5 V</td></tr>
<tr><td id="3-a">Operating temperature:</td><td id="3-b">-20 to 85 °C</td></tr>
<tr><td id="3-c">Receiver Field Of View (diagonal FOV)</td><td id="3-d">Programmable from 15 to 27 degrees</td></tr>
<tr><td id="3-e">Infrared emitter</td><td id="3-f">940 nm</td></tr>
<tr><td id="3-g">I²C</td><td id="3-h">Up to 400 kHz (Fast mode) serial bus Programmable address. Default is 0x52.</td></tr>
</table>

<a id='1d2562e9-d774-4f4a-abc9-540c8162644e'></a>

1.2 System block diagram Figure 1. VL53L1X block diagram <::VL53L1X block diagram: diagram::> <::The diagram shows the VL53L1X module, which contains the VL53L1X silicon. The VL53L1X silicon consists of several blocks: Single Photon Avalanche Diode (SPAD) Detection array, Non Volatile Memory, ROM, RAM, Microcontroller, Advanced Ranging Core, and VCSEL Driver. External connections to the module are: GND, SDA, SCL, and AVSSVCSEL on the left side; and AVDD, XSHUT, GPIO1, and AVDDVCSEL on the right side. The VCSEL Driver is connected to an IR emitter with terminals IR+ and IR-, indicating a 940nm wavelength.::>

<a id='76d062f0-dbd3-4638-96de-fe0c49c8f0b1'></a>

4/35

<a id='3c2a1f47-ded7-4bbb-809d-46a69bef3d16'></a>

DocID031281 Rev 3

<a id='a7458246-6e87-4f8f-b2f2-94f3cc9d4ee1'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" stylized in blue, with a horizontal line underneath.::>

<!-- PAGE BREAK -->

<a id='57234303-fcf5-422d-bb4b-54adf1a3bd00'></a>

VL53L1X

<a id='ac8f8a4f-7142-47ea-badc-836ece079a9e'></a>

Product overview

<a id='be149aff-187d-4a3b-8baa-3540c25374cd'></a>

## 1.3 Device pinout

Figure 2 shows the pinout of the VL53L1X (see also Figure 18).

<a id='464beb7a-954a-42a8-bac3-b441f8f9f5ca'></a>

Figure 2. VL53L1X pinout (bottom view)

<::VL53L1X pinout diagram:

GND3
GPIO1: 7
DNC: 8
SDA: 9
SCL: 10
AVDD: 11

XSHUT: 5
GND2: 4
GND: 3
AVSSVCSEL: 2
AVDDVCSEL: 1
12
GND4::>

<a id='21217f91-447f-4a05-af4d-a4b2cb12f637'></a>

Table 2. VL53L1X pin description
<table id="4-1">
<tr><td id="4-2">Pin number</td><td id="4-3">Signal name</td><td id="4-4">Signal type</td><td id="4-5">Signal description</td></tr>
<tr><td id="4-6">1</td><td id="4-7">AVDDVCSEL</td><td id="4-8">Supply</td><td id="4-9">VCSEL supply, to be connected to main supply</td></tr>
<tr><td id="4-a">2</td><td id="4-b">AVSSVCSEL</td><td id="4-c">Ground</td><td id="4-d">VCSEL ground, to be connected to main ground</td></tr>
<tr><td id="4-e">3</td><td id="4-f">GND</td><td id="4-g">Ground</td><td id="4-h">To be connected to main ground</td></tr>
<tr><td id="4-i">4</td><td id="4-j">GND2</td><td id="4-k">Ground</td><td id="4-l">To be connected to main ground</td></tr>
<tr><td id="4-m">5</td><td id="4-n">XSHUT</td><td id="4-o">Digital input</td><td id="4-p">Xshutdown pin, active low</td></tr>
<tr><td id="4-q">6</td><td id="4-r">GND3</td><td id="4-s">Ground</td><td id="4-t">To be connected to main ground</td></tr>
<tr><td id="4-u">7</td><td id="4-v">GPIO1</td><td id="4-w">Digital output</td><td id="4-x">Interrupt output. Open drain output</td></tr>
<tr><td id="4-y">8</td><td id="4-z">DNC</td><td id="4-A">Digital input</td><td id="4-B">Do not connect, must be left floating</td></tr>
<tr><td id="4-C">9</td><td id="4-D">SDA</td><td id="4-E">Digital input/output</td><td id="4-F">I²C serial data</td></tr>
<tr><td id="4-G">10</td><td id="4-H">SCL</td><td id="4-I">Digital input</td><td id="4-J">I²C serial clock input</td></tr>
<tr><td id="4-K">11</td><td id="4-L">AVDD</td><td id="4-M">Supply</td><td id="4-N">Supply, to be connected to main supply</td></tr>
<tr><td id="4-O">12</td><td id="4-P">GND4</td><td id="4-Q">Ground</td><td id="4-R">To be connected to main ground</td></tr>
</table>

<a id='fe1ffc7b-b322-48f7-8764-55884d9cdfd4'></a>

Note: AVSSVCSEL and GND are ground pins and can be connected together in the application schematics.

<a id='3006e783-ee30-4f09-be11-2cf7d202c8ef'></a>

GND2, GND3, and GND4 are standard pins that we force to the ground domain in the
application schematics to avoid possible instabilities if set to other states.

<a id='905c83ea-4850-43a5-983c-2bba877af9b0'></a>

<::logo: STMicroelectronics
ST
A blue stylized 'ST' logo with a horizontal line underneath.::>

<a id='b9095ec7-0a4c-49ad-a460-e1135952b8d8'></a>

DocID031281 Rev 3

<a id='f9938aff-0d5d-4b0a-9ac8-49689326dae1'></a>

5/35

<!-- PAGE BREAK -->

<a id='28559f7d-5200-43fd-9475-a1a4c9a011ad'></a>

Product overview

<a id='9832844f-02cb-499d-a219-686e7cd1fe5f'></a>

VL53L1X

<a id='d8a04f64-8638-45de-a19b-095e7291adfd'></a>

## 1.4 Application schematic

*Figure 3* shows the application schematic of the VL53L1X.

<a id='d69952aa-03a7-42d1-b698-28da9011c3f2'></a>

Figure 3. VL53L1X schematic<::A schematic diagram illustrating the connections for the VL53L1X sensor. The central component is the VL53L1X integrated circuit. On the left side, a "HOST" block is connected to several pins of the VL53L1X: pin 5 (XSHUT), pin 7 (GPIO1), pin 9 (SDA), and pin 10 (SCL). These four pins are also connected to the IOVDD rail via individual pull-up resistors. On the right side of the VL53L1X, pin 1 (AVDDVCSEL) and pin 11 (AVDD) are connected to the AVDD rail. The AVDD rail is filtered by two capacitors in parallel: a 100nF capacitor and a 4.7µF capacitor, both connected to ground. A text note next to these capacitors states: "Capacitors as close as possible to VL53L1X". The VL53L1X has multiple ground pins: pin 3 (GND), pin 4 (GND2), pin 6 (GND3), and pin 12 (GND4), all connected to a common ground reference. Other pins on the VL53L1X include pin 2 (AVSSVCSEL) and pin 8 (DNC).: schematic::>

<a id='d38381e5-635d-409a-8303-706396963a6a'></a>

Note:
Capacitors on external supply AVDD should be placed as close as possible to the AVDDVCSEL and AVSSVCSEL module pins.

<a id='f25e7b63-bacc-4d71-9b82-acaeb6db1377'></a>

Note: External pull up resistor values can be found in IC-bus specification. Pull ups are typically
fitted only once per bus, near the host. For suggested values see Table 3.

<a id='5b965693-adf0-442d-917b-39159a48b19a'></a>

Note: XSHUT pin must always be driven to avoid leakage current. A pull up is needed if the host state is not known.

<a id='dc0338a7-370a-4750-99b8-1d79f0005e75'></a>

_XSHUT_ is needed to use HW standby mode (no I&#178;C communication).

<a id='01b68f50-ec7d-4082-8b81-6d9910e818f2'></a>

Note: XSHUT and GPIO1 pull up recommended values are 10 kOhms

<a id='48a23c90-04c6-4d9c-9c9b-1a1d8ffc76b4'></a>

Note:
GPIO1 to be left unconnected if not used
Table 3 show recommended values for the pull up and series resistors for an AVDD of 1.8 V
to 2.8 V in I2C Fast mode (up to 400 kHz).

<a id='6f5ec403-7802-4fb7-895e-480551d9403b'></a>

Table 3. Suggested pull up and series resistors for I²C Fast mode
<table id="5-1">
<tr><td id="5-2">IC load capacitance (C₁) (1)</td><td id="5-3">Pull up resistor (Ohms)</td></tr>
<tr><td id="5-4">C₁ ≤ 90 pF</td><td id="5-5">3.6 k</td></tr>
<tr><td id="5-6">90 pF &lt; C₁ ≤ 140 pF</td><td id="5-7">2.4 k</td></tr>
<tr><td id="5-8">140 pF &lt; C₁ ≤ 270 pF</td><td id="5-9">1.2 k</td></tr>
<tr><td id="5-a">270 pF &lt; C₁ ≤ 400 pF</td><td id="5-b">0.8 k</td></tr>
</table>
1. For each bus line, Cₗ is measured in the application PCB by the customer.

<a id='56ac7c2e-6f1e-4864-8c4b-d8568c860fe2'></a>

6/35

<a id='b0fbdf24-ba27-416d-9f63-00cda4a462e5'></a>

DocID031281 Rev 3
---

<a id='1d367fdb-a68a-442b-be76-63ae19938f72'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a line underneath.::>

<!-- PAGE BREAK -->

<a id='d89be6e2-6d1a-4c72-bb24-49de5b01f86d'></a>

VL53L1X

<a id='35d66566-7589-4ba7-9527-d6c18abd4611'></a>

Functional description

<a id='10945ba7-5a8d-427a-b4df-dd2c8a2eafa3'></a>

2 Functional description

<a id='8af50796-3490-4dd1-a530-180bafec6d6d'></a>

## 2.1 System functional description

Figure 4 shows the system level functional description. The host customer application controls the VL53L1X device using an API (application programming interface). The API implementation is delivered to the customer as a driver (Bare C code).

<a id='c8f5f7da-f4e2-4275-9143-df84543f6246'></a>

The driver shares with the customer application a set of high-level functions that allow control of the VL53L1X like initialization, ranging start/stop, and setting the system accuracy.

<a id='ccb93e89-85e5-4614-9324-71d617d25d60'></a>

The driver enables fast development of end user applications without the complication of direct multiple register access. The driver is structured in a way that it can be compiled on any kind of platform through a good hardware abstraction layer.

<a id='bcc544f0-d80c-4e68-92aa-428ee4ecd987'></a>

A detailed description of the driver is available in the VL53L1X API user manual (UM2356).

<a id='f6bb6be8-839c-4731-835b-2cc5ff775f22'></a>

Figure 4. VL53L1X system functional description

<::
HOST
  User Application <-> VL53L1X driver
VL53L1X driver --> VL53L1X (via I2C)
: diagram::>

<a id='f574b4c7-bd5b-4dc6-8d30-ddf9127686cf'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='6fe24bed-3cbe-4da4-9c58-7752cbbaded0'></a>

DocID031281 Rev 3

<a id='c7360eef-4477-4af3-a836-cbcf5429695b'></a>

7/35

<!-- PAGE BREAK -->

<a id='7b3a65dd-a190-451d-96e2-dda81c190413'></a>

Functional description

<a id='f10a1b73-1eae-4e1f-9d25-ec73676cc4b1'></a>

VL53L1X

<a id='d8988ab7-9dc5-4256-8bd8-c86692348e42'></a>

## 2.2 System state machine description

Figure 5 shows the system state machine.

<a id='d119d6de-51bc-4452-ac3b-014cf56bb190'></a>

Figure 5. System state machine
<::
flowchart::>
Legend:
- Device States or action: Yellow rounded rectangle
- Host action: Blue rectangle

Flowchart starts with "Power Off" (Device State).

From "Power Off":
- An arrow points to "VDD lowered" (Host action).
- An arrow points to "VDD raised" (Host action).
- An arrow from "VDD lowered" points to "Power Off".
- An arrow from "VDD raised" points to "Power Off".

From "VDD lowered" (Host action):
- An arrow points to "HW Standby" (Device State).
- An arrow from "HW Standby" points to "VDD lowered".

From "VDD raised" (Host action):
- An arrow points to "HW Standby" (Device State).
- An arrow from "HW Standby" points to "VDD raised".

From "HW Standby" (Device State):
- An arrow points to "XSDN lowered" (Host action).
- An arrow points to "XSDN raised" (Host action).
- An arrow from "XSDN lowered" points to "HW Standby".
- An arrow from "XSDN raised" points to "HW Standby".

From "XSDN lowered" (Host action):
- An arrow points to "SW Standby" (Device State).
- An arrow from "SW Standby" points to "XSDN lowered".

From "XSDN raised" (Host action):
- An arrow points to "SW Standby" (Device State).
- An arrow from "SW Standby" points to "XSDN raised".

From "SW Standby" (Device State):
- An arrow points to "Start Measurement" (Host action).
- An arrow from "Stop Measurement" (Host action) points back to "SW Standby".

From "Start Measurement" (Host action):
- An arrow points to "Ranging" (Device State).

From "Ranging" (Device State):
- An arrow points to "Interrupt raised" (Device State).
- An arrow from "Inter meas. completed ?" (Decision) 'YES' path points back to "Ranging".

From "Interrupt raised" (Device State):
- An arrow points to "Get ranging data" (Host action).

From "Get ranging data" (Host action):
- An arrow points to "Clear interrupt" (Host action).

From "Clear interrupt" (Host action):
- An arrow points to "Stop ?" (Decision).

From "Stop ?" (Decision):
- If 'YES', an arrow points to "Stop Measurement" (Host action).
- If 'NO', an arrow points to "Inter meas. completed ?" (Decision).

From "Inter meas. completed ?" (Decision):
- If 'YES', an arrow points back to "Ranging" (Device State).
- If 'NO', an arrow points to "Wait for inter meas completed" (Device State).

From "Wait for inter meas completed" (Device State):
- An arrow points back to "Inter meas. completed ?" (Decision).
<::

<a id='38c68f07-7a21-4376-969d-49b3b0b10953'></a>

8/35

<a id='3130b303-b454-4715-b88c-b0dbbd566247'></a>

DocID031281 Rev 3

<a id='8bced8ab-e18f-419f-8f01-079b1b6ac8bf'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>

<!-- PAGE BREAK -->

<a id='e4afb298-2acb-49c3-bfc0-1a8088c16269'></a>

VL53L1X

<a id='53fb5717-8d6e-4621-a2a5-dea7cb9a1be9'></a>

Functional description

<a id='eb269ac1-87fc-46ec-a231-0b88c6d8fe25'></a>

## 2.3 Customer manufacturing calibration flow

The VL53L1X driver includes calibration functions. To benefit from device full performances, it is recommended they be run once at the customer production line.

Device calibration allows part-to-part parameter variations and cover glass presence that may affect device performances to be compensated.

Calibration data stored in the host have to be loaded into the VL53L1X at each startup using a dedicated driver function.

Three calibration steps are needed: RefSPAD, offset and crosstalk.

RefSPAD and crosstalk calibrations have to be performed whenever the customer adds a protective cover glass on top of the VL53L1X module.

Offset calibration has to be performed in all situations. It allows reflow and cover glass effects to be compensated.

The detailed procedure is provided in the VL53L1X API user manual (UM2356).

<a id='25e5ace5-35f4-4f78-b8ec-4b130ced003d'></a>

## 2.4 Ranging description

The VL53L1X software driver proposes turnkey solution to allow fast implementation and easy ranging in all customer applications:

**Autonomous ranging mode** is the default configuration that offers the optimized VL53L1X functionalities.

*   Ranging is continuous, with a programmable delay between two ranging operations (called an inter-measurement period). Ranging duration (timing budget) is also programmable.
*   The user can set distance thresholds (below, above, inside, or outside the user-defined thresholds). An interrupt is raised only when threshold conditions are met.
*   ROI size and position are programmable: the user may chose a custom FoV from 4x4 SPADs (minimum size) up to 16x16 SPADs (full FoV).
*   A clear interrupt is mandatory to allow the next ranging data to be updated.

If the ranging distance cannot be measured (in the case of no target or a weak signal), a corresponding range status is generated and can be read by the host.

The VL53L1X software driver provides turnkey functions to read output results after the measurement. The main values reported are:

*   Ranging distance in mm
*   Return signal rate
*   Ambient signal rate
*   Range status

<a id='00906155-622e-462c-8986-878dfa09fd3f'></a>

Range status and output measurement definitions are provided in the VL53L1X API user
manual (UM2356).

<a id='978dbac2-9640-44a9-a22d-22fdf5c23792'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font, with a horizontal line beneath it.::>

<a id='9d4662fd-f981-43f5-8f1f-1bcd71437ba7'></a>

DocID031281 Rev 3

<a id='d32b8073-cdd0-46ae-8691-54ceabbce94f'></a>

9/35

<!-- PAGE BREAK -->

<a id='0d8898af-dd94-4b92-adb9-07da56c5ddcb'></a>

Functional description

<a id='8cdf1700-592e-4f45-90c6-c67b38652e6e'></a>

VL53L1X

<a id='a8217fbd-cb73-49ef-8bc3-50181cb3ba2b'></a>

2.5 Key parameters

<a id='b7aa2897-379c-447b-b9a7-6b55bbfdef4c'></a>

## 2.5.1 Distance mode

The VL53L1X has three distance modes (DM): short, medium, and long.

<a id='71c3fab0-ba83-49af-89e0-d949a2de7665'></a>

Long distance mode allows the longest possible ranging distance of 4 m to be reached.
However, this maximum ranging distance is impacted by ambient light.

<a id='cbbbb242-9132-4977-8468-da2c66fe105c'></a>

Short distance mode is more immune to ambient light, but its maximum ranging distance is typically limited to 1.3 m.

<a id='01f2c932-8cc1-449d-a033-b54f0331acde'></a>

Table 4. Maximum distance vs. Distance mode under ambient light
<table id="9-1">
<tr><td id="9-2">Distance mode</td><td id="9-3">Max. distance in dark (cm)</td><td id="9-4">Max. distance under strong ambient light (cm)</td></tr>
<tr><td id="9-5">Short</td><td id="9-6">136</td><td id="9-7">135</td></tr>
<tr><td id="9-8">Medium</td><td id="9-9">290</td><td id="9-a">76</td></tr>
<tr><td id="9-b">Long</td><td id="9-c">360</td><td id="9-d">73</td></tr>
</table>

<a id='c5bddc78-0ec0-4a64-8e3a-d7795c4fc4a9'></a>

Test conditions: timing budget = 100 ms, white target 88%, dark = no IR ambient,
ambient light = 200 kcps/SPAD.

<a id='a7c681aa-86c2-45bf-a9aa-7b6bb2a17a08'></a>

10/35

<a id='7d94a4d4-3296-4f5f-baa3-e481341435ee'></a>

DocID031281 Rev 3

<a id='5e63e7f4-1c88-4a27-8f03-538eb2f7f084'></a>

<::logo: STMicroelectronics
ST
The logo features a stylized blue 'ST' symbol with a horizontal line beneath it.::>

<!-- PAGE BREAK -->

<a id='8e2824f8-1475-4f7f-994d-43aa2d28813f'></a>

VL53L1X

<a id='6fb13a36-c430-4f71-a0a3-239e5210ca66'></a>

Functional description

<a id='534d08c7-97da-479d-b22e-54a34a0bbc56'></a>

## 2.5.2 Timing budget (TB)
The VL53L1X timing budget can be set from 20 ms up to 1000 ms.
* 20 ms is the minimum timing budget and can be used only in Short distance mode.
* 33 ms is the minimum timing budget which can work for all distance modes.
* 140 ms is the timing budget which allows the maximum distance of 4 m (in the dark on a white chart) to be reached under Long distance mode

<a id='7216213d-a1e4-4a18-a4fb-1a661dac778c'></a>

Increasing the timing budget increases the maximum distance the device can range and improves the repeatability error. However, average power consumption augments accordingly.

<a id='dcc82277-edaa-4c50-995f-248304e070c9'></a>

Figure 6. Maximum distance and repeatability error vs. timing budget<::chart: The figure displays three subplots, all titled "Measured distance & Repeatability error" and sharing a common X-axis labeled "Actual distance" ranging from 0 to 4000 (with major ticks at 0, 200, 400, ..., 4000). Each subplot has a left Y-axis with two scales: an upper scale for range from 0 to 3600 (with major ticks at 0, 1200, 1800, 2400, 3000, 3600) and a lower scale for repeatability error from 1.0 to 4.0 (with major ticks at 1.0, 1.6, 2.2, 2.8, 3.4, 4.0). The left Y-axis is labeled "Timing budget" with specific values for each subplot.  The charts plot two data series: "Mean range" (blue line with dots) and "Repeatability error" (red dots).  **Subplot 1: Timing budget = 33 ms**  The blue line for "Mean range" starts around (0, 1200) and increases linearly to approximately (3100, 3600). A label "Max dist = 310 cm" is associated with the end of this line. The red dots for "Repeatability error" start around (0, 3.4), decrease to a minimum around (1200, 1.0), and then slowly increase towards the end of the plot. A label "STDEV (1 sigma) = 5 mm" is associated with the repeatability error data.  **Subplot 2: Timing budget = 140 ms**  The blue line for "Mean range" starts around (0, 1200) and increases linearly to approximately (4000, 3600). A label "Max dist = 400 cm" is associated with the end of this line. The red dots for "Repeatability error" start around (0, 3.4), decrease to a minimum around (1200, 1.0), and then remain relatively low and flat. A label "STDEV = 3.5 mm" is associated with the repeatability error data.  **Subplot 3: Timing budget = 200 ms**  The blue line for "Mean range" starts around (0, 1200) and increases linearly to approximately (4000, 3600). A label "Max dist = 400 cm" is associated with the end of this line. The red dots for "Repeatability error" start around (0, 3.4), decrease to a minimum around (1200, 1.0), and then remain consistently low and flat. A label "STDEV = 2.5 mm" is associated with the repeatability error data.::>

<a id='27c11de0-537d-4ff6-99ae-0279fe18a446'></a>

Test conditions: timing budget = 33 ms, 140 ms, 200 ms, grey target 54 %,
ambient light = dark.

<a id='908c158a-1d95-4a7f-9f01-d15a397b7138'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, italicized blue font, with a horizontal line beneath it.::>

<a id='96e4a1cb-477c-4124-af9b-dedbb5af1720'></a>

DocID031281 Rev 3

<a id='105359b7-9ced-4a75-a8af-12b03daa6415'></a>

11/35

<!-- PAGE BREAK -->

<a id='dda3f7e6-7dd1-45ce-96c3-bfe17690622e'></a>

Functional description

<a id='8c082fe9-cce0-4c52-8c88-3c2bb8154546'></a>

VL53L1X

<a id='4279d6c5-3643-471b-b815-8f27cc1ec476'></a>

## 2.6 Power sequence

### 2.6.1 Power up and boot sequence

There are two options available for device power up/boot.
**Option 1**: the XSHUT pin is connected and controlled from the host.

This option optimizes power consumption as the VL53L1X can be completely powered when not used, and then woken up through a host GPIO (using the XSHUT pin).

<a id='c22ec438-5a9a-464d-b37a-ad07f7545fa4'></a>

Hardware (HW) standby mode is defined as the period when the power supply is present and XSHUT is low.

<a id='a2c5d766-1f1f-4e41-a875-f514ebc7136e'></a>

Figure 7. Power up and boot sequence
<::This figure illustrates the power up and boot sequence with two signal lines and system states over time. The y-axis labels are "Power Supply", "XShut", and "System State".

The "Power Supply" line starts low, then rises to a high level at the first vertical dotted line, and remains high.

The "XShut" line starts low, rises to a high level at the second vertical dotted line, and remains high.

The "System State" is represented by colored blocks along the bottom:
- "Power Off" is the initial state.
- At the first vertical dotted line, it transitions to "HW Standby".
- At the second vertical dotted line, it transitions to "Boot".
- Finally, it transitions to "SW Standby".
: figure::>

<a id='6b56afab-9454-4ca1-a34e-40ca479e3175'></a>

Note:
Boot duration is 1.2ms max.

**Option 2**: the XSHUT pin is not controlled by the host, it is tied to the power supply value through the pull up resistor.

<a id='9d8fabfb-7f2b-4ef7-9f50-dc55d4f38639'></a>

When the XSHUT pin is not not controlled, the power up sequence is presented in Figure 8. In this case, the device goes automatically to Software (SW) standby after boot, without entering HW standby.

<a id='3230a747-3d8c-4331-8c92-5b58efcceb08'></a>

Figure 8. Power up and boot sequence with XSHUT not controlled<::timing diagram::>The diagram illustrates a power up and boot sequence. It shows three rows: 'Power Supply', 'XShut', and 'System State'. The 'Power Supply' line starts low, then transitions to a high state. The 'XShut' line also starts low and transitions to a high state, occurring shortly after the 'Power Supply' transition. The 'System State' is depicted in three sequential blocks: 'Power Off', followed by 'Boot', and then 'SW Standby'. A vertical dashed line indicates the time when 'Power Supply' and 'XShut' transition to high, coinciding with the system state changing from 'Power Off' to 'Boot'. The system then transitions from 'Boot' to 'SW Standby' while 'Power Supply' and 'XShut' remain high.::>

<a id='7aa32125-d484-40ff-a3c6-d32e36386316'></a>

Note: Boot duration is 1.2 ms max.
Note: In all cases, XSHUT has to be raised only when the power supply is tied on.

<a id='0e3ed642-22ca-453e-bb5b-47df2de2e57e'></a>

12/35

<a id='9c6f626d-3e85-4685-8358-91c0548a3e91'></a>

DocID031281 Rev 3

<a id='9590fab0-c98f-4b30-b2bd-255e880e055b'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, futuristic font, with a horizontal line underneath.::>

<a id='89eba69c-afa4-4ab0-b127-41e0a16e521f'></a>

off

<!-- PAGE BREAK -->

<a id='2da62e22-c6e9-4f4a-b684-8c410b4077a1'></a>

VL53L1X

<a id='09e41b65-ccd4-49d3-bc25-7592b0427eb1'></a>

Functional description

<a id='f7d26260-da55-4ac8-b021-37fafd9a11bf'></a>

## 2.7 Ranging sequences
The following figure shows the combination of the driver commands and the system states.

<a id='a4fbc659-7f66-4ba5-86e2-1b2dd4f0217f'></a>

Figure 9. Autonomous sequence

<::
Power Supply
XShut
GPIO1 (Interrupt)
Driver Command: Start Ranging, Get Rang.1, Clear Int., Get Rang.2, Stop Rang.
System State: SW Standby, Ranging Init, Ranging1, Inter. Measurement, Ranging2, Inter. Measurement, SW Standby
Timing Budget
Inter Measurement Period
: chart::>

<a id='4c6eebf7-0e9e-4d73-addf-3b61658f7f8b'></a>

Note: *Timing budget and inter measurement timings are the parameters set by the user, using a dedicated driver function.*

<a id='405df380-9caa-442f-bd81-6c4d23ac1a64'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='4d9188ce-e7fd-4294-af2d-1cded99dfcc8'></a>

DocID031281 Rev 3

<a id='a6efb9a3-69d2-4ce6-ba7d-650b2d2b6e37'></a>

13/35

<!-- PAGE BREAK -->

<a id='3ff4618a-660e-4502-935e-976fda24eec8'></a>

Functional description

<a id='9e50dac0-eb21-4d6c-9fb9-65d167fd422a'></a>

VL53L1X

<a id='7f382d3e-05d7-463f-94e6-226f4ef09631'></a>

## 2.8 Sensing array optical center
VL53L1X module includes a lens that focus the photons on the 16x16 SPADs sensing array.
The sensing array optical center specification takes into account the part-to-part variation in production.

<a id='9371f592-8a7c-4dcf-9247-c72ea7f4d036'></a>

The optical center is defined by coordinates (Xo and Yo).

<a id='19edb4b0-0b45-48e6-980a-b390a426d586'></a>

The optical center is measured for each part during a factory test at STMicroelectronics. The coordinates are stored in the VL53L1X non-volatile memory and are readable by the customer through the software driver in the application. This helps optimize design alignment with the camera and ranging performances in the application.

<a id='230aee5c-734d-4e16-9525-f0fa5dbbd987'></a>

The green array in *Figure 10: Optical center specification* gives the possible location of the optical center.

<a id='93e9164e-f429-477e-8086-2d5f7f4ce52f'></a>

Table 5. Optical center specification
<table id="13-1">
<tr><td id="13-2">Parameter</td><td id="13-3">Min.</td><td id="13-4">Typ.</td><td id="13-5">Max.</td><td id="13-6">Unit</td></tr>
<tr><td id="13-7">Xo offset</td><td id="13-8">-2</td><td id="13-9">0</td><td id="13-a">2</td><td id="13-b" rowspan="2">SPAD</td></tr>
<tr><td id="13-c">Yo offset</td><td id="13-d">-2</td><td id="13-e">0</td><td id="13-f">2</td></tr>
</table>

<a id='7717f608-bc4b-45a2-adb7-f7dae43a0b68'></a>

Figure 10. Optical center specification<::A 2D coordinate system with a grid. The x-axis and y-axis intersect at the origin. A light green square is centered at the origin, extending from -2 to 2 on both the x and y axes. The four corners of the square are labeled with their coordinates: top-left (-2, 2), top-right (2, 2), bottom-left (-2, -2), and bottom-right (2, -2). Each label has an arrow pointing to its respective corner.: diagram::>

<a id='d51119ff-c0a9-4814-885f-ca0386d780b0'></a>

For more details please refer to VL53L1X API user manual (UM2356)

<a id='9e742850-9391-423f-8264-907472131a88'></a>

14/35

<a id='b134c4dd-5e92-48f9-9285-745685007901'></a>

DocID031281 Rev 3

<a id='972f56b4-bd7a-459a-87a7-90c2ece51727'></a>

<::logo: STMicroelectronics
ST
The logo features a stylized blue 'ST' symbol above a thin horizontal line.::>

<!-- PAGE BREAK -->

<a id='e23275f6-9965-4ce2-ba3f-602375f67751'></a>

VL53L1X

<a id='717c1ba9-1696-4710-ba55-17e66d63a69c'></a>

Ranging performances

<a id='d5bf507f-4b22-481a-b99d-856a86e28c4a'></a>

# 3 Ranging performances

## 3.1 Test conditions

In all measurement tables of this specification, it is considered that:
1. The full FoV (typically 27°) is covered or a partial FoV is covered after a specific ROI is programmed by the user (array size from 4x4 SPADs to 16x16 SPADs).
2. Charts used as targets are: grey 17 % reflectance (N4.74 Munsell), grey 54 % reflectance (N8.25 Munsell), and white 88 % reflectance (N9.5 Munsell).
3. Nominal voltage (2.8 V) and temperature (23 °C).
4. Detection rate is considered as 100 %.
5. Unless mentioned, the device is setup and controlled through the driver using the following settings:
    a) Distance mode is long
    b) Timing budget is 100 ms
    c) No cover glass is present
    d) Target covers the full FoV
6. Ambient light is defined as follows:
    a) Dark = no IR light in the band 940 nm ±30 nm
    b) 50 kcps/SPAD = lighting on a sunny day from behind a window(a)
    c) 200 kcps/SPAD = lighting on a sunny day from behind a window, with direct illumination on the sensor
    d) For reference, usual office lighting is around 5 kcps/SPAD

<a id='d61ec9c8-366a-4935-a16a-f3139040f6ef'></a>

a. kcps is kilo counts per second. kcps/SPAD is the return ambient rate measured by the VL53L1X.

<a id='de109660-6e36-4bc5-8016-d28421a844be'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, blue font, with a horizontal line underneath.::>

<a id='682e7e46-3238-4c9b-bff4-e8a75317af50'></a>

DocID031281 Rev 3

<a id='965c99d3-d77d-4ad3-a6d6-5470c9000e1a'></a>

15/35

<!-- PAGE BREAK -->

<a id='d78b6723-72b2-432d-b9ad-4e2f293a6fe6'></a>

Ranging performances

<a id='00d2b042-2ce4-40f2-98ba-0c693902b026'></a>

VL53L1X

<a id='d5136169-ac98-4d8b-91c2-3e0efbaf5149'></a>

## 3.2 Accuracy, repeatability, and ranging error definitions

### 3.2.1 Accuracy definition

Accuracy = mean distance – actual distance
*   Mean distance is the average of 32 measured distances
*   Actual distance is the actual target distance

Accuracy can be affected by an offset error, a temperature drift, and a voltage drift.

### 3.2.2 Repeatability definition

Repeatability is the standard deviation of the mean ranging value of 32 measurements. It can be improved by increasing the timing budget. A typical repeatability value for VL53L1X is from \u00b11 % to \u00b10.15 % depending on the timing budget and the ambient light.

### 3.2.3 Ranging error definition

Ranging error = accuracy + repeatability error.

This ranging error value is our metrics in the following performances tables.

## 3.3 Minimum ranging distance

The minimum ranging distance is 4 cm. Under this minimum distance, the sensor will detect a target, but the measurement will not be accurate.

<a id='588b489c-7e1d-406d-8782-29b21b0d17d8'></a>

3.4 Performances in dark conditions
Table 6. Performances in dark conditions
<table id="15-1">
<tr><td id="15-2">Parameter</td><td id="15-3">Target reflectance</td><td id="15-4">Min. value</td><td id="15-5">Typ. value</td></tr>
<tr><td id="15-6" rowspan="3">Max distance (cm)</td><td id="15-7">White 88 %</td><td id="15-8">260</td><td id="15-9">360 (400 with TB = 140 ms)</td></tr>
<tr><td id="15-a">Grey 54 %</td><td id="15-b">220</td><td id="15-c">340</td></tr>
<tr><td id="15-d">Grey 17 %</td><td id="15-e">80</td><td id="15-f">170</td></tr>
<tr><td id="15-g" colspan="2">Ranging error (mm)</td><td id="15-h" colspan="2">± 20</td></tr>
</table>

<a id='e95ef8a5-b7ec-47fe-96f6-99dc5b5ff620'></a>

Test conditions (including those described in _Section 3.1: Test conditions_) are:
* Ambient light = dark
* Timing budget = 100 ms unless mentioned
* Long distance mode

<a id='d77adf99-b134-4c0a-8e0a-f5fd565f542c'></a>

16/35

<a id='b87f57c6-385c-44ef-86d6-09385b59e250'></a>

DocID031281 Rev 3

<a id='d7b8999b-194e-4ede-ac75-be46055ecf27'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a horizontal line beneath it.::>

<!-- PAGE BREAK -->

<a id='bbdbbc5b-0f0e-455b-b2d3-9c1082b5fb64'></a>

VL53L1X

<a id='22b3341f-fde1-43ad-9b88-2042094deb10'></a>

Ranging performances

<a id='c4c2c071-ac6e-456b-a117-ef3344a34a0b'></a>

## 3.5 Performances in ambient light conditions

<a id='27d091e5-1762-4747-8a02-375a534455cf'></a>

## 3.5.1 Long distance mode

<a id='fc0dc0e4-afdb-42b7-9e00-7f89997ca291'></a>

Table 7. Typical performances in ambient light with long distance mode
<table id="16-1">
<tr><td id="16-2">Parameter</td><td id="16-3">Target reflectance</td><td id="16-4">Dark</td><td id="16-5">50 kcps/SPAD</td><td id="16-6">200 kcps/SPAD</td></tr>
<tr><td id="16-7" rowspan="3">Max. distance (cm)</td><td id="16-8">White 88%</td><td id="16-9">360</td><td id="16-a">166</td><td id="16-b">73</td></tr>
<tr><td id="16-c">Grey 54%</td><td id="16-d">340</td><td id="16-e">154</td><td id="16-f">69</td></tr>
<tr><td id="16-g">Grey 17%</td><td id="16-h">170</td><td id="16-i">114</td><td id="16-j">68</td></tr>
<tr><td id="16-k" colspan="2">Ranging error (mm)</td><td id="16-l">± 20</td><td id="16-m">± 25</td><td id="16-n">± 25</td></tr>
</table>

<a id='206115c2-7335-4d08-bbb5-e9af6faaf04f'></a>

Test conditions (including those described in Section 3.1: Test conditions) are:
* Ambient light = dark, 50 kcps/SPAD, 200 kcps/SPAD
* Distance mode = long

<a id='1f95c9fb-4e1a-4887-8d2d-ec578114ccb3'></a>

3.5.2 Short distance mode

<a id='afdb729b-7381-4ab1-b82d-ea60d2462c86'></a>

Table 8. Typical performances in ambient light conditions with short distance mode
<table id="16-o">
<tr><td id="16-p">Parameter</td><td id="16-q">Target reflectance</td><td id="16-r">Dark</td><td id="16-s">200 kcps/SPAD</td></tr>
<tr><td id="16-t" rowspan="3">Max. distance (cm)</td><td id="16-u">White 88 %</td><td id="16-v">130</td><td id="16-w">130</td></tr>
<tr><td id="16-x">Grey 54 %</td><td id="16-y">130</td><td id="16-z">130</td></tr>
<tr><td id="16-A">Grey 17%</td><td id="16-B">130</td><td id="16-C">120</td></tr>
<tr><td id="16-D" colspan="2">Ranging error (mm)</td><td id="16-E">± 20</td><td id="16-F">± 25</td></tr>
</table>

<a id='1bb0e857-c2b1-4b8c-b098-b73c7da3bee9'></a>

Test conditions (including those described in Section 3.1: Test conditions) are:
* Ambient light = dark, 200 kcps/SPAD
* Distance mode = short

<a id='2bd31124-f0bc-49b4-bc74-5e9b6d34855c'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font, with a horizontal line beneath it.::>

<a id='25b79ae0-6d83-4d4e-87da-acd09d1fb9e8'></a>

DocID031281 Rev 3

<a id='21c97845-d61d-4605-96d1-f59f55b02cfc'></a>

17/35

<!-- PAGE BREAK -->

<a id='a0ec232c-45a0-42f3-ae71-84b6675fbd4b'></a>

Ranging performances

<a id='ab0fabcf-0abb-4f78-80b6-9514008c2da7'></a>

VL53L1X

<a id='84b5a66f-9f8c-46dd-9f42-851d11ddf812'></a>

3.6 Performances in partial ROI in dark conditions
Table 9. Typical performances in partial ROI in dark conditions
<table id="17-1">
<tr><td id="17-2">Parameter</td><td id="17-3">Target reflectance</td><td id="17-4">16x16</td><td id="17-5">8x8</td><td id="17-6">4x4</td></tr>
<tr><td id="17-7" rowspan="3">Max. distance (cm)</td><td id="17-8">White 88 %</td><td id="17-9">360</td><td id="17-a">308</td><td id="17-b">170</td></tr>
<tr><td id="17-c">Grey 54 %</td><td id="17-d">340</td><td id="17-e">254</td><td id="17-f">143</td></tr>
<tr><td id="17-g">Grey 17%</td><td id="17-h">170</td><td id="17-i">119</td><td id="17-j">45</td></tr>
<tr><td id="17-k" colspan="2">Diagonal FoV (degrees)</td><td id="17-l">27</td><td id="17-m">20</td><td id="17-n">15</td></tr>
<tr><td id="17-o" colspan="2">Ranging error (mm)</td><td id="17-p">± 20</td><td id="17-q">± 20</td><td id="17-r">± 20</td></tr>
</table>

<a id='acfe99c2-4a0f-476e-85e8-3aa680b0dd00'></a>

Test conditions (including those described in Section 3.1: Test conditions) are:
* Ambient light = dark
* Target covers partial FoV
* ROI centered on optical center
* Long distance mode

<a id='7ca33d0e-8aca-44f1-b467-ac719858ec4a'></a>

18/35

<a id='c11b23b9-358d-4ca5-a9c2-b97cea27a1ab'></a>

DocID031281 Rev 3

<a id='edd5d049-22b0-4cf5-bacd-2834805e9bd7'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>

<!-- PAGE BREAK -->

<a id='487479da-0f9b-45db-8027-b94b174629c8'></a>

VL53L1X

<a id='d72c57e4-76fb-48a8-8ec8-3e78e8708286'></a>

Control interface

<a id='6c12a7ad-a3e2-4ed8-93f3-561c8c8715c1'></a>

## 4 Control interface

This section specifies the control interface. The I2C interface uses two signals: the serial data line (SDA) and serial clock line (SCL). Each device connected to the bus uses a unique address and a simple master/slave relationships exists.

<a id='5835f05b-d260-4a25-906a-eb47b13687f9'></a>

Both SDA and SCL lines are connected to a positive supply voltage using pull up resistors located on the host. Lines are only actively driven low. A high condition occurs when the lines float and the pull up resistors pull them up. When no data are transmitted both lines are high.

<a id='56b4d91d-37e1-4d64-bc30-f5f6fdd31cd7'></a>

Clock signal (SCL) generation is performed by the master device. The master device initiates data transfer. The I2C bus on the VL53L1X has a maximum speed of 400 kbits/s and uses a device address of 0x52.

<a id='69475f21-3281-43b1-bfc0-0052ddc861b7'></a>

Figure 11. Data transfer protocol
<::timing diagram::
This timing diagram illustrates a data transfer protocol, likely I2C, showing the interaction between SDA (Serial Data) and SCL (Serial Clock) lines.

Key elements:
- **SDA line**: Shows data transitions.
- **SCL line**: Shows clock pulses.

Sections of the protocol:
1.  **Start condition (S)**: Indicated by a high-to-low transition on SDA while SCL is high.
2.  **Address or data byte**: A sequence of 8 bits transmitted, synchronized by 8 clock pulses on SCL. The first bit is labeled MSB (Most Significant Bit), and the eighth bit is labeled LSB (Least Significant Bit). The SCL clock pulses are numbered 1 through 8.
3.  **Acknowledge (Ac/Am)**: After the 8 data bits, a 9th clock pulse occurs. During this pulse, the receiving device acknowledges by pulling the SDA line low.
4.  **Stop condition (P)**: Indicated by a low-to-high transition on SDA while SCL is high.

The diagram uses arrows to point to the "Start condition" and "Acknowledge" events, and a box around the 8-bit data transfer labeled "Address or data byte".
::>

<a id='d310e31c-bbad-4d24-b6f6-53267f8d5f5e'></a>

Information is packed in 8-bit packets (bytes) always followed by an acknowledge bit, Ac for VL53L1X acknowledge and Am for master acknowledge (host bus master). The internal data are produced by sampling SDA at a rising edge of SCL. The external data must be stable during the high period of SCL. The exceptions to this are start (S) or stop (P) conditions when SDA falls or rises respectively, while SCL is high.

<a id='bed87642-f187-413f-ae54-97c5a2ecb6fa'></a>

A message contains a series of bytes preceded by a start condition and followed by either a stop or repeated start (another start condition but without a preceding stop condition) followed by another message. The first byte contains the device address (0x52) and also specifies the data direction. If the least significant bit is low (that is, 0x52) the message is a master-write-to-the-slave. If the LSB is set (that is, 0x53) then the message is a master-read-from-the-slave.

<a id='6b9f9acb-8b44-47ce-a0c1-92db00c823f8'></a>

Figure 12. VL53L1X I²C device address: 0x52
MSBit
LSBit
<table id="18-1">
<tr><td id="18-2">0</td><td id="18-3">1</td><td id="18-4">0</td><td id="18-5">1</td><td id="18-6">0</td><td id="18-7">0</td><td id="18-8">1</td><td id="18-9">R/W</td></tr>
</table>

<a id='333713d9-ba06-48d9-b905-1fe8eefbee4e'></a>

All serial interface communications with the camera module must begin with a start condition. The VL53L1X module acknowledges the receipt of a valid address by driving the SDA wire low. The state of the read/write bit (LSB of the address byte) is stored and the next byte of data, sampled from SDA, can be interpreted. During a write sequence, the second byte received provides a 16-bit index which points to one of the internal 8-bit registers.

<a id='954d50bd-006f-47b0-9484-e32dab7ac0c3'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='1c494f03-dffd-4d7c-bc72-aba18a3a2f76'></a>

DocID031281 Rev 3

<a id='eef2b108-d44d-4da4-b86c-4be10b7fcf9d'></a>

19/35

<!-- PAGE BREAK -->

<a id='01b8036d-b305-4c19-9037-3c5e1cf1fa4c'></a>

Control interface

<a id='2f3e27bb-7305-44b6-abfb-1b59636de6c0'></a>

VL53L1X

<a id='53b018ba-0f7b-4075-943f-d1215bb90b06'></a>

Figure 13. VL53L1X data format (write)

<::
Start
S | ADDRESS[7:0] | As | INDEX[15:8] | As | INDEX[7:0] | As | DATA[7:0] | As | P
VL53L1X acknowledges valid address
Acknowledge from VL53L1X
0x52 (write)
Stop
: chart::>

<a id='c5dd0d47-d9e2-469e-8fdd-febb2688f492'></a>

As data are received by the slave, they are written bit-by-bit to a serial/parallel register. After
each data byte has been received by the slave, an acknowledge is generated, the data are
then stored in the internal register addressed by the current index.

<a id='3b5d4c89-3b3a-4c63-b66a-8a7cb1731463'></a>

During a read message, the contents of the register addressed by the current index is read out in the byte following the device address byte. The contents of this register are parallel loaded into the serial/parallel register and clocked out of the device by the falling edge of SCL.

<a id='68e0f65b-9973-437e-90e0-3d076ff6b1a4'></a>

Figure 14. VL53L1X data format (read)

<::
0x52 (write)
S ADDRESS[7:0] As INDEX[15:8] As INDEX[7:0] As P

0x53 (read)
S ADDRESS[7:0] As DATA[7:0] Am P
: chart::>

<a id='8ff5e83d-bec8-47b4-a5e0-bf9fde90f9a4'></a>

At the end of each byte, in both read and write message sequences, an acknowledge is issued by the receiving device (that is, the VL53L1X for a write and the host for a read).

<a id='d52591db-3a6d-43a6-be45-c34cab876db0'></a>

A message can only be terminated by the bus master, either by issuing a stop condition or by a negative acknowledge (that is, **not** pulling the SDA line low) after reading a complete byte during a read operation.

<a id='8c92e2a7-995c-43be-83d0-ab2fac667e06'></a>

The interface also supports auto-increment indexing. After the first data byte has been transferred, the index is automatically incremented by 1. The master can therefore send data bytes continuously to the slave until the slave fails to provide an acknowledge or the master terminates the write communication with a stop condition. If the auto-increment feature is used the master does not have to send address indexes to accompany the data bytes.

<a id='9c0e9023-5195-4bcc-965e-16ed34cb98a4'></a>

Figure 15. VL53L1X data format (sequential write)
0x52 (write)
<table id="19-1">
<tr><td id="19-2">S</td><td id="19-3">ADDRESS[7:0]</td><td id="19-4">As</td><td id="19-5">INDEX[15:8]</td><td id="19-6">As</td><td id="19-7">INDEX[7:0]</td><td id="19-8">As</td><td id="19-9">P</td></tr>
</table>
<table id="19-a">
<tr><td id="19-b">DATA[7:0]</td><td id="19-c">As</td><td id="19-d">DATA[7:0]</td><td id="19-e">As</td><td id="19-f">DATA[7:0]</td><td id="19-g">As (element symbol)</td><td id="19-h">P (element symbol)</td></tr>
</table>

<a id='0f3c566d-1c6a-4677-ac99-d30a8bfbcf83'></a>

20/35

<a id='32d00436-e53a-498e-a2ef-48246a62b869'></a>

DocID031281 Rev 3

<a id='681fc1d8-b531-4ac6-8585-5940ba1ccf69'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a line underneath.::>

<!-- PAGE BREAK -->

<a id='3f0bb5aa-66fe-4a2f-8546-0ced453f0a6c'></a>

VL53L1X

<a id='c1db8d04-953a-4ecc-872c-d76812131111'></a>

Control interface

<a id='7f77cd2c-bc80-480d-91d7-a09a25b5cbc5'></a>

Figure 16. VL53L1X data format (sequential read)
0x52 (write)
<table id="20-1">
<tr><td id="20-2">S</td><td id="20-3">ADDRESS[7:0]</td><td id="20-4">As</td><td id="20-5">INDEX[15:8]</td><td id="20-6">As</td><td id="20-7">INDEX[7:0]</td><td id="20-8">As</td><td id="20-9">P</td></tr>
</table>
0x53 (read)
<table id="20-a">
<tr><td id="20-b">S</td><td id="20-c">ADDRESS[7:0]</td><td id="20-d">As</td><td id="20-e">DATA[7:0]</td><td id="20-f">Am</td><td id="20-g">DATA[7:0]</td><td id="20-h">Am</td></tr>
</table>
<table id="20-i">
<tr><td id="20-j">DATA[7:0]</td><td id="20-k">Am</td><td id="20-l">DATA[7:0]</td><td id="20-m">Am</td><td id="20-n">DATA[7:0]</td><td id="20-o">Am</td><td id="20-p">P</td></tr>
</table>

<a id='f3ec4514-5b61-4ab0-9981-f846fb9b65f0'></a>

## 4.1 I2C interface - timing characteristics

Timing characteristics are shown in Table 10. Please refer to Figure 17 for an explanation of the parameters used.

<a id='688c7242-8185-4ce6-ad81-ab43103ce82c'></a>

Table 10. I²C interface - timing characteristics for Fast mode (400 kHz)
<table id="20-q">
<tr><td id="20-r">Symbol</td><td id="20-s">Parameter</td><td id="20-t">Min.</td><td id="20-u">Typ.</td><td id="20-v">Max.</td><td id="20-w">Unit</td></tr>
<tr><td id="20-x">F12C</td><td id="20-y">Operating frequency</td><td id="20-z">0</td><td id="20-A"></td><td id="20-B">400</td><td id="20-C">kHz</td></tr>
<tr><td id="20-D">tLOW</td><td id="20-E">Clock pulse width low</td><td id="20-F">1.3</td><td id="20-G"></td><td id="20-H"></td><td id="20-I" rowspan="2">μs</td></tr>
<tr><td id="20-J">tHIGH</td><td id="20-K">Clock pulse width high</td><td id="20-L">0.6</td><td id="20-M"></td><td id="20-N"></td></tr>
<tr><td id="20-O">tSP</td><td id="20-P">Pulse width of spikes which are suppressed by the input filter</td><td id="20-Q"></td><td id="20-R"></td><td id="20-S">50</td><td id="20-T">ns</td></tr>
<tr><td id="20-U">tBUF</td><td id="20-V">Bus free time between transmissions</td><td id="20-W">1.3</td><td id="20-X"></td><td id="20-Y"></td><td id="20-Z">μs</td></tr>
<tr><td id="20-10">tHD.STA</td><td id="20-11">Start hold time</td><td id="20-12">0.26</td><td id="20-13"></td><td id="20-14"></td><td id="20-15" rowspan="3">μs</td></tr>
<tr><td id="20-16">tSU.STA</td><td id="20-17">Start set-up time</td><td id="20-18">0.26</td><td id="20-19"></td><td id="20-1a"></td></tr>
<tr><td id="20-1b">tHD.DAT</td><td id="20-1c">Data in hold time</td><td id="20-1d">0</td><td id="20-1e"></td><td id="20-1f">0.9</td></tr>
<tr><td id="20-1g">tSU.DAT</td><td id="20-1h">Data in set-up time</td><td id="20-1i">50</td><td id="20-1j"></td><td id="20-1k"></td><td id="20-1l" rowspan="3">ns</td></tr>
<tr><td id="20-1m">tr R</td><td id="20-1n">SCL/SDA rise time</td><td id="20-1o"></td><td id="20-1p"></td><td id="20-1q">300</td></tr>
<tr><td id="20-1r">tF</td><td id="20-1s">SCL/SDA fall time</td><td id="20-1t"></td><td id="20-1u"></td><td id="20-1v">300</td></tr>
<tr><td id="20-1w">tsu.STO</td><td id="20-1x">Stop set-up time</td><td id="20-1y">0.6</td><td id="20-1z"></td><td id="20-1A"></td><td id="20-1B">μs</td></tr>
<tr><td id="20-1C">Ci/o</td><td id="20-1D">Input/output capacitance (SDA)</td><td id="20-1E"></td><td id="20-1F"></td><td id="20-1G">10</td><td id="20-1H" rowspan="3">pF</td></tr>
<tr><td id="20-1I">Cin</td><td id="20-1J">Input capacitance (SCL)</td><td id="20-1K"></td><td id="20-1L"></td><td id="20-1M">4</td></tr>
<tr><td id="20-1N">CḶ</td><td id="20-1O">Load capacitance</td><td id="20-1P">–</td><td id="20-1Q">125</td><td id="20-1R">400</td></tr>
</table>

<a id='31b9fd54-4e78-4eff-8577-104fb62a68ae'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font with a horizontal line beneath it.::>

<a id='c975390b-de4f-422a-94e2-12e2d40ce84e'></a>

DocID031281 Rev 3

<a id='25691e6a-1c8a-4219-9c97-7defdf695892'></a>

21/35

<!-- PAGE BREAK -->

<a id='eb1f91c7-2a6c-4440-869d-f1dbe0cfc982'></a>

Control interface

<a id='75392c5d-975c-4510-a54e-b73967fad061'></a>

VL53L1X

<a id='f80af2f0-7f25-4e61-9293-4f3aed586fcb'></a>

Figure 17. I²C timing characteristics<::timing diagram::The diagram illustrates I²C timing characteristics with two waveforms: SDA (Serial Data Line) and SCL (Serial Clock Line). Both waveforms show voltage levels relative to VIH (High-level input voltage) and VIL (Low-level input voltage).The SDA line shows 'stop' and 'start' conditions. A 'stop' condition is indicated by a rising edge on SDA while SCL is high, and a 'start' condition by a falling edge on SDA while SCL is high.The SCL line shows clock pulses.Various timing parameters are indicated:tBUF: Bus free time between a stop and start condition.tLOW: Clock low time.tR: Rise time of the signal.tHD.STA: Hold time for the start condition.tHD.DAT: Hold time for data.tF: Fall time of the signal.tHIGH: Clock high time.tSU.DAT: Setup time for data.tSU.STA: Setup time for the start condition.tSU.STO: Setup time for the stop condition.The diagram includes ellipses (...) to indicate continuation of the waveforms.All timings are measured from either VIL or VIH.::>All timings are measured from either VIL or VIH.

<a id='7e48c62c-f5ab-47e0-8bc8-a14df72da5cf'></a>

## 4.2 IC interface - reference registers
The registers shown in the table below can be used to validate the user IC interface.

<a id='9eaa93f5-fe67-48cc-a9cd-89cd407e87f1'></a>

Table 11. Reference registers
<table id="21-1">
<tr><td id="21-2">Register name</td><td id="21-3">Index</td><td id="21-4">After fresh reset, without driver loaded</td></tr>
<tr><td id="21-5">Model ID</td><td id="21-6">0x010F</td><td id="21-7">0xEA</td></tr>
<tr><td id="21-8">Module Type</td><td id="21-9">0x0110</td><td id="21-a">0xCC</td></tr>
<tr><td id="21-b">Mask Revision</td><td id="21-c">0x0111</td><td id="21-d">0x10</td></tr>
</table>

<a id='2304e17d-cb1f-4bc8-bdf8-14c50ccdff55'></a>

Note:
The I2C read/writes can be 8,16 or 32-bit. Multi-byte reads/writes are always addressed in ascending order with MSB first as shown in *Table 12*.
The customer must use the VL53L1X software driver for easy and efficient ranging operations to match performance and accuracy criteria. Hence full register details are not exposed. The customer should refer to the VL53L1X API user manual (UM2356).

<a id='0ca60893-9de5-4c94-afcf-3543476b094b'></a>

Table 12. 32-bit register example
<table id="21-e">
<tr><td id="21-f">Register address</td><td id="21-g">Byte</td></tr>
<tr><td id="21-h">Address</td><td id="21-i">MSB</td></tr>
<tr><td id="21-j">Address + 1</td><td id="21-k">..</td></tr>
<tr><td id="21-l">Address + 2</td><td id="21-m">..</td></tr>
<tr><td id="21-n">Address + 3</td><td id="21-o">LSB</td></tr>
</table>

<a id='e9f159cd-7531-4d87-a390-904e566db6f7'></a>

22/35

<a id='dd50f809-503d-4f2f-8677-daec5a42f1dd'></a>

DocID031281 Rev 3

<a id='38aa7995-7c3b-4fcb-8cea-6c9e820d1f47'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>

<!-- PAGE BREAK -->

<a id='9943eb1a-75be-46ec-b5d7-e06bd9b141de'></a>

VL53L1X

<a id='f8e50ccb-b771-4cd1-92f0-7b9fa6e1088a'></a>

Electrical characteristics

<a id='8f829073-6120-44ed-9375-8cea9f99ee9f'></a>

5 Electrical characteristics

<a id='b24875a4-3985-426f-b2e5-7e6deabec671'></a>

5.1 Absolute maximum ratings

Table 13. Absolute maximum ratings

<table id="22-1">
<tr><td id="22-2">Parameter</td><td id="22-3">Min.</td><td id="22-4">Typ.</td><td id="22-5">Max.</td><td id="22-6">Unit</td></tr>
<tr><td id="22-7">AVDD</td><td id="22-8">-0.5</td><td id="22-9"></td><td id="22-a">3.6</td><td id="22-b" rowspan="2">V</td></tr>
<tr><td id="22-c">SCL, SDA, XSHUT and GPIO1</td><td id="22-d">-0.5</td><td id="22-e"></td><td id="22-f">3.6</td></tr>
</table>

<a id='b1022811-00a2-4515-a863-81f024ddbe1e'></a>

Note:
Stresses above those listed in Table 13 may cause permanent damage to the device. This is a stress rating only and functional operation of the device at these or any other conditions above those indicated in the operational sections of the specification is not implied. Exposure to absolute maximum rating conditions for extended periods may affect device reliability.

<a id='f64af1de-e9cf-44df-a6aa-a3be33dc299a'></a>

5.2 Recommended operating conditions
Table 14. Recommended operating conditions (1)
<table id="22-g">
<tr><td id="22-h" colspan="2">Parameter</td><td id="22-i">Min.</td><td id="22-j">Typ.</td><td id="22-k">Max.</td><td id="22-l">Unit</td></tr>
<tr><td id="22-m" colspan="2">Voltage (AVDD)</td><td id="22-n">2.6</td><td id="22-o">2.8</td><td id="22-p">3.5</td><td id="22-q" rowspan="3">V</td></tr>
<tr><td id="22-r" rowspan="2">IO (IOVDD) (2)</td><td id="22-s">Standard mode</td><td id="22-t">1.6</td><td id="22-u">1.8</td><td id="22-v">1.9</td></tr>
<tr><td id="22-w">2V8 mode (3)(4)</td><td id="22-x">2.6</td><td id="22-y">2.8</td><td id="22-z">3.5</td></tr>
<tr><td id="22-A" colspan="2">Ambient temperature (normal operating)</td><td id="22-B">-20</td><td id="22-C"></td><td id="22-D">85</td><td id="22-E">°C</td></tr>
</table>

<a id='6eaec633-8fe2-4c26-bddf-9e4d13dc31fa'></a>

1. There are no power supply sequencing requirements. The I/Os may be high, low, or floating when AVDD is applied. The I/Os are internally failsafe with no diode connecting them to AVDD
2. XSHUT should be high level only when AVDD is on.
3. SDA, SCL, XSHUT and GPIO1 high levels have to be equal to AVDD in 2V8 mode.
4. The default driver mode is 1V8.
2V8 mode is programmable using device settings loaded by the driver. For more details please refer to the VL53L1X API user manual (UM2356).

<a id='23c21412-83a1-4ddf-837f-677041d2a875'></a>

## 5.3 ESD
The VL53L1X is compliant with ESD values presented in *Table 15*

<a id='95e13942-df12-472a-b3ca-e9614d0d147a'></a>

Table 15. ESD performances
<table id="22-F">
<tr><td id="22-G">Parameter</td><td id="22-H">Specification</td><td id="22-I">Conditions</td></tr>
<tr><td id="22-J">Human body model</td><td id="22-K">JS-001-2012</td><td id="22-L">± 2 kV, 1500 Ohms, 100 pF</td></tr>
<tr><td id="22-M">Charged device model</td><td id="22-N">JESD22-C101</td><td id="22-O">± 500 V</td></tr>
</table>

<a id='c73f726d-a1eb-4057-bd95-8d60ec5fdc26'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, futuristic blue font with a horizontal line underneath.::>

<a id='9833d65a-59af-4f03-a9f8-a12e9919add0'></a>

DocID031281 Rev 3

<a id='83ef723e-e8f3-486e-aa51-e4d295b36fbc'></a>

23/35

<!-- PAGE BREAK -->

<a id='048e1eef-45e1-4984-97ec-117829949e49'></a>

Electrical characteristics

<a id='6ce4e4ad-f0d3-44f1-994d-569fc85a89a9'></a>

VL53L1X

<a id='d180aff2-fb6e-490a-b424-c45e7cb72550'></a>

5.4 Current consumption
Table 16. Power consumption at ambient temperature (1)
<table id="23-1">
<tr><td id="23-2">Parameter</td><td id="23-3">Min.</td><td id="23-4">Typ.</td><td id="23-5">Max.</td><td id="23-6">Unit</td></tr>
<tr><td id="23-7">HW standby</td><td id="23-8">3</td><td id="23-9">5</td><td id="23-a">7</td><td id="23-b" rowspan="3">uA</td></tr>
<tr><td id="23-c">SW standby (2)</td><td id="23-d">4</td><td id="23-e">6</td><td id="23-f">9</td></tr>
<tr><td id="23-g">Inter measurement</td><td id="23-h"></td><td id="23-i">20</td><td id="23-j"></td></tr>
<tr><td id="23-k">Ranging average (AVDD + AVDDVCSEL) (3) (4)</td><td id="23-l"></td><td id="23-m">16</td><td id="23-n">18</td><td id="23-o">mA</td></tr>
<tr><td id="23-p">Average power consumption at 10 Hz with 33 ms timing budget</td><td id="23-q"></td><td id="23-r"></td><td id="23-s">20</td><td id="23-t" rowspan="3">mW</td></tr>
<tr><td id="23-u">Average power consumption at 1 Hz with 20 ms timing budget when no target detected</td><td id="23-v"></td><td id="23-w">0.9</td><td id="23-x"></td></tr>
<tr><td id="23-y">Average power consumption at 1 Hz with 20 ms timing budget when target detected</td><td id="23-z"></td><td id="23-A">1.4</td><td id="23-B"></td></tr>
</table>
1. All current consumption values include silicon process variations. Temperature and voltage are nominal
conditions (23 °C and AVDD 2v8). All values include AVDD and AVDDVCSEL.
2. In 2v8 (IOVDD) mode, pull ups have to be modified, then SW Standby consumption is increased by 0.6 μΑ.
3. Average consumption during ranging operation in long distance mode.
4. Peak current (including VCSEL) can reach 40 mA.

<a id='4c7a901f-f721-48f1-9cb1-6252deb2cd4a'></a>

5.5 Digital I/O electrical characteristics
Table 17. Digital I/O electrical characteristics
<table id="23-C">
<tr><td id="23-D"></td><td id="23-E">Symbol</td><td id="23-F">Parameter</td><td id="23-G">Min.</td><td id="23-H">Typ.</td><td id="23-I">Max.</td><td id="23-J">Unit</td></tr>
<tr><td id="23-K" rowspan="5">Interrupt pin (GPIO1)</td><td id="23-L">VIL</td><td id="23-M">Low level input voltage</td><td id="23-N">–</td><td id="23-O" rowspan="5"></td><td id="23-P">0.3 IOVDD</td><td id="23-Q" rowspan="4">V</td></tr>
<tr><td id="23-R">VIH</td><td id="23-S">High level input voltage</td><td id="23-T">0.7 IOVDD</td><td id="23-U"></td></tr>
<tr><td id="23-V">VOL</td><td id="23-W">Low level output voltage (IOUT = 4 mA)</td><td id="23-X">–</td><td id="23-Y">0.4</td></tr>
<tr><td id="23-Z">VOH</td><td id="23-10">High level output voltage (IOUT = 4 mA)</td><td id="23-11">IOVDD-0.4</td><td id="23-12"></td></tr>
<tr><td id="23-13">FGPIO</td><td id="23-14">Operating frequency (CLOAD = 20 pF)</td><td id="23-15">0</td><td id="23-16">108</td><td id="23-17">MHz</td></tr>
<tr><td id="23-18" rowspan="5">I²C interface (SDA/SCL)</td><td id="23-19">VIL</td><td id="23-1a">Low level input voltage</td><td id="23-1b">-0.5</td><td id="23-1c" rowspan="5"></td><td id="23-1d">0.6</td><td id="23-1e" rowspan="3">V</td></tr>
<tr><td id="23-1f">VIH</td><td id="23-1g">High level input voltage</td><td id="23-1h">1.12</td><td id="23-1i">IOVDD+0.5</td></tr>
<tr><td id="23-1j">VOL</td><td id="23-1k">Low level output voltage (IOUT = 4 mA)</td><td id="23-1l">- (hyphen)</td><td id="23-1m">0.4</td></tr>
<tr><td id="23-1n" rowspan="2">I_IL / I_IH</td><td id="23-1o">Leakage current (1)</td><td id="23-1p">- (hyphen)</td><td id="23-1q">10</td><td id="23-1r" rowspan="2">μA</td></tr>
<tr><td id="23-1s">Leakage current (2)</td><td id="23-1t"></td><td id="23-1u">0.15</td></tr>
</table>
1. AVDD = 0 V
2. AVDD = 2.85 V; I/O voltage = 1.8 V

<a id='025c47ea-73dd-466d-8346-0f49136c8bb6'></a>

24/35

<a id='2a07239d-a85e-4f01-ad0e-307d8ed738ed'></a>

DocID031281 Rev 3

<a id='ed279a70-56a8-432a-908a-5a017b4fa045'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>

<!-- PAGE BREAK -->

<a id='1f7ec158-a745-499e-af92-60f2ff55bcec'></a>

VL53L1X

<a id='ab354696-c8fa-4018-b02a-561af70f2ed4'></a>

Outline drawing

<a id='80d9941c-1bd9-49bf-9323-4a9865cad251'></a>

6

<a id='911ad32d-84b4-4ea4-86e7-2d3ea800b094'></a>

Outline drawing

<a id='6b2942b3-3f30-4f9b-8c17-245968e01c4d'></a>

Figure 18. Outline drawing (page 1/3) <::An outline drawing of the VL53L1 Module, featuring multiple views with detailed dimensions and a connection table. The drawing includes:

**Isometric Views (Top Left):**
Two perspective views of the module, one showing the top and front, the other the top and rear. These views are labeled "Diametric View Scale 10:1".

**Detailed Top-Down View (Middle Left):**
A top-down view of the module showing two circular apertures (lenses) and various dimensions:
- R0.10 in 3 pos.
- Φ0.70 ±0.02 EMT Aperture beneath filter glass
- Φ0.85 RTN Lens diameter beneath filter glass
- 45° angle
- 0.20
- 1.56 ±0.04 (overall width)
- 2.50 ±0.05
- 1.25 ±0.03
- 0.97 ±0.03
- 3 ±0.02
- 4.90 ±0.05 (overall length)
Text: "No draft on trapezoid shaped ends (see note 3)" is placed next to a side profile view of the module.

**Detailed Bottom View (Middle Right):**
A bottom view of the module showing 12 rectangular pads, numbered 1 through 12, with the marking "VL53L1 A PLL Y WW". Dimensions are provided for the pads and their spacing:
- 4.80 (total length of the pad array)
- □0.50 in 12 pos. (size of each pad)
- 2.40 (width of the pad array)
- Vertical spacing dimensions: 1.60, 0.80, 0, 0.15, 0.200 ±0.105, 0.55, 0.600 ±0.105.
- Horizontal spacing dimensions: 0.90, 2.40, 3.20.
An arrow points to an area above the pins, labeled "Area reserved for laser marking".

**Connection Table (Top Right):**
| Pin | Connection |
|---|---|
| 1 | AVDDVCSEL |
| 2 | AVSSVCSEL |
| 3 | GND1 |
| 4 | GND2 |
| 5 | XSHUT |
| 6 | GND3 |
| 7 | GPIO1 |
| 8 | DNC |
| 9 | SDA |
| 10 | SCL |
| 11 | AVDD |
| 12 | GND4 |::>
A
REV.
1.0
2.0
3.0
B
REVISIONS
DESCRIPTION
INITIAL RELEASE
Updated Liner
Area for laser marking of substrate noted on page 1.
DATE
14/12/2016
10/01/2017
07/03/2017
E
F
Drawn Joseph Hannan All dimensions in mm
Date 09/08/2016 Scale 20:1
Drawing No STMicroelectronics Sheet 1 OF 3
Imaging Division
Title VL53L1 Module Outline
life.augmented DM00319387
Notes:---
1. Dimensions marked are inspection dimensions checked at OQC.
2. Unspecified radii 0.05.
3. 2DEG draft on external side side walls of module, unless stated. Dimensions given on edge of
   plastic cap are datumed to base cap surface.
4. Page 2 shows exclusion cones to be kept free of mechanical items which will interfere with
   module operation. They are not system performance cones.
5. Metal connection pads 1-12 are electrolytic plated 0.0003 THK Gold over 0.005 THK Nickel
Interpret drawing per BS8888,
3RD Angle Projection
Tolerances, unless otherwise stated
Linear
0 Place Decimals 0 ±0.05
1 Place Decimals 0. ±0.05
2 Place Decimals 0.0 ±0.05
3 Place Decimals 0.00 ±0.05
Angular ±2 degrees
Diameter +0.05
Position 0.10
Material
---
Finish
---
This drawing and the information within this document are the property of
STMicroelectronics and are STMicroelectronics CONFIDENTIAL INFORMATION.
STMicroelectronics reserves all rights attaching to the drawing and the
information. It must not be copied, transmitted, made public or used in any
manner other than which STMicroelectronics has given prior written permission. 

<a id='b869347e-3ea9-4bdb-b9f7-cfdf90801b71'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, futuristic font, with a horizontal line underneath.::>

<a id='eedececc-0d1c-49bc-9e99-ec13cc11a049'></a>

DocID031281 Rev 3

<a id='c221a89c-74b6-4f73-b06e-d4506f860613'></a>

25/35

<!-- PAGE BREAK -->

<a id='5a935e49-758e-4aa3-8513-83c2b6ec1c4f'></a>

Outline drawing

<a id='94ac167b-66ea-4ced-b27f-10f0d7428063'></a>

VL53L1X

<a id='59547a63-ac9f-4262-a355-fd8383e2c9bf'></a>

Figure 19. Outline drawing (page 2/3)
<::Outline drawing of a VL53L1 module, showing multiple views with dimensions and a PCB pad layout.

**Top View (Left side of drawing)**
-   Overall dimensions and features:
    -   Gate relief 0.05 DEEP in 2 pos.
    -   Dimensions along one side: 0.20, 0.25, 1.82, 2.05, 2.10, 2.25, 2.30
    -   Dimensions along another side: 0.75, 0.40, 0.25, 0.20, 0
    -   Circular features: Ø0.70 0.03 DEEP, Ø0.50 0.05 DEEP in 2 pos.
    -   Other dimensions: 2.45, 2.80, 2.85, 3.08, 4.65

**Side View (Top-middle of drawing)**
-   Dimensions:
    -   Height: 3 ±0.02
    -   Widths: 1.25 ±0.03 (top and bottom), 0.97 ±0.03

**Keepout Cones (Right-middle of drawing)**
-   RTN KEEPOUT Cone:
    -   Angle: 39.60°
    -   Diameter at datum A: Ø1.08
    -   Height: (1.50)
-   EMT KEEPOUT Cone:
    -   Angle: 36.50°
    -   Diameter at datum A: Ø0.84
    -   Height: (1.27)
-   Datum A is indicated.

**PCB Pad Layout (Bottom-middle of drawing)**
-   Title: PCB Pad Layout (looking through top of module)
-   Overall length: 3.70
-   Pad dimensions and spacing:
    -   Width of individual pads: 0.50
    -   Spacing between rows of pads: 1.85
    -   Horizontal spacing between pads: 0.80
    -   Vertical spacing between pads: 0.25
    -   Outer dimensions: 1.05, 2.10
    -   Small feature: 0.08

**Revision History**
| Rev | Date       |
|:----|:-----------|
| 3.0 | 07/03/2017 |
: technical_diagram::>
Rev Date
3.0 07/03/2017

ST
Drawn Joseph Hannan All dimensions in mm
STMicroelectronics
Imaging Division
Date 09/08/2016
Drawing No
life.augmented DM00319387
Scale 20:1
Sheet 2 OF 3
Title VL53L1 Module Outline

Tolerances, unless otherwise stated
Linear
1 Place Decimals 0 ±0.05
2 Place Decimals 0.00 ±0.05
Angular ±2 degrees
Diameter +0.05
Position 0.10
Interpret drawing per BS8888,
3RD Angle Projection
Material
Finish
This drawing and the information within this document are the property of
STMicroelectronics and are STMicroelectronics CONFIDENTIAL INFORMATION.
STMicroelectronics reserves all rights attaching to the drawing and the
information. It must not be copied, transmitted, made public or used in any
manner other than which STMicroelectronics has given prior written permission. 

<a id='ead2832b-56c0-4901-86aa-83fd0b030f00'></a>

26/35

<a id='9fa87051-805e-4a45-9b58-fc7811228bb9'></a>

DocID031281 Rev 3

<a id='409699f5-992a-4775-9bd9-f9d55350abb3'></a>

<::logo: STMicroelectronics
ST
The logo features a stylized blue 'ST' with a horizontal line beneath it.::>

<!-- PAGE BREAK -->

<a id='72aa912e-9fa1-4533-b1b0-91a08077644a'></a>

VL53L1X

<a id='71c112ff-e19e-4847-a3d5-480b904bfc5a'></a>

Outline drawing

<a id='224417c4-4d3d-4a3c-b824-7ebaf405a01b'></a>

The VL53L1X module is delivered with a protective liner covering the top of the cap to protect the sensor from foreign material during the assembly process. It must be removed by the customer just before mounting the cover glass.

<a id='6b0c0b15-049a-426d-8374-f600fa272cfa'></a>

Figure 20. Outline drawing (page 3/3

<::outline drawing of a VL53L1 module, showing a top view and a side view. The top view depicts a rectangular module with overall dimensions 5.20 mm in length and 2.80 mm in width. It features two internal rectangular components and a rounded extension on one side, with dimensions 0.52 mm and 1 mm for the extension. The side view shows the module's height as 1.60 mm (reference) and a small feature with a height of 0.04 mm. The drawing is set against a grid with alphanumeric labels A-F and 1-8.
: technical drawing::>

Rev Date
3.0 07/03/2017

Tolerances, unless otherwise stated
Interpret drawing per BS8888,
3RD Angle Projection
Linear
0 Place Decimals 0 : ±0.10
1 Place Decimals 0.0 : ±0.10
2 Place Decimals 0.00 : ±0.10
Angular : ±2 degrees
Diameter : ±0.10
Position : ±0.10

This drawing and the information within this document are trhe property of
STMicroelectronics and are STMicroelectronics CONFIDENTIAL INFORMATION.
STMicroelectronics reserves all rights attaching to the drawing and the
information. It must not be copied, transmitted, made public or used in any
manner other than which STMicroelectronics has given prior written permission.

Material -
Finish -

<::STMicroelectronics logo with the tagline "life.augmented", accompanied by drawing details including "Drawn Joseph Hannan", "Date 09/08/2016", "STMicroelectronics Imaging Division", "Drawing No DM00319387", "Title VL53L1 Module Outline", "Scale 40:1", and "Sheet 3 OF 3".
: logo and drawing information::>

Drawn Joseph Hannan All dimensions in mm
Date 09/08/2016 STMicroelectronics
Drawing No Imaging Division Scale 40:1
Title VL53L1 Module Outline Sheet 3 OF 3
DM00319387

<a id='1606761e-e5ee-49e6-86dc-d2f048eed47d'></a>

<::logo: STMicroelectronics
ST
The logo features stylized blue letters "ST" with a horizontal line beneath them.::>

<a id='ac145849-654d-4507-87ed-df42f17630f7'></a>

DocID031281 Rev 3
---

<a id='dacab78c-684f-40fa-8c4c-2f0e3780f36c'></a>

27/35

<!-- PAGE BREAK -->

<a id='70b678af-f9fc-43ec-a013-724b7184005c'></a>

Laser safety considerations

<a id='58611532-32ed-4c52-bda1-be2e28d89b9b'></a>

VL53L1X

<a id='9e3b320f-4d62-4f33-86fa-e76604261a57'></a>

7
# Laser safety considerations

The VL53L1X contains a laser emitter and corresponding drive circuitry. The laser output is designed to remain within Class 1 laser safety limits under all reasonably foreseeable conditions including single faults in compliance with IEC 60825-1:2014 (third edition).

<a id='fe533f3a-2968-4e33-87a2-b5023cf93661'></a>

The laser output remains within Class 1 limits as long as the STMicroelectronics'
recommended device settings (driver settings) are used and the operating conditions
specified are respected.

<a id='9303edc0-5fc4-48e9-85a3-167fb4f11841'></a>

The laser output remains within Class 1 limits as long as the STMicroelectronic's recommended device settings are used and the operating conditions specified are respected (particularly the maximum timing budget, as described in the VL53L1X API user manual UM2356).

<a id='ee52a121-fbcc-4b1b-b4e8-b5f30b755082'></a>

The laser output power must not be increased by any means and no optics should be used with the intention of focusing the laser beam.

<a id='a67444be-a424-4112-9682-f68192c97e0c'></a>

Caution: Use of controls or adjustments or performance of procedures other than those specified herein may result in hazardous radiation exposure.

<a id='968418d5-4c78-4a75-8ea1-2cff8b8ebd8e'></a>

Figure 21. Class 1 laser product label

<::CLASS 1
LASER PRODUCT
: figure::>

<a id='c92d7ebe-be3f-476d-a78e-edc1ea83794e'></a>

28/35

<a id='ecf6b3e1-f8ef-4c9a-8f23-ad720a90512d'></a>

DocID031281 Rev 3

<a id='7b22a63b-2200-4eae-a610-a004eb0c8679'></a>

<::logo: STMicroelectronics
ST
The logo features a stylized blue 'ST' with a horizontal line beneath it.::>

<!-- PAGE BREAK -->

<a id='72c85d7f-af5b-4a99-a8fe-86be86c3b80e'></a>

VL53L1X

<a id='8eb0a958-870b-42bf-bec7-6cf6b0f958c6'></a>

Packaging and labeling

<a id='52cf59be-8354-4675-9814-ffadcd06a982'></a>

# 8 Packaging and labeling

## 8.1 Product marking

A 2-line product marking is applied on the backside of the module (i.e. on the substrate). The first line is the silicon product code, and the second line, the internal tracking code.

<a id='05bfbf04-820a-484c-aa77-163c78b716c7'></a>

Figure 22. Example of prototype marking <::An image of a small rectangular electronic component (likely a sensor or integrated circuit) with a green substrate. There are ten square gold-colored pads arranged in two rows of five. In the center of the component, between the two rows of pads, the text "VL53L1B" is visible above "K076651".: figure::>

<a id='38b09857-7705-452b-b4fe-6ef88e7b57bc'></a>

## 8.2 Inner box labeling
The labeling follows the ST standard packing acceptance specification.
The following information will be on the inner box label:
*   Assembly site
*   Sales type
*   Quantity
*   Trace code
*   Marking
*   Bulk ID number

<a id='2bf9ee01-c98b-41a6-a2fd-061557416e6b'></a>

## 8.3 Packing
At customer/subcontractor level, it is recommended to mount the VL53L1X in a clean environment to avoid foreign material deposition.

<a id='e4f12b85-1897-4263-a82a-ce167581deca'></a>

To help avoid any foreign material contamination at phone assembly level the modules are shipped in a tape and reel format with a protective liner.

<a id='2e876eb7-1546-4d65-bff8-2ae22704521d'></a>

The packaging is vacuum-sealed and includes a desiccant.

<a id='a878c7e0-591f-43ae-ae54-0a30f3ea5224'></a>

The liner is compliant with reflow at 260 C. It must be removed during assembly of the customer device, just before mounting the cover glass.

<a id='e655dcd9-a5b4-465c-b6dc-0ccd69fdeb6a'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font, with a horizontal line beneath it.::>

<a id='3ca83079-79b2-4fb9-8d58-9bd36bb5c723'></a>

DocID031281 Rev 3

<a id='9b704039-22d0-4d22-9344-f654c16dd226'></a>

29/35

<!-- PAGE BREAK -->

<a id='ba4f3a37-b8ef-4348-bad0-c762009f6b94'></a>

Packaging and labeling

<a id='7525b2e8-6cf0-480b-86c9-888e4c4d0aed'></a>

VL53L1X

<a id='aa8d404f-0357-443a-8318-8a7540503e02'></a>

8.4 Tape outline drawing

<a id='ff6db93b-1956-4a12-843c-fdfd955f6691'></a>

Figure 23. Tape outline drawing

<a id='eb27989a-6f16-4aca-afdb-c448c7edabd0'></a>

<::Technical drawing: A cross-sectional view of a component, likely an electronic package, showing various dimensions and features. The drawing is labeled "SECTION B-B".

Dimensions provided are:
- Overall thickness (T): 0.30 ± 0.05
- Radius: 2-R0.3max.
- Angle: 45°
- Internal height: 5 max.
- Internal width (bottom): 4.90ref.
- Internal width (top, labeled Bo): 5.30(Bo)
- Overall base width: 6.00ref.
- Step height: 0.62ref.
- Overall height (labeled Ko): 2.00(Ko)
: figure::>

<a id='8658925f-be13-454f-b073-393d19c2644b'></a>

<::Technical drawing of a component or packaging layout with dimensions.: figure::>  
  
<::The drawing shows a series of rectangular pockets and circular holes arranged in a strip.  
  
**Dimensions:**  
*   **Top horizontal dimension:** 5.50±0.05(F)  
*   **Right vertical dimension (holes):** Φ1.50+0.1/-0(Do)  
*   **Vertical spacing of holes:** 4.0(Po)  
*   **Vertical spacing of pockets:** 8.00(P1)  
*   **Vertical offset from pocket center to hole center:** 2.0±0.05(P2)  
*   **Diameter of circular feature within pocket:** Φ1.5MIN (D1)  
*   **Bottom right horizontal dimension:** 1.75(E)  
  
**Labels:**  
*   PIN 1 (pointing to the top-left pocket)  
*   ref. (reference line on the left)  
*   A (two arrows indicating a cross-section or view direction)  
*   B (two lines indicating a dimension or section)  
  
The drawing depicts a repeating pattern of a larger rectangular pocket, followed by a smaller rectangular feature, and then another larger pocket. A series of circular sprocket holes run along the right edge. Dashed lines indicate centerlines and dimension lines.::>

<a id='0767597b-0051-4685-9219-eb0fd1b8c3b3'></a>

1. MATERIAL: CONDUCTIVE POLYSTYRENE
2. Po/P1 10 PITCHES CUMULATIVE TOLERANCE ON TAPE: 0.20
3. Ao & Bo MEASUREMENT POINT TO BE 0.3 FROM BOTTOM POCKET.
4. ALLOWABLE CAMBER TO BE 1/100mm, NON-CUMULATIVE OVER 250mm
5. SURFACE RESISTIVITY 1x10^4<SR<1x10^11 OHMS
6. UNLESS OTHERWISE SPECIFIED ALL INSIDE RADII SHOULD BE 0.2MAX
7. MOLD TYPE: ROTARY MOLD

<a id='959f1f72-dca8-4fb3-9d51-c2290b1a3b74'></a>

<::Technical drawing showing a cross-section, labeled "SECTION A-A", with various dimensions:
- 0.20re
- 1.40ref.
- 1.2pref.
- 4.00ref.
- 0.62ref.
- 2.80(Ao)
- 8 max
- 0.30
- 2-R0.30max.
: technical drawing::>

<a id='a6e2f33d-f8dd-4041-ad65-bbcc041bceb5'></a>

30/35

<a id='60456d33-0f38-4e80-aa6c-bc4fc069fad6'></a>

DocID031281 Rev 3

<a id='0858e7b9-921d-41e1-87de-6dd53a2f0eb8'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold, blue font with a horizontal line beneath it.::>

<!-- PAGE BREAK -->

<a id='3f55be34-92ff-4814-9c58-863b1c0badaa'></a>

VL53L1X

<a id='c26ddcd7-7e5a-401b-a09c-362f132cf583'></a>

Packaging and labeling

<a id='cd3e10f7-17b1-45df-b675-e154bc3c62e2'></a>

## 8.5 Pb-free solder reflow process

Table 18 and Figure 24 show the recommended and maximum values for the solder profile.
Customers have to tune the reflow profile depending on the PCB, solder paste, and material used. We expect customers to follow the recommended reflow profile, which is specifically tuned for VL53L1X package.

<a id='dad89e7b-b8b8-4010-a392-e820447d9531'></a>

For any reason, if a customer must perform a reflow profile which is different from the recommended one (especially peak >240 °C), this new profile must be qualified by the customer at their own risk. In any case, the profile has to be within the "maximum" profile limit described in _Table 18_.

<a id='5cbd71b3-f403-408f-bd4d-78ed8137a16f'></a>

Table 18. Recommended solder profile
<table id="30-1">
<tr><td id="30-2">Parameters</td><td id="30-3">Recommended</td><td id="30-4">Maximum</td><td id="30-5">Units</td></tr>
<tr><td id="30-6">Minimum temperature (Ts min)</td><td id="30-7">130</td><td id="30-8">150</td><td id="30-9">°C</td></tr>
<tr><td id="30-a">Maximum temperature (Ts max)</td><td id="30-b">200</td><td id="30-c">200</td><td id="30-d">°C</td></tr>
<tr><td id="30-e">Time ts (Ts min to Ts max)</td><td id="30-f">90-110</td><td id="30-g">60-120</td><td id="30-h">S</td></tr>
<tr><td id="30-i">Temperature (TL)</td><td id="30-j">217</td><td id="30-k">217</td><td id="30-l">°C</td></tr>
<tr><td id="30-m">Time (tL)</td><td id="30-n">55-65</td><td id="30-o">55 - 65</td><td id="30-p">s</td></tr>
<tr><td id="30-q">Ramp up</td><td id="30-r">2</td><td id="30-s">3</td><td id="30-t">°C/s</td></tr>
<tr><td id="30-u">Temperature (Tp-10)</td><td id="30-v"></td><td id="30-w">235</td><td id="30-x">°C</td></tr>
<tr><td id="30-y">Time (tp)</td><td id="30-z"></td><td id="30-A">10</td><td id="30-B">s</td></tr>
<tr><td id="30-C">Ramp up</td><td id="30-D"></td><td id="30-E">3</td><td id="30-F">°C/s</td></tr>
<tr><td id="30-G">Peak temperature (Tp)</td><td id="30-H">240</td><td id="30-I">245</td><td id="30-J">°C</td></tr>
<tr><td id="30-K">Time to peak</td><td id="30-L">300</td><td id="30-M">300</td><td id="30-N">s</td></tr>
<tr><td id="30-O">Ramp down (peak to T₁)</td><td id="30-P">-4</td><td id="30-Q">-6</td><td id="30-R">°C/s</td></tr>
</table>

<a id='14e93861-0410-4d3a-8d60-9573d71cdf51'></a>

Figure 24. Solder profile
<::A line graph illustrating a solder reflow profile. The y-axis represents temperature, with labeled points from bottom to top as T_Smin, T_Smax, T_L, T_p-10, and T_p. The x-axis represents time, labeled as "Time to peak" for the duration from the start to the highest temperature point. The graph shows a curve with four main segments:
1. An initial rise from the origin to T_Smin.
2. A slower rise from T_Smin to T_Smax, labeled with a time interval t_S.
3. A steeper rise from T_Smax to the peak temperature T_p.
4. A decrease from T_p back to the baseline.
Horizontal dashed lines extend from each temperature label (T_Smin, T_Smax, T_L, T_p-10, T_p) across the graph. Vertical dashed lines mark key points in time corresponding to these temperature levels. The graph also indicates:
- A time interval t_L, representing the duration the temperature is above T_L.
- A time interval t_p, representing the duration the temperature is above T_p-10, centered around the peak temperature T_p.
: chart::>

<a id='769bf51c-4b7e-40b4-bff7-35889552ffb0'></a>

Note: _Temperature mentioned in Table 18 is measured at the top of the VL53L1X package._
Note: _The component should be limited to a maximum of three passes through this solder profile._

<a id='5aae5d9c-a524-411b-8a82-581ab35dcb5c'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='f7cbb3bb-b66c-4f74-a44b-0c33af8aeeed'></a>

DocID031281 Rev 3

<a id='ab934024-a36b-4cc5-ad48-14f03c9262e9'></a>

31/35

<!-- PAGE BREAK -->

<a id='2e34df1c-a355-4713-8c8c-6518adf2510d'></a>

Packaging and labeling VL53L1X

<a id='3a3e3af6-867a-491a-8121-4c0fbfc9642e'></a>

Note:
As the VL53L1X package is not sealed, only a dry reflow process should be used (such as convection reflow). Vapor phase reflow is not suitable for this type of optical component.
The VL53L1X is an optical component and as such, it should be treated carefully. This would typically include using a 'no-wash' assembly process

<a id='990aff95-fad4-48ea-88ed-1f8d85f3a415'></a>

8.6 Handling and storage precautions

<a id='5972114a-46d7-4c48-b3ee-10b6f394894a'></a>

8.6.1

### Shock precaution
Sensor modules house numerous internal components that are susceptible to shock damage. If a unit is subject to excessive shock, is dropped on the floor, or a tray/reel of units is dropped on the floor, it must be rejected, even if no apparent damage is visible.

<a id='7d3cfc85-5eab-45e5-975d-b7f31f02e0eb'></a>

## 8.6.2 Part handling
Handling must be done with non-marring ESD safe carbon, plastic, or teflon tweezers. Ranging modules are susceptible to damage or contamination. The customer is advised to use a clean assembly process after removing the tape from the parts, and until a protective cover glass is mounted.

<a id='f5d1505c-c52f-4521-9cb1-94510b826369'></a>

8.6.3
**Compression force**
A maximum compressive load of 25 N should be applied on the module.

<a id='933620e4-25a4-416d-b895-582458a561a5'></a>

## 8.6.4 Moisture sensitivity level
Moisture sensitivity is level 3 (MSL) as described in IPC/JEDEC JSTD-020-C

<a id='dc238b5c-a7a3-4186-acfb-39e38bd3c119'></a>

8.7 Storage temperature conditions

Table 19. Recommended storage conditions

<table id="31-1">
<tr><td id="31-2">Parameter</td><td id="31-3">Min.</td><td id="31-4">Typ.</td><td id="31-5">Max.</td><td id="31-6">Unit</td></tr>
<tr><td id="31-7">Temperature (storage)</td><td id="31-8">-40</td><td id="31-9">23</td><td id="31-a">85</td><td id="31-b">°C</td></tr>
</table>

<a id='36b18be3-dc21-48e5-b1c6-1289feb663bd'></a>

32/35

<a id='76aa8391-7c3c-454e-be26-2b778ae4c93c'></a>

DocID031281 Rev 3

<a id='3bbf0dc2-6620-4b62-8252-731ae84f29ae'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a horizontal line beneath it.::>

<!-- PAGE BREAK -->

<a id='958ed181-4978-4d25-a2f0-188957e91f86'></a>

VL53L1X

<a id='a88e72df-c0f5-4bcd-b652-a3f251f00b59'></a>

Ordering information

<a id='43c70c57-ac39-4a44-87b4-14d64e890260'></a>

9 Ordering information

<a id='835a324c-93f7-4a83-ab45-24f16de5f20b'></a>

Table 20. Order codes
<table id="32-1">
<tr><td id="32-2">Sales type</td><td id="32-3">Package</td><td id="32-4">Packing</td><td id="32-5">Minimum order quantity</td></tr>
<tr><td id="32-6">VL53L1CXV0FY/1</td><td id="32-7">Optical LGA12 with liner</td><td id="32-8">Tape and reel</td><td id="32-9">3600 pcs</td></tr>
</table>

<a id='cfb6bef7-c287-4231-bfa6-869eea197bd6'></a>

10 Acronyms and abbreviations

<a id='5cf64798-36c8-4b54-a6c2-b991236c944c'></a>

Table 21. Acronyms and abbreviations

<table id="32-a">
<tr><td id="32-b">Acronym/abbreviation</td><td id="32-c">Definition</td></tr>
<tr><td id="32-d">ESD</td><td id="32-e">Electrostatic discharge</td></tr>
<tr><td id="32-f">I²C</td><td id="32-g">Inter-integrated circuit (serial bus)</td></tr>
<tr><td id="32-h">NVM</td><td id="32-i">Non volatile memory</td></tr>
<tr><td id="32-j">SPAD</td><td id="32-k">Single photon avalanche diode</td></tr>
<tr><td id="32-l">FoV</td><td id="32-m">Field of view</td></tr>
<tr><td id="32-n">VCSEL</td><td id="32-o">Vertical cavity surface emitting laser</td></tr>
</table>

<a id='d781afc6-7b91-48ce-a9ca-f9a48d369416'></a>

11

# ECOPACK®

In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK® packages, depending on their level of environmental compliance. ECOPACK® specifications, grade definitions and product status are available at: www.st.com.
ECOPACK® is an ST trademark.

<a id='8954ea41-e316-48fd-a5e5-147b324061e2'></a>

Note: _The ECOPACK® grade for VL53L1X is ECOPACK®2._

<a id='e0802a13-fd9f-46b2-a797-80fd42570780'></a>

<::logo: STMicroelectronics
ST
A stylized blue 'ST' logo with a horizontal line underneath.::>

<a id='e0c4ec8e-2f3c-45fa-bc31-dec8726baa09'></a>

DocID031281 Rev 3

<a id='5b06628d-04cd-4a4f-98e9-746331601fed'></a>

33/35

<!-- PAGE BREAK -->

<a id='5803369e-c2af-4f2b-88ad-cb6effb883ce'></a>

Revision history

<a id='70ef38ac-b5db-4858-9192-9af112c273b6'></a>

VL53L1X

<a id='955326b7-53b8-47f0-bb25-a49ce3e6df18'></a>

# 12 Revision history

<a id='2a4a31fb-48fe-4ad8-96e8-5e3c1ff1c722'></a>

Table 22. Document revision history
<table id="33-1">
<tr><td id="33-2">Date</td><td id="33-3">Revision</td><td id="33-4">Changes</td></tr>
<tr><td id="33-5">08-Feb-2018</td><td id="33-6">1</td><td id="33-7">Initial release</td></tr>
<tr><td id="33-8">14-Feb-2018</td><td id="33-9">2</td><td id="33-a">Updated Applications and Description</td></tr>
<tr><td id="33-b">29-Nov-2018</td><td id="33-c">3</td><td id="33-d">Updated Features: I²C interface up to 400 kHz Table 10: updated tBUF, tR, and tF Table 18: modified Time (tp-10) to Time(tp) Modified Figure 18, Figure 19, and Figure 20 Updated Section 7: Laser safety considerations</td></tr>
</table>

<a id='bfb41458-4527-447a-94c1-3725a17565bf'></a>

34/35

<a id='0f6221b0-491e-4f4d-a645-8f363696cd2e'></a>

DocID031281 Rev 3

<a id='9b58a39e-65fd-4d28-a5ea-09182c598408'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, modern font, with the "T" integrated into the "S", and a horizontal line beneath it, all in blue.::>

<!-- PAGE BREAK -->

<a id='d1b44857-b6c8-4ebd-98cb-cb1c0a6e1326'></a>

VL53L1X

<a id='124fdcbe-cdf5-47fd-b731-6a21e0149292'></a>

**IMPORTANT NOTICE – PLEASE READ CAREFULLY**

<a id='e7e3ef12-6dd0-4063-bee5-cc4ec77fea16'></a>

STMicroelectronics NV and its subsidiaries ("ST") reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST's terms and conditions of sale in place at the time of order acknowledgement.

<a id='1fefd600-deb8-4e85-9944-0ce237f99f2e'></a>

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of Purchasers' products.

<a id='98837190-eb92-45a4-a2f9-2df90ee5a152'></a>

No license, express or implied, to any intellectual property right is granted by ST herein.

<a id='7f1daac8-216d-4faf-a7d8-f801ccc02fce'></a>

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

<a id='b68ec9ac-5a2f-41e4-bfc1-df1c88fe37ac'></a>

ST and the ST logo are trademarks of ST. All other product or service names are the property of their respective owners.

<a id='f2e7f148-a176-4e09-823d-6a09371ec9be'></a>

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

<a id='bb740963-27f4-468e-ae23-52b9fcd4f858'></a>

© 2018 STMicroelectronics – All rights reserved

<a id='f7baaca5-9719-4162-9f5c-0c07d9cf49ec'></a>

<::logo: STMicroelectronics
ST
The logo features the letters "ST" in a stylized, bold blue font, with a horizontal line beneath it.::>

<a id='97ea754c-061e-41c5-9628-ce28d10555bf'></a>

DocID031281 Rev 3

<a id='b9ec1f77-2801-472d-8fd3-df54515b3aa9'></a>

35/35