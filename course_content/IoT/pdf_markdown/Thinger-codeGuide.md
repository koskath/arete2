<a id='0933d691-5ec4-4fae-9bb1-ef8bfccf04a8'></a>

≡ thinger.io ⬜

<a id='04f002d8-639b-4d56-a182-e81f33a87486'></a>



<a id='fab626c6-4dc3-4bc0-bcb1-95729ac768be'></a>

<li class="right-items">
<li class="right-items">
<li class="right-items">
</ul>
</nav>
<section id="intro-section">
<article id="intro-section--text">
![waving hand](images/icons/waving-hand.png)
<h1 class="section--header">
Hey, ik ben Arnold!
</h1>
<p class="section--text">
Ik ben een front-end developer en student
</p>
<a href="#work--section" class="pink-button scroll">
</article>
![Arnold Francisca](images/hero-pf.jpg)
</section>

<a id='a09c33a3-aeda-471c-a45f-4c4d841d0bcc'></a>

CODING GUIDE

<a id='bf051427-14be-440a-a5b6-f448ac519c70'></a>

<::transcription of the content
: Button with GitHub Octocat icon, "Edit" text, and a dropdown arrow::>

<a id='3d559f0d-e9eb-442c-8994-0c73b7c15901'></a>

# Sketch Overview

Almost all Arduino Sketches share a common structure, consisting of a `setup` method and a `loop` method. This structure remains unchanged when integrating with Thinger.io. However, it is important to understand where device resources should be defined and where interaction with external services is possible. In general terms, any device resource (such as an LED, relay, sensor, or servo) must be defined inside the `setup()` method. Similar to initializing devices, setting the input/output direction of a digital pin, or initializing the Serial port speed, resources also need to be initialized here. This essentially involves configuring which values or resources are to be exposed over the Internet.

<a id='41486192-36f6-46a6-a757-882d65e222eb'></a>

The `loop()` is the designated place to consistently call the `thing.handle()` method, allowing the Thinger libraries to manage the platform connection. This method also serves as the location for calling endpoints or streaming real-time data to a dashboard. It is important to avoid adding any delays within the `loop()` unless specific actions, such as working with deep sleep modes on a device, are being implemented. Any other delay will negatively impact Thinger's proper functioning on the device. Additionally, reading a sensor value in every loop iteration can be detrimental if the sensor requires significant time to complete a read, as this will lead to a device with noticeable lag when responding to commands.

<a id='88dc711d-8e6f-42fd-82d0-f201f00db973'></a>

1

<!-- PAGE BREAK -->

<a id='114b8dde-7bdc-4d8e-8884-b89241b69dac'></a>

// add required headers according to the device
#include <ThingerESP32.h>

// initialize Thinger instance (type can change depending on the
device)
ThingerESP32 thing("username", "deviceId", "deviceCredential");

void setup() {
  // initialize sensors and pins

  // initialize wifi (see examples for the device)

  // add resources here, like sensors, lights, etc.
}

void loop() {
  // call always the thing handled in the loop and avoid any delay
  // here
  thing.handle();
  // here it is possible to call endpoints
  // and also it is possible to stream resources
}

<a id='56359d11-30a4-40e7-bc6f-5b2141c9fee0'></a>

# Setting Credentials

All devices connected to the platform require authentication against the server. When a device is created in the `console`, a new device identifier is generated and device credentials are set. Therefore, these credentials must also be configured in the Arduino code to allow the device to be recognized and associated with the account. This is typically done during the initialization of the Thinger instance in the code, specifically when the `thing` instance is defined. The `username`, `deviceId`, and `deviceCredential` should be replaced with the values registered in the cloud. It is worth noting that credentials used to be defined inside `arduino_secrets.h`.

<a id='151f8a9f-de20-46d9-a4a0-5ac404cbb6fe'></a>

ThingerESP32 thing("username", "deviceId", "deviceCredential");

<a id='e74597dd-ff7a-4755-af10-7a6777c868c0'></a>

Adding Resources

<a id='d28ca4bd-2eb2-4019-bef2-e7b406edc9a1'></a>

2

<!-- PAGE BREAK -->

<a id='8a2f2d6c-d6a7-4e46-a02e-240a55945d94'></a>

In the Thinger.io platform, each device can define several resources. A resource can be considered anything that can be sensed or activated. For example, typical resources include a sensor value like temperature or humidity, or a relay that controls a light. Therefore, the resources that need to be exposed over the Internet should be defined.

<a id='6eff77b7-9534-4c49-b0eb-7404819efde2'></a>

All resources must be defined inside the `setup()` method of the Arduino sketch. This way, the resources are configured at the beginning, but can be accessed later as necessary.

<a id='36718241-5e93-496b-9e6f-50f4d533b0fe'></a>

There are three different types of resources, which are explained in the following sections.

<a id='0b5fcc69-26f6-48d6-adff-3ed071eebef8'></a>

# Input Resources

If control or actuation of an IoT device is required, an input resource must be defined. An input resource serves as a source of information for the device. Examples include resources for controlling a light or relay, adjusting a servo position, or modifying a device parameter.

<a id='30d7114d-1dc9-49bf-8dcc-f73a1f22876b'></a>

To control or actuate an IoT device, it is necessary to define an input resource. An input resource is anything that can provide information to a device. Examples include a resource for turning a light or a relay on and off, changing a servo position, or adjusting a device parameter.

