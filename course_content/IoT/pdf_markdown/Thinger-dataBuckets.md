<a id='84ac70c1-b6ce-41b2-8d5d-28a0a4422761'></a>

<::logo: thinger.io
thinger.io
The logo features the company name in black sans-serif font, with a hamburger menu icon to the left and a square outline around the '.io' suffix.:>

<a id='837f6cf3-f3b1-45a6-92cf-463c59f34416'></a>



<a id='8757fec9-a3b8-4b64-8b47-a412a0ba3efe'></a>

PLATFORM FEATURES

<a id='86530c80-4923-4012-bcb0-0abd2bb89ac6'></a>

GitHub icon Edit v Edit

<a id='296d89d7-1c6c-4745-af9e-e038bf4053dc'></a>

# DATA BUCKETS
A data bucket is a type of virtual storage that can hold time series data, such as temperature or humidity measurements over time. However, it can also be used to store other types of events, such as motion detections, garage door openings, temperature alerts, and more.

<a id='a06b87a2-2122-4aaf-ac0d-5bee2077c5b0'></a>

This information can be used to plot information in dashboards or can be exported in different formats for offline processing.

<a id='c7c79ed1-a5c5-4890-befd-469519be45fe'></a>

# Create Bucket

To create a data bucket, access the `Data Buckets` feature, by clicking on this section:

<a id='2ab4d202-22f2-4680-8954-96db894d3515'></a>

Data Buckets

<a id='8c5a2a54-f0cb-4179-a22e-49ce8da1a3ae'></a>

To create the bucket, just press the **Add Bucket** button, which will show the following screen:

<a id='60128d3e-feaf-41d4-8b77-f5532200762d'></a>

1

<!-- PAGE BREAK -->

<a id='37b66dbb-8980-4116-88a1-544bf79404c7'></a>

thinger.io

B Statistics user

Buckets > Add

# Bucket Details

## Bucket Settings

Bucket Id ⓘ: Enter a bucket id

## Bucket Information

Bucket Name ⓘ: Bucket name

Bucket Description ⓘ: Optional bucket description

## Bucket Configuration

Enabled ⓘ: [toggle switch - on]

Data Tags ⓘ: Type tags...

Data Source ⓘ: Select data source

## Advanced Options

option Asset Type ⓘ: [ ] Select Type...

option Asset Group ⓘ: [ ] Select Group...

option Product ⓘ: [ ] Select Product...

## Database Options

Backend ⓘ: MongoDB

Retention: 3 months

--- Add Bucket ---

## Navigation

*   Statistics
*   Devices
*   Dashboards
*   Data Buckets
*   Endpoints
*   Alarms
*   Access Tokens
*   Assets
*   File Storages
*   Products
*   Projects
*   Plugins
*   Toolbox
*   Administration
    *   User Accounts
    *   Cluster Hosts
    *   Domains
    *   Brands
    *   OAuth2 Clients
    *   Proxies
    *   Billing

<a id='5f6f5683-cde0-4b5a-bde7-b9d8daf8ff0a'></a>

Here, it is necessary to configure different parameters:

*   **Bucket ID**: Unique identifier for the bucket.
*   **Bucket name**: Use a representative name to remember the bucket scope, like `WeatherData`.
*   **Bucket description**: Fill here any description with more details, like Temperature and humidity in the house.
*   **Enabled**: Data bucket recording can be enabled or disabled. Just switch it on to enable it.
*   **Data source**: This parameter allows setting the behavior of the data bucket by selecting the data source and also the sampling method. As there are many different options, this feature is detailed in the section below.

<a id='b903ba29-d268-41d9-9f80-cde17803381e'></a>

The following sections explain the different data bucket data acquisition modes and timing configurations:

<a id='402f9acc-ba95-4999-bc3a-015a6276a7dc'></a>

From Device Resource

<a id='5a21a213-496f-40e5-8cc6-4ace01f85fc1'></a>

2

<!-- PAGE BREAK -->

