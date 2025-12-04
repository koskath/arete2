<a id='d2edda40-bbae-48ca-9dd1-2936e3eb1a65'></a>

12/4/25, 2:49 PM

<a id='37aa6aec-b087-45d9-bd80-94bded749fd8'></a>

ArduinoBLE | Arduino Documentation

<a id='8134b098-3beb-4613-af08-cf934a3e9473'></a>

ARDUINODOCS

<a id='0138df83-7625-4730-b233-c67aabba4ef4'></a>

Search on Docs /

<a id='a4462f9a-01a9-4eb6-97b6-f49f854fa7a1'></a>

← Go Back

## Library

<a id='e3b9fda0-0c22-4beb-9f55-9375b96ce46f'></a>

Recents viewed

<a id='b0602277-c118-46e3-af74-e575c979b66d'></a>

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

<a id='760c3196-e5c4-46d8-ab2d-9bdb741c55ff'></a>

Home / Programming / Library / ArduinoBLE

<a id='1f2e8980-f883-4667-ad99-d73fd9e8b22e'></a>

### COMMUNICATION
# ArduinoBLE

ARDUINO GNU Lesser General Public License v2.1 V1.4.1 Arduino 24/07/2025

Arduino <info@arduino.cc>
https://www.arduino.cc/en/Re... info@arduino.cc

Enables Bluetooth® Low Energy connectivity on the Arduino MKR WiFi 1010, Arduino UNO WiFi Rev2, Arduino Nano 33 IoT, Arduino Nano 33 BLE, Nicla Sense ME and UNO R4 WiFi.

<a id='d4341be7-d647-42b9-8ca0-7a47dd4f392e'></a>

This library supports creating a Bluetooth® Low Energy peripheral &
central mode.

<a id='1432ae16-071f-4308-9bcc-dac135ded397'></a>

GO TO REPOSITORY

<a id='619adb39-e92c-430d-91cd-4afb7ea5583e'></a>

Usage/Examples Compatibility Releases

This library supports all the Arduino boards that have the hardware enabled for Bluetooth® Low Energy and Bluetooth® 4.0 and above; these include Nano 33 BLE, Arduino NANO 33 IoT, Uno WiFi Rev2, MKR WiFi 1010, Nicla Sense ME.

<a id='c15b4ad9-28ac-402b-8e53-c905d05be89b'></a>

To use this library

```c
#include <ArduinoBLE.h>
```

<a id='034d2b5d-45bd-49a7-9645-36631c8c1ad1'></a>

A quick introduction to BLE

Bluetooth® 4.0 includes both traditional Bluetooth®, now labeled "Bluetooth® Classic", and the Bluetooth® Low Energy. Bluetooth® Low Energy is optimized for low power use at low data rates, and was designed to operate from simple lithium coin cell batteries.

<a id='4eb04877-65d7-40bb-8ddb-75fd72f5c6a0'></a>

Unlike standard Bluetooth® communication basically based on an an asynchronous serial connection (UART) a Bluetooth® LE radio acts like a community bulletin board. The computers that connect to it are like community members that read the bulletin board. Each radio acts as either the bulletin board or the reader. If your radio is a bulletin board (called a peripheral device in Bluetooth® LE parlance) it posts data for all radios in the community to read. If your radio is a reader (called a central device in Bluetooth LE terms) it reads from any of the bulletin boards (peripheral devices) that have information about which it cares. You can also think of peripheral devices as the servers in a client-server transaction, because they contain the information that reader radios ask for. Similarly, central devices are the clients of the Bluetooth® LE world because they read information available from the peripherals.

<a id='77be8dc8-d5fe-4e74-86c9-5e80de74e84b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='1c85ea63-b86a-40bc-9755-bfcf9688d45b'></a>

Help

<a id='e481b41b-a56d-4e72-b0bd-d5d258b6c5c7'></a>

1/26

<a id='c2efce69-07d6-4878-9c81-27b668648399'></a>

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

<a id='d12311f4-fcf7-464a-8854-5cff88bc711d'></a>

12/4/25, 2:49 PM

<a id='a8fae72f-1e1a-469b-9ec1-cc64752a02ac'></a>

ArduinoBLE | Arduino Documentation

<a id='0e45a1bb-ab89-4617-a33d-1a64eab7ef34'></a>

ARDUINODOCS

<a id='3ddaf491-e15f-4f13-aa8c-b5af53aac0f7'></a>

