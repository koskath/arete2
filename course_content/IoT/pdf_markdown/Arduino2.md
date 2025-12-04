<a id='e2704209-e8f8-4c3e-a200-95afe4e41db6'></a>

12/4/25, 2:51 PM

<a id='1bdcc652-b88a-4e5f-b9c1-214602b221d1'></a>

ArduinoBLE | Arduino Documentation

<a id='ce1c51ec-e287-461a-9bb9-a7031b5920c3'></a>

ARDUINODOCS

<a id='cd28836d-5666-4cb1-9484-4c28d3fc0342'></a>

Search on Docs /

<a id='f771097d-fec5-434c-9b85-518a8441db9c'></a>

← Go Back

## Library

<a id='87c182eb-aabb-4d32-9955-0d3d452d6d30'></a>

Recents viewed

<a id='116e3272-e842-4e32-b99e-5b64815e3bb6'></a>

option ArduinoBLE: [x]
option ArduinoMqttClient: [ ]
option WiFiNINA: [ ]
option Arduino SigFox for MKRFox1200: [ ]
option autowp-mcp2515: [ ]
option Arduino_MKRENV: [ ]
option Arduino_MKRGPS: [ ]
option Arduino_APDS9960: [ ]
option Arduino_MKRIoTCarrier: [ ]

<a id='99e29aa4-5bc4-4fa4-83b0-9be3323323c5'></a>

Home / Programming / Library / ArduinoBLE

<a id='14143782-8570-4162-aa8c-4f489f94786f'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='919833c3-f293-4b06-8d73-666ade0ef524'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='5fa51426-0a60-4516-b1e8-543ba7339bb5'></a>

GO TO REPOSITORY

<a id='7a72381f-5069-42ae-9c1c-38cd4506bfd8'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='96f99b12-45cd-4065-805b-e5821a931be2'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='4c6090c6-b789-4b2d-bc89-db555ad0ecbb'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled "Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low Energy is optimized for low power use at low data rates, and was designed to operate from simple lithium coin cell batteries.

<a id='a89f8326-ed49-4b6d-ab5f-23a6a186db85'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='64f8ce01-64de-4242-a90f-d8c46beec97b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='4ce2d9ad-fbdd-400b-85ea-be3b24bc1a52'></a>

Help

<a id='35de5ece-036d-40cf-ab40-9a6b6e5cea17'></a>

1/24

<a id='48666032-422b-4213-973c-429e9c03e894'></a>

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

<a id='5d1aa133-8c28-4682-b623-c533d4986676'></a>

12/4/25, 2:51 PM

<a id='15d07dc0-eb1b-4901-8f3d-e72f943fb13e'></a>

ArduinoBLE | Arduino Documentation

<a id='d9d69280-d599-412e-8a96-e9834da28ce4'></a>

ARDUINODOCS

<a id='77ac6573-fff2-4312-95ec-3e9cc1f5eacf'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='e5f82baa-50a0-4772-a2ff-388ce467c5f0'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='43852655-ebd7-4527-a969-9e07475ddd8b'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='39c8f49f-c3bc-41c8-9ec6-d2da7471f69b'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='07f576e2-780a-4882-8af5-ad17246d6883'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='c1e9d5ea-76e4-43b6-b0aa-bdd52dcb81c2'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='10fac00d-0a05-4ce8-87f0-d0aeb85adde4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='cb4e5ba4-a9db-479f-ac2c-1202c1a098f2'></a>

2/24

<!-- PAGE BREAK -->

<a id='11df5073-c015-40b9-9955-8c005280b7a9'></a>

12/4/25, 2:51 PM

<a id='744a5ec0-d235-4600-ae25-0d7177fa93d7'></a>

ArduinoBLE | Arduino Documentation

<a id='aa513f75-acf7-4f1a-8aad-3fb302482048'></a>

ARDUINODOCS

<a id='0e1e7514-932e-4cef-860d-b498e66ba01b'></a>

# Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='1f0d3b02-d064-43b8-ad9a-c59cdf01814f'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='0c440740-84c5-4b5e-b0de-87166106efb3'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='75234a61-419b-4672-a40a-acb08153c0d7'></a>

Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint
in designing services. Given this limit, you should consider how best to
store data about your sensors and actuators most effectively for your
application. The simplest design pattern is to store one sensor or actuator
value per characteristic, in ASCII encoded values.

<a id='1e18f61c-55b3-425f-8aac-f0b3718d4f18'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='1b9f389d-8d1b-46ec-a105-17ca30396b3f'></a>

This is also the most expensive in memory terms, and would take the longest to read. But it's the simplest for development and debugging.

<a id='e06be320-f1a9-457d-ae05-60689cb2f109'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='edcd5b9e-3562-405f-8f14-189afaf0f25d'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='4ac1845d-3c50-44c1-9ced-6dda1aa951cb'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='b4f8640f-3ddb-4b14-a50a-e9ef678eec93'></a>

Read/write/notify/indicate

<a id='443c52ac-0ec0-4c58-adb0-47b8cc81fa15'></a>

There are 4 things a central device can do with a characteristic:

<a id='4003e3be-f46f-4dc4-98a5-513d2b8468d0'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='aa1e0b7a-9ea8-4cdb-9332-afd42fe3dc05'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='1ba53e8b-287e-4c33-bcb0-7fc35712a3c2'></a>