<a id='2c47bd9f-5809-4cf9-bf58-a6572484a393'></a>

This option subscribes Thinger.io Server to a specific device resource (such as temperature, motion, and so on). It can be configured to retrieve data from the device in a specific sampling interval or wait for asynchronous communications from devices by means of the "Refresh mode" parameter.

<a id='b216bd2a-b630-4229-a0d8-23fdd610e3ad'></a>

Note that this option is only compatible with devices that have been provided with Thinger.io Software client libraries (Arduino, Linux or Raspberry), and it will only work properly if the device maintains a permanent connection with the server.

<a id='2a5b5973-021b-4a13-b2a3-89159a446394'></a>

*   **Sampling interval:** Configure the bucket profile to retrieve data from device resources at a specific timing, which can be changed on demand, without modifying the device sketch. Another benefit is that no additional codification is needed to implement this feature and start storing data. The next basic code example will store two variables in the data bucket when using the "sampling interval" configuration.

<a id='1eeaf7ef-449a-4e10-b8a7-59d3dc9272f7'></a>

```
// define the resource just once in the setup() section
thing["TempHum"] >> [] (pson &out){
    out["temperature"] = dht.readTemperature();
    out["humidity"] = dht.readHumidity();
};
```

<a id='2ac8cd74-2534-467e-b23d-cd6e71fb375d'></a>

- **Update by Device:** This option allows the device to stream the information when required, i.e., by raising an event when detected. In this case, refresh mode must be set as the `Update by Device` option while configuring the bucket, and the device source code will contain a streaming instruction for the resources (also described in more detail here ↗). This way, the data bucket will be listening to a device resource, and its information is registered in every stream call.

<a id='e23170a5-2d0f-40a2-858e-d5863fea829b'></a>

3

<!-- PAGE BREAK -->

<a id='eac8a2bd-68a8-4485-877b-7bc2416f73ab'></a>

```c
/*"TempHum" resource was declared in the setup() function
but the stream instuction is added in the loop*/
void loop() {
  thing.handle();
  // use own logic here to determine when to stream/record the
  resource.
  if(requires_recording) {
    thing.stream("TempHum");
  }
}
```

<a id='097e1117-a2e3-4cdb-9905-002182cb36be'></a>

! This instruction should NEVER be called each loop execution or at lower than 60s streaming rates, as the bucket system will only store data every 60s.

<a id='0db8a983-8ff6-49b2-8e16-4a4297a7cd72'></a>

# From device Write Call

This option sets the bucket in passive mode, waiting to be called by any Thinger.io "Generic Device" (with Thinger.h libraries on it) by means of the `write_bucket()` method. The distinguishing feature of this mode is its ability to store data from multiple devices in a single data bucket.

<a id='22b0ba20-aab2-4fe5-8d95-070c7c9dab96'></a>

Here is an example of an ESP8266 device writing information to a bucket using the `write_bucket` function:

<a id='90a0eb0e-74fd-4149-8e7a-163d7e7c2646'></a>

4

<!-- PAGE BREAK -->

<a id='9b2a8f59-cf66-46a9-b48c-582a29efcfc8'></a>

void setup() {
  // define the resource with temperature and humidity
  thing["TempHum"] >> [] (pson &out){
    out["temperature"] = dht.readTemperature();
    out["humidity"] = dht.readHumidity();
  };
}

void loop() {
  // handle connection
  thing.handle();
  // write to bucket BucketId the TempHum resource
  thing.write_bucket("BucketId", "TempHum");
  // sleep the device SLEEP_MS milliseconds
  ESP.deepSleep(SLEEP_MS*1000, WAKE_RF_DEFAULT);
}

<a id='e27f75c5-3002-42c2-8228-514e5e88d285'></a>

## From API Request (for 3rd parties):

This configuration allows to store data from any other device or data source that can't be equipped with Thinger.io libraries on its codification. The data bucket will be set in passive mode, waiting to receive data from any **HTTP Device Callback** that has been properly configured to send data to this data bucket.