<::Diagram: Bluetooth LE Peripheral Device with Services and Characteristics, interacting with Central Devices.The diagram shows a large rectangular box labeled "Peripheral Device". Inside this box, there are five smaller rectangular boxes representing services, arranged in two rows.The top row contains:
- "Service 1" with three nested rectangles labeled "Characteristic".
- "Service 2" with two nested rectangles labeled "Characteristic".
- "Service 3" with three nested rectangles labeled "Characteristic".The bottom row contains:
- "Service 4" with two nested rectangles labeled "Characteristic".
- "Service 5" with three nested rectangles labeled "Characteristic".Outside the "Peripheral Device" box, there are three stick figures, each labeled "Central device".
- One "Central device" is on the left, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is on the right, connected to the "Peripheral Device" by a dashed line.
- One "Central device" is at the bottom, connected to the "Peripheral Device" by a dashed line.::>Think of a Bluetooth® LE peripheral device as a bulletin board and central devices as viewers of the board. Central devices view the services, get the data, then move on. Each transaction is quick (a few milliseconds), so multiple central devices can get data from one peripheral.

<a id='d22d5cb8-2d1f-4a86-8d23-5a17c7c543ef'></a>

The information presented by a peripheral is structured as **services**, each of which is subdivided into **characteristics**. You can think of services as the notices on a bulletin board, and characteristics as the individual paragraphs of those notices. If you're a peripheral device, you just update each service characteristic when it needs updating and don't worry about whether the central devices read them or not. If you're a central device, you connect to the peripheral then read the boxes you want. If a given characteristic is readable and writable, then the peripheral and central can both change it.

<a id='ff34c634-d8c4-410c-a94f-e911329d7ecb'></a>

## Notify

The Bluetooth® LE specification includes a mechanism known as **notify** that lets you know when data's changed. When notify on a characteristic is enabled and the sender writes to it, the new value is automatically sent to the receiver, without the receiver explicitly issuing a read command. This is commonly used for streaming data such as accelerometer or other sensor readings. There's a variation on this specification called **indicate** which works similarly, but in the indicate specification, the reader sends an acknowledgment of the pushed data.

<a id='0915fdf2-6934-4dbb-a5c4-eb8f95764ca2'></a>

The client-server structure of Bluetooth® LE, combined with the notify characteristic, is generally called a **publish-and-subscribe model**.

<a id='b8b8fbfa-f5c9-41bb-ac42-bc735405ecb5'></a>

# Update a characteristic
Your peripheral should update characteristics when there's a significant change to them. For example, when a switch changes from off to on, update its characteristic. When an analog sensor changes by a significant amount, update its characteristic.

<a id='69de824d-2c17-4cc0-938d-18ffd6783ed4'></a>

Just as with writing to a characteristic, you could update your
characteristics on a regular interval. but this wastes processing power and

<a id='d5a6457d-4fd1-41b4-a7ea-bfbead67505c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='86c3df77-56e1-4e93-beba-2f68cae05e81'></a>

2/26

<!-- PAGE BREAK -->

<a id='d640c32f-de61-4eb8-a142-56eee0aaa915'></a>

12/4/25, 2:49 PM

<a id='2fb1b9b3-911e-4134-82d1-5ddb856c6a44'></a>

ArduinoBLE | Arduino Documentation

<a id='ac4f5d41-3c54-441e-b42d-82ed1e8af3e8'></a>

ARDUINODOCS

<a id='7c724c10-00dc-4c54-ba29-159a2484e7b6'></a>

## Central and Peripheral Devices

**Central** devices are **clients**. They read and write data from peripheral devices. **Peripheral** devices are **servers**. They provide data from sensors as readable characteristics, and provide read/writable characteristics to control actuators like motors, lights, and so forth.

<a id='a87588cd-0eff-4d5a-98bb-3b9e368ad247'></a>

# Services, characteristics, and UUIDs
A Bluetooth® Low Energy peripheral will provide **services**, which in turn provide **characteristics**. You can define your own services, or use standard services (see section 3.4 in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/)).

<a id='4a5d6907-be56-46ae-85a8-e682da2be71e'></a>

Services are identified by unique numbers known as UUIDs. You know about UUIDs from other contexts. Standard services have a 16-bit UUID and custom services have a 128-bit UUID. The ability to define services and characteristics depends on the radio you're using and its firmware.

<a id='2e3a94cb-7b36-4fee-bf84-9eee4cfee2ec'></a>

# Service design patterns

A characteristic value can be up to 512 bytes long. This is a key constraint in designing services. Given this limit, you should consider how best to store data about your sensors and actuators most effectively for your application. The simplest design pattern is to store one sensor or actuator value per characteristic, in ASCII encoded values.

<a id='3adb809d-169f-4608-8ca1-4b6a82ef3b76'></a>

<table id="2-1">
<tr><td id="2-2">Characteristic</td><td id="2-3">Value</td></tr>
<tr><td id="2-4">Accelerometer X</td><td id="2-5">200</td></tr>
<tr><td id="2-6">Accelerometer Y</td><td id="2-7">134</td></tr>
<tr><td id="2-8">Accelerometer Z</td><td id="2-9">150</td></tr>
</table>

<a id='4b4b27bd-aa7b-4630-85ec-976239505e26'></a>

