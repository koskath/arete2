<a id='314e1e4d-969b-49ad-844c-55903de7d2f2'></a>

12/4/25, 2:52 PM

<a id='d946f9d6-a811-426f-aabf-96b7a71088bf'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='721e0120-4252-4cd5-877c-1a8e6426fca5'></a>

ARDUINODOCS

Search on Docs /

<a id='74a04559-9fc9-4ced-976c-dbf3ce4e20a5'></a>

← Go Back

Library

<a id='1f6dfa95-11db-45fe-aa8a-03a1f7f276ca'></a>

Recents viewed

<a id='87b6c9af-3a6b-448c-8a62-37c84b0a18da'></a>

Arduino SigFox for
MKRFox1200

autowp-mcp2515

Arduino_MKRENV

Arduino_MKRGPS

Arduino_APDS9960

Arduino_MKRIoTCarrier

<a id='fae383d8-0403-43ff-ada8-b35f2af25223'></a>

Home / Programming / Library / Arduino SigFox for MKRFox1200

ON THIS PAGE

<a id='81df35db-23f7-44f1-981e-593609a6b973'></a>

DEVICE CONTROL

Arduino SigFox for
MKRFox1200

<a id='8dbc0fcc-81f7-41f6-a6e5-12c1bde6a8a8'></a>

ARDUINO LGPL-2.1 V1.0.5 Arduino 07/11/2022

Arduino LLC
https://www.arduino.cc/en/Re...

Helper library for MKR Fox 1200 board and ATAB8520E
Sigfox module

This library allows some high level operations on
Sigfox modules, to ease integration with existing
projects

<a id='ff657307-8c9d-4609-9a87-1f16e2dd8a09'></a>

GO TO REPOSITORY

<a id='d58c7483-7318-4b12-be3c-32096e7e96fe'></a>

Usage/Examples Compatibility Releases

<a id='77730daf-d675-4f7b-b695-0f80b08b9c1f'></a>

This library allows you to use the ATMEL SigFox
transceiver (ATAB8520E) on the Arduino MKR FOX
1200 board. You can find out more about this
board through the following links:

<a id='d17efc98-6560-4aea-86fa-e9e96ead3517'></a>

MKR FOX 1200 Store Page.
MKR FOX 1200 Documentation Page.

<a id='c4c946f1-80a9-441c-8349-776aebe89627'></a>

SigFox employs a cellular system that enables
remote devices to connect using Ultra-Narrow
Band (UNB) technology. It requires little energy,
being termed Low-power Wide-area network
(LPWAN).

<a id='baf84a49-7f5f-40d7-9fb9-263a0f221e44'></a>

Check the SigFox coverage in your area!

<a id='4e1f4b86-d003-481f-9875-967757f8b044'></a>

To use this library:

```
1 #include <SigFox.h>
```

<a id='1f2dfaca-310f-4dca-88fc-9e35194bc90c'></a>

Sigfox Class
---


<a id='9f573867-1936-4ec9-87cd-25158a5a7ba9'></a>

SigFox.begin()

## Description

Initializes the Sigfox library and module

<a id='1f60fff1-8677-4bb9-8994-1de34600a519'></a>

Help

<a id='d27d6179-b5b8-476e-87cd-6f62a313eabd'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='3f705dfa-2f1d-40da-9888-f84d2188c845'></a>

1/13

<a id='03a5403c-c1f9-4f64-bd60-b68c1acb421f'></a>

Usage/Examples
Compatibility
Releases
Sigfox Class +

<!-- PAGE BREAK -->

<a id='b0fbbb67-d0eb-4429-9a8b-3db2c9858199'></a>

12/4/25, 2:52 PM

<a id='96e90d48-9c04-45da-b030-864c26c88ec2'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='c8b1213e-3ab6-4f17-a654-bf9dcd56cb0e'></a>

ARDUINODOCS

<a id='785874a7-69d9-4d6c-b56a-f65d8226d992'></a>

## Syntax

```
1 SigFox.begin();
```

<a id='8c6f92cc-9e24-46c9-87d3-fad10c89fa83'></a>

Parameters

None

<a id='841d28e6-6c30-4cd4-8e46-9e93923b5211'></a>

