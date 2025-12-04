<a id='4bab3e3b-ff6e-4119-bf65-8abe72f0ae53'></a>

ARDUINO DOCS

<a id='95260ddc-a711-4587-8821-c83dd83e88bc'></a>

Search on Docs /

<a id='476a6ffe-e5be-41e6-9231-fc0c9b7b2d6a'></a>

Home / Hardware / MKR Connector
Carrier / **DHT Sensor and OLED with**
**MKR Connector Carrier**

<a id='b8a4def8-8af8-4cee-a821-7d7ff8c49a96'></a>

DHT Sensor and
OLED with MKR
Connector Carrier

Learn how to display temperature and
Humidity on an OLED display with the
MKR Connector Carrier.

<a id='4759bc98-179d-47aa-92d2-1cf7cc77a04f'></a>

Author • Arduino
Last revision • 25/01/2022

<a id='5e2f2567-a371-42b2-b0b9-84b4461fac4c'></a>

This basic example teaches you
how to create a circuit that uses
two Grove modules and requires
no soldering. The MKR board you
choose may be anyone of the
MKR family because the
connection is managed through
the MKR Connector Carrier.

<a id='9941a68f-c7b2-43cd-9989-fb4cc3021a0d'></a>

# Hardware Required

*   Arduino MKR family board
*   Arduino MKR Connector Carrier
*   Grove DHT Module
*   Grove OLED 0.96"

<a id='6cdcb3b0-629b-4858-a32f-a0f36673fbfc'></a>

# Circuit

The connection to the Carrier
board requires two standard
Grove cables. The DHT humidity
and temperature sensor goes to
the D0 connector. The OLED
screen is connected to the TWI
connector.

<a id='57d141bd-b7ff-4ef7-b7b8-fcff141ed895'></a>

Help

<!-- PAGE BREAK -->

<a id='1784b379-1c3e-4197-87ea-c2cc30f33d42'></a>

ARDUINODOCS

<a id='a321ef74-8552-4154-a1d6-b5d959a9d357'></a>

← Go Back

## Hardware

---

<a id='84f65b84-8d29-4fb9-8327-167b9808fe8d'></a>

MKR Connector Carrier

Tutorials
---
MKR Connector Carrier Basics
**DHT Sensor and OLED with MKR Connector Carrier**

<a id='356d0401-8260-48f9-bd3e-bde5ef5d511b'></a>

<::image of a blue circuit board labeled "MKR CONNECTOR CARRIER". The board features white connectors along its left edge labeled A0, A1, A2, A3, A4, A5, A6 (under "SERIAL"). Along its right edge, there are white connectors labeled D0, D1, D2, D3, D4, D5, D6 (under "TWI"). In the center, there are pin headers with labels including AREF, DAC0, A0-A6 on one side, and 5V, VIN, VCC, GND, RESET, TX->14, RX<-13, SCL 12, SDA 11, MISO 10, SCK 9, MOSI 8 on the other. At the bottom, a blue screw terminal block is labeled VIN, 5V, 3.3V, GND. The board also contains various integrated circuits and other electronic components.: circuit board::> The MKR Connector Carrier.

<a id='490e7fa7-241a-4a21-858e-52db72172bb4'></a>

<::Top view of a Grove DHT sensor module, showing the white sensor housing with a grid pattern and pins labeled GND, VCC, NC, SIG. The bottom view of the module shows the circuit board with various components, including capacitors, resistors, and an integrated circuit labeled '100'. There are also pins labeled GND, VCC, SDA, SCL, and NC. The module is labeled 'AOSONG AM2322'.
: figure::>
Grove DHT sensor
module.

<a id='eb47976a-8e89-4f3a-bf2a-f66a2a7552cb'></a>

We did not put a MKR board on
the Carrier, but it is required to
get the circuit to work, as
specified in the bill of materials.

<a id='943e1f46-1eb9-4e91-ac81-bde0763f9ca3'></a>

The DHT module uses a specific
pin to communicate with the MKR
board and it is mapped on D0.
This happens because the Grove
standard for digital connections
follows this rule:

<a id='7488ddae-d4d7-4b6f-a1dc-ad6c5574f149'></a>

PinFunctrionNotes

pin1 DnPrimary digital i/o
pin2 Dn+1Secondary digital i/o
pin3 VCC Power to module 5V/3.3V
pin4 GND Ground

<a id='fd58bc76-bc66-440b-8b1f-1b0af9d1b284'></a>

and the module sends SIG on pin
1 that is mapped on the primary
digital I/O.

<a id='0b227559-909a-4d3c-b421-9caf33c74eba'></a>