This is also the most expensive in memory terms, and would take the
longest to read. But it's the simplest for development and debugging.

<a id='9c01df57-d39c-40eb-89b6-a85f75439534'></a>

You could also combine readings into a single characteristic, when a given sensor or actuator has multiple values associated with it.

<a id='f6e51645-a833-47de-9807-70bb6f994e45'></a>

<table id="2-a">
<tr><td id="2-b">Characteristic</td><td id="2-c">Value</td></tr>
<tr><td id="2-d">Motor Speed, Direction</td><td id="2-e">150,1</td></tr>
<tr><td id="2-f">Accelerometer X, Y, Z</td><td id="2-g">200,133,150</td></tr>
</table>

<a id='47d6d850-893c-4b7a-a39d-b9b7e52a7da3'></a>

This is more efficient, but you need to be careful not to exceed the 512-
byte limit. The accelerometer characteristic above, for example, takes 11
bytes as an ASCII-encoded string.

<a id='b8b884b2-0c97-4984-b1a9-7bfa163deba0'></a>

Read/write/notify/indicate

<a id='f31a7c8c-449a-433e-9ba1-bfe6e2fb2db8'></a>

There are 4 things a central device can do with a characteristic:

<a id='da51b1bd-352d-47d6-951a-b98f585c8d87'></a>

**Read:** ask the peripheral to send back the current value of the characteristic. Often used for characteristics that don't change very

<a id='0c74cd62-b5f1-4a03-9d8b-a7791e3b07ae'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='9f9e401f-df58-41e0-a5d8-6daa784f4ba9'></a>

3/26

<a id='f09eb424-3b80-460a-97d6-ccc67cb504b1'></a>



<!-- PAGE BREAK -->

<a id='4ed0ce9f-3185-4cb0-8ae4-1a4993bc7ca8'></a>

12/4/25, 2:49 PM

<a id='7fba2ad5-bd69-40da-817c-24e4a3bbb818'></a>

ArduinoBLE | Arduino Documentation

<a id='72d27ed7-6da5-479c-8fda-63ad50f351fe'></a>

ARDUINODOCS

<a id='97609240-dc6a-4886-8a33-9415c7c60603'></a>

Write: modify the value of the characteristic. Often used for things that are like commands, for example telling the peripheral to turn a motor on or off.

<a id='01883dbe-bf72-45ae-86cf-ca33c5617548'></a>

Indicate and **Notify**: ask the peripheral to continuously send updated values of the characteristic, without the central having to constantly ask for it.

<a id='0391cbd4-462e-49b3-a7d2-d041d0123d06'></a>

# Advertising and GAP

BLE devices let other devices know that they exist by advertising using the **General Advertising Profile (GAP)**. Advertising packets can contain a device name, some other information, and also a list of the services it provides.

<a id='4e55fa3b-d965-4c2f-af0f-9de899a74fe1'></a>

Advertising packets have a limited size. You will only be able to fit a single 128-bit service UUID in the packet. Make sure the device name is not too long, or you won't even be able to fit that.

<a id='5f395aa2-53fd-4301-906f-a88ba434b853'></a>

You can provide additional services that are not advertised. Central
devices will learn about these through the connection/bonding process.
Non-advertised services cannot be used to discover devices, though.
Sometimes this is not an issue. For example, you may have a custom
peripheral device with a custom service, but in your central device app
you may know that it also provides the Battery Service and other services.

<a id='39e6f555-d0fd-4815-a9ed-5a5a3a20d7c4'></a>

GATT

The Bluetooth LE protocol operates on multiple layers. **General Attribute Profile (GATT)** is the layer that defines services and characteristics and enables read/write/notify/indicate operations on them. When reading more about GATT, you may encounter GATT concepts of a "server" and "client". These don't always correspond to central and peripherals. In most cases, though, the peripheral is the GATT server (since it provides the services and characteristics), while the central is the GATT client.

<a id='776031e9-066c-4cfd-a74a-407d45ba657f'></a>

# Library structure

As the library enables multiple types of functionality, there are a number of different classes.

<a id='9a258263-2eab-4441-9f11-70fbc7956721'></a>

`BLE` used to enable the Bluetooth® Low Energy module.
`BLEDevice` used to get information about the devices connected or discovered while scanning.
`BLEService` used to enable the services board provides or interact with services a remote board provides.
`BLECharacteristic` used to enable the characteristics board offers in a service or interact with characteristics a remote board provides.
`BLEDescriptor` used to describe a characteristic the board offers.

<a id='ed68171c-5fb5-4e30-afe5-2f5b437afa99'></a>

BLE class BLEDevice Class BLEService Class

<a id='f3fea811-6b3c-4acc-a3bd-e65c62282ec8'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='3f0d6241-b169-417b-a00b-28fb54f91ffb'></a>

4/26

