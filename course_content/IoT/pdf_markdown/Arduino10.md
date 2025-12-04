<a id='0579fcdc-0ded-4a5e-a638-8d2f22020f97'></a>

12/4/25, 2:52 PM

<a id='1f47efa0-8344-4440-aa4f-2053be98d6ab'></a>

WiFiNINA | Arduino Documentation

<a id='bfdf50c9-ed82-4c20-bfec-923f9c790ac4'></a>

ARDUINODOCS

<a id='d6a77d2e-71bb-4673-a28d-b2824ecb8692'></a>

Search on Docs /

<a id='bddbc484-848a-4d5c-a4fd-8a75e3dd7ddc'></a>

← Go Back

Library

<a id='66b5a1e1-946f-4568-8bc1-884436a3c698'></a>

Recents viewed

<a id='8c4eabf8-5c95-4581-8ea8-03946b7e4eab'></a>

- WiFiNINA
- Arduino SigFox for
  MKRFox1200
- autowp-mcp2515
- Arduino_MKRENV
- Arduino_MKRGPS
- Arduino_APDS9960
- Arduino_MKRIoTCarrier

<a id='59723ef1-42ee-4b12-bcee-e6e39d4f1c80'></a>

Home / Programming / Library / WiFiNINA

<a id='a77241f3-6ded-45a3-a141-cc7d89cccd7f'></a>

COMMUNICATION
# WiFiNINA

ARDUINO LGPL-2.1 V1.9.1 Arduino 20/03/2025

<a id='a9e7e3f2-5f01-4cc2-84a4-3d4167182d45'></a>

Arduino <info@arduino.cc>
http://www.arduino.cc/en/Ref... info@arduino.cc

<a id='9606fa83-d7c4-49cb-8281-3ae9d8fcad81'></a>

Enables network connection (local and Internet) with the
Arduino MKR WiFi 1010, Arduino MKR VIDOR 4000,
Arduino Uno WiFi Rev.2 and Nano 33 IoT.

<a id='d095e902-9d72-40f3-9fca-d8a62e17a127'></a>

With this library you can instantiate Servers, Clients
and send/receive UDP packets through WiFi. The
board can connect either to open or encrypted
networks (WEP, WPA). The IP address can be
assigned statically or through a DHCP. The library
can also manage DNS.

<a id='14418d04-0aee-4cc6-9d07-5ab6921846c6'></a>

GO TO REPOSITORY

<a id='2ea28c5b-a6c6-407f-b25c-52d1d010024c'></a>

Usage/Examples Compatibility Releases

This library allows you to use the Arduino Uno WiFi Rev.2, Arduino Nano 33 IoT, Arduino MKR 1010 and Arduino MKR VIDOR 4000 WiFi capabilities. It can serve as either a server accepting incoming connections or a client making outgoing ones. The library supports WEP, WPA2 Personal and WPA2 Enterprise encryptions. This library supports all the same methods of the original WiFi library plus the connectSSL(). The WiFININA library is very similar to the Ethernet and the WiFi library, and many of the function calls are the same.

<a id='fa7f9a72-e698-4031-b4fd-284a344f3936'></a>