3/24

<a id='47cde113-fdc4-43b1-bfbc-53cb7ad0f4be'></a>



<!-- PAGE BREAK -->

<a id='282bfb95-cefe-463e-b014-9117d53d050e'></a>

12/4/25, 2:51 PM

<a id='e858013d-31b7-44d3-a147-0ea384bf6075'></a>

ArduinoBLE | Arduino Documentation

<a id='4accd674-b650-43bd-b434-16f1b5b011e6'></a>

ARDUINODOCS

<a id='98f91b39-0b23-4ac3-a67c-ea228c69d103'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='d05f0068-1b43-4f34-89eb-e1eb364e5fee'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='3e74d089-570f-4c84-9b01-204133a0fba7'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='86ac59a4-48fe-427b-9243-4b86c77bc23b'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='30390742-aeb7-48b9-b47c-795bcdaf98a8'></a>

You can provide additional services that are not advertised. Central devices will learn about these through the connection/bonding process. Non-advertised services cannot be used to discover devices, though. Sometimes this is not an issue. For example, you may have a custom peripheral device with a custom service, but in your central device app you may know that it also provides the Battery Service and other services.

<a id='d9d02e99-b0cc-4658-82e7-f7472eccc569'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='3c12a3c7-0cb8-4e48-af14-1a9bdd0dc6a0'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='32996292-5b03-4c65-b15d-76bbdc728da5'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='56e52f78-3d8b-443e-9d72-262d05002d11'></a>

BLE class BLEDevice Class BLEService Class

<a id='423fba50-4c61-4d58-a114-dda01c349487'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='465a30fd-5092-4f12-b365-ab2dc507f434'></a>

4/24

<!-- PAGE BREAK -->

<a id='f1f59aa4-9f55-473b-95f3-dd437644046c'></a>

12/4/25, 2:51 PM

<a id='204ce839-a63d-4cc5-a981-df2c8c7ee26d'></a>

ArduinoBLE | Arduino Documentation

<a id='1cc26f81-69fd-45b4-80d2-ed3c845b325a'></a>

ARDUINODOCS

<a id='a4e4338a-fcaa-4915-9880-099d38779e43'></a>

Used to get information about the devices connected or discovered while scanning

<a id='9d176bf9-270f-44a4-b318-0ac6fdc5850a'></a>

bleDevice.poll()
Poll for Bluetooth® Low Energy radio events for the specified Bluetooth® Low Energy device and handle them.

### Syntax

```
bleDevice.poll()
bleDevice.poll(timeout)
```

### Parameters

timeout: optional timeout in ms, to wait for event. If not specified defaults to 0 ms.

### Returns

Nothing

### Example

```
// listen for Bluetooth® Low Energy centrals to co
BLEDevice central = BLE.central();

// if a central is connected to peripheral:
if (central) {
  central.poll();
}

// ...
```

<a id='0a52f717-105b-4874-9a01-4d11bf47ee6e'></a>

bleDevice.connected()

<a id='723aac76-6f2a-4241-928b-dc52bae5403c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='0e9debf5-077d-4b44-9a8a-828692e585eb'></a>

5/24

<!-- PAGE BREAK -->

<a id='818b6629-ccd6-469b-8682-b8fc6fba71fb'></a>

12/4/25, 2:51 PM

<a id='30d03dcf-6bfb-415d-8390-dc1edfe93f42'></a>

ArduinoBLE | Arduino Documentation

<a id='793b31fb-9726-4ade-882b-9d0cba532d1b'></a>

ARDUINODOCS

<a id='947f9359-1991-4343-8a87-c82fb2a1728b'></a>



<a id='4736489c-2a6a-4c17-b37a-16cf34fe2063'></a>

Query if a Bluetooth® Low Energy device is connected

## Syntax

```
bleDevice.connected()
```

<a id='6616d54e-2d15-4f5d-b72b-51db1f5f1bd7'></a>

Parameters

None

<a id='68394d2d-8071-4495-a724-1825fd30aad4'></a>

## Returns

**true** if the Bluetooth® Low Energy device is connected,
otherwise **false**.

<a id='12a5cce3-10b9-4757-a83d-9dbb1b1bbc60'></a>

## Example

```
// listen for Bluetooth® Low Energy centrals to connect
BLEDevice central = BLE.central();

// while the central is still connected
while (central.connected()) {

  // ...
}
```

<a id='ee0c3b5b-cd69-4a56-9503-46d744247567'></a>

bleDevice.disconnect()

<a id='edc44ddf-e8f8-4950-928d-e0852d740b75'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='ad750222-795f-4b72-abd7-47e9dc9dde20'></a>

6/24

<!-- PAGE BREAK -->

<a id='c5a7ef41-390b-4028-a1d5-84933699f37d'></a>

12/4/25, 2:51 PM

<a id='3491cde2-8433-447c-a812-37b840d29254'></a>

ArduinoBLE | Arduino Documentation

<a id='7d67bc2f-aadc-403d-8d6a-bae5435d242b'></a>

ARDUINODOCS

<a id='4a656b02-749b-4d6e-aa8f-b5f3df9eed68'></a>

<::transcription of the content
: empty text box::>

<a id='1c0ded36-3c50-4793-b5ba-a89626266f91'></a>

Disconnect the Bluetooth® Low Energy device, if connected

## Syntax