<!-- PAGE BREAK -->

<a id='75e2eddc-88b8-49b0-85db-499716f0b4a6'></a>

12/4/25, 2:49 PM

<a id='599b2167-4b3f-4435-8154-7753a73d65ee'></a>

ArduinoBLE | Arduino Documentation

<a id='3c6e70c3-ef90-4f20-89d0-1b9d41459fe8'></a>

ARDUINODOCS

<a id='12bf651d-11b1-412a-8406-cd02919728a0'></a>

<::An empty rectangular box
: figure::>

<a id='aa05fa40-d081-4414-96ba-a94246a0160a'></a>

Used to enable the Bluetooth® Low Energy module.

<a id='bb307528-aaf2-4e69-aa05-05f2346d2b26'></a>

## BLE.begin()
Initializes the Bluetooth® Low Energy device.

### Syntax
```
BLE.begin()
```

### Parameters
None

### Returns
1 on success
0 on failure

### Example
```c
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy");
  while (1);
}
```

<a id='212cb315-620d-4285-8293-99caf94ee258'></a>

### BLE.end()
Stops the Bluetooth® Low Energy device.

### Syntax
```
1 BLE.end()
```

### Parameters
None

### Returns
Nothing

<a id='122647de-d672-43e9-a68c-3bce5dd62b3b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='0da38d62-c20d-40ed-ac06-f8ff3b968c5a'></a>

5/26

<!-- PAGE BREAK -->

<a id='801cc123-80cd-4b08-9cf6-9ca0d6653d03'></a>

12/4/25, 2:49 PM

<a id='3f542e9d-4ebe-4235-ac7a-5209d4fa39a8'></a>

ArduinoBLE | Arduino Documentation

<a id='6b109459-dfca-4474-a05c-c61eb68bca4c'></a>

ARDUINODOCS

<a id='5489ac3d-7713-4924-bc14-ac081c2f1f4c'></a>



<a id='9941bf8f-bbdc-44eb-846a-6d1097918ed3'></a>

## Syntax

```
1 BLE.setEventHandler(eventType, callback)
```

<a id='69682f7f-b5b5-4b12-b615-173a42fc5259'></a>

## Parameters

**eventType**: event type (BLEConnected, BLEDisconnected)
**callback**: function to call when event occurs

<a id='fdf47bbf-74bf-41d8-a347-f52aff4dad66'></a>

Returns

Nothing.

<a id='4b1f6ced-d8c9-4416-a8f9-a992b9dea1ad'></a>

Example

```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4 
5   while (1);
6 }
7 
8 // ...
9 
10 // assign event handlers for connected, disconnected
11 BLE.setEventHandler(BLEConnected, blePeripheralConnectHandler);
12 BLE.setEventHandler(BLEDisconnected, blePeripheralDisconnectHandler);
13 
14 
15 
16 void blePeripheralConnectHandler(BLEDevice central) {
17   // central connected event handler
18   Serial.print("Connected event, central: ");
19   Serial.println(central.address());
20 }
21 
22 void blePeripheralDisconnectHandler(BLEDevice central) {
23   // central disconnected event handler
24   Serial.print("Disconnected event, central: ");
25   Serial.println(central.address());
26 }
```

<a id='3a0a3094-1614-451d-a002-05f71d57f7b0'></a>

v BLE.connected()
Query if another Bluetooth® Low Energy device is connected

<a id='b0ef517b-4e55-422b-a917-662229558701'></a>

Syntax

<a id='49725903-be6a-40c0-b77f-9104ef7d53cb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='3a12b44b-af76-40ab-a1a4-52ea2f103ed2'></a>

7/26

<!-- PAGE BREAK -->

<a id='876a9fbd-d5a7-4361-854f-de587cdbbf59'></a>

12/4/25, 2:49 PM

<a id='cb23d359-a7ba-40fe-a0aa-e4d836108923'></a>

ArduinoBLE | Arduino Documentation

<a id='a644278f-8099-4869-bd65-0b9e1c70534a'></a>

ARDUINODOCS

<a id='1916ec78-03c2-4410-b301-8096c60b2737'></a>

[Empty Field]

<a id='2a975653-3edf-4f62-93ff-7d632739be76'></a>

1 BLE.connected()

<a id='58d02138-342e-4540-b267-0f1930f46117'></a>

Parameters

None

<a id='39ecd40b-be17-44d3-a2f0-aff093387c97'></a>

## Returns

**true** if another Bluetooth® Low Energy device is connected, otherwise **false**.

<a id='8d1b1f84-ecf1-45fd-b277-3fcea1f2deac'></a>

Example

```
1 // while the central is still connected to periphe
2 while (BLE.connected()) {
3 
4     // ...
5 }
```

<a id='2247ab1d-4ca0-4b34-9ca3-70bb4d2271b1'></a>

