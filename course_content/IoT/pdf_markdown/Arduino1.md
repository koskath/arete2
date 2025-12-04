<a id='cf5b4aed-64c8-4c0a-b915-97ed338a432d'></a>

12/4/25, 2:50 PM

<a id='80773bf3-ad5a-4916-94b7-7b0633c91517'></a>

ArduinoBLE | Arduino Documentation

<a id='17e3db92-7ccf-435b-bc44-3a036ddf6909'></a>

ARDUINODOCS

<a id='23481b9f-7bba-4809-8a0c-dd7b22f5e16c'></a>

Search on Docs /

<a id='e1474826-0de3-432e-b8ae-71366f58c78b'></a>

← Go Back

## Library

<a id='1b9294c8-c670-4548-ae28-18559dfd9d6b'></a>

Recents viewed

<a id='3d2bdb82-a363-4a3d-ab3b-5e75337b5258'></a>

ArduinoBLE

ArduinoMqttClient

WiFiNINA

Arduino SigFox for
MKRFox1200

autowp-mcp2515

Arduino_MKRENV

Arduino_MKRGPS

Arduino_APDS9960

Arduino_MKRIoTCarrier

<a id='f56ba910-8d1d-46b5-96e7-ab5d6e8e4c78'></a>

Home / Programming / Library / ArduinoBLE

<a id='63d7128d-4523-452e-9e58-4f314d4145b9'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='eaa0fd10-37c4-4043-a493-eb3a55680e19'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='27bb371f-2410-4352-b118-dd2ed078c401'></a>

GO TO REPOSITORY

<a id='5275f48a-4412-4179-9214-44e8649746d8'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='3ffef8de-6609-4375-81f1-3bee10edd3ce'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='67a44623-3bd4-4aba-af84-19088c13dc9c'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled
"Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low
Energy is optimized for low power use at low data rates, and was
designed to operate from simple lithium coin cell batteries.

<a id='3e7bc3d7-b55d-406e-a3d7-44185f31d502'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='62fa04cb-16a7-4054-a72d-e4f93440dd12'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='e4b5634c-fb09-4088-892d-96b6073cee0f'></a>

Help

<a id='b5b8f95f-a6c2-40e0-861b-dc21801eb187'></a>

1/10

<a id='d6dff80b-f353-41d6-a8ba-7ea7449b8845'></a>

ON THIS PAGE

* Usage/Examples
* Compatibility
* Releases
* BLE class
* BLEDevice Class
* BLEService Class
* BLECharacteristic
* BLEDescriptor Clas

<!-- PAGE BREAK -->

<a id='842d66f1-e2ff-475d-a1fb-25b04a7d1ec1'></a>

12/4/25, 2:50 PM

<a id='dd850597-231c-49e5-95d5-43761313b83e'></a>

ArduinoBLE | Arduino Documentation

<a id='ca0ef624-ee91-4629-aaaa-9781a370cabd'></a>

ARDUINODOCS

<a id='332dc4e7-0216-412f-9ab7-c2121626bdb4'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='74cd5f17-d30a-4c17-a8c9-ffccc6dffb09'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='96425fed-1e30-45f3-a3d4-2a7d4ca0cf6a'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='9b7293db-66f3-46a6-9b3f-488231ae07ce'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='0d9eddce-c34e-4924-bef0-4987d614453e'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='27784aa6-00b2-4c92-9826-4a3286a0a18c'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='8cdaad63-de4d-42a5-9dd3-fe6ae67e0766'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='0348b2b6-d180-4463-93b9-95973360a0e2'></a>

2/10

<!-- PAGE BREAK -->

<a id='e8ea5755-bd6b-441c-8e44-358091ebc84c'></a>

12/4/25, 2:50 PM

<a id='d1575c57-8c99-4c71-9d06-1667e92267a7'></a>

ArduinoBLE | Arduino Documentation

<a id='d253b197-2b57-49d5-80b8-13dc495e6b6e'></a>

ARDUINODOCS

<a id='3c96cf49-861c-46a6-91dd-384ef151392c'></a>

# Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='36017858-2115-45fc-991a-636174f8bb5f'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='f76086cc-fef9-4a19-91dc-a3ffe14a4794'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='035f55ab-0769-4f88-af52-f466ee6ca2c0'></a>

# Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint in designing services. Given this limit, you should consider how best to store data about your sensors and actuators most effectively for your application. The simplest design pattern is to store one sensor or actuator value per characteristic, in ASCII encoded values.

<a id='5101fdd9-259e-4394-b0a4-085492713595'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='13033691-549a-4395-8dae-aec0f33c6fb6'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='452a3d02-079c-438a-a985-23cd3e4b3a82'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='3d40da86-a611-421f-9a1d-a7ecf55e4993'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='c48b963d-ec17-407f-bf0a-d6f7e051f41f'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='a7032c21-aeef-4924-9072-bac5f46e67af'></a>

Read/write/notify/indicate

<a id='04385798-713e-4658-8561-8311dcb539f6'></a>

There are 4 things a central device can do with a characteristic:

<a id='86d6fc23-317b-4be3-be60-9c2688641f63'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='236ae1f2-3560-48d3-a061-387a5a40c033'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='904b5ef9-ab26-4f61-a0d9-6c3ee730f2c4'></a>

3/10

<a id='4b8da8e2-df9e-4b55-b0a8-c50b7bb1abbc'></a>



<!-- PAGE BREAK -->

<a id='423a8602-37ef-43a8-a3ee-33010d9aa794'></a>

12/4/25, 2:50 PM

<a id='bc449983-7c9a-49d3-83be-0d25497c887a'></a>

ArduinoBLE | Arduino Documentation

<a id='bc10dc56-4ee6-4b32-88c7-76e99447d901'></a>

ARDUINODOCS

<a id='636e23ad-d24f-4103-a344-02de0e95e23b'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='3f5a4088-45c1-4d73-9e98-6ecc1cbc7a3e'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='c55a57b6-90bb-4ff6-9a54-09db79035ecc'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='d341de5c-9f99-4062-9932-3c41f4e49d61'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='4d4f5007-9a4b-4958-853b-e6e376baf6a8'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='25ba315e-f1d7-437f-af56-e7ac4e610c35'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='daa042ec-e32f-46b0-ac2d-4454ccf12fc5'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='05e91d60-f331-47da-b896-5dca1dcfdddf'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='327bd7a2-7864-4075-9a3e-830c689389d8'></a>

BLE class BLEDevice Class BLEService Class

<a id='b4770c03-2e26-4888-8729-f6b658cdc0de'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='22eb070c-0c1f-4b7c-a885-57fd8ecb71d4'></a>

4/10

<!-- PAGE BREAK -->

<a id='4e303fbe-59a7-4f0d-a50c-d36486a2adba'></a>

12/4/25, 2:50 PM

<a id='4c7c2182-4876-4512-a508-6078de6d9e65'></a>

ArduinoBLE | Arduino Documentation

<a id='2c7caebe-c287-4c80-a385-7e945c5e2f3d'></a>

ARDUINODOCS

<a id='dd780b0a-e87c-4706-a87c-db0febbb0fd9'></a>

Used to describe a characteristic the board offers

<a id='20ca9c3f-b9ab-4fe9-8ef4-72a1dcbc6004'></a>

## BLEDescriptor()
Create a new Bluetooth® Low Energy descriptor.

### Syntax
```
1 BLEDescriptor (uuid, value, valueSize)
2 BLEDescriptor (uuid, stringValue)
```

### Parameters
*   **uuid**: 16-bit or 128-bit UUID in string format
*   **value**: byte array value
*   **valueSize**: size of byte array value
*   **stringValue**: value as a string

### Returns
New **BLEDescriptor** with the specified **UUID** and value

### Example
```
1 BLEDescriptor millisLabelDescriptor("2901", "mill:
```

<a id='9cd59ae7-7790-4b75-8185-eacd08532548'></a>

bleDescriptor.uuid()

<a id='c7f71419-6a1e-4439-8bd7-50d988547825'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='05a35227-6cee-4695-ad0d-ed079315327d'></a>

5/10

<!-- PAGE BREAK -->

<a id='333a5b80-1737-46a0-9445-1f3a32dd9509'></a>

12/4/25, 2:50 PM

<a id='4ab19179-4d8a-4275-90ed-4a033f11a02c'></a>

ArduinoBLE | Arduino Documentation

<a id='1e210d06-458e-4916-b821-fef76fa4070c'></a>

ARDUINODOCS

<a id='48030e5f-566b-4b64-b9ea-8a8c182cc8c4'></a>