<a id='b09a4a8a-3d12-4ffa-b749-be32f6b5f0d2'></a>

This feature can also be used to store data directly from any third-party platform just calling the data bucket REST API and sending information in JSON format. But it is preferable to use the HTTP device way.

<a id='8695d6b1-e656-4a3f-aa5a-b675c8ad94e7'></a>

## From MQTT Topic

Data buckets can be configured to subscribe to an MQTT topic in the same way as another MQTT client can. This feature enables storing published data within the same topic. Therefore, caution is advised if multiple devices are publishing to it. This configuration can be applied during the creation of a new data bucket or later using the Settings tab.

<a id='f62b989f-3e22-486b-805c-986133fcefce'></a>

5

<!-- PAGE BREAK -->

<a id='80cf1694-66a8-4501-893d-95c0e9fdc0d9'></a>

thinger.io

- Statistics
- Devices
- Dashboards
- **Data Buckets**
- Endpoints
- Alarms
- Access Tokens
- Assets
- File Storages
- Products
- Projects
- Plugins
- Toolbox

<a id='5132e85e-5363-4c53-81fb-79ceca11bfbf'></a>

Administration

User Accounts

Cluster Hosts

Domains

Brands

OAuth2 Clients

Proxies

Billing

<a id='b4fe98ef-1653-4e87-a001-e3d9cf00dda7'></a>

[Menu/List Icon] [Folder Icon] Statistics [Dropdown Arrow] [Add/Plus Icon]

<a id='90080098-569c-49b7-915e-41ba10037fa9'></a>

user

<a id='fc7170de-8126-4fe7-93e2-a9356dedf587'></a>

Buckets > Add

### Bucket Details

#### Bucket Settings
Bucket Id: MQTTexample

#### Bucket Information
Bucket Name: from MQTT topic
Bucket Description: Bucket subscribed to MQTT Topic

#### Bucket Configuration
option Enabled: [ ]
Data Tags: Type tags...
Data Source: Select data source

#### Advanced Options
option Asset Type: [ ] Select Type...
option Asset Group: [ ] Select Group...
option Product: [ ] Select Product...

#### Database Options
Backend: MongoDB
Retention: 3 months

Add Bucket

<a id='efa932dd-0b5a-43ae-9159-f7f4203fa626'></a>

Once this source has been selected, the interface will show a new input text in which the topic trace can be written:

<a id='75e82977-b1d6-4418-bed1-444a8a61da04'></a>

6

<!-- PAGE BREAK -->

<a id='0bdb2169-01f7-487a-a82b-9f9c7ecaa516'></a>

thinger.io

- Statistics
- Devices
- Dashboards
- Data Buckets
- Endpoints
- Alarms
- Access Tokens
- Assets >
- File Storages
- Products
- Projects
- Plugins
- Toolbox >

<a id='79de8e1c-d031-4983-8a7e-82ba7a28ab37'></a>

Administration
User Accounts
Cluster Hosts
Domains
Brands
OAuth2 Clients
Proxies
Billing

Account

<a id='065f5de2-59aa-459e-abbe-e8f8fb58510f'></a>

Menu icon | Folder icon | Statistics dropdown | Plus icon | Megaphone icon | user- | User profile icon

<a id='447017e8-1927-4d9a-9b2d-b4f2ec18ee83'></a>

user

<a id='2a8ab5fa-06aa-494f-bd70-efa467be3f93'></a>

Buckets > Add

### Bucket Details

#### Bucket Settings

Bucket Id: MQTTexample

#### Bucket Information

Bucket Name: from MQTT topic
Bucket Description: Bucket subscribed to MQTT Topic

#### Bucket Configuration

option Enabled: [x]
Data Tags: Type tags...
Data Source: From MQTT Topic
MQTT Topic: kitchen/temperature

#### Advanced Options

option Asset Type: [ ] Select Type...
option Asset Group: [ ] Select Group...
option Product: [ ] Select Product...