## BLE.disconnect()
Disconnect any Bluetooth® Low Energy devices that are connected

### Syntax
```
1 BLE.disconnect()
```

### Parameters
None

### Returns
**true** if any Bluetooth® Low Energy device that was previously connected was disconnected,
otherwise **false**.

<a id='7582058f-8480-41ca-b874-5c1cc55c993c'></a>

Example

____________________________________________________________________________________________________

<a id='caf558d9-9dbb-42a5-ad0c-b0584db3da61'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='7b2c1bfe-2c64-4864-92ef-9293b0043512'></a>

8/26

<!-- PAGE BREAK -->

<a id='30870471-9be1-4334-b0a1-99eda3096e9e'></a>

12/4/25, 2:49 PM

<a id='521d9966-7b04-4463-a3de-fc0d5adc3f02'></a>

ArduinoBLE | Arduino Documentation

<a id='c4c0e739-fe90-487b-b847-cddcfd601534'></a>

ARDUINODOCS

<a id='f07b6223-4682-4811-a48b-df60c789cef0'></a>

[Empty input field]

<a id='eae402e1-b86d-4608-bbfd-9c96cafd1c48'></a>

1 if (BLE.connected()) {
2   BLE.disconnect();
3 }

<a id='fb62a011-dc6d-4420-977d-6bb6fdcf9489'></a>

v BLE.address()
Query the Bluetooth® address of the Bluetooth® Low Energy device.

<a id='b4a8eefe-081e-46f2-ac44-485b865c7225'></a>

## Syntax

```
1 BLE.address()
```

<a id='36fcaa4a-5fd9-4afb-baec-8811f758d825'></a>

Parameters

None

<a id='3bc5dd31-ceb9-44b6-869f-96a5fb91dc16'></a>

## Returns

The **Bluetooth® address** of the Bluetooth® Low Energy device (as a String).

<a id='c99af429-863b-49a1-b44c-da6c7831cd62'></a>

Example

```
1 String address = BLE.address();
2
3 Serial.print("Local address is: ");
4 Serial.println(address);
```

<a id='8422799f-9af9-4641-8a22-d41470f7d703'></a>

√ BLE.rssi()

Query the RSSI (Received signal strength indication) of the connected Bluetooth® Low Energy device.

# Syntax

```
1 BLE.rssi()
```

<a id='66a9366f-74ab-47a7-8816-504f941bd8d3'></a>

Parameters

<a id='cefa9af9-aead-4289-9dca-3f2747a08053'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='5904297e-f721-4490-bbf4-2e4d23f5c99d'></a>

9/26

<!-- PAGE BREAK -->

<a id='c570851c-d85a-4bdf-81c4-cd767881632c'></a>

12/4/25, 2:49 PM

<a id='42fb27c0-c051-476f-b969-18d9f77dcae5'></a>

ArduinoBLE | Arduino Documentation

<a id='9c0f4e88-ce86-4538-8636-a19a2aaeec68'></a>

ARDUINODOCS

<a id='7554cb30-a6c0-4e1a-aadb-882f889bbb36'></a>

An empty input field.

<a id='57610e10-f63f-484b-8f6b-e640d4b9a765'></a>

## Returns
The **RSSI** of the connected Bluetooth® Low Energy device, 127 if no Bluetooth® Low Energy device is connected.

<a id='434c716e-db26-4c4a-a759-ff3b0f72b49b'></a>

# Example

```
1 if (BLE.connected()) {
2    Serial.print("RSSI = ");
3    Serial.println(BLE.rssi());
4 }
```

<a id='1b8f30d5-6b38-4a0b-8728-b9cafeb24b5c'></a>

BLE.setAdvertisedServiceUuid()
Set the advertised service UUID used when advertising.

# Syntax

```
1 BLE.setAdvertisedServiceUuid(uuid)
```

<a id='3f98910a-44a2-4fc0-9cbb-8a28c4c73e88'></a>

## Parameters

**uuid**: 16-bit or 128-bit Bluetooth® Low Energy UUID in **String** format

<a id='d468c20b-2ada-48fc-996f-dc0a6d1aef42'></a>

Returns
Nothing

<a id='14ca31eb-19d5-480e-8174-cf8ec9589334'></a>

Example

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energy");
  while (1);
}

BLE.setAdvertisedServiceUuid("19B10000-E8F2-537");

// ...

