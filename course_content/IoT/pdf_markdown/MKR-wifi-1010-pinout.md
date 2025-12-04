<a id='7d255006-df24-483e-9db1-3259d9d846f1'></a>

<::logo: Arduino
ARDUINO
It features an infinity symbol with a minus sign on the left and a plus sign on the right, all in a light gray color.::>

<a id='1cd18851-a023-44e5-b319-21e2c4fb4a3c'></a>

ARDUINO
MKR WIFI 1010
STORE.ARDUINO.CC/MKR-WIFI-1010

<a id='2cb8a469-a667-4ca3-a324-b79432e43666'></a>

<::An illustration of a circuit board (likely an Arduino-compatible board) with a Li-Po battery connected. The board is teal colored and features various electronic components like chips, resistors, capacitors, and LEDs. A gray rectangular Li-Po 3.7 V battery is shown on the left, connected to the board via red and black wires, indicating positive (+) and negative (-) terminals. On the top edge of the board, an orange LED is labeled "Battery Charger LED" and a green LED is labeled "Power". The board has pin headers along both long sides, with numerous pins labeled for their functions.On the right side of the board, from top to bottom, the pins are labeled as follows:  - GND  - PA08 SDA  - PA09 SCL  - PA21 WK  - +5V  - LED_BUILTIN  - +5V  - VIN  - +3V3  - GND  - RESET  - D14 PB22 TX (SC5)  - D13 PB23 RX (SC5)  - ~D12 PA09 SCL (SC2)  - D11 PA08 SDA (SC2)  - ~D10 PA19 CIPO (SC1)  - D9 PA17 SCK (SC1)  - ~D8 PA16 COPI (SC1)  - ~D7 PA21  - ~D6 PA20On the left side of the board, from top to bottom, the pins are labeled as follows:  - AREF/AIN[1] PA03 AREF  - DAC0/AIN[0] PA02 A0 D15  - AIN[10] PB02 A1 D16  - AIN[11] PB03 A2 D17  - AIN[4] PA04 A3 D18~  - AIN[5] PA05 A4 D19~  - AIN[6] PA06 A5 D20  - AIN[7] PA07 A6 D21  - PA22 D0~  - PA23 D1~  - PA10 D2~  - PA11 D3~  - PB10 D4~  - PB11 D5~  : figure::>

<a id='eb0af77d-b20b-41b6-a402-a79000484ab4'></a>

Getting Started

Connecting the debugger

<::- Black square: Ground
- Red square: Power
- Teal square: LED
- Gray square: Internal Pin
- Brown square: SWD Pin
: legend::>

This is the pinout for connecting to the target device:

<::visual content::>

<a id='1e005d43-ce50-4a71-b7b6-6f7696777f97'></a>

<::Digital Pin: [Orange filled square]
Analog Pin: [Orange outlined square]
Other Pin: [White outlined square]
Microcontroller's Port: [Solid orange square]
Default: [Solid yellow square]
: legend::>

<a id='7c435dd0-5ef5-4221-90fe-de48db870305'></a>

! MAXIMUM current per pin is 7mA
! MAXIMUM source current is 46mA
! MAXIMUM sink current is 65mA per pin group

<a id='c280a8da-ad0f-43a9-805e-35e524ebced0'></a>

VIN Input voltage to the board.

NOTE: CIPO/COPI have previously
been referred to as MISO/MOSI

<a id='05bc351f-b00d-4e4b-933b-f6dae07ec7dd'></a>

<::logo: Creative Commons
CC BY SA
The logo features two interlocking 'C's, a human figure, and a circular arrow, all within rectangular and circular shapes, in a monochromatic grey scale::>

<!-- PAGE BREAK -->

<a id='d95daeda-e4a4-4db6-9a8d-262f72964369'></a>

<::logo: Arduino
ARDUINO
It features an infinity symbol with a minus sign on the left and a plus sign on the right, all in a light gray color.::>

<a id='b5c323fd-ef60-4b59-88f0-138f128706cb'></a>

ARDUINO
MKR WIFI 1010
STORE.ARDUINO.CC/MKR-WIFI-1010

<a id='3b9e092c-89a4-4f5f-a90a-205589b2b06c'></a>