To use this library:

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
```

<a id='7badc199-7322-40a1-8072-13f7b4995877'></a>

# Examples

Several examples for the **WiFiNINA** library are available from the **Examples from Libraries** page.

<a id='1eae9b8b-3888-4cb4-b97e-86e680be48aa'></a>

ON THIS PAGE

- Usage/Examples
- Compatibility
- Releases
  - WiFi Class +
  - Client Class +
  - Server Class +
  - UDP Class +

<a id='aeaac052-2138-47d7-8814-2d62d7e7354e'></a>

WiFi Class Client Class Server Class

UDP Class

<a id='c2280105-f065-4304-a4b8-07ab92c01125'></a>

Help

<a id='79f9a855-2f56-46e6-984c-10e9827654c9'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='dbb7e04f-3d33-4d2d-b1c4-6e87b0deade9'></a>

1/16

<!-- PAGE BREAK -->

<a id='cc31447b-6cfb-4f37-8e53-f11c8591b53f'></a>

12/4/25, 2:52 PM

<a id='8d997c8f-ce25-4f24-88b9-f2a68d38e61a'></a>

WiFiNINA | Arduino Documentation

<a id='b4ea99f6-bc7c-4425-9b31-f7a5b999b962'></a>

ARDUINODOCS

<a id='6cddb6c0-321b-4bcd-9716-13422802077e'></a>

## Description

Client is the base class for all WiFi client based calls. It is not called directly, but invoked whenever you use a function that relies on it.

<a id='08c664fd-e358-46b9-92c4-7c6f37710c00'></a>

WiFiClient()

<a id='a65d766b-3513-4e59-b3c9-b1c2a5978a4b'></a>

# Description

Creates a client that can connect to to a specified internet IP address and port as defined in client.connect().

<a id='da079377-7a21-4a0b-bddb-ebd5f1b20553'></a>

## Syntax

```
1 WiFiClient client;
```

<a id='0e125739-e4a5-43bb-8c70-3e893d2b1af3'></a>

## Parameters

client : the named client to refer to

<a id='00745531-31c9-4863-8088-76a95f4f12d2'></a>

Returns

None

<a id='3c950694-287d-4302-80db-5541ee0e0d41'></a>

Example

____________________

<a id='d25f3f6e-4a48-4879-b9dd-008a21537b98'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='ce8acfbc-4428-4543-bd95-6b6f96cb6512'></a>

2/16

<!-- PAGE BREAK -->

<a id='452c7d33-93af-458d-886b-9fb357371ff3'></a>

12/4/25, 2:52 PM

<a id='c15d43ab-9a4b-41b5-a331-d9ff33bc8c54'></a>

WiFiNINA | Arduino Documentation

<a id='e633d4f6-9755-430f-9178-8e8461cdda29'></a>

ARDUINODOCS

<a id='49b060e5-d1b7-4210-adc2-4b986b299086'></a>

```c
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 char ssid[] = "myNetwork";
5 char pass[] = "myPassword";
6 
7 int status = WL_IDLE_STATUS;
8 IPAddress server(74, 125, 115, 1);
9 
10 // Initialize the client libr
11 WiFiClient client;
12 
13 void setup() {
14 Serial.begin(9600);
15 Serial.println("Attempting");
16 Serial.print("SSID: ");
17 Serial.println(ssid);
18 
19 status = WiFi.begin(ssid, pass);
20 if ( status != WL_CONNECTED ) {
21 Serial.println("Couldn't");
22 // don't do anything else
23 while(true);
24 }
25 else {
26 Serial.println("Connected");
27 Serial.println("\nStartin");
28 // if you get a connectio
```

<a id='c5b5550f-5250-4c18-8331-c9280a167fb2'></a>

WiFiSSLClient

<a id='507206e0-c1a9-425c-8fff-cadf190e6830'></a>

## Description

This class allows to create a client that always connects in SSL to the specified IP address and port, even if client.connect() is used instead of client.connectSSL(). This is useful If you have a library that accepts only plain Client, but you want to force it to use SSL, keeping the same method names of the non SSL client.

<a id='586ea1b3-512b-4c01-9219-e5dad22ce67c'></a>

## Syntax

```
1 WiFiNINASSLClient client;
```

<a id='d79b2bfe-eb89-4dcc-939f-878f80089624'></a>

# Parameters

client : the named client to refer to

<a id='a7a41ef8-fa25-4105-81dc-c84215646cc6'></a>

Return

None

<a id='159e7c1d-8db3-4a69-895b-27f2e91c4925'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='b9e1d922-2e58-484c-9cf4-0fc24a0d72fe'></a>

3/16

<!-- PAGE BREAK -->

<a id='09c002c3-8b4a-4265-b72d-e65eb00c6359'></a>

12/4/25, 2:52 PM

<a id='8e1040c5-0d33-4d4c-9221-a9c5d5103773'></a>

WiFiNINA | Arduino Documentation

<a id='b15164dc-a07b-41c2-b8de-90cf35f20110'></a>

ARDUINODOCS

<a id='42f2873e-7836-4018-9466-08bc6bf3bdde'></a>

An empty rectangular box.

<a id='1f72e5fd-9008-4952-960d-2fc30783b717'></a>

Example

```
1 /*
2 This example creates a client
3 data using always SSL.
4
5 It is compatible with the met
6 connections, like client.conn
7
8 Written by Arturo Guadalupi
9 last revision November 2015
10
11 */
12
13 #include <SPI.h>
14 #include <WiFiNINA.h>
15
16 #include "arduino_secrets.h"
17 /////please enter your sens
18 char ssid[] = SECRET_SSID;
19 char pass[] = SECRET_PASS;
20 int keyIndex = 0;
21
22 int status = WL_IDLE_STATUS;
23 // if you don't want to use D
24 // use the numeric IP instead
25 //IPAddress server(74,125,232,
26 char server[] = "www.google.c
27
28 // Initialize the Ethernet cl
29 // with the TD address and --
```

<a id='cccdf301-bc43-4d55-869b-bb2a90b22409'></a>

expand client.connected()

<a id='05a2cdcc-86fa-42b3-bfaa-ffe46903d331'></a>

## Description
Whether or not the client is connected. Note that a client is considered connected if the connection has been closed but there is still unread data.

<a id='34da3b2d-ad6e-4a4c-8025-d22b86ddb298'></a>

## Syntax

```
1 client.connected()
```

<a id='93162213-3e0a-4996-a274-0bfd0206c469'></a>

Parameters

None

<a id='d615e0b7-e15f-4e33-bed5-2314c3076f51'></a>

## Returns

Returns true if the client is connected,

<a id='a2d606f6-d4c3-4b66-b45f-4a5d1c0af53a'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='1e0c9bd2-222c-4acc-b659-43da413639a1'></a>

4/16

<!-- PAGE BREAK -->

<a id='37a6bdf2-a050-42c3-a570-14f2261f122c'></a>

12/4/25, 2:52 PM

<a id='9bcce4b0-209a-4f04-907d-15a7f70fbee8'></a>

WiFiNINA | Arduino Documentation

<a id='d7d4e1b8-d5a2-486b-bf07-6e087ff5eea1'></a>

ARDUINODOCS

<a id='04f3fb68-2a73-41e0-a1be-8f9d62617209'></a>



<a id='9227a3ee-ed54-4b73-802e-7171d08001e6'></a>

Example

```
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 char ssid[] = "myNetwork";
5 char pass[] = "myPassword";
6 
7 int status = WL_IDLE_STATUS;
8 IPAddress server(74, 125, 115, 1;
9 
10 // Initialize the client libr
11 WiFiClient client;
12 
13 void setup() {
14   Serial.begin(9600);
15   Serial.println("Attempting to connect...");
16   Serial.print("SSID: ");
17   Serial.println(ssid);
18 
19   status = WiFi.begin(ssid, pass);
20   if ( status != WL_CONNECTED) {
21     Serial.println("Couldn't connect to WiFi");
22     // don't do anything else
23     while(true);
24   } else {
25     Serial.println("Connected to WiFi");
26     Serial.println("\nStarting web server...");
27     // if you get a connectio
28     // client connect/server...
```

<a id='e4272bb7-cb85-464e-8c62-401e04edf2e7'></a>

client.connect()

<a id='bf600d8d-2bb6-42da-a483-746211db308e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='5e595790-e4da-42a7-b0e9-248acb7a805c'></a>

5/16

<!-- PAGE BREAK -->

<a id='8d7e61bb-0a5a-42c3-a071-3e387e332666'></a>

12/4/25, 2:52 PM

<a id='6b336e6a-f779-4a4f-b41b-6aba3778e5d2'></a>

WiFiNINA | Arduino Documentation

<a id='f2b3e370-1412-4add-ba5d-760adf3e7075'></a>

ARDUINODOCS

<a id='12d4e01e-5b41-439e-9d8e-7ae06abd0b9f'></a>

## Description

Connect to the IP address and port specified in the constructor. The return value indicates success or failure. connect() also supports DNS lookups when using a domain name (e.g., google.com).

<a id='9a6bb942-fafa-4f00-80a6-1e48594c611f'></a>

## Syntax

```
1 client.connect(ip, port)
2 client.connect(URL, port)
```

<a id='d39aa706-f5a1-4935-a2d7-7770030cde5a'></a>

# Parameters

ip: the IP address that the client will connect to (array of 4 bytes)

URL: the domain name the client will connect to (string e.g., "arduino.cc")

port: the port that the client will connect to (int)

<a id='f5a5c851-214c-463e-b1f6-5dfb4d84d3d1'></a>

# Returns

Returns true if the connection succeeds, false if not.

<a id='d92d6e3d-f6d4-4bd1-bb1e-9494a5371ee9'></a>

Example

____________________________________

<a id='a1f9845b-c0e9-4ea5-87e8-f5d0eddfed40'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e548320f-d190-43ce-991a-054db303525e'></a>

6/16

<!-- PAGE BREAK -->

<a id='d35485ad-a7be-474e-a22d-2f886175bdc4'></a>

12/4/25, 2:52 PM

<a id='591b2356-2341-4d88-9c20-3f93b544c586'></a>

WiFiNINA | Arduino Documentation

<a id='b0c84f2e-8c53-4878-bcb7-585404f11ba7'></a>

ARDUINODOCS

<a id='be15d152-b655-463c-bdc5-452e14f4993a'></a>

```c
#include <SPI.h>
#include <WiFiNINA.h>

char ssid[] = "myNetwork";
char pass[] = "myPassword";

int status = WL_IDLE_STATUS;
char servername[]="google.com";

WiFiClient client;

void setup() {
  Serial.begin(9600);
  Serial.println("Attempting");
  Serial.print("SSID: ");
  Serial.println(ssid);

  status = WiFi.begin(ssid, pass);
  if ( status != WL_CONNECTED ) {
    Serial.println("Couldn't");
    // don't do anything else
    while(true);
  }
  else {
    Serial.println("Connected");
    Serial.println("\nStartin");
    // if you get a connectio
    if (client.connect(server
```

<a id='8cb52e65-600c-440a-94b8-a34ed050b944'></a>

client.connectSSL()

<a id='ebb97f72-778e-4cfe-972e-8350dcfbe896'></a>

# Description
Connect to the IP address and port specified in the constructor using the SSL protocol. The method connectSSL is required when the server provides only HTTPS connections. Before using this method, it is required to load the SSL certificate used by the server into the Arduino WiFi module. The boards come already loaded with certificates and it should be ready to use. To change or upload new SSL certificates you should follow the procedures that will be made available. connectSSL() also supports DNS lookups when using a domain name (e.g., google.com).

<a id='318efe34-338f-43a5-b54d-1db8d0aa0639'></a>

# Syntax

```
1 client.connectSSL (ip, port)
2 client.connectSSL (URL, port)
```

<a id='2cd96d1e-b6ba-45a5-893d-f7780b4f1bda'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e9c41620-4a40-4d02-9a03-1748efa629d6'></a>

7/16

<!-- PAGE BREAK -->

<a id='62f26bdb-17e5-4db3-8459-698da5bd21ff'></a>

12/4/25, 2:52 PM

<a id='86610b17-ca0f-4a7e-a2c9-89ceb09fea6b'></a>

WiFiNINA | Arduino Documentation

<a id='8381096e-2ae4-45a2-9a66-f4407d7f16e0'></a>

ARDUINODOCS

<a id='5784ad36-6d78-4d88-80ca-a2769dbbf2e8'></a>

ip: the IP address that the client will connect to (array of 4 bytes)

URL: the domain name the client will connect to (string e.g., "arduino.cc")

port: the port that the client will connect to (int)

<a id='ad0d0a80-f917-417a-8194-85e1295dd7ae'></a>

## Returns

Returns true if the connection succeeds,
false if not.

<a id='5f99b9b7-b6f0-4f26-8b14-b4c87f04c383'></a>

Example

1 ...
2
3 /*
4   Web client
5
6   This sketch connects to a web client
7   using a WiFi board.
8
9   This example is written for a network with
10  WEP or WPA, change the WiFi.h library.
11
12 Circuit:
13  * WiFiNINA supported board
14
15  created 13 July 2010
16  by dlf (Metodo2 srl)
17  modified 31 May 2012
18  by Tom Igoe
19 */
20
21
22 #include <SPI.h>
23 #include <WiFiNINA.h>
24
25 char ssid[] = "yourNetwork";
26 char pass[] = "secretPassword";
27 int keyIndex = 0;
28
29 int status = WL_IDLE_STATUS;

<a id='cad0a6f5-962c-489a-8718-613831f72d9d'></a>

client.status()

## Description

Return Connection status.

<a id='2e3fa71e-8b05-454d-82ac-c04ff4784ca4'></a>

Syntax

```
client.status()
```

<a id='9f1d726b-0923-4868-a985-b503e7e11e73'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e312c4c8-df08-4eb1-a2a0-53d2f57f679a'></a>

8/16

<!-- PAGE BREAK -->

<a id='5b2cfce9-b6f2-4647-8057-99c7e22ef54c'></a>

12/4/25, 2:52 PM

<a id='0cd6cc90-673a-472d-a63d-a14b0658cf67'></a>

WiFiNINA | Arduino Documentation

<a id='be5f4cd8-176e-4c66-af92-58dcb34692f2'></a>

ARDUINODOCS

<a id='e1377ab5-044c-435f-a84c-878c176f44df'></a>

# Parameters

None

# Returns

The client connection status

# Example

```
1
2
3 void setup() {
4
5     Serial.begin(9600);
6     while (!Serial) {
7         ;
8     }
9     if (WiFi.status() == WL_NO_SOC) {
10         Serial.println("Communication with WiFi module failed!");
11         while (true);
12     }
13
14     while (status != WL_CONNECTED) {
15         Serial.print("Attempting to connect to SSID: ");
16         Serial.println(ssid);
17         status = WiFi.begin(ssid, pass);
18         delay(10000);
19     }
20     Serial.println("Connected to WiFi");
21     printWifiStatus();
22
23     Serial.println("\nStarting connection to \"www.google.com\"");
24     IPAddress result;
25     int err = WiFi.hostByName("www.google.com", result);
26     if (err == 1) {
27         Serial.print("IP address for google.com: ");
28         Serial.println(result);
29     } else {
30         Serial.print("Failed to resolve google.com: ");
```

<a id='d66b2807-59cc-4785-82a3-57e3efd08fb8'></a>

client.write()

# Description

Write data to all the clients connected to a server.

# Syntax

```
1 client.write(data)
2 client.write(buffer, size);
```

<a id='62bf3bb8-fe6e-4db4-a09c-696e86aa4089'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='1586b323-af2d-4f6e-835a-1ce4d7ca2377'></a>

9/16

<!-- PAGE BREAK -->

<a id='857d876d-18ae-434d-b36a-d789c3084fa1'></a>

12/4/25, 2:52 PM

<a id='9086759c-851e-4b96-a7dd-fa936e302f6d'></a>

WiFiNINA | Arduino Documentation

<a id='36a2922f-78a2-405b-be63-ef612827e77d'></a>

ARDUINODOCS

<a id='9422a797-0d05-4de3-b3c4-a750053493ba'></a>

data: the outgoing byte
buffer: the outgoing message
size: the size of the buffer

<a id='3ed26df2-addb-405a-9da8-5af8d13aa02b'></a>

# Returns

The number of bytes written. It is not
necessary to read this.

<a id='e5997b7b-3dae-45fc-921e-fe804f780fa2'></a>

client.print()

<a id='f9d0d1fb-2f98-4707-a5f2-1c592d3bc194'></a>

## Description

Print data to the server that a client is connected to. Prints numbers as a sequence of digits, each an ASCII character (e.g. the number 123 is sent as the three characters '1', '2', '3').

<a id='ccb691d1-6ca7-42be-9209-adf944c77131'></a>

## Syntax

```
client.print(data)
client.print(data, BASE)
```

<a id='107a18ee-9e4b-4a8e-ae38-3f9cde217ac0'></a>

# Parameters

data: the data to print (char, byte, int, long, or string)

BASE (optional): the base in which to print numbers:, DEC for decimal (base 10), OCT for octal (base 8), HEX for hexadecimal (base 16).

<a id='f4bcd83d-40b5-4ee0-82a1-0ede0d492a8a'></a>

Returns

byte : returns the number of bytes
written, though reading that number is
optional

<a id='083fb54e-2d90-45cb-88ba-a5c44b3aa8a3'></a>

client.println()

<a id='bfe53cdc-4a92-4797-a15f-8ed361563af9'></a>

# Description
Print data, followed by a carriage return and newline, to the server a client is connected to. Prints numbers as a sequence of digits, each an ASCII character (e.g. the number 123 is sent as the three characters '1', '2',

<a id='09cef40e-b280-438d-9c60-9e0c5b6649fc'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='caadd0d8-2231-47d4-aad2-1f92e5ed3f76'></a>

10/16

<!-- PAGE BREAK -->

<a id='e806efd8-858d-4da9-bea2-7a80f2a387b6'></a>

12/4/25, 2:52 PM

<a id='b72a6295-ae19-4830-9e7e-729cccabb8af'></a>

WiFiNINA | Arduino Documentation

<a id='fbf9f13b-4629-4a32-95e6-adbe79adc8c5'></a>

ARDUINODOCS

<a id='212b238c-4234-4ad2-a859-d06c0d8e929d'></a>



<a id='cc596e0a-b5e8-4fc3-b10e-c17b2dc92f7d'></a>

# Syntax

```
1 client.println()
2 client.println(data)
3 client.print(data, BASE)
```

<a id='74ddfe24-2c61-462b-82e4-d17c288f2396'></a>

# Parameters

data (optional): the data to print (char,
byte, int, long, or string)

BASE (optional): the base in which to
print numbers: DEC for decimal (base
10), OCT for octal (base 8), HEX for
hexadecimal (base 16).

<a id='3591e797-230c-4635-a041-983684d4cd0b'></a>

## Returns

byte: return the number of bytes
written, though reading that number is
optional

<a id='ad6d2c07-d466-4351-a1e9-febb8bbc143c'></a>

client.available()

<a id='f4645d9d-8e60-4579-bd1e-db9341396376'></a>

## Description

Returns the number of bytes available for reading (that is, the amount of data that has been written to the client by the server it is connected to).

<a id='e3b1820b-84b1-484f-9ba3-5e2588c7a029'></a>

available() inherits from the Stream utility class.

<a id='8b03ea34-39db-4bdf-8a99-0cbea0747887'></a>

## Syntax

```
1 client.available()
```

<a id='cd4e4a02-b291-4446-a119-28d516c517b7'></a>

Parameters

None

<a id='9e9025d9-1d60-4b75-9866-9536fa16ca35'></a>

## Returns

The number of bytes available.

<a id='85e9b110-5616-4b6e-9538-311cc15179a0'></a>

Example

<a id='81d280a5-4d7f-4ca6-8915-6250a46f3dc4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='3ca8ffb4-7eae-4e2e-8e8b-20425926a2b7'></a>

11/16

<!-- PAGE BREAK -->

<a id='0512a948-52de-4cbf-8d32-d736e7bbb1ce'></a>

12/4/25, 2:52 PM

<a id='42fa9f6c-362d-4a36-8665-a4088fa1df5f'></a>

WiFiNINA | Arduino Documentation

<a id='f478c1f3-e7fb-4791-acc5-a45f776b401b'></a>

ARDUINODOCS

<a id='2e930f36-8762-4184-b720-59551d42f9d1'></a>

```cpp
1 #include <SPI.h>
2 #include <WiFiNINA.h>
3 
4 char ssid[] = "myNetwork";
5 char pass[] = "myPassword";
6 
7 int status = WL_IDLE_STATUS;
8 char servername[]="google.com";
9 
10 WiFiClient client;
11 
12 void setup() {
13   Serial.begin(9600);
14   Serial.println("Attempting to connect to WiFi...");
15   Serial.print("SSID: ");
16   Serial.println(ssid);
17 
18   status = WiFi.begin(ssid, pass);
19   if ( status != WL_CONNECTED) {
20     Serial.println("Couldn't connect to WiFi");
21     // don't do anything else
22     while(true);
23   }
24   else {
25     Serial.println("Connected to WiFi");
26     Serial.println("\nStarting connection to server...");
27     // if you get a connection, report back via serial:
28     if (client.connect(servername, 80)) {
29       Serial.println("connected to server");
```

<a id='4e12c2a8-f1b6-4f45-9034-61950ee4b4fa'></a>

client.peek()

<a id='a2f67a0f-4a6f-4aac-ab1d-8f3156ef1edb'></a>

## Description

Read a byte from the file without advancing to the next one. That is, successive calls to peek() will return the same value, as will the next call to read().

<a id='51124554-5095-459e-98b6-ed2c6723c35e'></a>

This function inherited from the Stream
class. See the Stream class main page for
more information.

<a id='6f7d4c59-ccad-4beb-9a5e-e9f6dcc608ab'></a>

# Syntax

```
1 client.peek()
```

<a id='af73cb32-b123-4493-8ab3-4f3abd9cca6a'></a>

Parameters

None

<a id='1d1bdc13-059a-408b-a452-c073f8dcaa1c'></a>

## Returns

b: the next byte or character

<a id='ed4ebc0a-44c3-4f0a-9f28-61703c0460b5'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='e22a2339-f5a2-4434-91f2-f6b9a6ece576'></a>

12/16

<!-- PAGE BREAK -->

<a id='b8b5d425-0cf0-49dd-9a8d-3ff050d1ce5a'></a>

12/4/25, 2:52 PM

<a id='cd90b600-b744-4895-bc3c-0be0b0f48afe'></a>

WiFiNINA | Arduino Documentation

<a id='1df0594b-06fd-4829-ae13-4a30794da769'></a>

ARDUINODOCS

<a id='d054ecc2-11ed-4134-9b91-33f1b3f09ad7'></a>

Example
```c
...
#include <SPI.h>
#include <WiFiNINA.h>

#include "arduino_secrets.h"
char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
int keyIndex = 0;

int status = WL_IDLE_STATUS;
char server[] = "www.google.c


WiFiClient client;

void setup() {
  //Initialize serial and wai
  Serial.begin(9600);
  while (!Serial) {
    ;
  }

  if (WiFi.status() == WL_NO_
    Serial.println("Commu
    while (true);
  }
}
while (status != WL_CONNECT
```

<a id='0ac6a2fb-e5ea-454f-95a2-0459bd13b4f4'></a>

<::A dropdown icon followed by the text "client.read()": figure::>

<a id='06189fcf-15a9-433b-bab8-ad529f8cc890'></a>

## Description
Reads data from the client. If no arguments are given, it will return the next character in the buffer.

<a id='5bd79469-6d2d-4dba-bdd6-827d56b823f4'></a>

## Syntax

```
1 client.read()
2 client.read(buffer, size);
```

<a id='2ae3322d-05da-4ac1-9482-e51ec9f50c39'></a>

## Parameters

buffer: buffer to hold incoming
packets (char*)

len: maximum size of the buffer (int)

<a id='bdac6792-8cfa-416e-9fbe-e0c1e39dc428'></a>

Returns

<a id='2554f6ca-cb98-4da3-8813-c48a43226f57'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='48d5cfdf-ca4e-4bdc-882b-aad48983090d'></a>

13/16

<!-- PAGE BREAK -->

<a id='6769baee-0312-449c-9b4b-b2d78f9db278'></a>

12/4/25, 2:52 PM

<a id='c3f50aaf-05a8-4a89-8e85-e558fa915fa5'></a>

WiFiNINA | Arduino Documentation

<a id='579a2309-bf12-4b32-ab99-0bbbfcb70c70'></a>

ARDUINODOCS

<a id='68f7eb86-7b61-41ce-ba04-861a434f0fb5'></a>

b: the next character in the buffer
(char)
size: the size of the data
-1: if no data is available

<a id='13e11089-ec44-42e6-a388-ca73c520d7f3'></a>

client.flush()

# Description

Clears the buffer once all outgoing
characters have been sent.

flush() inherits from the **Stream** utility class.

<a id='4c58f375-0da8-41c5-8996-f9cdc4f70470'></a>

## Syntax

```
1 client.flush()
```

<a id='d1e26d22-0e1e-4db4-bc02-d962a9f8619a'></a>

Parameters

None

<a id='4d631a55-befb-4c5f-afa8-962e86c1854a'></a>

Returns
None

<a id='5dce2c80-d4c1-4439-8b22-5bab81f8bd9c'></a>

## client.stop()

### Description
Disconnect from the server.

### Syntax
```
client.stop()
```

### Parameters
None

### Returns
None

<a id='3129f531-3ca3-44d6-bb20-015fa86ca74b'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='c0e8e449-c55a-4c18-816b-4f69fe97d1c3'></a>

14/16

<!-- PAGE BREAK -->

<a id='3d27ece3-64aa-4783-b3bd-f33f506ba5d8'></a>

12/4/25, 2:52 PM

<a id='661bfa00-cf33-4ee3-9c97-2a26376e1024'></a>

WiFiNINA | Arduino Documentation

<a id='7800d2b4-c88b-4cfa-ae54-4f019c0dfb38'></a>

ARDUINODOCS

<a id='cb7f167e-f101-47e4-b7b9-44326d112278'></a>

⌄ client.remoteIP()

<a id='9489a745-fe09-4fd6-8f04-87aa54206f7d'></a>

# Description

Gets the IP address of the remote connection.

<a id='8f728d25-bc43-42c4-9fa4-88c752f73627'></a>

## Syntax

```
1 client.remoteIP()
```

<a id='584d3900-cb98-4bdf-aa30-7e62706524c6'></a>

Parameters

None

<a id='da5549f4-3c8d-42da-950e-96a7813f3baa'></a>

# Returns

The IP address of the host the client is
connected to

<a id='0fff251b-3173-4647-9194-1ccfe41f73ff'></a>

v client.remotePort()

<a id='07ccc7ab-0134-44c1-8976-43a8c78a77f0'></a>

## Description

Gets the port number of the remote connection.

<a id='8ae7c0ae-7b64-4a76-888a-76299789fcd4'></a>

## Syntax

```
1 client.remotePort()
```

<a id='ab84275d-e390-4d73-b37a-71c3d0ae3df3'></a>

Parameters

None

<a id='2683299c-9650-4b49-80ff-f3de4eba8857'></a>

### Returns

The port of the remote host that the client is connected to

<a id='8b61a9e3-8946-4b6e-8e6f-efc98d21d120'></a>

Was this article helpful?

<a id='4c898f6b-6581-4ed5-8fce-f05579f9f18d'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='cc1285ca-bd9e-419e-9622-e476218985fe'></a>

15/16

<!-- PAGE BREAK -->

<a id='d16a32b2-926d-4dba-a84e-d97a88edcc1a'></a>

12/4/25, 2:52 PM

<a id='5f142be6-28fb-4c3d-a848-4de1d8386812'></a>

WiFiNINA | Arduino Documentation

<a id='5eadef36-10de-41f2-ad68-9f6e42e7f1f9'></a>

ARDUINODOCS

<a id='c92df5d8-b151-4895-bb60-d9197d99b8e0'></a>

____________________________________________________________________________________________________

<a id='2c9a8c3b-04f9-4006-8584-00128c9b4aa7'></a>

## Connect and Contribute

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='e1f86599-4c41-4d07-b754-56ab81644b3f'></a>

© 2025 Arduino                                        Terms Of Service     Privacy Policy     Security     Cookie Settings

<a id='05224ecb-0b6f-4b98-ae97-c573e2b00f4f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='888f03c9-023d-44af-95f8-1d75a0f1f68d'></a>

16/16