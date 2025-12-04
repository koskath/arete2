<a id='d139f0b1-282e-4631-8c98-eb8b9fb0ed3c'></a>

12/4/25, 2:50 PM

<a id='ad91adff-f367-4d70-9c45-54ee3a074d88'></a>

ArduinoBLE | Arduino Documentation

<a id='188fb5a4-b6ce-4eca-bea2-e5e96e421a3c'></a>

ARDUINODOCS

<a id='fd57bc26-814f-4633-93a4-eb1699a92e7b'></a>

Search on Docs /

<a id='aa337ae4-d7b1-4efe-a621-b66f7bcb1b17'></a>

← Go Back

## Library

<a id='f582dda6-9c05-4d82-a146-29e61199f285'></a>

Recents viewed

<a id='980bebc4-16b5-43cd-b606-f14155f7d567'></a>

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

<a id='7e65a48a-0740-45f0-a0d1-6de6ed07db75'></a>

Home / Programming / Library / ArduinoBLE

<a id='01915786-ddd6-4951-8f14-7abfa2e282e6'></a>

COMMUNICATION

# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>

https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='d31c79f3-c1cf-4150-b682-bad5bad8963c'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='18d0f3f4-032a-419d-9950-3bcc74dc109b'></a>

GO TO REPOSITORY

<a id='291c07b7-38cd-4fd2-9a47-5527fcdc0d24'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='b2b53c9f-15f4-4942-a0c1-62dead893760'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='a3a8d1b0-61e5-4b6e-bf38-125eaa4f6055'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled
"Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low
Energy is optimized for low power use at low data rates, and was
designed to operate from simple lithium coin cell batteries.

<a id='fc805117-9f4d-471b-b7be-d4b47b9d5093'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='1a7df304-7244-4a16-aab2-5a694fdaac0e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='6a26eaaf-3282-47ad-9ca2-786857858eae'></a>

Help

<a id='8a886a8c-2906-4236-87ca-a533e43bd183'></a>

1/22

<a id='1b9182d7-f752-4152-b0e2-bbd068a4fa74'></a>

ON THIS PAGE

*   Usage/Examples
*   Compatibility
*   Releases
*   BLE class
*   BLEDevice Class
*   BLEService Class
*   BLECharacteristic
*   BLEDescriptor Clas

<!-- PAGE BREAK -->

<a id='251a392d-76cd-465b-af25-36c076be1705'></a>

12/4/25, 2:50 PM

<a id='186ee290-750b-4461-9b8d-d25027c4afe4'></a>

ArduinoBLE | Arduino Documentation

<a id='5cf00db7-7d4c-4d2f-a917-032cd4564227'></a>

ARDUINODOCS

<a id='9c28e01f-4ac8-4596-b922-4722444ee5ed'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='a923d464-5d0f-4018-8916-5bfd2ea12f2c'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='04a006a0-7357-48a7-8cf8-65932d35f07f'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='c35e4e66-ef35-4b6c-bcac-364e82bcc554'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='365c1188-60d8-4073-8f0f-2da8503bd0d2'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='ca4f8806-83fc-4cdc-a131-131528dc85ce'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='b23af4b0-7719-4088-a4de-1ad7c0e665af'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='ad843ef3-61b4-456b-9c0a-c51d0e3958c0'></a>

2/22

<!-- PAGE BREAK -->

<a id='661f5b9c-31b8-48b4-90c9-f3f08ed325b2'></a>

12/4/25, 2:50 PM

<a id='d8d5dc2a-931f-4bc3-83c0-9ff22dee4d01'></a>

ArduinoBLE | Arduino Documentation

<a id='da491785-9a5e-4906-9ae8-5a89ebd4ce0e'></a>

ARDUINODOCS

<a id='85550516-d5b2-4e51-aabc-112b0c98a384'></a>

## Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='b4a6473a-bbf5-461f-9c60-657cf9a1e625'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='10ca3b93-a8de-4c10-b907-04dae4ce0ca6'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='55d2c7a2-7b71-4d70-865f-87f4e1512bda'></a>

# Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint in designing services. Given this limit, you should consider how best to store data about your sensors and actuators most effectively for your application. The simplest design pattern is to store one sensor or actuator value per characteristic, in ASCII encoded values.

<a id='28fd47ca-15db-4e80-b364-efea37bf181a'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='c6c0e920-a6e8-4cb2-b24b-5cdf5c0537ae'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='37dc68e8-81f0-418d-af1a-9dee8696cefa'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='4114953c-775d-47ff-a1ad-21ba4e965513'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='6d714b9f-7007-4e31-81aa-0fb379a0ce44'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='d62da9ef-2149-4646-9c05-a8f68f332ab8'></a>

Read/write/notify/indicate

<a id='190cf473-2664-4dd2-aad1-0d767c576dd8'></a>

There are 4 things a central device can do with a characteristic:

<a id='9a806fea-68de-4941-90c9-76b440038d38'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='c328c40e-a673-47fe-86ff-f2e66464dd2a'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='6595c60e-780f-4fde-a85d-beeea28e2614'></a>

3/22

<a id='7dc01968-abd0-4704-a625-479c5c7ed72c'></a>



<!-- PAGE BREAK -->

<a id='8a071277-ac60-4971-bde1-8f88744c68d1'></a>

12/4/25, 2:50 PM

<a id='ced33241-7deb-4bd2-9663-8a17aaf0e692'></a>

ArduinoBLE | Arduino Documentation

<a id='3b716c8f-7989-46f2-8568-efc88e969bdf'></a>

ARDUINODOCS

