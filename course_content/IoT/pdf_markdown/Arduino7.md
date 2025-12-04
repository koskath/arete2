<a id='1ae8a843-0880-4236-a91c-c0f906718335'></a>

12/4/25, 2:52 PM

<a id='01e9202a-1739-403f-ab56-69f68581dd52'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='bea3f173-b9c0-493b-8c2a-ced2d63aa6a8'></a>

ARDUINO DOCS

<a id='e58ebb5d-7a28-4495-baa8-d721b2b9bfd5'></a>

Search on Docs /

<a id='9877fb9f-809f-4d81-b783-b97bebbdefbc'></a>

← Go Back

# Hardware

---

< (navigation arrow)

<a id='6e94308d-cdff-4e5b-bd26-aace6bcb8e44'></a>

MKR GPS Shield

Tutorials
---
MKR GPS Shield Basics

<a id='f0fa55ef-c428-4f20-bb4e-bd0a4bcdd480'></a>

Home / Hardware / MKR GPS Shield / MKR GPS Shield Basics

<a id='9664b915-c2cb-4503-81b5-28ba398fce3e'></a>

# MKR GPS Shield Basics

Learn how to access GPS data from the module on board the MKR GPS Shield.

Author: Karl Söderby
Last revision: 17/07/2024

<a id='d83a91b4-8a11-453e-b45c-248a7eaa1988'></a>

# Introduction

The ability to pinpoint your exact location can be very useful for different types of projects. With the MKR GPS Shield, we can reach high accuracy with minimal power consumption.

<a id='059fe3f9-afcf-404a-aa6b-1d5c1989448c'></a>

In this tutorial, we will use a very
basic example from the
**Arduino_MKRGPS** library, which
records different geolocation data
directly from the GPS shield, and
prints them in the Serial Monitor.

<a id='a01e2521-e4be-4dd9-8508-f8098f66cde6'></a>

# Goals

The goals of this project are:

* Set up the MKR GPS Shield.
* Record longitude, latitude, speed and altitude.
* Print the data in the Serial Monitor.

<a id='c49f6e16-31ea-498e-9cd4-8f156fd4c1a4'></a>

Hardware &
Software Needed

<a id='01f748b8-2798-4ecf-8dca-1344e615e616'></a>

Arduino IDE (online or
offline).

Arduino_MKRGPS library

<a id='155825e0-badf-4601-813c-ace7e226baaa'></a>

ON THIS PAGE

<a id='b026d65e-f407-43d4-9ccf-102c9b470779'></a>

Introduction
- Goals
- Hardware & Software Needed
- Global Positioning System (GPS) —
  - Circuit
- Programming the Board
- Testing It Out —
  - Troubleshoot
- Conclusion

<a id='a273bd2f-ae18-4483-82f6-aab0ec2d11e2'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='763196b6-a54e-4ae9-8e49-29e73a25b181'></a>

1/7

<a id='dfef2815-1cce-40b3-bef6-30f5e5512b74'></a>

Help

<!-- PAGE BREAK -->

<a id='623306e7-362f-47db-aeb7-2e4f9a445393'></a>

12/4/25, 2:52 PM

<a id='4314e00e-bfed-482e-bade-6163b6191e98'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='ec0daef8-6de1-439f-84b8-f0afe9ba2f46'></a>

ARDUINO DOCS

<a id='04a55d7e-4951-4ad2-9766-846d316ef6b2'></a>



<a id='944f718f-0476-4353-935e-e87ca6f39874'></a>

MKR GPS Shield (link to store).
Arduino MKR family board (link to store).

<a id='ce7e2f11-8ec4-40db-90f8-62ddcfb1a8b5'></a>

# Global Positioning System (GPS)

The GPS is an incredible technology that is used to pinpoint an exact geographical location. Even more interesting, it uses a series of satellites orbiting the Earth to do so. Basically, a satellite in orbit continuously sends signals towards the Earth, which are picked up by GPS receivers, that exist in e.g. smartphones. As the satellite has a positioning system, it knows where it is, relative to the Earth. But this signal can only pinpoint where you are in a certain part of the world, e.g. in the Atlantic Ocean or Asia. For more accuracy, data from other satellites are also used, where for every satellite the accuracy increases.

<a id='5b5a944a-8643-4305-ab37-c981d60d0afe'></a>

It is quite spectacular, that
something 20.000 kilometers
above the Earth can pinpoint your
exact location. What is even more
interesting, is that we can create
our own projects using this
technology. The MKR GPS shield
can get extremely accurate
readings on where we are in the
world. This can be used to first
locate where we are in the world,
but we can also use it to record
for example speed.

<a id='8aba49a5-b8dc-4053-947a-165191c38281'></a>

There is, of course, much more
behind the GPS technology. If we
want to read more, why not start
at NASA's own article on how GPS

