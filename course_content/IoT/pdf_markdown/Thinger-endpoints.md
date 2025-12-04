<a id='aa7410f1-c289-4753-9bd1-714eb77d8be5'></a>

<::logo: thinger.io
thinger.io
The logo features the text "thinger.io" in black, with a hamburger menu icon to its left and a rectangular outline around the last two characters of the text.::>

<a id='ea726db0-8632-4af4-bfb6-e5db8690c9d2'></a>



<a id='53b1cc37-1dae-4e80-aa72-819acad7acba'></a>

PLATFORM FEATURES

<a id='d1090b84-9d3d-4761-b175-ff295ccffd30'></a>

GitHub icon Edit v

<a id='017deaf4-214b-45c6-b368-8db227e97144'></a>

ENDPOINTS

<a id='c64da006-eb12-4cbc-9070-04176df25347'></a>

An endpoint is the entry point to a service, a process, or any other destination. So, in Thinger.io, an endpoint can be defined like a target destination that can be called by devices to perform any action, like sending an email, sending an SMS, calling a REST API, interacting with IFTTT, calling a device from a different account, or calling any other HTTP endpoint.

<a id='441a94e8-517b-48d2-8454-1c57d8930365'></a>

Calling those endpoints directly by devices can be complex in small microcontrollers,
and would require more bandwidth in devices. This way, Thinger.io can handle endpoint
calls that can be requested directly by devices, activating them by using their identifier
and passing any information required. It also adds some flexibility, as the endpoint
request can be dynamically changed as necessary, while the deployed code in the
device remains the same.

<a id='f18d7047-d758-483b-8f34-efb38573ae57'></a>

## Create Endpoint

To manage all the endpoints, it is necessary to access the Endpoints section, by clicking on the menu item:

<a id='1864d5a2-3123-4b0d-a374-2c9f8ed95423'></a>

<::A black rectangular button/tab with a white list-like icon on the left and the word "Endpoints" in white text on the right.
: figure::>

<a id='1b475d14-608a-435d-a2f6-da842925bbac'></a>

Then click on the Add Endpoint button, which will open a new interface for entering the endpoint details:

<a id='ff09b7a5-adc8-41d2-a378-aa9a917cc961'></a>

1

<!-- PAGE BREAK -->

<a id='e228bc9e-1aa2-4731-949e-ee6eea00cecd'></a>

thinger.io

[Icon] [Icon] Statistics [Dropdown Icon] [Icon]

user [Dropdown Icon] [Profile Icon]

Endpoints > Add

Statistics

Devices

Dashboards

Data Buckets

Endpoints

Alarms

Access Tokens

Assets

File Storages

Products

Endpoint Details

Endpoint Identifier [Info Icon]
Enter endpoint identifier

Endpoint Name [Info Icon]
Enter endpoint name

Endpoint Description [Info Icon]
Enter endpoint description

Enabled [Info Icon]
option Enabled: [x]

Endpoint Type [Info Icon]
Select endpoint type [Dropdown Icon]

[Checkmark Icon] Add Endpoint

<a id='b3d2785e-be83-46b9-94ea-b3ddfbee875f'></a>

Here, it is necessary to configure different parameters:

*   **Endpoint Identifier**: Unique identifier for the endpoint (*the device must use this identifier for activating the endpoint*).
*   **Endpoint Name**: Unique name for the endpoint.
*   **Endpoint Description**: Fill here any description or detailed information needed to keep about the dashboard.
*   **Endpoint Type**: Defines the endpoint type, depending on the selected type, the endpoint will present different fields. In the following sections are described some of these types.

<a id='d42b79cb-9e7b-4150-8534-88892aad002f'></a>

Useful Endpoint types

<a id='1a9ae432-e6e7-4ba1-a206-38973432fa31'></a>

# Email Endpoint

An email endpoint enables the sending of emails from devices. The target email address, subject, and email body can be defined.

<a id='2050bb62-b02c-446f-b469-1a79da8dc279'></a>

The configurable parameters are:

*   **Email Address**: The target email address of the message.
*   **Email Subject**: The email subject.
*   **Email Body**: Allows defining the email body, which can be a plain JSON text with the data sent from the device, or a custom body that can also contain information gathered from the device.

<a id='b215c540-01e4-4417-ae04-d481771098be'></a>

2

<!-- PAGE BREAK -->

<a id='0c34ad17-3b46-4185-96b5-bc065c97fd49'></a>

There is an example of an email endpoint that contains some text and variables that are filled when the device calls the endpoint, adding the current temperature and humidity reported by the device. Notice that `temperature` and `humidity` variables are closed inside double brackets `{{}}`, so the endpoint will be expecting this information to complete the body.

<a id='9b633ce2-ab70-4b19-bf95-9daac7034696'></a>

Endpoint Type
Email

Email Address
alvarolb@gmail.com

Email Subject
Example email for documentation

Email Body
option Send device data as JSON: [ ]
option Send custom body: [x]

<a id='246791ab-5127-4326-8e05-ea22187ab19a'></a>