<a id='13984431-77ab-4655-85fe-87d6f632f921'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='23302c5c-d250-467d-87a2-c6ed975d21dc'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='b59680aa-7011-43eb-b835-007819742a91'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='15ea87f3-5455-470f-b301-281ad3c9c770'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='bb979a10-3fe6-4171-a023-0f874b7ffd06'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='4807a0ba-ff58-4fee-bcf4-7202306bf5e2'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='eb4c6a49-f33a-47d9-b26c-ad0885a70a0c'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='0404b35b-153b-4b43-ad47-eb7a539a2879'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='0be6187f-e924-497a-914c-de8183d638f5'></a>

BLE class BLEDevice Class BLEService Class

<a id='905d083f-e554-44eb-b8d8-8180dca5b4a7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='703a63af-19b9-4fe7-9ae2-48bf69028088'></a>

4/22

<!-- PAGE BREAK -->

<a id='e92bed01-0530-4d76-9700-a3c5e17b3f06'></a>

12/4/25, 2:50 PM

<a id='e6c82615-3222-41ee-b88c-14c740ec5291'></a>

ArduinoBLE | Arduino Documentation

<a id='d3f216bc-2923-452a-a3cb-72d090f1dda0'></a>

ARDUINODOCS

<a id='569395a0-9861-408f-92f7-8b10fec6ac15'></a>

Used to enable the characteristics board offers in a service or interact with
characteristics a remote board provides.

<a id='3ce5a001-148c-4d24-9bf7-6cd2e422f519'></a>

BLECharacteristic()

Create a new Bluetooth® Low Energy characteristic.

## Syntax

```
BLECharacteristic(uuid, properties, valueSize)
BLECharacteristic(uuid, properties, valueSize, fixedLength)
BLECharacteristic(uuid, properties, stringValue)

BLEBoolCharacteristic(uuid, properties)
BLEBooleanCharacteristic(uuid, properties)
BLECharCharacteristic(uuid, properties)
BLEUnsignedCharCharacteristic(uuid, properties)
BLEByteCharacteristic(uuid, properties)
BLEShortCharacteristic(uuid, properties)
BLEUnsignedShortCharacteristic(uuid, properties)
BLEWordCharacteristic(uuid, properties)
BLEIntCharacteristic(uuid, properties)
BLEUnsignedIntCharacteristic(uuid, properties)
BLELongCharacteristic(uuid, properties)
BLEUnsignedLongCharacteristic(uuid, properties)
BLEFloatCharacteristic(uuid, properties)
BLEDoubleCharacteristic(uuid, properties)
```

<a id='bc32a0c8-9cfe-47bf-9aea-75ab427ee719'></a>

# Parameters
uuid: 16-bit or 128-bit UUID in **String** format
properties: mask of the properties (BLEBroadcast, BLERead,
BLEWriteWithoutResponse, BLEWrite, BLENotify, BLEIndicate)
valueSize: (maximum) size of characteristic value
fixedLength: if true, size of characteristic value is fixed
stringValue: value as a string

<a id='0ba8e4af-fcc6-48ce-b46d-bc2f9e46558f'></a>

## Returns

New **BLECharacteristic** with the specified **UUID** and value

<a id='776217be-ed82-48ae-aa4c-ba589e204ac8'></a>

Example

```
1 // Bluetooth® Low Energy Battery Level Characteristic
2 BLEUnsignedCharCharacteristic batteryLevelChar("2A19",
3 BLERead | BLENotify); // remote clients will be able to read and subscribe to notifications
```

<a id='f97e8e73-9171-4c04-a2a1-5bd6ded267ea'></a>

bleCharacteristic.uuid()

<a id='b16e4bb5-f17e-4454-9be5-7fa2060aaae7'></a>

Query the UUID of the specified BLECharacteristic

<a id='fb4aecdc-3732-4c9c-9261-c0085b7f7060'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='95b009d5-92a4-4a36-9c78-4488f96ee1d2'></a>

5/22

<!-- PAGE BREAK -->

<a id='110a2998-a832-4afd-b39e-ba4034753d2f'></a>

12/4/25, 2:50 PM

<a id='f14fb5cc-88bf-4340-bdfd-b93aeb0fc308'></a>

ArduinoBLE | Arduino Documentation

<a id='1a459f04-a0d0-46a6-988b-79da2cc9e4dd'></a>

ARDUINODOCS

<a id='c5b788c8-5436-4527-a980-f837f81cd095'></a>



<a id='afe30df5-5a00-496e-b379-15e9bdabcac3'></a>

## Syntax

```
1 bleCharacteristic.uuid()
```

<a id='b54a55f3-3cec-402d-b60c-974213bc8a5f'></a>

Parameters

None

<a id='f9f80d5b-1feb-4cf5-8813-8785fb052230'></a>

**Returns**

**UUID** of the Bluetooth® Low Energy service as a **String**.

<a id='0bd4fcc7-cc04-4ecb-a295-c69422a635ae'></a>

Example

```
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B100
3
4
5 Serial.print("Switch characteristic UUID = ");
6 Serial.println(switchCharacteristic.uuid());
```

<a id='ae5d2d7a-b1f6-414e-bb3e-0ec9e530e1b7'></a>

bleCharacteristic.properties()

Query the property mask of the specified BLECharacteristic.

<a id='0ed1e0f6-c8ba-450d-bbce-5318b18f232a'></a>

## Syntax

```
1 bleCharacteristic.properties()
```

<a id='928e0dfd-6644-4eec-9946-f9c1e7be1c22'></a>

Parameters

None