```
1 bleDevice.disconnect()
```

<a id='651fa749-0855-4bcc-b83c-9642595d4299'></a>

**Parameters**

None

<a id='ab692a25-0193-4fe7-b528-00e81b08a397'></a>

## Returns

**true** if the Bluetooth® Low Energy device was disconnected,
otherwise **false**.

<a id='0ea13d79-422f-4227-8592-afa0279fde34'></a>

Example

```
1 // listen for Bluetooth® Low Energy centrals to co
2 BLEDevice central = BLE.central();
3 
4 
5 central.disconnect();
```

<a id='fa6708c9-657d-44a0-b886-c1828aa4653e'></a>

✓ bleDevice.address()
Query the Bluetooth® address of the Bluetooth® Low Energy device.

<a id='bd0b8376-1d8e-43ad-9d57-0f5d012a5fe2'></a>

## Syntax

```
1 bleDevice.address()
```

<a id='0657d562-df6f-4bb9-8dd0-2353e6f25755'></a>

Parameters

None

<a id='edc3ee1c-b402-4466-89d8-2d5c0abf7527'></a>

## Returns

**Bluetooth® address** of the Bluetooth® Low Energy device (as a String).

<a id='6e16a248-b0e7-43b1-bb61-b859b77d3789'></a>

Example

<a id='71045ca0-3779-4aba-a3f7-7a36586c59b9'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='d933d4ed-1cd9-47e0-a306-ceaa38d3ca91'></a>

7/24

<!-- PAGE BREAK -->

<a id='6936260c-567b-44a7-b3f0-efc46d234773'></a>

12/4/25, 2:51 PM

<a id='f78e0292-2f26-4e4f-8e07-69a0ad5fc1e8'></a>

ArduinoBLE | Arduino Documentation

<a id='fb22d90d-2215-4fd6-a2c5-f2af4a1f386d'></a>

ARDUINODOCS

<a id='0d676843-6f39-4426-8b8c-c995fc692ee1'></a>

```c
// listen for Bluetooth® Low Energy peripherals to
BLEDevice central = BLE.central();

// if a central is connected to peripheral:
if (central) {
  Serial.print("Connected to central: ");
  // print the central's MAC address:
  Serial.println(central.address());
}
```

<a id='bc19d891-45f3-489f-b355-bceb6c17a25c'></a>

bleDevice.rssi()
Query the RSSI (Received signal strength indication) of the Bluetooth® Low Energy device.

<a id='dd7a15a4-38c7-41de-ab93-1240e8c08eab'></a>

## Syntax

```
1 bleDevice.rssi()
```

<a id='3da0a5ff-7ca8-40d3-b567-83f819bf49c4'></a>

Parameters

None

<a id='e69203d4-1b06-4413-8106-c7d2b53268d1'></a>

Returns

**RSSI** of the connected Bluetooth® Low Energy device, 127 if
the Bluetooth® Low Energy device is not connected.

<a id='65be3d43-87a0-4a84-ad6e-37522530bd32'></a>

# Example

```
1 if (bleDevice.connected()) {
2   Serial.print("RSSI = ");
3   Serial.println(bleDevice.rssi());
4 }
```

<a id='20765b72-a14c-41bd-8369-1e7c6cf7d19a'></a>

v bleDevice.characteristic()
  Get a BLECharacteristic representing a Bluetooth® Low Energy
  characteristic the device provides.

<a id='a6f3d58d-3d16-4d15-87af-c51dd9d4ab77'></a>

Syntax

```

```

<a id='5668a19d-2096-4a72-aef8-c957194de6ba'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='0e0379dc-bc8f-4591-b3e5-50ce2ad0fc83'></a>

8/24

<!-- PAGE BREAK -->

<a id='ee78d540-f302-4809-b740-f2bfad974812'></a>

12/4/25, 2:51 PM

<a id='35488780-3223-4387-8697-bce5d296706a'></a>

ArduinoBLE | Arduino Documentation

<a id='3d3fed59-8292-48d5-b2a4-df01e9e6d42a'></a>

ARDUINODOCS

<a id='1ee83438-698c-40f0-8bdc-327feaa61bba'></a>

[Empty Field]

<a id='bc0d52c7-be34-4525-b0a1-4e628e8c542c'></a>

1 bleDevice.characteristic(index)
2 bleDevice.characteristic(uuid)
3 bleDevice.characteristic(uuid, index)

<a id='e46d822b-3b80-48e6-a818-b2b0ab87d7d7'></a>

## Parameters

**index**: index of characteristic
**uuid**: uuid (as a **String**)

<a id='012b28ef-ab8d-402a-9cf3-8d06edb0bb5f'></a>

## Returns

**BLECharacteristic** for provided parameters

<a id='88f1242f-1136-4c81-ad30-f262e82cb3d4'></a>