#### Database Options

Backend: MongoDB
Retention: 3 months

<a id='9ed9a5e1-4c52-4cff-b145-379d97188af3'></a>

option Add Bucket: [x]

<a id='d4913740-d835-40b4-a33b-8b03b82a4faa'></a>

i Note that the data buckets system has been created to store JSON format messages, so the data from the MQTT device must be in this format.

<a id='f10c2e34-2f70-4f57-bf7d-2d24768ae9bc'></a>

# Custom data timestamp

Thinger.io data bucket feature has been created using time series databases, The system has been programmed to store the data points using the timestamp of the instant they are stored in the database as the indexing variable, however, it is possible to customize this variable by entering a timestamp in the payload using this key-value structure:

<a id='150c5260-50c1-4c90-8bbf-c5188c34e3ba'></a>

7

<!-- PAGE BREAK -->

<a id='cdf5de3e-5e4b-4f2a-b878-86c2bada30a5'></a>

// example of datapoint with custom timestamp
{
  "ts": 1671536877360,
  "lat": 40.416775,
  "lng": -3.70379,
  "temperature": 23.33,
  "humidity": 32.44
}

<a id='05c0434e-69eb-4dd6-85a8-8b6b0b6620b3'></a>

The time must be expressed with a standard Epoch Timestamp expressed in milliseconds. This functionality allows storing data by the time they were produced instead of being stored. It also allows to correct or modify data already stored in the platform.

<a id='1d9ef91b-4795-4b27-8f40-ea4f3bd7269f'></a>

! Note that if the TS of a new datapoint matches with an old data bucket entry, it will be overwritten.

<a id='1726092b-402d-418d-abb9-ffbb8c9b0e00'></a>

## Review Bucket Data

Once the data bucket has been configured and it starts to record data from a device or from write calls, it will display the information inside a table. Every record contains the server timestamp in UTC (but shown in local time zone in the console) and the record value. The value stored in the data bucket can be a single value or any other JSON document. If the JSON document is composed of key-value pairs, like in the previous examples, they will be displayed in tabular format:

<a id='b2c412e5-652a-49b3-9ec3-85a5f38ab232'></a>

8

<!-- PAGE BREAK -->

<a id='bfa5dbd8-071b-49c8-a204-436bf40d7c2c'></a>

Buckets > DBClimaStick1 > Data

<a id='4871c0f9-3dfb-489a-b63a-6bd2d3c5e4c0'></a>

Data

<a id='d2fb675f-8b6a-4012-b0b2-8301b7668b38'></a>

Import

<a id='573f6933-a85c-495b-ab70-59ccfd622fcf'></a>

Export

<a id='3c03ad92-4fd6-464d-b371-2ef4e767b000'></a>

Clear

<a id='dc5aad9f-4552-4c4d-a0c5-80da9e49f038'></a>



<a id='f2f64e45-da8b-431c-9b6e-ea63414d691f'></a>

Last 24 hours

<a id='f21e2fd0-d584-4834-8b11-ef4ee63ec49b'></a>