<a id='33293a11-06cf-4c5f-ae3d-dd92f1a8f648'></a>

## Returns

Properties of the characteristic masked (BLEBroadcast, BLERead, BLEWriteWithoutResponse, BLEWrite, BLENotify, BLEIndicate)

<a id='9d903df9-cdbe-43ca-9ca5-4fb5439cb8f4'></a>

## Example

[Empty input field]

<a id='2a3ab0e3-f349-4580-bc0e-e7f1fd2932fb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='14cd2798-e30b-4efb-88b0-1ae348bb0c9d'></a>

6/22

<!-- PAGE BREAK -->

<a id='3f4e545a-61b3-4158-a29b-ba6284391851'></a>

12/4/25, 2:50 PM

<a id='2d5422a2-5acc-4a46-a188-98164fc3d4f2'></a>

ArduinoBLE | Arduino Documentation

<a id='b0fa45eb-c136-4b46-8af8-9882dec415d1'></a>

ARDUINODOCS

<a id='bc4b2f51-ba9f-4f57-8203-ceb2f019c6da'></a>

```c
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B16
3
4
5 byte properties = switchCharacteristic.properties;
6
7 if (properties & BLERead) {
8   // characteristic is readable ...
9 }
10
11 if (properties & (BLEWrite | BLEWriteWithoutResp)) {
12   // characteristic is writable ...
13 }
```

<a id='2473d987-06f9-4ef8-9623-3be1185729c1'></a>

bleCharacteristic.valueSize()

> Query the maximum value size of the specified BLECharacteristic.

<a id='d58a119f-0a4d-4727-86cc-d1f5e612aece'></a>

## Syntax

```
1 bleCharacteristic.valueSize()
```

<a id='e059208e-184b-4a32-a892-60a3d4405562'></a>

**Parameters**

None

<a id='55959da7-dd78-46a4-a972-996b81bed2dd'></a>

## Returns
The **maximum value** size of the characteristic (in bytes)

<a id='9f64f50f-5f71-48b9-8c50-e8949a29b4d6'></a>

Example

```
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B106
3
4
5
6 Serial.print("value size = ");
7 Serial.println(switchCharacteristic.valueSize());
```

<a id='ad95b19b-3345-4f39-8282-5437df71c472'></a>

bleCharacteristic.value()
Query the current value of the specified BLECharacteristic.

<a id='c4654af1-fc4b-402b-b5bb-caf54a31da52'></a>

Syntax

<a id='7c9d992b-7f1e-49da-a7ad-a43d86ea5bd4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='7e425225-b8c2-4a86-84ab-2106152ea0c5'></a>

7/22

<!-- PAGE BREAK -->

<a id='22bfbe2c-bc33-456c-816e-28dc9792c86a'></a>

12/4/25, 2:50 PM

<a id='aadee55d-2319-4a4b-b38b-b75edb1c16eb'></a>

ArduinoBLE | Arduino Documentation

<a id='023fc917-d517-43c3-b8a8-b1826b6a7cd2'></a>

ARDUINODOCS

<a id='53e05cc5-48c2-4779-ad5d-42a40df0d44a'></a>



<a id='af79c391-3926-4d41-bd14-83387b9439fb'></a>

1 bleCharacteristic.value()

<a id='fbb5fb32-adee-42be-924b-b7eec55fbce3'></a>

Parameters

None

<a id='115cecd0-65db-4a56-bece-878b8fa0a0fe'></a>

## Returns

The **current value** of the characteristic, value type depends on the constructor used

<a id='8bf21a08-1bbb-498e-8258-bb4a25c019dc'></a>

Example

```
1 // Bluetooth® Low Energy LED Switch Characteristic
2 BLEByteCharacteristic switchCharacteristic("19B16
3 
4 
5 
6 if (switchCharacteristic.value()) { // any value
7   Serial.println("LED on");
8   digitalWrite(ledPin, HIGH); // will turn the
9 } else { // a 0 value
10   Serial.println(F("LED off"));
11   digitalWrite(ledPin, LOW); // will turn the
12 }
```

<a id='a567479c-ba37-4267-b534-f92673b44148'></a>

### bleCharacteristic.valueLength()
Query the current value size of the specified BLECharacteristic.

### Syntax

```
1 bleCharacteristic.valueLength()
```

<a id='029ccaf8-d329-40e9-aec7-b99d31399803'></a>

Parameters

None

<a id='7f51aefe-0626-4015-8547-75c51c1d3152'></a>

Returns

The **current value** size of the characteristic (in bytes)

<a id='c8ff9747-2979-450c-b766-d1388af5830c'></a>

Example

________________________________________________________________________________

<a id='c56f1e63-4f17-49d2-a16a-2c7c23918486'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='2cfdd82f-6310-4984-bf0e-0f93e920338d'></a>

8/22

<!-- PAGE BREAK -->

<a id='ebb7658c-68dc-4bfb-b719-41fd98492492'></a>

12/4/25, 2:50 PM

<a id='92e095bd-ecad-4fe1-9686-f3d0781eb7ba'></a>

ArduinoBLE | Arduino Documentation

<a id='fffc93e0-5217-4a62-bb14-6ade2207508c'></a>

ARDUINODOCS

<a id='e7721738-7176-47a9-90cf-be4d7afbdc03'></a>

```
// Bluetooth® Low Energy LED Switch Characteristic
BLEByteCharacteristic switchCharacteristic("19B100



Serial.print("value length = ");
Serial.println(switchCharacteristic.valueLength())
```

<a id='7559374e-4792-494f-9cd7-c5e9509f982b'></a>