Example

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6
7 Serial.println("BLE Central scan");
8
9 // start scanning for peripheral
10 BLE.scan();
11
12
13 BLEDevice peripheral = BLE.available();
14
15 if (peripheral) {
16   // ...
17
18   Serial.println("Connecting ...");
19
20   if (peripheral.connect()) {
21     Serial.println("Connected");
22   } else {
23     Serial.println("Failed to connect!");
24     return;
25   }
26
27   // discover peripheral attributes
28   Serial.println("Discovering attributes ...");
29 }
```

<a id='5be29873-5283-4b21-b864-31e6a47e0ab0'></a>

### bleDevice.discoverAttributes()
Discover all of the attributes of Bluetooth® Low Energy device.

## Syntax

```
1 bleDevice.discoverAttributes()
```

<a id='f99c9b92-674a-410f-a4d2-33389400bd02'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='ffd44084-3f46-4a1f-9e93-00fa814133ed'></a>

9/24

<!-- PAGE BREAK -->

<a id='a3bef749-1a62-4116-a78d-a31ffc387761'></a>

12/4/25, 2:51 PM

<a id='9979ac99-35d1-446a-998f-f00629d8fa4f'></a>

ArduinoBLE | Arduino Documentation

<a id='b34d2cce-c74c-440c-b3ff-675081c538cc'></a>

ARDUINODOCS

<a id='1ee54206-a012-46c3-8883-7dea89c1aa61'></a>

## Parameters

None

## Returns

**true**, if successful,
**false** on failure.

<a id='beab9954-0cb5-4201-9478-316663eae6b8'></a>

Example

```c
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();
if (peripheral) {
  // ...
  Serial.println("Connecting ...");
  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }
}

// discover peripheral attributes
Serial.println("Discovering attributes...");
```

<a id='5a8adcec-167c-4bb2-b048-a8d66b965447'></a>

### bleDevice.discoverService()

Discover the attributes of a particular service on the Bluetooth® Low Energy device.

## Syntax

```
1 bleDevice.discoverService(serviceUuid)
```

<a id='f4a4aeca-144a-4ec2-a8cd-37ececb06d27'></a>

Parameters

<a id='4d9daced-bf31-4ab5-96b8-d655cc394a9b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='32e04844-c7f7-49b8-817f-a0034c0dd19f'></a>

10/24

<!-- PAGE BREAK -->

<a id='2b83a105-6deb-4703-b701-91faae70ec77'></a>

12/4/25, 2:51 PM

<a id='f1333506-4d95-46b1-a65a-82e9d75844c2'></a>

ArduinoBLE | Arduino Documentation

<a id='bdec0f0e-64dc-4653-8bff-356bc18dce53'></a>

ARDUINODOCS

<a id='c2f2f7ab-7998-4800-84b6-8b59079d9fae'></a>

Returns

**true**, if successful,
**false** on failure.

<a id='541f29bf-69dd-4b94-b94e-81b9ac7a08e5'></a>

Example

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ene
4   while (1);
5 }
6
7 Serial.println("BLE Central scan");
8
9 // start scanning for peripheral
10 BLE.scan();
11
12
13 BLEDevice peripheral = BLE.available();
14
15 if (peripheral) {
16   // ...
17
18   Serial.println("Connecting ...");
19
20   if (peripheral.connect()) {
21     Serial.println("Connected");
22   } else {
23     Serial.println("Failed to connect!");
24     return;
25   }
26 }
27
28 // discover service attributes
```

<a id='91bf1456-f0b7-4402-b5df-c25182c4b19d'></a>

v bleDevice.deviceName()
Query the device name (BLE characteristic UUID 0x2a00) of a
Bluetooth® Low Energy device.

<a id='33eaee89-5703-45b0-b893-52d1dd4bef1d'></a>

## Syntax

```
1 bleDevice.deviceName()
```

<a id='fc25890c-e2ad-421d-8446-8b33ee7623c8'></a>

**Parameters**

None

<a id='369417b7-8edd-4d85-86d2-a0565b0ee340'></a>

Returns

<a id='9e4e7b8b-916f-4a87-ac33-1a2ce7098316'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='5fd13aa1-149f-4865-bd53-2f0b295fd260'></a>

11/24

<!-- PAGE BREAK -->

<a id='b82ea5d9-9977-4338-9376-77af7dd53449'></a>

12/4/25, 2:51 PM

<a id='dbd58217-5870-4fb8-a417-194776925b02'></a>

ArduinoBLE | Arduino Documentation

<a id='58d70b27-05f6-4936-845b-8bb1fc9f3d00'></a>

ARDUINODOCS

<a id='efb0d9d0-2311-4584-9f30-c9627216f48e'></a>

Example

```c++
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6
7 Serial.println("BLE Central scan");
8
9 // start scanning for peripheral
10 BLE.scan();
11
12
13 BLEDevice peripheral = BLE.available();
14
15 if (peripheral) {
16   // ...
17
18   Serial.println("Connecting ...");
19
20   if (peripheral.connect()) {
21     Serial.println("Connected");
22   } else {
23     Serial.println("Failed to connect!");
24     return;
25   }
26 }
27
28 // discover peripheral attributes
```

<a id='5a41cd48-5984-491e-8215-1267c1a589d8'></a>

v bleDevice.appearance()
Query the appearance (BLE characteristic UUID 0x2a01) of a
Bluetooth® Low Energy device.

## Syntax

```
1 bleDevice.appearance()
```

## Parameters
None

## Returns
**Appearance value** (as a number).

## Example
```
```

<a id='cbb55dde-6480-4889-a67d-ce058ce557ce'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='39c36137-7b8d-4530-83d8-4253b7c8dd59'></a>

12/24

<!-- PAGE BREAK -->

<a id='b612d708-cc86-45c8-b7c9-a5ddc56b73f9'></a>

