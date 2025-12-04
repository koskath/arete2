<a id='12e5bfb4-bb54-4435-8e05-ce126b38e0c4'></a>

<::logo: Arduino
ARDUINO
Two interlocking infinity symbols, one with a minus sign and the other with a plus sign, form the main graphic element.:>

<a id='cb780777-5556-4ca7-bf54-98662add7ae7'></a>

ARDUINO
MKR FOX 1200
STORE.ARDUINO.CC/MKR-FOX-1200

<a id='f972244f-99ae-4f49-9a19-8a4cf54ae64d'></a>

<::An illustration of a circuit board (likely an Arduino-compatible microcontroller) connected to a battery pack.The battery pack consists of two AA batteries, with a red wire (positive) and a black wire (negative) connecting to the circuit board's power input pins.The circuit board is blue and rectangular, featuring various electronic components, including integrated circuits, resistors, and capacitors. A USB port is visible at the top.A green LED labeled "Power" is located at the top of the board, and a yellow LED labeled "LED_BUILTIN" is on the right side.The pins on the left side of the board are labeled as follows (from top to bottom):AREF/AIN[1] PA03 AREFDAC0/AIN[0] PA02 A0 D15AIN[10] PB02 A1 D16AIN[11] PB03 A2 D17AIN[4] PA04 A3 D18~AIN[5] PA05 A4 D19~AIN[6] PA06 A5 D20AIN[7] PA07 A6 D21PA22 D0~PA23 D1~PA10 D2~PA11 D3~PB10 D4~PB11 D5~The pins on the right side of the board are labeled as follows (from top to bottom, below LED_BUILTIN):+5VVIN+3V3GNDRESETD14 PB22 TX (SC5)D13 PB23 RX (SC5)~D12 PA09 SCL (SC2)D11 PA08 SDA (SC2)~D10 PA19 CIPO (SC1)D9 PA17 SCK (SC1)~D8 PA16 COPI (SC1)~D7 PA21~D6 PA20: circuit diagram::>

<a id='b9113c3e-a2d8-498c-acdf-e557ce8044ec'></a>

<::Legend:
- Black square: Ground
- Red square: Power
- Teal square: LED
- Gray square: Internal Pin
- Brown square: SWD Pin
- Orange square with diagonal lines: Digital Pin
- Orange outlined square: Analog Pin
- White outlined square: Other Pin
- Solid orange square: Microcontroller's Port
- Yellow square: Default: legend::>

<a id='9121e150-c3f4-48b3-9354-1715846b22f8'></a>

! **MAXIMUM** current per pin is 7mA

! **MAXIMUM** source current is 46mA

! **MAXIMUM** sink current is 65mA per pin group

<a id='7ab777fa-feea-400c-b687-66ed9666fc47'></a>

**VIN** Input voltage to the board.

NOTE: CIPO/COPI have previously
been referred to as MISO/MOSI

<a id='1f852416-60ba-4054-93f4-f0193a24cf4f'></a>

<::logo: ARDUINO.CC
ARDUINO.CC
Last update: 23/03/2020
This logo features the text "ARDUINO.CC" and "Last update: 23/03/2020", along with Creative Commons symbols (CC, BY, SA) in a rectangular box.::>

<!-- PAGE BREAK -->

<a id='4d315896-e5cc-45d7-8786-87452572f086'></a>

<::logo: Arduino
ARDUINO
A gray infinity symbol with a minus sign on the left and a plus sign on the right sits above the company name.::>

<a id='f10543d1-111a-49dc-a68a-1e7e76f3209c'></a>

ARDUINO
MKR FOX 1200
STORE.ARDUINO.CC/MKR-FOX-1200

<a id='98b8db94-b604-4cae-a25b-955f78473240'></a>

<::Arduino Pinout Diagram:figure::>
## Power Input
- Two AA batteries connected to the board.
- Power input labeled 'Power'.

## Power Pins
- +5V
- VIN
- +3V3
- GND
- RESET
- LED_BUILTIN