✓ bleCharacteristic.readValue()
Read the current value of the characteristic. If the characteristic is on a remote device, a read request will be sent.

<a id='2cc9c132-da4c-4d84-973a-6ba9e59d7d79'></a>

## Syntax

```
1 bleCharacteristic.readValue(buffer, length)
2 bleCharacteristic.readValue(value)
```

<a id='23674157-b50a-468c-b668-d33905c0a418'></a>

## Parameters

**buffer**: byte array to read value into length: size of buffer
argument in bytes

**value**: variable to read value into (by reference)

<a id='5caff8db-7c65-4541-b512-a46d0111b7fb'></a>

Returns

Number of bytes read

<a id='b2ce3f63-5d38-4a1e-98ce-dfa19021f6b9'></a>

Example

```
while (peripheral.connected()) {
  // while the peripheral is connected

  // check if the value of the simple key chara
  if (simpleKeyCharacteristic.valueUpdated()) {
    // yes, get the value, characteristic is 1
    byte value = 0;
    simpleKeyCharacteristic.readValue(value);

    if (value & 0x01) {
      // first bit corresponds to the right but
      Serial.println("Right button pressed");
    }

    if (value & 0x02) {
      // second bit corresponds to the left but
      Serial.println("Left button pressed");
    }
  }
}
```

<a id='f5896af8-7d7e-4576-a27b-44c41bf35872'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='c90ac188-c440-474e-add9-d274e3d2814b'></a>

9/22

<!-- PAGE BREAK -->

<a id='9c5cdcc0-2de2-4357-8b44-55e3f88e6856'></a>

12/4/25, 2:50 PM

<a id='fae54cd6-5e0a-4293-a929-a7050a892b7c'></a>

ArduinoBLE | Arduino Documentation

<a id='16e8e289-57b5-47a8-b590-18217f3aa9ec'></a>

ARDUINODOCS

<a id='89d23e78-3700-4255-96f3-89e8c77bbaff'></a>



<a id='6cecd41d-b740-40de-aa7a-af15ceb1a9f8'></a>

bleCharacteristic.writeValue()

Write the value of the characteristic. If the characteristic is on a remote device, a write request or command will be sent.

## Syntax
```
bleCharacteristic.writeValue(buffer, length)
bleCharacteristic.writeValue(value)
```

## Parameters

buffer: byte array to write value with
length: number of bytes of the buffer argument to write
value: value to write

## Returns

1 on success,
0 on failure

## Example
```c
// read the button pin
int buttonState = digitalRead(buttonPin);

if (oldButtonState != buttonState) {
  // button changed
  oldButtonState = buttonState;

  if (buttonState) {
    Serial.println("button pressed");

    // button is pressed, write 0x01 to turn
    ledCharacteristic.writeValue((byte)0x01);
  } else {
    Serial.println("button released");

    // button is released, write 0x00 to turn
    ledCharacteristic.writeValue((byte)0x00);
  }
}
```

<a id='6d38fc2c-6059-45dd-a775-ac2fe31bbc51'></a>

bleCharacteristic.setEventHandler()
Set the event handler (callback) function that will be called when the specified event occurs.

<a id='c2de5d1b-8f52-4c58-91be-73de8f71cba6'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='5191d198-0300-419f-84d5-1a6896375c76'></a>

10/22

<!-- PAGE BREAK -->

<a id='5cf9b423-f9d6-4b48-a259-ad88c19b2f56'></a>

12/4/25, 2:50 PM

<a id='2e83c46b-f8cf-4694-809e-986d6244a4e1'></a>

ArduinoBLE | Arduino Documentation

<a id='b9542587-9903-47c4-a24d-e08dac61374d'></a>

ARDUINODOCS

<a id='4cb9f7ce-c5c8-4332-8b5d-cfa134504fa7'></a>

## Syntax

```
1 bleCharacteristic.setEventHandler(eventType, call
```

<a id='4f515a37-acc3-4b3d-a3f2-8eadd30e48ac'></a>

# Parameters

**eventType**: event type (BLESubscribed, BLEUnsubscribed,
BLERead, BLEWritten)
**callback**: function to call when the event occurs

<a id='19372c32-c3d8-4b4f-a126-1eebb3d90c4f'></a>

Returns

Nothing

<a id='15b9c77c-48d2-46cc-b32c-54ff6b643266'></a>

Example

```c
// create switch characteristic and allow remote
BLEByteCharacteristic switchCharacteristic("19B16");



// assign event handlers for characteristic
switchCharacteristic.setEventHandler(BLEWritter);



void switchCharacteristicWritten(BLEDevice central) {
  // central wrote new value to characteristic, it
  Serial.print("Characteristic event, written: ");

  if (switchCharacteristic.value()) {
    Serial.println("LED on");
    digitalWrite(ledPin, HIGH);
  } else {
    Serial.println("LED off");
    digitalWrite(ledPin, LOW);
  }
}
```

<a id='a146d44e-7f12-4d83-aead-39d51c331919'></a>

- bleCharacteristic.broadcast()
  > Broadcast the characteristics value as service data when advertising.

<a id='a870b002-3a93-48fb-b2b4-5eedd0108464'></a>

# Syntax
---
1. h1>Characteristic broadcast()

<a id='b134fd17-ccb0-4962-a4b0-5945b94a759b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='45fc5ba8-bb34-4ddc-adcd-6cd6e73d99de'></a>

11/22

<!-- PAGE BREAK -->

<a id='fb0cb680-aafe-4473-9fc3-b6426e7b3b8e'></a>

