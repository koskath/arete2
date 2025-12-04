<a id='b0c71285-e5b1-42f1-a5b6-ce8590913a7f'></a>

12/4/25, 2:51 PM

<a id='daa1882f-b289-4f9a-9b4b-00fd02f0c1f7'></a>

ArduinoBLE | Arduino Documentation

<a id='ea20673c-4c74-437a-bbac-900114c7b4ea'></a>

ARDUINODOCS

<a id='ee4af612-d988-4b49-bb26-32aa8a944947'></a>

Search on Docs /

<a id='66b1f426-1c23-4960-9478-c2486e0db584'></a>

← Go Back

## Library

<a id='e35306a4-6f08-4fd4-8096-d81283479573'></a>

Recents viewed

<a id='4803ff6a-d0a4-4a24-9f03-ef0ad49c90b1'></a>

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

<a id='ec4ce92d-c7f6-4d17-9119-1310e18af554'></a>

Home / Programming / Library / ArduinoBLE

<a id='8006e031-3090-4fc9-8d9e-e18cbf21cdb1'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='fc695392-e6c1-4f2a-980e-d9c98b962738'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='ccd15875-a867-4353-9cc2-950ebd6e7392'></a>

GO TO REPOSITORY

<a id='a2c47c8f-9fb1-4f8c-9b71-e51bd929e8e2'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='77f72e37-616e-4be8-96ac-dbf9fef0e48e'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='2ba68331-6208-497b-93ed-512b3018b194'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled "Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low Energy is optimized for low power use at low data rates, and was designed to operate from simple lithium coin cell batteries.

<a id='9e88d0c4-09e1-4c88-91cb-4988f1805375'></a>

Unlike standard Bluetooth® communication basically based on an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='861249d5-7199-46c1-84b8-96729b8279a0'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='45212e04-f0ff-4156-b0e2-3e7ed8c9e11d'></a>

Help

<a id='ef3477ed-939f-41c9-829e-71dc47f8f8e0'></a>

1/9

<a id='b05ae062-93bb-4245-a01a-22271aa499a7'></a>

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

<a id='c5bf1791-d919-4173-b516-31e974bad5fe'></a>

12/4/25, 2:51 PM

<a id='cd43aad5-4e64-4111-b81d-473e2e9eb80f'></a>

ArduinoBLE | Arduino Documentation

<a id='daa4eea6-f75f-4804-b9be-2ae613aacbda'></a>

ARDUINODOCS

<a id='560fb671-5f6e-49b3-99cc-afdb32cf4316'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='bf33901d-9ad3-4bd4-b415-907691f9ea10'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='de4d6d7e-8293-4471-acc9-72af2649e19a'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='138714c0-273c-4014-8aff-57f87136086d'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='1c256e8f-5087-40b9-abc8-877810e60e00'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='5c968eaa-4a68-43a4-aa76-d6380b352f4c'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='4e62bece-10a4-427d-9a74-927e51f22654'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='25404521-5344-4e51-a727-c2fe3bd06e8e'></a>

2/9

<!-- PAGE BREAK -->

<a id='df681d2b-3fa7-4b90-aa14-d5f57edb68a2'></a>

12/4/25, 2:51 PM

<a id='1e522255-4b31-4b1e-8d84-c434002660d0'></a>

ArduinoBLE | Arduino Documentation

<a id='8e9ae789-76cb-4ee1-a4c0-764a736fad71'></a>

ARDUINODOCS

<a id='7d879763-bcf7-4793-8042-3bc1c08ad032'></a>

## Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='aae90367-9bb1-496b-b484-686cb60cd94d'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='bdf3abc1-79c8-4896-b363-423d1d47fa72'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='b9012e86-789c-4bf8-a406-c04cd3305013'></a>

Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint
in designing services. Given this limit, you should consider how best to
store data about your sensors and actuators most effectively for your
application. The simplest design pattern is to store one sensor or actuator
value per characteristic, in ASCII encoded values.

<a id='a1ac3e3f-a16d-4bcb-b24f-7d6bfb6f25e7'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='b8c2a5f9-6220-4cb9-80b6-f42c5b86cf93'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='573ea7fd-926e-4120-bba3-95fcfc57855e'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='6895c79b-5b93-484e-83c6-dc3b1929a037'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='ec7cb37b-d57b-4af7-b6bd-afcebce6d2ae'></a>

This is more efficient, but you need to be careful not to exceed the 512-byte limit. The accelerometer characteristic above, for example, takes 11 bytes as an ASCII-encoded string.

<a id='0c4112bb-c9d2-48ef-aaab-7ee075dfadb4'></a>

Read/write/notify/indicate

<a id='ae9bf990-4d21-4da4-9e15-c22b783be853'></a>

There are 4 things a central device can do with a characteristic:

<a id='4c19363c-1c42-4cf8-b267-a6fc610e2c43'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='3e8154ac-2114-404d-a959-090614f16b98'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='9ce1b406-6a93-476d-ba6f-ad67c390717c'></a>