## Left Side Pins (Digital/Analog)
- INT[3]
- INT[2]
- SC5 P0A: INT[2], TC6/WO[0]
- SC5 P1A: INT[3], TC6/WO[1]
- SC0 P0A: INT[4], TCC0/WO[0]
- SC0 P1A: INT[5], TCC0/WO[1]
- SC0 P2A: INT[6], TCC1/WO[0]
- SC0 P3A: INT[7], TCC1/WO[1], I2S_SD0
- SC3 P0/SC5 P0A: INT[6], TC4/WO[0], TCC0/WO[4]
- SC3 P1/SC5 P1A: INT[7], TC4/WO[1], TCC0/WO[5]
- SC0 P2/SC2 P2A: INT[10], TCC1/WO[0], TCC0/WO[2], I2S_SCK[0]
- SC0 P3/SC2 P3A: INT[11], TCC1/WO[1], TCC0/WO[3], I2S_FS[0]
- SC4 P2A: INT[10], TC5/WO[0], TCC0/WO[4]
- INT[11], TC5/WO[1], TC5/WO[1]

## Middle Left Pins (Analog/Digital)
- AREF/AIN[1]: AREF/AIN[1], PA03, AREF
- DAC0/AIN[0]: DAC0/AIN[0], PA02, A0, D15
- AIN[10]: AIN[10], PB02, A1, D16
- AIN[11]: AIN[11], PB03, A2, D17
- AIN[4]: AIN[4], PA04, A3, D18~
- AIN[5]: AIN[5], PA05, A4, D19~
- AIN[6]: AIN[6], PA06, A5, D20
- AIN[7]: AIN[7], PA07, A6, D21
- PA22: D0~
- PA23: D1~
- AIN[18]: PA10, D2~
- AIN[19]: PA11, D3~
- PB10: D4~
- PB11: D5~

## Right Side Pins (Digital/Communication)
- D14: PB22, TX (SC5) (UART)
  - TC7/WO[0], INT[6], SC5 P2A
- D13: PB23, RX (SC5) (UART)
  - TC7/WO[1], INT[7], SC5 P3A
- ~D12: PA09, SCL (SC2) (I2C), AIN[17], I2S_MCK[0]
  - TCC0/WO[0], TCC1/WO[3], INT[9], SC0 P1/SC2 P1A
- D11: PA08, SDA (SC2) (I2C), AIN[16], I2S_SD1
  - TCC0/WO[0], TCC1/WO[2], NMI, SC0 P0/SC2 P0A
- ~D10: PA19, CIPO (SC1) (SPI)
  - TC3/WO[1], TCC0/WO[3], INT[3], SC1 P3/SC3 P3A
- D9: PA17, SCK (SC1) (SPI)
  - TCC2/WO[1], TCC0/WO[7], INT[1], SC1 P1/SC3 P1A
- ~D8: PA16, COPI (SC1) (SPI)
  - TCC2/WO[0], TCC0/WO[6], INT[0], SC1 P0/SC3 P0A
- ~D7: PA21
  - TC7/WO[1], TCC0/WO[7], INT[5], SC5 P3/SC3 P3A
- ~D6: PA20
  - TC7/WO[0], TCC0/WO[6], INT[4], SC5 P2/SC3 P2A

<a id='a3405939-51d1-45be-bb12-38a51ba96665'></a>

<::Legend:
- Black solid square: Ground
- Red solid square: Power
- Teal solid square: LED
- Grey solid square: Internal Pin
- Brown solid square: SWD Pin
- Orange striped square: Digital Pin
- Orange hollow square: Analog Pin
- White hollow square: Other Pin
- Yellow-orange solid square: Microcontroller's Port
- Yellow solid square: Default
- Dark teal solid square: Analog
- Dark teal striped square: Communication
- Teal solid square: Timer
- Light blue solid square: Interrupt
- White hollow square: Sercom

Warnings:
- Red exclamation mark icon: MAXIMUM current per pin is 7mA
- Red exclamation mark icon: MAXIMUM source current is 46mA
- Red exclamation mark icon: MAXIMUM sink current is 65mA per pin group
: legend::>

<a id='00bf3a01-cbca-4ce1-8236-e1385afe9c00'></a>

VIN Input voltage to the board.

NOTE: CIPO/COPI have previously
been referred to as MISO/MOSI

<a id='12c731f3-6e4d-4953-bfb2-ec17464a486a'></a>

