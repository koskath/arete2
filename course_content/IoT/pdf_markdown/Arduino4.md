<a id='3db16be6-573b-40ef-9eeb-d3131d095f0c'></a>

12/4/25, 2:51 PM

<a id='719b4997-9ad1-4a38-b8e9-4b30f47adcb5'></a>

Arduino_MKRENV | Arduino Documentation

<a id='581d201e-c56e-4a4b-9c90-b0f43e1809ea'></a>

ARDUINODOCS

Search on Docs /

<a id='28686ef3-b200-467b-b49c-e2781544bc58'></a>

← Go Back

Library

<a id='8da0d689-93e2-4e0b-aba6-9441d3374644'></a>

Recents viewed

<a id='1a86baa5-1520-46a2-9945-deea2bb36b5d'></a>

Arduino_MKRENV
Arduino_MKRGPS
Arduino_APDS9960
Arduino_MKRIoTCarrier

<a id='f3a24a65-3774-4446-be83-7633bd613610'></a>

Home / Programming / Library / Arduino_MKRENV ON THIS PAGE

<a id='0da40dc9-8a96-4f29-b892-f560a715f005'></a>

SENSORS

# Arduino_MKRENV

option ARDUINO: [x]
LGPL-2.1 V1.2.1 Arduino 11/08/2021

Arduino <info@arduino.cc>
http://github.com/arduino-lib...
info@arduino.cc

Allows you to read the temperature, humidity, pressure, light and UV sensors of your MKR ENV Shield.

<a id='0840cef2-7626-462b-b055-eb15b7df6372'></a>

GO TO REPOSITORY

<a id='24c3f1f5-377f-4535-b34e-e6750fb9b1d4'></a>

Usage/Examples Compatibility Releases

The Arduino MKR ENV library allows you to read the sensors on the MKR ENV Shield. It manages the different interfaces used by the sensors on the shield to give you an uniform and simple set of functions to read them. The library takes care of the calculations needed to produce values in the requested units. The values returned are signed floats.

<a id='4a125b84-841f-4ddb-90e0-16480c064b29'></a>

To use this library:

```
1 #include <Arduino_MKRENV.h>
```

<a id='734265e1-04e1-434f-b302-2229ebb1dfdd'></a>

The Arduino MKR ENV library takes care of the sensor initialization and sets its values as follows:

Absolute pressure range: 260 to 1260 hPa.
Humidity range: 0 to 100% relative humidity (rH).
Humidity accuracy: ± 3.5% rH, 20 to +80% rH.
Temperature range -40 to 120 °C.
Temperature accuracy: ± 0.5 °C from 15 to 40 °C.
Lux range: 10 to 100,000 lux.
UVA/UVB resolution: 16-bit; unit µW/cm2.
UVIndex: 1 to 11+.

<a id='efd43ef1-5ed0-4f22-9fed-9ceda1dbcf2b'></a>

Usage/Examples
Compatibility
Releases
Methods +

<a id='e4c2e082-967b-40d2-a85d-2e7b75228337'></a>

Methods

\/ begin()

<a id='4db7b758-f400-4c93-a3a3-944fabc0a095'></a>

Help

<a id='732a9586-4371-4842-b76f-076eaa857e0f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='27dd4145-3270-4ffb-858c-67f6ee54ae90'></a>

1/10

<!-- PAGE BREAK -->

<a id='cb4b1ab1-c95f-4c34-be98-f7ac7a3a07a1'></a>

12/4/25, 2:51 PM

<a id='d24ed296-fb24-460e-9242-3704c830180a'></a>

Arduino_MKRENV | Arduino Documentation

<a id='92169dea-4fd8-44ec-abb9-4b9fd765114b'></a>

ARDUINODOCS

<a id='06f1bbbb-a56f-456e-abdd-3655e23b5f3a'></a>

Initialize the sensors on the shield.

<a id='70e0c676-1142-40e1-b9b7-0d8b965ed716'></a>

# Syntax

```
1 ENV.begin()
```

<a id='adfa65c9-241a-4af5-9a60-681e428179aa'></a>

Parameters

None.

<a id='9e4dff73-5f46-44b9-a998-ad3269d1be07'></a>

## Returns

1 on success, 0 on failure.

<a id='eeb54d06-3b98-42e9-b6ba-67c5ecd18312'></a>

# Example

```
1 if (!ENV.begin()) {
2   Serial.println("Failed to i
3   while (1);
4 }
```

<a id='48206411-75bb-4b91-84e2-471f21a4f6f0'></a>

## See also

end()
readTemperature()
readHumidity()
readPressure()
readIlluminance()
readUVA()
readUVB()
readUVIndex()

<a id='59126eea-fb5b-4b0a-bba5-52fd8f6c47d2'></a>