## Returns
true if correctly configured, false otherwise

<a id='17402491-3c2d-4ff0-ba2f-5ac250d2aba0'></a>

# Example

```
1 #include <SigFox.h>
2 #include <ArduinoLowPower.h>
3 
4 void setup() {
5   Serial.begin(115200);
6   while (!Serial) {};
7 
8   if (!SigFox.begin()) {
9     Serial.println("Shield error");
10    return;
11  }
12 
13 void loop() {
14 }
```

<a id='1165aeca-5c25-4d61-9eb4-d86f844f75d9'></a>

SigFox.beginPacket()

<a id='065fa427-2b3e-4915-a743-9bd028dbf7bd'></a>

**Description**

Begins the process of sending a packet

<a id='9445a51f-c7ca-44c7-a383-093ba1fe7cdb'></a>

## Syntax

```
1 SigFox.beginPacket();
```

<a id='b87d5e6f-9283-45cc-b849-2d77726f19a9'></a>

**Parameters**
None

<a id='bef4712c-d679-4d6c-935f-45993e556e65'></a>

Example

<a id='b3821720-4c66-4a17-b434-8ede59098355'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='23f3eb6e-367a-4adc-a787-f7562fe909c7'></a>

2/13

<!-- PAGE BREAK -->

<a id='fdeeeff5-0844-4028-947e-bc86c7e7bad4'></a>

12/4/25, 2:52 PM

<a id='59139d85-255d-4448-b153-2901d895556c'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='2e1a1199-5735-434d-a783-1d46e1e1a92c'></a>

ARDUINODOCS

<a id='4527386b-e9fa-4dc0-be65-88fba45cd156'></a>

#include <SigFox.h>
#include <ArduinoLowPower.h>

void setup() {
 Serial.begin(115200);
 while (!Serial) {};

 if (!SigFox.begin()) {
  Serial.println("Shield error");
  return;
 }
}

void loop() {
 SigFox.begin();
 SigFox.beginPacket();
 SigFox.print("123456789012");
 int ret = SigFox.endPacket();
 if (ret == 0)
  Serial.println("OK");
 else
  Serial.println("KO");
 while (1);
}

<a id='c6a3ff46-3d98-40b6-b573-2abfbe2774cf'></a>

SigFox.parsePacket()

<a id='5991b3bc-80e5-4412-9607-e46ee983fa8e'></a>

## Description
Checks for the presence of a SigFox packet, and reports the size. parsePacket() must be called before reading the buffer with SigFox.read().

<a id='e74e33ff-34e9-42de-8f3c-99f3f4561a24'></a>

## Syntax

```
1 SigFox.parsePacket()
```

<a id='6f96e4ce-6433-4a1e-9e4d-ba52b02309c4'></a>

**Parameters**

None

<a id='999ae2d4-7aa1-44d7-9b29-0df0e340914d'></a>

## Returns

int: the size of a received SigFox packet

<a id='a4d03f03-c8ed-4de7-8efb-1d8acd1b6b11'></a>

v SigFox.statusCode()

# Description

Returns the protocol status code

<a id='4e3ccda2-9c68-4495-b403-67f51dbb8d89'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='02aaa3cb-5ab0-4cab-980f-2516a1349df6'></a>

5/13

<!-- PAGE BREAK -->

<a id='07be0d24-d03e-4c29-88bf-9d8059426a05'></a>

12/4/25, 2:52 PM

<a id='127c28f9-6858-491d-8438-87717a443fe2'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='e3bf6c8f-642d-439b-bdd3-f6f3ce64b089'></a>

ARDUINODOCS

<a id='31d14393-924c-4e5e-bb26-17cdf88e604a'></a>

[ ]

<a id='c94fb2cb-e9d8-4c5d-8e3b-1c6c65f4a45a'></a>

## Syntax

```
1 SigFox.statusCode(protocol);
```

<a id='2093a134-6016-4ca9-bd38-5f535ff857cb'></a>

## Parameters

protocol: can be one of either:
- SSM
- ATMEL
- SIGFOX

<a id='f3e93206-6fd9-4bc4-86c4-d0c4c032a7ef'></a>