<::pinout diagram: The diagram illustrates the pinout of a microcontroller board, showing connections for a Li-Po 3.7 V battery, power indicators, and various digital and analog pins with their multiple functions. A Li-Po 3.7 V battery is connected to the board's power input, which also has a "Battery Charger LED" and "Power" indicator. The board itself features a "LED_BUILTIN" indicator. The pins are labeled with their primary functions and alternative uses, grouped by type of interface. On the left side, from top to bottom, the pins are: AREF/AIN[1], PA03, AREF; DAC0/AIN[0], PA02, A0, D15; AIN[10], PB02, A1, D16; AIN[11], PB03, A2, D17; AIN[4], PA04, A3, D18~; AIN[5], PA05, A4, D19~; AIN[6], PA06, A5, D20; AIN[7], PA07, A6, D21; PA22, D0~; PA23, D1~; PA10, D2~; PA11, D3~; PB10, D4~; PB11, D5~. On the right side, from top to bottom, the pins are: GND; PA08, SDA, AIN[16], I2S_SD1; PA09, SCL, AIN[17], I2S_MCK[0]; PA21, WK; +5V; VIN; +3V3; GND; RESET; D14, PB22, TX (SC5); D13, PB23, RX (SC5); ~D12, PA09, SCL (SC2), AIN[17], I2S_MCK[0]; D11, PA08, SDA (SC2), AIN[16], I2S_SD1; ~D10, PA19, CIPO (SC1); D9, PA17, SCK (SC1); ~D8, PA16, COPI (SC1); ~D7, PA21; ~D6, PA20. Functional blocks are shown alongside the pin labels: Left-side blocks: INT[3]; INT[2]; SC5 P0A, INT[2], TC6/WO[0]; SC5 P1A, INT[3], TC6/WO[1]; SC0 P0A, INT[4], TCC0/WO[0]; SC0 P1A, INT[5], TCC0/WO[1]; SC0 P2A, INT[6], TCC1/WO[0]; SC0 P3A, INT[7], TCC1/WO[1]; I2S_SD0, AIN[7]; SC3 P0/SC5 P0A, INT[6], TC4/WO[0], TCC0/WO[4]; SC3 P1/SC5 P1A, INT[7], TC4/WO[1], TCC0/WO[5]; SC0 P2/SC2 P2A, INT[10], TCC1/WO[0], TCC0/WO[2], I2S_SCK[0], AIN[18]; SC0 P3/SC2 P3A, INT[11], TCC1/WO[1], TCC0/WO[3], I2S_FS[0], AIN[19]; SC4 P2A, INT[10], TC5/WO[0], TCC0/WO[4]; INT[11], TC5/WO[1], TC5/WO[1]. Right-side blocks: I2C; TCC0/WO[0], TCC1/WO[2], NMI, SC0 P0/SC2 P0A; TCC0/WO[0], TCC1/WO[3], INT[9], SC0 P1/SC2 P1A; TC7/WO[1], TCC0/WO[7], INT[5], SC5 P3/SC3 P3A; UART; TC7/WO[0], INT[6], SC5 P2A; TC7/WO[1], INT[7], SC5 P3A; I2C; SPI; TCC0/WO[0], TCC1/WO[3], INT[9], SC0 P1/SC2 P1A; TCC0/WO[0], TCC1/WO[2], NMI, SC0 P0/SC2 P0A; TC3/WO[1], TCC0/WO[3], INT[3], SC1 P3/SC3 P3A; TCC2/WO[1], TCC0/WO[7], INT[1], SC1 P1/SC3 P1A; TCC2/WO[0], TCC0/WO[6], INT[0], SC1 P0/SC3 P0A; TC7/WO[1], TCC0/WO[7], INT[5], SC5 P3/SC3 P3A; TC7/WO[0], TCC0/WO[6], INT[4], SC5 P2/SC3 P2A.::>

<a id='2dd72a35-b44a-4b3a-b4ea-1690abbd4d89'></a>

<::Legend for pin types and current ratings:
Ground
Power
LED
Internal Pin
SWD Pin
Digital Pin
option Analog Pin: [ ]
option Other Pin: [ ]
Microcontroller's Port
Default
Analog
Communication
Timer
Interrupt
option Sercom: [ ]
MAXIMUM current
per pin is 7mA
MAXIMUM source
current is 46mA
MAXIMUM sink current
is 65mA per pin group
: legend::>

<a id='50e1a86e-2300-43c7-8c46-56ffe2cdf364'></a>

VIN Input voltage to the board.

NOTE: CIPO/COPI have previously been referred to as MISO/MOSI

<a id='c0a34b15-062a-4322-b1e8-b1ebcac7e206'></a>

<::logo: Creative Commons
CC BY SA
A gray rectangular logo with three circular icons representing Creative Commons licenses, featuring the letters "CC" and "BY SA" below.::>

<!-- PAGE BREAK -->