<a id='09b3597b-74b4-494e-aed7-e3ccbad54d96'></a>

To define an input resource it the operator is used << , pointing to the resource name,
and it uses a C++11 Lambda function to define the function.

<a id='55fbd457-f882-40fa-b5d3-8fecc9187ff0'></a>

The input resource function takes one parameter of type `pson` that is a variable type that can contain booleans, numbers, floats, strings, or even structured information like in a JSON document.

<a id='39a96035-4537-43b6-b7e2-bdc2b13a3644'></a>

The following subsections will show how to define different input resources for typical use cases.

<a id='ca4ede91-3d8d-4be5-871e-74db2c98be49'></a>

*Turn on/off a LED, a relay, etc*

<a id='02bd4718-ab1b-46bb-a65f-8ce68e009193'></a>

3

<!-- PAGE BREAK -->

<a id='44db2917-efa8-4034-940b-132e135c0d36'></a>

This kind of resource only requires an on/off state, so it can be enabled or disabled as required. As the `pson` type can hold multiple data types, we can think that the `pson` parameter of the input function is like a boolean.

<a id='37d3e4f4-78e6-4964-adf3-2a1878582b44'></a>

So, inside the setup function, place a resource called led (but use any other name),
of input type (using the operator <<), that takes a reference to a pson parameter.
This example will turn on/off the digital pin 10 using a ternary operator over the in
parameter.

<a id='96550b32-f8a5-4250-ab2c-91d10e5dc663'></a>

thing["led"] << [](pson& in){
    digitalWrite(10, in ? HIGH : LOW);
};

<a id='db35727b-2643-4bfc-a348-e92e5a4b54b3'></a>

### Modify a servo position

Modifying a servo position is quite similar to turning on/off a LED. In this case, however, it is necessary to use an integer value. As the `pson` type can hold multiple data types, we can still use the `pson` type as an integer value.

<a id='1d69c364-ec07-437d-afbd-dfb3cca0e939'></a>

thing["servo"] << [](pson& in){
    myServo.write(in);
};

<a id='ad9d1b36-507f-4e55-b117-14a729ba3bc2'></a>

_**Update sketch variables**_

Input resources can also be used to update sketch variables, allowing for dynamic changes in device behavior. This is quite useful in situations where it is desirable to temporarily disable an alarm, change reporting intervals, update a hysteresis value, and so on. In this way, additional resources can be defined to change variables.

<a id='b0a50418-cac0-4d9b-9dbc-79aaca72f55b'></a>

```
float hysteresis = 0; // defined as a global variable
thing["hysteresis"] << [] (pson& in){
    hysteresis = in;
};
```

<a id='803b09c3-d2a3-451a-be65-25a9b7b8c15b'></a>

Pass multiple data

<a id='1c51dcfe-737d-4a44-8084-6b68c9ed1a7a'></a>

4

<!-- PAGE BREAK -->

<a id='e30b1961-fb04-4a16-b3e6-fe774d5296d0'></a>

The `pson` data type can hold not only different data types, but also is fully compatible with JSON documents. The PSON data type can be utilized to receive multiple values simultaneously. This example will receive two different floats that are stored with the `lat` and `lon` keys.

<a id='3b794f73-a64f-4e51-9cfb-b44611283c57'></a>

thing["location"] << [](pson& in){
    float lat = in["lat"];
    float lon = in["lon"];
};

<a id='8f039236-e9c1-4b89-8c6e-750df13f2eca'></a>

## Show Input Resources State in Dashboards and API

The Dashboards or API work in a way that when opening them, they query the associated resources to correctly print their current state, i.e., the switch is on or off. In this way, when the API or a Dashboard is open, each associated input resource is called, receiving empty data in the call, as there is no intention to control the resource (the pson input will be empty).

<a id='bd3ab188-7eac-4a9c-9a4b-3675817ab994'></a>

So, how do the Dashboards or the API know what is the current state of an input resource? The resource must set its current state in the input parameter, if it is empty, or use the input value if there is one. This way, we can obtain three different things: query the current resource state (without modifying it), modify the current resource state, and obtain the expected input on the resource (this is how the API explorer on the device works).

<a id='f7f81111-8b26-4d0e-925f-ea529f0f4177'></a>

Therefore, a correct input resource definition that actually allows to display of the current state of the resource in a Dashboard or in the API, will be like this example code.

<a id='e22a1cd1-c33b-4d94-bfbb-33d858dbe56f'></a>

```
thing["resource"] << [](pson& in){
    if(in.is_empty()){
        in = currentState;
    }
    else{
        currentState = in;
    }
};
```

<a id='2fcc286d-cd67-4761-813a-f0544efe3541'></a>

5

<!-- PAGE BREAK -->

<a id='bff21c99-6ac3-4076-b8da-c77a0c2d1e34'></a>

This sample code basically returns the current state (like a boolean, a number, etc) if there is no input control, or uses the incoming data to update the current state. This can be easily adapted for controlling a LED, while showing its current state in the dashboard once opened or updated.

<a id='2faee321-f1ba-4398-a560-64c9baabc3a1'></a>

thing["led"] << [] (pson& in){
    if(in.is_empty()){
        in = (bool) digitalRead(pin);
    }
    else{
        digitalWrite(pin, in ? HIGH : LOW);
    }
};