Refresh
Last 24 hours
<table id="8-1">
<tr><td id="8-2">Date</td><td id="8-3">altitude</td><td id="8-4">humidity</td><td id="8-5">lux</td><td id="8-6">pressure</td><td id="8-7">temperature</td></tr>
<tr><td id="8-8">6/6/2025, 11:34:33</td><td id="8-9">683.7427978515625</td><td id="8-a">18.109375</td><td id="8-b">0</td><td id="8-c">933.7755737304688</td><td id="8-d">37.459999084472656</td></tr>
<tr><td id="8-e">6/6/2025, 11:34:28</td><td id="8-f">683.97705078125</td><td id="8-g">18.0390625</td><td id="8-h">0</td><td id="8-i">933.7492065429688</td><td id="8-j">37.5</td></tr>
<tr><td id="8-k">6/6/2025, 11:34:23</td><td id="8-l">683.9899291992188</td><td id="8-m">18.0869140625</td><td id="8-n">0</td><td id="8-o">933.7477416992188</td><td id="8-p">37.5099983215332</td></tr>
<tr><td id="8-q">6/6/2025, 11:34:18</td><td id="8-r">684.1339111328125</td><td id="8-s">18.111328125</td><td id="8-t">0</td><td id="8-u">933.7315673828125</td><td id="8-v">37.52000045776367</td></tr>
<tr><td id="8-w">6/6/2025, 11:34:13</td><td id="8-x">683.9147338867188</td><td id="8-y">18.1005859375</td><td id="8-z">0</td><td id="8-A">933.7562255859375</td><td id="8-B">37.560001373291016</td></tr>
<tr><td id="8-C">6/6/2025, 11:34:08</td><td id="8-D">683.8480834960938</td><td id="8-E">18.1572265625</td><td id="8-F">0</td><td id="8-G">933.7637329101562</td><td id="8-H">37.470001220703125</td></tr>
<tr><td id="8-I">6/6/2025, 11:34:03</td><td id="8-J">683.9968872070312</td><td id="8-K">18.205078125</td><td id="8-L">0</td><td id="8-M">933.7470092773438</td><td id="8-N">37.459999084472656</td></tr>
<tr><td id="8-O">6/6/2025, 11:33:58</td><td id="8-P">683.9953002929688</td><td id="8-Q">18.2041015625</td><td id="8-R">0</td><td id="8-S">933.7471923828125</td><td id="8-T">37.45000076293945</td></tr>
<tr><td id="8-U">6/6/2025, 11:33:53</td><td id="8-V">683.6176147460938</td><td id="8-W">18.103515625</td><td id="8-X">0</td><td id="8-Y">933.7896118164062</td><td id="8-Z">37.619998931884766</td></tr>
<tr><td id="8-10">6/6/2025, 11:33:48</td><td id="8-11">683.5880737304688</td><td id="8-12">18.06640625</td><td id="8-13">0</td><td id="8-14">933.79296875</td><td id="8-15">37.59000015258789</td></tr>
<tr><td id="8-16">6/6/2025, 11:33:43</td><td id="8-17">683.9577026367188</td><td id="8-18">18.13671875</td><td id="8-19">0</td><td id="8-1a">933.7514038085938</td><td id="8-1b">37.54999923706055</td></tr>
<tr><td id="8-1c">6/6/2025, 11:33:38</td><td id="8-1d">683.7562255859375</td><td id="8-1e">18.1796875</td><td id="8-1f">0</td><td id="8-1g">933.7740478515625</td><td id="8-1h">37.439998626708984</td></tr>
<tr><td id="8-1i">6/6/2025, 11:33:33</td><td id="8-1j">683.8201904296875</td><td id="8-1k">18.1796875</td><td id="8-1l">0</td><td id="8-1m">933.766845703125</td><td id="8-1n">37.43000030517578</td></tr>
</table>

<a id='7ac99d5d-9093-4f2a-8c47-51caf6c80f2b'></a>

# Bucket Data Import

In order to make bulk data upload or buckets backup processes, the data bucket system has been provided with an import feature that is able to retrieve information from .csv files from a Thinger.io **File System** and store its data using the timestream specified in the file rows.

<a id='1e49eb35-2176-4e5d-a946-6b97eab12618'></a>

Note that using this feature has a **few restrictions**.

1. Each row must contain just one variable and use a ";" separation mark.
2. The file must contain a column identified as "ts" with the Linux Timestream in milliseconds, which will be used to create the temporary serial.

<a id='f3653e39-f9af-40d4-901b-056104aba1cf'></a>

Also, the user account must be able to use File Systems, which is a premium feature, so freemium users can't perform these processes. The accompanying image serves merely as an example; labels such as "File Storage" and "File Name" may vary in the interface:

<a id='dcfc91ba-a9c0-4146-ae90-6b15d54cff94'></a>