// start advertising
BLE.advertise();
```

<a id='22f0f0dd-6df2-42d4-823e-2c9193232a0f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='97135ad1-3ac8-4070-b646-8b676cd803c5'></a>

10/26

<!-- PAGE BREAK -->

<a id='0427e091-00d7-4f07-917c-238ec73389b9'></a>

12/4/25, 2:49 PM

<a id='d4d8ba53-461d-4b9a-9113-c03fe5f989e2'></a>

ArduinoBLE | Arduino Documentation

<a id='c43d06a3-7071-411d-a4c4-83b6b23ef87c'></a>

ARDUINODOCS

<a id='15d009a9-6945-441b-adf9-7054dbdaf4d5'></a>

BLE.setAdvertisedService()
Set the advertised service UUID used when advertising to the value
of the BLEService provided.

<a id='acdce79a-0ead-4528-83ab-b7351eef6c6b'></a>

## Syntax

```
1 BLE.setAdvertisedService(bleService)
```

<a id='80ba4f5a-c9b0-4906-bb7d-83cab42edf54'></a>

Parameters

bleService: BLEService to use UUID from

<a id='cbcefd3e-b3c7-43d3-b9e1-4f06374ae52c'></a>

Returns

Nothing

<a id='71ccfded-30c5-42d7-ba0d-e3c36911f875'></a>

Example

```
1 BLEService ledService("19B10000-E8F2-537E-4F6C-D1
2 
3 // ...
4 
5 // begin initialization
6 if (!BLE.begin()) {
7   Serial.println("starting Bluetooth® Low Energ
8 
9   while (1);
10 }
11 
12 BLE.setAdvertisedService(ledService);
13 
14 // ...
15 
16 // start advertising
17 BLE.advertise();
```

<a id='5088fb9b-6339-43cc-9351-6bdb7ac3ad50'></a>

### BLE.setManufacturerData()
Set the manufacturer data value used when advertising.

### Syntax

```
1 BLE.setManufacturerData(data, length)
```

<a id='5ada2a73-72b0-41da-a84f-a8e36074137f'></a>

Parameters

<a id='a36ba6c6-a014-415b-ac53-21bfe493a1d7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='487d480d-c7b5-4cdd-8bc8-beecb99bf9fa'></a>

11/26

<!-- PAGE BREAK -->

<a id='cb09f4a7-64c0-4d54-ba7c-b83a88ed84f2'></a>

12/4/25, 2:49 PM

<a id='4270cdb9-75e8-4807-811c-3821f7358b91'></a>

ArduinoBLE | Arduino Documentation

<a id='716785b4-58cf-4639-b96b-006bfccffbd8'></a>

ARDUINODOCS

<a id='636d2f97-d12b-46b2-b6fe-6065f5d8c030'></a>

Set the appearance in the built in appearance characteristic. If not set, the value defaults to 0x0000.

### Syntax
```
BLE.setAppearance(appearance)
```

### Parameters
appearance: appearance value

### Returns
Nothing

### Example
```cpp
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ
4 while (1);
5 }
6 
7 BLE.setAppearance(0x8000);
8 
9 // ...
10 
11 // start advertising
12 BLE.advertise();
```

<a id='d2bd51dc-8a58-49e9-8304-b8940f54d051'></a>

BLE.addService()

<a id='81d33b0b-a126-49e2-b4e9-959e12159307'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='7a47e104-74f9-48ba-9e5b-805b6c7dc2b5'></a>

14/26

<!-- PAGE BREAK -->

<a id='e1b11806-0e98-49c0-a84b-5c8b1e9e165f'></a>

12/4/25, 2:49 PM

<a id='800bf829-ab48-44c1-8cb7-16dbdc61b7fb'></a>

ArduinoBLE | Arduino Documentation

<a id='95e47a89-7dfe-4494-aae6-dd47a4778685'></a>

ARDUINODOCS

<a id='bcddf7dc-0f94-49b4-a311-08ea7aa4b173'></a>

Add a BLEService to the set of services the Bluetooth® Low Energy device provides

## Syntax
```
BLE.addService(service)
```

## Parameters
service: BLEService to add

## Returns
Nothing

## Example
```
BLEService ledService("19B10000-E8F2-537E-4F6C-D1

// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energ
  while (1);
}
// ...
BLE.addService(ledService);
```

<a id='e3c26872-d5eb-4f51-9da8-d21b80061595'></a>

### BLE.advertise()

Start advertising.

## Syntax

```
1 BLE.advertise()
```

## Parameters

None

<a id='204a3574-38d0-415e-b533-c7f84c888bfd'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='0d60c841-b5cd-4a17-a4c4-a135d5d63f91'></a>

15/26

<a id='a9d50be3-cfa8-4a73-966a-aa333ada1d0f'></a>

15
16 // ...

<!-- PAGE BREAK -->

<a id='48e6f1d0-9eb2-41d2-8ca1-e517489cef43'></a>

12/4/25, 2:49 PM

<a id='d3466cb0-896c-4e1c-8fca-6333f8b583d3'></a>

ArduinoBLE | Arduino Documentation

<a id='f9be48f9-bbad-46fe-9389-dd9fe932f39a'></a>

ARDUINODOCS

<a id='5bd1fdbe-8f76-4f3c-9557-9d715d46110e'></a>



<a id='6efa1081-f85b-4212-8c1c-8612de71711b'></a>

Returns

1 on success,
0 on failure.

<a id='dc323bbf-50c6-44e9-8465-b41ec9f26679'></a>

Example

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energy");
4   while (1);
5 }
6 
7 // ...
8 BLE.advertise();
9 // ...
```

<a id='f5fd595c-e98b-4a42-aed9-68ce2ee85b73'></a>

BLE.stopAdvertise()
Stop advertising.

<a id='f2e8bc02-8b39-4daa-b176-657a1dc6a838'></a>

Syntax

```
1 BLE.stopAdvertise()
```

<a id='ed2e4560-73e0-4a32-a43f-9ffe111889c6'></a>

**Parameters**

None

<a id='533d05ab-90f8-46f9-89e8-d49729d71a8e'></a>

Returns

Nothing

<a id='ffc49552-c804-4f4f-aeb5-7a155e5cb8d1'></a>

**Example**

___

<a id='739f7777-e10c-40b7-8726-b18d7adffcf9'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='a0c7f467-0c52-4111-8516-d13d61cd851b'></a>

16/26

<!-- PAGE BREAK -->

<a id='e378eb63-bc6d-4af6-b1b3-7bfd470712f8'></a>

12/4/25, 2:49 PM

<a id='fc0b8636-e3c2-4b55-832a-b184084898d7'></a>

ArduinoBLE | Arduino Documentation

<a id='bc6e83ee-cabf-408d-b41d-1179e3c0b813'></a>

ARDUINODOCS

<a id='2f6ca508-3357-403a-a47e-e43e3b4d177e'></a>

An empty rectangular box.

<a id='de72cb4b-a4fb-4fae-a358-71058e9950ba'></a>

### Syntax

```
1 BLE.setAdvertisingInterval(advertisingInterval)
```

<a id='a78304a6-7037-4a4b-9ac7-ba023ce405c6'></a>

## Parameters

**advertisingInterval**: advertising interval in units of 0.625 ms

<a id='bce68962-b8b1-4859-85dd-ab92c9ab4240'></a>

Returns

<a id='99cd7ad4-549e-4083-bb27-a9ffd1b8038f'></a>

Nothing.

<a id='15805274-9e72-48cd-b4a8-7f003f1cd0d5'></a>

Example

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energ
  while (1);
}