<a id='980cea33-65fe-47a9-b231-06468d0d7087'></a>

Note: For controlling a digital pin, just use the method explained in the Easier Resources
Section.

<a id='b969f1fd-d53b-4c7e-8149-61e21fa6148e'></a>

## Output Resources

Output resources should be used in general when needed to sense or read a sensor value, like temperature, humidity, etc. So the output resources are quite useful for extracting information from the device.

<a id='a802f9de-0c87-46ed-848c-94c1c99bea47'></a>

To define an output resource it is used the operator >> to point to the resource name,
and it uses a C++11 Lambda function to define the output function.

<a id='2734d709-10ff-4e88-ba5f-17ba11cd3569'></a>

The output resource function takes one parameter of `pson` type that is a variable type that can contain booleans, numbers, floats, strings, or even structured information like in a JSON document.

<a id='7bdbe836-f67d-4c62-a3df-e2684bfb710b'></a>

The following subsections will show how to define different output resources for typical use cases.

<a id='0908fd9a-2d58-45dc-809f-d05af94f7abf'></a>

Read a sensor value

<a id='9c3cb80a-a0ce-4669-82b2-29d4affbe9e5'></a>

6

<!-- PAGE BREAK -->

<a id='e4396056-5e8f-49e5-aed9-537ab6d1b74e'></a>

Defining an output resource is quite similar to defining an input resource, but in this case it is used the operator `>>`. In the callback function, we can fill the output value with any value we want, like in this case, the output from a sensor reading.

<a id='939f7db0-790d-4b2a-9c49-a0ad667a2648'></a>

thing["temperature"] >> [](pson& out){
    out = dht.readTemperature();
};

<a id='727b0a73-730a-43f7-a468-d22c8a64b62a'></a>

*Read multiple datasets*

In the same way, the input resources can receive multiple values at the same time, the
output resources can also provide multiple data. This is an example of providing both
latitude and longitude from a GPS.

<a id='a4854b79-a2da-483f-9916-3294a2986e55'></a>

```
thing["location"] >> [] (pson& out) {
    out["lat"] = gps.getLatitude();
    out["lon"] = gps.getLongitude();
};
```

<a id='2872323d-2f1c-4eb6-8897-1d749938129d'></a>

**Read sketch variables**

If the sketch cannot provide a single sensor reading, as it is doing some kind of data integration, an output resource can also be used for reading the sketch variables, where the computed result is updated frequently.

<a id='22354760-e547-4f5a-a2b0-77d09e8df6e4'></a>

float yaw = 0; // defined as a global variable
thing["yaw"] >> [] (pson& out){
out = yaw;
};

<a id='ce180313-8d11-4635-8017-98a541a1b066'></a>

## Input/Output Resources

The last resource type is a resource that not only takes an input or an output, but takes both parameters. This is particularly useful when an output is dependent on an input, such as when a changing reference value needs to be provided to a sensor.

<a id='a305c49b-7c77-41c2-a4be-d41e758f779c'></a>

7

<!-- PAGE BREAK -->

<a id='53176497-72ea-4082-bb26-d392dc0ab560'></a>

These kinds of resources are defined with the operator `=`. In this case, the function takes two different `pson` parameters. One for input data and another for output data. This example provides an altitude reading using the BMP180 Sensor. It takes the reference altitude as input and provides the current altitude as output.

<a id='9a2fadb6-0336-4da4-9d05-6f17020070ac'></a>

thing["altitude"] = [](pson& in, pson& out){
    out = bmp.readAltitude(in);
};

<a id='d6b0f9a3-768d-4efd-85d8-4a94b6269c58'></a>

Also, define more complex input/output resources that take several input values, to provide multiple output values, like in this example that takes `value1` and `value2` to provide the `sum` and `mult` values.

<a id='11cdfec3-d8be-4fa9-89b1-00ebad0b1e02'></a>

thing["in_out"] = [] (pson& in, pson& out){
out["sum"] = (long)in["value1"] + (long)in["value2"];
out["mult"] = (long)in["value1"] * (long)in["value2"];
};

<a id='f3a8d369-cba9-48c1-89aa-ec277ddecd8e'></a>

# Resources without parameters
It is also possible to define resources that do not require any input or generate any output. These are like callbacks that can be executed as needed, for example, to reboot the device or perform a required action.

<a id='846cdeed-f2c2-4110-babc-08e427d90669'></a>

In this case, the resource is defined as a function without any input or output parameters.

<a id='5a364ccb-f0c5-4555-9cf8-df7d0428e88a'></a>

```
thing["resource"] = [](){
// write here the execution code
};
```

<a id='abaac68e-e9eb-491b-a3bc-e8e850d93a82'></a>

Easier Resources

<a id='d1566e83-e3c1-40c5-a700-4a41a5d3d884'></a>

8

<!-- PAGE BREAK -->

<a id='82cd3be8-65d5-478c-88a6-ae5ef600c5dc'></a>

The client library also includes some useful syntactic sugar definitions for declaring resources more easily without having to think about input or output resources. These syntactic sugar features are macros that are expanded automatically to define the resources in the standard way.

<a id='32c72c0b-4d63-4af1-a626-c05c03b3398f'></a>

The advantage of using this kind of definition is that resources will be able to handle the state when queried from the API. For example, if a digital pin is enabled or disabled, its current state will be visible in both the API explorer and a dashboard.