**Returns**
the status code of the chosen protocol:

<a id='b532a5cf-d912-41b8-a531-f859b78a619a'></a>

SSM

TBD

<a id='f077ddc7-ca56-4fd8-9449-d52dab291752'></a>

**Atmel**

Bit0: PA on/off indication Bit6: System ready
to operate (system ready event) Bit5: Frame
sent (frame ready event) Bit4 to Bit1: Error
code

<a id='7939c9d9-cf6b-4c42-bdd4-f447d1ba0d05'></a>

0000: no error
0001: command error / not supported
0010: generic error
0011: frequency error
0100: usage error
0101: opening error
0110: closing error
0111: send error

<a id='a89b37f2-7dd0-4885-870e-107a2e632bc2'></a>

SIGFOX
<table id="5-1">
<tr><td id="5-2">0x00</td></tr>
<tr><td id="5-3">No error</td></tr>
<tr><td id="5-4">0x01</td></tr>
<tr><td id="5-5">Manufacturer error</td></tr>
<tr><td id="5-6">0x02</td></tr>
<tr><td id="5-7">ID or key error</td></tr>
<tr><td id="5-8">0x03</td></tr>
<tr><td id="5-9">State machine error</td></tr>
<tr><td id="5-a">0x04</td></tr>
<tr><td id="5-b">Frame size error</td></tr>
<tr><td id="5-c">0x05</td></tr>
<tr><td id="5-d">Manufacturer send error</td></tr>
<tr><td id="5-e">0x06</td></tr>
<tr><td id="5-f">Get voltage/temperature error</td></tr>
<tr><td id="5-g">0x07</td></tr>
<tr><td id="5-h">Close issues encountered</td></tr>
<tr><td id="5-i">0x08</td></tr>
<tr><td id="5-j">API error indication</td></tr>
</table>

<a id='bf6d93a8-b481-43af-8210-a46e1989a809'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='eff8fa5e-123e-437d-9580-d5d3638479d9'></a>

6/13

<!-- PAGE BREAK -->

<a id='2cba6d9d-c1fd-440e-9051-a00719685c7e'></a>

12/4/25, 2:52 PM

<a id='cfab2a6b-f251-4a16-a2fc-f5e437c8f32d'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='cf1e569f-69fc-4355-8993-8ce2b2a2114d'></a>

ARDUINODOCS

<a id='b411d92e-2605-4fd3-b4b0-6ae984266b1b'></a>

0x0A
: Error getting frequency

0x0B
: Error building frame

0x0C
: Error in delay routine

0x0D
: callback causes error

0x0E
: timing error

0x0F
: frequency error

<a id='2fc59756-3e44-4b2e-ba4e-d412ac92cea8'></a>

SigFox.AtmVersion()

# Description

Returns the Atm version

# Syntax

```
1 SigFox.AtmVersion();
```

# Returns

a String of 2 bytes containing the Atm
version

<a id='86202113-62a7-4fc1-a6be-029d10581373'></a>

## SigFox.SigVersion()

### Description
Returns the module's firmware version

### Syntax
```
1 SigFox.SigVersion();
```

### Returns
a String of 2 bytes containing the SigFox
version

<a id='7477f8c6-df30-440e-885b-b80dc5417454'></a>

SigFox.ID()

<a id='7c8c8610-e95b-4934-bc62-50a21246dab0'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='376a6da9-0f5f-4fdc-8bf0-79054859692a'></a>

7/13

<!-- PAGE BREAK -->

<a id='147e4b32-34ab-4197-9f0c-831a51379318'></a>

12/4/25, 2:52 PM

<a id='ce0e2087-6381-48e6-8949-05887f241e3d'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='24f2cdb9-4daa-42fb-bcc1-a7b34ae04dc2'></a>

ARDUINODOCS

<a id='e3ad485d-106d-44ef-81c5-48021e04d1f2'></a>

# Description

Returns the module ID. When a module is manufactured, a unique SigFox ID is recorded in its permanent memory. It is very important to keep and store the ID tray carefully, as it will be useful to insure the tracability of these devices and to register them on a SigFox Network Operator (SNO).

<a id='f52da79d-d530-48fc-b207-6c108afbc2f7'></a>

