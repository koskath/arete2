<a id='9ad25555-7674-4e88-9c78-709cb3db8995'></a>

<::logo: thinger.io
thinger.io
The logo features a hamburger menu icon to the left of the text "thinger.io", with the ".io" part enclosed in a gray square outline.:>

<a id='f8176f14-55b0-4de7-9366-14e59b9d9e93'></a>



<a id='9a3e8dac-bc2e-4082-8077-36734bf7bd5c'></a>

LPWAN DEVICES

<a id='34d9833d-5fc6-4696-b269-46191e80031d'></a>

<::A button with a GitHub Octocat icon, the text "Edit", and a dropdown arrow.
: figure::>

<a id='916997df-06b3-483f-a570-3a47ac5848b4'></a>

**SIGFOX**
0G Technology. LPWAN dedicated to Massive IoT.

<a id='7e798de1-db6e-4e1a-9ad8-a30018892392'></a>

<::logo: Sigfox
sigfox
The logo features a stylized butterfly or X-shape in shades of gray, accompanied by the word "sigfox" in black, lowercase letters.::>

<a id='6b8a9820-a601-4e56-92de-8617f4c56fde'></a>

## Introduction

<a id='deb76a64-edb5-4495-a5f6-81fc338cb051'></a>

Sigfox is a company founded in 2009 that builds wireless networks to connect low-energy objects such as electricity meters, smartwatches, and washing machines, which need to be continuously on and emitting small amounts of data. Sigfox employs a proprietary technology that enables communication using the Industrial, Scientific and Medical ISM radio band, which uses 868 MHz in Europe and 902 MHz in the US. It utilizes a wide-reaching signal that passes freely through solid objects, called "ultra-narrowband" and requires little energy, being termed "Low-power Wide-area network (LPWAN)". The network is based on a one-hop star topology and requires a mobile operator to carry the generated traffic. The signal can also be used to easily cover large areas and to reach underground objects.

<a id='ce1d4a94-cd1d-4298-8335-2ef2475b09de'></a>

Sigfox has partnered with a number of firms in the LPWAN industry, such as Texas Instruments and Silicon Labs. The ISM radio band supports bidirectional communication. The existing standard for Sigfox communications supports up to **140 uplink messages a day**, each of which can carry a payload of **12 Bytes** (Excluding message header and transmission information), and up to 4 downlink messages per day, each of which can carry a payload of 8 Bytes. For more details about Sigfox, please visit the Sigfox Developer Portal ↗.

<a id='2d847af0-d8ad-4400-9081-353ceb138e18'></a>

1

<!-- PAGE BREAK -->

<a id='0c908e79-25a9-4389-a368-367c6273b2eb'></a>

This documentation will describe how to integrate SigFox devices and their data into the Thinger.io Platform. In the first steps, we will review how to configure Thinger.io resources, and then, on the Sigfox side, we will configure the communication with the platform for pushing our sensor's data.

<a id='93dcede8-1232-4e5a-bd09-91b7c76419ae'></a>

# Integrating a Sigfox Device with Thinger.io

This process is carried out in two parts: on the one hand, the preparation of Thinger.io to receive data from Sigfox and, on the other hand, the configuration of the Sigfox cloud callback that will send the information to Thinger.io. During the next sections, we will explain both parts, starting with Thinger.io side steps:

<a id='8c97744e-b04d-4e77-b4cf-c68a6d16eef4'></a>

There are two ways to configure Thinger.io to work with Sigfox devices. The best option is by deploying the "Sigfox Plugin", which will manage the integration, providing advanced features such as device auto-provisioning (good to integrate large networks), Uplink/Downlink payload processing and device management, but this option is only available for subscribed developers. Freemium accounts can also make individual Sigfox device integration using the "HTTP device". Both ways are explained below:

<a id='ae93b8ab-e604-450d-a8b3-8af9f2b14b8d'></a>

**Advanced Integration (with Sigfox plugin)**

> SigFox Plugin

<a id='b5d2739f-0665-491e-bb43-f2d6768dd4e8'></a>

## Single Device Integration (without plugins)

When implementing little prototypes or maker projects using the free account, it is possible to integrate an individual device using the "HTTP device" that allows using almost every Thinger.io platform feature, including:

* Store data in buckets
* Show data in customizable dashboards
* Send endpoints to post data on emails, social networks or third parties

<a id='13cbda64-00d9-4e82-adbe-68b760634e3d'></a>

2

<!-- PAGE BREAK -->

<a id='23459c74-ea14-4146-a3e4-addad4a56b09'></a>

* Sigfox downlink processes to send configuration data to the device

<a id='96238bc3-9971-42f0-a403-2fcf9ca64949'></a>

␓ Payload data processing is only available using plugin integration

<a id='011c6b8b-abb6-41a2-87ac-d6f81c5cf1f3'></a>

To perform this integration, it is required to create a new HTTP device and configure its callback flows as it is explained in the HTTP devices section of this documentation:

<a id='1ec4be82-8b7d-4609-8f6c-2840e47b7224'></a>

<table id="2-1">
<tr><td id="2-2">HTTP DEVICES (right arrow)</td></tr>
</table>

<a id='d63a0572-a146-4dec-b3bd-fe728fa4aeb4'></a>