<a id='2ddc9314-f57f-4957-9d5a-414194232dfd'></a>

# Control a digital pin

This kind of resource will allow defining a resource for declaring control over a digital pin, so it is possible to alternate over on/off states, which can be used for controlling a LED, a relay, a light, etc.

<a id='6762a2bd-b7fb-419c-b172-490aa9c54d9f'></a>

It is required to define the digital pin as OUTPUT in the setup code, or the resource will not work properly.

```
thing["relay"] << digitalPin(PIN_NUMBER);
thing["relay"] << invertedDigitalPin(PIN_NUMBER);
```

<a id='8605d4d7-0c34-43a0-98a1-cd7c73242be9'></a>

## Define Output Resources

This kind of resource will allow defining a resource for declaring a read-only resource, like a value obtained from a sensor, or a given variable in our sketch.

<a id='141bae95-7f16-4ae5-b310-b80331b94f4b'></a>

In this example, we are defining a resource that exposes a sensor reading, like the DHT11 sensor temperature.

<a id='0d03a60e-39a1-45e7-8ac6-8338e115a325'></a>

thing["temperature"] >> outputValue(dht.readTemperature());

<a id='d605c159-8bb6-4ba5-8ba3-d0512c82946e'></a>

But it is also possible to define an output resource for any global variable in our sketch.

```
thing["variable"] >> outputValue(myVar);
```

<a id='90da2aca-c8d4-45fa-af0d-5365fb43a2f3'></a>

9

<!-- PAGE BREAK -->

<a id='484fd79f-7552-4798-b3ed-200296c2312d'></a>

# Modify Sketch Variables

Our sketch usually defines some parameters or variables that are used inside the loop code. These kinds of resources are normally used to handle or control the execution behaviour. With these kinds of resources, we can modify any parameter we want to expose, like a float, an integer, a boolean, etc.

<a id='a8416200-6e54-42fe-94b1-7f8b6d7992b1'></a>

In this example, it is possible to remotely modify the boolean `sdLogging` variable defined as a global variable.

<a id='213006a1-ceab-4e2f-b30b-55b0d96ddc41'></a>

thing["logging"] << inputValue(sdLogging);

<a id='6e066dff-6c14-4485-a92d-a9ce316b79a4'></a>

It is also possible to define a callback function to know when the variable has changed, so we can perform any other action. For this use case, define the resource to have some code executed when the `hysteresisVar` changes.

<a id='a46dd314-2ed4-4b23-b280-b8a7c5512889'></a>

```
thing["hysteresis"] << inputValue(hysteresisVar, {
// execute some code when the value changes
Serial.println("Hystereis changed to: ");
Serial.print(hysteresisVar);
});
```

<a id='87a5c01a-74fb-4073-9542-fddb3239221e'></a>

# Servo control

It is also possible to define a resource for controlling a servo instance. This way, the defined resource will automatically handle the servo instance, reading its current position, or changing to a new one according to the API interactions.

<a id='8a26ca93-85f3-4794-8325-c733ffc22b38'></a>

To define a servo resource, just define and initialize the servo as usual, and then use the declared instance in the resource definition.

<a id='8e6aa5ba-e547-4fa3-9d12-a892c9f9ab61'></a>

thing["servo"] << servo(myServoInstance);

<a id='1e023a41-12fe-4946-925e-af2aef3bc5b0'></a>

10

<!-- PAGE BREAK -->

<a id='9eb5d84c-ea7c-444c-828c-9d343322c43f'></a>

# Communication between devices

In Thinger.io, it is possible that devices can communicate between them. There are two possibilities here. One is the communication between devices from the same account, and the other is the communication between devices from different accounts. Here we describe the two different approaches:

<a id='944c4c65-4cf5-447d-9080-5c946ee0d8d6'></a>

# Same account communication

For this use case, in which both devices belong to the same user account, there is a specific method that allows devices to communicate with other devices with low latency and simple codification. This communication can contain data or not (it is possible to make an empty call). Let's suppose that we have two devices: deviceA and deviceB, and we want to communicate both calls from deviceB to a specific deviceA input resource. We can use "thing.call_device(,);":

<a id='047399cc-25da-44aa-97fc-6ab1ae1035e3'></a>

The `deviceA` defines a resource:

```
setup(){
    thing["resource_On_A"] = [](){
        Serial.println("Someone is calling me!");
    };
}
```

`deviceB` can easily call this resource and send data to it:

```
loop(){
    thing.handle();
    // be sure to call it at an appropriate rate
    thing.call_device("deviceA", "resource_On_A");
}
```

<a id='ad1317ae-7918-48a9-93ad-16eade23231d'></a>

On the other hand, if we want to send the message with a `pson` payload in order to share data between devices. In this case, the `deviceA` will need to define a resource with some expected input

<a id='367bf585-f1c0-44c2-a006-0670025d765a'></a>

11

<!-- PAGE BREAK -->

<a id='c59b149c-03b5-41d9-a26c-9fb2cd5d9842'></a>

```
setup(){
    thing["resourceOnA"] << [](pson& in){
        int val1 = in["anyValue1"];
        float val2 = in["anyValue2"];
        // Work with the updated parameters here
    };
}
```

<a id='81773c17-2cba-456b-a95d-4a0b7bb2e700'></a>