// ...

BLE.setAdvertisingInterval(320); // 200 * 0.625
BLE.advertise();
```

<a id='f998d4b8-4cb0-47fd-9af3-bb98c857e539'></a>

BLE.setConnectionInterval()

<a id='6c641e39-6234-40e1-9cae-e5a047607bb7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='9ff76e12-6329-4ad4-877c-5479e182e5e8'></a>

18/26

<!-- PAGE BREAK -->

<a id='85541095-2679-443e-8a90-48d51e96508b'></a>

12/4/25, 2:49 PM

<a id='52669e7f-bb6d-4f01-8f22-d3a6e68af1f8'></a>

ArduinoBLE | Arduino Documentation

<a id='cc104fb8-4ebe-4d1e-b868-085f68b97f44'></a>

ARDUINODOCS

<a id='8b49ac5a-eab5-4410-a3c3-8b892d4f248f'></a>

Set if the device is connectable after advertising, defaults to **true**.

### Syntax

```
1 BLE.setConnectable(connectable)
```

<a id='33d76a8c-ad6f-4100-8603-2ee0b54ab5d6'></a>

# Parameters
true: the device will be connectable when advertising
false: the device will NOT be connectable when advertising

<a id='efa33b03-6594-421a-9d1d-86636e654481'></a>

Returns

Nothing.

<a id='29c4fe65-ea47-4eb0-a87d-b51d1f2b1a75'></a>

Example

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ
4 
5   while (1);
6 }
7 
8 // ...
9 
10 BLE.setConnectable(false); // make the device i
```

<a id='4427336f-cd82-42ff-a57e-1854f7351802'></a>

BLE.scan()
Start scanning for Bluetooth® Low Energy devices that are advertising.

## Syntax

```
1 BLE.scan()
2 BLE.scan(withDuplicates)
```

<a id='e67a037f-6bab-4d67-a750-3025cef0ac29'></a>

## Parameters

**withDuplicates**: optional, defaults to **false**. If **true**,
advertisements received more than once will not be filtered

<a id='3c7e5991-7378-440e-83f9-8619de5bd9e1'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='42494768-05fb-48d4-ae6a-01c40ddba371'></a>

20/26

<!-- PAGE BREAK -->

<a id='02229d94-5a83-4697-8c1b-a044ade242c1'></a>

12/4/25, 2:49 PM

<a id='4156d761-15c8-485f-9afb-8ae36d86aee0'></a>

ArduinoBLE | Arduino Documentation

<a id='dacd2ed9-7066-4d8c-84de-c19e360f092f'></a>