<::logo: Creative Commons
CC BY SA
Three gray circles with white icons, including a double 'c', a person, and a circular arrow, are arranged horizontally above the letters 'BY' and 'SA' in a rounded rectangle.::>

<!-- PAGE BREAK -->

<a id='c0e70c6a-802f-4a08-9866-6ab216785404'></a>

<::logo: Arduino
ARDUINO
It features an infinity symbol with a minus sign on the left and a plus sign on the right, all in a light gray color.::>

<a id='3a5f5788-8ca9-4b53-ae81-65d27c261332'></a>

ARDUINO
MKR FOX 1200
STORE.ARDUINO.CC/MKR-FOX-1200

<a id='2e0043d7-3a71-4e3a-969c-c93461a9d828'></a>

<::A technical diagram illustrating the pinout and connections for a microcontroller board. The diagram is split into two main sections: a top view of the board on the left and a bottom view on the right. The top view shows a light blue circuit board with various components, including a chip labeled "SAMD21". On the top edge, a set of pins are connected to external labels: +5V (red wire), USB N (white wire) connected to PA24, USB P (green wire) connected to PA25, USB ID (black wire) connected to PA18, and GND (black wire). These pins are also associated with functions such as SC3 P2/SC5 P2A INT[12] TC5/WO[0], SC3 P3/SC5 P3A INT[13] TC5/WO[1], and SC1 P2/SC3 P2A INT[2] TC3/WO[0]. On the bottom left side of the top view, another set of pins is connected to labels: SC2 P0/SC4 P0A INT[12] TCC2/WO[0] connected to PA12 COPI, SC2 P1/SC4 P1A INT[13] TCC2/WO[1] connected to PA13 SCK, SC2 P2/SC4 P2A INT[14] TC3/WO[0] connected to PA14 SSN/NSS, SC2 P3/SC4 P3A INT[15] TC3/WO[1] connected to PA15 CIPO, INT[15] connected to PA27 PC0/RESET, INT[8] connected to PA28 PB4/PWR_ON, and SC4 P1A INT[9] TC4/WO[1] AIN[3] connected to PB09 PB6/EVENT. The label "ATAB8520E" is visible near these pins. The right section shows the "BOTTOM" view of the board, which is dark blue. On the right side of the bottom view, a series of numbered pins (1 to 6) are shown. Pin 1 is connected to +3V3 (red wire). Pin 2 is connected to SWDIO, which leads to PA31 TCC1/WO[1] INT[11] (orange wire). Pin 4 is connected to SWCLK, which leads to PA30 TCC1/WO[0] INT[10] (black wire). Pin 5 is connected to GND (brown wire). Small numbered squares (6, 5, 4, 3, 2, 1) are also visible on the bottom view of the board.: diagram::>

<a id='fc4c3e39-a81e-4fd6-9379-4998c68ff6cb'></a>

<::Legend:
- Black square: Ground
- Red square: Power
- Teal square: LED
- Gray square: Internal Pin
- Brown square: SWD Pin
: legend::>

<a id='e918e1a3-ad5a-418f-8074-d6f20620a0bb'></a>

<::Legend:
- Orange solid square with diagonal lines: Digital Pin
- Orange outlined square: Analog Pin
- White outlined square: Other Pin
- Orange solid square: Microcontroller's Port
- Yellow solid square: Default
- Dark teal solid square: Analog
- Dark teal solid square with diagonal lines: Communication
- Teal solid square: Timer
- Light blue solid square: Interrupt
- Light blue outlined square: Sercom
: legend::>

<a id='839b30cd-4468-4ab5-beaf-585290daae74'></a>

! MAXIMUM current per pin is 7mA

! MAXIMUM source current is 46mA

! MAXIMUM sink current is 65mA per pin group

<a id='c8bf28a5-d7f2-4541-bba5-11868d24e3c1'></a>

VIN Input voltage to the board.

NOTE: CIPO/COPI have previously been referred to as MISO/MOSI

<a id='0613b000-4223-406e-a5a8-9769737c0ac9'></a>

<::logo: Creative Commons
CC BY SA
The logo features three circles, two of which contain 'CC' and an icon of a person, and the third containing an arrow forming a circle.::>