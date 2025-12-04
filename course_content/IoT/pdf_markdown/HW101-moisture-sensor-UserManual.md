<a id='0994540e-a566-4db7-933c-e34aa3a304ea'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULE

<a id='c20bdc26-ba74-408d-ad47-c1894ab8645a'></a>

<::logo: HaiWang
HaiWang
A blue stylized 'HW' monogram is positioned above the company name in red text.::>

<a id='9f17b9e2-5462-488b-b664-5adbf398b760'></a>

**HW-101 HW-moisture sensor V1.2**

**Specification**

<a id='d4848aa8-407c-44b7-a54b-7c42c615466a'></a>

<::A black capacitive soil moisture sensor with the text "Capacitive Soil Moisture Sensor v1.2" printed on it. The sensor has a narrow, elongated shape, tapering to a point at one end, which is designed to be inserted into soil. The wider end of the sensor has a small circuit board with various electronic components (capacitors C1-C6, resistors R1-R4, integrated circuit U2, and a transistor T1) and a white 3-pin connector. A three-wire cable (red, black, and yellow wires) is connected to this connector. The other end of the cable has a black 3-pin female header connector.: figure::>

<!-- PAGE BREAK -->

<a id='cc6e6c98-234b-494c-8cd4-bc7d6a46df5e'></a>

<::logo: HaiWang
HaiWang
This logo features a blue abstract letter 'H' above the company name in red text.::>

<a id='6cfba4a2-1c46-4677-8a0d-7c5c28832ede'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULE

<a id='5e3a3a7d-b5af-4831-856d-13b97dcd2fbb'></a>

1. New soil moisture sensor. This capacitive soil moisture sensor is different from most resistive sensors on the market. It uses the principle of capacitive sensing to detect soil moisture. The problem that the resistance sensor is easily corroded is avoided, and its working life is greatly extended.
2. The sensor has a built-in voltage regulator chip, which supports a 3.3~5.5V wide voltage working environment, which means that it can work normally even on the 3.3V Arduino main control board. The iconic DFRobot-Gravity interface ensures the compatibility of the interface and can be directly connected to the Gavity IO expansion board.
3. A micro PC such as a Raspberry Pi only needs an external ADC (analog signal to digital signal) conversion module to work.
4. With an external screen and a motherboard, you can talk to your plant to see if the beloved one is thirsty, and whether it needs a little more water.

<a id='f52ae713-d0e0-401a-9d58-30e31caa2d84'></a>

Product parameters

Working voltage: 3.3 ~ 5.5 VDC

Output voltage: 0 ~ 3.0 VDC

Interface: PH2.54-3P

Size: 98 x 23mm (LxW)

<a id='018956c4-7dfb-480e-b9d1-7e66672bd96a'></a>

Instructions

Prepare

<a id='0d183ea5-962f-4202-92db-04a8b1abcebf'></a>

## Hardware

*   UNO control board x1
*   Soil moisture sensor x1
*   PH2.54-3P wiring x1

<a id='db09ae55-0b1d-4245-874b-90f8a3b81d25'></a>

## Software

*   Arduino IDE V1.6.5

<a id='a5128edd-e83b-414f-81ab-188f0b8bf70c'></a>

**Wiring diagram**

1. Connect the sensor and the main control board as shown

<!-- PAGE BREAK -->

<a id='9678fec9-59b2-458b-be2e-b9b30232f432'></a>

<::logo: HaiWang
HaiWang
A blue stylized 'W' shape with a central rectangular cut-out sits above the company name in red text.::>

<a id='2b001a1d-7dea-4741-b476-c1b4fccb6bdf'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULI

<a id='5e346f59-c429-48c3-8943-62192358a7f0'></a>

<::An image showing an Arduino board (DFRduino UNO v3.0[R3]) connected to a Capacitive Soil Moisture Sensor v1.0. The DFRduino board is black with various components and headers, including a USB port, power jack, digital pins (0-13, GND, AREF), analog pins (A0-A5), and power pins (IOREF, RESET, 3V3, 5V, GND, GND, VIN). The board has 'DFROBOT DFRduino UNO v3.0[R3]' printed on it. The capacitive soil moisture sensor is a black, elongated, spade-shaped PCB with 'Capacitive Soil Moisture Sensor v1.0 DFROBOT' printed on it. It has a 3-pin connector. Three wires connect the sensor to the Arduino: a red wire from the sensor to the 5V pin on the Arduino, a gray wire from the sensor to a GND pin on the Arduino, and a blue wire from the sensor to the A0 analog input pin on the Arduino.: figure::>

<a id='b466aad7-fa97-42e5-b4ca-3b58b0503aa4'></a>

# Calibration code

1. Before officially testing the soil moisture, a calibration process is required;
2. Burn in the calibration code to the Arduino main control board;
3. Open the serial monitoring assistant.
---


<a id='13f6dcf7-26c6-483f-bcf9-516bd7cf38af'></a>

```
void setup() {
  Serial.begin(9600); // open serial port, set the baud rate to 9600 bps
}
void loop() {
  int val;
  val = analogRead(0); //connect sensor to Analog 0
  Serial.print(val); //print the value to serial
  delay(100);
}
```

<a id='1a458595-a1c3-442e-8275-facac3e81bc9'></a>

# Calibration procedure

## Dry humidity calibration

Calibration instructions: define a measurement range by reading the sensor values in air and water respectively.
Open the serial monitor and set the baud rate to 9600 according to the program.

<a id='cf478a0b-80d6-4d4d-a1c7-8fa78a5ec642'></a>