<table id="2-1">
<tr><td id="2-2">H1</td><td id="2-3">H2</td><td id="2-4">H3</td><td id="2-5">H4</td><td id="2-6">H5</td><td id="2-7">H6</td><td id="2-8">P</td><td id="2-9">pre</td><td id="2-a">&quot;</td><td id="2-b">B</td><td id="2-c">I</td><td id="2-d">U</td><td id="2-e">S (with strikethrough)</td><td id="2-f">bulleted list icon</td><td id="2-g">numbered list icon</td><td id="2-h">curved arrow pointing left</td><td id="2-i">curved arrow pointing right</td><td id="2-j">circle with diagonal line</td></tr>
<tr><td id="2-k">four horizontal lines</td><td id="2-l">four horizontal lines</td><td id="2-m">four horizontal lines</td><td id="2-n">four horizontal lines</td><td id="2-o">four horizontal lines (with play icon)</td><td id="2-p">menu icon</td><td id="2-q">&lt;/&gt;</td><td id="2-r">image icon</td><td id="2-s">link icon</td><td id="2-t">play button icon</td><td id="2-u"></td><td id="2-v"></td><td id="2-w"></td><td id="2-x"></td><td id="2-y"></td><td id="2-z"></td><td id="2-A"></td><td id="2-B"></td></tr>
</table>

<a id='a01ea9e4-736c-4de5-82dd-89639ce0c783'></a>

Hi Dude! ☁️
Temperature is: {{temperature}} °C
Humidity is: {{humidity}} %

<a id='4eabaf0f-803b-4887-b6ea-36901bb244d0'></a>

Calling endpoints is well documented here ↗, but it is basically required to call the endpoint by using the `call_endpoint` method, which requires the endpoint id, `ExampleEmail` in this example, the optional data to be sent to the endpoint, which is a `pson` document (quite similar to JSON) with two keys named `temperature` and `humidity` holding the readings from a DHT sensor:

<a id='505d8098-c041-4645-9fa7-fe05ae4c5d40'></a>

3

<!-- PAGE BREAK -->

<a id='d96271d5-ef2f-464f-a92c-11b6987f3926'></a>

Endpoint Type
HTTP Request

Request URL
POST https://dummyhost.com/data

Request Headers
Authorization Bearer 14in63er41v4r(
+ Add Header

Request Body
option Send device data as JSON: [x]
option Send custom data: [ ]

<a id='f117d059-a7a3-4275-b59f-018e0c28f5a3'></a>

Telegram Bot Endpoint

<a id='3102e33e-511c-4b98-86f8-3f50383a9b7f'></a>

This endpoint is pre-configured to send data to a Telegram bot in a simple way and thus use the messaging platform to get alerts or data from the IoT devices through Thinger.io.

<a id='1503fe4d-f419-4478-9c68-8127bb859093'></a>

thinger.io

Statistics
Devices
Dashboards
Data Buckets
**Endpoints**
Alarms
Access Tokens
Assets
File Storages
Products
Projects
Plugins
Toolbox

<a id='23daf549-aea2-498d-b51a-2932a2198af4'></a>

☰ 🗃 Statistics ▾ ⊕ 📣 user ▾ 👤

<a id='44a14d2c-d660-4d76-85c4-6e24cf5ccbb0'></a>

Endpoints > Add

Endpoint Details

Endpoint Identifier: TelegramTest
Endpoint Name: FirstEndpoint
Endpoint Description: Sending data to telegram bot
option Enabled: [ ]
Endpoint Type: Telegram Send Message
Bot Token: 9x1x3x4x6:AxH0JcxmPUhnERY_VXXnnO5c_8valwZ9XOOXX
Chat Identifier: 1096342XXX
Chat Message: the current temperature is {{temperature}}

Add Endpoint

<a id='7cf50854-6856-48ee-9e49-61d2c31a84a6'></a>

The next parameters need to be configured to work with Telegram bot:

<a id='a9d9db2c-de8d-437c-ac09-43f67415c814'></a>

• Bot Token: Is the bot identification and authorization stream; this parameter can be left empty on this form in order to specify it directly in the device source code with the key "token".

<a id='058bb91d-2503-4ebb-8617-31874b2615b4'></a>

5

<!-- PAGE BREAK -->

<a id='86a6632d-b4bd-4903-b5fc-d90bd6b25119'></a>

- **Chat Identifier**: Is a 10-digit chat identifier that can be obtained from Telegram conversation information. It can be left empty at this configuration and be called in the source code with the key "chat".
- **Chat Message**: The text and device data that is to be sent in the message can be specified here or hardcoded in the device to be sent on the endpoint call with the key "message".

<a id='ab234f18-3234-4bcd-808d-ff89b3e2b3d9'></a>

Previous
DASHBOARDS

<a id='d3003965-7792-4f66-9b26-1335e9e0baa6'></a>

Next
ALARMS

<a id='c310839d-524c-4031-9156-7679640ba4ae'></a>

Last updated 4 months ago

<a id='eb9a3906-00a8-49f3-b068-5a0aca1339be'></a>

Was this helpful?
option Happy: [ ]
option Neutral: [ ]
option Sad: [ ]

<a id='f7e17b94-0028-4e0d-b094-6f5f0d9a1b6b'></a>

<::Three icons are displayed horizontally. From left to right: a sun icon (representing light mode), a computer monitor icon (representing system mode), and a crescent moon icon (representing dark mode). The computer monitor icon is highlighted with a light gray background, indicating it is selected.: figure::>

<a id='2f5cdc60-2d58-4885-b902-8778ad32245a'></a>

6