12/4/25, 2:50 PM

<a id='95c0c251-fdb7-4c62-b8b7-3de5e0de4fd4'></a>

ArduinoBLE | Arduino Documentation

<a id='5d7dee4c-28b0-4c2e-b4fa-96d148a804d7'></a>

ARDUINODOCS

<a id='af2223b6-f1c2-46ea-a907-bd5c7baf6667'></a>

**Parameters**

None

**Returns**

1 on success,
0 on failure

<a id='0cac5827-a374-40a6-be23-7f511907b86d'></a>

Example

```
1 // create button characteristic and allow remote (
2 BLEByteCharacteristic buttonCharacteristic("19B100
3 
4 
5 
6 buttonCharacteristic.broadcast();
```

<a id='e3e5e884-f2a0-425a-9318-279776baac77'></a>

- bleCharacteristic.written()
  Query if the characteristic value has been written by another
  Bluetooth® Low Energy device.

<a id='6c974819-f85b-4a8f-9479-5fcd1ec0b73c'></a>

## Syntax

```
1 bleCharacteristic.written()
```

<a id='a4097ce8-b5a9-403d-b9b4-ac4606810a6a'></a>

Parameters

None

<a id='342fd312-6402-49ea-ab63-cb2099a02324'></a>

## Returns

**true** if the characteristic value has been written by another Bluetooth® Low Energy device,

**false** otherwise

<a id='1cf58b9f-bca4-4a40-a013-d6b63c6abf93'></a>

Example

___

<a id='db889de1-4e83-477d-8a13-ec3f42330dbe'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='4090c8ca-78c1-4a85-971f-f1f4a72f756e'></a>

12/22

<!-- PAGE BREAK -->

<a id='9d873977-5cf9-41f2-9bd7-d4bf543df5e0'></a>

12/4/25, 2:50 PM

<a id='63e0a693-b14f-4898-a497-6e25b0df2835'></a>

ArduinoBLE | Arduino Documentation

<a id='1d66b59c-d665-45f4-88aa-e3e7f53d645d'></a>

ARDUINODOCS

<a id='bf93bcc4-2853-4c62-9557-3fc6588ad524'></a>

```c
// Bluetooth® Low Energy LED Switch Characteristic
BLEByteCharacteristic switchCharacteristic("19B

// listen for Bluetooth® Low Energy peripheral:
BLEDevice central = BLE.central();

// if a central is connected to peripheral:
if (central) {
  Serial.print("Connected to central: ");
  // print the central's MAC address:
  Serial.println(central.address());
}

// while the central is still connected to |
while (central.connected()) {
  // if the remote device wrote to the characteristic
  // use the value to control the LED:
  if (switchCharacteristic.written()) {
    if (switchCharacteristic.value()) {
      Serial.println("LED on");
      digitalWrite(ledPin, HIGH);
    } else {
      Serial.println(F("LED off"));
      digitalWrite(ledPin, LOW);
    }
  }
}
```

<a id='6472e130-383e-479c-81d5-9bfb451fc7c4'></a>

bleCharacteristic.subscribed()

Query if the characteristic has been subscribed to by another Bluetooth® Low Energy device.

## Syntax

```
1 bleCharacteristic.subscribed()
```

<a id='9d9fa796-d8ea-45ae-ac84-31db756e2927'></a>

Parameters

None

<a id='b5a3860e-10b0-4942-91b0-084e0a843e2e'></a>

## Returns

**true** if the characteristic value has been subscribed to by another Bluetooth® Low Energy device,
**false** otherwise

<a id='b55a7116-d9de-40c4-84d5-9dd904ce00fc'></a>

Example

---

<a id='2c83e347-005a-420b-bb74-5f6369bfde50'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='56e37bb4-95da-480a-a037-978d6210ecf0'></a>

13/22

<!-- PAGE BREAK -->

<a id='02768c68-21f0-4fea-ba1d-1037a5164984'></a>

12/4/25, 2:50 PM

<a id='b4d28ce9-78dc-4dad-858c-6a89a362b83a'></a>

ArduinoBLE | Arduino Documentation

<a id='70d23533-4cee-4087-806d-16b9e5996b2c'></a>

ARDUINODOCS

<a id='548e4d05-0eb2-430d-8a5b-8e83ad311f0a'></a>

// Bluetooth® Low Energy Battery Level Characteristic
BLEUnsignedCharCharacteristic batteryLevelChar("2
BLERead | BLENotify); // remote clients will





if (batteryLevelChar.subscribed()) {
  // set a new value , that will be pushed to
  batteryLevelChar.writeValue(0xab);
}

<a id='3960b986-420e-4da7-8f5f-4ce079489697'></a>

bleCharacteristic.addDescriptor()
Add a BLEDescriptor to the characteristic.

## Syntax
```
bleCharacteristic.addDescriptor(bleDescriptor)
```

## Parameters
bleDescriptor: descriptor to add to the characteristic

## Returns
Nothing

## Example
```
// Bluetooth® Low Energy Battery Level Characteristic
BLEUnsignedCharCharacteristic batteryLevelChar("2
BLERead | BLENotify); // remote clients will
BLEDescriptor batteryLevelDescriptor("2901", "mi]
batteryLevelChar.addDescriptor(batteryLevelDesc
```

<a id='7a4a5c13-f797-4838-a4a5-d9dfcf6e9868'></a>

bleCharacteristic.descriptorCount()

Query the number of Bluetooth® Low Energy descriptors
discovered for the characteristic