Then `deviceB` can call this method, providing the appropriate input by defining a `pson` type that is filled with the same keys used on `resource0nA` :

<a id='82cd7ba5-3e07-4ab8-923a-38481ce4887b'></a>

```
loop(){
  thing.handle();
  // be sure to call it at an appropriate rate
  pson data;
  data["anyValue1"] = 3;
  data["anyValue2"] = 43.1;
  thing.call_device("deviceA", "resourceOnA", data);
}
```

<a id='5a3bb941-0b98-4043-a34a-3c67c32d1a0e'></a>

`deviceB` can also call this method by providing the information from a defined resource that generates the information. In this case, the call is similar to the previous example, but using the resource as the data source.

<a id='dc0f5382-d522-435d-9084-3760129dd633'></a>

setup(){
    thing["resourceName"] >> [] (pson& out){
        out["anyValue1"] = 3;
        out["anyValue2"] = 43.1;
    };
}

loop(){
    thing.handle();
    // be sure to call it at an appropriate rate
    thing.call_device("deviceA", "resource0nA",
    thing["resourceName"]);
}

<a id='1a48507a-15c6-40bb-bc49-0a1ff4204401'></a>

Communication between different accounts

<a id='874ee620-1415-4c34-81d0-8886c7ebb16b'></a>

12

<!-- PAGE BREAK -->

<a id='fd35ef73-d248-411a-a965-0be782d386c4'></a>

If we want to communicate devices from different accounts, we can do that by calling an endpoint of type `Thinger.io Device Call`. Just register an endpoint of this type in the console:

<a id='c2287865-5a4a-4d3c-bb94-a0192b756c05'></a>

## Endpoint Details

Endpoint Identifier: DeviceACall
Endpoint Name: Endpoint
Endpoint Description: Endpoint for calling Device A from
option Enabled: [ ]
Endpoint Type: Thinger.io Device Call
Device Owner Username: otherUser
Device Identifier: deviceA
Resource Name: resourceOnA
Device Access Token: paste here a deviceA token device that gives you access to the device

[x] Add Endpoint

<a id='5a4a6d9d-63ba-4b19-992e-df206262ae62'></a>

In this case, it is required to define different parameters in the endpoint:

*   Endpoint Identifier: The endpoint ID that the device will use for calling the device.
*   Endpoint Name: The name of the endpoint, which does not need to equal the "Endpoint Identifier". The endpoint will show in the list of endpoints with this name.
*   Endpoint Description: This is an optional field. It is useful to remember what the endpoint consists of.
*   Device Owner: The device owner's username.
*   Device Identifier: The device ID of the other account.
*   Resource Name: The resource on the device to be called.
*   Device Access Token: A device token generated in the other account for granting external access to the device.

<a id='620b2347-3b02-4a7b-8f60-6912e3493217'></a>

Once defined, the device will be able to call the endpoint, as explained in the following section. It basically consists of calling the `call_endpoint` method.

<a id='1d3d7640-fd60-4cdf-b361-f8160b9d61ea'></a>

```
thing.call_endpoint("DeviceACall");
```

<a id='e0825346-76c4-482f-97a2-ab34518c5a9e'></a>

13

<!-- PAGE BREAK -->

<a id='ceeb7202-f5ed-4370-b55f-28e379ec5821'></a>

# Using Endpoints

In Thinger.io, an endpoint is defined as some kind of external resource that can be accessed by the device. With the endpoints feature, devices can easily send emails, SMS, push data to external Web Services, interact with IFTTT, and perform any general action that can be made by using WebHooks (Calling HTTP/HTTPS URLs).

<a id='653b1701-e2f9-4e4b-ae55-76c87f6441de'></a>

Calling an endpoint is so easy from the Arduino sketch, as it only requires calling the `call_endpoint` method over the `thing` variable.

```
thing.call_endpoint("endpoint_id");
```

<a id='bed3994c-5a36-423a-a228-5613615219a8'></a>

Endpoints can be called from the device code in order to execute any action, like sending a predefined email. The call can also include some reading values, which is especially useful to send the device's data to third-party services.

<a id='5ae5a266-6b81-4dee-a503-f1a1a43f19bd'></a>

① Extra attention must be taken while calling resources, in order to avoid uncontrolled recurrency. If the interval is too short, the server will lock the device connection

<a id='6bca64e6-c3cd-40f2-82d4-4bf6c97e99ef'></a>

## Calling Endpoints

In this case, we will see a simple example to send an email alert based on a temperature value. For this example, we have configured an email endpoint `high_temp_email` that contains some warning text about the temperature. For this case, we do not want to check the temperature every millisecond, so we are introducing some variables to control the sensing and warning frequency. In this example, the temperature is checked every hour, and if it is above 30°C, it will call the endpoint called `high_temp_email` which will send us an email with the predefined text. It is important here **not to add delays** inside the loop method, as it will prevent the required execution of the `thing.handle()` method, so we are using a non-blocking delay based on the `millis()` function.

<a id='ab70e7c7-2b17-476a-8c75-92e5ef35edd6'></a>

14

<!-- PAGE BREAK -->

<a id='1c7b9643-a924-405e-b565-668d016a81d1'></a>