3/9

<a id='85afacbc-3322-4d85-a4de-42ebbf35eb7a'></a>



<!-- PAGE BREAK -->

<a id='fd4813ef-4ff9-4a53-9d09-7871cfd2c3fb'></a>

12/4/25, 2:51 PM

<a id='daec8e2b-618a-4be3-98a9-722047a9faa3'></a>

ArduinoBLE | Arduino Documentation

<a id='8d214c3d-7fd4-45a5-a1cb-3f7b2b23ce20'></a>

ARDUINODOCS

<a id='a4edf696-c0b6-4bb5-afba-449a87b2a757'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='dab266cd-0b94-40f2-865d-eaaf93785a74'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='f04c00bb-2a11-4dcb-b3d2-97055efcbde6'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='329fab6a-2d54-48c2-ab6e-630fe6a377b8'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='2538ac1a-4127-4fc9-9961-096ece98ad72'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='1b94ae7b-6e60-4160-a216-84cb1e552f24'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='a73c68fa-de22-43da-ba15-75768fa55b3b'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='77e54ff2-8241-4d18-ba9a-b3d73b14c8dc'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='3e592232-e569-465e-be77-b8912593d739'></a>

BLE class BLEDevice Class BLEService Class

<a id='e30b203c-d266-46c3-98c7-008c9820b127'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='2a22c9d3-7328-47e1-abf9-cc9076084943'></a>

4/9

<!-- PAGE BREAK -->

<a id='890f8c31-d1a6-44f2-9a18-60509ed04649'></a>

12/4/25, 2:51 PM

<a id='49e2e818-e982-4a34-932b-16ed5e5aefc1'></a>

ArduinoBLE | Arduino Documentation

<a id='294c1e09-cf8f-4309-910e-caff9ed019bd'></a>

ARDUINODOCS

<a id='15b5005a-94ae-4ad1-8af7-5fb6ec4a8223'></a>

Used to enable the services board provides or interact with services a remote board
provides.

<a id='6fc835a9-5b96-4b84-ab13-64b0cf0ea1ec'></a>

BLEService()
Create a new Bluetooth® Low Energy service.

### Syntax
```
BLEService(uuid)
```

### Parameters

uuid: 16-bit or 128-bit UUID in String format

### Returns

New BLEService with the specified UUID

### Example
```
BLEService ledService("19B10000-E8F2-537E-4F6C-D16
```

<a id='81e452f3-9ba2-45bc-873e-fd3e66f84004'></a>

### bleService.uuid()
Query the UUID of the specified BLEService.

## Syntax
```
1 bleService.uuid()
```

## Parameters
None

## Returns
UUID of the Bluetooth® Low Energy service as a **String**.

## Example

<a id='62b934b0-595f-43da-992f-400afda462e7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='f0a4ebbb-8b2a-4799-b824-8134ca7e1aff'></a>

5/9

<!-- PAGE BREAK -->

<a id='63c7d4c0-43dc-4d42-9259-9fe10caa074f'></a>

12/4/25, 2:51 PM

<a id='c4183200-a30e-472c-b90d-b809a9ba6be1'></a>

ArduinoBLE | Arduino Documentation

<a id='15d166ee-a950-4e38-be19-4845b13dede9'></a>

ARDUINODOCS

<a id='70e8e135-4343-4d94-87a4-dbe7be86f0b0'></a>