12/4/25, 2:51 PM

<a id='81a28c42-a0c1-4a0d-b490-b784b4b895e0'></a>

ArduinoBLE | Arduino Documentation

<a id='c79f951e-bcd0-4818-9526-bbb6b143af28'></a>

ARDUINODOCS

<a id='94c84597-ca1c-49b5-ad97-32aaa553c715'></a>



<a id='403aae55-df21-4613-85de-b6b5a3438d51'></a>

```cpp
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy setup failed!");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...

  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }
}

// discover peripheral attributes
Serial.println("Discovering attributes...");
```

<a id='d3b4950f-8625-4d16-893a-c48eea1fcaf4'></a>

bleDevice.serviceCount()

Query the number of services discovered for the Bluetooth® Low Energy device.

### Syntax

```
1 bleDevice.serviceCount()
```

<a id='5e647eee-c7ea-495a-a6c6-3a9bd281ec43'></a>

Parameters

None

<a id='84ff523d-6f03-46b5-81b7-49da6ff104df'></a>

### Returns

The number of **services discovered** for the Bluetooth® Low Energy device.

<a id='29ad44ff-b6d7-49a5-83d3-305f7174ff2e'></a>

Example

<::text: empty input box::>

<a id='1f094404-b91a-4cb1-96c8-30252b4664a3'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='df611c91-d0d4-4097-9be3-c9620e113376'></a>

13/24

<!-- PAGE BREAK -->

<a id='ac660c7d-6ab0-4ad6-aa7d-2c91855c654e'></a>

12/4/25, 2:51 PM

<a id='77bc74bf-4a5b-4db5-9bf5-333d0aaf38ce'></a>

ArduinoBLE | Arduino Documentation

<a id='4b59ebbb-c1f9-483f-ac4b-c257c62c81b0'></a>

ARDUINODOCS

<a id='72f46fa7-b681-4317-84d6-e1dca3aa0803'></a>

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ene
4   while (1);
5 }
6
7
8 Serial.println("BLE Central scan");
9
10 // start scanning for peripheral
11 BLE.scan();
12
13
14 BLEDevice peripheral = BLE.available();
15
16 if (peripheral) {
17   // ...
18
19   Serial.println("Connecting ...");
20
21   if (peripheral.connect()) {
22     Serial.println("Connected");
23   } else {
24     Serial.println("Failed to connect!");
25     return;
26   }
27 }
28 // discover peripheral attributes
```

<a id='4406ded6-cd14-4e12-a109-c2018c18ff2e'></a>

bleDevice.hasService()

Query if the Bluetooth® Low Energy device has a particular service.

<a id='c5c6ecf2-34ce-4a7b-8268-8486945b031d'></a>

## Syntax

```
1 bleDevice.hasService(uuid)
2 bleDevice.hasService(uuid, index)
```

<a id='2f448e5e-6ac3-4370-b7f6-725e5aad5d4d'></a>

# Parameters

**uuid**: uuid to check (as a **String**)
**index**: optional, index of service to check if the device provides
more than on. Defaults to 0, if not provided.

<a id='3fdb31a8-8338-49aa-aed4-e1c1966d3d32'></a>

## Returns

**true**, if the device provides the service,
**false** otherwise.

<a id='de35ced4-a6f8-48ce-8c47-1fbc84beac24'></a>

Example

[           ]

<a id='a18e5be9-2432-49a6-8c16-daa34b810678'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='95ef0cd5-b3b4-4b5c-9eb8-b4100a1d8a4d'></a>

14/24

<!-- PAGE BREAK -->

<a id='b8718940-dad8-4c72-9c5e-24a246268a12'></a>

12/4/25, 2:51 PM

<a id='65d1275f-3f85-470a-864b-55c9de022583'></a>

ArduinoBLE | Arduino Documentation

<a id='bd22b26a-d0e0-4228-95f9-b4aad543a328'></a>

ARDUINODOCS

<a id='964ee5c7-ed26-4fcb-9bbf-cb746f6517ee'></a>

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ene");
4   while (1);
5 }
6 
7 Serial.println("BLE Central scan");
8 
9 // start scanning for peripheral
10 BLE.scan();
11 
12 
13 BLEDevice peripheral = BLE.available();
14 
15 if (peripheral) {
16   // ...
17 
18   Serial.println("Connecting ...");
19 
20   if (peripheral.connect()) {
21     Serial.println("Connected");
22   } else {
23     Serial.println("Failed to connect!");
24     return;
25   }
26 }
27 
28 // discover peripheral attributes
```

<a id='2a42d94e-33a5-4775-8266-0390811b78f9'></a>

bleDevice.service()
Get a BLEService representing a Bluetooth® Low Energy service the device provides.

### Syntax

```
1 bleDevice.service(index)
2 bleDevice.service(uuid)
3 bleDevice.service(uuid, index)
```

### Parameters

index: index of service
uuid: uuid (as a String)

### Returns

BLEService for provided parameters

### Example

<a id='dacff8c7-426d-4ebd-a402-fb58eacab368'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='55318519-0bf4-47d3-b488-70e1dc318f74'></a>

15/24

<!-- PAGE BREAK -->

<a id='92db9a23-2281-4867-88e1-31f477ea9d43'></a>

12/4/25, 2:51 PM

<a id='1b52d41a-3e3a-4c7e-ad44-6812886f7d71'></a>