<a id='aed51ade-3960-41f0-a4c8-8f96979c5dfb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='17e8181c-e04b-416b-a684-5b2fef72a33b'></a>

14/22

<!-- PAGE BREAK -->

<a id='82f166e4-af8d-45e8-8f37-3cdd51a22efe'></a>

12/4/25, 2:50 PM

<a id='2714c5e2-5d5c-4d0e-8afe-0c14f926b6ca'></a>

ArduinoBLE | Arduino Documentation

<a id='05d84afc-c457-4d93-a2b5-0f7409d63816'></a>

ARDUINODOCS

<a id='9a7f992e-e2be-456a-9bd4-7d592cdee56f'></a>



<a id='bcd4ff74-9205-4c0f-91e5-c126e0d52ac1'></a>

## Syntax

```
1 bleCharacteristic.descriptorCount()
```

<a id='cb0ab12e-8566-4e80-9f40-0158d77f83bf'></a>

**Parameters**

None

<a id='3db11c92-756f-4a32-931c-2af1e8c1d954'></a>

## Returns

The **number of Bluetooth® Low Energy descriptors** discovered for the characteristic

<a id='a2bbedf0-328d-45fb-b90d-6f9c2c8ee48e'></a>

Example
```java
1 // loop the descriptors of the characteristic and
2 for (int i = 0; i < characteristic.descriptorCo
3     BLEDescriptor descriptor = characteristic.desc
4 
5     // ...
6 }
```

<a id='5fdb25b4-6bde-466e-ad78-e8ae842f528b'></a>

bleCharacteristic.hasDescriptor()
Check if a characteristic has a particular descriptor.

<a id='05353db3-19ff-44be-8569-279a402b8ccb'></a>

## Syntax

```
1 bleCharacteristic.hasDescriptor(uuid)
2 bleCharacteristic.hasDescriptor(uuid, index)
```

<a id='795eef76-bf4e-4994-926e-7f866f487e34'></a>

# Parameters

**index**: index of descriptor
**uuid**: uuid (as a String)

<a id='768ea601-8edd-47e4-8a42-42ae906d35a5'></a>

## Returns

**true**, if the characteristic has a matching descriptor,
otherwise **false**.

<a id='44a662b0-14f9-4e58-9636-c4a46b58f91b'></a>

Example

<a id='93026086-4a6b-4a7f-81f7-98319700c2d4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='e4647313-ede8-4ae3-a78d-f75bdccd5db0'></a>

15/22

<!-- PAGE BREAK -->

<a id='b1f94f9f-164b-4f8d-85ec-adf578d4672c'></a>

12/4/25, 2:50 PM

<a id='a6f6afe4-ea6c-404e-a595-22ad819d70c8'></a>

ArduinoBLE | Arduino Documentation

<a id='6e297ece-2f88-4fd9-8339-c6be7a480df3'></a>

ARDUINODOCS

<a id='1be42e9c-0b54-490a-b2b8-8fde7dd0e75e'></a>



<a id='8d1ebbba-7e52-4eb5-8fb8-b3f7089a6fa7'></a>

if (characteristic.hasDescriptor("2901")) {
    Serial.println("characteristic has descriptor");
}

<a id='2dac57a2-f835-40f6-a750-d73e071e8072'></a>

⌵ bleCharacteristic.descriptor()
Get a BLEDescriptor that represents a characteristics Bluetooth® Low Energy descriptor.

<a id='43413fb2-54cf-47e9-9cd6-bc5ceaaf37b5'></a>

## Syntax

```
1 bleCharacteristic.descriptor(index)
2 bleCharacteristic.descriptor(uuid)
3 bleCharacteristic.descriptor(uuid, index)
```

<a id='1c3b8b60-9ee7-485b-b840-8af969870346'></a>

Parameters

index: index of descriptor

uuid: uuid (as a String)

<a id='1db22ed4-32fc-4c43-84a9-cbfd4a0c4f41'></a>

## Returns

BLEDescriptor that represents a characteristics Bluetooth® Low Energy descriptor

<a id='5381120c-b65f-4223-9382-57e951ee3806'></a>

Example
```
1 if (characteristic.hasDescriptor("2901")) {
2   Serial.println("characteristic has descriptior
3 }
```

<a id='74766711-14aa-4227-af8b-82dc3aa9b325'></a>

bleCharacteristic.canRead()
Query if a Bluetooth® Low Energy characteristic is readable.

## Syntax

```
1 bleCharacteristic.canRead()
```

<a id='3f7c3ece-2596-4768-8202-8fad13910833'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='c0477f86-28b0-4d0d-9b4b-12974fe59961'></a>

16/22

<!-- PAGE BREAK -->

<a id='bc22fb37-e4e9-4ec0-963b-9a458cfdddf8'></a>

12/4/25, 2:50 PM

<a id='9219a5b1-a12f-4eb5-a80a-46babc430e36'></a>

ArduinoBLE | Arduino Documentation

<a id='7b12955a-303f-4d76-b193-1c5733a859fd'></a>

ARDUINODOCS

<a id='93b363d4-6f8e-48a5-895a-8f0672b7d15d'></a>

None

**Returns**

**true**, if characteristic is readable,
**false** otherwise

<a id='f833bd7d-d880-4e42-9634-7fcccad6be01'></a>

## Example

```
1 if (characteristic.canRead("2901")) {
2   Serial.println("characteristic is readable");
3 }
```

<a id='1b96c9d9-8b03-4572-b581-f8c1094c32ed'></a>

read

Perform a read request for the characteristic.

<a id='c149a355-958e-4a76-b1cd-f673307f005f'></a>

## Syntax