end()
De-initialize the sensors on the shield.

## Syntax

```
1 ENV.end()
```

## Parameters

<a id='6fd6f7bb-9f73-4484-a3f8-204a95e189ea'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='2c91b8da-dfb6-4b31-ab8a-f48a7b205253'></a>

2/10

<!-- PAGE BREAK -->

<a id='e3235c99-92a5-4269-b33c-8828e1d07ea6'></a>

12/4/25, 2:51 PM

<a id='f60f1a9b-2772-4e2e-8cf3-fe74b58d3647'></a>

Arduino_MKRENV | Arduino Documentation

<a id='6d66a4d0-0dac-451c-85a9-404119f4a738'></a>

ARDUINODOCS

<a id='e23c57ea-5ef5-48a2-8acd-18cdb4cc8646'></a>

## Returns
None.

## Example
```
1 ENV.end();
```

## See also
- begin()
- readTemperature()
- readHumidity()
- readPressure()
- readIlluminance()
- readUVA()
- readUVB()
- readUVIndex()

<a id='69eb483c-859f-4bc5-b5ee-3d2264f3e773'></a>

v readTemperature()
Read the temperature sensor's value. If no unit is specified as parameter, the value will be expressed in Celsius.

<a id='8f2d5a97-a56c-4a43-96d4-598bf16a6a68'></a>

## Syntax

```
1 ENV.readTemperature(unit)
```

<a id='25775d53-be17-45a5-9a49-07c06fa36c07'></a>

## Parameters

*unit*: FAHRENHEIT to get the temperature in Fahrenheit and CELSIUS to get the temperature in Celsius (default).

<a id='d13cf056-70f8-4276-8527-ec6805171fcd'></a>

## Returns

The sensor's temperature value as float in the specified unit.

<a id='b15dc297-39d3-43db-afc3-8adb1a631c99'></a>

Example

<a id='2ed9ca43-f59c-418b-9cb6-674cbd2dcc07'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='9899b577-2615-453b-8a52-faf190bc51b3'></a>

3/10

<!-- PAGE BREAK -->

<a id='213d08c8-2012-4e1a-b377-b2f153be1de8'></a>

12/4/25, 2:51 PM

<a id='3fcb5d0e-38c7-464f-9822-cb1f1ca1ddff'></a>

Arduino_MKRENV | Arduino Documentation

<a id='fb4c23b0-d48b-42a6-91b2-1e0285fc237b'></a>

ARDUINODOCS

<a id='be7ffb32-94ed-43da-ba1f-ad6cbf2dd25c'></a>

```
1 Serial.print("Temperature = ");
2 Serial.print(ENV.readTemperatur
3 Serial.println(" C");
```

<a id='cdb26587-aac6-4be5-a28c-1a37920f8254'></a>

## See also

begin()

end()

readHumidity()

readPressure()

readIlluminance()

readUVA()

readUVB()

readUVIndex()

<a id='d17dca78-4e56-4fd6-9c7f-45e106752136'></a>

readHumidity()

Read the HTS221 sensor's relative humidity
(rH), and returns it as a percentage. Read
more about relative humidity in this article.

<a id='527f440c-90f6-4acc-830f-8f605b06ba3c'></a>

# Syntax

```
1 ENV.readHumidity()
```

<a id='726fa45a-645e-4145-b671-3fb32697f580'></a>

Parameters

None.

<a id='0d1f4fe7-52c4-45ae-97ed-4ecddffca264'></a>

## Returns

Returns the relative humidity (rH) in percentage.

<a id='24473f61-20a1-42dd-91b9-3c52541ad402'></a>

# Example

```
Serial.print("Humidity     = ");
Serial.print(ENV.readHumidity());
Serial.println(" %");
```

<a id='aaec5b20-25e8-405d-b90b-cb511554ca3b'></a>

See also

begin()

<a id='9597ac38-da8d-449f-9efe-a65908b62440'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='42d48612-14ed-4003-bb92-618e54741afd'></a>

4/10

<!-- PAGE BREAK -->

<a id='8c8439f3-8a31-4c33-9859-da3e33408844'></a>

12/4/25, 2:51 PM

<a id='95e31dcf-635b-452d-8276-d2c31b7c1302'></a>

Arduino_MKRENV | Arduino Documentation

<a id='478b392b-36f8-4c6f-adb0-2eefa0b4a385'></a>

ARDUINODOCS

<a id='1a13148e-4214-4a1c-b4b0-98031b12f900'></a>

readPressure()
readIlluminance()
readUVA()
readUVB()
readUVIndex()

<a id='045b2379-625f-43eb-9bfc-19b73cf644b8'></a>

readPressure()

Read the pressure sensor's value. If no unit is specified, the value will be expressed in kilopascal.