<a id='bfcef409-fdf1-43e1-96fa-e33119da93b8'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='40ebcaea-ff07-49ef-8613-99eb0fbe71b2'></a>

2/7

<!-- PAGE BREAK -->

<a id='a3b2367b-97a8-487f-9edc-996fd74fd39b'></a>

12/4/25, 2:52 PM

<a id='5c05efa9-abbb-444a-8c40-701c1a3884d2'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='46a70e3f-b396-4aad-a6ab-03476d8466d8'></a>

ARDUINODOCS

<a id='3e309b8b-03e9-4cc7-ad2a-bf9107fa48b1'></a>

# Circuit

The circuit in this tutorial is pretty
simple, and the simplest assembly
is to connect an I2C cable from a
MKR board directly to the MKR
GPS Shield. This cable comes with
every GPS shield, and has an
ESLOV connector at each

<a id='15e8e2eb-1cf3-491a-80be-735f0e4311be'></a>

<::logo: [Not a Logo]
[No readable text]
[No notable visual elements]::>

<a id='05789e39-a902-4c55-b2b4-5751eb32148e'></a>

If you are using a third party cable to connect the MKR board and MKR GPS Shield via I2C, make sure the cable is wired identically to the cable that comes with the shield.

<a id='5ff27b31-98a1-494e-b4a6-2b6b180dd3a8'></a>

Programming the Board

<a id='c1f03eea-4da9-492b-b0e9-1b18000ddda2'></a>

We will now get to the
programming part of this tutorial.

1. First, let's make sure we have
the drivers installed for the board
we are using. If we are using the
Cloud Editor, we do not need to
install anything. If we are using an
offline editor, we need to install it
manually. This can be done by
navigating to **Tools > Board >**
**Board Manager**.... Here we need
to look for the **Arduino SAMD**
**boards (32-bits Arm® Cortex®-**
**M0+)** and install it.

<a id='24d8c736-0dc4-47a9-ad27-13756ded18d0'></a>

2. Now, we need to install the
library needed. If we are using the
Cloud Editor, there is no need to

<a id='da2dd7aa-f119-4757-ba3f-3fdd54349a87'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='8fe79c88-a9a1-47ca-9512-a4630efb9684'></a>

3/7

<!-- PAGE BREAK -->

<a id='fc58b8fc-c18d-48df-b654-5b8addacedd9'></a>

12/4/25, 2:52 PM

<a id='360af965-6e2a-46b1-917d-8a766b2d51f7'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='f43f2bab-62c8-4665-9080-dc398b7f5b33'></a>

ARDUINO DOCS

<a id='296a02d1-fd92-4347-9308-e556efbe8520'></a>

____________________________________________________________________________________________________

<a id='fcb86be0-9870-464a-a542-fe725fef459f'></a>

for Arduino_MKRGPS and install it.

3. Here are some of the core functions of this sketch:

`GPS.begin` - initializes the GPS library.

`GPS.available()` - checks for available GPS data from the module.

`GPS.latitude()` - records latitude.

`GPS.longitude()` - records longitude.

`GPS.altitude()` - records altitude.

`GPS.speed()` - records speed in km/h.

<a id='89539a78-e74c-43f8-9c02-ba0708ddda8a'></a>

The sketch can be found in the
snippet below. Upload the sketch
to the board.

<a id='d4fdad71-c86b-4ce4-8cb9-8a81e4b04b3b'></a>

```cpp
1 #include <Arduino_MKR
2 
3 void setup() {
4   // initialize seria
5   Serial.begin(9600);
6   while (!Serial) {
7     ; // wait for ser
8   }
9 
10   // If you are using
11   // the GPS_MODE_SHI
12   if (!GPS.begin()) {
13     Serial.println("F
14     while (1);
15   }
16 }
17 
18 void loop() {
19   // check if there i
20   if (GPS.available()
21   // read GPS value
22   float latitude
23   float longitude
24   float altitude
25   float speed
26   int satellites
27 
28   // print GPS valu
```

<a id='b74026de-de5d-4a83-97c6-a49634cb520e'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='33d50d10-6738-484c-8a58-7a78e1b14cf3'></a>

4/7

<a id='0abb6ab0-0331-401e-bbf6-9105417905bf'></a>

Manage libraries.., and search

<!-- PAGE BREAK -->

<a id='68082bc5-7ca5-4d63-ba79-4aab022d6a9e'></a>

12/4/25, 2:52 PM

<a id='2f184aa0-689c-451a-87dd-bbdd60bd33d8'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='affd4996-bb7f-47b8-9c44-e3ef2eaedb85'></a>

ARDUINO DOCS

<a id='11cc468d-7e48-4baf-928b-ec5146fc51ff'></a>

# Testing It Out

After we have uploaded the code to the board, we need to open the Serial Monitor to start the program. It is a good idea to have our setup close to a window. Once the data is available, it will start printing the values in the Serial Monitor.

<a id='94efe2d9-da27-407a-8d23-a04725e0ec6d'></a>