```
unsigned long lastCheck = 0;

loop(){
    thing.handle(); // required thing handle

    unsigned long currentTs = millis();

    if(currentTs-lastCheck>=60*60*1000){
        lastCheck = currentTs;
        if(dht.readTemperature()>30){
            thing.call_endpoint("high_temp_email");
        }
    }
}
```

<a id='1faab68e-c51c-4f36-8272-960235c132bc'></a>

Endpoints offer significant creative flexibility, allowing for automation based on various events. For example, endpoints can be triggered by a presence sensor detection, a humidity sensor reporting no water in plants, or a device's unexpected location. Furthermore, endpoints can be integrated with services like IFTTT (If This Then That) to interact with multiple third-party platforms.

<a id='641c94fb-48f7-4fad-8141-44cafb30f1a8'></a>

# Sending Data to Endpoints

Sending data to an endpoint (in JSON format) is also quite easy. We also need to call the `call_endpoint` method, but in this case, adding some information based on the `pson` data format, which will be automatically converted to JSON. For example, if we want to report data to a third-party service like Keen.io, we can create such kind of endpoint in the console. Once configured, we can call the endpoint with our readings, for example, with humidity and temperature values from a DHT sensor.

<a id='3121e59c-ea77-4223-86a2-4d7f21b3b2de'></a>

```
// be careful of sending data at an appropriate rate!
pson data;
data["temperature"] = dht.readTemperature();
data["humidity"] = dht.readHumidity();
thing.call_endpoint("keen_endpoint", data);
```

<a id='cc576206-9e19-4c85-b82a-9ddad3c289ee'></a>

Data can also be sent based on a defined resource; for instance, if a resource already provides temperature and humidity. It is possible to reuse this definition for sending the same data to the endpoint, without having to redefine the sensor reading:

<a id='cb2d893a-2307-444a-8e94-ba8dfa5424cd'></a>

15

<!-- PAGE BREAK -->

<a id='073015ea-d781-4e3b-bef0-fd69ae68d846'></a>

```
setup(){
  // defined resource in the setup for reading a sensor value
  thing["data"] >> (pson& out){
    out["temperature"] = dht.readTemperature();
    out["humidity"] = dht.readHumidity();
  }
}

loop(){
  // be careful of sending data at an appropriate rate!
  thing.call_endpoint("endpoint", thing["data"]);
}
```

<a id='18cd3a14-89a7-408e-acbb-b113158124d7'></a>

## Email Type Endpoint Example

This is a simple example, applied to an email-type endpoint, with a custom body

```
setup()
{
  thing["temperature"] >> outputValue(analogRead(0));
}
loop()
{
  if(actualLevel>UpperLevel && endpointUpperFlag)
  {
    thing.call_endpoint("endpoint_id",thing["temperature"]);
    endpointUpperFlag=0;
  }
}
```

<a id='87ee500e-78f0-4649-9887-9825a2236f3e'></a>

Notice that there are a variable that limitates the run of this "if" just once, its important
to define any condition or method to warrantee that this kind of enpoint call is executed
just once (or at appropiate rate), because it can get a lot of emails generated by the
microcontroller across thinger.io platform.

<a id='95ebe38a-3340-4d17-a0b4-ef6d3cdd6281'></a>

At endpoint configuration, in the custom body email, we must add double brackets "{{<variable_key>}}" to invoke the variable sent by the microcontroller.

<a id='01e518c5-d4cb-4d1e-99c8-595352d344f0'></a>

"The room temperature is {{{temperature}}}%"

<a id='b538631d-2c9d-46ba-a564-fe60397bf5bf'></a>

16

<!-- PAGE BREAK -->

<a id='31ecdff2-9322-4f8d-b4b9-154794afed80'></a>

And receiving an email with the text:

<a id='5f014367-2901-4875-8fbb-9f9d73a083d3'></a>

The the room temperature is 80.34%

<a id='d854461c-8259-44d4-90cf-d5243734cdf2'></a>

# Using Data Buckets

Thinger.io provides an easy-to-use and extremely scalable virtual storage system that allows for storing long-term device data from device output resources. This information can be used to be plotted in dashboards, or can be exported in different formats for offline processing or a third-party Data Analysis process.

<a id='0287d181-1834-4404-a658-d312822c9e23'></a>

# From Device Resource

It is not necessary to implement specific codification in device firmware to start storing data in a data bucket. Data buckets will retrieve information from output resources; simply configure the Data Bucket to set the source and sampling interval as explained in the Console documentation. ↗

<a id='a1ba7b93-6e9c-4ccc-afa8-ae52e3b72b45'></a>

# Streaming Resource Data

To enable the device to stream information only when required, such as upon event detection, the "Update by Device" option can be used during bucket configuration. This utilizes streaming resource instructions. For instance, using a previously defined Output Resource named "location," this could be achieved with this code snippet:

<a id='d3bc2c3f-3cac-4a15-a4b3-ec7eb3d9c566'></a>

```c
void loop() {
    thing.handle();
    // use the logic here to determine when to stream/record the
    resource.
    if(requires_recording){
        thing.stream("location");
    }
}
```

<a id='ad8cb95a-f7f9-4290-becc-d6acfe53752e'></a>

17

<!-- PAGE BREAK -->

<a id='1b3171b1-d217-4028-8138-71505c72b892'></a>

# From Write Call

