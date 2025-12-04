<a id='323e2138-aafe-4840-a6a5-85c6e5293fe5'></a>

12/4/25, 2:52 PM

<a id='cafc3ac7-dafd-48ca-8e6d-0b06419ce387'></a>

WiFiNINA | Arduino Documentation

<a id='72b13f93-414a-4728-bb6b-0723bbd7c4a9'></a>

ARDUINODOCS

<a id='c87b98a9-5836-4696-b055-7abbbc6fcc78'></a>

Search on Docs /

<a id='81d2aaf2-a744-4144-bb8e-6c66ea5cedda'></a>

← Go Back

Library

<a id='2af300c3-deed-4007-9951-bc9d27d30402'></a>

Recents viewed

<a id='579cc73d-7677-436a-b648-eb3d8986109c'></a>

- WiFiNINA
- Arduino SigFox for
  MKRFox1200
- autowp-mcp2515
- Arduino_MKRENV
- Arduino_MKRGPS
- Arduino_APDS9960
- Arduino_MKRIoTCarrier

<a id='487e47bc-644e-4c44-988b-83294c2641fd'></a>

Home / Programming / Library / WiFiNINA

<a id='aa121ba8-c84d-43e8-b8bb-1dc7bdeec106'></a>

COMMUNICATION
# WiFiNINA

ARDUINO LGPL-2.1 V1.9.1 Arduino 20/03/2025

<a id='2955323c-b795-4020-87bb-e4b545d70d5b'></a>

🔧 Arduino <info@arduino.cc>
🌐 http://www.arduino.cc/en/Ref... ✉️ info@arduino.cc

<a id='8fc36f15-bb1b-41ff-9a71-b51cae8227b2'></a>

Enables network connection (local and Internet) with the
Arduino MKR WiFi 1010, Arduino MKR VIDOR 4000,
Arduino Uno WiFi Rev.2 and Nano 33 IoT.

<a id='db8b1ecf-c596-468f-b8ff-c0152df144e1'></a>

With this library you can instantiate Servers, Clients
and send/receive UDP packets through WiFi. The
board can connect either to open or encrypted
networks (WEP, WPA). The IP address can be
assigned statically or through a DHCP. The library
can also manage DNS.

<a id='633bf287-7fa4-429e-872a-b923677b184d'></a>

GO TO REPOSITORY

<a id='b0e5cb25-8bf9-49a5-9f40-d297f4552aa8'></a>

Usage/Examples Compatibility Releases

This library allows you to use the Arduino Uno WiFi Rev.2, Arduino Nano 33 IoT, Arduino MKR 1010 and Arduino MKR VIDOR 4000 WiFi capabilities. It can serve as either a server accepting incoming connections or a client making outgoing ones. The library supports WEP, WPA2 Personal and WPA2 Enterprise encryptions. This library supports all the same methods of the original WiFi library plus the connectSSL(). The WiFININA library is very similar to the Ethernet and the WiFi library, and many of the function calls are the same.

<a id='5179c7e9-30a8-4b78-aeb4-bb567dbfe897'></a>