Once the new device has been created, Thinger.io will provide a REST API callback that can be used to configure the Sigfox cloud, as it is explained in the section below:

<a id='3be21c36-c0c5-4433-b48a-d5ba5055659b'></a>

# Sigfox Cloud Configuration

After making all the configurations that are required to get Thinger.io ready for receiving data, the next step is to configure the Sigfox Backend for pushing data to it, using our token identifier and the token we have generated.

<a id='7427fba5-a1a4-4bc1-bcb0-783c5c066028'></a>

# Creating Sigfox Callback

In this step, we will create a Sigfox callback that will push the information from our Sigfox device to our Thinger.io data bucket. In our example, a callback is just an endpoint that is called when the Sigfox device sends data over the network, so we will configure the callback to point to our data bucket.

<a id='bc0df201-d8f6-44bb-bdeb-f950bbd250b7'></a>

To create a callback in Sigfox:

1. Go to https://backend.sigfox.com and log in to the account. It is assumed that the device has already been registered with the platform.
2. Click on `Device Type` tab on the top, and then click on the desired device type name to configure. Alternatively, navigate to the `Device` tab and click on the `Device type` column of the device.
3. Click on `Callbacks` on left menu, and then create a new one.

<a id='a9c078a3-4906-451a-9481-1f1f557e48f4'></a>

3

<!-- PAGE BREAK -->

<a id='30a0597a-d78a-424a-b117-a50cba8c046a'></a>

In this step, select the option to create a `Custom Callback`, as there is a need to call an endpoint not directly supported by the Sigfox back-end.

<a id='f874b84e-51ca-49a0-90af-f8c2dd262125'></a>

sigfox

DEVICE DEVICE TYPE USER GROUP

<::icon: person::><::icon: A::><::icon: question mark::><::icon: refresh::>

<a id='d3c4f738-3205-4f69-a982-dcf1e325ab77'></a>

INFORMATION
LOCATION
ASSOCIATED DEVICES
DEVICES BEING TRANSFERRED
STATISTICS
EVENT CONFIGURATION
CALLBACKS

Device type 'SmartEverything' - New Callback

Create callbacks to connect Sigfox cloud to your server/platform
A callback is a custom http request containing your device(s) dati
aforesaid device(s) message is received by Sigfox cloud.

Custom callback
Creates a new callback from Sigfox cloud to your
You can create a full custom request (http methc

AWS IoT
AWS IoT is a managed cloud platform that lets cI
other devices. AWS IoT can support billions o
messages to AWS endpoints and to other device!

AWS Kinesis
Amazon Kinesis is a platform for streaming data
streaming data, and also providing the ability for

Microsoft Azure™ Event hub

https://backend.slgfox.com/devicetype/58f72ac99e93a17a4af23d0f/callbacks/new
Copyright © Sigfox-6.4.4

<a id='78a81585-e64c-4c9e-a477-9ae5e416994e'></a>

AWS IoT
AWS IoT is a managed cloud platform that lets connected devices easily and securely interact with cloud applications and other devices. AWS IoT can support billions of devices and trillions of messages, and can process and route those messages to AWS endpoints and to other devices reliably and securely.

<a id='f92d50d8-6586-4236-af42-3141b890ad9e'></a>

AWS Kinesis
Amazon Kinesis is a platform for streaming data on AWS, offering powerful services to make it easy to load and analyze streaming data, and also providing the ability for you to build custom streaming data applications for specialized needs.

<a id='2a377dc8-b55b-4ad5-a0a6-79616b4b1b5b'></a>

MICROSOFT AZURE EVENT HUB
https://backend.sigfox.com/devicetype/68f72ec89e93a17e4ef23d0f/callbacks/new Copyright © Sigfox - 6.4.6 - 257 - Terms and conditions / Cookie policy.

<a id='5ed3c2f9-8fb5-47d1-ace8-884bfea06d45'></a>

Then, we need to configure the callback to write to our data bucket. Here is the configuration. Details for each field are provided after this:

<a id='a49d9d7f-d139-4ab4-bb24-0c933c50e30c'></a>

4

<a id='fc20434e-f594-457f-8a8c-517974bd3f6d'></a>

a, along with other variables, sent to a given server/platform when the

<a id='5914a96b-8b76-4951-bbd9-d42ab04df785'></a>

own server. This is the "default" callback type.
id, content type, headers, etc).

<!-- PAGE BREAK -->

<a id='083d1f29-cedf-4af3-ad52-d6a9298ac83a'></a>

Type:
option DATA: [x]
option UPLINK: [x]

Channel:
option URL: [x]

Send duplicate: [ ]

Custom payload
config: temp::float:32:little-endian hum::float:32:little-endian

<a id='3e80f738-0a11-46b0-ac46-b493b36611f2'></a>

URL syntax: http://host/path?id={device}&time={time}&key1={var1}&key2={var2}...
Available variables: device, time, duplicate, snr, station, data, avgSnr, lat, lng, rssi, seqNumber
Custom variables: customData#temp, customData#hum
Url pattern https://api.thinger.io/v1/users/alvarolb/buckets/SmartEverything/data

<a id='31d1581f-1781-4c2c-b04a-067631c557da'></a>

Use HTTP Method option POST: [x]

Send SNI: [ ] (Server Name Indication) for SSL/TLS connections

