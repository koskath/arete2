<a id='6377c64f-7bbb-4718-9f18-13c4540b2262'></a>

<::logo: TruSens
TruSens
The logo features the word "TruSens" with "Tru" in blue and "Sens" in red, separated by a red and blue radiating signal icon.::>

<a id='f60b3d25-dffa-40cf-a1da-9a312ff1e2db'></a>

**PIR Motion Module**
**HC-SR505**

Order code: 78-4110

<a id='3654518f-2725-4134-b351-e0f1bd3945e4'></a>

<::Two images of an HC-SR505 mini infrared PIR motion sensor module. The module consists of a small green printed circuit board (PCB) with a white dome-shaped sensor at one end. On the PCB, there is a black integrated circuit (IC) and two yellow rectangular capacitors labeled "226C 22387" and "226C 2822". Text on the PCB reads "HC-SR505 D+" and "OS". At the opposite end of the sensor, there are three metal pins for connection. The two images show the module from slightly different angles, highlighting its compact design.: figure::>

<a id='dc73b7fe-8b9d-4817-9251-324257623498'></a>

<::A close-up photograph of an HC-SR505 miniature PIR motion sensor module. The module consists of a green printed circuit board (PCB) with various electronic components mounted on it. On the left side, there is a black three-pin header with silver pins. Two small, rectangular, tan-colored capacitors labeled "A226C 223J2" are visible near the pins. In the center of the PCB, a black integrated circuit (IC) with eight pins is mounted. The text "HC-SR505 D+" is printed in white on the PCB. On the right side, a white, translucent, dome-shaped Fresnel lens, which is characteristic of PIR sensors, is attached to the PCB. The background is dark grey or black.: figure::>

<a id='b3c86168-c161-434a-b77f-0ffb57611402'></a>

# Product Specification

Operating voltage range: DC4.5-20V
Quiescent Current: <60uA
Level output: High 3.3V / Low OV
Trigger: reusable trigger (default)
Delay Time: The default 8S + -30%
Board Dimensions: 10 * 23mm
Induction angle: <100 degrees cone angle
Sensing distance: 3 meters
Working temperature: -20 to +80 degrees
Sensor Lens Dimensions: Diameter 10mm

<a id='297f4321-39ea-4fe3-afaf-0bdcb3953c3f'></a>

1.Interface
<:: Schematic diagram showing a component interface. The component has a curved input side and an output side with three pins. The pins are labeled:
1. -V
2. OUTPUT
3. +V
: diagram::>
2.DC Load
Project 1
<:: Schematic diagram for "DC Load Project 1". The output pin (OUT) of the component is connected to the base of an S8050 NPN transistor. The collector of the transistor is connected to a relay (J) and a parallel diode, which then connects to +12V. The emitter of the transistor is grounded. The relay is labeled "J: Relay".
: diagram::>
3.DC Load
Project 2
<:: Image of a circuit board for "DC Load Project 2". The board has connections labeled 'S', 'O+', '+', '-'. Two red text boxes point to components on the board:
- "Take out the Resistance" points to a resistor.
- "Put on the S8050 Audion(NPN)" points to a transistor.
An output from the board is connected to a relay (J) and a parallel diode, which then connects to +12V. The relay is labeled "J: Relay".
: image::> 

<a id='743ede75-8dcf-484e-839a-4e0bef03d5c2'></a>

Page 1 of 2

<a id='0ae03516-e471-44a2-949b-5ee9f3e07d84'></a>

www.rapidonline.com

<!-- PAGE BREAK -->

<a id='ecf74ba6-0768-4be0-9192-44a6ff27678f'></a>

<::logo: TruSens
TruSens
The logo features the word "TruSens" with "Tru" in blue and "Sens" in red, separated by a red and blue radiating wave symbol.::>

<a id='69d8080f-5498-4876-99f1-bf62e0d361b6'></a>

PIR Motion Module
HC-SR505

<a id='b786e71b-69f0-4178-b182-ed789b7200e5'></a>

Order code: **78-4110**

<a id='e8eb7bc5-1a61-4029-994a-e9495371daf9'></a>