This option will allow setting the bucket in a state that it will not register any information by default, but it will just wait for writing calls, both from the Arduino library using the write_bucket method, as shown here, or calling the REST API directly, as done with Sigfox. This feature opens the option to register information in the same bucket from different devices, or store information from devices that are not connected permanently with the server, that are in sleep mode, or use a different technology like Sigfox.

<a id='5ef22aa1-a440-484d-a1ba-02bdfbbfa93b'></a>

Here is an example of an ESP8266 device writing information to a bucket using the write_bucket function:

<a id='c0ff637d-e8b6-4d4e-9c70-a284499d7f7b'></a>

void setup() {
  // define the resource with temperature and humidity
  thing["door_status"] >> [] (pson &out){
    out["OPEN"] = (bool)digitalRead(SENSOR_PIN);
  };
}

void loop() {
  // handle connection
  thing.handle();

  if(digitalRead(SENSOR_PIN)!=previous_status) {
    // write to bucket BucketId when the door changes its status
    thing.write_bucket("BucketId", "door_status");
  }
  previous_status=digitalRead(SENSOR_PIN);
}

<a id='2c32ff5e-9acf-4607-a45a-898f6d75a830'></a>

Note that this instruction will retrieve the ["door_status"] resource PSON, so it is also possible to call this function by attaching a custom PSON:

<a id='d1ea89b5-1b56-4cb5-a13e-67b80d872d3f'></a>

18

<!-- PAGE BREAK -->

<a id='2a720072-34cc-4aa7-adb9-3fdacba73b5b'></a>

```c
void loop(){
  // handle connection
  thing.handle();

  if(digitalRead(SENSOR_PIN)!=previous_status){
    // write to bucket BucketId when the door changes its status
    thing.write_bucket("BucketId", "door_status");
  }
  previous_status=digitalRead(SENSOR_PIN);
}
```

<a id='ca97aecf-c8e2-4bbf-9748-0428ee8c776e'></a>

# Streaming Resources

In Thinger.io, WebSocket connections can be opened against devices to receive real-time sensor values, events, or other information. WebSockets are primarily utilized in the Console's Dashboard feature for streaming resources at a fixed, configurable interval. This functionality is available by default when an output resource is defined. However, to transmit information precisely when required, such as upon detection of movement or presence, a specific code, similar to calling an endpoint, must be programmed.

<a id='29a9b1e3-24e4-4b11-bca2-469c468dbae3'></a>

In such cases, it is necessary to detect when to stream the event, for example, when an accelerometer value exceeds a threshold, a presence sensor makes a detection, or the compass heading changes. The determination of when to stream new data is left to the implementer. Streaming resources also require that another endpoint is connected, listening for them (i.e., from a WebSocket connection), so if there is no one listening for this data, the data is not sent. This is handled automatically by the client library and the server, therefore, it is safe to stream data always, as the device will transmit the information only when there is a destination.

<a id='44ab51a3-f693-4da6-96a3-15c3635ca6dd'></a>

This example will report the compass heading in real-time if the heading value changes by more than 1 degree.

<a id='7a5ef1f4-dba6-4708-a495-2709b5bc0da8'></a>

19

<!-- PAGE BREAK -->

<a id='6827d6df-9082-4835-a723-72b7a292d30a'></a>

thinger.io Overview Statistics Dashboards Devices Endpoints Account Profile Settings Resources Community Github Libraries Connect Twitter Email Resources ESP8266 Heading Heading <::A donut chart displaying a value of "268.51°" in the center, with approximately 75% of the circle filled.: chart::> <::A screenshot of a web browser's "Developer Tools" window, open to the "Network" tab. The table lists multiple network requests for "resource 'heading'" with columns including Name, Status, Type, Initiator, Size, and Time. Below the table, it shows "62 requests | 1.1 MB transferred | Finish: 7.35 s | DOMContentLoaded: 1.12 s | Load: 1.29 s".: screenshot::> <::An image of an ESP8266 development board with multiple wires connected to it, mounted vertically.: image::> © 2019 Copyright. Thinger.io

<a id='49cc9dba-d303-40c1-aa38-0ac9f07b7a40'></a>

```
void setup(){
  thing["heading"] >> [] (pson& out){
    out = getHeading();
  };
}

float previousHeading = 0;
void loop() {
  thing.handle();
  float currentHeading = getHeading();
  if(abs(currentHeading-previousHeading)>=1.0f){
    thing.stream(thing["heading"]);
    previousHeading=currentHeading;
  }
}
```

<a id='c665bf74-eb92-45ee-9d95-58299f60b704'></a>

# Enabling Debug Output

Thinger.io library provides extensive logging of its activities, which is especially useful when one needs to troubleshoot authentication and Wi-Fi connectivity issues. Include this definition in the sketch, but *make sure it comes first*, before any other includes (it was reported to cause crashes on some boards otherwise):

<a id='cf4017f6-066b-4a46-8502-67b49a9971f8'></a>

#define THINGER_SERIAL_DEBUG

// the rest of the sketch goes here

<a id='ac062a00-f361-4d4a-9f47-ef88e4bca074'></a>

20

<!-- PAGE BREAK -->

<a id='a7639e3a-f2d5-4106-a61f-66bbed0ba3a1'></a>

It is also necessary to enable `Serial` communication, as all the debugging information is displayed over the Serial. So, enable it in the sketch in the setup method.

<a id='b9a2b73b-719e-4801-84af-703753c64dd4'></a>