Headers

<table><thead><tr><th>Authorization</th><th>Bearer eyJhbGciOiJIUzI1NilsInR5cCl6lkpXVCJ9.eyJqdGkiOiJTbWFydEV22</th></tr></thead><tbody><tr><td>header</td><td>value</td></tr></tbody></table>

<a id='6670a87f-8c4e-42c7-8313-412a22d24b01'></a>

Content type application/json
Body
{
"device": "{device}",
"snr": {snr},
"rssi": {rssi},
"station": "{station}",
"latitude": {lat},
"longitude": {lng},
"temperature": {customData#temp},
"humidity": {customData#hum}
}

<a id='baff2b34-96e0-4952-9edc-5d56a9f79e3f'></a>

The configuration in our example is:

1. `Type` is `DATA` with `UPLINK`, as we want to send our device data.
2. `Channel` is of type `URL`, as we will be calling an HTTP endpoint.
3. `Send duplicate` as disabled to avoid writing duplicate messages received by different base stations.
4. `Custom payload config` will completely depend on the payload sent by the device. In our case, our device will be sending the temperature and humidity as 32-bit floats, so we have configured the payload as `temp::float:32:little-endian hum::float:32:little-endian`, where we define the `temp` and `hum` parameters as 32-bit floats in little-endian. Notice that Sigfox only supports 12 bytes of payload per message, so it is a must to optimize this space, like sending temperature and humidity as integers if it is not required decimal accuracy. For example, this will work.

<a id='312c202b-1e6f-4614-84ad-6152918370d5'></a>

5

<!-- PAGE BREAK -->

<a id='6b19b32f-6ccc-4246-8630-cc5c215f3bb5'></a>

5. `Url pattern` must be configured according to the Thinger.io user ID and our bucket name.

*   The pattern should be like
    `https://api.thinger.io/v1/users/{user_id}/buckets/{bucket_id}/data`.
*   The `{user_id}` and `{bucket_id}` must be changed to match the account. For example, the final URL pattern will be
    `https://api.thinger.io/v1/users/alvarolb/buckets/SmartEverything/data`.
    Note that Sigfox variables can also be used to compose the URL; for instance, to store data from each device in a different bucket, a URL could be created:
    `https://api.thinger.io/v1/users/alvarolb/buckets/{device}/data`.
6. `HTTP Method` should be set to POST.
7. In `Headers` we must include an `Authorization` header with our device token in order to authenticate the bucket write request.
*   Header name should be `Authorization`
*   Header value should be `Bearer {access_token}`, where the `{access_token}` token is generated in the previous steps.
*   This is the example final header value. Note the space between `Bearer` and the token itself:

    ```
    Bearer
    eyJhbGci0iJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGki0iJTbWFydEV2ZX
    J5dGhpbmciLCJ1c3Ii0iJhbHZhcm9sYiJ9.0Qb48c_ToBiIVcC0dvXU2Kn5
    1mTnGLDcN44shVRzN1s
    ```
8. The final step is to configure the `Body` and its `Content type`. For content type, we will set `application/json` as the bucket can store arbitrary JSON data. The body will then contain all the information we want to store, formatted in JSON. In Sigfox, the body can be defined using available variables, which include those provided by the platform (such as device ID, link quality, or device location) and those defined by the payload configuration. In our case, we defined variables `temp`, and `hum`, that will be included with other Sigfox variables. For this example, the payload is:

<a id='3073ac0b-0b32-47c0-a3ac-d47a14e38d51'></a>

6

<!-- PAGE BREAK -->

<a id='f4371619-4a0a-4255-ba82-153989031fbb'></a>

```
{
  "device" : "{device}",
  "snr" : {snr},
  "rssi" : {rssi},
  "station": "{station}",
  "latitude": {lat},
  "longitude": {1ng},
  "temperature" : {customData#temp},
  "humidity" : {customData#hum}
}
```

<a id='1d25086b-3295-407c-b4b5-5678060dcd81'></a>

Notice that we are mixing Sigfox variables, like `{device}`, with our own custom data in the payload, like `{customData#temp}`. This body is then processed on every message reception, and the variables will be replaced with the current values. So, the server will receive a JSON payload with the device identifier, device temperature, humidity, coarse location (km accuracy), and signal quality.

<a id='3b88c0f5-8c28-4584-9698-e3451f0bf82f'></a>

After these steps, we should now have a callback completely configured to push data to our data bucket.

<a id='302e72f8-d0bf-410a-a2cc-0ef324eab4e5'></a>

# Programming Sigfox Devices

Now it is time to program our Sigfox Device that will be sending data to our buckets. In this case, we provide examples for the SmartEverything device and the Arduino MKRFOX1200.

<a id='b950d5f1-d456-4d78-8f25-5f4b0f584d93'></a>

# Arduino MKRFOX1200

Arduino MKRFOX1200 has been designed to offer a practical and cost-effective solution for makers seeking to add SigFox connectivity to their projects with minimal previous experience in networking. It is based on the Microchip SAMD21 and an ATA8520 SigFox module. Can run for over six months on 2 AA 1.5V batteries with typical usage. The design includes the ability to power the board using two 1.5V AA or AAA batteries or an external 5V.

<a id='3112407e-6674-4960-b862-b37bad4fbc56'></a>

7

<!-- PAGE BREAK -->

<a id='4ff911e9-b196-4d3b-9b08-4d6ed038c987'></a>

<::An overhead, slightly angled view of a black Arduino MKRFOX 1200 development board. The board features various electronic components, including integrated circuits (ICs), resistors, capacitors, and connectors. There are two long rows of pin headers on either side of the board, with some pins labeled A0, A1, A2, A3, A4, A5, A6, A7, AREF, DACB/I, and I/O. A micro-USB port is visible on one end, along with a two-pin screw terminal connector. Text visible on the board includes "MKRFOX", "1200", and "WINO.CC".
: figure::>

<a id='7b22f020-4669-48d1-9ead-500fbbc35aa2'></a>

## Initial Setup

To program this device, we will use the Arduino IDE. In this case, it is necessary to install or update the board toolchain, which can be done directly from the Boards Manager, searching for `mrk`, and selecting the Arduino SAMD Boards.

<a id='fdb8406f-8d2e-4227-b678-08511361f9a7'></a>

Boards Manager

Type All mkr

Arduino SAMD Boards (32-bits ARM Cortex-M0+) by Arduino version 1.6.15 INSTALLED
Boards included in this package:
Arduino/Genuino Zero, Arduino/Genuino MKR1000, Arduino MKRZero, Arduino MKRFox1200, Arduino MO Pro, Arduino MO, Arduino Tian, Adafruit Circuit Playground Express.
Online help
More info

Close

<a id='f591ded4-34c4-4c23-8aee-52e531ae7f17'></a>

8

<!-- PAGE BREAK -->

<a id='abc12495-7146-4906-9689-b73404657fb4'></a>

Install the `Arduino SigFox for MKRFox1200` library that is available from the Library Manager, and it is also **NECESSARY** to install the `Arduino Low Power` , and the `RTCZero` libraries.

<a id='89b26c5c-d9d4-4741-806e-b81d49a195e8'></a>

## Library Manager

Type: All Topic: All
sigfox

### Arduino SigFox for MKRFox1200 by Arduino
Helper library for MKRFox1200 board and ATAB8520E Sigfox module This library allows some high level operations on Sigfox module, to ease integration with existing projects
More info

Install

### SmartEverything SIGFOX LE51-868 by Mik Version 2.1.1 INSTALLED
Library code for the TELEIT LE51-868 a SIGFOX module
The LE51-868 S is a high performance certified Short Range to Long Range module designed to cover the 863-870 MHz band working with the Telit Proprietary protocol and acting as a SIGFOX gateway.
It has high value technical characteristics such as a -126dBm sensitivity, ultra-low power consumption and up to 15.5dBm of Output power.
It is very easy to integrate, with small form factor and acts as a long range communication module connecting directly to SIGFOX network
More info

Close

<a id='c2a4b37d-42b4-4388-8ea2-4bfcd173f7b5'></a>

After a successful installation, we can now select the Board in the Arduino IDE. Just select the Arduino MKRFOX12000. Select, as with any other Arduino board, the port where de device is connected.

<a id='6e515ab3-2ecb-433e-a1cc-8e6bfe10594e'></a>

Arduino SAMD (32-bits ARM Cortex-M0+) Boards
option Arduino/Genuino Zero (Programming Port): [ ]
option Arduino/Genuino Zero (Native USB Port): [ ]
option Arduino/Genuino MKR1000: [ ]
option Arduino MKRZero: [ ]
option Arduino MKRFox1200: [x]
option Adafruit Circuit Playground Express: [ ]
option Arduino MO Pro (Programming Port): [ ]
option Arduino MO Pro (Native USB Port): [ ]
option Arduino MO: [ ]
option Arduino Tian: [ ]

<a id='aa7bd441-bbdb-45e6-90ca-9b591bc9acf8'></a>

Check that everything is up and running by flashing this example, which will provide information about the module, like the board ID and PAC. This information is necessary for registering the device in Sigfox.

<a id='2665d7d6-dee4-46d2-bd48-360183a3763d'></a>

9

<!-- PAGE BREAK -->

<a id='1a55e575-9f64-44b8-a954-eddd49f3fba9'></a>

#include <SigFox.h>

<a id='3858d126-f243-4c51-ae8f-d8ef865f7dc0'></a>

void setup() {
  Serial.begin(9600);
}

<a id='dce69c13-9066-41ba-b390-9521427f1026'></a>

while(!Serial) {};

<a id='735a9936-ff27-4f9d-af45-f947cdf205f2'></a>

```c
if (!SigFox.begin()) {
    Serial.println("Shield error or not present!");
    return;
}
```

<a id='eac9b17a-20ed-4de7-9a87-8fdc9be13378'></a>

```
String version = SigFox.SigVersion();
String ID = SigFox.ID();
String PAC = SigFox.PAC();
```

<a id='45d912c5-2053-41d6-9001-a8ad19eb817d'></a>

// Display module information
Serial.println("MKRFox1200 Sigfox first configuration");
Serial.println("SigFox FW version " + version);
Serial.println("ID = " + ID);
Serial.println("PAC = " + PAC);

<a id='3c71095d-dd69-465a-af38-8779b9270774'></a>

Serial.println("");

<a id='74846a7c-eb1e-43e0-bcbc-75ae5ec6c763'></a>

Serial.print("Module temperature: ");
Serial.println(SigFox.internalTemperature());

<a id='cb21c66a-d6cb-4f71-a5cb-f15278a2e653'></a>

Serial.println("Register your board on https://backend.sigfox.com/activate with provided ID and PAC");

<a id='d72e0fab-acae-414a-88e1-57ce7ddae624'></a>

delay(100);

<a id='643219ab-91f4-4257-9396-867bd157b31a'></a>

// Send the module to the deepest sleep
SigFox.end();

<a id='4acdedb0-1136-43a6-814b-2461c8a89772'></a>

}
void loop() {
ר
// put your main code here, to run repeatedly:

<a id='032f70fa-9de5-43ee-ac29-0b75c825a3be'></a>

**Notice:** From this point on, it is assumed that the board has already been registered on the Sigfox account. If not, refer to the [First Configuration ↗](https://example.com/first-configuration-tutorial) tutorial from Arduino.

<a id='64c1192c-665a-4811-9514-83f27a5a67e1'></a>

Pushing data to Sigfox

<a id='7c9f481c-76d7-40b7-8878-954bf9a2b25e'></a>

10

<!-- PAGE BREAK -->

<a id='be4c1f2a-1de1-4e71-9f05-8980088a2f5b'></a>

Now that we have our toolchain running, it is time to code something to push data to the Sigfox Backend. Before presenting the code, **remember** that in the callback we have defined in the Sigfox, we established a payload config that is expecting to receive two floats representing both temperature and humidity. So, our payload must match this definition:

<a id='af70699a-c122-4ea7-8452-300891e7be01'></a>

temp::float:32:little-endian hum::float:32:little-endian

<a id='d5117b0f-34c4-4d69-9c94-3ba86977196e'></a>

In our code, this payload can be easily represented by a `struct` that holds two floats.
Defining custom structs with different data types is possible, but **structure padding** and
**architecture** must be carefully considered. The **Sigfox payload** will require
reconfiguration to ensure proper decoding of the transmitted fields.

<a id='9a753266-98cc-4b03-9b83-321f0d329b0d'></a>

```c
struct data{
    float temp;
    float hum;
};
```

<a id='8e662eea-533f-4120-893e-e735df40b549'></a>

In this case, we are using the Arduino MKRFOX1200 along with a DHT sensor providing temperature and humidity required for the callback we have configured in the Sigfox back-end. If a DHT sensor is unavailable, the board's internal temperature sensor can be utilized by calling `SigFox.internalTemperature()`, and setting the humidity value to zero or any other value.

<a id='614882ad-37d6-4593-b34d-f5e79e02a14b'></a>

11

<!-- PAGE BREAK -->

<a id='2bb9a87a-c8f9-4382-b4a3-1630b1a84438'></a>

12

<!-- PAGE BREAK -->

<a id='b41f5883-6901-4f4a-8cd7-f669ec585a03'></a>

```c
#include <SigFox.h>
#include <SimpleDHT.h>
#include <ArduinoLowPower.h>

#define DHT11_PIN 0

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}
```

<a id='939615ce-750c-445f-ade3-e11d12f79ed5'></a>

```c
void blink(unsigned int count, unsigned long ms){
    for(int i=0; i<count; i++){
        digitalWrite(LED_BUILTIN, HIGH);
        delay(ms);
        digitalWrite(LED_BUILTIN, LOW);
        delay(ms);
    }
}
```

<a id='b67ab491-b486-4357-874b-cfd6d5bfeff6'></a>

void send_data(){
//Initialize Sigfox module
SigFox.begin();
delay(100);

// Enable debug LED and disable automatic deep sleep
SigFox.debug();

// clears all pending interrupts
SigFox.status();
delay(1);

// define Sigfox payload data structure
struct data{
  float temp;
  float hum;
};

// read temperature and humidity from DHT sensor connected at
pin DHT11_PIN
SimpleDHT11 dht11;
byte temp, hum;
dht11.read(DHT11_PIN, &temp, &hum, NULL);

<a id='98c5296d-d2ba-4822-913d-1da729dd13e7'></a>

// NOTE! It is not quite efficient sending bytes as floats over
the net, but this is just for illustrative purposes
struct data reading;
reading.temp = temp;

<a id='03df01b7-9d9f-4a45-90c3-07c2bebc1bbc'></a>

13

<!-- PAGE BREAK -->

<a id='1cc852a9-e6f0-4d1d-87ce-450771a0d58f'></a>

**Notice,** The `LowPower.sleep` function call can be uncommented, and the standard `sleep` function call commented out, to enable deep sleep on the Arduino MKRFOX1200, which is beneficial when operating on batteries. It is possible to avoid using the `Serial`, and the `SigFox.debug()` that is, they're just for debugging purposes. In sleep mode, the device requires a manual reset before flashing it again.

<a id='b5e8925f-3666-424c-8fd1-5b82f2968c3d'></a>

## SmartEverything
SmartEverything is an IoT device specially designed for rapid prototyping, as it has full Arduino compatibility, with multiple sensors ready to use, like MEMS Pressure Sensor, Proximity and Ambient Light Sensor, iNEMO 9-axis inertial module, humidity and temperature sensors, and even NFC NTAG, or a GPS/GNSS integrated antenna. If these features are quite interesting by themselves, this board also integrates a Bluetooth Low Energy (BLE) and, of course, a Sigfox Module (Telit LE51-868 S 868MHz module).

<a id='2c787369-176d-4303-9f27-a9fd9b46d144'></a>

<::An electronic circuit board, labeled "SMARTEVERYTHING NFC V2". Visible text on the board includes: "NXP", "PROJECT BY AMEL-TECH", "PRODUCT BY CIPIERRE", "AMEL-TECH", "CIPIERRE.IT.COM", "1998 IF". Another component on the board is labeled "Telit", "LES1-868", "CE0682", "SIN-GPA405004LJ", and "Made in China". The board features various electronic components, connectors, and pins.: figure::>

<a id='2822c239-ea8a-4005-8e80-dcec3aaa3288'></a>

With these awesome features, we can use the board for multiple purposes, like vehicle tracking with the GPS, building a micro meteorological station, registering vibrations and impacts with the accelerometers, or any other use case. For this example, we will register just the temperature and humidity. This way, we have created a simple code that will register temperature and humidity every 10 minutes.

<a id='4b469303-bcc7-42f2-9435-66357bd9690e'></a>

Initial Setup

<a id='15f88b26-52f4-4e12-b22b-948be76195e7'></a>

14

<!-- PAGE BREAK -->

<a id='ed104639-efe7-41d1-bd71-efe15cf06caf'></a>

To program this device, we will use the Arduino IDE ↗. In this case, it is necessary to install the board toolchain, which can be done directly from the Boards Manager, searching for `smarteverything` and selecting the Arrow Boards by Axel Elettronica.

<a id='78c84c42-8e95-482e-9bc1-f3b3d62b07a5'></a>

Boards Manager

Type All

smarteverything

Arrow Boards by Axel Elettronica S.r.l. version 2.1.0 INSTALLED
Boards included in this package:
SmartEverything Fox, SmartEverything Fox3, SmartEverything Lion, SmartEverything Dragonfly, Analog ADI, SmartTutto.
Online help
More info

Select version
Install
Remove

AMEL-Tech Boards by replaced by Arrow Boards
Boards included in this package:
SmartEverything Fox.
Online help
More info

Close

<a id='2c9a69a0-dcea-4a4f-a830-2a1e4b7e35a6'></a>

After a successful installation, we can now select the Board in the Arduino IDE. Just select the SmartEverything Fox (Native USB Port). Select, as with any other Arduino board, the port where de device is connected.

<a id='dfc96fc4-f893-4c21-bc6a-00a12f01b146'></a>

15

<!-- PAGE BREAK -->

<a id='a581d503-220a-418e-bd55-93d49be59153'></a>

SmartEverything Boards
option SmartEverything Fox (via Atmel-ICE): [ ]
option SmartEverything Fox (Native USB Port): [x]
option SmartEverything Fox3 (via Atmel-ICE): [ ]
option SmartEverything Fox3 (Native USB Port): [ ]
option SmartEverything Lion (via Atmel-ICE): [ ]
option SmartEverything Lion (Native USB Port): [ ]
option SmartEverything Dragonfly (via Atmel-ICE): [ ]
option SmartEverything Dragonfly (Native USB Port): [ ]
option Analog ADI (via Atmel-ICE): [ ]
option Analog ADI (Native USB Port): [ ]
option SmartTutto (via Atmel-ICE): [ ]
option SmartTutto (Native USB Port): [ ]

<a id='fd901831-dbd7-477f-96ea-8020d66b7f2a'></a>

## Pushing data to Sigfox

Now it is time to write a simple sketch to send our sensor readings to Sigfox. The provided sample sketch will basically initialize, in the setup, the Sigfox Modem, the sensors, and the USB Serial port for some debugging. Then, in the loop, our sketch will read both the temperature and humidity and will transmit the data to Sigfox. It will also check if the transmission is OK to blink a green LED on success or a red LED otherwise. After that, it will sleep for 10 minutes, as we mentioned in the introduction, Sigfox will allow only 140 messages a day.

<a id='c2f11895-7c12-4c75-b30f-8568ae75dd28'></a>

Before presenting the code, **remember** that in the callback we have defined in the Sigfox, we established a payload config that is expecting to receive two floats representing both temperature and humidity. So, our payload must match this definition:

<a id='fba392f3-a3e5-4a25-a141-3641e50757a5'></a>

temp::float:32:little-endian hum::float:32:little-endian

<a id='9d259d97-69c0-40ea-817d-1c4a588cb945'></a>

16

<!-- PAGE BREAK -->

<a id='9cd87b30-beee-44f6-9ba5-1a55d7944285'></a>

In the code, this payload can be easily represented by a `struct` containing two floats. It is possible to define custom structs with different data types (though **structure padding** and **architecture** should be considered). However, the **Sigfox payload** must be reconfigured to properly decode the fields being sent.

<a id='eed3ded8-37a7-4cb7-b890-7e3f15f81049'></a>

```c
struct data{
    float temp;
    float hum;
};
```

<a id='fbf565f8-f9d5-4717-81cf-cbefe36ec34c'></a>

**Notice** that this code has not been optimized for battery-powered use cases. Use the power-saving mode on the device if needed, but this is out of the scope of this example.

<a id='35934f17-912c-4016-80cf-5a1acaee5549'></a>

17

<!-- PAGE BREAK -->

<a id='539b548d-fbc6-4276-ace3-4f88b276b034'></a>

18

<!-- PAGE BREAK -->

<a id='9a82c79e-4bdf-4bde-97da-8ce282b4c5d7'></a>

#include <Wire.h>
#include <SmeSFX.h>
#include <Arduino.h>
#include <HTS221.h>

<a id='245a2d8b-37ed-441f-8905-0ea02f332a1c'></a>

```c
void setup() {
  // init temp & hum sensor
  Wire.begin();
  smeHumidity.begin();

  // init serial
  SerialUSB.begin(115200);

  // init sigfox module
  sfxAntenna.begin(19200, &SigFox);
  sfxAntenna.setSfxDataMode();
}

void send_data(){
  // define Sigfox payload data structure
  struct data{
    float temp;
    float hum;
  };

  // read sensor data into the struct
  struct data reading;
  reading.temp = smeHumidity.readHumidity();
  reading.hum = smeHumidity.readTemperature();

  // send the structure to Sigfox (8 bytes)
  SerialUSB.println("Sending SigFox message!");
  sfxAntenna.sfxSendData((const char*)&reading, sizeof(reading));
}

void loop() {
  // send Sigfox data
  send_data();

  // wait for a response
  bool response=false;
  do{
    if (sfxAntenna.hasSfxAnswer()) {
      switch (sfxAntenna.sfxDataAcknoledge()) {
        case SFX_DATA_ACK_OK:
          ledGreenLight(HIGH);
          SerialUSB.println("Answer OK! :)");
          delay(2000);
```

<a id='49d0909e-ce23-40a0-9475-dacb60c6d383'></a>

19

<!-- PAGE BREAK -->

<a id='5957141a-0204-464f-9f4f-2e879a477692'></a>

## Checking Sigfox Setup

After we have both the device code running, the Sigfox callback configured, and the data bucket created, we should check that everything is up and running.

<a id='d1e069d5-8a4e-4549-a591-f5c24b9bcd32'></a>

We can start by checking that the Sigfox platform is receiving our messages. Just go to the device in the Sigfox back-end, and open the `Messages` section that is on the left panel. Here, some messages have been received. See the payload being sent (in hexadecimal), and some other information like link quality, timestamp, or callback result.

<a id='86b83c13-370b-4080-ba0f-5e486b7d6cc7'></a>

Time Data / Decoding Location Link quality Callbacks
2017-04-22 22:22:58 5a7dcf41e1182342 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 22:12:50 e0f1cf4130272242 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 22:02:42 4e94ce4110462442 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 21:52:35 f9c3bb41aec44c42 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 21:36:59 a264cb4154c12542 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 21:26:52 45c9ca4137612642 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>

<a id='a839be6b-f6c2-4563-8c58-c8e693a9a616'></a>

It is interesting here to check that our callback response is successful, as the callback icon changes from green to red depending on the result. In our case, our callbacks are in green, so the request was ok. Click on the icon to see the server response, which is a 200 OK HTTP response.

<a id='6e300b08-74ce-4bd7-8339-908eda9d85e3'></a>

20

<!-- PAGE BREAK -->

<a id='820278ce-c7a1-4a6e-a571-f5e487a35de5'></a>

Callback - OK

[OK] - Base station 06C9 < 1 second
200 - OK

[POST] https://api.thinger.io/v1/users/alvarolb/buckets/SmartEverything/data

<a id='cab6eb16-130a-4234-9594-f3283ae63720'></a>

Then we can also check that our data bucket is being populated with the data received from Sigfox. So, open the data bucket in Thinger.io. Nice! We have our data now being stored. **Notice** that the columns in the bucket are just the fields we configured in the Sigfox callback body.

<a id='8bd43ee5-c452-47b1-bd0a-bff6b3595add'></a>

Bucket Explorer
<table id="20-1">
<tr><td id="20-2">Date</td><td id="20-3">device</td><td id="20-4">humidity</td><td id="20-5">latitude</td><td id="20-6">longitude</td><td id="20-7">rssi</td><td id="20-8">snr</td><td id="20-9">station</td><td id="20-a">temperature</td></tr>
<tr><td id="20-b">2017-04-23T01:03:30.688+0200</td><td id="20-c">C378F</td><td id="20-d">41.874535</td><td id="20-e">41</td><td id="20-f">-4</td><td id="20-g">-130</td><td id="20-h">21.28</td><td id="20-i">06C9</td><td id="20-j">25.32931</td></tr>
<tr><td id="20-k">2017-04-23T00:53:22.895+0200</td><td id="20-l">C378F</td><td id="20-m">41.72929</td><td id="20-n">41</td><td id="20-o">-4</td><td id="20-p">-132</td><td id="20-q">19.29</td><td id="20-r">06C9</td><td id="20-s">25.386208</td></tr>
<tr><td id="20-t">2017-04-23T00:43:14.984+0200</td><td id="20-u">C378F</td><td id="20-v">41.384327</td><td id="20-w">41</td><td id="20-x">-4</td><td id="20-y">-129</td><td id="20-z">21.93</td><td id="20-A">06C9</td><td id="20-B">25.518965</td></tr>
<tr><td id="20-C">2017-04-23T00:33:07.300+0200</td><td id="20-D">C378F</td><td id="20-E">41.03574</td><td id="20-F">41</td><td id="20-G">-4</td><td id="20-H">-130</td><td id="20-I">21.36</td><td id="20-J">06C9</td><td id="20-K">25.765518</td></tr>
<tr><td id="20-L">2017-04-23T00:22:59.397+0200</td><td id="20-M">C378F</td><td id="20-N">40.774296</td><td id="20-O">41</td><td id="20-P">-4</td><td id="20-Q">-130</td><td id="20-R">21.01</td><td id="20-S">06C9</td><td id="20-T">25.936207</td></tr>
<tr><td id="20-U">2017-04-23T00:12:51.492+0200</td><td id="20-V">C378F</td><td id="20-W">40.53827</td><td id="20-X">41</td><td id="20-Y">-4</td><td id="20-Z">-129</td><td id="20-10">21.62</td><td id="20-11">06C9</td><td id="20-12">25.993103</td></tr>
<tr><td id="20-13">2017-04-23T00:02:43.686+0200</td><td id="20-14">C378F</td><td id="20-15">41.06842</td><td id="20-16">41</td><td id="20-17">-4</td><td id="20-18">-129</td><td id="20-19">22.02</td><td id="20-1a">06C9</td><td id="20-1b">25.822414</td></tr>
<tr><td id="20-1c">2017-04-22T23:52:35.800+0200</td><td id="20-1d">C378F</td><td id="20-1e">51.19207</td><td id="20-1f">41</td><td id="20-1g">-4</td><td id="20-1h">-130</td><td id="20-1i">20.77</td><td id="20-1j">1D62</td><td id="20-1k">23.47069</td></tr>
<tr><td id="20-1l">2017-04-22T23:37:00.903+0200</td><td id="20-1m">C378F</td><td id="20-1n">41.438797</td><td id="20-1o">41</td><td id="20-1p">-4</td><td id="20-1q">-131</td><td id="20-1r">19.81</td><td id="20-1s">1D62</td><td id="20-1t">25.424137</td></tr>
<tr><td id="20-1u">2017-04-22T23:26:53.076+0200</td><td id="20-1v">C378F</td><td id="20-1w">41.594936</td><td id="20-1x">41</td><td id="20-1y">-4</td><td id="20-1z">-133</td><td id="20-1A">18.21</td><td id="20-1B">06C9</td><td id="20-1C">25.348276</td></tr>
</table>
Refresh
Viewing 0 to 54 items

<a id='82511d0a-b501-4b83-91d7-33154f63bb8d'></a>

## Building a Dashboard

Now that we have our data in the bucket, we can just create a real-time dashboard from our Sigfox data. Create the widgets by selecting the bucket as the data source, and that's all!

<a id='04dd09cb-45ac-4d0e-a36e-bdb4dc7c7010'></a>

21

<!-- PAGE BREAK -->

<a id='9252b9ab-7de4-4106-be7e-b5e374596a85'></a>

Sigfox Dashboard option : [ ] <::Temperature & Humidity chart. The chart displays two lines, one for humidity and one for temperature, over time. The legend indicates a dark gray line for humidity and a light gray line for temperature. The left Y-axis represents humidity, ranging from 30 to 55. The right Y-axis represents temperature, ranging from 23.0 to 26.5. The X-axis represents time, from 17:00 to 01:00. Both lines show fluctuations, with the humidity line generally staying between 40 and 45, and the temperature line generally staying between 24.5 and 25.5, with some spikes and dips.::>

<a id='e8e912b5-21b0-4d5a-b608-2ebc59c33718'></a>

Sigfox device location<::A map centered on Segovia, Spain, showing a location pin. The map displays roads (E-5, AP-6) and nearby towns such as Arévalo, Coca, Ávila, and La Granja de S. Ildefonso. Options for "Mapa" and "Satélite" are visible at the top left. Map controls including zoom in/out (+/-) and a person icon are present on the right. At the bottom, text reads "Datos de mapas", "Términos de uso", and "Informar de un error de Maps" from Google.: map::>Link Quality<::A circular gauge, partially filled with a dark segment at the top right, indicating a value of "-130RSSI" in the center.: gauge::>Monitored DeviceC378FSigfox Station06C9

<a id='c0d6fe00-f941-4898-9337-2a17093b7d45'></a>

Previous
REMOTE CONSOLE

<a id='63875123-fad4-4dc2-8d4b-374e51d244bd'></a>

Next
LoRaWAN

<a id='90953799-ac37-4397-83c4-d24719fdc028'></a>

Last updated 5 months ago

<a id='5f680051-98d5-43e5-806e-b9c2f08c70a1'></a>

Was this helpful?
option Happy: [ ]
option Neutral: [ ]
option Sad: [ ]

<a id='ab7cd884-e4a4-4028-b533-82302c275bba'></a>

<::logo: [Unknown] option : [ ] option : [x] option : [ ] Three icons are displayed: a sun, a computer monitor, and a moon, with the monitor icon highlighted.::>

<a id='76772921-e67a-436d-9e26-9623dfc85b13'></a>

22