<a id='5eed13a6-8868-443f-bf5c-7d96ca80e3f5'></a>

## Syntax

```
1 ENV.readPressure(unit)
```

<a id='4b23d3d9-2a7f-4e8d-990d-c5fd6af066e2'></a>

## Parameters

unit: PSI to get the pressure in pound
per square, MILLIBAR to get the
pressure in millibar and KILOPASCAL
to get the pressure in kilopascal
(default).

<a id='d12099b8-84cf-438c-af0e-963fefc90a5d'></a>

## Returns

The sensor's pressure value as float in the specified unit.

<a id='2f201705-2284-4d54-be68-2c5bbe58ddba'></a>

## Example

```
1 Serial.print("Pressure = ");
2 Serial.print(ENV.readPressure());
3 Serial.println(" kPa");
```

<a id='1e52de22-f561-4fce-8246-757c4c290b53'></a>

## See also

* begin()
* end()
* readTemperature()
* readHumidity()
* readIlluminance()
* readUVA()
* readUVB()
* readUVIndex()

<a id='7e329bb8-9ed3-4cfe-9088-0742ef1ae0a4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='401ec97d-9336-46cc-a875-0e83ea5ff910'></a>

5/10

<!-- PAGE BREAK -->

<a id='8149eb51-ad7d-452c-a9ec-b7fd7f0d232f'></a>

12/4/25, 2:51 PM

<a id='e5d4e548-2719-43ca-b71a-a9eaef09414d'></a>

Arduino_MKRENV | Arduino Documentation

<a id='91b7e701-afb8-4f26-9307-9c8707d716f9'></a>

ARDUINODOCS

<a id='8dee1664-518f-431e-8ce0-7b7ce1b12fac'></a>

readIlluminance()
Read the light sensor's value.

<a id='3e8665e5-cc53-419e-b47d-e6c0bcae752c'></a>

## Syntax

```
1 ENV.readIlluminance(unit)
```

<a id='e4fae01e-047f-4a97-b110-40ffe63a5489'></a>

# Parameters

unit: FOOTCANDLE to get the light
value in footcandle, METERCANDLE to
get the light in metercandle and LUX to
get the light value in lux (default).

<a id='2d1bc875-cf37-4271-b3ec-5b6a39753c0e'></a>

# Returns

The light sensor's value as float in the specified unit.

<a id='821fa859-9db0-460f-9110-a0645243752d'></a>

Example

```
1 Serial.print("Lux = ");
2 Serial.println(ENV.readIllumina
```

<a id='bcb9a5a4-cfae-4217-a269-b0ecdb86e2e7'></a>

See also

begin()
end()
readTemperature()
readHumidity()
readPressure()
readUVA()
readUVB()
readUVIndex()

<a id='7d8e18f0-b759-4b2d-8928-42741953114a'></a>

readUVA()
Read the UV sensor's UV A value.

<a id='151b2088-351f-4814-a4fe-cbe3fad7a353'></a>

Syntax

```
1 ENV.readUVA()
```

<a id='0f431a30-e401-48dc-ad32-913370550ca4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='c95f9bd5-9388-464f-869c-d2cdb670ac0e'></a>

6/10

<!-- PAGE BREAK -->

<a id='9a461e64-7318-4679-bd75-108a6254b683'></a>

12/4/25, 2:51 PM

<a id='9c58371c-d830-42cb-b1b9-8efe8ac31ae6'></a>

Arduino_MKRENV | Arduino Documentation

<a id='a96cd745-b828-46ff-af25-39a3c370eaa1'></a>

ARDUINODOCS

<a id='97e2236c-88ff-4694-9783-f3fc8c6ee2df'></a>

## Parameters
None.

## Returns
The UV sensor's UV A value.

## Example
```
1 Serial.print("UVA = ");
2 Serial.println(ENV.readUVA());
```

## See also
begin()
end()
readTemperature()
readHumidity()
readPressure()
readIlluminance()
readUVB()
readUVIndex()

<a id='b1aa42cc-f1e0-4cf1-b288-8a89c0d3fd76'></a>

readUVB()
Read the UV sensor's UV B value.

### Syntax

```
1 ENV.readUVB()
```

### Parameters

None.

### Returns

The UV sensor's UV B value.

### Example

<a id='be585a3b-73dd-4e61-b640-8d88317be409'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='94157c91-de29-47d9-926a-4c57340d06d8'></a>

7/10

<!-- PAGE BREAK -->

<a id='5ed32cee-630a-47c6-a282-a38f3309974a'></a>

12/4/25, 2:51 PM

<a id='d91c4cc9-d89a-480f-a86d-e025567ee208'></a>

Arduino_MKRENV | Arduino Documentation