```
void setup() {
  Serial.begin(115200);
}
```

<a id='d47057d1-5c7a-4af3-b00f-2e7c11ff5855'></a>

# Listen for Connection State

Sometimes it can be useful for an application to know the current connection status with Thinger.io, i.e., to notify disconnected status with a LED, request device configuration after authentication, or any other internal control flow according to connection state.

<a id='357575d3-151b-46a5-a602-5f611d926fe2'></a>

In order to create a listener for such connection states, it can be done with the `set_state_listener` function in the `setup()` method. For example, it is possible to define a listener that will receive the different connection states for the network, server, or authentication:

<a id='df90e769-5919-42e7-aaf3-e57aad9a36ab'></a>

21

<!-- PAGE BREAK -->

<a id='40f7aecd-eb32-4ed2-b054-3875a23dccf5'></a>

```cpp
void setup() {
  // the setup code here..

  thing.set_state_listener([&](ThingerClient::THINGER_STATE
  state) {
    switch (state) {
      case ThingerClient::NETWORK_CONNECTING:
        break;
      case ThingerClient::NETWORK_CONNECTED:
        break;
      case ThingerClient::NETWORK_CONNECT_ERROR:
        break;
      case ThingerClient::SOCKET_CONNECTING:
        break;
      case ThingerClient::SOCKET_CONNECTED:
        break;
      case ThingerClient::SOCKET_CONNECTION_ERROR:
        break;
      case ThingerClient::SOCKET_DISCONNECTED:
        break;
      case ThingerClient::SOCKET_ERROR:
        break;
      case ThingerClient::SOCKET_TIMEOUT:
        break;
      case ThingerClient::THINGER_AUTHENTICATING:
        break;
      case ThingerClient::THINGER_AUTHENTICATED:
        break;
      case ThingerClient::THINGER_AUTH_FAILED:
        break;
      case ThingerClient::THINGER_STOP_REQUEST:
        break;
    }
  });
}
```

<a id='d0f29651-d108-4127-a9e9-7b206876edd6'></a>

In this table it is detailed the different values and their descriptions.

<a id='8f5bc14b-3b4a-4137-88b8-ec54adec2a78'></a>

22

<!-- PAGE BREAK -->

<a id='d515e3e3-7891-440f-bbc8-af104b3704ef'></a>

<table id="22-1">
<tr><td id="22-2">State</td><td id="22-3">Description</td></tr>
<tr><td id="22-4">NETWORK_CONNECTING</td><td id="22-5">The underlying network is being connected, i.e., initializing ethernet, wifi, gsm, etc.</td></tr>
<tr><td id="22-6">NETWORK_CONNECTED</td><td id="22-7">The network is connected and ready to be used.</td></tr>
<tr><td id="22-8">NETWORK_CONNECT_ERROR</td><td id="22-9">The network cannot be initialized, i.e., bad WiFi credentials, cannot reach GSM, etc.</td></tr>
<tr><td id="22-a">SOCKET_CONNECTING</td><td id="22-b">After the network is connected, it means that the client is connecting to Thinger.io servers.</td></tr>
<tr><td id="22-c">SOCKET_CONNECTED</td><td id="22-d">The socket has been connected to the server.</td></tr>
<tr><td id="22-e">SOCKET_CONNECTION_ERROR</td><td id="22-f">The socket cannot be connected to Thinger.io. If often means a bad Internet connection.</td></tr>
<tr><td id="22-g">SOCKET_DISCONNECTED</td><td id="22-h">The connection with Thinger.io has been closed.</td></tr>
<tr><td id="22-i">SOCKET_ERROR</td><td id="22-j">An error happened with the socket, i.e, bad read or write, which will cause a disconnect.</td></tr>
<tr><td id="22-k">SOCKET_TIMEOUT</td><td id="22-l">The socket timed out while reading or writing, so the connection will be closed.</td></tr>
<tr><td id="22-m">THINGER_AUTHENTICATING</td><td id="22-n">Thinger.io client is connected and it is being authenticated.</td></tr>
<tr><td id="22-o">THINGER_AUTHENTICATED</td><td id="22-p">Thinger.io client is connected and authenticated, so it can use Thinger.io, i.e., call an endpoint, read a property, etc.</td></tr>
<tr><td id="22-q">THINGER_AUTH_FAILED</td><td id="22-r">Thinger.io client authentication failed. Please, review the server, username, device id, and password.</td></tr>
<tr><td id="22-s">THINGER_STOP_REQUEST</td><td id="22-t">Thinger.io client was requested to stop, i.e., from the source code, or by the server.</td></tr>
</table>
Previous
OTHER DEVICES

<a id='372e4cc3-b2c2-4e2e-a381-c4b944975f7d'></a>

23

<!-- PAGE BREAK -->

<a id='92fd39aa-0a80-482d-8c24-2b71f40d09df'></a>

Next
TROUBLESHOOTING

<a id='99d4ad77-ebbe-4f25-95a6-df1008fa1a1b'></a>

Last updated 4 months ago

<a id='a3ca2225-f794-4efd-acd1-b2d6d73fc227'></a>

Was this helpful?
option Happy face: [ ]
option Neutral face: [ ]
option Sad face: [ ]

<a id='fa4e9b6c-d9ea-4e15-9984-cddf5f5817c3'></a>

24