## Syntax

```
1 SigFox.ID();
```

<a id='c464a330-8702-4834-9174-7e1616d0c19b'></a>

# Returns

A String that contains the 4 bytes ID.

<a id='5a307330-9166-41e2-bba7-abbebee617f0'></a>

SigFox.PAC()

<a id='956f202d-f02e-4d6d-afe8-1743ffe1dfce'></a>

# Description

Returns the module PAC. For each module, a PAC key is a secret key corresponding to the Sigfox ID. The PAC key will be useful to register a device on a SigFox Network Operator (SNO). As opposed to the SigFox ID, a PAC key is not transferable and must be re-generated if the module's ownership is changed.

<a id='6cfbdccd-1bdd-4768-8ca7-2ce52b6643de'></a>

## Syntax

```
1 SigFox.PAC();
```

<a id='3159d5f0-cc09-4a42-b55c-e13eb9c7fbe2'></a>

## Returns

A String that contains the 16 bytes PAC.

<a id='6cf1ee6f-78d0-4840-8583-b0c219d5178e'></a>

SigFox.reset()

<a id='fb3a319c-f181-41f5-b883-0b31b11b9aa3'></a>

Description

<a id='d4ca0e7c-1edc-4b43-a462-c77ceb2f0599'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='bd06cd9d-8c7d-48ee-8cb8-1a176541e55d'></a>

8/13

<!-- PAGE BREAK -->

<a id='34233a43-2d8b-47dc-b290-5cf69b41a23c'></a>

12/4/25, 2:52 PM

<a id='57c17a2c-5e27-40b5-97e8-82042eb39ba9'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='17a5ff23-48fc-4993-81ea-4462aa6a86b3'></a>

ARDUINODOCS

<a id='ada64e97-8758-40c8-a1f1-2bb34dbd6899'></a>

## Syntax

```javascript
1 SigFox.reset();
```

## Returns

None

<a id='83acb49a-4d81-4e7c-806d-bc9ce40cab5a'></a>

v SigFox.internalTemperature()

<a id='c1b0a111-b053-42a3-9140-1d0598db656a'></a>

# Description

Returns the internal temperature sensor
reading

<a id='6419a214-44d7-4d69-96c7-5ccb446d77c8'></a>

## Syntax

```
1 SigFox.internalTemperature();
```

<a id='cf34f13a-4207-460e-885c-658feed13bda'></a>

## Returns

a float representing the reading

<a id='99bc36e3-d8a0-4946-9ed8-93b9427466ea'></a>

SigFox.debug()

<a id='ec36dc45-f992-487d-9587-2267e24a69b5'></a>

# Description

Enable debugging. Enabling the debugging all the power saving features are disabled and the led indicated as signaling pin (LED_BUILTIN as default) is used during transmission and receive events.

<a id='04450ae0-84fc-4424-99d5-54d431d775a2'></a>

## Syntax

```
1 SigFox.debug();
```

<a id='62015238-c39e-4f0f-85c1-870687231fb0'></a>

Parameters

None

<a id='66f63e31-1d11-4957-85fc-6ff396eb08bc'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='e23da710-8761-4fa9-8993-34ae00c00805'></a>

9/13

<!-- PAGE BREAK -->

<a id='efb25340-1440-4edd-a352-0b726c975cbd'></a>

12/4/25, 2:52 PM

<a id='4acadd74-df12-40ac-acd4-de50c9350f44'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='d0235cc1-a4c5-417b-aaca-0be2fa857cc0'></a>

ARDUINODOCS

<a id='73f9e42d-e6ed-43b6-8f11-61aa9e9f9113'></a>

v SigFox.noDebug()

<a id='82f4b5fd-16d6-4644-9ff1-dd5edc341ff7'></a>

## Description

Disable debugging. Disabling the debugging
all the power saving features are enabled
and the led indicated as signaling pin
(LED_BUILTIN as default) is not used during
transmission and receive events.

<a id='dcb8747a-fc70-4aff-81d6-82c6b50165d7'></a>

## Syntax

```
1 SigFox.debug();
```

<a id='d4d30974-358f-42c1-b62e-df60ac51c14c'></a>

**Parameters**