9

<!-- PAGE BREAK -->

<a id='a3c91262-63f5-4556-a64f-930913f7fcd5'></a>

Buckets > DBClimaStick1 > Import

Data Import Export Clear [menu icon]

### Bucket Data Import

File Storage [info icon]: CodigoBC660 [dropdown arrow]

File Name [info icon]: test.csv

Import Progress [info icon]: 0%

Import Data

<a id='385a9db5-054f-41af-afcd-d7b5f840e236'></a>

ⅰ Files resulting from a data bucket export are completely suitable for the import feature, so they are perfect examples to observe a valid data frame

<a id='80cb53d4-22a9-4e61-bb89-775d5922292e'></a>

The import process allows filling the data bucket with the same data contained in the CSV, ordered based on the TimeStamp in milliseconds included in the file.

<a id='5c0582a7-0961-40ce-8821-74eb914e99c2'></a>

To execute an import, the following steps must be carried out:
1. Create a new File System (following these instructions) profile with public access configuration, or open an existing one and upload the .csv file to be imported into the File System.
2. Create the new data bucket
3. Select the source File System and place the file identifier in the "Filename" section.
4. Click on the "Import Data" button.

<a id='4c88a9c7-acf5-40c6-b77c-10742986d2f0'></a>

# Export Bucket Data

It is possible to export all stored information in various file formats, allowing for offline data processing, such as applying Artificial Intelligence, Business Analytics, Big Data, and so on. To do this, access the bucket and configure the export process:

<a id='af98d05e-f997-4875-ba47-271ac1082f20'></a>

10

<!-- PAGE BREAK -->

<a id='79ef523c-9d0d-409d-b67a-d3499c96700b'></a>

thinger.io
* Statistics
* Devices
* Dashboards
* Data Buckets
* Endpoints
* Alarms
* Access Tokens
* Assets >
* File Storages
* Products

<a id='07415b25-8a39-45aa-97dc-f69753e9a756'></a>

☰ 📁 Statistics ▾ ⊕

<a id='b5a6d1f1-91a1-4fdb-8bd9-885f085ab901'></a>

user

<a id='d91da3d3-360e-488f-ab90-ed178783e332'></a>

Buckets > DBClimaStick1 > Export

<a id='b13ede94-23e7-4c9a-b240-4450220a11ee'></a>

Buckets > DBClimaStick1 > Export Data Import option Export: [x] Clear <::hamburger menu icon::>

Bucket Data Export

Export Format
option CSV (Comma Separated Values): [x]

Timestamp
option ISO Date: [x]

Export Range
option Export all data in bucket: [x]
option Specify a custom data range for export the data: [ ]

Callback
option None: [x]

Export Data

<a id='746826b2-c651-411c-a5cf-15d1f1216aa6'></a>

The data bucket download configurable parameters are:
*   **Export format**: To obtain a CSV, ARFF, or JSON format file
*   **Timestamp**: Timestamp or ISO date format
*   **Export range**: This section allows downloading the complete data bucket or selecting a custom range.
*   **Callback**: To set how the ending of the data bucket export process will be notified. Currently, there are two ways:
    *   Sending an email to the account's associated address
    *   Calling an endpoint. This option allows sending the download link to third parties using an Endpoint profile.

<a id='1a445ab1-ac3e-4309-b092-68d717b98788'></a>

Once the export data range and format have been selected, the system will create a download link that will be stored in the "Export List" section below. These links can be used to provide customers with custom data reports from the IoT data.

<a id='e17c4633-3bed-41f9-b416-cc00c68f1ebc'></a>

<table id="10-1">
<tr><td id="10-2">C (refresh icon)</td><td id="10-3">Refresh</td><td id="10-4"></td><td id="10-5">Q Search Export</td></tr>
<tr><td id="10-6"></td><td id="10-7">File</td><td id="10-8">Export Date</td><td id="10-9">Export State</td></tr>
<tr><td id="10-a"></td><td id="10-b">20250529T081102Z.jt.DBClimaStick1.cHcrrXfj.csv</td><td id="10-c">5d</td><td id="10-d">Completed</td></tr>
<tr><td id="10-e">Sho</td><td id="10-f">ving 1 export</td><td id="10-g"></td><td id="10-h"></td></tr>
</table>