<a id='a7d5e315-83d6-437e-8355-d27f62957d97'></a>

ARDUINODOCS

<a id='a9e19fb7-adcc-4c4b-94cc-061dcffc7613'></a>



<a id='84023407-79e6-42f3-a569-bef0267be1db'></a>

```
1 Serial.print("UVB = ");
2 Serial.println(ENV.readUVB());
```

<a id='7533eeb4-e67c-41eb-9ea3-4a7be7cb8357'></a>

## See also

* begin()
* end()
* readTemperature()
* readHumidity()
* readPressure()
* readIlluminance()
* readUVA()
* readUVIndex()

<a id='deb633a8-1487-4716-bd7f-7f6fbca1464e'></a>

readUVIndex()
  Read the UV sensor's UV index value.

<a id='cb8431ce-c110-47ab-8f28-a2c1fff0c955'></a>

## Syntax

```
1 ENV.readUVIndex()
```

<a id='d0a31388-bd96-416c-a712-72b36fd50ff1'></a>

**Parameters**

None.

<a id='871e1c43-125e-46eb-9b41-40b3ea0b056c'></a>

Returns

The UV sensor's UV index value.

<a id='054c00fb-dfa3-4ca9-a2d6-72523cbbd6f4'></a>

Example

```
1 Serial.print("UV Index = ");
2 Serial.println(ENV.readUVIndex(
```

<a id='6d3e0516-f68c-467a-8925-19ca3b0d2433'></a>

**See also**

begin()
end()
readTemperature()
readHumidity()
readPressure()

<a id='2025cc46-f6eb-4e11-aafc-db2da76e2c65'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='1b2d5d8b-dfc5-4371-aa9f-af95fb0f57b9'></a>

8/10

<!-- PAGE BREAK -->

<a id='2d2fac21-7c30-406c-902c-be96b5f15a52'></a>

12/4/25, 2:51 PM

<a id='32678fd2-0a33-40a8-9a10-59a6fe03f6ec'></a>

Arduino_MKRENV | Arduino Documentation

<a id='b623c261-8b5a-4aac-8726-c4ae86f80826'></a>

ARDUINODOCS

<a id='3b37c270-ba83-4bbe-865e-e3c7fb91c9d5'></a>



<a id='cce38344-b16f-46e3-8ec5-afa1c953eab3'></a>

readUVB()

<a id='93c58bc5-8007-4e20-807b-f2ded433e0b8'></a>

dropdown arrow readLux()

<a id='804474de-5ce7-47be-9340-40c090cf001f'></a>

### Description

Read the light sensor's value.

<a id='56da0884-f717-49b3-a19e-4db5176c07c4'></a>

## Syntax

```
1 ENV.readLux()
```

<a id='c23932f1-6787-45a6-94a3-fe032cff65ea'></a>

Parameters

None

<a id='d536eb05-dde1-4c79-bd56-7203d00800ae'></a>

# Returns

The light sensor's value in Lux.

<a id='8abdc02a-279f-4d2b-b4bb-2b8b1590f0f1'></a>

## Example

```
1 Serial.print("Lux: ");
2 Serial.println(ENV.readLux());
```

<a id='21ce0fed-9e95-4190-86c7-56a1cf10e1cb'></a>

See also

begin()
end()
readTemperature()
readHumidity()
readPressure()
readIlluminance()
readUVA()
readUVB()
readLux()

<a id='d6fd92af-d9be-4740-9c33-ce0eddefb928'></a>

Was this article helpful?

---

option Thumbs up: [ ]
option Thumbs down: [ ]

<a id='43e97c59-f0a5-4b6d-8869-4131d67e6496'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='6533c145-a5cb-4645-a588-f62134a6c514'></a>

9/10

<!-- PAGE BREAK -->

<a id='5df86494-4ede-4b2e-92c1-2f74630fbf26'></a>

12/4/25, 2:51 PM

<a id='72d450ee-1a67-4923-9e68-badc52df0cab'></a>

Arduino_MKRENV | Arduino Documentation

<a id='6951507d-86c9-4d9b-96d3-0c70750402e4'></a>

ARDUINODOCS

<a id='68153756-b517-4d2e-ae9e-8f89fdd49d23'></a>



<a id='1d1412a4-b4b2-4394-917b-4085e8c82e43'></a>

Project Hub
GitHub Repository
Forum

Product Compliance
Help Center
Trademarks & Licensing

<a id='fd5223ff-41e6-405d-965b-aa4a413af624'></a>

© 2025 Arduino

Terms Of Service Privacy Policy Security Cookie Settings

<a id='61d913c8-98d3-4b06-9a2f-0e298838c822'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='091e56b1-f27d-4fe9-9096-b753c5f4d5bf'></a>

10/10