```
1 bleCharacteristic.read()
```

<a id='0c7fa313-3d5d-4f95-9586-cc40bbcdc2bb'></a>

Parameters

None

<a id='213d979e-6021-46ab-b927-e4e9c774ec54'></a>

## Returns

**true**, if successful,

**false** on failure

<a id='bd9da21c-eb95-4510-a38c-9beabf8f8c7b'></a>

# Example

```
1 if (characteristic.read()) {
2   Serial.println("characteristic value read");
3 
4   // ...
5 } else {
6   Serial.println("error reading characteristic");
7 }
```

<a id='ab647dff-6378-461d-8e3b-05dc97ffd425'></a>

v bleCharacteristic.canWrite()

<a id='bf627398-61f1-436f-82e7-fa74b21907de'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='a96522d2-dc81-4352-887c-94cd77eee6c8'></a>

17/22

<!-- PAGE BREAK -->

<a id='116c1818-e691-4c34-8c99-b6dae3a089f9'></a>

12/4/25, 2:50 PM

<a id='70cd7a66-31c7-4050-ae07-4a7b1be77bcf'></a>

ArduinoBLE | Arduino Documentation

<a id='038a30b3-08b7-45d0-8f57-14eff5d590af'></a>

ARDUINODOCS

<a id='ca24e147-fcb1-4f54-b62a-bebf999fa905'></a>



<a id='5f35b3ba-e98e-4278-adbe-df0195e95f3e'></a>

Query if a Bluetooth® Low Energy characteristic is writable.

### Syntax

```
1 bleCharacteristic.canWrite()
```

<a id='3a7a3b0a-51fe-41e2-8cdf-3e1459633fa8'></a>

## Parameters

None

<a id='57f1b3fb-e893-4af5-967f-078b2aa89f0e'></a>

## Returns

**true**, if characteristic is writable,
**false** otherwise

<a id='15a7a4ab-6fed-4bc2-ad70-25d8aef81990'></a>

## Example

```
1 if (characteristic.canWrite()) {
2    Serial.println("characteristic is writable");
3 }
```

<a id='60116221-423d-469e-a4bb-4e536d78bd13'></a>

v bleCharacteristic.canSubscribe()
Query if a Bluetooth® Low Energy characteristic is subscribable.

<a id='3fdd724b-a939-4885-b371-fc7cb8bcbb5d'></a>

## Syntax

```
1 bleCharacteristic.canSubscribe()
```

<a id='0c440346-f9ca-4af7-a876-b1b39d14c206'></a>

Parameters

None

<a id='487662d0-0873-416e-9eeb-32620403d6fe'></a>

## Returns

**true**, if characteristic is subscribable,
**false** otherwise

<a id='eba40556-040a-4a4e-8b73-6a7bde0d2800'></a>

Example

<a id='a2a91539-8890-477c-abe6-702e993e3042'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='a242979c-743a-41ad-9d5a-bab11b1d8738'></a>

18/22

<!-- PAGE BREAK -->

<a id='ebf27ca2-1b14-4723-aa9a-90c606c47cc1'></a>

12/4/25, 2:50 PM

<a id='befab821-f810-4a14-ac20-f5085f374aa1'></a>

ArduinoBLE | Arduino Documentation

<a id='18c81feb-906c-4354-ac48-6bf29ed9ab6a'></a>

ARDUINODOCS

<a id='5b8c04e1-ab46-4de0-a111-7b7f117161d6'></a>



<a id='87e56706-a390-425d-8ede-b519838a1dbd'></a>

```
1 if (characteristic.canSubscribe()) {
2   Serial.println("characteristic is subscribable");
3 }
```

<a id='db89acf2-aed3-4f77-97e5-744106fc976b'></a>

> bleCharacteristic.subscribe()
> Subscribe to a Bluetooth® Low Energy characteristics notification or indications.

<a id='5edd635a-4921-431b-b5be-25f9dfce5b4f'></a>

**Syntax**

```
1 bleCharacteristic.subscribe()
```

<a id='81c4c12d-104f-4a56-b0da-a62310cc562f'></a>

## Parameters

None

<a id='f4a91d6c-0e81-4edb-a162-4d35ceb31820'></a>

**Returns**

**true**, on success,
**false** on failure

<a id='e43eb9a9-faad-462e-b59e-24c822d4e767'></a>

Example

```
1 // ...
2
3 // retrieve the simple key characteristic
4 BLECharacteristic simpleKeyCharacteristic = peripheral.getCharacteristic(SIMPLE_KEY_CHARACTERISTIC_UUID);
5
6 // subscribe to the simple key characteristic
7 Serial.println("Subscribing to simple key characteristic...");
8 if (!simpleKeyCharacteristic) {
9   Serial.println("no simple key characteristic found!");
10   peripheral.disconnect();
11   return;
12 } else if (!simpleKeyCharacteristic.canSubscribe()) {
13   Serial.println("simple key characteristic is not subscribable!");
14   peripheral.disconnect();
15   return;
16 } else if (!simpleKeyCharacteristic.subscribe()) {
17   Serial.println("subscription failed!");
18   peripheral.disconnect();
19   return;
20 }
21
22 // ...
```

<a id='726bece7-8c2a-4ae0-85f6-b3aca547cb50'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='2d40fec9-c444-4ab1-80f0-ea9da586fc36'></a>

19/22

<!-- PAGE BREAK -->

<a id='57fdcf08-53ea-46b7-b018-19c15b4dfc33'></a>

12/4/25, 2:50 PM

<a id='8e1bde96-f998-4e40-8b15-440ce6525cc0'></a>