<a id='2cdbbf89-1b5d-4de1-baaf-cfafa4578cdf'></a>

The download links will be available for 3 months if the instance administrator has not specified a different interval.

<a id='1922be00-44a7-4941-a1df-fdc30179a1c7'></a>

Clear Bucket Data

<a id='8ff89248-1ba1-43cf-853e-965c1841ade2'></a>

11

<!-- PAGE BREAK -->

<a id='ebee5c6d-2d9a-419d-9264-ddc8834bba12'></a>

Sometimes it can be useful to clear the bucket information without deleting the whole bucket, creating and configuring it again. Therefore, the bucket, or a portion of it, can be easily cleared from the bucket page. During the clearing process, the bucket can still record information from devices.

<a id='d3da15f5-d6f2-4466-86a7-576836aed5b4'></a>

thinger.io

Statistics
Devices
Dashboards
Data Buckets
Endpoints
Alarms

Buckets > DBClimaStick1 > Clear

user
Data Import Export Clear

Bucket Data Clear

Clear Range:
option Clear all data in bucket: [x]
option Specify a custom data range for clearing the data: [ ]

Clear Data

<a id='da42ab1e-11e2-4775-b60e-d55fb2a40ed5'></a>

Data bucket profiles can also be deleted from the data bucket list by selecting the profiles to be deleted and pressing the red "Remove Bucket" button:

<a id='8d58b142-c52b-47d4-877c-aa8e5d4efa33'></a>

thinger.io

- Statistics
- Devices
- Dashboards
- Data Buckets
- Endpoints
- Alarms
- Access Tokens
- Assets >
- File Storages
- Products

<a id='25647fad-7e18-453c-b4f6-ababb8ca4657'></a>

Statistics
user
Buckets
< 1 Set Type Set Group Clone Remove
<table><thead><tr><th></th><th>Bucket</th><th>Description</th><th>State</th><th>Type</th><th>Group</th></tr></thead><tbody><tr><td>option : [ ]</td><td>from MQTT topic<br>MQTTexample</td><td>Bucket subscribed to MQTT Topic</td><td>Normal</td><td></td><td></td></tr><tr><td>option : [ ]</td><td>EnvCS<br>EnvCS</td><td>Environment de ClimaStick, con data source from device resource, en vez de from api request</td><td>Normal</td><td></td><td></td></tr><tr><td>option : [ ]</td><td>EnvironmentClimaStick<br>EnvironmentCS</td><td></td><td>Normal</td><td></td><td></td></tr><tr><td>option : [ ]</td><td>DBClimaStick1<br>DBClimaStick1</td><td>soy el data bucket de la ClimaStick online</td><td>Normal</td><td></td><td></td></tr></tbody></table>
Showing 4 buckets

<a id='cc98329a-85b3-4800-962e-f2f457a2d275'></a>

Previous
DEVICES ADMINISTRATION

<a id='f2809132-0970-49b2-8120-3c85975cc4d7'></a>

Next
DASHBOARDS

<a id='c1dd0dcd-1c52-486b-8f5c-87617ea53dfa'></a>

Last updated 5 months ago

<a id='6810333b-9e05-4534-a157-877c425e7bf9'></a>

Was this helpful?
option happy face: [ ]
option neutral face: [ ]
option sad face: [ ]

<a id='ea1680cb-8a29-4b3b-b65d-9492df82ec5d'></a>

<::option Sun (Light Mode): [ ]
option Computer Monitor (System Default): [x]
option Moon (Dark Mode): [ ]
: figure::>

<a id='e39155a3-e4a2-464e-a5dd-cc0c20728b0f'></a>

12