ArduinoBLE | Arduino Documentation

<a id='40420958-e43d-4fb5-8caf-59d7b73eeca6'></a>

ARDUINODOCS

<a id='74a57665-4b20-4c7b-a132-3ba4539fdd16'></a>

___

<a id='afa50122-bad4-44c9-aafe-a81bf92a11d2'></a>

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6 
7 Serial.println("BLE Central scan");
8 
9 // start scanning for peripheral
10 BLE.scan();
11 
12 
13 BLEDevice peripheral = BLE.available();
14 
15 if (peripheral) {
16   // ...
17   
18   Serial.println("Connecting ...");
19   if (peripheral.connect()) {
20     Serial.println("Connected");
21   } else {
22     Serial.println("Failed to connect!");
23     return;
24   }
25 }
26 
27 // discover peripheral attributes
28 Serial.println("Discovering attributes ...");
```

<a id='6890b603-25dc-413a-a82a-4179553fa675'></a>

✓ bleDevice.characteristicCount()
Query the number of characteristics discovered for the Bluetooth®
Low Energy device.

<a id='ba279de0-0be0-4608-8e5c-272c5df0cc96'></a>

## Syntax

```
1 bleDevice.characteristicCount()
```

<a id='19bdfc84-c047-4eef-9339-b8d3ca3b93fb'></a>

Parameters

None

<a id='eddd4412-17de-4fe9-929c-20b353db935d'></a>

## Returns

The **number of characteristics** discovered for the Bluetooth® Low Energy device.

<a id='60ef4a8c-3806-4249-a37d-ed85c97fe2a9'></a>

Example

---

<a id='68b23d92-e001-4c8a-be0c-00f6c7e0dfd6'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='7dca9566-c9c0-4a6e-9ccc-c627c162cd23'></a>

16/24

<!-- PAGE BREAK -->

<a id='87d84770-f8aa-4f61-9c84-191292c30b6a'></a>

12/4/25, 2:51 PM

<a id='6276abd1-5a04-4f70-9e8a-b25236ae5b7a'></a>

ArduinoBLE | Arduino Documentation

<a id='96749d7e-4193-40ea-836a-d9cb1c3af0e0'></a>

ARDUINODOCS

<a id='ff79b52d-32ae-4e78-8653-bcc875298000'></a>

A very faint, light grey rectangular outline is visible in the center of the image, appearing empty.

<a id='238a0857-e618-41ed-9761-49a88b5d5720'></a>

// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy...");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...

  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }
}

// discover peripheral attributes

<a id='1108230d-6f74-4552-a434-c2ee54fecec4'></a>

v bleDevice.hasCharacteristic()
Query if the Bluetooth® Low Energy device has a particular characteristic.

<a id='eed2ae10-8bf1-4712-8235-7375e76633aa'></a>

## Syntax

```
1 bleDevice.hasCharacteristic(uuid)
2 bleDevice.hasCharacteristic(uuid, index)
```

<a id='034686ef-2088-4ec8-a9a7-cd2cf6839b7e'></a>

## Parameters

**uuid**: uuid to check (as a **String**)

**index**: optional, index of characteristic to check if the device
provides more than on. Defaults to 0, if not provided.

<a id='37c4fb5a-84a2-4948-a197-aa12b1cac396'></a>

## Returns

**true**, if the device provides the characteristic,
**false** otherwise.

<a id='3d30bfbd-6436-4e87-879d-a6e2cdaae062'></a>

Example

<a id='f4e692e6-08d3-448e-b48e-df98ec25a42d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='8cd2d6a0-79be-4ce5-8abc-5becb4e03d6d'></a>

17/24

<!-- PAGE BREAK -->

<a id='22ec92e6-4364-414c-9251-d7d3ff530b1f'></a>

12/4/25, 2:51 PM

<a id='9f8ed2ad-892b-4c23-bf7f-340a3d509df9'></a>

ArduinoBLE | Arduino Documentation

<a id='7989c7c4-4e87-4ab2-b053-c48c3fdb3395'></a>

ARDUINODOCS

<a id='1bee55ac-204d-42be-a142-6ad7d0fcd4e7'></a>

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6
7 Serial.println("BLE Central scan");
8
9 // start scanning for peripheral
10 BLE.scan();
11
12
13 BLEDevice peripheral = BLE.available();
14
15 if (peripheral) {
16   // ...
17
18   Serial.println("Connecting ...");
19
20   if (peripheral.connect()) {
21     Serial.println("Connected");
22   } else {
23     Serial.println("Failed to connect!");
24     return;
25   }
26
27   // discover peripheral attributes
28
```

<a id='08caafda-124c-4457-8c95-b82697c0b9a6'></a>

## bleDevice.hasLocalName()
Query if a discovered Bluetooth® Low Energy device is advertising a local name.

### Syntax
```
1 bleDevice.hasLocalName()
```

### Parameters
Nothing

### Returns
**true**, if the device is advertising a local name,
**false** otherwise.

### Example

<a id='2df3bd1c-4353-4763-b096-58c2986b5c1d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='ad808b4d-56f8-4984-be85-86522b79387b'></a>

18/24

<!-- PAGE BREAK -->

<a id='576131e2-32e2-4ed1-9272-b7542ddbaec5'></a>

12/4/25, 2:51 PM