None

<a id='04527f2f-3f76-4d72-8a27-1222b91001c6'></a>

SigFox.end()

<a id='321ac8e4-7dcd-4d4c-94f0-0d8a45a62bb9'></a>

## Description

De-initializes the Sigfox library and module

<a id='baa63c65-101d-4129-90e9-03803f4da3bd'></a>

**Syntax**

```
1 SigFox.end();
```

<a id='b0aaa832-0947-4630-af6d-b3729deff65b'></a>

Returns

None

<a id='09a750f3-5d6c-4da4-ac50-c4edbcdd7a25'></a>

Example

____________________________________________________________________________________________________

<a id='56763728-f07a-4938-8154-5db8d50f729e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='bb73e8ad-8e0c-4bee-8e7c-49e4b9174e64'></a>

10/13

<!-- PAGE BREAK -->

<a id='e5d47319-4b70-4bf2-a82b-83a92dc1ef3e'></a>

12/4/25, 2:52 PM

<a id='54a64f5a-6f16-4c35-8f1b-82661de29cae'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='ebd738fe-8e33-4b91-a761-3a7b66a2fd83'></a>

ARDUINODOCS

<a id='3dcf5904-90e2-46ff-b333-14b5c2e635cb'></a>

buffer (which holds 8 bytes). available()
inherits from the Stream utility class.

## Syntax

```
1 SigFox.available()
```

## Parameters

none

## Returns

the number of bytes available to read

<a id='a8944df7-f411-4db2-9352-eabeaddf1d14'></a>

read()

<a id='2e5b8daa-5aeb-4250-a500-a183a8ce3baf'></a>

# Description
Reads incoming SigFox data. read() inherits
from the Stream utility class.

<a id='6dacc00d-5242-45c5-8103-33a51cf7cd85'></a>

## Syntax

```
1 SigFox.read()
```

<a id='54f79565-83d2-400c-90fb-8b64762a1e73'></a>

**Parameters**

None

<a id='668d75d2-bfda-40dc-a4ff-12aefb3ba773'></a>

Returns
the first byte of incoming SigFox data
available (or -1 if no data is available) - int

<a id='2b867b2f-4656-4497-b3cc-658f24e13bc2'></a>

Example

[ ]

<a id='7663f6cb-e74c-4915-9e2c-942ae0636e14'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='97b4f15a-e612-4883-9580-a92a2f977869'></a>

12/13

<!-- PAGE BREAK -->

<a id='4016af1f-1b7d-4779-8097-85e92bbf1788'></a>

12/4/25, 2:52 PM

<a id='6cdc9ce7-7b8e-4fc5-a75a-0da7ef52a91c'></a>

Arduino SigFox for MKRFox1200 | Arduino Documentation

<a id='5ab6016a-36fd-4e4f-9092-12bf43669ac1'></a>

ARDUINODOCS

<a id='3a914906-e348-47c0-9f27-b29568f24286'></a>

```c
/*
 SigFox First Configuration

 This sketch demonstrates the
 Since the board is designed

 This example code is in the
*/

#include <SigFox.h>
#include <ArduinoLowPower.h>

void setup() {
 Serial.begin(9600);
 while (!Serial) {};

 // Uncomment this line and
 //if (!SigFox.begin(SPI1, 3))
 if (!SigFox.begin()) {
 Serial.println("Shield error");
 return;
 }
 // Enable debug led and disable
 // Comment this line when shipping
 SigFox.debug();

 String version = SigFox.SigfoxVersion();
 String ID = SigFox.ID();
```

<a id='e323c98a-36fd-4c8d-ad7d-c6e641f1883c'></a>

Was this article helpful?
---
option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='d063b06e-77d2-4497-8de4-5e772022df50'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='6eedbb39-805e-4812-b050-d8670fed9f33'></a>

 2025 Arduino

<a id='d611ad4c-ba35-4852-b2c6-79e288fc1451'></a>

Terms Of Service Privacy Policy Security Cookie Settings

<a id='9325da7f-a1fc-453d-98bd-2bf5f62c3f0d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-sigFox-library.html

<a id='c18562bc-84bf-4d44-8992-9073d073dcf8'></a>

13/13