<a id='bdfb63bb-aafe-4d21-bb8b-8efc0ca84158'></a>

ARDUINO
MKR WIFI 1010
STORE.ARDUINO.CC/MKR-WIFI-1010

<a id='1b217804-b067-40d9-ae33-562eebd2c4ad'></a>

<::logo: Arduino
ARDUINO
A grey infinity symbol with a minus sign on the left loop and a plus sign on the right loop, with the word ARDUINO below it.::>

<a id='0a604b9c-105c-4a3f-ac78-c0b1ba6d96a4'></a>

e, VBUS works as output ed from the LiPo battery +5V VBUS PA24 USB N PA25 USB P PA18 USB ID GND BOTTOM BQ24195L NMI TC0/WO[0] PA08 PMIC_SDA INT[9] TC0/WO[0] PA09 PMIC_SCL PA18 PMIC_OTG VBATT PMIC_BAT S2B-PH-SM4-TB(LF) (SN) SM05B-SRSS-TB <::A detailed diagram of a circuit board. On the left side, various input/output pins and components are labeled and connected to the board. On the board, a central chip is labeled 'SAMD21'. The right side shows a bottom view of the board with a pin header. The pin header has 6 pins, with labels and corresponding functions.::>
1 +3V3
2 SWDIO PA31 TCC1/WO[1] INT[11]
3 
4 SWCLK PA30 TCC1/WO[0] INT[10]
5 GND
6 
INT[9] TC4/WO[1] PB09 ADC_VBAT NINA W102 INT[12] TCC2/WO[0] PA12 36-GPIO12/NINA_COPI INT[13] TCC2/WO[1] PA13 1-SPIV_DI/NINA_CIPO INT[14] TC3/WO[0] PA14 28-SPIV_CS/NINA_CS INT[15] TC3/WO[1] PA15 29-SPIV_CLK/NINA_SCK INT[15] PA27 27-GPIO0/NINA_GPIO0 INT[8] TC4/WO[0] PB08 19-RESET/NINA_RESET INT[8] PA28 7-GPIO_33/NINA_ACK INT[14] TC3/WO[0] PA14 21-UART_CTS/NINA_CS INT[15] TC3/WO[1] PA15 20-UART_CTS/NINA_SCK INT[7] TC7/WO[1] PB23 22-UART_RXD/Serial1_RX INT[6] TC7/WO[0] PB22 23-UART_TXD/Serial1_TX ECC508 NMI TC0/WO[0] PA08 SDA INT[9] TC0/WO[0] PA09 SCL

<a id='0ee57f2d-0b31-4d71-88a8-75ef706c53d2'></a>

VIN Input voltage to the board.

<a id='9ff97e33-3e94-423c-87da-593ecdd71bb4'></a>

VIN Input voltage to the board.

<a id='d082e696-816b-4388-b38d-4cb1b229dfa1'></a>

<::logo: ARDUINO.CC
ARDUINO.CC
Last update: 7/08/2020
CC BY SA
The logo features a stylized "CC" within a circle, alongside a human figure icon and a refresh icon, all in shades of gray.::>

<a id='9c89af49-4182-4c1b-ba03-ed1e639ec5f9'></a>

This work is licensed under the Creative Commons
Attribution-ShareAlike 4.0 International License. To view
a copy of this license, visit http://creativecommons.
org/licenses/by-sa/4.0/ or send a letter to Creative
Commons, PO Box 1866, Mountain View, CA 94042, USA.

<a id='83ec85f8-f17b-4e06-8315-ced7a94ae0cb'></a>

<::Legend:
- Black square: Ground
- Red square: Power
- Teal square: LED
- Gray square: Internal Pin
- Brown square: SWD Pin
: legend::>

<a id='8dcef44c-2c10-45e1-b70d-33e819a7b4f8'></a>

<::Legend:
- Orange square with diagonal lines: Digital Pin
- Orange outlined square with diagonal lines: Analog Pin
- Orange outlined square: Other Pin
- Solid orange square: Microcontroller's Port
- Solid yellow square: Default
- Solid dark teal square: Analog
- Dark teal square with diagonal lines: Communication
- Solid teal square: Timer
- Solid light teal square: Interrupt
- Light teal outlined square: Sercom
: legend::>

<a id='cc5687c1-824d-4d40-ad0b-4c25e6c580c2'></a>

When in USB OTG mod and 5V is generat

<a id='8b427c0e-37e9-412d-9e4e-ff36d7e65d0d'></a>

! MAXIMUM current per pin is 7mA
! MAXIMUM source current is 46mA
! MAXIMUM sink current is 65mA per pin group