ARDUINODOCS

<a id='0a2d31c3-7acf-4861-a4d1-9dba8f521efd'></a>



<a id='668e26ee-2e6b-46bd-8c84-29c7b14e808a'></a>

```
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scanForAddress("aa:bb:cc:ee:dd:ff");
12 
13 
14 BLEDevice peripheral = BLE.available();
15 
16 if (peripheral) {
17   // ...
18 }
```

<a id='dc93a7ed-54cf-43d1-8dca-859d5c2e4cf4'></a>

√ BLE.scanForUuid()
Start scanning for Bluetooth® Low Energy devices that are advertising with a particular (service) UUID.

<a id='61055130-044d-4d74-a8ae-8faba5eabab4'></a>

## Syntax

```
1 BLE.scanForUuid(uuid)
2 BLE.scanForUuid(uuid, withDuplicates)
```

<a id='dc4e83c6-fd62-444b-adf6-a06d0d66c3c9'></a>

## Parameters

**uuid**: (service) UUID (as a **String**) to filter for
**withDuplicates**: optional, defaults to **false**. If **true**, advertisements received more than once will not be filtered.

<a id='119f02d4-b113-445d-8366-bfb84362c2db'></a>

# Returns

1 on success,
0 on failure.

<a id='7d5a5a28-aa67-48fa-a027-66eb4fe5f43e'></a>

Example

---

<a id='74a361cf-afdf-4797-9fb7-83f6af128be7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='6b0e518a-c9c6-4a58-b8ac-cc5adbd9a12e'></a>

23/26

<!-- PAGE BREAK -->

<a id='93e10077-1587-43df-9673-ee3c4bec3896'></a>

12/4/25, 2:49 PM

<a id='8678b430-64a0-42a0-b034-04f89a735907'></a>

ArduinoBLE | Arduino Documentation

<a id='62e41610-e1c5-4a94-a67b-4b99ab6b7710'></a>

ARDUINODOCS

<a id='663b2449-1d3a-4ce2-aa58-60e8791807ba'></a>

```c
1 // begin initialization
2 if (!BLE.begin()) {
3   Serial.println("starting Bluetooth® Low Energ");
4 
5   while (1);
6 }
7 
8 Serial.println("BLE Central scan");
9 
10 // start scanning for peripheral
11 BLE.scan();
12 
13 BLE.stopScan();
```

<a id='bd5d867e-0372-4a7b-87f0-4600a9569056'></a>

v BLE.available()
Query for a discovered Bluetooth® Low Energy device that was
found during scanning.

<a id='6d4afbc9-9ee7-4679-95ca-28cc59201b0f'></a>

## Syntax

```
1 BLE.available()
```

<a id='eb17ef9a-ee4c-4b78-a312-2cc16ebdbfdf'></a>

Parameters

Nothing

<a id='f6f849d0-c765-45be-9cae-62a45d3840a2'></a>

## Returns

**BLEDevice** representing the discovered device.

<a id='99bc4565-fbe5-44d6-8d5a-9d77ef34e730'></a>

Example

____________________________________________________________________________________________________

<a id='4d85c41a-d482-40db-a023-b40aa70456ec'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='992b8607-6615-406b-8dc8-d0680fb58264'></a>

25/26

<!-- PAGE BREAK -->

<a id='598e2eb4-fedc-43e0-a462-149924678bb4'></a>

12/4/25, 2:49 PM

<a id='a1bdc9be-9c24-4d72-9172-b04f59c6d041'></a>

ArduinoBLE | Arduino Documentation

<a id='87d0ca35-f8be-4131-af2b-11ea3b5597f8'></a>

ARDUINODOCS

<a id='d7e5a6d7-14c6-42dd-8967-6d2ec56bc5d4'></a>



<a id='6332eb83-17c5-40f0-9acd-ff5220340e47'></a>

```
// begin initialization
if (!BLE.begin()) {
  Serial.println("starting Bluetooth® Low Energ");
  while (1);
}

Serial.println("BLE Central scan");

// start scanning for peripheral
BLE.scan();

BLEDevice peripheral = BLE.available();

if (peripheral) {
  // ...
}
```

<a id='6790fd3c-1561-4292-8b89-e0cb6afc66f0'></a>

Was this article helpful?

---

option Like: [ ]
option Dislike: [ ]

<a id='71873b81-f1b8-45d4-8421-c6f6f8b2bcd4'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='f8cacc53-c4f2-41da-aa5f-1e0b6bbea715'></a>

 2025 Arduino

<a id='36cfbbdf-b6e6-46d1-819c-c3e2ea029e08'></a>

Terms Of Service Privacy Policy Security Cookie Settings

<a id='87b97e58-d420-422d-8b75-be84125218af'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='46a096c7-3076-4bba-baa5-abb893d3680b'></a>

26/26