<::screenshot of Arduino IDE and Serial Monitor showing GPS data: screenshot::>
GPS data printed in the Serial Monitor.

**Arduino IDE 1.8.19 - Serial Monitor**
01:19:04 $GPRMC,011904.00,A,3540.84000,N,08233.16000,W,0.200,314.01,230421,,,A*7A
01:19:04 Lat: 35.680666
01:19:04 Lon: -82.552666
01:19:04 Speed: 0.20 km/h
01:19:04 Heading: 314.01
01:19:05 $GPRMC,011905.00,A,3540.84000,N,08233.16000,W,0.199,314.01,230421,,,A*7B
01:19:05 Lat: 35.680666
01:19:05 Lon: -82.552666
01:19:05 Speed: 0.20 km/h
01:19:05 Heading: 314.01
::>


<a id='805c0aa0-bdb5-4443-9b7a-5846f04c9569'></a>

Note: This process may take
some time. If no data is
available after 5 minutes or so,
try moving your device closer to
a window.

<a id='3953748c-6aed-4738-987e-b7c55c2a4162'></a>

Once we start getting the values,
we can double check that they are
alright. For example,

<a id='44995ebf-4c10-4965-a1a1-2566e7ed13a6'></a>

longitude
and
latitude
should be very accurate, and be
able to pinpoint almost your exact
location. You can enter the
coordinates in
Google Maps
for example, to see if the values
match.

<a id='e4e4ca5c-1d72-4615-8ff2-86071deed983'></a>

## Troubleshoot

If the code is not working, there
are some common issues we can
troubleshoot:

<a id='61e341a4-4ece-4f3b-8b2b-579be88ad826'></a>

We have not installed the
**MKRGPS** library.
We have selected the wrong
port and board to upload to.

<a id='d1d094ab-53ff-4107-a529-0950a9114493'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='1f1f96aa-5267-4005-9cdf-4eac2d7fb5ef'></a>

5/7

<!-- PAGE BREAK -->

<a id='77a9a3e2-4053-42db-8ba9-06d02a17bf69'></a>

12/4/25, 2:52 PM

<a id='a80ac7ee-97c0-4224-989b-2b025da607d2'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='c71a4200-4f3f-4a34-8b2d-b39668d84608'></a>

ARDUINO DOCS

<a id='4d2b2503-2e3a-44e3-8f88-5c51b4e71138'></a>



<a id='ad12e73e-3ec2-462a-a348-5c38322e35f7'></a>

We need to move the MKR GPS Shield closer to a window.

<a id='bf5ee6b6-b41c-4221-9ba4-0a234a75f44d'></a>

# Conclusion

In this tutorial, we learned how to retrieve accurate location data from the **MKR GPS Shield**. We managed to retrieve a lot of useful data and print it in the Serial Monitor. With it, we can ideate some pretty cool ideas, such as speedometer, tracking device or maybe a geolocation game. GPS is a great technology that can retrieve data from anywhere in the world as long it has clear sight, which makes it very useful for remote projects.

<a id='08d823a3-fb66-48bd-8b40-8a3739d0c10d'></a>

Feel free to explore the
Arduino_MKRGPS library further,
and try out some of the many cool
functions.

<a id='27c285a5-d8da-4c98-be63-d36f75031d04'></a>

**Suggest changes**
The content on docs.arduino.cc is facilitated through a public GitHub repository. If you see anything wrong, you can edit this page here.

**Need support?**
Help Center
Ask the Arduino Forum
Discover Arduino Discord

**License**
The Arduino documentation is licensed under the Creative Commons Attribution-Share Alike 4.0 license.

<a id='b3a87903-b51a-4078-a8c1-f57756761bf4'></a>

Was this article helpful?

<a id='984dd8a5-3fa6-4cf5-9961-17f24e715872'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='b213085f-d4b1-44fe-b13d-5118f731cf3d'></a>

6/7

<!-- PAGE BREAK -->

<a id='01507c07-8a44-4e5d-9a0a-f5e6fa43eb83'></a>

12/4/25, 2:52 PM

<a id='a1114b0f-4f71-4c60-834a-9b5a9aecd693'></a>

MKR GPS Shield Basics | Arduino Documentation

<a id='f64f8cdb-fabc-407a-91af-a28a09e266da'></a>

ARDUINODOCS [input field]

<a id='323075e2-3d55-4e4b-96cd-4a8d8ccd7d0f'></a>

<::thumbs-up and thumbs-down icons separated by a horizontal line
: figure::>

<a id='bd36e8bf-d252-4694-b7d3-9fb0ecfaf39b'></a>

&#169; 2025 Arduino
Terms Of Service Privacy Policy Security Cookie Settings

<a id='eca64add-0365-4271-85d6-94346be9f0c2'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-userManual.html

<a id='688fb2c6-3739-451a-a79b-a4c0fa246964'></a>

7/7