<a id='3457b018-43dd-4656-865d-aa793d8327b4'></a>

ArduinoBLE | Arduino Documentation

<a id='c9616af9-9311-4a98-85fa-81a7ac0e0117'></a>

ARDUINODOCS

<a id='4503d0b7-c4c4-4b92-aeb5-b59842275556'></a>

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scan();
12 
13 
14 BLEDevice peripheral = BLE.available();
15 
16 if (peripheral) {
17   // ...
18 
19   // print the local name, if present
20   if (peripheral.hasLocalName()) {
21     Serial.print("Local Name: ");
22     Serial.println(peripheral.localName());
23   }
24 }
25 // ...
26 }
```

<a id='51b0efde-edbf-44fa-90bd-55b47033f413'></a>

✓ bleDevice.hasAdvertisedServiceUuid()
Query if a discovered Bluetooth® Low Energy device is advertising
a service UUID.

<a id='e64b68a1-5ee4-4ed6-8637-c5a58a2fc49b'></a>

## Syntax

```
1 bleDevice.hasAdvertisedServiceUuid()
2 bleDevice.hasAdvertisedServiceUuid(index)
```

<a id='52d3faec-0603-40af-b69a-35cf1d9e717e'></a>

## Parameters

**index**: optional, defaults to 0, the index of the service UUID, if the device is advertising more than one.

<a id='650dbe09-c3fe-4911-b199-05e661643310'></a>

## Returns

**true**, if the device is advertising a service UUID,
**false** otherwise.

<a id='0de7bdc3-7ee2-4d00-a1ab-5a3f3df3e24b'></a>

Example

________________________________________________________________________________

<a id='89318beb-50d2-4b5c-a505-32a650381ea4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='96082551-12ea-4b38-87ba-9cd0de05cf02'></a>

19/24

<!-- PAGE BREAK -->

<a id='22e52980-98fc-4429-a88c-45a8c655496f'></a>

12/4/25, 2:51 PM

<a id='efc9e4c0-f0da-40dc-8fb7-6cf6b78af6ed'></a>

ArduinoBLE | Arduino Documentation

<a id='2c2ec017-f66e-4863-bdc7-fbdf027d898b'></a>

ARDUINODOCS

<a id='cd8dc661-2275-41a2-841e-c733dfc091e5'></a>



<a id='13277a7c-986d-4d05-bce6-6d1f6f22a14e'></a>

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scan();
12 
13 
14 BLEDevice peripheral = BLE.available();
15 
16 if (peripheral) {
17   // ...
18 
19   // print the advertised service UUIDs, if present
20   if (peripheral.hasAdvertisedServiceUuid()) {
21     Serial.print("Service UUIDs: ");
22     for (int i = 0; i < peripheral.advertisedServiceUuidCount(); i++) {
23       Serial.print(peripheral.advertisedServiceUuid(i));
24       Serial.print(" ");
25     }
26     Serial.println();
27   }
28 }
29 //
```

<a id='d1d027c1-7514-4809-a8c5-de6180e5ab3c'></a>

✓ bleDevice.advertisedServiceUuidCount()
Query the number of advertised services a discovered Bluetooth® Low Energy device is advertising.

<a id='d3fcd8e9-604c-411a-aee1-ce0e784b0ff8'></a>

## Syntax

```
1 bleDevice.advertisedServiceUuidCount()
```

<a id='32871765-98f6-4380-8fb7-e3d599616068'></a>

Parameters

None

<a id='1a479121-a54b-4e19-b8da-29a10c2d4385'></a>

Returns
The number of **advertised services** a discovered Bluetooth®
Low Energy device is advertising.

<a id='93a852de-e285-4b92-96aa-03c550669fe4'></a>

Example

---

<a id='a70a2a49-82fc-4510-98b9-b27fe12602d8'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='c6bac505-9728-4699-98d8-4b754052502e'></a>

20/24

<!-- PAGE BREAK -->

<a id='eec32a84-731e-4f64-b95f-bba3637de7d4'></a>

12/4/25, 2:51 PM

<a id='20abcde3-d678-4eed-8fa2-d04503d4b913'></a>

ArduinoBLE | Arduino Documentation

<a id='e92c5f37-9567-45ef-bfe5-179e804c49d7'></a>

ARDUINODOCS

<a id='f458ff77-68fe-42e0-88dc-cf7bb3eefeb4'></a>



<a id='f98bd20e-626d-4541-be27-0a45b16347d5'></a>

```cpp
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Ene
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...

  // print the advertised service UUIDs, if p
  if (peripheral.hasAdvertisedServiceUuid())
    Serial.print("Service UUIDs: ");
    for (int i = 0; i < peripheral.advertised:
      Serial.print(peripheral.advertisedServi
      Serial.print(" ");
    }
    Serial.println();
}
//
```

<a id='97420243-2ba1-4105-8cd9-f7ab9e8e770a'></a>

## bleDevice.localName()
Query the local name a discovered Bluetooth® Low Energy device is advertising with.

### Syntax
```
1 bleDevice.localName()
```

### Parameters
Nothing

### Returns
Advertised local name (as a String).

### Example

<a id='9cd11ebb-1ea9-43af-a5bb-a7dfc3329e0c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='0e4b41da-cbe9-477c-884c-2571b2aed96b'></a>

21/24

<!-- PAGE BREAK -->