First, place the sensor in the air to read the analog value, which represents the reading when dry. Then take a glass of water, insert the sensor into the water to a certain depth (make a mark, this depth is the depth you will insert into the soil), must not exceed the red warning line! And record the analog value read at this time, which represents 100% humidity. (The output data is inversely proportional to the humidity, and the output in the water is the smallest.) The insertion depth is recommended as shown in the figure.

<!-- PAGE BREAK -->

<a id='432c8e33-aa2f-4bc5-a73e-fb6f997c53d6'></a>

<::logo: HaiWang
HaiWang
This logo features a blue stylized letter 'W' or 'U' shape above the brand name in red text.::>

<a id='8ce35872-ec9a-417c-8a23-6580672e4b15'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULE

<a id='ed437d20-70c6-485d-b4a3-b911ebb0da06'></a>

<::An illustration of a black capacitive soil moisture sensor. The top part of the sensor has a white connector with three wires (red, blue, brown) and some electronic components. Text on the sensor reads "Capacitive Soil Moisture Sensor v1.0DFROBOT" and "DRIVE THE FUTURE". A red horizontal line crosses the sensor, labeled "Warning Line" with a red downward arrow. Two green horizontal lines indicate a range on the sensor, labeled "Recommend Depth" with a green upward and downward arrow. Gray diagonal lines and the word "soil" are shown to the left of the sensor, indicating where it would be inserted into the ground.
: figure::>

<a id='c8119861-75b1-4595-aec4-0cc31a3a51be'></a>

<::transcription of the content
SOII
Recom
ctive
oixture
: figure::>

<a id='40ba57ff-9a30-4df4-ab3d-22ea0625f419'></a>

## Interval setting

Because the sensor value will be affected by the depth of the soil and the tightness of the soil, only the relative humidity of the soil can be detected. We divide the range of humidity into three equal parts, which means dry, humid, and very humid. The two data recorded before are the humidity interval. For example: the reading in the air is 520, and the reading in the water is 260, so it can be divided into (520,430), (430,350], (350,260). These three sections represent dry, wet, and very humid.

<a id='a3c22844-5f6f-476e-8975-fd4c79c25962'></a>

Note: Since this sensor will monitor soil moisture based on the principle of capacitive sensing, placing it in different places with different soil moisture, different tightness, and different insertion depth will reflect different humidity, even in the same place, at the same depth, at During the second insertion, since the first extraction has caused loosening of the soil, the humidity may be lower than the first reading. A

<a id='8faa3b07-7691-4a6b-b9b5-6c7bf9611a36'></a>

Note: Humidity is inversely proportional to the reading.

<a id='003488fc-74c6-49db-9a2e-73b082313863'></a>

## Test code

Bring the two sets of data just recorded into your test code.

<a id='d215dd63-f771-416a-a055-2d683b18da48'></a>

/***************************************************************
This example reads Capacitive Soil Moisture Sensor.

Created 2015-10-21
By berinie Chen <bernie.chen@dfrobot.com>

<!-- PAGE BREAK -->

<a id='8572c888-6d52-4947-ab94-40cf0ff9dfc8'></a>

<::logo: HaiWang
HaiWang
The logo features a stylized blue 'W' shape, which also incorporates an 'H' within its structure, with the brand name 'HaiWang' in red text below it.::>

<a id='b7e89a98-8f71-41a3-8bfc-a9fcae6614ae'></a>

深圳市海王传感器有限公司
Shenzhen haiwang sensor co., LTD HC-SR501 PIR SENSOR MODULE

<a id='5713b11a-b720-4957-9041-abd5406f4a41'></a>

GNU Lesser General Public License.
See <http://www.gnu.org/licenses/> for details.
All above must be included in any redistribution
***

<a id='eb84f2aa-8e24-4620-bd96-8926e1a568bd'></a>

/***Notice and Trouble shooting***
1. Connection and Diagram can be found here
2. This code is tested on Arduino Uno.
***/

<a id='b7c4d5a2-d3c7-429c-b047-1d382332211f'></a>

const int AirValue = 520; //you need to change this value that you had recorded in the air
const int WaterValue = 260; //you need to change this value that you had recorded in the water
int intervals = (AirValue - WaterValue)/3;
int soilMoistureValue = 0;

void setup() {

<a id='35fb35e5-7c56-4b8d-bec5-3b17631f0779'></a>

```c
}
void loop() {
  soilMoistureValue = analogRead(A0); //put Sensor insert into soil
  if (soilMoistureValue > WaterValue && soilMoistureValue < (WaterValue + intervals))
  {
    Serial.println("Very Wet");
  }
  else if (soilMoistureValue > (WaterValue + intervals) && soilMoistureValue < (AirValue - intervals))
  {
    Serial.println("Wet");
  }
  else if (soilMoistureValue < AirValue && soilMoistureValue > (AirValue - intervals))
```

<a id='2175af76-e81a-426e-af2a-b3e7e3082e47'></a>

{Serial.println("Dry");}delay(100);}
---

<a id='1ec32448-6c5d-4009-ae73-e208a991fe30'></a>

RFQ

Q 1. Why is my reading very different from the actual value, I use your Romeo?

<a id='013ac0c9-82b0-4cc5-ac82-915fb1d2224c'></a>

A: Hello! Because Romeo's analog port A0 has an external button, please set the switch next to the button to Off, or use another analog port.

<a id='059b0acc-2588-4792-9a03-627777be8fdb'></a>

Serial.begin(9600); // open serial port, set the baud rate to 9600 bps