To use this library:

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
```

<a id='c28864b0-2292-4c60-b86a-5b62c3ce1d5b'></a>

# Examples

Several examples for the **WiFiNINA** library are available from the **Examples from Libraries** page.

<a id='37410bf8-b733-4b82-a12f-b178a0e0fbf6'></a>

ON THIS PAGE

<a id='ffcc4651-45f5-416c-a861-7be116e59294'></a>

Usage/Examples
Compatibility
Releases
WiFi Class +
Client Class +
Server Class +
UDP Class +

<a id='dd590577-b9bc-4aed-ac89-7b53dbe6be76'></a>

WiFi Class
---
UDP Class

<a id='5f6ca9d8-f3e7-48f3-ae67-dd2c599d6270'></a>

Client Class Server Class

<a id='bfaf3163-4f02-43b8-bdd8-19dec603a266'></a>

Help

<a id='8d4580c8-9cf7-42d3-80ca-a342b55f5a27'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='7ec07a96-f7b3-417c-b010-2582c0cba002'></a>

1/30

<!-- PAGE BREAK -->

<a id='bad69d66-641c-451c-89de-bd562f78c104'></a>

12/4/25, 2:52 PM

<a id='68fa49d9-a129-4b3b-8c5f-6f1132f8f06f'></a>

WiFiNINA | Arduino Documentation

<a id='83583e31-df03-4f1d-a4be-a08feb45b8c9'></a>

ARDUINODOCS

<a id='4afcdfff-c976-4384-ae94-30ee63265b5c'></a>

## Description

Initializes the WiFiNINA library's network settings and provides the current status.

<a id='53e5f66a-d88e-4c6a-8a0c-4db9fc3da0b7'></a>

Syntax

```
1 WiFi.begin(ssid);
2 WiFi.begin(ssid, pass);
3 WiFi.begin(ssid, keyIndex, key)
```

<a id='b11b90c5-a86f-4f62-8b13-4a55ba0949b7'></a>

# Parameters

ssid: the SSID (Service Set Identifier) is
the name of the WiFi network you
want to connect to.

<a id='afde4903-e8eb-4ced-bf00-d15d9a19686e'></a>

keyIndex: WEP encrypted networks can hold up to 4 different keys. This identifies which key you are going to use.

<a id='bd22af35-2e90-4315-aacf-5a8309787e5e'></a>

key: a hexadecimal string used as a security code for WEP encrypted networks.

<a id='d47e54a9-ffe3-4095-a5de-89dd0614d8ed'></a>

pass: WPA encrypted networks use a
password in the form of a string for
security.

<a id='eb7bd3fb-30f3-4970-b551-82abb70089ff'></a>

## Returns

WL_CONNECTED when connected to a network

WL_IDLE_STATUS when not connected to a network, but powered on

<a id='6986567f-8f7d-43f2-98f2-2d966cf7b175'></a>

Example

```
1 #include <WiFiNINA.h>
2
3 //SSID of your network
4 char ssid[] = "yourNetwork";
5 //password of your WPA Network
6 char pass[] = "secretPassword";
7
8 void setup()
9 {
10   WiFi.begin(ssid, pass);
11 }
12
13 void loop () {}
```

<a id='24be27b1-d0ed-4a4e-862b-3550ab21410d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='eba433b7-7e9b-4e40-9da2-4f864986fec4'></a>

2/30

<!-- PAGE BREAK -->

<a id='afaa3420-877e-488c-8e09-8b78981f135f'></a>

12/4/25, 2:52 PM

<a id='297511bf-3f0c-4a8d-806c-2621dc0d8188'></a>

WiFiNINA | Arduino Documentation

<a id='1d558dda-218f-49eb-9d9a-80ebac189347'></a>

ARDUINODOCS

<a id='64e08f93-3ed6-4e43-9607-fd7d8b6542f1'></a>

WiFi.end()

# Description

Turns off the WiFi module. If WiFi.begin()
was used to connect to an access point, the
connection will be disconnected. If
WiFi.beginAP() was used before to create an
access point, the WiFi.end() will stop
listening it too.

<a id='6860e942-f14f-4678-8329-886184f3c2b4'></a>

## Syntax

```
1 WiFi.end();
```

<a id='de7bcae8-a167-4a14-af73-9479044595f4'></a>

Parameters

None

<a id='73734f28-61d1-40df-9dff-22392af83987'></a>

Returns

Nothing

<a id='a7ab93d5-5533-409f-ada9-4db09457d2e6'></a>

WiFi.beginAP()

<a id='9b70c9d8-dcb4-4407-aac9-3bb19770ee35'></a>

# Description

Initializes the WiFININA library in Access Point (AP) mode. Other WiFi devices will be able to discover and connect to the created Access Point.

<a id='490a8edf-7e54-4243-8a58-5ea260b8197e'></a>

Syntax

```
1 WiFi.beginAP(ssid);
2 WiFi.beginAP(ssid, channel);
3 WiFi.beginAP(ssid, passphrase);
4 WiFi.beginAP(ssid, passphrase,
```

<a id='e909bfb7-dbb5-44ae-be29-e686062a5385'></a>

## Parameters

ssid: the SSID (Service Set Identifier) of the created Access Point. Must be 8 or more characters.

passphrase: optional, the WPA password of the created Access Point. Must be 8 or more characters.

<a id='638713fd-13a6-4249-b4c0-460019127dd4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='f2943b44-037b-4356-b38e-8b9e4a822bd0'></a>

3/30

<!-- PAGE BREAK -->

<a id='c5d93a0c-be5c-4d63-a1f9-57423b27f7c6'></a>

12/4/25, 2:52 PM

<a id='3680016f-f8a9-4eb3-bc16-84d507e05f42'></a>

WiFiNINA | Arduino Documentation

<a id='e8c61eb3-e6c7-4e7f-ac92-0d0ff9eb862d'></a>

ARDUINODOCS

<a id='6f992d19-c77d-470a-b90b-1b2d671d786b'></a>

channel 1;

## Returns

WL_AP_LISTENING when creating
access point succeeds
WL_CONNECT_FAILED when creating
access point fails

<a id='0f485ec3-5111-4cf3-8d69-8ce02f7d01d8'></a>

Example

```
1 /*
2
3 WiFi Web Server LED Blink
4
5 A simple web server that le
6 This sketch will create a n
7 It will then launch a new s
8 to the Serial Monitor. From
9 to turn on and off the LED
10
11 If the IP address of your b
12 http://yourAddress/H turn
13 http://yourAddress/L turn
14
15 created 25 Nov 2012
16 by Tom Igoe
17 adapted to WiFi AP by Adafr
18 */
19 #include <SPI.h>
20 #include <WiFiNINA.h>
21 #include "arduino_secrets.h"
22 /////please enter your sens
23 char ssid [] = SECRET_SSID;
24 char pass [] = SECRET_PASS;
25 int keyIndex = 0;
26
27 int led = LED_BUILTIN;
28 int status = WL_IDLE_STATUS;
```

<a id='b54b9a53-6cf5-4115-8f0c-518566b4d566'></a>

v WiFi.beginEnterprise()

<a id='cacecd1c-c483-40e2-a41e-7f415171fc44'></a>

# Description
Initializes the WiFININA library's network settings for a common WPA2 Enterprise network with username and password authentication (PEAP/MSCHAPv2).

<a id='459062f4-fb9a-46a3-96cd-26fd49504a9e'></a>

Note: this feature requires NINA firmware
version 1.3.0 or later. All string parameter
supplied must have a combined length of
under 4000 bytes.

<a id='e5171a18-e2a1-4ac8-94aa-58e540d8f2b6'></a>

Syntax

<a id='8146a189-8d61-4229-8fc1-89d65095850f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='db8b764c-2e93-41e3-afb4-f72875326ae8'></a>

4/30

<!-- PAGE BREAK -->

<a id='d7ba6eb1-e923-4ec3-9b7c-b4c4d29b4ee6'></a>

12/4/25, 2:52 PM

<a id='4208d3ed-b89d-4b64-8367-7c35f331e56a'></a>

WiFiNINA | Arduino Documentation

<a id='dfd74369-2f41-4dbc-8245-ccb3be647df2'></a>

ARDUINODOCS

<a id='7aab82a2-59b4-42dc-bd53-bc68ba05b039'></a>

1 WiFi.beginEnterprise(ssid, user
2 WiFi.beginEnterprise(ssid, user
3 WiFi.beginEnterprise(ssid, user

<a id='83b4b58f-4867-41fe-bba5-78b21b2e61d3'></a>

# Parameters

ssid: the SSID (Service Set Identifier) is
the name of the WiFi network you
want to connect to.

username: username part of WPA2
Enterprise (RADIUS) credentials

password: password part of WPA2
Enterprise (RADIUS) credentials

identity: WPA2 enterprise identity
(optional)

ca: root certificate (string) to validate
against (optional)

<a id='1946dc07-13c1-411e-a768-8c945b7d5b25'></a>

# Returns

WL_CONNECTED when connected to a
network
WL_IDLE_STATUS when not connected
to a network, but powered on

<a id='b71993e4-44a7-4015-afb7-9d0afaa5eae3'></a>

Example
1 /*
2 This example connects to a
3 Then it prints the MAC addr
4 the IP address obtained, an
5 
6 Based on ConnectWithWPA.ino
7 */
8 #include <SPI.h>
9 #include <WiFiNINA.h>
10 
11 #include "arduino_secrets.h"
12 ///////please enter your sens
13 char ssid [] = SECRET_SSID; /
14 char user[] = SECRET_USER; /
15 char pass[] = SECRET_PASS; /
16 int status = WL_IDLE_STATUS;
17 
18 void setup() {
19 //Initialize serial and wai
20 Serial.begin(9600);
21 while (!Serial) {
22 ; // wait for serial port
23 }
24 
25 // check for the WiFi modul
26 if (WiFi.status() == WL_NO_
27 Serial.println("Communica
28 // don't continue

<a id='fd8a4565-8c36-4c13-8fe2-06a0aa3ef95d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='f85b184e-df3c-4976-9286-59bed2a280d8'></a>

5/30

<!-- PAGE BREAK -->

<a id='2957bcaa-3084-4111-894b-7e1fbe7a8d56'></a>

12/4/25, 2:52 PM

<a id='2369f2bb-93b6-4585-920a-559e9069124a'></a>

WiFiNINA | Arduino Documentation

<a id='42b0c0eb-dafc-4181-8993-bf76eb90ba0c'></a>

ARDUINODOCS

<a id='dd9f946b-7c9f-470c-833d-e740d429e185'></a>

WiFi.disconnect()

## Description
Disconnects the WiFi from the current
network.

## Syntax
```
1 WiFi.disconnect()
```

## Parameters
None

## Returns
Nothing

<a id='9f1b598f-ef27-4d61-bbed-01c596484244'></a>

WiFi.config()

<a id='82c50c3f-c78a-4100-999c-7767bd296199'></a>

## Description
WiFi.config() allows you to configure a static IP address as well as change the DNS, gateway, and subnet addresses on the WiFi shield.

<a id='2d6bbeff-7efe-4d63-a281-267ad4f64e54'></a>

Unlike WiFi.begin() which automatically
configures the WiFi shield to use DHCP,
WiFi.config() allows you to manually set the
network address of the shield.

<a id='2cb7e9f5-8695-4927-9038-99c6a7263325'></a>

Calling WiFi.config() before WiFi.begin()
forces begin() to configure the WiFi shield
with the network addresses specified in
config().

<a id='a429c007-77a1-4a9d-9b12-1f81d7bdaf6d'></a>

You can call WiFi.config() after WiFi.begin(),
but the shield will initialize with begin() in
the default DHCP mode. Once the config()
method is called, it will change the network
address as requested.

<a id='cc7ecb47-d578-42d9-8b67-64fc85593fa1'></a>

Syntax

<a id='18472d8b-a457-49b4-9c97-177dd92d2cb4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='d879b97e-31cc-4328-854d-c5c910dc5356'></a>

6/30

<!-- PAGE BREAK -->

<a id='4fdb7e6c-fc3b-4c1f-b83d-16b044f0c940'></a>

12/4/25, 2:52 PM

<a id='f785b77f-1382-467c-b444-a6aae7880af4'></a>

WiFiNINA | Arduino Documentation

<a id='19f2c342-e6d5-4ecb-8ec5-8d957642cfc6'></a>

ARDUINODOCS

<a id='046f7115-33a1-441a-a5ea-782a4f7ba9ad'></a>



<a id='01c3df0b-8a4e-4639-95b9-85e0b5444208'></a>

```
1 WiFi.config(ip);
2 WiFi.config(ip, dns);
3 WiFi.config(ip, dns, gateway);
4 WiFi.config(ip, dns, gateway, s
```

<a id='9f093069-9373-4054-9641-25ee1e73f54e'></a>

# Parameters

ip: the IP address of the device (array of 4 bytes)

dns: the address for a DNS server.

gateway: the IP address of the network gateway (array of 4 bytes). - optional: defaults to the device IP address with the last octet set to 1

subnet: the subnet mask of the network (array of 4 bytes). optional: defaults to 255.255.255.0

<a id='f957cfd6-253a-4395-a092-f53c9c980f7f'></a>

Returns

Nothing

<a id='733d71b6-262c-4d22-9604-a3a0b2d95f9b'></a>

Example
```c
1 This example shows how to set
2
3 #include <SPI.h>
4 #include <WiFiNINA.h>
5
6 // the IP address for the shield
7 IPAddress ip(192, 168, 0, 177);
8
9 char ssid[] = "yourNetwork";
10 char pass[] = "secretPassword";
11
12 int status = WL_IDLE_STATUS;
13
14 void setup()
15 {
16   // Initialize serial and wait for port to open:
17   Serial.begin(9600);
18   while (!Serial) {
19     ;
20   }
21
22   WiFi.config(ip);
23
24   // attempt to connect to WiFi network
25   while (status != WL_CONNECTED) {
26     Serial.print("Attempting to connect to SSID: ");
27     Serial.println(ssid);
28     // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
29     status = WiFi.begin(ssid, pass);
```

<a id='26db6748-7ad5-4f28-85d6-3a3d831611c1'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='ae00bd30-965a-4b4d-9d50-f456c6d21a79'></a>

7/30

<!-- PAGE BREAK -->

<a id='24bf044d-9b67-4f35-8b98-f3eb298dc9ed'></a>

12/4/25, 2:52 PM

<a id='2a04abbb-ee56-4e8f-8a70-20a7a9731293'></a>

WiFiNINA | Arduino Documentation

<a id='d2b1890c-6c96-451a-adb2-71d5be4e1fc3'></a>

ARDUINODOCS

<a id='a4a208dd-55f6-4e82-adb1-4c4598cc3f1d'></a>



<a id='93ca6ab2-17ca-49fb-a668-ec8b8210250a'></a>

### Description

WiFi.setDNS() allows you to configure the DNS (Domain Name System) server.

<a id='45000e56-e35a-43f7-867e-7ca7eef453df'></a>

## Syntax

```
1 WiFi.setDNS(dns_server1)
2 WiFi.setDNS(dns_server1, dns_se
```

<a id='418ad3c5-3450-42d8-b874-b6a6e99cada8'></a>

## Parameters

dns_server1: the IP address of the primary DNS server

dns_server2: the IP address of the secondary DNS server

<a id='3c577834-6b45-42da-9df4-0bf6f459a9f7'></a>

Returns
Nothing

<a id='9b089c30-4183-4399-b79d-a0e8be73bce4'></a>

Example
```c
1 This example shows how to set
2
3 #include <SPI.h>
4 #include <WiFiNINA.h>
5
6 // the IP address for the shi
7 IPAddress dns(8, 8, 8, 8); /
8
9 char ssid[] = "yourNetwork";
10 char pass[] = "secretPassword";
11
12 int status = WL_IDLE_STATUS;
13
14 void setup()
15 {
16   // Initialize serial and wa
17   Serial.begin(9600);
18   while (!Serial) {
19     ; // wait for serial port
20   }
21
22   // attempt to connect to Wi
23   while (status != WL_CONNEC
24   Serial.print("Attempting");
25   Serial.println(ssid);
26   // Connect to WPA/WPA2 ne
27   status = WiFi.begin(ssid,
28   // wait 10 seconds for --
```

<a id='a4e624b2-fd1f-4b97-994d-ae1bde4e330d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='249b5037-6bf4-476a-90e3-8a8ea270cb46'></a>

8/30

<!-- PAGE BREAK -->

<a id='12297ffa-acf1-41ca-84ec-b892c5e181cf'></a>

12/4/25, 2:52 PM

<a id='00e6090b-6953-4089-a84e-d378c8067e1e'></a>

WiFiNINA | Arduino Documentation

<a id='a76c9f9b-0398-4748-8e13-a2c8866d4e77'></a>

ARDUINODOCS

<a id='181f7a91-c7ce-461e-bff8-0d6636849e83'></a>

WiFi.setHostname()

# Description

Sets the hostname of the module, the
hostname is sent in WiFi.begin(...) when an
IP address is requested from a DHCP server.

<a id='3da4d025-2997-4478-8afa-80c4af5ac6ad'></a>

## Syntax

```
1 WiFi.setHostname(hostname)
```

<a id='a08aafce-799a-4431-90a0-119baaa2d9aa'></a>

## Parameters

hostname - new hostname to use

<a id='6cf84426-dfc7-405c-b709-5cbb757fada2'></a>

Returns
Nothing

<a id='bc11976d-7901-4e8e-affb-eb0fe88cf176'></a>

Example

```arduino
1   ...
2   WiFi.setHostname("MyArduino"
3   
4   // attempt to connect to WiF
5   while (status != WL_CONNECTE
6       Serial.print("Attempting t
7       Serial.println(ssid);
8   // Connect to WPA/WPA2 net
9   status = WiFi.begin(ssid, 
10  
11  // wait 10 seconds for con
12  delay(10000);
13  }
14  ...
```

<a id='3b489754-32c2-46b1-bfc8-feaf187f3ecf'></a>

WiFi.setTimeout()

### Description
Sets the connection timeout value in milliseconds for WiFi.begin(...).

### Syntax


<a id='d3cdce8b-f99e-4a18-9b38-33b0181b2b83'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='95c68263-b61e-4ad9-95e4-4de7f72e8a08'></a>

9/30

<!-- PAGE BREAK -->

<a id='306d0856-ff5a-4678-bced-2cd90253cc1c'></a>

12/4/25, 2:52 PM

<a id='e34a0abc-96d3-4c87-82c1-8b0a4e60684e'></a>

WiFiNINA | Arduino Documentation

<a id='54937263-c765-41af-b2d0-8b8baa356dc1'></a>

ARDUINODOCS

<a id='8593600d-d09c-4b8a-b2fd-6ac84d8af302'></a>

# Parameters
timeout - the connection timeout value
in milliseconds

# Returns
Nothing

# Example
```
1   ...
2   WiFi.setTimeout(120 * 1000);
3
4   // attempt to connect to WiFi
5   while (status != WL_CONNECTED) {
6     Serial.print("Attempting to connect to SSID: ");
7     Serial.println(ssid);
8     // Connect to WPA/WPA2 network. Change this to your WiFi name and password
9     status = WiFi.begin(ssid, password);
10
11    // wait 10 seconds for connection
12    delay(10000);
13  }
14
15  ...
```

<a id='6bdcc00c-e91a-416a-ac8a-1be7f5ca202f'></a>

WiFi.SSID()

<a id='153444d9-89e0-4952-8a28-c94bb63bbe46'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='a0861e9c-1586-4810-805e-639400f0b622'></a>

10/30

<!-- PAGE BREAK -->

<a id='47ab4cd2-eae4-4f6f-89bc-301865dd7c61'></a>

12/4/25, 2:52 PM

<a id='50801420-1841-47b2-afa8-b48c3055cc66'></a>

WiFiNINA | Arduino Documentation

<a id='b94c09e0-7020-4d9d-933e-11c0eea7e057'></a>

ARDUINODOCS

<a id='6a103cc6-fe29-4cb4-b054-f21d6f4df7c9'></a>

### Description

Gets the SSID of the current network

<a id='887b042d-b460-4be1-a660-4fc11343309b'></a>

## Syntax

```
1 WiFi.SSID();
2 WiFi.SSID(wifiAccessPoint)
```

<a id='8472ea0a-8b9a-46d8-9747-39df89688f31'></a>

## Parameters

wifiAccessPoint: specifies from which network to get the information

<a id='31d0bbc0-0562-467d-b2fb-0d6787d11b19'></a>

# Returns
A string containing the SSID the WiFi is currently connected to.
A string containing name of network requested.

<a id='40d5350a-ee36-4bcf-b6b6-131208d12308'></a>

Example

```c
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 //SSID of your network
5 char ssid[] = "yourNetwork";
6 int status = WL_IDLE_STATUS;
7 
8 void setup()
9 {
10   // initialize serial:
11   Serial.begin(9600);
12 
13   // scan for existing networks
14   Serial.println("Scanning available networks");
15   scanNetworks();
16 
17   // attempt to connect using ssid as target
18   Serial.println("Attempting to connect to SSID: ");
19   status = WiFi.begin(ssid);
20 
21   Serial.print("SSID: ");
22   Serial.println(ssid);
23 }
24 
25 void loop() {}
26 
27 void scanNetworks() {
28   // code for scanning networks
```

<a id='98270af8-37a0-4263-8b72-d1f4b390644c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='065b12ad-b461-4294-ab68-16d776b3c691'></a>

11/30

<!-- PAGE BREAK -->

<a id='ab3daf86-820b-4108-a396-8be10aa80336'></a>

12/4/25, 2:52 PM

<a id='ce3b4385-6a7b-472c-be73-e9f830ced2b2'></a>

WiFiNINA | Arduino Documentation

<a id='935eaf7c-e823-44a7-9bb9-e76e139f1ebf'></a>

ARDUINODOCS

<a id='6adbd65d-d0d8-4c1a-b786-66faf82ef279'></a>

WiFi.BSSID()

# Description

Gets the MAC address of the router you are
connected to or the MAC address of a
network that was scanned.

<a id='af63b505-654a-4604-9181-2c45860e9a22'></a>

## Syntax

```
1 WiFi.BSSID(bssid)
2 WiFi.BSSID(wifiAccessPoint, bss
```

<a id='1ab12277-be84-4d36-91b5-cce852adb012'></a>

## Parameters

bssid - 6 byte array
wifiAccessPoint - specifies from which network to get the information (optional), only needed after a scan

<a id='d56ccbe0-be23-4092-b603-990e419ecfbb'></a>

# Returns
A byte array containing the MAC address of the router the WiFi shield is currently connected to or the MAC address of a network that was scanned. The first array index contains the last byte of the MAC address.

<a id='db0a0b7a-93a4-4c93-a2cc-0f69078b3e94'></a>

Example

___

<a id='8055a135-1024-46dc-a10f-238e5be6f660'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='f76ff872-0a9d-4022-9ebb-34ce66b5f106'></a>

12/30

<!-- PAGE BREAK -->

<a id='15eedcd6-5145-463e-9a14-a136005fd088'></a>

12/4/25, 2:52 PM

<a id='b1b8791f-9758-4b4e-b30a-6e13007a7eb2'></a>

WiFiNINA | Arduino Documentation

<a id='ac8183f0-7906-469f-a0cb-626cbbaf757f'></a>

ARDUINODOCS

<a id='9b8d78e0-4b57-4e2b-baaf-2cbf249d76cc'></a>

```c
#include <SPI.h>
#include <WiFiNINA.h>

//SSID of your network
char ssid[] = "yourNetwork";
//password of your WPA Network
char pass[] = "secretPassword";

void setup() {
  WiFi.begin(ssid, pass);

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Couldn't get connected");
    while(true);
  }
  // if you are connected, print
  else {
    // print the received signal
    long rssi = WiFi.RSSI();
    Serial.print("RSSI:");
    Serial.println(rssi);
  }
}

void loop () {}
```

<a id='82aaed40-1442-4f7c-90e8-c77d5c55edd6'></a>

option WiFi.channel(): [ ]

<a id='0232e4c7-7065-433a-8b21-1cb3eaf9888f'></a>

## Description
Gets the WiFi channel of a network that was scanned.

<a id='c40cfd80-aeb5-46c6-b4dc-356e03c35abf'></a>

## Syntax

```
1 WiFi.channel(wifiAccessPoint)
```

<a id='10fe7650-41d8-4ec3-bfe5-a068d3688ec7'></a>

## Parameters

wifiAccessPoint - specifies from which
network to get the information

<a id='129be353-2781-4b79-8294-2d565055c43a'></a>

Returns

WiFi channel of scanned network

<a id='6fdf75e9-9cf6-49ce-b0bc-f9cf0eba4a1a'></a>

Example

________________________________________________________________________________

<a id='7fd9a584-fd3d-4df3-b4b1-b02bc18d2892'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='fbc82e3b-9db5-41fc-9219-4a588cbb1e7b'></a>

14/30

<!-- PAGE BREAK -->

<a id='ac639f16-09ca-4e37-898a-f189ccd251f6'></a>

12/4/25, 2:52 PM

<a id='d10f6253-2135-479e-834a-0d8af2974dc6'></a>

WiFiNINA | Arduino Documentation

<a id='d7121856-cdbd-4f91-afd9-f87013a13921'></a>

ARDUINODOCS

<a id='30d6ef3b-b024-42eb-ae25-bb64024bc019'></a>

```
1 ...
2 // scan for nearby networks
3 Serial.println("** Scan Net
4 int numSsid = WiFi.scanNetw
5 if (numSsid == -1)
6 {
7   Serial.println("Couldn't
8   while (true);
9 }
10 
11 // print the list of networ
12 Serial.print("number of ava
13 Serial.println(numSsid);
14 
15 // print the network number
16 for (int thisNet = 0; thisN
17   Serial.print(thisNet + 1)
18   Serial.print(") ");
19   Serial.print("Signal: ");
20   Serial.print(WiFi.RSSI(th
21   Serial.print(" dBm");
22   Serial.print("\tChannel:
23   Serial.print(WiFi.channel
24   byte bssid[6];
25   Serial.print("\t\tBSSID:
26   printMacAddress(WiFi.BSSI
27   Serial.print("\tEncryptio
28   printEncryptionType(WiFi.
```

<a id='d3ac184a-ba74-4509-b25c-1d613adea86a'></a>

WiFi.encryptionType()

<a id='5962878b-02fa-4661-b0d5-4533529b17a1'></a>

## Description

Gets the encryption type of the current network

<a id='6f593ada-228a-4320-9834-2cf92e481a31'></a>

## Syntax

```
1 WiFi.encryptionType();
2 WiFi.encryptionType(wifiAccessP
```

<a id='a76378e4-273e-4eef-bc9d-958e98b7a81a'></a>

## Parameters

wifiAccessPoint: specifies which network to get information from

<a id='936969b5-a36e-4a1f-a721-198620bd19c1'></a>

## Returns

byte : value represents the type of encryption

<a id='65222850-2fa7-4f08-b38b-9744b79331c2'></a>

TKIP (WPA) = 2

WEP = 5

<a id='d0933840-a4b8-4f60-a526-9de198f6816c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='54529465-8d9b-472f-93ac-a57f300633fc'></a>

15/30

<!-- PAGE BREAK -->

<a id='6b5948d7-4dd0-470d-941e-7fddaa84771c'></a>

12/4/25, 2:52 PM

<a id='7cd20707-2af3-4771-ab3a-6e4cc767c460'></a>

WiFiNINA | Arduino Documentation

<a id='02b97c4f-46a3-4565-b911-893003b04de2'></a>

ARDUINODOCS

<a id='8be127b5-1458-42c8-9a1f-84bf554a3eba'></a>

AUTO = 8

# Example

```c
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 //SSID of your network
5 char ssid[] = "yourNetwork";
6 //password of your WPA Network
7 char pass[] = "secretPassword";
8 
9 void setup() {
10   WiFi.begin(ssid, pass);
11 
12   if (status != WL_CONNECTED) {
13     Serial.println("Couldn't get connected");
14     while(true);
15   }
16   // if you are connected, print the encryption type
17   else {
18     byte encryption = WiFi.encryptionType();
19     Serial.print("Encryption Type: ");
20     Serial.println(encryption, HEX);
21   }
22 }
23 
24 void loop () {}
```

<a id='f15abd79-fdda-40da-bf43-a261b20f767f'></a>

WiFi.scanNetworks()

<a id='b5d2a90e-398a-4814-9bbd-8459962c37eb'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='beb17267-65b9-4925-beac-196ac32a3c60'></a>

16/30

<!-- PAGE BREAK -->

<a id='4465869f-bc25-4ab2-880b-59f41f23188c'></a>

12/4/25, 2:52 PM

<a id='570f6c83-95cf-48a9-babc-aa784bef9e3a'></a>

WiFiNINA | Arduino Documentation

<a id='d5fed216-289b-4964-9f6b-d64570c2599a'></a>

ARDUINODOCS

<a id='dfc7b26e-95f6-4eaa-893a-e7efd19e2c88'></a>

## Description

Scans for available WiFi networks and returns the discovered number

<a id='a45fd6ab-e4c7-4769-bd71-5ccd4b01e17d'></a>

## Syntax

```
1 WiFi.scanNetworks()
```

<a id='c613a30b-3f1a-4a26-bf84-7384ffce763e'></a>

Parameters

None

<a id='03b325d5-8694-4c75-af47-cc141db592a8'></a>

## Returns

byte : number of discovered networks

<a id='ae88d1ec-6a6e-45f3-b374-28e5a49d86d8'></a>

# Example
```
/*
This example prints the boar
scans for available WiFi net
Every ten seconds, it scans
connect to any network, so n

Circuit:
* Board with NINA module (Ar

created 13 July 2010
by dlf (Metodo2 srl)
modified 21 Junn 2012
by Tom Igoe and Jaymes Dec
*/

#include <SPI.h>
#include <WiFiNINA.h>

void setup() {
  //Initialize serial and wai
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port
  }

  // check for the WiFi modul
  if (WiFi.status() == WL_NO_
```

<a id='5e863048-30c7-48e2-8637-b1cde58091ea'></a>

v WiFi.ping()

<a id='867b10dc-ac3b-442e-ab09-acd54abad47c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='9fd738b4-8b9b-4e7c-8c8c-f7f6e96e5985'></a>

17/30

<!-- PAGE BREAK -->

<a id='e7eead98-3007-4dd6-b54c-02fa722c2c04'></a>

12/4/25, 2:52 PM

<a id='868a7987-6eb7-4617-a1fa-451cda1f5bbd'></a>

WiFiNINA | Arduino Documentation

<a id='cad5c783-c5a8-4418-8f25-af9739195019'></a>

ARDUINODOCS

<a id='5f216f59-5a7e-4dda-b4ee-01de4d0b4160'></a>

Ping a remote device on the network.

<a id='c3714269-2cc6-4ec6-8b3f-7c53a94b5295'></a>

# Syntax

```
1 WiFi.ping(ip);
2 WiFi.ping(ip, ttl);
3 WiFi.ping(host);
4 WiFi.ping(host, ttl);
```

<a id='3f4d81ac-7dfb-40f3-beb6-fa59e8343306'></a>

## Parameters

ip: the IP address to ping (array of 4 bytes)
host: the host to ping (string)
ttl: Time of live (optional, defaults to 128). Maximum number of routers the request can be forwarded to.

<a id='ec685e79-2686-4b22-9362-5960aebbe1e6'></a>

## Returns

WL_PING_SUCCESS when the ping was successful

WL_PING_DEST_UNREACHABLE when the destination (IP or host is unreachable)

WL_PING_TIMEOUT when the ping times out

WL_PING_UNKNOWN_HOST when the host cannot be resolved via DNS

WL_PING_ERROR when an error occurs

<a id='146e15b6-78fc-4e06-b651-2792f815eb0d'></a>

Example

________________________________________________________________________________

<a id='4da2f4c8-fee1-405c-bb8f-60d54cf938d7'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='67f2efe9-8545-4ea0-a6f3-245d0e3c03b6'></a>

18/30

<!-- PAGE BREAK -->

<a id='bef74c83-7928-4aec-8adf-a17bad4ae902'></a>

12/4/25, 2:52 PM

<a id='8be368e7-b4f3-4fe2-9a77-561efab87f8d'></a>

WiFiNINA | Arduino Documentation

<a id='0891a047-b75c-4615-ad05-d075a0ec391c'></a>

ARDUINODOCS

<a id='2219a809-8a4e-42d3-a7a4-db73bb35bd8c'></a>

```
/*
This example connects to an
Then it prints the MAC address and
the IP address obtained, and
Then it continuously pings

Circuit:
* Board with NINA module (Arduino

created 13 July 2010
by dlf (Metodo2 srl)
modified 09 June 2016
by Petar Georgiev
*/
#include <SPI.h>
#include <WiFiNINA.h>

#include "arduino_secrets.h"
//////// please enter your credentials in arduino_secrets.h
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int status = WL_IDLE_STATUS;

// Specify IP address or host
String hostName = "www.google.com";
int pingResult;

void setup() {
  // Initialize serial and wait for port to open:
```

<a id='40775030-5bde-4b7b-8d50-fc275ed0829f'></a>

v WiFi.status()

<a id='c2156440-bc23-4f16-b01c-d4c979d92b0f'></a>

### Description

Return the connection status.

<a id='1b449024-f863-4520-93d9-f23de9d8e58e'></a>

Syntax

```
1 WiFi.status()
```

<a id='5cfdb222-8bb2-4be8-921e-ed359f752660'></a>

Parameters

None

<a id='6b7c0af0-8100-4286-852d-7b1fa3f4b09c'></a>

Returns

WL_CONNECTED: assigned when
connected to a WiFi network;

WL_AP_CONNECTED: assigned when a
device is connected in Access Point
mode;

WL_AP_LISTENING : assigned when the
listening for connections in Access
Point mode;

<a id='80986064-760a-4ef3-81b0-4b24f05ee47f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='7e6a2bad-41af-4b3e-9b86-4f5e83caf0e0'></a>

19/30

<!-- PAGE BREAK -->

<a id='950fe3f4-8278-41cb-837f-2e0fa896bb40'></a>

12/4/25, 2:52 PM

<a id='d6a75bdc-1393-40eb-bb98-84b2f63ea1bf'></a>

WiFiNINA | Arduino Documentation

<a id='955be11e-cedb-47cc-986f-70b3e22f4e66'></a>

ARDUINODOCS

<a id='81c943a9-b290-47c8-8633-90885610926d'></a>

WL_NO_MODULE: assigned when the
communication with an integrated
WiFi module fails;
WL_IDLE_STATUS: it is a temporary
status assigned when WiFi.begin() is
called and remains active until the
number of attempts expires (resulting
in WL_CONNECT_FAILED) or a
connection is established (resulting in
WL_CONNECTED);
WL_NO_SSID_AVAIL: assigned when no
SSID are available;
WL_SCAN_COMPLETED: assigned
when the scan networks is completed;
WL_CONNECT_FAILED: assigned when
the connection fails for all the
attempts;
WL_CONNECTION_LOST: assigned
when the connection is lost;
WL_DISCONNECTED: assigned when
disconnected from a network;

<a id='aa95b717-0f10-4437-a6f3-651c42830af4'></a>

Example

```
#include <SPI.h>
#include <WiFiNINA.h>

char ssid[] = "yourNetwork";
char key[] = "DØDØDEADFØDABB";
int keyIndex = 0;
int status = WL_IDLE_STATUS;

void setup() {
  //Initialize serial and wai
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port
  }

  // attempt to connect to Wi
  while (status != WL_CONNEC) {
    Serial.print("Attempting");
    Serial.println(ssid);
    status = WiFi.begin(ssid, key);
  }

  // wait 10 seconds for co
  delay(10000);

  // once you are connected :
  Serial.print("You're connec");
}
```

<a id='4c598a92-9a11-4b1c-9a73-6f987e3010e6'></a>

WiFi.macAddress()

<a id='cb238207-bb09-4d15-b1a4-836c1109d81e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='08998486-4938-4498-8c7e-bf7001090375'></a>

20/30

<!-- PAGE BREAK -->

<a id='3273760a-c799-45cb-a2db-d9d2f2fb9310'></a>

12/4/25, 2:52 PM

<a id='ba3497f5-d776-4390-836b-6335270771af'></a>

WiFiNINA | Arduino Documentation

<a id='ba61cb0e-71c2-477c-bae9-44c34405560d'></a>

ARDUINODOCS

<a id='bcb78b8d-8870-44bd-8f33-825e89c4d848'></a>

Description

Gets the MAC Address of your WiFi NINA
module

<a id='b14ade21-e8dc-40fb-9b76-76e660783e4d'></a>

## Syntax

```
1 WiFi.macAddress(mac)
```

<a id='246206c4-4098-4ee8-9c84-e57909c8257e'></a>

## Parameters

mac: a 6 byte array to hold the MAC address

<a id='dbff5cd1-2801-471a-9c78-f6e36574effc'></a>

## Returns

byte array : 6 bytes representing the MAC address of your module

<a id='7430f287-fdbd-4b7c-b464-10643c10c342'></a>

Example

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3
4 char ssid[] = "yourNetwork";
5 int status = WL_IDLE_STATUS;
6
7 byte mac[6];
8
9
10 void setup()
11 {
12   Serial.begin(9600);
13
14   status = WiFi.begin(ssid);
15
16   if (status != WL_CONNECTED)
17     Serial.println("Couldn't
18     while(true);
19   }
20   // if you are connected, pr
21   else {
22     WiFi.macAddress(mac);
23     Serial.print("MAC: ");
24     Serial.print(mac[5], HEX);
25     Serial.print(":");
26     Serial.print(mac[4], HEX);
27     Serial.print(":");
28     Serial.print(mac[3], HEX);
30
```

<a id='9b7d5576-6d9f-48dc-92df-d0a705001a3d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='ec4a2813-8731-4d43-9996-1a1f69993d07'></a>

21/30

<!-- PAGE BREAK -->

<a id='14ac22f7-1277-4e4e-8003-8f63b503d5ae'></a>

12/4/25, 2:52 PM

<a id='3a7751cb-4d00-40fe-b104-0df5153d542d'></a>

WiFiNINA | Arduino Documentation

<a id='3f834fbd-7ca9-419b-8182-4c442fbb2220'></a>

ARDUINODOCS

<a id='2611c8bd-2b95-464a-986b-4dde819e8895'></a>

# Description

Returns the firmware version running on the module as a string.

<a id='f252d268-6ad5-4fb1-b476-5621eb56d9b7'></a>

## Syntax

```
1 WiFi.firmwareVersion()
```

<a id='2ac0f700-f3d4-4671-8440-023f404943b9'></a>

Parameters

None

<a id='1cc67f62-1341-4e15-b95d-0ec4d3721de3'></a>

**Returns**

The firmware version running on the module as a string

<a id='2b0f3296-3595-40a3-b352-65b64dc57fb5'></a>

Example

```
1 ...
2 String fv = WiFi.firmwareVersio
3 if (fv < "1.0.0") {
4     Serial.println("Please upgrad
5 }
6 ...
```

<a id='d7c6c412-fa19-4f18-ad57-c41a17a12b67'></a>

⌄ WiFi.lowPowerMode()

<a id='1e6f1f5f-a55c-48c9-9635-8605d3e7d68e'></a>

# Description

Enable low power mode. This is an automatically managed mode where the WiFi NINA Module reduces its power drain bringing the overall power consumption to 30 mA. Any incoming data is received and the device sends out regularly the beacon signal each 100 ms to keep the AP connection alive.

<a id='2f3854c5-b426-4fb1-b727-0065d54ea002'></a>

## Syntax

```
1 WiFi.lowPowerMode()
```

<a id='c2cddecb-5443-4d53-b492-0cdc68607d1c'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='5570462a-8bc6-43ae-a393-a3473a860048'></a>

22/30

<!-- PAGE BREAK -->

<a id='1281dac2-bc1a-414b-88bf-818cf1d52de3'></a>

12/4/25, 2:52 PM

<a id='629f6a4c-eafe-46ca-8460-2afdda9ecd09'></a>

WiFiNINA | Arduino Documentation

<a id='d527fbbe-8fc1-4ac5-b19b-7ae9c4e60a65'></a>

ARDUINODOCS

<a id='2a4613c2-b0ed-4360-bc11-9316b483f44e'></a>

Returns
None

<a id='7922312e-0266-478c-83d5-dae1b0b57523'></a>

WiFi.noLowPowerMode()

<a id='38957334-fc50-4d6d-abdc-e65b58bfd7c7'></a>

Description

Disables the power saving modes enabled
with lowPowerMode(). This is the default
status of Power Mode.

<a id='f3d3dbc1-015e-4e69-bd35-be7cf13d57bc'></a>

# Syntax

```
1 WiFi.noLowPowerMode()
```

<a id='166dcff1-ed31-44d5-93a8-cca2b4f4d230'></a>

Returns

None

<a id='5623d4a3-beeb-46d2-bceb-31f508e02e63'></a>

WiFi.reasonCode()

<a id='d0129aef-5b45-4ade-b7a9-7fddeeb50285'></a>

# Description

Return The deauthentication reason code.

<a id='cd516885-f607-40af-93fc-141a8186c8af'></a>

## Syntax

```
1 WiFi.reasonCode()
```

<a id='038a3319-6327-4c2d-b8ac-583597ff8541'></a>

Parameters

None

<a id='ff59ee79-4f44-4cd6-af42-79dd73609f1e'></a>

Returns

The deauthentication reason code

<a id='5d93a157-bda7-4ca4-ac30-1f05d0f149f1'></a>

Example

[  ]

<a id='731fa18b-b546-43a4-a401-816920fe7485'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='4de9705d-e19d-4988-9177-d0922022e716'></a>

23/30

<!-- PAGE BREAK -->

<a id='b9c9543c-7175-4d92-a503-afe7fb5bc0e5'></a>

12/4/25, 2:52 PM

<a id='b41db34d-c70f-4211-a7aa-6e75e1583f3e'></a>

WiFiNINA | Arduino Documentation

<a id='831af1c5-f071-4a41-a07b-e58b27998f80'></a>

ARDUINODOCS

<a id='ba28cc91-c0c8-4827-ad18-13127d1b9761'></a>

```
1 ...
2 
3 while (status != WL_CONNECTED) {
4     Serial.print("Attempting to connect to SSID: ");
5     Serial.println(ssid);
6     // Connect to WPA/WPA2
7     status = WiFi.begin(ssid, password);
8     if (status != WL_CONNECTED) {
9 
10         Serial.print("Connection failed, retrying...");
11         Serial.println();
12     }
13 }
14 // wait 10 seconds for
15 delay(10000);
16 }
17 
18 ...
```

<a id='e4a1693d-a78c-4460-ae35-47fdbad439d0'></a>

WiFi.hostByName()

<a id='358060fb-a530-45fd-9dae-b728bd925d48'></a>

## Description

Resolve the given hostname to an IP
address

<a id='69c71c01-6fa4-46ee-9b3b-f02bbbd552c0'></a>

# Syntax

```
1 WiFi.hostByName(hostname, resul
```

<a id='6fbfbad1-edad-4876-a034-954955073447'></a>

# Parameters

hostname: Name to be resolved

result: IPAddress structure to store the
returned IP address

<a id='883e545a-b44d-4805-97cc-2c726328323f'></a>

# Returns

1 if hostname was successfully
converted to an IP address, else the
error code

<a id='7ae30a0b-6492-44ec-8488-98d5174ef148'></a>

Example

[ ]

<a id='e23e6cfc-92a3-4a84-b862-461c89a9aff5'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='de601b82-131e-4af7-a98f-e15b66c97d09'></a>

24/30

<!-- PAGE BREAK -->

<a id='3e6bed45-6c44-473d-9f0e-1e75fae44e54'></a>

12/4/25, 2:52 PM

<a id='26ec5d5f-6b08-461e-91f7-4be0b2c38676'></a>

WiFiNINA | Arduino Documentation

<a id='65be345a-7231-47dc-96bf-a0d6d597ebb2'></a>

ARDUINODOCS

<a id='622b3db3-16b9-4ce4-8dc4-9f513a72c40f'></a>

1
...
3 while (status != WL_CONNECTED) {
4     Serial.print("Attempting to connect to ");
5     Serial.println(ssid);
6     status = WiFi.begin(ssid, password);
7     delay(10000);
8 }
9 Serial.println("Connected to WiFi");
10 printWifiStatus();
11
12 Serial.println("\nStarting connection to host");
13 IPAddress result;
14 int err = WiFi.hostByName(serverName, result);
15 if(err == 1){
16     Serial.print("IP address of ");
17     Serial.println(result);
18 } else {
19     Serial.print("Error code: ");
20     Serial.println(err);
21 }
22
23 ...

<a id='17297675-fa8b-47ad-ab5a-8b4300d8c604'></a>

WiFi.localIP()

<a id='3017ae07-dce7-4161-92a0-e252956f15c8'></a>

**Description**

Gets the WiFi's IP address

<a id='ca285ccb-53c4-4157-8ef4-b076a0d947f9'></a>

## Syntax

```
1 WiFi.localIP()
```

<a id='59dfe946-f5b2-41b3-bb2a-581dc4886a8f'></a>

Parameters

None

<a id='149c9244-171e-48c8-9754-df5c69b58e55'></a>

Returns

the IP address of the board

<a id='41942b27-6acd-4119-b834-dfc3ec867615'></a>

Example

___

<a id='4186f2ce-5bbc-4c5f-96b4-58fccd10ce99'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='e22ffa3c-d2d8-4157-8624-565633a157e6'></a>

25/30

<!-- PAGE BREAK -->

<a id='3d8495ab-d1e9-4f88-aba6-f6d2fcd02fb6'></a>

12/4/25, 2:52 PM

<a id='14a5ed11-ba61-4fdb-832b-a8cde24fe630'></a>

WiFiNINA | Arduino Documentation

<a id='b2d861af-74fb-4be9-82ec-566512e5aae8'></a>

ARDUINODOCS

<a id='012ab823-bc34-4a68-bcd6-2bd33d32eb93'></a>

```c
1 #include <WiFiNINA.h>
2 
3 char ssid[] = "yourNetwork";
4 
5 int status = WL_IDLE_STATUS;
6 
7 IPAddress ip;
8 
9 void setup()
10 {
11   // initialize serial:
12   Serial.begin(9600);
13 
14   WiFi.begin(ssid);
15 
16   if ( status != WL_CONNECTED ) {
17     Serial.println("Couldn't");
18     while(true);
19   }
20   // if you are connected, pr
21   else {
22     //print the local IP address
23     ip = WiFi.localIP();
24     Serial.println(ip);
25   }
26 }
27 }
28 
29 // void loop() {
```

<a id='c5d238fc-2ee4-4469-957d-5fdc5515e0ed'></a>

WiFi.subnetMask()

<a id='35de8c9a-8ee2-4544-b8df-0653c5555279'></a>

### Description

Gets the WiFi's subnet mask

<a id='2b72a433-a8d7-4ea4-9313-8acf657b820c'></a>

## Syntax

```
1 WiFi.subnet()
```

<a id='6c7c1434-6c37-4627-ac9e-e8e27d8125fc'></a>

Parameters

None

<a id='93add709-6064-4712-9655-51979bd68b77'></a>

Returns

the subnet mask of the board

<a id='21c8b18b-0a36-4d90-a3ca-7e5d285739e8'></a>

Example

____________________________________________________________________

<a id='f5231257-f302-4c23-bb67-8826af39d58d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='271dde9e-6508-4001-b3d0-d059400300fb'></a>

26/30

<!-- PAGE BREAK -->

<a id='cfcced9d-9215-4fc0-bd10-c5ba51206ec6'></a>

12/4/25, 2:52 PM

<a id='74248961-8432-441f-98fc-1ae697076fe6'></a>

WiFiNINA | Arduino Documentation

<a id='30721c3a-9813-4e2f-8e5d-ada498cd5d3b'></a>

ARDUINODOCS

<a id='d0ebae58-e9b8-4abc-ac82-76179d7bba33'></a>

```cpp
1 #include <WiFiNINA.h>
2 int status = WL_IDLE_STATUS;
3 
4 //SSID of your network
5 char ssid[] = "yourNetwork";
6 //password of your WPA Networ
7 char pass[] = "secretPassword";
8 
9 IPAddress ip;
10 IPAddress subnet;
11 IPAddress gateway;
12 
13 void setup()
14 {
15   WiFi.begin(ssid, pass);
16 
17   if ( status != WL_CONNECTED ) {
18     Serial.println("Couldn't");
19     while(true);
20   }
21   // if you are connected, pr
22   else {
23 
24     // print your subnet mask
25     subnet = WiFi.subnetMask();
26     Serial.print("NETMASK: ");
27     Serial.println();
28   }
29 }
```

<a id='7a598e5e-c1da-415b-84a8-8c39296ad448'></a>

# WiFi.gatewayIP()

## Description
Gets the WiFi's gateway IP address.

## Syntax
```
1 WiFi.gatewayIP()
```

## Parameters
None

## Returns
An array containing the board's gateway IP address

## Example

<a id='53ba1878-43cf-48b8-8779-fac5ab0fd998'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='8f76b906-1293-45bf-844c-f11fecb5b555'></a>

27/30

<!-- PAGE BREAK -->

<a id='f357885c-56cf-405f-b266-64e04b879947'></a>

12/4/25, 2:52 PM

<a id='ea7b49a1-01fe-4041-af05-9548563418e4'></a>

WiFiNINA | Arduino Documentation

<a id='4e4eb69f-1d10-406b-b581-b0d075ee4db3'></a>

ARDUINODOCS

<a id='48d4afb8-f3d3-4966-9483-483d786137e2'></a>

```cpp
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 int status = WL_IDLE_STATUS;
5 
6 //SSID of your network
7 char ssid[] = "yourNetwork";
8 //password of your WPA Network
9 char pass[] = "secretPassword";
10 
11 IPAddress gateway;
12 
13 void setup()
14 {
15   Serial.begin(9600);
16 
17   WiFi.begin(ssid, pass);
18 
19   if ( status != WL_CONNECTED ) {
20     Serial.println("Couldn't");
21     while(true);
22   }
23   // if you are connected, print
24   else {
25 
26     // print your gateway address
27     gateway = WiFi.gatewayIP();
28     Serial.print("GATEWAY: ");
29     Serial.println(gateway);
30   }
```

<a id='687cb252-9f60-4e75-aca5-7ed134224fb5'></a>

WiFi.dnsIP()

# Description
Returns the DNS server IP address for the device.

# Syntax
```
1 WiFi.dnsIP()
2 WiFi.dnsIP(n)
```

# Parameters
optional parameter n for the number of the DNS server to get the second DNS serverv

# Returns
the DNS server IP address for the device (IPAddress).

# Example

<a id='d4963e22-0165-4be0-9188-d5a257a8687e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='1b66043b-65c8-4e79-a609-e5dd6f9890c6'></a>

28/30

<!-- PAGE BREAK -->

<a id='4f29e42c-7c9f-4f0b-b687-a3570caedbfe'></a>

12/4/25, 2:52 PM

<a id='d10a5a39-0c14-4362-9fba-6a826456e265'></a>

WiFiNINA | Arduino Documentation

<a id='d4363d70-c98a-4ae3-a614-06795f1d10c3'></a>

ARDUINODOCS

<a id='29aab0ff-35a9-45af-b0cf-e22f99c8cc98'></a>

```cpp
#include <WiFiNINA.h>

#include "arduino_secrets.h"
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;

IPAddress emptyIP;

void setup() {
  Serial.begin(115200);
  while (!Serial) {}

  Serial.print("Attempting to ");
  Serial.println(ssid);
  int status = WiFi.begin(ssid, pass);
  if (status != WL_CONNECTED) {
    Serial.println("Couldn't connect");
    while(true);
  }

  Serial.print("DHCP assigned ");
  IPAddress dns1 = WiFi.dnsIP();
  if (dns1 == emptyIP) {
    Serial.println("not set");
  } else {
    dns1.printTo(Serial);
    Serial.println();
  }
  // ... code continues
}
```

<a id='22ac221b-9df2-48dc-be4d-e52e4d0652fc'></a>

WiFi.getTime()

<a id='84c5a9b6-f78c-4b3e-a0a6-ba41222f944b'></a>

# Description

Get the time in seconds since January 1st,
1970. The time is retrieved from the WiFi
module which periodically fetches the NTP
time from an NTP server.

<a id='37647c0a-4af0-4ba4-8132-8e9a880975e4'></a>

## Syntax

```
1 WiFi.getTime();
```

<a id='63f5c687-84e0-41da-95b5-a6757663c944'></a>

Parameters

None

<a id='6a4e2d83-bdd1-489b-a099-8bf218507b04'></a>

# Returns

Returns the time in seconds since January 1st, 1970 on success. O on failure.

<a id='56d3f5ff-a268-4ca1-b402-68d0d8cf0c7e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='e3a675c0-a0df-44ef-a7f1-cd193a16b5bd'></a>

29/30

<!-- PAGE BREAK -->

<a id='9a59da3f-1132-4202-9b9e-d5d377670fba'></a>

12/4/25, 2:52 PM

<a id='09a900fd-10a0-4863-a23b-efca2e83e3bb'></a>

WiFiNINA | Arduino Documentation

<a id='d708af6c-3cd1-43ac-ae06-c7c73fe6b0eb'></a>

ARDUINODOCS

<a id='dee12ee3-f5af-4468-a228-33c01db0f5f4'></a>



<a id='c7fc1bd3-2819-4d31-aacf-58ba73170227'></a>

Was this article helpful?

option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='49869535-9888-4c07-8ede-5cc7194eafdc'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='b0661fdf-9009-4671-9c6c-05e158465b7e'></a>

© 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='0cf9beba-680b-424f-9880-a9c988ee807e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifi-library.html

<a id='1375cc23-9f95-4b69-a606-baf6667544e4'></a>

30/30