<a id='0de03a74-6ca2-4796-bf51-c97008b69091'></a>

12/4/25, 2:51 PM

<a id='9bf84ee6-5a51-4c17-8251-88b0e18ea5e4'></a>

ArduinoBLE | Arduino Documentation

<a id='bff8beb9-c191-4271-8f64-8d81dfbd4cb6'></a>

ARDUINODOCS

<a id='2a673a4b-b08e-4862-a3db-b73e08363157'></a>

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Ener{");
4   while (1);
5 }
6 
7 Serial.println("BLE Central scan");
8 
9 // start scanning for peripheral
10 BLE.scan();
11 
12 
13 BLEDevice peripheral = BLE.available();
14 
15 if (peripheral) {
16   // ...
17 
18   // print the local name, if present
19   if (peripheral.hasLocalName()) {
20     Serial.print("Local Name: ");
21     Serial.println(peripheral.localName());
22   }
23 }
24 // ...
25 
26 
```

<a id='62ec5d6b-8272-46ef-adeb-2cc8761842ef'></a>

✓ bleDevice.advertisedServiceUuid()
Query an advertised service UUID discovered Bluetooth® Low
Energy device is advertising.

<a id='89e7df42-cbb4-48d5-b1bb-43d1f911f1bf'></a>

## Syntax

```
1 bleDevice.advertisedServiceUuid()
2 bleDevice.advertisedServiceUuid(index)
```

<a id='bfdcf560-0366-4bc8-828d-689fb10fa06c'></a>

## Parameters

**index**: optional, defaults to 0, the index of the **service UUID**, if the device is advertising more than one.

<a id='2b1044a8-3229-4d76-833a-6830080ebd9e'></a>

# Returns

Advertised service **UUID** (as a String).

<a id='6cedcaaa-84f1-490f-b499-dd10f8dca399'></a>

Example

___

<a id='17d20161-7b3d-4a4c-af3c-cc4357eec85e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='4004cced-7b24-4a7f-9383-454bb76c5fde'></a>

22/24

<!-- PAGE BREAK -->

<a id='7c438814-1e6c-4b8a-bb88-9193c095939f'></a>

12/4/25, 2:51 PM

<a id='cc8c46c0-8f8d-4197-bc18-547a94678cf0'></a>

ArduinoBLE | Arduino Documentation

<a id='1eb18bf4-c6ad-4569-9cc9-9fb5a559625d'></a>

ARDUINODOCS

<a id='974b5723-044d-478f-849b-616b91a88867'></a>



<a id='64ac3e74-88b6-4c00-afcd-9242fd124cbc'></a>

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6
7 Serial.println("BLE Central scan");
8
9 // start scanning for peripheral
10 BLE.scan();
11
12 BLEDevice peripheral = BLE.available();
13
14 if (peripheral) {
15   // ...
16
17   // print the advertised service UUIDs, if present
18   if (peripheral.hasAdvertisedServiceUuid()) {
19     Serial.print("Service UUIDs: ");
20     for (int i = 0; i < peripheral.advertisedServiceUuidCount(); i++) {
21       Serial.print(peripheral.advertisedServiceUuid(i));
22       Serial.print(" ");
23     }
24     Serial.println();
25   }
26 }
27
28 //
```

<a id='6cc67a68-cb9f-4488-a5e4-711bb800e492'></a>

✓ bleDevice.connect()
Connect to a Bluetooth® Low Energy device.

<a id='c2ff2891-8e0b-4213-95f0-45c2263f39bc'></a>

## Syntax

```
bleDevice.connect()
```

<a id='d14560d5-1ee4-4775-90b2-4eefe89487a3'></a>

**Parameters**

None

<a id='dcbad363-9726-4804-b177-e7ee752adb99'></a>

Returns

**true**, if the connection was successful,

**false** otherwise.

<a id='71a742aa-6153-4be5-bbb5-d131a1d9e570'></a>

Example

___

<a id='7e7533dc-7795-4010-b507-02460ed27822'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='2f0d600e-1cc1-498d-b6ba-648cd926e09a'></a>

23/24

<!-- PAGE BREAK -->

<a id='79c9770a-f417-4cb4-9b87-7b6cbc70df7c'></a>

12/4/25, 2:51 PM

<a id='848f5f41-de59-410d-93f8-064c5e44b8ad'></a>

ArduinoBLE | Arduino Documentation

<a id='12807490-63fb-4cd1-9c76-8b5e4f74da44'></a>

ARDUINODOCS

<a id='38e75ef5-7fe0-4c0a-baf5-72d4a9317441'></a>



<a id='c3ea867f-8ea2-4d3a-8b20-ceab654c791c'></a>

// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy...");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();


BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...

  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }
}
// ...

<a id='866ea623-84c2-4813-8608-cc708e9589a7'></a>

Was this article helpful?

---

option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='87ab46fa-7209-4a27-8809-9bc828d82882'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='f068e882-cbc4-495d-af32-165345d83dc2'></a>

© 2025 Arduino

<a id='053b0c9a-9408-48e1-9f71-28c183f36c8a'></a>

Terms Of Service

Privacy Policy

Security

Cookie Settings

<a id='8eb4d830-0c32-4425-be12-f40816e3ce7f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEDevice-library.html

<a id='172fd2d5-4997-4b56-968a-b2cd1107bf35'></a>

24/24