SCHEMATIC
<::Schematic diagram:
IC1 7133-1 VOUT VIN Gnd
D1
+C101 22μ
CY1 103
CY2 104
JP1
U4 BISS0001
Pin 9 INH, Pin 8 VRE/R
Pin 10 AFI, Pin 7 VSS
Pin 11 VCC, Pin 6 ENR
Pin 12 2-, Pin 5 ENC
Pin 13 2+, Pin 4 TC
Pin 14 1-, Pin 3 TR
Pin 15 1+, Pin 2 OUT
Pin 16 A, Pin 1 O
R33 1M
RT1
R13 10k 1M
R14 1K
R32 1M
R6470K RL2 1M
C3 103
R7 6.8K
R4 18K
R9 1M
C6 103
C9 502
R8 18K
C5 103
C103+ 47μ
R10 2K
C4 104
C104 22μ
R3 1M
Cds2
C102 47μ
R1 10K
R2 18K
PIR2
PIR
R5 47k
C2 103::>


<a id='277cb51c-f433-4ad5-891a-d01b8aefa8ea'></a>

www.rapidonline.com

<a id='7375106f-babb-4847-941f-01cd5dc2c00b'></a>

Page 2 of 2

<!-- PAGE BREAK -->

<a id='9cabbc48-af55-4a7a-9628-679a7ae23d2b'></a>

<::logo: TruSens
TruSens
The logo features the word "TruSens" with "Tru" in blue and "Sens" in red, separated by blue and red curved lines that resemble a signal icon.::>

<a id='759f9962-e744-4df5-a38d-d86cbc9e8c0b'></a>

PIR Motion Module
HC-SR505

<a id='6751f148-a884-48fe-bf6e-1055a9ec427b'></a>

Order code: **78-4110**

<a id='6fd7aabe-652f-44df-aa57-24e10c3c0773'></a>

## Hardware
Connect the PIR Motion Sensor to your Arduino/Crowduino power supply pin and digital pins.
You can can connect the "s" terminal to any of your arduino Pins, like the "D6" as belows:

<a id='f3a779b1-6dbe-4e85-bb08-16593e3cc6f4'></a>

<::An orange circuit board, resembling an Arduino, is connected via a blue USB cable to the left. Wires extend from the circuit board to a small sensor module on the right. Labels on the circuit board indicate connections: a yellow wire connected to "D6", a black wire connected to "GND", and a red wire connected to "5V". These three wires then connect to the sensor module, which has corresponding labels "+", "S", and "-" on its connector. The sensor module itself is green with a white dome, characteristic of a PIR motion sensor.: figure::>

<a id='0779355c-3c6f-4ccf-8565-638b95640023'></a>

## Programming

1. Copy the following program to Arduino IDE and upload to your Arduino/Crowduino:

<a id='fdaeb961-e117-44b8-bf01-1fd6903f21cc'></a>

void setup()
{
  Serial.begin(9600);
  pinMode (6, INPUT);
  digitalWrite(6,LOW);
}
void loop()
{
  if (digitalRead(6)==HIGH)
  {
    Serial.println("Somebody is here.");
  }
  else
  {
    Serial.println("Nobody.");
  }
  delay(1000);
}

<a id='bc04c920-95a9-4896-982a-8dbdcda4beca'></a>

Page 3 of 4

<a id='e4a7128b-231d-42a9-921d-a45e1ebae479'></a>

www.rapidonline.com

<!-- PAGE BREAK -->

<a id='b6a483da-c024-41a0-8a97-aa163bf42a32'></a>

<::logo: TruSens
TruSens
This logo features the word "TruSens" with "Tru" in blue and "Sens" in red, separated by a red and blue radiating wave symbol.::>

<a id='f76d85c2-fec5-456e-85c0-8eaf4ed9986d'></a>

PIR Motion Module
HC-SR505

Order code: 78-4110

<a id='9f5149d3-b28e-4cc4-97a7-e8cd7cd7191d'></a>

2. Open the Serial moniter, and set the baudrate to 9600, you will see that When somebody is in front of the sensor, the Serial Monitor will output "Somebody is here." Or, the Serial Monitor output "Nobody."

<a id='16a118f5-5ba0-421d-b6cb-9d3840456f3d'></a>

COM33

[ ] Send

Nobody.
Nobody.
Nobody.
Nobody.
Nobody.
Nobody.
Nobody.
Somebody is here.
Somebody is here.
Somebody is here.
Somebody is here.
Somebody is here.
Somebody is here.
Somebody is here.
Somebody is here.

option Autoscroll: [x]
Newline
9600 baud

<a id='570ed8b9-a34a-421a-947d-cfb2e3925f39'></a>

Page 4 of 4

<a id='668ab877-3726-45bd-8623-bca9d1e72e04'></a>

www.rapidonline.com