ArduinoBLE | Arduino Documentation

<a id='130fffea-b6b7-49c2-b19c-7d9cdafc1f46'></a>

ARDUINODOCS

<a id='3ed88632-12e6-49eb-b10c-3f216cb82567'></a>



<a id='ca52daf9-9b93-4f76-abcc-e8851940e8f6'></a>

Query if a Bluetooth Low Energy characteristic is unsubscribable.

## Syntax

```
1 bleCharacteristic.canUnsubscribe()
```

<a id='7b758869-156f-48ea-a37d-1db9498859c9'></a>

## Parameters

None

<a id='0e665ba9-b02c-4a6f-9cd8-c929e54e2bc7'></a>

Returns

true, if characteristic is unsubscribable,
false otherwise

<a id='5eeedd14-399d-4501-9e02-fc247252855d'></a>

# Example

```java
1 if (characteristic.canUnsubscribe()) {
2   Serial.println("characteristic is unsubscribat
3 }
```

<a id='f8197cc8-cad9-4e40-9f69-428f61950251'></a>

> bleCharacteristic.unsubscribe()
Unsubscribe to a Bluetooth® Low Energy characteristics
notifications or indications.

<a id='90a70fdd-6e49-427f-9a92-b71cd53ba06c'></a>

## Syntax

```
1 bleCharacteristic.unsubscribe()
```

<a id='d6ffa511-1bdf-4c2a-9756-00e446c4d0ed'></a>

**Parameters**

None

<a id='cf82434f-3842-4976-8f12-4e599fcc1f56'></a>

Returns

true, on success,
false on failure

<a id='bbbd53f5-c78d-4f1d-aede-18f6643d8ff4'></a>

Example

<a id='effb768d-bae5-4611-8621-7d248dc332cd'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='817912ce-1e9a-4dab-a1c0-a17c845f1a4f'></a>

20/22

<!-- PAGE BREAK -->

<a id='fa242a42-06c7-4e9c-b451-5ab9655888df'></a>

12/4/25, 2:50 PM

<a id='a97cda28-7e8c-4e0b-9f27-7501175b2969'></a>

ArduinoBLE | Arduino Documentation

<a id='dd76e6a2-03a6-4959-bbca-388ed5580af6'></a>

ARDUINODOCS

<a id='ea6d3e72-4eca-4f23-b54e-834794e37adb'></a>

// ...

// retrieve the simple key characteristic
BLECharacteristic simpleKeyCharacteristic = per

// subscribe to the simple key characteristic
Serial.println("Subscribing to simple key chara
if (!simpleKeyCharacteristic) {
    Serial.println("no simple key characteristic
    peripheral.disconnect();
    return;
} else if (!simpleKeyCharacteristic.canSubscrib
    Serial.println("simple key characteristic is
    peripheral.disconnect();
    return;
} else if (!simpleKeyCharacteristic.subscribe()
    Serial.println("subscription failed!");
    peripheral.disconnect();
    return;
}

// ...

simpleKeyCharacteristic.unsubscribe();

<a id='961ca291-381a-4d27-b728-f4bd34e98841'></a>

v bleCharacteristic.valueUpdated()
Has the characteristics value been updated via a notification or
indication.

<a id='9299aa0d-ab6c-4199-bf8f-6474d77f0414'></a>

# Syntax

```
1 bleCharacteristic.valueUpdated()
```

<a id='e5f47171-034e-4880-ac73-ab71b83dd50f'></a>

Parameters

None

<a id='89109143-6128-4fef-b570-b16b26bccb2d'></a>

Returns

**true**, if the characteristics value been updated via a notification or indication

<a id='683d0d1e-e7f5-47f3-a2a4-af95336abfef'></a>

Example

________________________________________________________________________________

<a id='b0891781-e563-451b-a149-e7ea94b57ddb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='a2be90fd-6150-41af-bb9b-8c23c6a2b7f8'></a>

21/22

<!-- PAGE BREAK -->

<a id='d7a26b4f-bdc9-4c49-9e07-e921e03aed18'></a>

12/4/25, 2:50 PM

<a id='ebf42978-302f-4db5-bdfd-6953b19b7b7c'></a>

ArduinoBLE | Arduino Documentation

<a id='29f91fde-86cf-4cc1-891b-762b3a91ee4e'></a>

ARDUINODOCS

<a id='4326a875-ac79-493a-9478-46e652841366'></a>

```c
1 while (peripheral.connected()) {
2   // while the peripheral is connected
3
4   // check if the value of the simple key characteristic
5   if (simpleKeyCharacteristic.valueUpdated()) {
6     // yes, get the value, characteristic is 1
7     byte value = 0;
8
9     simpleKeyCharacteristic.readValue(value);
10
11    if (value & 0x01) {
12      // first bit corresponds to the right button
13      Serial.println("Right button pressed");
14    }
15
16    if (value & 0x02) {
17      // second bit corresponds to the left button
18      Serial.println("Left button pressed");
19    }
20  }
21 }
```

<a id='4489552a-43ac-4956-aace-29b2c055f61a'></a>

Was this article helpful?

option Thumbs Up: [ ]
option Thumbs Down: [ ]

<a id='cc45b29d-85b0-4948-94d0-724cedd07e96'></a>

Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='d787c582-c43d-456c-94c9-434d5c04fff9'></a>

© 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='300e5d8b-0def-4bde-b9e9-0b43ead751a0'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLECharacteristic-library.html

<a id='4bccb0ca-c80e-4909-a561-1d40f07407a2'></a>

22/22