1 BLEService ledService("19B10000-E8F2-537E-4F6C-D16
2
3
4 Serial.print("LED service UUID = ");
5 Serial.println(ledService.uuid());

<a id='89240c9d-3664-48d9-ba81-ccfb43ed141f'></a>

## bleService.addCharacteristic()
Add a BLECharacteristic to the Bluetooth® Low Energy service.

### Syntax
```
bleService.addCharacteristic(bleCharacteristic)
```

### Parameters
None

### Returns
Nothing

### Example
```
BLEService ledService("19B10000-E8F2-537E-4F6C-D1

// Bluetooth® Low Energy LED Switch Characteristi
BLECharacteristic switchCharacteristic ("19B10001-




// add the characteristic to the service
ledService.addCharacteristic(switchCharacteristic
```

<a id='f06d2dc8-885f-4131-b131-9b502abd88ac'></a>

bleService.characteristicCount()
Query the number of characteristics discovered for the Bluetooth®
Low Energy service.

<a id='672aa3c1-67ba-4e69-b317-a63a202063da'></a>

Syntax

```
1 bleService.characteristicCount()
```

<a id='171a2820-8adc-4d1d-a652-50a5b1c4a16d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='0cbf0d3c-de86-4ea8-82de-fef668555946'></a>

6/9

<!-- PAGE BREAK -->

<a id='32ffc04a-0c27-4d61-ac19-992a7b2f12b4'></a>

12/4/25, 2:51 PM

<a id='03a9d16c-444d-4646-9724-b7760f91cc37'></a>

ArduinoBLE | Arduino Documentation

<a id='4b32ba38-0848-45c7-8951-18a0c1d0dff9'></a>

ARDUINODOCS

<a id='38e77556-1c75-4d45-87d0-85b6a7a4e367'></a>

### Parameters
None

<a id='afdf15b8-b6e8-4248-b485-ab7bd44be437'></a>

### Returns

The **number of characteristics** discovered for the Bluetooth® Low Energy service.

<a id='7cab91bb-e05c-42e5-86a8-888c53ddabc7'></a>

Example

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy...");
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
14 if (peripheral) {
15   // ...
16
17   Serial.println("Connecting ...");
18
19   if (peripheral.connect()) {
20     Serial.println("Connected");
21   } else {
22     Serial.println("Failed to connect!");
23     return;
24   }
25 }
26
27 // discover peripheral attributes
28 Serial.println("Discovering attributes...");
```

<a id='5679e312-610f-488e-98ac-15afc87ec234'></a>

√ bleService.hasCharacteristic()
Query if the Bluetooth® Low Energy service has a particular
characteristic.

<a id='51986cbd-127d-4bfa-8261-e4a8d1a7abd2'></a>

## Syntax

```
bleservice.hasCharacteristic(uuid)
bleservice.hasCharacteristic(uuid, index)
```

<a id='bc93d281-28ed-4234-bde5-a8d885ce137e'></a>

Parameters

<a id='edacbd4b-4067-483a-b5be-0053551993ad'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='ee36547e-2d36-49a6-b22b-45ebc18f9e13'></a>

7/9

<!-- PAGE BREAK -->

<a id='60cc001d-8311-4ecb-b380-9f9b06b9a9be'></a>

12/4/25, 2:51 PM

<a id='a291cb01-cca6-4ebf-93f5-c483f240a391'></a>

ArduinoBLE | Arduino Documentation

<a id='841149bf-51ca-4f9f-a4c3-8593dbbf1766'></a>

ARDUINODOCS

<a id='505b4c7f-376f-420a-9245-0aff4749beda'></a>

___

<a id='c6047601-724b-4e3b-9bc6-bcc4dc078f7d'></a>

index: optional, index of characteristic to check if the device provides more than on. Defaults to 0, if not provided.

<a id='e35d10c2-f7cc-4eb8-87f5-30050ca29314'></a>

## Returns

**true**, if the service provides the characteristic,
**false** otherwise.

<a id='5c513e8f-6b8e-4d7a-ac0b-2b7c9946fef2'></a>

Example

```
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

  // discover peripheral attributes
  Serial.println("Discovering attributes ...");
  // ... (rest of code is cut off)
```

<a id='4abffbc8-e710-4186-af77-b468aeca8e46'></a>

- bleService.characteristic()
  Get a BLECharacteristic representing a Bluetooth® Low Energy characteristic the service provides.

<a id='9209d578-5c61-4a6b-ba91-4e01aadda733'></a>

Syntax

```
1 bleService.characteristic(index)
2 bleService.characteristic(uuid)
3 bleService.characteristic(uuid, index)
```

<a id='1dce9e07-6213-49e7-9b9f-94bd630cffd4'></a>

Parameters

<a id='2986fae7-bd9b-4aae-822d-2d785c5b1448'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='58a618c1-2951-4bda-8a1d-f810b451cbfc'></a>

8/9

<!-- PAGE BREAK -->

<a id='e490e4c3-29ae-4e8b-aaf2-1983c458e4c4'></a>

12/4/25, 2:51 PM

<a id='27694a78-e806-4670-8d78-8403f7252240'></a>

ArduinoBLE | Arduino Documentation

<a id='259fde2c-d447-4065-983c-b6ccdc7cad85'></a>

ARDUINODOCS

<a id='b085d94b-e9d0-4507-b404-3330e198f9cf'></a>

## Returns
BLECharacteristic for provided parameters

## Example
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
17   Serial.println("Connecting ...");
18
19   if (peripheral.connect()) {
20     Serial.println("Connected");
21   } else {
22     Serial.println("Failed to connect!");
23     return;
24   }
25
26   // discover peripheral attributes
27   Serial.println("Discovering attributes...");
```

<a id='b08a0186-3bea-4c37-8a61-87c1a39ea511'></a>

Was this article helpful?
---
[Thumbs up icon] [Thumbs down icon]

<a id='9bee1561-bcee-4231-abfd-39b2c99b4ee5'></a>

## Connect and Contribute

---

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='872c7539-22dc-4c0f-b909-ec48d7193f86'></a>

© 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='617a3afd-ffc1-4b60-ad73-d3d01162ee8d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLEService-library.html

<a id='d5fa02bd-29c3-4cec-9b45-a9d0fc37bcba'></a>

9/9