<a id='cfa5c3db-23c5-4273-965b-025f6f9d1ca5'></a>

Query the UUID of the specified BLEDescriptor.

# Syntax

```
1 bleDescriptor.uuid()
```

<a id='99c9cf59-5454-4ee4-ad25-e49cd2444c76'></a>

**Parameters**

None

<a id='906fe3a1-a867-4ed1-a4fa-6ea11ef51b96'></a>

## Returns

**UUID** of the Bluetooth® Low Energy descriptor (as a String).

<a id='08ea4f7e-5dd4-42b5-a656-aaf356ca701c'></a>

# Example

```cpp
1 BLEDescriptor millisLabelDescriptor("2901", "mill:
2
3
4 Serial.print("millis label descriptor UUID = ");
5 Serial.println(millisLabelDescriptor.uuid());
```

<a id='d14d8934-aeba-48d4-af4b-7563dfa991b1'></a>

bleDescriptor.valueSize()
Query the value size of the specified BLEDescriptor.

<a id='617a86f4-2bc1-4262-a7c5-1a17f651b967'></a>

## Syntax

```
1 bleDescriptor.valueSize()
```

<a id='2cf82898-af76-4bdf-9415-01f098d014c7'></a>

**Parameters**

None

<a id='c3c25f9e-01e6-40d0-855b-5b54227675a2'></a>

## Returns

**Value size** (in bytes) of the Bluetooth® Low Energy descriptor.

<a id='1c232784-d86a-4de7-87b1-d93397d924bd'></a>

Example

________________________________________________________________________________

<a id='14cab879-2d02-40b0-b3fc-904c6952c3fa'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='c5f12234-ca08-4b11-99a5-be9fbfd6a19b'></a>

6/10

<!-- PAGE BREAK -->

<a id='e03cfa17-b036-4899-aa92-9fdea24412f7'></a>

12/4/25, 2:50 PM

<a id='757fbf44-1deb-4a2f-b932-84ee84a3a0a4'></a>

ArduinoBLE | Arduino Documentation

<a id='15866406-a89d-4a55-9a84-13a03c057b81'></a>

ARDUINODOCS

<a id='291f3108-c532-45d8-bc41-a95e8b60dde4'></a>