In the picture, the OLED module is
shown from component side to
let you see the Grove connector. It

<a id='d7a82861-e12c-4761-90f0-421f8af01d5d'></a>

ON THIS PAGE

  Hardware Required
  Circuit
  **Code**

<!-- PAGE BREAK -->

<a id='0c84d4c7-91a6-4447-a491-a3b2c2612cb9'></a>

ARDUINODOCS

<a id='d9bff3bc-a39a-4913-86b0-cb6587269a5f'></a>

Empty input field.

<a id='81aec2c2-ffbc-412f-8ca1-fedfb5e246be'></a>

MKR Connector Carrier that follows this pin mapping:

<a id='86ea08db-d832-4940-842a-56f646977af7'></a>

PinFunctrionNotespin1SCLI2C
Clockpin2SDAI2C
Datapin3VCCPower to module
5V/3.3Vpin4GNDGround

<a id='e405aa0a-67a2-4bac-bdf3-99cac6d4a390'></a>

# CodeTo drive the modules you need to load four separate libraries:```cpp1 #include <DHT.h>2 #include <DHT_U.h>3 #include <Wire.h>4 #include <SeeedOLED.h>```

<a id='0b690440-217f-4790-8fb7-c9ca61069812'></a>

The DHT module is mapped on
D0 when the object dht is
instantiated:

<a id='a03e6ad8-34ad-4db2-a570-b5bbeeed6640'></a>

1 DHT dht(0, DHT22);

<a id='504a97cf-0087-4909-8604-32a0e47e6630'></a>

The rest of the code is
straightforward and keeps
reading the `hum` and `temp`
values to be printed on the OLED
screen.

<a id='2e1a23b5-3618-4faa-9ff6-1a2af8de8d34'></a>

Here is the complete sketch:

<::transcription of the content
: An empty, rounded rectangular box representing a sketch.::>

<!-- PAGE BREAK -->

<a id='ecb9a44a-16d9-44f9-991b-cc0d8515241c'></a>

ARDUINODOCS

<a id='0c598019-e1b5-48c1-91c8-373d7e1da2cb'></a>

____________________________________________________________________________________________________

<a id='51eccad5-44b4-4414-ab4d-19d9f73a0f86'></a>

```c
1 #include <DHT.h>
2 #include <DHT_U.h>
3 #include <Wire.h>
4 #include <SeeedOLED.h>
5 
6 DHT dht(0, DHT22);
7 
8 void setup() {
9 
10   Wire.begin();
11 
12   SeeedOled.init();
13 
14   SeeedOled.clearDisp();
15 
16   SeeedOled.setNormal();
17 
18   SeeedOled.setPageMo();
19 }
20 
21 void loop() {
22 
23   float temp, hum;
24 
25   //Read temperature
26 
27   do {
28 
29     hum = dht.readHum();
30 
    temp = dht.readTemp();
   } while (isnan(hum) || isnan(temp));

   SeeedOled.clearDisplay();
   SeeedOled.setTextXY(0,0);
   SeeedOled.putString("Temp: ");
   SeeedOled.putFloat(temp);
   SeeedOled.putString(" C");

   SeeedOled.setTextXY(1,0);
   SeeedOled.putString("Hum: ");
   SeeedOled.putFloat(hum);
   SeeedOled.putString(" %");

   delay(2000);
}
```

<a id='be79899f-3d8f-4e2c-8483-297d554ff021'></a>

## Suggest changes
The content on [docs.arduino.cc](docs.arduino.cc) is facilitated through a public [GitHub repository](repository.). If you see anything wrong, you can edit this page [here](here.).

## Need support?
*   [Help Center](Help%20Center)
*   [Ask the Arduino Forum](Ask%20the%20Arduino%20Forum)
*   [Discover Arduino](Discover%20Arduino)
*   [Discord](Discord)

## License
The Arduino documentation is licensed under the [Creative Commons Attribution-Share Alike 4.0 license](Creative%20Commons%20Attribution-Share%20Alike%204.0%20license.).

<a id='1c2c542a-0694-4efb-93d3-f2ecbdc4e58c'></a>

Was this article helpful?

<!-- PAGE BREAK -->

<a id='b6b6791b-ff92-4bb4-853e-940cc878ee0a'></a>

ARDUINODOCS

[ ]

<a id='b8e4c17d-2b58-4640-a99f-8c4029a2e5a1'></a>

<::thumbs-up icon and thumbs-down icon
: figure::>

<a id='5602b671-f7de-4c0f-9d7f-93056b56f9e4'></a>

 2025 Arduino Terms Of Service Privacy Policy Security Cookie Settings