1 BLEDescriptor millisLabelDescriptor("2901", "mill:
2
3
4 Serial.print("millis label descriptor value size :
5 Serial.println(millisLabelDescriptor.valueSize())

<a id='666d8886-1a54-47fc-936b-a82d3dc1b664'></a>

✓ bleDescriptor.valueLength()

Query the length, in bytes, of the descriptor current value.

## Syntax

```
bleDescriptor.valueLength()
```

## Parameters

None

## Returns

Length of descriptor value in bytes.

## Example

```cpp
1 // read the descriptor value
2 descriptor.read();
3
4 // print out the value of the descriptor
5 Serial.print(", value 0x");
6 printData(descriptor.value(), descriptor.valuel
7 // ...
8
9 void printData(const unsigned char data[], int
10 for (int i = 0; i < length; i++) {
11 unsigned char b = data[i];
12
13 if (b < 16) {
14 Serial.print("0");
15 }
16
17 Serial.print(b, HEX);
18 }
19 }
```

<a id='36087d70-e1ce-40f3-8e25-27823a9fb809'></a>

bleDescriptor.value()

<a id='56d39cb6-9c95-49a9-81bc-af58106b7de6'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='7d27c6a4-9729-453a-8fd1-545e4fbbfeec'></a>

7/10

<!-- PAGE BREAK -->

<a id='fec4cfb6-83f4-4544-8656-ccdb72bbb4b5'></a>

12/4/25, 2:50 PM

<a id='baa5b6ea-c05c-4cdd-a9e1-64908b9e708d'></a>

ArduinoBLE | Arduino Documentation

<a id='50988b83-f7ca-4874-937d-078aaa22308e'></a>

ARDUINODOCS

<a id='cf610da1-5837-402a-a8da-efaf0dac7cea'></a>



<a id='385f4419-d609-4f90-b085-5d6a96148cb7'></a>

## Syntax

```
1 bleDescriptor.value()
```

<a id='a9df6cc9-4d12-42b7-925c-6fd3d30f18a6'></a>

Parameters

None

<a id='5d59a9d4-fe77-40bb-950a-4259caa18156'></a>

## Returns

Value byte array of the **BLE descriptor**.

<a id='6583effc-d50b-4aac-a45c-61e3b768b49b'></a>

Example

```
1 BLEDescriptor millisLabelDescriptor("2901", "mil]
2
3
4
5   int descriptorValueSize = millisLabelDescriptor
6   byte descriptorValue[descriptorValueSize];
7
8   for (int i = 0; i < descriptorValueSize; i++) {
9     descriptorValue[i] = millisLabelDescriptor.va
10  }
```

<a id='c64535d3-8d22-4ea4-80b3-553fd087137e'></a>

bleDescriptor.readValue()

Read the current value of the descriptor. If the descriptor is on a remote device, a read request will be sent.

### Syntax

```
1 bleDescriptor.readValue(buffer, length)
2 bleDescriptor.readValue(value)
```

<a id='933c8ad2-51a8-4f0a-924f-c4ade665a97d'></a>

## Parameters

**buffer**: byte array to read value into
**length**: size of buffer argument in bytes
**value**: variable to read value into (by reference)

<a id='26a80ff6-ab8a-435f-8f42-b68d259621b0'></a>

Returns

<a id='b83c384f-47dc-420d-9d7a-194a3e3a60d2'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='32301cda-e487-4b91-ae12-510a73e568f9'></a>

8/10

<!-- PAGE BREAK -->

<a id='44eaa3c0-be9a-49f6-a90d-c573ee8656e4'></a>

12/4/25, 2:50 PM

<a id='fc904177-8e7e-4d1a-9e57-9186314171cb'></a>

ArduinoBLE | Arduino Documentation

<a id='9e11a09f-0497-44c4-9b6d-1fdd133ea0d1'></a>

ARDUINODOCS

<a id='e0d8000f-554e-4718-9f39-94c884f77519'></a>



<a id='e38ccc0a-99ea-4f17-ac9c-f50cb6b18031'></a>

Example

```
1 byte value = 0;
2
3 // get the value, descriptor is 1 byte so use by
4 descriptor.readValue(value);
```

<a id='261cc339-f71a-47bd-84bc-bb517174bfcd'></a>

v bleDescriptor.read()
> Perform a read request for the descriptor.

<a id='3303034f-e96f-4716-a9fb-ae02e72c595c'></a>

## Syntax

```
1 bleDescriptor.read()
```

<a id='802a9eda-b2a9-464f-b0f5-31ada463fc68'></a>

**Parameters**

None

<a id='c9daaf86-b003-4285-8400-432bb751cffb'></a>

Returns

**true**, if successful,
**false** on failure

<a id='28ac1cfd-0802-49eb-8fdd-9ab872b64dd7'></a>

Example

```
1 if (descriptor.read()) {
2   Serial.println("descriptor value read");
3
4   // ...
5 } else {
6   Serial.println("error reading descriptor value");
7 }
```

<a id='3dac71ea-3cfe-49c7-90b2-38f9b51098e7'></a>

Was this article helpful?

---



See more related articles

<a id='fefaf83b-4cfd-4891-95e0-384dff27f383'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='2df2b138-cb11-48f4-8e3a-8e78aee32db2'></a>

9/10

<a id='9ae0c459-3fd3-4d62-8c19-2c23e1cedcea'></a>

Connect and Contribute

<!-- PAGE BREAK -->

<a id='d70543f9-600c-427c-a7be-2c2c109e02bb'></a>

12/4/25, 2:50 PM

<a id='17cf9d6e-730c-49e6-b1eb-de160592abf1'></a>

ArduinoBLE | Arduino Documentation

<a id='6b51ebc4-d780-4409-9f99-eb1cda012225'></a>

ARDUINODOCS

<a id='5c23e9a3-9b37-4c4e-907d-bcac7cba36a2'></a>



<a id='861376d1-804f-4bcf-83be-9562dfff96ac'></a>

Forum

<a id='6301c070-d9ce-4ee2-8147-f8c847f01528'></a>

Trademarks & Licensing

<a id='7245f70a-e407-4128-a9c7-35e6db73d378'></a>

© 2025 Arduino
Terms Of Service Privacy Policy Security Cookie Settings

<a id='60a024ac-2caa-4c0b-b7be-cf301ee6032a'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDescriptor-library.html

<a id='cda83a77-a3b5-4143-b533-212e00e63ba9'></a>

10/10