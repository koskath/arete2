<a id='35ae14e4-b1e9-4819-8328-576ffede1d65'></a>

<::logo: Analog Devices
ANALOG DEVICES
A black square with a white play symbol to the left of the company name.::>

<a id='5593fc71-db36-4a04-bd21-744d7cbcfade'></a>

Mixed-Signal Front-End (MxFE™) Processor
for Broadband Communications

<a id='c75f2f96-1355-43a7-998c-683b62c1c83d'></a>

AD9860/AD9862*

<a id='e27324dd-7066-4663-a3e4-8e0671f08a9f'></a>

## FEATURES

Mixed-Signal Front-End Processor with Dual Converter Receive and Dual Converter Transmit Signal Paths

**Receive Signal Path Includes:**
*   Two 10-/12-Bit, 64 MSPS Sampling A/D Converters with Internal or External Independent References,
*   Input Buffers, Programmable Gain Amplifiers,
*   Low-Pass Decimation Filters, and a Digital Hilbert Filter

**Transmit Signal Path Includes:**
*   Two 12-/14-Bit, 128 MSPS D/A Converters with
*   Programmable Full-Scale Output Current, Channel
*   Independent Fine Gain and Offset Control, Digital
*   Hilbert and Interpolation Filters, and Digitally Tunable
*   Real or Complex Up-Converters

Delay-Locked Loop Clock Multiplier and Integrated Timing Generation Circuitry Allow for Single Crystal or Clock Operation

Programmable Output Clocks, Serial Programmable Interface, Programmable Sigma-Delta, Three Auxiliary DAC Outputs and Two Auxiliary ADCs with Dual Multiplexed Inputs

<a id='8451eb28-d64d-49ec-8798-c283c8e0b739'></a>

## **APPLICATIONS**

**Broadband Wireless Systems**
*   Fixed Wireless, WLAN, MMDS, LMDS

**Broadband Wireline Systems**
*   Cable Modems, VDSL, PowerPlug

**Digital Communications**
*   Set-Top Boxes, Data Modems

<a id='1325ccd9-dc53-41fe-94c0-983e7fd17312'></a>

**GENERAL DESCRIPTION**
The AD9860 and AD9862 (AD9860/AD9862) are versatile
integrated mixed-signal front-ends (MxFE) that are optimized
for broadband communication markets. The AD9860/AD9862
are cost effective, mixed signal solutions for wireless or wireline
standards based or proprietary broadband modem systems where
dynamic performance, power dissipation, cost, and size are all
critical attributes. The AD9860 has 10-bit ADCs and 12-bit DACs;
the AD9862 has 12-bit ADCs and 14-bit DACs.

<a id='19a92872-9ad3-49ea-9087-6ee3f072367f'></a>

The AD9860/AD9862 receive path (Rx) consists of two channels
that each include a high performance, 10-/12-bit, 64 MSPS analog-
to-digital converter (ADC), input buffer, Programmable Gain
Amplifier (RxPGA), digital Hilbert filter, and decimation filter. The
Rx can be used to receive real, diversity, or I/Q data at baseband or
low IF. The input buffers provide a constant input impedance for
both channels to ease impedance matching with external com-
ponents (e.g., SAW filter). The RxPGA provides a 20 dB gain

<a id='5edc5d1c-8c08-4bfb-b594-77fc638d8a49'></a>

*Protected by U.S.Patent No. 5,969,657.MxFE is a trademark of Analog Devices, Inc.

<a id='e64f8368-4a3b-4194-b168-700eb082b43f'></a>

REV. 0

<a id='8aa11499-7696-4398-bd04-4ba4efcfa46e'></a>

Information furnished by Analog Devices is believed to be accurate and reliable. However, no responsibility is assumed by Analog Devices for its use, nor for any infringements of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of Analog Devices.

<a id='0d23c9ca-8fd4-4b73-b37d-874c025d3026'></a>

FUNCTIONAL BLOCK DIAGRAM

<::Functional Block Diagram: AD9860/AD9862

Inputs (Left Side):
VIN+A, VIN-A connect to a 1x gain block, then PGA, then ADC, which feeds into a BYPASSABLE LOW-PASS DECIMATION FILTER. This filter connects to a HILBERT FILTER, which then feeds a multiplexer for RxA DATA [0:11].
VIN+B, VIN-B connect to a 1x gain block, then PGA, then ADC, which feeds into a multiplexer for RxB DATA [0:11]. This multiplexer also receives a LOGIC LOW input.
SIGDELT connects to a Σ-Δ block.
AUX_DAC_A, AUX_DAC_B, AUX_DAC_C each connect to an AUX DAC block.
AUX_ADC_A1, AUX_ADC_A2 connect to an AUX ADC block.
AUX_ADC_B1, AUX_ADC_B2 connect to another AUX ADC block.
IOUT+A, IOUT-A connect to a PGA, then a DAC, which feeds into a BYPASSABLE DIGITAL QUADRATURE MIXER. This mixer also receives input from a BYPASSABLE LOW-PASS INTERPOLATION FILTER (with FS/4, FS/8 options).
IOUT+B, IOUT-B connect to a PGA, then a DAC, which feeds into another BYPASSABLE DIGITAL QUADRATURE MIXER. This mixer also receives input from the BYPASSABLE LOW-PASS INTERPOLATION FILTER and an NCO.

Central Blocks:
SPI REGISTERS connect to an SPI INTERFACE.
Rx PATH TIMING and Tx PATH TIMING feed into a CLOCK DISTRIBUTION BLOCK. This block connects to a DLL (1x, 2x, 4x), which outputs to OSC1 and OSC2. The CLOCK DISTRIBUTION BLOCK also outputs CLKOUT1 and CLKOUT2.

Outputs (Right Side):
RxA DATA [0:11] is output from a multiplexer fed by the HILBERT FILTER.
RxB DATA [0:11] is output from a multiplexer fed by the ADC path and LOGIC LOW.
SPI INTERFACE is connected to SPI REGISTERS.
OSC1, OSC2 are outputs from the DLL.
CLKOUT1, CLKOUT2 are outputs from the CLOCK DISTRIBUTION BLOCK.
Tx DATA [0:13] is output from a multiplexer, which is fed by a HILBERT FILTER. This HILBERT FILTER is fed by the two BYPASSABLE DIGITAL QUADRATURE MIXERS.::>

<a id='0cbffbc4-ceae-43a4-ad00-62990c9df5aa'></a>

range for both channels. The output data bus can be multi-
plexed to accommodate a variety of interface types.

<a id='1bace24c-885f-4263-8bca-89c1c73ed8dc'></a>

The AD9860/AD9862 transmit path (Tx) consists of two chan-
nels that contain high performance, 12-/14-bit, 128 MSPS
digital-to-analog converters (DAC), programmable gain amplifiers
(TxPGA), interpolation filters, a Hilbert filter, and digital mixers
for complex or real signal frequency modulation. The Tx latch
and demultiplexer circuitry can process real or I/Q data. Interpo-
lation rates of 2× and 4× are available to ease requirements on
an external reconstruction filter. For single channel systems, the
digital Hilbert filter can be used with an external quadrature
modulator to create an image rejection architecture. The two
12-/14-bit, high performance DACs produce an output signal
that can be scaled over a 20 dB range by the TxPGA.

<a id='f9a6b0cd-ae5a-4f16-88d0-ab452fef940d'></a>

A programmable delay-locked loop (DLL) clock multiplier and integrated timing circuits enable the use of a single external reference clock or an external crystal to generate clocking for all internal blocks and also provides two external clock outputs. Additional features include a programmable sigma-delta output, four auxiliary ADC inputs and three auxiliary DAC outputs. Device programmability is facilitated by a serial port interface (SPI) combined with a register bank. The AD9860/AD9862 is available in a space saving 128-lead LQFP.

<a id='48444cae-9227-4565-93d9-aa11783d4b70'></a>

One Technology Way, P.O. Box 9106, Norwood, MA 02062-9106, U.S.A.
Tel: 781/329-4700
Fax: 781/326-8703
www.analog.com
© Analog Devices, Inc., 2002

<!-- PAGE BREAK -->

<a id='fa53308d-f62a-48d4-a78e-e8a6eaee07fe'></a>

AD9860/AD9862—SPECIFICATIONS (Vₐ = 3.3 V ± 5%, Vᴅ = 3.3 V ± 10%, fᴅᴀᴄ = 128 MHz, fᴀᴅᴄ = 64 MHz
Normal Timing Mode, 2× DLL Setting, Rₛₑₜ = 4 kΩ, 50 Ω DAC Load,
RxPGA = +6 dB Gain, TxPGA = +20 dB Gain.)

<a id='e71521f4-55dd-4c1e-a95f-b08ef7fe1c8e'></a>

<table id="1-1">
<tr><td id="1-2">Tx PARAMETERS</td><td id="1-3">Temp</td><td id="1-4">Test Level</td><td id="1-5">Min</td><td id="1-6">AD9860/AD9862 Typ</td><td id="1-7">Max</td><td id="1-8">Unit</td></tr>
<tr><td id="1-9">12-/14-BIT DAC CHARACTERISTICS</td><td id="1-a"></td><td id="1-b"></td><td id="1-c"></td><td id="1-d"></td><td id="1-e"></td><td id="1-f"></td></tr>
<tr><td id="1-g">Resolution</td><td id="1-h">NA</td><td id="1-i">NA</td><td id="1-j"></td><td id="1-k">12/14</td><td id="1-l"></td><td id="1-m">Bits</td></tr>
<tr><td id="1-n">Maximum Update Rate</td><td id="1-o"></td><td id="1-p"></td><td id="1-q">128</td><td id="1-r"></td><td id="1-s"></td><td id="1-t">MSPS</td></tr>
<tr><td id="1-u">Full-Scale Output Current</td><td id="1-v">Full</td><td id="1-w">I</td><td id="1-x">2</td><td id="1-y"></td><td id="1-z">20</td><td id="1-A">mA</td></tr>
<tr><td id="1-B">Gain Error (Using Internal Reference)</td><td id="1-C">25°C</td><td id="1-D">I</td><td id="1-E">-5.5</td><td id="1-F">+0.5</td><td id="1-G">+5.5</td><td id="1-H">%FS</td></tr>
<tr><td id="1-I">Offset Error</td><td id="1-J">25°C</td><td id="1-K">I</td><td id="1-L">-1</td><td id="1-M">0.0</td><td id="1-N">+1</td><td id="1-O">%FS</td></tr>
<tr><td id="1-P">Reference Voltage (REFIO Level)</td><td id="1-Q">25°C</td><td id="1-R">I</td><td id="1-S">1.15</td><td id="1-T">1.22</td><td id="1-U">1.28</td><td id="1-V">V</td></tr>
<tr><td id="1-W">Negative Differential Nonlinearity (-DNL)</td><td id="1-X">25°C</td><td id="1-Y">III</td><td id="1-Z"></td><td id="1-10">-0.5/-0.5</td><td id="1-11"></td><td id="1-12">LSB</td></tr>
<tr><td id="1-13">Positive Differential Nonlinearity (+DNL)</td><td id="1-14">25°C</td><td id="1-15">III</td><td id="1-16"></td><td id="1-17">1/2</td><td id="1-18"></td><td id="1-19">LSB</td></tr>
<tr><td id="1-1a">Integral Nonlinearity (INL)</td><td id="1-1b">25°C</td><td id="1-1c">III</td><td id="1-1d"></td><td id="1-1e">±1/±3</td><td id="1-1f"></td><td id="1-1g">LSB</td></tr>
<tr><td id="1-1h">Output Capacitance</td><td id="1-1i">25°C</td><td id="1-1j">III</td><td id="1-1k"></td><td id="1-1l">5</td><td id="1-1m"></td><td id="1-1n">pF</td></tr>
<tr><td id="1-1o">Phase Noise @ 1 kHz Offset, 6 MHz Tone Crystal and OSC IN Multiplier Enabled at 4×</td><td id="1-1p">25°C</td><td id="1-1q">III</td><td id="1-1r"></td><td id="1-1s">-115</td><td id="1-1t"></td><td id="1-1u">dBc/Hz</td></tr>
<tr><td id="1-1v">Output Voltage Compliance Range</td><td id="1-1w">Full</td><td id="1-1x">II</td><td id="1-1y">-0.5</td><td id="1-1z"></td><td id="1-1A">+1.5</td><td id="1-1B">V</td></tr>
<tr><td id="1-1C">TRANSMIT TxPGA CHARACTERISTICS</td><td id="1-1D"></td><td id="1-1E"></td><td id="1-1F"></td><td id="1-1G"></td><td id="1-1H"></td><td id="1-1I"></td></tr>
<tr><td id="1-1J">Gain Range</td><td id="1-1K">25°C</td><td id="1-1L">III</td><td id="1-1M"></td><td id="1-1N">20</td><td id="1-1O"></td><td id="1-1P">dB</td></tr>
<tr><td id="1-1Q">Step Size Accuracy</td><td id="1-1R">25°C</td><td id="1-1S">III</td><td id="1-1T"></td><td id="1-1U">±0.1</td><td id="1-1V"></td><td id="1-1W">dB</td></tr>
<tr><td id="1-1X">Step Size</td><td id="1-1Y">25°C</td><td id="1-1Z">III</td><td id="1-20"></td><td id="1-21">0.08</td><td id="1-22"></td><td id="1-23">dB</td></tr>
<tr><td id="1-24">Tx DIGITAL FILTER CHARACTERISTICS</td><td id="1-25"></td><td id="1-26"></td><td id="1-27"></td><td id="1-28"></td><td id="1-29"></td><td id="1-2a"></td></tr>
<tr><td id="1-2b">Hilbert Filter Pass Band (&lt;0.1 dB Ripple)</td><td id="1-2c">Full</td><td id="1-2d">II</td><td id="1-2e">12.5</td><td id="1-2f"></td><td id="1-2g">38</td><td id="1-2h">% fDATA¹</td></tr>
<tr><td id="1-2i">2×/4× Interpolator Stop Band²</td><td id="1-2j">Full</td><td id="1-2k">II</td><td id="1-2l"></td><td id="1-2m"></td><td id="1-2n">±38</td><td id="1-2o">% fDATA</td></tr>
<tr><td id="1-2p">DYNAMIC PERFORMANCE (AOUT = 20 mA FS, f = 1 MHz)</td><td id="1-2q"></td><td id="1-2r"></td><td id="1-2s"></td><td id="1-2t"></td><td id="1-2u"></td><td id="1-2v"></td></tr>
<tr><td id="1-2w">Differential Phase</td><td id="1-2x">25°C</td><td id="1-2y">III</td><td id="1-2z"></td><td id="1-2A">&lt;0.1</td><td id="1-2B"></td><td id="1-2C">Degree</td></tr>
<tr><td id="1-2D">Differential Gain</td><td id="1-2E">25°C</td><td id="1-2F">III</td><td id="1-2G"></td><td id="1-2H">&lt;1</td><td id="1-2I"></td><td id="1-2J">LSB</td></tr>
<tr><td id="1-2K">AD9860 Signal-to-Noise Ratio (SNR)</td><td id="1-2L">Full</td><td id="1-2M">I</td><td id="1-2N">68.2</td><td id="1-2O">70.7</td><td id="1-2P"></td><td id="1-2Q">dB</td></tr>
<tr><td id="1-2R">AD9860 Signal-to-Noise and Distortion Ratio</td><td id="1-2S">Full</td><td id="1-2T">I</td><td id="1-2U">62.5</td><td id="1-2V">66.1</td><td id="1-2W"></td><td id="1-2X">dB</td></tr>
<tr><td id="1-2Y">AD9860 Total Harmonic Distortion (THD)</td><td id="1-2Z">Full</td><td id="1-30">I</td><td id="1-31"></td><td id="1-32">-74.5</td><td id="1-33">-64.0</td><td id="1-34">dB</td></tr>
<tr><td id="1-35">AD9860 Wideband SFDR (to Nyquist)</td><td id="1-36"></td><td id="1-37"></td><td id="1-38"></td><td id="1-39"></td><td id="1-3a"></td><td id="1-3b"></td></tr>
<tr><td id="1-3c">1 MHz Analog Out, IOUT = 2 mA</td><td id="1-3d">25°C</td><td id="1-3e">III</td><td id="1-3f"></td><td id="1-3g">70.6</td><td id="1-3h"></td><td id="1-3i">dBc</td></tr>
<tr><td id="1-3j">1 MHz Analog Out, IOUT = 20 mA</td><td id="1-3k">25°C</td><td id="1-3l">I</td><td id="1-3m">64.4</td><td id="1-3n">75</td><td id="1-3o"></td><td id="1-3p">dBc</td></tr>
<tr><td id="1-3q">6 MHz Analog Out, IOUT = 20 mA</td><td id="1-3r">25°C</td><td id="1-3s">III</td><td id="1-3t"></td><td id="1-3u">75</td><td id="1-3v"></td><td id="1-3w">dBc</td></tr>
<tr><td id="1-3x">AD9860 Narrowband SFDR (1 MHz Window)</td><td id="1-3y"></td><td id="1-3z"></td><td id="1-3A"></td><td id="1-3B"></td><td id="1-3C"></td><td id="1-3D"></td></tr>
<tr><td id="1-3E">1 MHz Analog Out, IOUT = 2 mA</td><td id="1-3F">25°C</td><td id="1-3G">III</td><td id="1-3H"></td><td id="1-3I">70.2</td><td id="1-3J"></td><td id="1-3K">dBc</td></tr>
<tr><td id="1-3L">1 MHz Analog Out, IOUT = 20 mA</td><td id="1-3M">25°C</td><td id="1-3N">I</td><td id="1-3O">83</td><td id="1-3P">90</td><td id="1-3Q"></td><td id="1-3R">dBc</td></tr>
<tr><td id="1-3S">AD9862 Signal-to-Noise Ratio (SNR)</td><td id="1-3T">Full</td><td id="1-3U">I</td><td id="1-3V">68.9</td><td id="1-3W">72.0</td><td id="1-3X"></td><td id="1-3Y">dB</td></tr>
<tr><td id="1-3Z">AD9862 Signal-to-Noise and Distortion Ratio</td><td id="1-40">Full</td><td id="1-41">I</td><td id="1-42">64.75</td><td id="1-43">69.8</td><td id="1-44"></td><td id="1-45">dB</td></tr>
<tr><td id="1-46">AD9862 Total Harmonic Distortion (THD)</td><td id="1-47">Full</td><td id="1-48">I</td><td id="1-49"></td><td id="1-4a">-75.5</td><td id="1-4b">-65.0</td><td id="1-4c">dB</td></tr>
<tr><td id="1-4d">AD9862 Wideband SFDR (to Nyquist)</td><td id="1-4e"></td><td id="1-4f"></td><td id="1-4g"></td><td id="1-4h"></td><td id="1-4i"></td><td id="1-4j"></td></tr>
<tr><td id="1-4k">1 MHz Analog Out, IOUT = 2 mA</td><td id="1-4l">25°C</td><td id="1-4m">III</td><td id="1-4n"></td><td id="1-4o">70.6</td><td id="1-4p"></td><td id="1-4q">dBc</td></tr>
<tr><td id="1-4r">1 MHz Analog Out, IOUT = 20 mA</td><td id="1-4s">25°C</td><td id="1-4t">I</td><td id="1-4u">64.9</td><td id="1-4v">76.0</td><td id="1-4w"></td><td id="1-4x">dBc</td></tr>
<tr><td id="1-4y">6 MHz Analog Out, IOUT = 20 mA</td><td id="1-4z">25°C</td><td id="1-4A">III</td><td id="1-4B"></td><td id="1-4C">76.0</td><td id="1-4D"></td><td id="1-4E">dBc</td></tr>
<tr><td id="1-4F">AD9862 Narrowband SFDR (1 MHz Window)</td><td id="1-4G"></td><td id="1-4H"></td><td id="1-4I"></td><td id="1-4J"></td><td id="1-4K"></td><td id="1-4L"></td></tr>
<tr><td id="1-4M">1 MHz Analog Out, IOUT = 2 mA</td><td id="1-4N">25°C</td><td id="1-4O">III</td><td id="1-4P"></td><td id="1-4Q">70.2</td><td id="1-4R"></td><td id="1-4S">dBc</td></tr>
<tr><td id="1-4T">1 MHz Analog Out, IOUT = 20 mA</td><td id="1-4U">25°C</td><td id="1-4V">I</td><td id="1-4W">83</td><td id="1-4X">90</td><td id="1-4Y"></td><td id="1-4Z">dBc</td></tr>
<tr><td id="1-50" colspan="7">Rx PARAMETERS</td></tr>
<tr><td id="1-51">RECEIVE BUFFER</td><td id="1-52"></td><td id="1-53"></td><td id="1-54"></td><td id="1-55"></td><td id="1-56"></td><td id="1-57"></td></tr>
<tr><td id="1-58">Input Resistance (Differential)</td><td id="1-59">Full</td><td id="1-5a">III</td><td id="1-5b"></td><td id="1-5c">200</td><td id="1-5d"></td><td id="1-5e">Ω</td></tr>
<tr><td id="1-5f">Input Capacitance (Each Input)</td><td id="1-5g">Full</td><td id="1-5h">III</td><td id="1-5i"></td><td id="1-5j">5</td><td id="1-5k"></td><td id="1-5l">pF</td></tr>
<tr><td id="1-5m">Maximum Input Bandwidth (-3 dB)</td><td id="1-5n">Full</td><td id="1-5o">III</td><td id="1-5p"></td><td id="1-5q">140</td><td id="1-5r"></td><td id="1-5s">MHz</td></tr>
<tr><td id="1-5t">Analog Input Range (Best Noise Performance)</td><td id="1-5u">Full</td><td id="1-5v">II</td><td id="1-5w"></td><td id="1-5x">2</td><td id="1-5y"></td><td id="1-5z">V p-p Diff</td></tr>
<tr><td id="1-5A">Analog Input Range (Best THD Performance)</td><td id="1-5B">Full</td><td id="1-5C">II</td><td id="1-5D"></td><td id="1-5E">1</td><td id="1-5F"></td><td id="1-5G">V p-p Diff</td></tr>
<tr><td id="1-5H">RECEIVE PGA CHARACTERISTICS</td><td id="1-5I"></td><td id="1-5J"></td><td id="1-5K"></td><td id="1-5L"></td><td id="1-5M"></td><td id="1-5N"></td></tr>
<tr><td id="1-5O">Gain Error</td><td id="1-5P">25°C</td><td id="1-5Q">I</td><td id="1-5R"></td><td id="1-5S">±0.3</td><td id="1-5T"></td><td id="1-5U">dB</td></tr>
<tr><td id="1-5V">Gain Range</td><td id="1-5W">25°C</td><td id="1-5X">I</td><td id="1-5Y">19</td><td id="1-5Z">20</td><td id="1-60">21</td><td id="1-61">dB</td></tr>
<tr><td id="1-62">Step Size Accuracy</td><td id="1-63">25°C</td><td id="1-64">I</td><td id="1-65"></td><td id="1-66">±0.2</td><td id="1-67"></td><td id="1-68">dB</td></tr>
<tr><td id="1-69">Step Size</td><td id="1-6a">25°C</td><td id="1-6b">I</td><td id="1-6c"></td><td id="1-6d">1</td><td id="1-6e"></td><td id="1-6f">dB</td></tr>
<tr><td id="1-6g">Input Bandwidth (-3 dB, Rx Buffer Bypassed)</td><td id="1-6h">25°C</td><td id="1-6i">III</td><td id="1-6j"></td><td id="1-6k">250</td><td id="1-6l"></td><td id="1-6m">MHz</td></tr>
<tr><td id="1-6n">10-/12-BIT ADC CHARACTERISTICS</td><td id="1-6o"></td><td id="1-6p"></td><td id="1-6q"></td><td id="1-6r"></td><td id="1-6s"></td><td id="1-6t"></td></tr>
<tr><td id="1-6u">Resolution</td><td id="1-6v">NA</td><td id="1-6w">NA</td><td id="1-6x"></td><td id="1-6y">10/12</td><td id="1-6z"></td><td id="1-6A">Bits</td></tr>
<tr><td id="1-6B">Maximum Conversion Rate</td><td id="1-6C">Full</td><td id="1-6D">I</td><td id="1-6E">64</td><td id="1-6F"></td><td id="1-6G"></td><td id="1-6H">MHz</td></tr>
</table>

<a id='ead5df7f-1f91-4aab-ac5f-ac1153e26204'></a>

-2-

<a id='c847e2af-e4f8-445f-8401-2cbc7c023a36'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='6dabc337-691a-4660-9475-9e8aa02dfbf1'></a>

AD9860/AD9862

<a id='4e68c7a0-8f1a-4796-9eea-b3a665868644'></a>

<table id="2-1">
<tr><td id="2-2"></td><td id="2-3"></td><td id="2-4">Test</td><td id="2-5" colspan="2">AD9860/AD9862</td><td id="2-6"></td><td id="2-7"></td></tr>
<tr><td id="2-8">KX PARAMETERS (continued)</td><td id="2-9">Temp</td><td id="2-a">Level</td><td id="2-b">Min</td><td id="2-c">Typ</td><td id="2-d">Max</td><td id="2-e">Unit</td></tr>
<tr><td id="2-f">DC ACCURACY</td><td id="2-g"></td><td id="2-h"></td><td id="2-i"></td><td id="2-j"></td><td id="2-k"></td><td id="2-l"></td></tr>
<tr><td id="2-m">Differential Nonlinearity</td><td id="2-n">25°C</td><td id="2-o">III</td><td id="2-p"></td><td id="2-q">±0.3/±0.4</td><td id="2-r"></td><td id="2-s">LSB</td></tr>
<tr><td id="2-t">Integral Nonlinearity</td><td id="2-u">25°C</td><td id="2-v">III</td><td id="2-w"></td><td id="2-x">±1.2/±5</td><td id="2-y"></td><td id="2-z">LSB</td></tr>
<tr><td id="2-A">Offset Error</td><td id="2-B">25°C</td><td id="2-C">III</td><td id="2-D"></td><td id="2-E">±0.1</td><td id="2-F"></td><td id="2-G">%FSR</td></tr>
<tr><td id="2-H">Gain Error</td><td id="2-I">25°C</td><td id="2-J">III</td><td id="2-K"></td><td id="2-L">±0.2</td><td id="2-M"></td><td id="2-N">%FSR</td></tr>
<tr><td id="2-O">Aperture Delay</td><td id="2-P">25°C</td><td id="2-Q">III</td><td id="2-R"></td><td id="2-S">2.0</td><td id="2-T"></td><td id="2-U">ns</td></tr>
<tr><td id="2-V">Aperture Uncertainty (liter)</td><td id="2-W">25°C</td><td id="2-X">III</td><td id="2-Y"></td><td id="2-Z">1.2</td><td id="2-10"></td><td id="2-11">ps rms</td></tr>
<tr><td id="2-12">Input Referred Noise</td><td id="2-13">25°C</td><td id="2-14"></td><td id="2-15"></td><td id="2-16">250</td><td id="2-17"></td><td id="2-18">μV</td></tr>
<tr><td id="2-19">Reference Voltage Error</td><td id="2-1a"></td><td id="2-1b"></td><td id="2-1c"></td><td id="2-1d"></td><td id="2-1e"></td><td id="2-1f"></td></tr>
<tr><td id="2-1g">REFT-REFB Error (1 V)</td><td id="2-1h">25°C</td><td id="2-1i">I</td><td id="2-1j"></td><td id="2-1k">±1</td><td id="2-1l">±4</td><td id="2-1m">mV</td></tr>
<tr><td id="2-1n" colspan="2">AD9860 DYNAMIC PERFORMANCE (A = -0.5 dBFS, f = 5 MHz)</td><td id="2-1o"></td><td id="2-1p"></td><td id="2-1q"></td><td id="2-1r"></td><td id="2-1s"></td></tr>
<tr><td id="2-1t">Signal-to-Noise Ratio</td><td id="2-1u">25°C</td><td id="2-1v">I</td><td id="2-1w">59.0</td><td id="2-1x">60.66</td><td id="2-1y"></td><td id="2-1z">dBc</td></tr>
<tr><td id="2-1A">Signal-to-Noise and Distortion Ratio</td><td id="2-1B">25°C</td><td id="2-1C">I</td><td id="2-1D">56.0</td><td id="2-1E">58.0</td><td id="2-1F"></td><td id="2-1G">dBc</td></tr>
<tr><td id="2-1H">Total Harmonic Distortion</td><td id="2-1I">25°C</td><td id="2-1J">I</td><td id="2-1K"></td><td id="2-1L">-76.5</td><td id="2-1M">-70.5</td><td id="2-1N">dBc</td></tr>
<tr><td id="2-1O">Spurious Free Dynamic Range</td><td id="2-1P">25°C</td><td id="2-1Q">I</td><td id="2-1R">70.3</td><td id="2-1S">81.0</td><td id="2-1T"></td><td id="2-1U">dBc</td></tr>
<tr><td id="2-1V" colspan="2">AD9862 DYNAMIC PERFORMANCE (A_IN = -0.5 dBFS, f = 5 MHz)</td><td id="2-1W"></td><td id="2-1X"></td><td id="2-1Y"></td><td id="2-1Z"></td><td id="2-20"></td></tr>
<tr><td id="2-21">Signal-to-Noise Ratio</td><td id="2-22">25°C</td><td id="2-23">I</td><td id="2-24">62.6</td><td id="2-25">64.2</td><td id="2-26"></td><td id="2-27">dBc</td></tr>
<tr><td id="2-28">Signal-to-Noise and Distortion Ratio</td><td id="2-29">25°C</td><td id="2-2a">I</td><td id="2-2b">62.5</td><td id="2-2c">64.14</td><td id="2-2d"></td><td id="2-2e">dBc</td></tr>
<tr><td id="2-2f">Total Harmonic Distortion</td><td id="2-2g">25°C</td><td id="2-2h">I</td><td id="2-2i"></td><td id="2-2j">-79.22</td><td id="2-2k">-73.2</td><td id="2-2l">dBc</td></tr>
<tr><td id="2-2m">Spurious Free Dynamic Range</td><td id="2-2n">25°C</td><td id="2-2o">I</td><td id="2-2p">77.09</td><td id="2-2q">85.13</td><td id="2-2r"></td><td id="2-2s">dBc</td></tr>
<tr><td id="2-2t">CHANNEL-TO-CHANNEL ISOLATION</td><td id="2-2u"></td><td id="2-2v"></td><td id="2-2w"></td><td id="2-2x"></td><td id="2-2y"></td><td id="2-2z"></td></tr>
<tr><td id="2-2A">Tx-to-Rx (AOUT = 0 dBFS, fOUT = 7 MHz)</td><td id="2-2B">25°C</td><td id="2-2C">III</td><td id="2-2D"></td><td id="2-2E">&gt;90</td><td id="2-2F"></td><td id="2-2G">dB</td></tr>
<tr><td id="2-2H">Rx Channel Crosstalk (f₁ = 6 MHz, f₂ = 9 MHz)</td><td id="2-2I">25°C</td><td id="2-2J">III</td><td id="2-2K"></td><td id="2-2L">&gt;80</td><td id="2-2M"></td><td id="2-2N">dB</td></tr>
<tr><td id="2-2O">PARAMETERS</td><td id="2-2P"></td><td id="2-2Q"></td><td id="2-2R"></td><td id="2-2S"></td><td id="2-2T" colspan="2"></td></tr>
<tr><td id="2-2U">CMOS LOGIC INPUTS</td><td id="2-2V"></td><td id="2-2W"></td><td id="2-2X"></td><td id="2-2Y"></td><td id="2-2Z"></td><td id="2-30"></td></tr>
<tr><td id="2-31">Logic “1” Voltage, Vɪʜ</td><td id="2-32">25°C</td><td id="2-33">II</td><td id="2-34" colspan="2">DRVDD - 0.7</td><td id="2-35"></td><td id="2-36">V</td></tr>
<tr><td id="2-37">Logic &quot;0&quot; Voltage, Vɪʟ</td><td id="2-38">25°C</td><td id="2-39">II</td><td id="2-3a"></td><td id="2-3b"></td><td id="2-3c">0.4</td><td id="2-3d">V</td></tr>
<tr><td id="2-3e">Logic &quot;1&quot; Current</td><td id="2-3f">25°C</td><td id="2-3g">II</td><td id="2-3h"></td><td id="2-3i"></td><td id="2-3j">12</td><td id="2-3k">μA</td></tr>
<tr><td id="2-3l">Logic “0” Current</td><td id="2-3m">25°C</td><td id="2-3n">II</td><td id="2-3o"></td><td id="2-3p"></td><td id="2-3q">12</td><td id="2-3r">μA</td></tr>
<tr><td id="2-3s">Input Capacitance</td><td id="2-3t">25°C</td><td id="2-3u">III</td><td id="2-3v"></td><td id="2-3w">3</td><td id="2-3x"></td><td id="2-3y">pF</td></tr>
<tr><td id="2-3z">CMOS LOGIC OUTPUTS (1 mA Load)</td><td id="2-3A"></td><td id="2-3B"></td><td id="2-3C"></td><td id="2-3D"></td><td id="2-3E"></td><td id="2-3F"></td></tr>
<tr><td id="2-3G">Logic &quot;1&quot; Voltage, VOH</td><td id="2-3H">25°C</td><td id="2-3I">II</td><td id="2-3J" colspan="2">DRVDD – 0.6</td><td id="2-3K"></td><td id="2-3L">V</td></tr>
<tr><td id="2-3M">Logic &quot;0&quot; Voltage, VOL.</td><td id="2-3N">25°C</td><td id="2-3O">II</td><td id="2-3P"></td><td id="2-3Q"></td><td id="2-3R">0.4</td><td id="2-3S">V</td></tr>
<tr><td id="2-3T">POWER SUPPLY</td><td id="2-3U"></td><td id="2-3V"></td><td id="2-3W"></td><td id="2-3X"></td><td id="2-3Y"></td><td id="2-3Z"></td></tr>
<tr><td id="2-40">Analog Supply Currents</td><td id="2-41"></td><td id="2-42"></td><td id="2-43"></td><td id="2-44"></td><td id="2-45"></td><td id="2-46"></td></tr>
<tr><td id="2-47">Tx (Both Channels, 20 mA FS Output)</td><td id="2-48">25°C</td><td id="2-49">I</td><td id="2-4a"></td><td id="2-4b">70</td><td id="2-4c">76</td><td id="2-4d">mA</td></tr>
<tr><td id="2-4e">Tx Powered Down</td><td id="2-4f">25°C</td><td id="2-4g">I</td><td id="2-4h"></td><td id="2-4i">2.5</td><td id="2-4j">5.0</td><td id="2-4k">mA</td></tr>
<tr><td id="2-4l">Rx (Both Channels, Input Buffer Enabled)</td><td id="2-4m">25°C</td><td id="2-4n">I</td><td id="2-4o"></td><td id="2-4p">275</td><td id="2-4q">307</td><td id="2-4r">mA</td></tr>
<tr><td id="2-4s">Rx (Both Channels, Input Buffer Disabled)</td><td id="2-4t">25°C</td><td id="2-4u">III</td><td id="2-4v"></td><td id="2-4w">245</td><td id="2-4x"></td><td id="2-4y">mA</td></tr>
<tr><td id="2-4z">Rx (32 MSPS, Low Power Mode, Buffer Disabled)</td><td id="2-4A">25°C</td><td id="2-4B">III</td><td id="2-4C"></td><td id="2-4D">155</td><td id="2-4E"></td><td id="2-4F">mA</td></tr>
<tr><td id="2-4G">Rx (16 MSPS, Low Power Mode, Buffer Disabled)</td><td id="2-4H">25°C</td><td id="2-4I">III</td><td id="2-4J"></td><td id="2-4K">80</td><td id="2-4L"></td><td id="2-4M">mA</td></tr>
<tr><td id="2-4N">Rx Path Powered Down</td><td id="2-4O">25°C</td><td id="2-4P">I</td><td id="2-4Q"></td><td id="2-4R">5.0</td><td id="2-4S">6.0</td><td id="2-4T">mA</td></tr>
<tr><td id="2-4U">DLL</td><td id="2-4V">25°C</td><td id="2-4W">III</td><td id="2-4X"></td><td id="2-4Y">12</td><td id="2-4Z"></td><td id="2-50">mA</td></tr>
<tr><td id="2-51">Digital Supply Current</td><td id="2-52"></td><td id="2-53"></td><td id="2-54"></td><td id="2-55"></td><td id="2-56"></td><td id="2-57"></td></tr>
<tr><td id="2-58">AD9860 Both Rx and Tx Path (All Channels Enabled)</td><td id="2-59"></td><td id="2-5a"></td><td id="2-5b"></td><td id="2-5c"></td><td id="2-5d"></td><td id="2-5e"></td></tr>
<tr><td id="2-5f">2× Interpolation, fDAC = fADC = 64 MSPS</td><td id="2-5g">25°C</td><td id="2-5h">I</td><td id="2-5i"></td><td id="2-5j">92</td><td id="2-5k">112</td><td id="2-5l">mA</td></tr>
<tr><td id="2-5m">AD9862 Both Rx and Tx Path (All Channels Enabled)</td><td id="2-5n"></td><td id="2-5o"></td><td id="2-5p"></td><td id="2-5q"></td><td id="2-5r"></td><td id="2-5s"></td></tr>
<tr><td id="2-5t">2× Interpolation, fDAC = fADC = 64 MSPS</td><td id="2-5u">25°C</td><td id="2-5v">I</td><td id="2-5w"></td><td id="2-5x">104</td><td id="2-5y">124</td><td id="2-5z">mA</td></tr>
<tr><td id="2-5A">Tx Path (fDAC = 128 MSPS)</td><td id="2-5B"></td><td id="2-5C"></td><td id="2-5D"></td><td id="2-5E"></td><td id="2-5F"></td><td id="2-5G"></td></tr>
<tr><td id="2-5H">Processing Blocks Disabled</td><td id="2-5I">25°C</td><td id="2-5J">III</td><td id="2-5K"></td><td id="2-5L">45</td><td id="2-5M"></td><td id="2-5N">mA</td></tr>
<tr><td id="2-5O">4× Interpolation</td><td id="2-5P">25°C</td><td id="2-5Q">III</td><td id="2-5R"></td><td id="2-5S">90</td><td id="2-5T"></td><td id="2-5U">mA</td></tr>
<tr><td id="2-5V">4× Interpolation, Coarse Modulation</td><td id="2-5W">25°C</td><td id="2-5X">III</td><td id="2-5Y"></td><td id="2-5Z">110</td><td id="2-60"></td><td id="2-61">mA</td></tr>
<tr><td id="2-62">4× Interpolation, Fine Modulation</td><td id="2-63">25°C</td><td id="2-64">III</td><td id="2-65"></td><td id="2-66">110</td><td id="2-67"></td><td id="2-68">mA</td></tr>
<tr><td id="2-69">4× Interpolation, Coarse and Fine Modulation</td><td id="2-6a">25°C</td><td id="2-6b">III</td><td id="2-6c"></td><td id="2-6d">130</td><td id="2-6e"></td><td id="2-6f">mA</td></tr>
</table>

<a id='d6d1664c-2141-4dc6-9038-cfcaeeb3d583'></a>

REV. 0

<a id='2746af13-c731-4c24-8c34-9d964b7dbee0'></a>

-3-

<!-- PAGE BREAK -->

<a id='c4f7825e-2678-47af-ba6b-ff114814cf9d'></a>

AD9860/AD9862

<a id='71b3e3c3-5e86-4cd1-b13c-b3fa9fc6965b'></a>

<table id="3-1">
<tr><td id="3-2"></td><td id="3-3" rowspan="2">Temp</td><td id="3-4" rowspan="2">Test Level</td><td id="3-5" colspan="3">AD9860/AD9862</td><td id="3-6"></td></tr>
<tr><td id="3-7">PARAMETERS (continued)</td><td id="3-8">Min</td><td id="3-9">Typ</td><td id="3-a">Max</td><td id="3-b">Unit</td></tr>
<tr><td id="3-c">POWER SUPPLY (continued)</td><td id="3-d"></td><td id="3-e"></td><td id="3-f"></td><td id="3-g"></td><td id="3-h"></td><td id="3-i"></td></tr>
<tr><td id="3-j">Rx Path (fADC = 64 MSPS)</td><td id="3-k"></td><td id="3-l"></td><td id="3-m"></td><td id="3-n"></td><td id="3-o"></td><td id="3-p"></td></tr>
<tr><td id="3-q">Processing Blocks Disabled</td><td id="3-r">25°C</td><td id="3-s">III</td><td id="3-t"></td><td id="3-u">9</td><td id="3-v"></td><td id="3-w">mA</td></tr>
<tr><td id="3-x">Decimation Filter Enabled</td><td id="3-y">25°C</td><td id="3-z">III</td><td id="3-A"></td><td id="3-B">15</td><td id="3-C"></td><td id="3-D">mA</td></tr>
<tr><td id="3-E">Hilbert Filter Enabled</td><td id="3-F">25°C</td><td id="3-G">III</td><td id="3-H"></td><td id="3-I">16</td><td id="3-J"></td><td id="3-K">mA</td></tr>
<tr><td id="3-L">Hilbert and Decimation Filter Enabled</td><td id="3-M">25°C</td><td id="3-N">III</td><td id="3-O"></td><td id="3-P">18.5</td><td id="3-Q"></td><td id="3-R">mA</td></tr>
</table>

<a id='bb639230-9032-4c09-b49e-d87fc8fb5747'></a>

NOTES
1% fDATA refers to the input data rate of the digital block.
2Interpolation filter stop band is defined by image suppression of 50 dB or greater.
Specifications subject to change without notice.

<a id='b4057c0f-f7d2-4777-83b5-52e069176570'></a>

TIMING CHARACTERISTICS
<table id="3-S">
<tr><td id="3-T" rowspan="2">(20 pF Load)</td><td id="3-U"></td><td id="3-V" rowspan="2">Test Level</td><td id="3-W"></td><td id="3-X" colspan="2">AD9860/AD9862</td><td id="3-Y"></td></tr>
<tr><td id="3-Z">Temp</td><td id="3-10">Min</td><td id="3-11">Typ</td><td id="3-12">Max</td><td id="3-13">Unit</td></tr>
<tr><td id="3-14">Minimum Reset Pulsewidth Low (tRL.)</td><td id="3-15">NA</td><td id="3-16">NA</td><td id="3-17">5</td><td id="3-18"></td><td id="3-19"></td><td id="3-1a">Clock Cycles</td></tr>
<tr><td id="3-1b">Digital Output Rise/Fall Time</td><td id="3-1c">25°C</td><td id="3-1d">III</td><td id="3-1e">2.8</td><td id="3-1f"></td><td id="3-1g">4</td><td id="3-1h">ns</td></tr>
<tr><td id="3-1i">DLL Output Clock</td><td id="3-1j">25°C</td><td id="3-1k">III</td><td id="3-1l">32</td><td id="3-1m"></td><td id="3-1n">128</td><td id="3-1o">MHz</td></tr>
<tr><td id="3-1p">DLL Output Duty Cycle</td><td id="3-1q">25°C</td><td id="3-1r">III</td><td id="3-1s"></td><td id="3-1t">50</td><td id="3-1u"></td><td id="3-1v">%</td></tr>
<tr><td id="3-1w">Tx-/Rx-Interface (See Figures 11 and 12)</td><td id="3-1x"></td><td id="3-1y"></td><td id="3-1z"></td><td id="3-1A"></td><td id="3-1B"></td><td id="3-1C"></td></tr>
<tr><td id="3-1D">TxSYNC/TxIQ Setup Time (trx1, 17x3)</td><td id="3-1E">25°C</td><td id="3-1F">III</td><td id="3-1G">3</td><td id="3-1H"></td><td id="3-1I"></td><td id="3-1J">ns</td></tr>
<tr><td id="3-1K">TxSYNC/TxIQ Hold Time (17x2, Tx4)</td><td id="3-1L">25°C</td><td id="3-1M">III</td><td id="3-1N">3</td><td id="3-1O"></td><td id="3-1P"></td><td id="3-1Q">ns</td></tr>
<tr><td id="3-1R">RxSYNC/RxIQ/IF to Valid Time(trat, tru3)</td><td id="3-1S">25°C</td><td id="3-1T">III</td><td id="3-1U"></td><td id="3-1V"></td><td id="3-1W">5.2</td><td id="3-1X">ns</td></tr>
<tr><td id="3-1Y">RxSYNC/RxIQ/IF Hold Time (tRx2, tRx4)</td><td id="3-1Z">25°C</td><td id="3-20">III</td><td id="3-21">0.2</td><td id="3-22"></td><td id="3-23"></td><td id="3-24">ns</td></tr>
<tr><td id="3-25">Serial Control Bus (See Figures 1 and 2)</td><td id="3-26"></td><td id="3-27"></td><td id="3-28"></td><td id="3-29"></td><td id="3-2a"></td><td id="3-2b"></td></tr>
<tr><td id="3-2c">Maximum SCLK Frequency (fSCLK)</td><td id="3-2d">Full</td><td id="3-2e">III</td><td id="3-2f"></td><td id="3-2g"></td><td id="3-2h">16</td><td id="3-2i">MHz</td></tr>
<tr><td id="3-2j">Minimum Clock Pulsewidth High (tH1)</td><td id="3-2k">Full</td><td id="3-2l">III</td><td id="3-2m">30</td><td id="3-2n"></td><td id="3-2o"></td><td id="3-2p">ns</td></tr>
<tr><td id="3-2q">Minimum Clock Pulsewidth Low (tLOW)</td><td id="3-2r">Full</td><td id="3-2s">III</td><td id="3-2t">30</td><td id="3-2u"></td><td id="3-2v"></td><td id="3-2w">ns</td></tr>
<tr><td id="3-2x">Maximum Clock Rise/Fall Time</td><td id="3-2y">Full</td><td id="3-2z">III</td><td id="3-2A"></td><td id="3-2B"></td><td id="3-2C">1</td><td id="3-2D">ms</td></tr>
<tr><td id="3-2E">Minimum Data/SEN Setup Time (ts)</td><td id="3-2F">Full</td><td id="3-2G">III</td><td id="3-2H">25</td><td id="3-2I"></td><td id="3-2J"></td><td id="3-2K">ns</td></tr>
<tr><td id="3-2L">Minimum SEN/Data Hold Time (tH)</td><td id="3-2M">Full</td><td id="3-2N">III</td><td id="3-2O">0</td><td id="3-2P"></td><td id="3-2Q"></td><td id="3-2R">ns</td></tr>
<tr><td id="3-2S">Minimum Data/SCLK Setup Time (tDS)</td><td id="3-2T">Full</td><td id="3-2U">III</td><td id="3-2V">25</td><td id="3-2W"></td><td id="3-2X"></td><td id="3-2Y">ns</td></tr>
<tr><td id="3-2Z">Minimum Data Hold Time (tDH)</td><td id="3-30">Full</td><td id="3-31">III</td><td id="3-32">0</td><td id="3-33"></td><td id="3-34"></td><td id="3-35">ns</td></tr>
<tr><td id="3-36">Output Data Valid/SCLK Time (tDV)</td><td id="3-37">Full</td><td id="3-38">III</td><td id="3-39"></td><td id="3-3a"></td><td id="3-3b">30</td><td id="3-3c">ns</td></tr>
<tr><td id="3-3d">AUXILARY ADC</td><td id="3-3e"></td><td id="3-3f"></td><td id="3-3g"></td><td id="3-3h"></td><td id="3-3i"></td><td id="3-3j"></td></tr>
<tr><td id="3-3k">Conversion Rate</td><td id="3-3l">25°C</td><td id="3-3m">III</td><td id="3-3n"></td><td id="3-3o">1.25</td><td id="3-3p"></td><td id="3-3q">MHz</td></tr>
<tr><td id="3-3r">Input Range</td><td id="3-3s">25°C</td><td id="3-3t">III</td><td id="3-3u"></td><td id="3-3v">3</td><td id="3-3w"></td><td id="3-3x">V</td></tr>
<tr><td id="3-3y">Resolution</td><td id="3-3z">25°C</td><td id="3-3A">III</td><td id="3-3B"></td><td id="3-3C">10</td><td id="3-3D"></td><td id="3-3E">Bits</td></tr>
<tr><td id="3-3F">AUXILARY DAC</td><td id="3-3G"></td><td id="3-3H"></td><td id="3-3I"></td><td id="3-3J"></td><td id="3-3K"></td><td id="3-3L"></td></tr>
<tr><td id="3-3M">Settling Time</td><td id="3-3N">25°C</td><td id="3-3O">III</td><td id="3-3P"></td><td id="3-3Q">8</td><td id="3-3R"></td><td id="3-3S">μs</td></tr>
<tr><td id="3-3T">Output Range</td><td id="3-3U">25°C</td><td id="3-3V">III</td><td id="3-3W"></td><td id="3-3X">3</td><td id="3-3Y"></td><td id="3-3Z">V</td></tr>
<tr><td id="3-40">Resolution</td><td id="3-41">25°C</td><td id="3-42">III</td><td id="3-43"></td><td id="3-44">8</td><td id="3-45"></td><td id="3-46">Bits</td></tr>
<tr><td id="3-47">ADC TIMING</td><td id="3-48"></td><td id="3-49"></td><td id="3-4a"></td><td id="3-4b"></td><td id="3-4c"></td><td id="3-4d"></td></tr>
<tr><td id="3-4e">Latency (All Digital Processing Blocks Disabled)</td><td id="3-4f">25°C</td><td id="3-4g">III</td><td id="3-4h"></td><td id="3-4i">7</td><td id="3-4j"></td><td id="3-4k">Cycles</td></tr>
<tr><td id="3-4l">DAC Timing</td><td id="3-4m"></td><td id="3-4n"></td><td id="3-4o"></td><td id="3-4p"></td><td id="3-4q"></td><td id="3-4r"></td></tr>
<tr><td id="3-4s">Latency (All Digital Processing Blocks Disabled)</td><td id="3-4t">25°C</td><td id="3-4u">III</td><td id="3-4v"></td><td id="3-4w">3</td><td id="3-4x"></td><td id="3-4y">Cycles</td></tr>
<tr><td id="3-4z">Latency (2× Interpolation Enabled)</td><td id="3-4A">25°C</td><td id="3-4B">III</td><td id="3-4C"></td><td id="3-4D">30</td><td id="3-4E"></td><td id="3-4F">Cycles</td></tr>
<tr><td id="3-4G">Latency (4× Interpolation Enabled)</td><td id="3-4H">25°C</td><td id="3-4I">III</td><td id="3-4J"></td><td id="3-4K">72</td><td id="3-4L"></td><td id="3-4M">Cycles</td></tr>
<tr><td id="3-4N">Additional Latency (Hilbert Filter Enabled)</td><td id="3-4O">25°C</td><td id="3-4P">III</td><td id="3-4Q"></td><td id="3-4R">36</td><td id="3-4S"></td><td id="3-4T">Cycles</td></tr>
<tr><td id="3-4U">Additional Latency (Coarse Modulation Enabled)</td><td id="3-4V">25°C</td><td id="3-4W">III</td><td id="3-4X"></td><td id="3-4Y">5</td><td id="3-4Z"></td><td id="3-50">Cycles</td></tr>
<tr><td id="3-51">Additional Latency (Fine Modulation Enabled)</td><td id="3-52">25°C</td><td id="3-53">III</td><td id="3-54"></td><td id="3-55">8</td><td id="3-56"></td><td id="3-57">Cycles</td></tr>
<tr><td id="3-58">Output Settling Time (TST) (to 0.1%)</td><td id="3-59">25°C</td><td id="3-5a">III</td><td id="3-5b"></td><td id="3-5c">35</td><td id="3-5d"></td><td id="3-5e">ns</td></tr>
</table>
Specifications subject to change without notice.

<a id='d09c81c6-ea67-433d-b2cc-3a5f2b5f4d31'></a>

-4-

<a id='3d8d4ee9-8c9e-4384-a9f2-5cd89320a1b5'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='c3893d47-2d56-40b3-8ebf-2a6467eec4e6'></a>

AD9860/AD9862

<a id='eb143069-d06e-4c9c-9e3a-e3e95997aabd'></a>

**ABSOLUTE MAXIMUM RATINGS**¹

Power Supply (V₀₃, V₀₃) ... 3.9 V
Digital Output Current ... 5 mA
Digital Inputs ... -0.3 V to DRVDD + 0.3 V
Analog Inputs ... -0.3 V to AVDD (IQ) + 0.3 V
Operating Temperature² ... -40°C to +70°C
Maximum Junction Temperature ... 150°C
Storage Temperature ... -65°C to +150°C
Lead Temperature (Soldering 10 sec) ... 300°C

<a id='7c57584b-45bc-4283-9179-fb86582eeaa1'></a>

NOTES

¹Absolute maximum ratings are limiting values, to be applied individually, and beyond which the serviceability of the circuit may be impaired. Functional operability under any of these conditions is not necessarily implied. Exposure to absolute maximum rating conditions for extended periods of time may affect device reliability.

<a id='39a5810f-164c-4e64-8e65-9d0df5ccfdb8'></a>

²The AD9860/AD9862 have been characterized to operate over the industrial temperature range (−40°C to +85°C) when operated in Half Duplex Mode.

<a id='36c8277d-f6fd-4953-aed3-d7cac042c273'></a>

### EXPLANATION OF TEST LEVELS
I. Devices are 100% production tested at 25°C and guaranteed by design and characterization testing for the extended industrial temperature range (-40°C to +70°C).
II. Parameter is guaranteed by design and/or characterization testing.
III. Parameter is a typical value only.
NA. Test level definition is not applicable.

<a id='80489a73-fd54-4a0e-832e-5ef74386445d'></a>

# THERMAL CHARACTERISTICS

## Thermal Resistance
128-Lead LQFP θJA = 29°C/W

<a id='e11f510c-260d-4442-ab55-4c084df978d8'></a>

ORDERING GUIDE
<table id="4-1">
<tr><td id="4-2">Model</td><td id="4-3">Temperature Range</td><td id="4-4">Package Description</td><td id="4-5">Package Option</td></tr>
<tr><td id="4-6">AD9860BST</td><td id="4-7">-40°C to +70°C*</td><td id="4-8">128-Lead Low Profile Plastic Quad Flatpack (LQFP)</td><td id="4-9">ST-128B</td></tr>
<tr><td id="4-a">AD9862BST</td><td id="4-b">-40°C to +70°C*</td><td id="4-c">128-Lead Low Profile Plastic Quad Flatpack (LQFP)</td><td id="4-d">ST-128B</td></tr>
<tr><td id="4-e">AD9860PCB</td><td id="4-f"></td><td id="4-g">Evaluation Board with AD9860</td><td id="4-h"></td></tr>
<tr><td id="4-i">AD9862PCB</td><td id="4-j"></td><td id="4-k">Evaluation Board with AD9862</td><td id="4-l"></td></tr>
</table>
*The AD9860/AD9862 have been characterized to operate over the industrial temperature range (-40°C to +85°C) when operated in Half Duplex Mode.

<a id='36ff9498-1b1f-4d7a-9480-44a372305d4c'></a>

CAUTION
---
ESD (electrostatic discharge) sensitive device. Electrostatic charges as high as 4000 V readily accumulate on the human body and test equipment and can discharge without detection. Although the AD9860/AD9862 features proprietary ESD protection circuitry, permanent damage may occur on devices subjected to high energy electrostatic discharges. Therefore, proper ESD precautions are recommended to avoid performance degradation or loss of functionality.

<a id='5fbfa93d-bd48-4795-b6fb-3a427a30b34e'></a>

<::logo: [ESD Warning Label]
WARNING!
ESD SENSITIVE DEVICE
This logo features a black rectangular background with white text and graphics, including a microchip and a hand discharging static electricity towards it, indicating a warning about electrostatic discharge sensitive devices.::>

<a id='d998f9e7-4b2a-4cce-b746-1ce50c33a5ad'></a>

REV. 0

<a id='fab08599-afb4-4312-b7c1-fd1894e0e1db'></a>

-5-

<!-- PAGE BREAK -->

<a id='0fdba30c-b317-4aa0-97f3-9c0fb4994412'></a>

AD9860/AD9862

<a id='be6e9a55-fb70-4fbf-a981-44a920f6dae5'></a>

PIN FUNCTION DESCRIPTIONS

<a id='c4c1b166-213e-47e2-a7b4-1728378f8f17'></a>

<table id="6-1">
<tr><td id="6-2">Pin No.</td><td id="6-3">Mnemonic</td><td id="6-4">Function</td></tr>
<tr><td id="6-5" colspan="3">Receive Pins</td></tr>
<tr><td id="6-6">68/70–79</td><td id="6-7">D0A to D9A/D11A</td><td id="6-8">10-/12-Bit ADC Output of Receive Channel A</td></tr>
<tr><td id="6-9">80/82–91</td><td id="6-a">D0B to D9B/D11B</td><td id="6-b">10-/12-Bit ADC Output of Receive Channel B</td></tr>
<tr><td id="6-c">92</td><td id="6-d">RxSYNC</td><td id="6-e">Synchronization Clock for Channel A and Channel B Rx Paths</td></tr>
<tr><td id="6-f">98, 99,</td><td id="6-g">AVDD</td><td id="6-h">Analog Supply Pins</td></tr>
<tr><td id="6-i">104, 105,</td><td id="6-j"></td><td id="6-k"></td></tr>
<tr><td id="6-l">117, 118,</td><td id="6-m"></td><td id="6-n"></td></tr>
<tr><td id="6-o">123, 124,</td><td id="6-p"></td><td id="6-q"></td></tr>
<tr><td id="6-r">100, 103,</td><td id="6-s">AGND</td><td id="6-t">Analog Ground Pins</td></tr>
<tr><td id="6-u">106, 109,</td><td id="6-v"></td><td id="6-w"></td></tr>
<tr><td id="6-x">110, 112,</td><td id="6-y"></td><td id="6-z"></td></tr>
<tr><td id="6-A">113, 116,</td><td id="6-B"></td><td id="6-C"></td></tr>
<tr><td id="6-D">119, 122,</td><td id="6-E"></td><td id="6-F"></td></tr>
<tr><td id="6-G">101</td><td id="6-H">REFT_B</td><td id="6-I">Top Reference Decoupling for Channel B ADC</td></tr>
<tr><td id="6-J">102</td><td id="6-K">REFB_B</td><td id="6-L">Bottom Reference Decoupling for Channel B ADC</td></tr>
<tr><td id="6-M">107</td><td id="6-N">VIN+B</td><td id="6-O">Receive Channel B Differential (+) Input</td></tr>
<tr><td id="6-P">108</td><td id="6-Q">VIN-B</td><td id="6-R">Receive Channel B Differential (-) Input</td></tr>
<tr><td id="6-S">111</td><td id="6-T">VREF</td><td id="6-U">Internal ADC Voltage Reference</td></tr>
<tr><td id="6-V">114</td><td id="6-W">VIN-A</td><td id="6-X">Receive Channel A Differential (-) Input</td></tr>
<tr><td id="6-Y">115</td><td id="6-Z">VIN+A</td><td id="6-10">Receive Channel A Differential (+) Input</td></tr>
<tr><td id="6-11">120</td><td id="6-12">REFB_A</td><td id="6-13">Bottom Reference Decoupling for Channel A ADC</td></tr>
<tr><td id="6-14">121</td><td id="6-15">REFT_A</td><td id="6-16">Top Reference Decoupling for Channel A ADC</td></tr>
</table>

<a id='413bf942-98b0-4deb-a4a6-201d15b0ea5b'></a>

Transmit Pins
<table id="6-17">
<tr><td id="6-18">18, 20</td><td id="6-19">AVDD</td><td id="6-1a">Analog Supply Pins</td></tr>
<tr><td id="6-1b">23, 32</td><td id="6-1c"></td><td id="6-1d"></td></tr>
<tr><td id="6-1e">19, 24,</td><td id="6-1f">AGND</td><td id="6-1g">Analog Ground Pins</td></tr>
<tr><td id="6-1h">27, 28, 31</td><td id="6-1i"></td><td id="6-1j"></td></tr>
<tr><td id="6-1k">21</td><td id="6-1l">REFIO</td><td id="6-1m">Reference Output, 1.2 V Nominal</td></tr>
<tr><td id="6-1n">22</td><td id="6-1o">FSADJ</td><td id="6-1p">Full-Scale Current Adjust</td></tr>
<tr><td id="6-1q">25</td><td id="6-1r">IOUT-A</td><td id="6-1s">Transmit Channel A DAC Differential (-) Output</td></tr>
<tr><td id="6-1t">26</td><td id="6-1u">IOUT+A</td><td id="6-1v">Transmit Channel A DAC Differential (+) Output</td></tr>
<tr><td id="6-1w">29</td><td id="6-1x">IOUT+B</td><td id="6-1y">Transmit Channel B DAC Differential (+) Output</td></tr>
<tr><td id="6-1z">30</td><td id="6-1A">IOUT-B</td><td id="6-1B">Transmit Channel B DAC Differential (-) Output</td></tr>
<tr><td id="6-1C">37-48/50</td><td id="6-1D">Tx11/Tx13 to Tx0</td><td id="6-1E">12-/14-Bit Transmit DAC Data (Interleaved Data when Required)</td></tr>
<tr><td id="6-1F">51</td><td id="6-1G">TxSYNC</td><td id="6-1H">Synchronization Input for Transmitter</td></tr>
<tr><td id="6-1I">62</td><td id="6-1J">MODE/ TxBLANK*</td><td id="6-1K">Configures Default Timing Mode, Controls Tx Digital Power Down</td></tr>
</table>
*The logic level of the Mode/TxBLANK pin at power up defines the default timing
mode; a logic low configures Normal Operation, logic high configures Alternate
Operation Mode.

<a id='8459d6ca-79d0-45a9-9411-1a43a1ffac5f'></a>

<table id="6-1L">
<tr><td id="6-1M">Pin No.</td><td id="6-1N">Mnemonic</td><td id="6-1O">Function</td></tr>
<tr><td id="6-1P" colspan="3">Clock Pins</td></tr>
<tr><td id="6-1Q">10</td><td id="6-1R">DLL_Lock</td><td id="6-1S">DLL Lock Indicator Pin</td></tr>
<tr><td id="6-1T">11, 16</td><td id="6-1U">AGND</td><td id="6-1V">DLL Analog Ground Pins</td></tr>
<tr><td id="6-1W">12</td><td id="6-1X">NC</td><td id="6-1Y">No Connect</td></tr>
<tr><td id="6-1Z">13</td><td id="6-20">AVDD</td><td id="6-21">DLL Analog Supply Pin</td></tr>
<tr><td id="6-22">14</td><td id="6-23">OSC1</td><td id="6-24">Single Ended Input Clock (or Crystal Oscillator Input)</td></tr>
<tr><td id="6-25">15</td><td id="6-26">OSC2</td><td id="6-27">Crystal Oscillator Input</td></tr>
<tr><td id="6-28">17</td><td id="6-29">CLKSEL</td><td id="6-2a">Controls CLKOUT1 Rate</td></tr>
<tr><td id="6-2b">64</td><td id="6-2c">CLKOUT2</td><td id="6-2d">Clock Output Generated from Input Clock (DLL Multiplier Setting and CLKOUT2 Divide Factor)</td></tr>
<tr><td id="6-2e">65</td><td id="6-2f">CLKOUT1</td><td id="6-2g">Clock Output Generated from Input Clock (1× if CLKSEL = 1 or /2 if CLKSEL = 0)</td></tr>
<tr><td id="6-2h" colspan="3">Various Pins</td></tr>
<tr><td id="6-2i">1</td><td id="6-2j">AUX_ADC_A1</td><td id="6-2k">Auxiliary ADC A Input 1</td></tr>
<tr><td id="6-2l">3, 4, 13</td><td id="6-2m">AVDD</td><td id="6-2n">Analog Power Pins</td></tr>
<tr><td id="6-2o">2, 9</td><td id="6-2p">AGND</td><td id="6-2q">Analog Ground Pins</td></tr>
<tr><td id="6-2r">5</td><td id="6-2s">SIGDELT</td><td id="6-2t">Digital Output from Programmable Sigma-Delta</td></tr>
<tr><td id="6-2u">6</td><td id="6-2v">AUX_DAC_A</td><td id="6-2w">Auxiliary DAC A Output</td></tr>
<tr><td id="6-2x">7</td><td id="6-2y">AUX_DAC_B</td><td id="6-2z">Auxiliary DAC B Output</td></tr>
<tr><td id="6-2A">8</td><td id="6-2B">AUX_DAC_C</td><td id="6-2C">Auxiliary DAC C Output</td></tr>
<tr><td id="6-2D">33, 36, 53,</td><td id="6-2E">DVDD</td><td id="6-2F">Digital Power Supply Pin</td></tr>
<tr><td id="6-2G">59, 61, 66, 93</td><td id="6-2H"></td><td id="6-2I"></td></tr>
<tr><td id="6-2J">34, 35, 52</td><td id="6-2K">DGND</td><td id="6-2L">Digital Ground Pin</td></tr>
<tr><td id="6-2M">58, 60, 67, 94</td><td id="6-2N"></td><td id="6-2O"></td></tr>
<tr><td id="6-2P">54</td><td id="6-2Q">SCLK</td><td id="6-2R">Serial Bus Clock Input</td></tr>
<tr><td id="6-2S">55</td><td id="6-2T">SDO</td><td id="6-2U">Serial Bus Data Bit</td></tr>
<tr><td id="6-2V">56</td><td id="6-2W">SDIO</td><td id="6-2X">Serial Bus Data Bit</td></tr>
<tr><td id="6-2Y">57</td><td id="6-2Z">SEN</td><td id="6-30">Serial Bus Enable</td></tr>
<tr><td id="6-31">63</td><td id="6-32">RESETB</td><td id="6-33">Reset (SPI Registers and Logic)</td></tr>
<tr><td id="6-34">95</td><td id="6-35">AUX_SPI_do</td><td id="6-36">Optional Auxiliary ADC Serial Bus Data Out Bit</td></tr>
<tr><td id="6-37">96</td><td id="6-38">AUX_SPI_clk</td><td id="6-39">Optional Auxiliary ADC Serial Bus Data Out Latch Clock</td></tr>
<tr><td id="6-3a">97</td><td id="6-3b">AUX_SPI_csb</td><td id="6-3c">Optional Auxiliary ADC Serial Bus Chip Select Bit</td></tr>
<tr><td id="6-3d">128</td><td id="6-3e">AUX_ADC_A2</td><td id="6-3f">Auxiliary ADC A Input 2</td></tr>
<tr><td id="6-3g">126</td><td id="6-3h">AUX_ADC_B1</td><td id="6-3i">Auxiliary ADC B Input 1</td></tr>
<tr><td id="6-3j">125</td><td id="6-3k">AUX_ADC_B2</td><td id="6-3l">Auxiliary ADC B Input 2</td></tr>
<tr><td id="6-3m">127</td><td id="6-3n">AUX_ADC_REF</td><td id="6-3o">Auxiliary ADC Reference</td></tr>
</table>

<a id='69e4af4a-c83b-425d-83b4-680464a48e76'></a>

REV. 0

<a id='418e089e-7cc2-4dbe-a607-2ebf006d5e48'></a>

-7-

<!-- PAGE BREAK -->

<a id='1e6e4df7-611c-4eb8-884b-bcb8185f7769'></a>

AD9860/AD9862

<a id='1fb4a181-b5fe-448f-886e-32a3e80e7d3b'></a>

**DEFINITIONS OF SPECIFICATIONS**

**Differential Nonlinearity Error (DNL, No Missing Codes)**
An ideal converter exhibits code transitions that are exactly 1 LSB apart. DNL is the deviation from this ideal value. Guaranteed no missing codes to 10-bit resolution indicate that all 1024 codes respectively, must be present over all operating ranges.

<a id='48398a84-31a6-4163-a5ca-5f084006e8c1'></a>

**Integral Nonlinearity Error (INL)**
Linearity error refers to the deviation of each individual code from
a line drawn from "negative full scale" through "positive full
scale." The point used as "negative full scale" occurs 1/2 LSB
before the first code transition. "Positive full scale" is defined as
a level 1 1/2 LSB beyond the last code transition. The deviation
is measured from the middle of each particular code to the true
straight line.

<a id='a018aa00-9cbf-4d0f-ba7b-209010ee9720'></a>

## Phase Noise
Single-sideband phase noise power is specified relative to the carrier (dBc/Hz) at a given frequency offset (1 kHz) from the carrier. Phase noise can be measured directly in Single Tone Trans- mit Mode with a spectrum analyzer that supports noise marker measurements. It detects the relative power between the carrier and the offset (1 kHz) sideband noise and takes the resolution bandwidth (rbw) into account by subtracting 10 log(rbw). It also adds a correction factor that compensates for the implementation of the resolution bandwidth, log display, and detector characteristic.

<a id='a73117fe-e829-4c52-9540-5f5c725dc782'></a>

**Output Compliance Range**
The range of allowable voltage at the output of a current-output DAC. Operation beyond the maximum compliance limits may cause either output stage saturation or breakdown, resulting in nonlinear performance.

<a id='98df7001-6228-4b30-a9e0-db33e0846278'></a>

**Spurious-Free Dynamic Range (SFDR)**
The difference, in dB, between the rms amplitude of the DAC's output signal (or ADC's input signal) and the peak spurious signal over the specified bandwidth (Nyquist bandwidth unless otherwise noted).

<a id='07fc98d1-c7d4-4bf0-b954-98bc618dd288'></a>

**Pipeline Delay (Latency)**
The number of clock cycles between conversion initiation and
the associated output data being made available.

<a id='3a6cb6a3-96e8-42e4-aa52-635e6a1bae1c'></a>

### Offset Error
First transition should occur for an analog value 1/2 LSB above
-full scale. Offset error is defined as the deviation of the actual
transition from that point.

<a id='a3bbf2e1-a204-4615-92a4-a80ba429582c'></a>

**Gain Error**
The first code transition should occur at an analog value 1/2 LSB
above -full scale. The last transition should occur for an analog
value 1 1/2 LSB below the nominal full scale. Gain error is the
deviation of the actual difference between first and last code
transitions and the ideal difference between first and last code
transitions.

<a id='00362d20-e740-4748-ac84-315d2766eb8e'></a>

**Aperture Delay**
The aperture delay is a measure of the Sample-and-Hold Ampli-
fier (SHA) performance and specifies the time delay between the
rising edge of the sampling clock input to when the input signal
is held for conversion.

<a id='01e68186-9f0f-4ad6-bfb7-fc6a1554e759'></a>

**Aperture Uncertainty (Jitter)**
Aperture jitter is the variation in aperture delay for successive samples and is manifested as noise on the input to the ADC.

<a id='2d1bf1bf-d62e-411d-a3dd-22b606a70cd6'></a>

**Input Referred Noise**
The rms output noise is measured using histogram techniques.
The ADC output code's standard deviation is calculated in LSB
and converted to an equivalent voltage. This results in a noise
figure that can be referred directly to the input of the AD9860/
AD9862.

<a id='fd46b555-4ffc-4045-bd42-70ee56fe44f8'></a>

**Signal-to-Noise and Distortion (S/N+D, SINAD) Ratio**
S/N+D is the ratio of the rms value of the measured input signal
to the rms sum of all other spectral components below the Nyquist
frequency, including harmonics but excluding dc. The value for
S/N+D is expressed in decibels.

<a id='887f901b-f5cb-4c36-8fc1-40450de99c8d'></a>

**Effective Number of Bits (ENOB)**
For a sine wave, *SINAD* can be expressed in terms of the number
of bits. Using the following formula:

<a id='f8b97a9b-2fc5-4e61-9f61-94ef90a9e88f'></a>

N = (SINAD - 1.76 dB) / 6.02

<a id='2bb5a226-1ebd-48e3-99f9-1601e46c661f'></a>

it is possible to get a measure of performance expressed as N,
the effective number of bits. Thus, effective number of bits for
a device for sine wave inputs at a given input frequency can be
calculated directly from its measured SINAD.

<a id='8826acad-2ec4-4a08-8aae-57da9ea8cea6'></a>

**Signal-to-Noise Ratio (SNR)**
SNR is the ratio of the rms value of the measured input signal to the rms sum of all other spectral components below the Nyquist frequency, excluding harmonics and dc. The value for SNR is expressed in decibels.

<a id='d3cd6387-f972-4098-a1b7-8d8b2e2740cc'></a>

**Total Harmonic Distortion (THD)**
THD is the ratio of the rms sum of the first six harmonic
components to the rms value of the measured input signal and
is expressed as a percentage or in decibels.

<a id='14db4ec9-9914-48a4-b9a7-074a86736a06'></a>

**Power Supply Rejection**
Power supply rejection specifies the converter's maximum full-scale change when the supplies are varied from nominal to minimum and maximum specified voltages.

<a id='ea893c6e-3d10-42f1-a472-2d99e8554353'></a>

**Channel-to-Channel Isolation (Crosstalk)**
In an ideal multichannel system, the signal in one channel will not influence the signal level of another channel. The channel- to-channel isolation specification is a measure of the change that occurs to a grounded channel as a full-scale signal is applied to another channel.

<a id='f02a5411-e193-4991-871a-3275a9e67050'></a>

-8-

<a id='89e8abf6-d607-4eac-8f14-9cae9cef711e'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='54b87e62-6215-4476-8eb1-09c565d3bbfa'></a>

Typical Performance Characteristics-AD9860/AD9862

<a id='eaf4e8af-286c-40a0-aaef-426d47789781'></a>

<::fDATA = 32MSPS
4X INTERPOLATION
MAGNITUDE - dBm
FREQUENCY – MHz
: chart::>

TPC 1. AD9862 Tx Output 6 MHz
Single Tone; CLKIN = 32 MHz;
DLL 4x Setting

<a id='de53e24b-f0b0-464a-8c09-2e445c5f9ebd'></a>

<::MAGNITUDE - dBm
fDATA = 32MSPS
4X INTERPOLATION
FREQUENCY – MHz
: chart::>

TPC 2. AD9862 Tx Output 6 MHz
Single Tone; CLKIN = 64 MHz;
DLL 2× Setting

<a id='4fbe9c08-ac48-4fa4-bf71-5bf7416d40ae'></a>

MAGNITUDE – dBm
<table id="8-1">
<tr><td id="8-2">O (blurred image)</td><td id="8-3" rowspan="2"></td><td id="8-4"></td><td id="8-5"></td><td id="8-6" rowspan="2"></td><td id="8-7" rowspan="2"></td><td id="8-8" rowspan="2" colspan="4">fDATA = 32MSPS 4× INTERPOLATION</td></tr>
<tr><td id="8-9" rowspan="8">10</td><td id="8-a"></td><td id="8-b"></td></tr>
<tr><td id="8-c"></td><td id="8-d"></td><td id="8-e"></td><td id="8-f"></td><td id="8-g"></td><td id="8-h"></td><td id="8-i"></td><td id="8-j"></td><td id="8-k"></td></tr>
<tr><td id="8-l"></td><td id="8-m"></td><td id="8-n"></td><td id="8-o"></td><td id="8-p"></td><td id="8-q"></td><td id="8-r"></td><td id="8-s"></td><td id="8-t"></td></tr>
<tr><td id="8-u"></td><td id="8-v"></td><td id="8-w"></td><td id="8-x"></td><td id="8-y"></td><td id="8-z"></td><td id="8-A"></td><td id="8-B"></td><td id="8-C"></td></tr>
<tr><td id="8-D"></td><td id="8-E"></td><td id="8-F"></td><td id="8-G"></td><td id="8-H"></td><td id="8-I"></td><td id="8-J"></td><td id="8-K">vertical dark line right</td><td id="8-L"></td></tr>
<tr><td id="8-M"></td><td id="8-N"></td><td id="8-O"></td><td id="8-P"></td><td id="8-Q"></td><td id="8-R"></td><td id="8-S"></td><td id="8-T">vertical dark line right</td><td id="8-U"></td></tr>
<tr><td id="8-V"></td><td id="8-W"></td><td id="8-X"></td><td id="8-Y"></td><td id="8-Z">vertical dark line, shadow right</td><td id="8-10"></td><td id="8-11"></td><td id="8-12">short dark line bottom</td><td id="8-13"></td></tr>
<tr><td id="8-14"></td><td id="8-15"></td><td id="8-16"></td><td id="8-17"></td><td id="8-18">two vertical dark lines, two short</td><td id="8-19">short dark line bottom</td><td id="8-1a">two dark vertical lines, one short</td><td id="8-1b">vertical dark line, shadow bottom</td><td id="8-1c"></td></tr>
<tr><td id="8-1d">100</td><td id="8-1e"></td><td id="8-1f"></td><td id="8-1g"></td><td id="8-1h"></td><td id="8-1i">dark wavy line top, shadow bottom</td><td id="8-1j">dark wavy line top, shadow bottom</td><td id="8-1k">dark wavy line top, shadow bottom</td><td id="8-1l">dark wavy line top, shadow bottom</td><td id="8-1m">dark wavy line top, shadow bottom</td></tr>
</table>
0 20 40 60 80 100 110 120 140
FREQUENCY – MHz
TPC 3. AD9862 Tx Output 6 MHz
Single Tone; CLKIN = 128 MHz;
DLL 1× Setting

<a id='a49e3a16-1ed6-4c2b-9480-21e228731de4'></a>

<::line graph: The graph plots MAGNITUDE (dBm) on the y-axis against FREQUENCY (MHz) on the x-axis. The y-axis ranges from -120 dBm to 0 dBm. The x-axis ranges from 0 MHz to 140 MHz. The graph displays a frequency spectrum with multiple lobes. The first lobe is prominent from approximately 0 MHz to 20 MHz, with magnitudes fluctuating between -40 dBm and -100 dBm. Subsequent lobes appear centered around 40 MHz, 60 MHz, 80 MHz, 100 MHz, and 120 MHz, each showing similar magnitude characteristics. An annotation in the top right corner states: f_DATA = 32MSPS, 1x INTERPOLATION. The caption for the figure is: TPC 4. TxDAC Generating an OFDM Signal; CLKIN = 64 MHz, DLL 2× Setting::>

<a id='de930000-54ee-488a-a8d8-f86c44930385'></a>

<::chart: A line graph with Magnitude (dBm) on the y-axis and Frequency (MHz) on the x-axis. The y-axis ranges from -120 dBm to 0 dBm, with major ticks at 0, -20, -40, -60, -80, -100, and -120. The x-axis ranges from 0 MHz to 140 MHz, with major ticks at 0, 20, 40, 60, 80, 100, 110, 120, and 140. The graph shows a signal with two main peaks, one near 0 MHz reaching approximately -40 dBm, and another smaller peak near 115 MHz reaching approximately -60 dBm. The baseline noise floor is around -100 dBm. Annotations on the graph indicate "f_{DATA} = 32MSPS" and "4x INTERPOLATION". Below the chart is the caption: TPC 5. TxDAC Generating an OFDM Signal; CLKIN = 64 MHz, DLL 2x Setting::>


<a id='11f54669-4c03-45ba-b0b1-46db9126eda0'></a>

<::chart: The chart displays Magnitude (dBm) on the y-axis, ranging from -120 to 0, and Frequency (MHz) on the x-axis, ranging from 7.90 to 8.08. The plot shows four distinct notched carriers of an OFDM signal. The magnitude peaks for these carriers are around -40 dBm, while the noise floor is approximately -105 dBm. An annotation in the top right corner indicates "f_DATA = 32MSPS" and "4× INTERPOLATION". The caption below the chart reads: "TPC 6. Zoomed in Plot of Four Notched Carriers of OFDM Signal; CLKIN = 64 MHz, DLL 2× Setting"::>

<a id='ea3daf05-d3c9-47b0-89b4-f8d1f297b147'></a>

<::chart: Line chart showing THD, 2nd, and 3rd harmonic distortion versus f_OUT.
- Y-axis: THD - dBc, from -90 to -60.
- X-axis: f_OUT - MHz, from 5 to 35.
- Legend:
  - THD (thick line)
  - 2nd (medium line)
  - 3rd (thin line)
- Additional information: f_DATA = 64MSPS, 2x INTERPOLATION.
- Caption: TPC 7. TxDAC Harmonic Distortion vs. f_OUT::>

<a id='b9c2b0a6-1bc7-4e9b-9d5c-4a242b33adda'></a>

<::line chart: TPC 8. Signal-to-Noise Ratio (SNR) vs. fOUT. The x-axis is labeled "FREQUENCY – MHz" and ranges from 0 to 30. The y-axis is labeled "SNR – dB" and ranges from 68 to 74. Two lines are plotted: one labeled "AD9862" and another labeled "AD9860". Additional text within the chart states "fDATA = 64MSPS" and "2× INTERPOLATION".::>

<a id='4e95b849-d658-42d5-b84a-b54439e8e7a2'></a>

<::chart: f_DATA = 64MSPS, 2x INTERPOLATION. Y-axis: IMD - dBc, ranging from -95 to -50. X-axis: CARRIER FREQUENCY - MHz, ranging from 5 to 30. Legend shows three lines: AVDD = 3.0V, AVDD = 3.3V, and AVDD = 3.6V. The chart displays curves showing IMD (dBc) increasing with carrier frequency for different AVDD values.::>
TPC 9. Two Tone Intermodulation vs. f_OUT1 (f_OUT2 = f_OUT1 + 1 MHz)

<a id='f7546c4d-2616-4e05-807c-592347a0d591'></a>

REV. 0

<a id='d824ff16-0ac4-46df-b6d3-87e4fe653977'></a>

-9-

<!-- PAGE BREAK -->

<a id='60e972f3-7ad8-4679-9420-6a95b84a560d'></a>

AD9860/AD9862<::chart: The chart shows an ADC Dual Tone FFT. The y-axis is labeled "FFT MAGNITUDE - dBFS" and ranges from 0 to -120 dBFS. The x-axis is labeled "FFT OUTPUT - MHz" and ranges from 0 to 30 MHz. There are two distinct peaks at approximately 4.5 MHz and 5.5 MHz, indicating the buffer tones. The noise floor is visible below -80 dBFS. TPC 10. ADC Dual Tone FFT with Buffer Tones at 4.5 MHz and 5.5 MHz::> 

<a id='fb624594-c01d-4fed-99b2-4a5156d357f2'></a>

<::chart: TPC 11. ADC Dual Tone FFT without Buffer Tones at 4.5 MHz and 5.5 MHz. The x-axis is labeled "FFT OUTPUT – MHz" and ranges from 0 to 30 MHz. The y-axis is labeled "FFT MAGNITUDE – dBFS" and ranges from -120 to 0 dBFS. The plot displays two prominent peaks at approximately 4.5 MHz and 5.5 MHz, both reaching close to 0 dBFS. The noise floor is visible between -90 dBFS and -100 dBFS across the rest of the spectrum.:>

<a id='bfcc3278-b511-452b-845a-d8914bdac1f4'></a>

<::FFT plot: The x-axis is labeled "FFT OUTPUT – MHz" and ranges from 0 to 30 MHz. The y-axis is labeled "FFT MAGNITUDE – dBFS" and ranges from 0 to -120 dBFS. The plot shows spectral peaks, with two dominant peaks around 5-7 MHz, and several smaller peaks across the frequency range. The noise floor is approximately -90 to -100 dBFS.
TPC 12. ADC Dual Tone FFT (undersampling) without Buffer Tones at 69.5 MHz and 70.5 MHz::>

<a id='663240e4-3fe6-4abb-808c-a63e3b3cff48'></a>

<::chart: The chart shows SINAD (dBc) on the left y-axis, ranging from 50 to 68, versus fIN (MHz) on the x-axis, ranging from 0 to 300. There is also an unlabeled right y-axis ranging from 8.0 to 11.0. Four curves are plotted: 1. "BUFFERED BYPASS 2V INPUT, 1x GAIN", 2. "BUFFERED BYPASS 1V INPUT, 2x GAIN", 3. "BUFFERED 2V INPUT, 1x GAIN", and 4. "BUFFERED 1V INPUT, 2x GAIN". The caption below the chart reads: TPC 13. AD9862 Rx SINAD vs. fIN at 64 MSPS.::>

<a id='c682962c-fc2d-4916-95dc-a7edb97ac3c6'></a>

<::chart: Y-axis: SINAD - dBc: X-axis: f_{IN} - MHz: Legend: - LOW POWER MODE 1, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN - BUFFER BYPASSED, 2V p-p, 1x RxPGA GAIN - LOW POWER MODE 1, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN - BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN: Caption: TPC 14. AD9862 Rx SINAD vs. f_{IN} at 32 MSPS::>

<a id='91fecc79-faff-4af6-b366-8a0f6174b652'></a>

<::chart: A line graph titled "TPC 15. AD9862 Rx SINAD vs. fIN at 16 MSPS" shows SINAD in dBc on the y-axis, ranging from 50 to 70, and fIN in MHz on the x-axis, ranging from 0 to 300. There are four distinct lines representing different operating conditions:
1. LOW POWER MODE 2, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN
2. BUFFER BYPASSED, 2V p-p, 1x RxPGA GAIN
3. LOW POWER MODE 2, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
4. BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
The lines generally show a decreasing trend in SINAD as fIN increases, with variations in slope and starting point based on the operating conditions.::>

<a id='2d3ab388-6310-46b6-8516-7c987f05c69f'></a>

<::chart: Line graph titled "TPC 16. AD9860 Rx SINAD vs. fIN at 64 MSPS". The x-axis is labeled "fIN - MHz" and ranges from 0 to 300. The left y-axis is labeled "SINAD - dBc" and ranges from 44 to 62. The right y-axis is unlabeled and ranges from 7.0 to 10.0. Four lines are plotted, representing different configurations: "BUFFERED BYPASS 1V INPUT, 2x GAIN", "BUFFERED 1V INPUT, 2x GAIN", "BUFFERED 2V INPUT, 1x GAIN", and "BUFFERED BYPASS 2V INPUT, 1x GAIN".::>

<a id='f1b55dac-16b1-4609-8173-37b17417f24c'></a>

<::chart: Line graph titled "TPC 17. AD9860 Rx SINAD vs. fIN at 32 MSPS". The y-axis is labeled "SINAD - dBc" and ranges from 44 to 62. The x-axis is labeled "fIN - MHz" and ranges from 0 to 300. Four lines are plotted:
1. A line labeled "LOW POWER MODE 1, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN" starts near 61 dBc and gradually decreases to approximately 51 dBc at 250 MHz.
2. A line labeled "BUFFER BYPASSED, 2V p-p, 1x RxPGA GAIN" starts near 60 dBc and gradually decreases to approximately 50 dBc at 250 MHz.
3. A line labeled "LOW POWER MODE 1, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN" starts near 58 dBc and sharply decreases to approximately 45 dBc at 150 MHz.
4. A line labeled "BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN" starts near 59 dBc and sharply decreases to approximately 46 dBc at 150 MHz.::>

TPC 17. AD9860 Rx SINAD vs. fIN at 32 MSPS

<a id='cbb5419c-06f0-483c-bb47-42c84e4fa828'></a>

<::chart: XY plot. X-axis: fIN - MHz from 0 to 300. Y-axis: SINAD - dBc from 44 to 62. The chart displays four data series:
- LOW POWER MODE 2, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN
- BUFFER BYPASSED, 2V p-p, 1x RxPGA GAIN
- LOW POWER MODE 2, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
- BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN

TPC 18. AD9860 Rx SINAD vs. fIN at 16 MSPS::>


<a id='599018ed-67f2-4aa2-b542-76ff1412752d'></a>

-10-

<a id='4ab288a1-ec35-4a8e-ac84-d1e79644be75'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='bed6877e-ee41-4ca5-8e50-80727ba96f3c'></a>

AD9860/AD9862

<a id='2ee97d8b-b0db-4c7a-aef1-7b486782f45a'></a>

<::chart: A line graph showing THD (Total Harmonic Distortion) in dBc versus Input Frequency in MHz. The y-axis ranges from -100 to -50 dBc. The x-axis is logarithmic, ranging from 0 to 1000 MHz, with major ticks at 0, 10, 100, and 1000. There are four data series plotted:
- BUFFERED BYPASS 2V INPUT, 1x GAIN
- BUFFERED 2V INPUT, 1x GAIN
- BUFFERED 1V INPUT, 2x GAIN
- BUFFERED BYPASS 1V INPUT, 2x GAIN
TPC 19. Rx THD vs. f_IN, F_ADC = 64 MSPS::>

<a id='ba7b2187-7035-4dba-afa1-b69fa8cf4784'></a>

<::chart: A line graph titled "Rx THD vs. fIN" with the X-axis labeled "fIN - MHz" ranging from 0 to 300, and the Y-axis labeled "THD - dBc" ranging from -90 to -50. Four curves are plotted, each representing different operating conditions:
1. AD9860 LOW POWER MODE 1, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
2. AD9862 LOW POWER MODE 1, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
3. AD9860 LOW POWER MODE 1, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN
4. AD9862 LOW POWER MODE 1, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN

TPC 20. Rx THD vs. fIN,
FADC = 32 MSPS::>

<a id='ebfaf258-8ca9-47ca-9c1a-bc77fccf386d'></a>

<::line chart with x-axis labeled "f_{IN} - MHz" ranging from 0 to 300, and y-axis labeled "THD - dBc" ranging from -90 to -50. There are four lines plotted with the following legends: AD9860 LOW POWER MODE 2, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN; AD9862 LOW POWER MODE 2, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN; AD9860 LOW POWER MODE 2, BUFFER BYPASSED, 2Vp-p INPUT, 1x RxPGA GAIN; AD9862 LOW POWER MODE 2, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN. The caption for the chart is: TPC 21. Rx THD vs. f_{IN}, F_{ADC} = 16 MSPS.: chart::>

<a id='a08cdba5-0d78-46b5-b19e-9e42a50cec44'></a>

<::A line chart showing SFDR (dBc) versus Input Frequency (MHz). The y-axis ranges from -100 to -50 in increments of 5 dBc. The x-axis is a logarithmic scale from 0 to 1000 MHz. There are four data series plotted:
- BUFFERED BYPASS, 1V INPUT, 2x GAIN
- BUFFERED BYPASS, 2V INPUT, 1x GAIN
- BUFFERED 2V INPUT, 1x GAIN
- BUFFERED 1V INPUT, 2x GAIN

TPC 22. Rx SFDR @ 64 MSPS
: chart::>

<a id='563c7875-7433-4a6d-9aa3-5ec663690354'></a>

<:: chart: A line graph with SFDR - dBc on the Y-axis, ranging from -95 to -50, and f_IN - MHz on the X-axis, ranging from 0 to 300. The graph displays four lines representing different configurations:
- AD9862 LOW POWER MODE 1, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
- AD9860 LOW POWER MODE 1, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN
- AD9860 LOW POWER MODE 1, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN
- AD9862 LOW POWER MODE 1, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN
Caption: TPC 23. Rx SFDR @ 32 MSPS
::>

<a id='776e5c59-3d55-44da-8e2a-a63252e3c99a'></a>

<::chart::>A line graph titled "TPC 24. Rx SFDR @ 16 MSPS" shows SFDR (dBc) on the y-axis and fIN (MHz) on the x-axis.The y-axis ranges from -95 dBc to -50 dBc.The x-axis ranges from 0 MHz to 300 MHz.The graph contains four curves, each representing different operating conditions:1. AD9860 LOW POWER MODE 2, BUFFER BYPASSED, 1V p-p INPUT, 2x RxPGA GAIN2. AD9860 LOW POWER MODE 2, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN3. AD9862 LOW POWER MODE 2, BUFFER BYPASSED, 2V p-p INPUT, 1x RxPGA GAIN4. AD9862 LOW POWER MODE 2, BUFFER ENABLED, 1V p-p INPUT, 2x RxPGA GAIN<::>

<a id='adefa7c4-7f9a-453f-b08d-925dfb778b56'></a>

<::chart: A line graph titled "TPC 25. Rx Input Attenuation" plots Relative Attenuation (dB) on the y-axis against Input Frequency (MHz) on the x-axis. The x-axis is logarithmic, ranging from 1 MHz to 1000 MHz. The y-axis is linear, ranging from -6 dB to 1 dB. Three lines are plotted:
- NO BUFF 2V x1 (thick dark line): Shows relatively flat response near 0 dB up to approximately 100 MHz, then drops sharply.
- BUFF 1V x2 (medium dark line): Shows attenuation starting around 30-50 MHz, dropping to about -3 dB by 100 MHz.
- BUFF 2V x1 (thin light line): Shows similar attenuation characteristics to "BUFF 1V x2", also dropping to about -3 dB by 100 MHz.::>

<a id='341e5da4-253a-4a8a-bc08-1c40d8f4bbc7'></a>

<::line chart: TPC 26. Rx Input Buffer Impedance vs. fIN. The x-axis is labeled "fIN – MHz" and ranges from 0 to 100. The y-axis is labeled "INPUT IMPEDANCE – Ω" and ranges from 180 to 280. The line plot shows input impedance starting at approximately 230 Ω at 0 MHz, decreasing to a minimum of approximately 222 Ω around 55 MHz, and then increasing to approximately 255 Ω at 100 MHz.::>

<a id='6c741c5c-980c-4a70-ab22-8728fb65dc36'></a>

<::line chart showing Rx Analog Power versus fADC::>Rx ANALOG POWER - mW on the y-axis, fADC - MSPS on the x-axis. Three lines are plotted:
- 16MSPS LP MODE: Starts around 180 mW at 0 MSPS, increases to approximately 220 mW at 15 MSPS.
- 32MSPS LP MODE: Starts around 400 mW at 20 MSPS, increases to approximately 430 mW at 30 MSPS.
- NOMINAL: Starts around 620 mW at 35 MSPS, increases to approximately 700 mW at 65 MSPS.
TPC 27. Rx Analog Power Consumption<::chart::>

<a id='3a868652-70fd-4e53-8a3a-650ae5db3c7f'></a>

REV. 0

<a id='7d921959-c2ce-471d-8f7c-3844a23147df'></a>

-11-

<!-- PAGE BREAK -->

<a id='3c8d3b52-ed76-48c5-9201-6a7794534859'></a>

AD9860/AD9862

<a id='63239eed-9311-420d-b500-6af0a986235e'></a>

REGISTER MAP (0x00–0x3F)¹
<table id="11-1">
<tr><td id="11-2">Register Name</td><td id="11-3">Address²</td><td id="11-4">Bit 7</td><td id="11-5">Bit 6</td><td id="11-6">Bit 5</td><td id="11-7">Bit 4</td><td id="11-8">Bit 3</td><td id="11-9">Bit 2</td><td id="11-a">Bit 1</td><td id="11-b">Bit 0</td><td id="11-c">Purpose</td></tr>
<tr><td id="11-d">General</td><td id="11-e">0</td><td id="11-f">SDIO BiDir</td><td id="11-g">LSB First</td><td id="11-h">Soft Reset</td><td id="11-i"></td><td id="11-j"></td><td id="11-k"></td><td id="11-l"></td><td id="11-m"></td><td id="11-n">SPI Setup</td></tr>
<tr><td id="11-o">Rx Power Down</td><td id="11-p">1</td><td id="11-q">VREF (diff)</td><td id="11-r">VREF</td><td id="11-s">Rx Digital</td><td id="11-t">Rx Channel B</td><td id="11-u">Rx Channel A</td><td id="11-v">Buffer B</td><td id="11-w">Buffer A</td><td id="11-x">All Rx</td><td id="11-y" rowspan="6">Receive Path Setup</td></tr>
<tr><td id="11-z">Rx A</td><td id="11-A">2</td><td id="11-B">Byp Buffer A</td><td id="11-C"></td><td id="11-D"></td><td id="11-E" colspan="5">RxPGA A</td></tr>
<tr><td id="11-F">Rx B</td><td id="11-G">3</td><td id="11-H">Byp Buffer B</td><td id="11-I"></td><td id="11-J"></td><td id="11-K" colspan="5">RxPGA B</td></tr>
<tr><td id="11-L">Rx Misc</td><td id="11-M">4</td><td id="11-N"></td><td id="11-O"></td><td id="11-P"></td><td id="11-Q"></td><td id="11-R"></td><td id="11-S">HS Duty Cycle</td><td id="11-T">Shared Ref</td><td id="11-U">Clk Duty</td></tr>
<tr><td id="11-V">Rx I/F</td><td id="11-W">5</td><td id="11-X"></td><td id="11-Y"></td><td id="11-Z"></td><td id="11-10">Three State</td><td id="11-11">Rx Retime</td><td id="11-12">Twos Complement</td><td id="11-13">Inv RxSync</td><td id="11-14">Mux Out</td></tr>
<tr><td id="11-15">Rx Digital</td><td id="11-16">6</td><td id="11-17"></td><td id="11-18"></td><td id="11-19"></td><td id="11-1a"></td><td id="11-1b">2 Channel</td><td id="11-1c">Keep -ve</td><td id="11-1d">Hilbert</td><td id="11-1e">Decimate</td></tr>
<tr><td id="11-1f">RSV</td><td id="11-1g">7</td><td id="11-1h" colspan="8">Reserved for Future Use</td><td id="11-1i" rowspan="14">Transmit Path Setup</td></tr>
<tr><td id="11-1j">Tx Power Down</td><td id="11-1k">8</td><td id="11-1l"></td><td id="11-1m"></td><td id="11-1n">Alt Timing Mode</td><td id="11-1o">TxOff Enable</td><td id="11-1p">Tx Digital</td><td id="11-1q" colspan="3">Tx Analog Power Down [2:0]</td></tr>
<tr><td id="11-1r">RSV</td><td id="11-1s">9</td><td id="11-1t" colspan="8">Reserved for Future Use</td></tr>
<tr><td id="11-1u">Tx A Offset</td><td id="11-1v">10</td><td id="11-1w" colspan="2">DAC A Offset [1:0]</td><td id="11-1x"></td><td id="11-1y"></td><td id="11-1z"></td><td id="11-1A"></td><td id="11-1B"></td><td id="11-1C">DAC A Offset Direction</td></tr>
<tr><td id="11-1D">Tx A Offset</td><td id="11-1E">11</td><td id="11-1F" colspan="8">DAC A Offset [9:2]</td></tr>
<tr><td id="11-1G">Tx B Offset</td><td id="11-1H">12</td><td id="11-1I" colspan="2">DAC B Offset [1:0]</td><td id="11-1J"></td><td id="11-1K"></td><td id="11-1L"></td><td id="11-1M"></td><td id="11-1N"></td><td id="11-1O">DAC B Offset Direction</td></tr>
<tr><td id="11-1P">Tx B Offset</td><td id="11-1Q">13</td><td id="11-1R" colspan="8">DAC B Offset [9:2]</td></tr>
<tr><td id="11-1S">Tx A Gain</td><td id="11-1T">14</td><td id="11-1U" colspan="2">DAC A Coarse Gain</td><td id="11-1V" colspan="6">DAC A Fine Gain</td></tr>
<tr><td id="11-1W">Tx B Gain</td><td id="11-1X">15</td><td id="11-1Y" colspan="2">DAC B Coarse Gain</td><td id="11-1Z" colspan="6">DAC B Fine Gain</td></tr>
<tr><td id="11-20">Tx PGA Gain</td><td id="11-21">16</td><td id="11-22" colspan="8">Tx PGA Gain</td></tr>
<tr><td id="11-23">Tx Misc</td><td id="11-24">17</td><td id="11-25"></td><td id="11-26"></td><td id="11-27"></td><td id="11-28"></td><td id="11-29"></td><td id="11-2a"></td><td id="11-2b">Slave Enable</td><td id="11-2c">Tx PGA Fast</td></tr>
<tr><td id="11-2d">Tx I/F</td><td id="11-2e">18</td><td id="11-2f"></td><td id="11-2g">Tx Retime</td><td id="11-2h">Q/I Order</td><td id="11-2i">Inv TxSync</td><td id="11-2j">Twos Complement</td><td id="11-2k">Inverse Sample</td><td id="11-2l">2 Edges</td><td id="11-2m">Interleaved</td></tr>
<tr><td id="11-2n">Tx Digital</td><td id="11-2o">19</td><td id="11-2p"></td><td id="11-2q"></td><td id="11-2r"></td><td id="11-2s">2 Data Paths</td><td id="11-2t">Keep -ve</td><td id="11-2u">Hilbert</td><td id="11-2v" colspan="2">Interpolation Control</td></tr>
<tr><td id="11-2w">Tx Modulator</td><td id="11-2x">20</td><td id="11-2y"></td><td id="11-2z"></td><td id="11-2A">Neg. Fine Tune</td><td id="11-2B">Fine Mode</td><td id="11-2C">Real Mix</td><td id="11-2D">Neg. Coarse Tune</td><td id="11-2E" colspan="2">Coarse Modulation</td></tr>
<tr><td id="11-2F">NCO Tuning Word</td><td id="11-2G">21</td><td id="11-2H" colspan="8">FTW [7:0]</td><td id="11-2I" rowspan="3">NCO Setup</td></tr>
<tr><td id="11-2J">NCO Tuning Word</td><td id="11-2K">22</td><td id="11-2L" colspan="8">FTW [15:8]</td></tr>
<tr><td id="11-2M">NCO Tuning Word</td><td id="11-2N">23</td><td id="11-2O" colspan="8">FTW [23:16]</td></tr>
<tr><td id="11-2P">DLL</td><td id="11-2Q">24</td><td id="11-2R">Reserved</td><td id="11-2S">Input Control Clock</td><td id="11-2T">ADC Div 2</td><td id="11-2U" colspan="2">DLL Multiplier</td><td id="11-2V">DLL Power Down</td><td id="11-2W"></td><td id="11-2X">DLL FAST</td><td id="11-2Y" rowspan="2">Clock Setup</td></tr>
<tr><td id="11-2Z">CLKOUT</td><td id="11-30">25</td><td id="11-31" colspan="2">CLKOUT2 Divide Factor</td><td id="11-32">Inv2</td><td id="11-33">Dis2</td><td id="11-34"></td><td id="11-35"></td><td id="11-36">Inv1</td><td id="11-37">Dis 1</td></tr>
<tr><td id="11-38">Aux ADC A2</td><td id="11-39">26</td><td id="11-3a" colspan="2">Aux ADC A2 Data [1:0]</td><td id="11-3b"></td><td id="11-3c"></td><td id="11-3d"></td><td id="11-3e"></td><td id="11-3f" colspan="2"></td><td id="11-3g" rowspan="10">Auxiliary ADC Data and Setup</td></tr>
<tr><td id="11-3h">Aux ADC A2</td><td id="11-3i">27</td><td id="11-3j" colspan="8">Aux ADC A2 Data [9:2]</td></tr>
<tr><td id="11-3k">Aux ADC A1</td><td id="11-3l">28</td><td id="11-3m" colspan="2">Aux ADC A1 Data [1:0]</td><td id="11-3n"></td><td id="11-3o"></td><td id="11-3p"></td><td id="11-3q"></td><td id="11-3r"></td><td id="11-3s"></td></tr>
<tr><td id="11-3t">Aux ADC A1</td><td id="11-3u">29</td><td id="11-3v" colspan="8">Aux ADC A1 Data [9:2]</td></tr>
<tr><td id="11-3w">Aux ADC B2</td><td id="11-3x">30</td><td id="11-3y" colspan="2">Aux ADC B2 Data [1:0]</td><td id="11-3z"></td><td id="11-3A"></td><td id="11-3B"></td><td id="11-3C"></td><td id="11-3D"></td><td id="11-3E"></td></tr>
<tr><td id="11-3F">Aux ADC B2</td><td id="11-3G">31</td><td id="11-3H" colspan="8">Aux ADC B2 Data [9:2]</td></tr>
<tr><td id="11-3I">Aux ADC B1</td><td id="11-3J">32</td><td id="11-3K" colspan="2">Aux ADC B1 Data [1:0]</td><td id="11-3L"></td><td id="11-3M"></td><td id="11-3N"></td><td id="11-3O"></td><td id="11-3P"></td><td id="11-3Q"></td></tr>
<tr><td id="11-3R">Aux ADC B1</td><td id="11-3S">33</td><td id="11-3T" colspan="8">Aux ADC B1 Data [9:2]</td></tr>
<tr><td id="11-3U">Aux ADC Control</td><td id="11-3V">34</td><td id="11-3W">Aux SPI</td><td id="11-3X">SelBnot A</td><td id="11-3Y">Refsel B</td><td id="11-3Z">Select B</td><td id="11-40">Start B</td><td id="11-41">Refsel A</td><td id="11-42">Select A</td><td id="11-43">Start A</td></tr>
<tr><td id="11-44">Aux ADC Clock</td><td id="11-45">35</td><td id="11-46"></td><td id="11-47"></td><td id="11-48"></td><td id="11-49"></td><td id="11-4a"></td><td id="11-4b"></td><td id="11-4c"></td><td id="11-4d">CLK/4</td></tr>
<tr><td id="11-4e">Aux DAC A</td><td id="11-4f">36</td><td id="11-4g" colspan="8">Aux DAC A</td><td id="11-4h" rowspan="6">Auxiliary DAC Data and Setup</td></tr>
<tr><td id="11-4i">Aux DAC B</td><td id="11-4j">37</td><td id="11-4k" colspan="8">Aux DAC B</td></tr>
<tr><td id="11-4l">Aux DAC C</td><td id="11-4m">38</td><td id="11-4n" colspan="8">Aux DAC C</td></tr>
<tr><td id="11-4o">Aux DAC</td><td id="11-4p">39</td><td id="11-4q" colspan="2">Slave Enable</td><td id="11-4r"></td><td id="11-4s"></td><td id="11-4t"></td><td id="11-4u">Update C</td><td id="11-4v">Update B</td><td id="11-4w">Update A</td></tr>
<tr><td id="11-4x">Update Aux DAC</td><td id="11-4y">40</td><td id="11-4z"></td><td id="11-4A"></td><td id="11-4B"></td><td id="11-4C"></td><td id="11-4D"></td><td id="11-4E">Power Down C</td><td id="11-4F">Power Down B</td><td id="11-4G">Power Down A</td></tr>
<tr><td id="11-4H">DAC Control</td><td id="11-4I">41</td><td id="11-4J"></td><td id="11-4K"></td><td id="11-4L"></td><td id="11-4M">Inv C</td><td id="11-4N"></td><td id="11-4O">Inv B</td><td id="11-4P"></td><td id="11-4Q">Inv A</td></tr>
<tr><td id="11-4R">SigDelt</td><td id="11-4S">42</td><td id="11-4T" colspan="4">Sigma-Delta Control Word [3:0]</td><td id="11-4U"></td><td id="11-4V"></td><td id="11-4W"></td><td id="11-4X">Flag</td><td id="11-4Y" rowspan="2">Sigma-Delta Data and Setup</td></tr>
<tr><td id="11-4Z">SigDelt</td><td id="11-50">43</td><td id="11-51" colspan="8">Sigma-Delta Control Word [11:4]</td></tr>
<tr><td id="11-52">ADC Low Power</td><td id="11-53">49, 50</td><td id="11-54" colspan="8">Low Power Register for Rx Path Operation below 32 MSPS</td><td id="11-55" rowspan="2">Rx Low Power</td></tr>
<tr><td id="11-56" rowspan="2">RSV</td><td id="11-57" rowspan="2">44–62</td><td id="11-58" rowspan="2" colspan="8">Reserved for Future Use</td></tr>
<tr><td id="11-59">Reserved</td></tr>
<tr><td id="11-5a"></td><td id="11-5b">63</td><td id="11-5c" colspan="8">Chip Rev ID</td><td id="11-5d">Chip ID</td></tr>
</table>

<a id='7abae037-adc1-415b-8e49-4658a403ae5a'></a>

NOTES
1 When writing to a register with unassigned register bit(s), a logic low must be written to the unassigned bit(s). By default, after power up or RESET, all registers are set low, except for the bits in the shaded boxes, which are set high.
2 Decimal

<a id='bc63c3a1-b0b2-4d70-8f0b-3c3e4a324b37'></a>

-12-

<a id='5afb9712-8ee7-4731-9dc5-65795530f349'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='e54a49c8-4ecc-4b89-88fa-1f2cad022b5b'></a>

AD9860/AD9862

<a id='8a281645-37c7-4b9d-93ba-b4b3d2784585'></a>

REGISTER BIT DEFINITIONS
REGISTER 0: GENERAL

<a id='301e7be7-64cb-471f-8128-a41ee39e93ea'></a>

**BIT 7: SDIO BiDir (Bidirectional)**
Default setting is low, which indicates SPI serial port uses dedicated input and output lines (i.e., 4-wire interface), SDIO and SDO Pins, respectively. Setting this bit high configures the serial port to use the SDIO Pin as a bidirectional data pin.

<a id='9e679741-72c6-4baa-9132-cc027f7b8dd4'></a>

**BIT 6: LSB First**
Default setting is low, which indicates MSB first SPI Port Access
Mode. Setting this bit high configures the SPI port access to
LSB first mode.

<a id='b90105a3-1449-4133-8d4a-c7bfe9b16a1d'></a>

**BIT 5: Soft Reset**
Writing a high to this register resets all the registers to their default values and forces the DLL to relock to the input clock. The Soft Reset Bit is a one shot register and is cleared immediately after the register write is completed.

<a id='406abcda-d272-406e-a542-a3f59ccfc9c4'></a>

**REGISTER 1: Rx PWRDWN**
**BIT 7: VREF, diff (Power-Down)**
Setting this bit high will power down the ADC's differential
references (i.e., REFT and REFB).

<a id='f197e1f8-fcbb-47fb-8067-d2142700e196'></a>

**BIT 6: VREF (Power-Down)**
Setting this register bit high will power down the ADC reference circuit (i.e., VREF).

<a id='8d5a3dd2-047b-4343-b87f-d550b3d425e0'></a>

**BIT 5: Rx Digital (Power-Down)**
Setting this bit high will power down the digital section of the
receive path of the chip. Typically, any unused digital blocks are
automatically powered down.

<a id='bb7dc2a3-eb49-42b9-94cc-2470933ab11d'></a>

BIT 4/3: Rx Channel B/Rx Channel A (Power-Down)
Either ADC or both ADCs can be powered down by setting the appropriate register bit high. The entire Rx channel is powered down, including the differential references, input buffer, and the internal digital block. The bandgap reference remains active for quick recovery.

<a id='c4e2b612-97d1-43dd-ae88-6d10416f8a80'></a>

**BIT 2/1: Buffer B/Buffer A (Power-Down)**
Setting either of these bits high will power down the input buffer
circuits for the respective channel. The input buffer should be
powered down when bypassed. By default, these bits are low and
the input buffers are enabled.

<a id='b33a7bed-a93a-4719-92f3-ffb9162dbe3c'></a>

BIT 0: All Rx (Power-Down)
Setting this bit high powers down all circuits related to the receive path.

<a id='8a976f26-049b-4bdc-87bd-fba305aeb362'></a>

**REGISTER 2/3: Rx A/Rx B**
**BIT 7: Bypass Buffer A/Bypass Buffer B**
Setting either of these bits high will bypass the respective input buffer circuit. When the buffer is bypassed, the input signal is routed directly to the switched capacitor SHA input of the RxPGA. When operating with buffer bypassed, it should be powered down.

<a id='46c2e5ec-1b6a-4554-baff-da9def4648c1'></a>

BIT 0–4: RxPGA A/RxPGA B
These 5-bit straight binary registers (Bit 0 is the LSB, Bit 4 is the MSB) provide control for the programmable gain amplifiers in the dual receive paths. A 0 dB to 20 dB gain range is accomplished through a switched capacitor network with fast settling of a few clock cycles. The step size is approximately 1 dB. The register default setting is minimum gain or hex00. The maximum setting for these registers is hex14.

<a id='24455a63-f960-4c1e-b792-eed659e8a981'></a>

REGISTER 4: Rx MISC
BIT 2: HS (High Speed) Duty Cycle
Setting this bit high optimizes duty cycle of the internal ADC
sampling clock. It is recommended that this bit be set high in

<a id='ee23547d-205b-4e96-99ea-c7233adaad72'></a>

high speed applications when clock duty cycle affects noise and distortion performance the most. This bit should be set high in conjunction with Clk Dut Enable register bit.

<a id='a5fe14d5-e25c-478c-8b5c-60b47d12c170'></a>

**BIT 1: Shared Ref**
Setting this bit high forces the dual receive ADCs into a mode
to share their differential references to provide superior gain
matching. When this option is enabled, the REFT of Channel A
and Channel B should be connected together off-chip and the
REFB of both channels should be connected.

<a id='c300f610-5f73-419d-93cb-484329b1a97c'></a>

**BIT 0: Clk Duty**
Setting this bit high enables an on-chip duty cycle stabilizer (DCS) circuit to generate the internal clock for the Rx block. This option is useful for adjusting for high speed input clocks with skewed duty cycle. The DCS Mode can be used with ADC sampling frequencies over 40 MHz.

<a id='f491772d-79fa-4f79-bc8e-8c747c941c92'></a>

REGISTER 5: Rx I/F (INTERFACE)
BIT 4: Three-state
Setting this bit high will force both Rx data output buses, including
the RxSYNC Pin, into a three-state mode.

<a id='9f8347e2-768c-4d74-bdd5-1e3acf653633'></a>

**BIT 3: Rx Retime**
The Rx path can use either of the clock outputs, CLKOUT1 or CLKOUT2, to latch the Rx output data. Since CLKOUT1 and CLKOUT2 have slight phase offsets, this provides some timing flexibility with the interface. By default, this bit is low and the Rx output latches use CLKOUT1. Setting this bit will force the Rx output latches to use CLKOUT2.

<a id='1d20b108-9243-4d60-a3d5-693a61e95715'></a>

BIT 2: Twos Complement
Default data format for the Rx data is straight binary. Setting this
bit high will generate two's complement data.

<a id='8b6df124-01d4-42b8-a60b-ed9cd1f0c125'></a>

**BIT 1: Inv RxSync**
When the receive data is multiplexed onto one data port (i.e., Mux Mode Enabled), the RxSYNC Pin can be used to decode which channel generated the current output data at the active port. Default condition is that RxSYNC is high when Channel A is at the output and is low when Channel B is at the output. Setting this bit high reverses this synchronization.

<a id='343e0df9-85c0-4198-b9b0-6244fd31728a'></a>

**BIT 0: Mux Out**
Setting this bit high enables the Rx Mux Mode. Default setting is low, which is Dual Port Mode, (i.e., non Rx Mux Mode). When in Rx Mux Mode, both Rx channels share the same output data bus, pins D0A to D9A (for AD9860) or D0A to D11A (for AD9862). The other Rx output bus (pins D0B to D9B or D0B to D11B) outputs a low logic.

<a id='c2a58723-de43-4e5a-aed8-ecd18445c340'></a>

**REGISTER 6: Rx Digital**
**BIT 3: 2 Channel**
Setting this bit low disables the Rx B output data port (pins D0B to D9B or D11B), forcing the output pins to zero. By default, the bit is high and both data paths are active.

<a id='289775c7-e21f-4218-abc0-f58055b8ca75'></a>

**BIT 2: Keep –ve**
This bit selects whether the receive Hilbert filter will filter positive or negative frequencies, assuming the filter is enabled. By default this bit is low, which passes positive frequencies. Setting this bit high will configure the filter to pass negative frequencies.

<a id='c1d38e18-a1ca-4e04-879f-455d62e2d96c'></a>

**BIT 1: Hilbert**
This bit enables or disables the Hilbert filter in the receive path.
By default, this bit is low, which disables the receive Hilbert filter.
Setting this bit high enables the receive Hilbert filter.

<a id='e966a5d5-88f6-4417-b82b-8420b0d91158'></a>

**BIT 0: Decimate**
This register enables or disables the decimation filters. By default,
the register setting is low and the decimation filter is disabled.

<a id='b5cb3c27-0646-43f2-9772-54923d2637b3'></a>

REV. 0

<a id='4516fc44-fc76-4ecb-a4e6-96632e183101'></a>

-13-

<!-- PAGE BREAK -->

<a id='5f6947b5-ed24-47e1-9ee2-72cbc0c06272'></a>

AD9860/AD9862

Setting this bit high enables the decimation filters and decimates the receive data by two.

<a id='f02fd079-5f9e-4990-8a62-617ec19c7130'></a>

## REGISTER 8: Tx PWRDWN
### BIT 5: Alt Timing Mode
The timing section in the data sheet describes two timing modes, the "Normal Operation" and the "Alternate Operation" modes. At power up, the default configuration is established from the logic level of the Mode/TxBlank pin. If Mode/TxBlank is logic low, the Normal Operation mode is the default; if the Mode/ TxBlank pin is held at a logic high, the Alternative Operation mode is configured at power-up (the DLL is forced to multiply by 4 at power-up by default in this mode). After power up, the operation mode can be configured so that the Mode/TxBlank pin can be used for other functions. To allow this, set this bit high.

<a id='bdf95058-8438-43f3-ad9c-3f658465ac0e'></a>

**BIT 4: TxOff Enable**
By default, the Mode/TxBlank pin is not used for any transmit synchronization. The Mode/TxBlank pin input can be used to serve two functions, blanking the DAC outputs and slaving the TxPGA gain control. When this bit is set high, a logic high on the Mode/TxBlank pin forces the Tx digital block to stop clocking. In this mode, the Tx outputs will be static, holding their last update values. To slave the TxPGA gain control to the Mode/TxBlank pin input, register Slave Enable (Register 17, Bit 1) needs to also be programmed. See that register for more information.

<a id='43fd0aaf-2531-4cf6-98e9-0eb9f4fa2a43'></a>

**BIT 3: Tx Digital (Power-Down)**
By default this bit is low, enabling the transmit path digital to operate as programmed through other registers. By setting this bit high, the digital blocks are not clocked to reduce power consumption. When enabled, the Tx outputs will be static, holding their last update values.

<a id='bb625de3-5ce6-4bc3-8b5e-6451486324b3'></a>

BIT 0-2: Tx Analog (Power-Down)
Three options are available to reduce analog power consumption for the Tx channels. The first two options disable the analog output from Tx channel A or B independently, and the third option disables the output of both channels and reduces the power consumption of some of the additional analog support circuitry for maximum power savings. With all three options, the DAC bias current is not powered down so recovery times are fast (typically a few clock cycles). The list below explains the different modes and settings used to configure them.

<a id='6dfa8035-db81-4890-bb53-eaf6ed99fead'></a>

**Power-Down Option**

Tx Analog Power-Down Bits Setting [2:0]

Power-Down Tx B Channel Analog Output [1 0 0]
Power-Down Tx A Channel Analog Output [0 1 0]
Power-Down Tx A and Tx B Analog Outputs [1 1 1]

<a id='3bd048ed-620e-4241-8b4d-2153376550b2'></a>

REGISTER 10/11/12/13: DAC OFFSET A/B
DAC A/DAC B Offset
These 10-bit, twos complement registers control a dc current
offset that is combined with the Tx A or Tx B output signal. An
offset current of up to 12% I₀₅₄₃ (2.4 mA for a 20 mA full-
scale output) can be applied to either differential pin on each
channel. The offset current can be used to compensate for offsets
that are present in an external mixer stage, reducing LO leakage
at its output. Default setting is hex00, no offset current. The
offset current magnitude is set using the lower nine bits. Setting
the MSB high will add the offset current to the selected differen-
tial pin, while an MSB low setting will subtract the offset value.

<a id='533b517a-dfe1-477e-9d37-41de5381a1a9'></a>

**DAC A/DAC B Offset Direction**
This bit determines to which of the differential output pins for the selected channel the offset current will be applied. Setting this bit low will apply the offset to the negative differential pin. Setting this bit high will apply the offset to the positive differential pin.

<a id='89b10c57-b298-4a9c-917e-3f61d327bb0e'></a>

REGISTER 14/15: DAC GAIN A/B
BIT 6, 7: DAC A/DAC B Coarse Gain Control
These register bits will scale the full-scale output current (IOUTFS)
of either Tx channel independently. IOUT of the Tx channels is a
function of the RSET resistor, the TxPGA setting, and the Coarse
Gain Control setting.

<a id='e9716d2c-f40f-4afd-8445-0ea87ff2a287'></a>

<table><thead><tr><th>MSB, LSB</th><th>Tx Channel Current Scaling</th></tr></thead><tbody><tr><td>10 or 11</td><td>Does not scale output current</td></tr><tr><td>01</td><td>Scales output current by 1/2</td></tr><tr><td>00</td><td>Scales output current by 1/11</td></tr></tbody></table>

<a id='48a44ba5-9130-4733-b23b-23d9af1bf09c'></a>

**BIT 5–0: DAC A/DAC B Fine Gain**
The DAC output curve can be adjusted fractionally through the Gain Trim Control. Gain trim of up to \u00b14% can be achieved on each channel individually. The Gain Trim register bits are a twos complement attention control word.

<a id='d439b31d-ad7e-471b-8c53-b24574514b9f'></a>

<table><thead><tr><th>MSB, LSB</th><th>Description</th></tr></thead><tbody><tr><td>100000</td><td>Maximum positive gain adjustment</td></tr><tr><td>111111</td><td>Minimum positive gain adjustment</td></tr><tr><td>000000</td><td>No adjustment (default)</td></tr><tr><td>000001</td><td>Minimum negative gain adjustment</td></tr><tr><td>011111</td><td>Maximum negative gain adjustment</td></tr></tbody></table>

<a id='bb77b4df-99ee-41c5-9679-48836246f96c'></a>

**REGISTER 16: TxPGA GAIN**
**BIT 0–7: TxPGA Gain**
This 8 bit, straight binary (Bit 0 is the LSB, Bit 7 is the MSB) register controls for the Tx programmable gain amplifier (TxPGA). The TxPGA provides a 20 dB continuous gain range with 0.1 dB steps (linear in dB) simultaneously to both Tx channels. By default, this register setting is hex00.

<a id='5093460d-2e6f-4e44-bce7-7132f1e88f68'></a>

MSB, LSB

000000 Minimum gain scaling -20 dB
111111 Maximum gain scaling 0 dB

<a id='2fe4ba36-7eea-490f-8e15-e6c32f284ee5'></a>

REGISTER 17: Tx MISC
BIT 1: Slave Enable
The TxPGA Gain is controlled through register TxPGA Gain
setting and by default is updated immediately after the register
write. If this bit is set, the TxPGA Gain update is synchronized
with the rising edge of a signal applied to the Mode/TxBlank
pin. Setting TxOff enable in Register 8 is also required.

<a id='c457cb18-38a3-4b36-8b17-1f064dc78559'></a>

**BIT 0: TxPGA Fast (Update Mode)**
The TxPGA Fast bit controls the update speed of the TxPGA.
When Fast Update mode is enabled, the TxPGA provides fast gain
settling within a few clock cycles. Default setting for this bit
is low, which indicates Normal Update mode. Fast mode is
enabled when this bit is set high.

<a id='658753cd-c305-4627-9600-4edf8dd5aa8d'></a>

**REGISTER 18: Tx IF (INTERFACE)**
**BIT 6: Tx Retime**
The Tx path can use either of the clock outputs, CLKOUT1 or CLKOUT2, to latch the Tx input data. Since CLKOUT1 and CLKOUT2 have slight phase offsets, this provides some timing flexibility with the interface. By default, this bit is high and the Tx input latches use CLKOUT1. Setting this bit low will force the Tx latches to use CLKOUT2.

<a id='56a27634-044a-4383-b62c-b2f34375da20'></a>

-14-

<a id='8e5f7296-49cd-451e-acd2-033d07edf486'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='f3ed6536-ce46-410c-b01c-0f62e3b0afe5'></a>

AD9860/AD9862

<a id='71746118-aa62-480b-bf1b-a6111a32e450'></a>

**BIT 5: Q/I Order**
This register indicates the order of received complex transmit
data. By default this bit is low, representing I data preceding
Q data. Alternatively, if this bit is set high, the data format is
defined as Q data preceding I data.

<a id='56c164ea-f8c8-4f9e-becb-ee945c26ab68'></a>

BIT 4: Inv TxSync
This register identifies how the first and second data sets are identified in a complex data set using the TxSYNC bit. By default this bit is low, and TxSYNC low indicates the first data set is at the Tx port; TxSYNC high indicates the second data set is at the Tx port. Setting this bit high inverts the TxSYNC bit. TxSYNC high indicates the first of the data set, and TxSYNC low indicates the second of the data set.

<a id='c41bb38b-f9f4-4fe3-8da4-d73494e2d155'></a>

BIT 3: Twos Complement
The default data format for Tx data is straight binary. Set this bit high when providing twos complement Tx data.

<a id='1aa08c49-30da-4f23-a8d4-8d00f4d14d4b'></a>

**BIT 2: Inverse Sample**
By default, the transmit data is sampled on the rising edge of the
CLKOUT. Setting this bit high will change this, and the transmit
data will be sampled on the falling edge.

<a id='15e590f3-86e0-4d78-88ac-cb3c65400723'></a>

**BIT 1: 2 Edges**
If the CLKOUT rate is running at half the interleaved data rate, both edges of the CLKOUT must latch transmit data. Setting this bit high allows this clocking configuration.

<a id='d40d3a05-945d-483c-b614-c5e600f78967'></a>

**BIT 0: Interleaved**
By default, the AD9860/AD9862 powers up in single DAC
operation. If dual transmit data is to be used, the interleaved data
option needs to be enabled by setting this bit high.

<a id='920af05c-4b62-4cab-9c37-d18b74c73732'></a>

**REGISTER 19: Tx DIGITAL**
**BIT 4: 2 Data Paths**
Setting this bit high enables both transmit digital paths. By default, this bit is low and the transmit path utilizes only a single channel.

<a id='520ab467-8b7f-453a-bb39-e92b0abbdffd'></a>

**BIT 3: Keep -ve**
This bit configures the Tx Hilbert filter for either positive or negative frequencies pass band, assuming it is enabled. By default this bit is low, which selects the positive frequencies. Setting this bit high will setup the Hilbert filter to pass negative frequencies.

<a id='ae7b57ce-2625-4db3-8001-1b1b45f98205'></a>

**BIT 2: Hilbert**
This bit enables or disables the Hilbert filter in the transmit path.
By default, this bit is low, which disables the transmit Hilbert
filter. Setting this bit high enables the transmit Hilbert filter.

<a id='c5b37df1-ee0a-40c6-a1c1-8b0b9d794a63'></a>

**BIT 1,0: Interpolation Control**
These register bits control the interpolation rate of the transmit path. Default settings are both bits low, indicating that both interpolation filters are bypassed. The MSB and LSB are address D19, Bits 1 and 0, respectively. Setting binary 01 provides an interpolation rate of 2×; binary 10 provides an interpolation rate of 4×.

<a id='87a1452d-b674-4213-a27e-fcb5a757370f'></a>

**REGISTER 20: Tx MODULATOR**

**BIT 5: Negative Fine Tune**
When this bit is low (default), the Numerically Controlled Oscillator (NCO) provides positive shifts in frequency, assuming fine modulation is enabled. Setting this bit high will use a negative frequency shift in the Fine Complex Modulator.

<a id='516ae8e6-6b6f-43b5-af4b-3138fb01e40f'></a>

**BIT 4: Fine Mode**
By default, the NCO and fine modulation stage are bypassed. Setting this bit high will enable the use of the digital complex modulator, enabling tuning with the NCO.

<a id='144dc309-f7de-4325-bb6e-015a0fc8b9f1'></a>

**BIT 3: Real Mix Mode**
This bit determines if the coarse modulation (controlled by register Coarse Modulation, will perform a separate real mix on each channel or a complex mix using the dual channel data. By default, this bit is set low and a complex mix will be performed. Setting this bit high will enable the Real Mix mode. Note, the Fine Modulator Block only performs complex mixing.

<a id='daa7b36e-5979-4f74-9d62-7ae856a7b101'></a>

**BIT 2: Negative Coarse Tune**
When this bit is low (default), the coarse modulator provides positive shifts in frequency. Setting this bit high will shift the coarse modulator processed data negative in frequency.

<a id='21c96319-72ba-4e50-9826-4d7f34e83059'></a>

**BIT 1,0: Coarse Modulation**
These bits control what coarse modulation processing will be performed on the transmit data. A setting of binary 00 (default) will bypass the modulation block, a setting of binary 01 will shift the transmit data by f_DAC/4, and a setting of binary 10 will shift the transmit data by f_DAC/8.

<a id='15a74aae-e8ce-4c48-b59a-98c60bb2d427'></a>

REGISTER 21/22/23: NCO TUNING WORD
FTW [23:0]
These three registers set the 24-bit frequency tuning word (FTW) for the NCO in the fine modulator stage of the Tx path. The NCO full-scale tuning word is straight binary and produces a frequency equivalent to fDAC/4 with a resolution of fDAC/2^26.

<a id='af316e7a-1a7b-4d14-93c1-983fee347e47'></a>

REGISTER 24: DLL
BIT 6: Input Clock Control
This bit defines what type of clock will be driving the AD9860/
AD9862. The default state is low, which allows either crystal con-
nected to OSC1 and OSC2 or single-ended reference clock driving
OSC1 to drive the internal timing circuits. If a crystal will not be
used, the internal oscillator should be disabled after power-up
by setting this bit high.

<a id='7208e965-53e0-41d6-a68c-8e727c2b7212'></a>

**BIT 5: ADC Div2**
By default, the ADC is driven directly by the input clock in Normal Timing Operation mode or the DLL output in the Alternative Timing Operation mode. Setting this bit high will clock the ADC at one half the previous clock rate. This is described further in the timing section.

<a id='0d2a0b4b-cd62-47a8-924c-706a367c76be'></a>

BIT 4,3: DLL Multiplier
These bits control the DLL multiplication factor. A setting of binary 00 will bypass the DLL, a setting of binary 01 will multiply the input clock by 2, and a setting of binary 10 will multiply the input clock by 4. Default mode is defined by Mode/TxBlank logic level at power-up or RESET, which configures either Normal Operation Timing mode or Alternative Timing mode. In Alternative Timing mode, the DLL will lock to 4× multiplication factor (the DLL FAST register remains low by default). If the Mode/TxBlank pin is low, by default the DLL will be bypassed and a 1× clock is used internally.

<a id='e75cbcfb-f505-4f28-be07-6aca6af0e5d8'></a>

**BIT 2: DLL Power-Down**
Setting this register bit high forces the CLK IN multiplier to a power-down state. This mode can be used to conserve power or to bypass the internal DLL. To operate the AD9860/AD9862 when the DLL is bypassed, an external clock equal to the fastest on-chip clock is supplied to the OSC pin(s).

<a id='f48e9bbf-65bd-4d42-a03f-93aabac8f769'></a>

**BIT 0: DLL FAST**
The DLL can be used to generate output frequencies between 32 MHz to 128 MHz. Because of the large range of locking fre-quencies allowed, the DLL is separated into two output frequency ranges, a "slow" range between 32 MHz to 64 MHz and a "fast" range starting at frequencies above 64 MHz to 128 MHz. By

<a id='fcce0517-32ab-4681-84fb-74149f102b6d'></a>

REV. 0

<a id='dfe3f871-5f79-40a1-a489-bd1043a861ef'></a>

-15-

<!-- PAGE BREAK -->

<a id='16549b38-af38-4033-81c1-385a79d69d32'></a>

## AD9860/AD9862

default, this bit is low, setting up the DLL in "slow" mode. This
bit must be set high for DLL output frequencies over 64 MHz.

<a id='e61054e0-d9aa-4d5e-af46-68ce83871502'></a>

## REGISTER 25: CLKOUT

### BIT 7, 6: CLKOUT2 Divide Factor
These bits control what rate the CLKOUT2 Pin will operate at relative to the DLL output rate. The DLL output rate can be output directly or divided by 2, 4, or 8. Bit 7 is the MSB and Bit 6 is the LSB.

<a id='2a4ef36f-5b2d-477c-97f7-d58b2d6b64a8'></a>

MSB, LSB

00 (Default)
01
10
11

Relative CLKOUT2 Frequency

Equals DLL output rate
Equals DLL output rate divided by 2
Equals DLL output rate divided by 4
Equals DLL output rate divided by 8

<a id='74ffba52-b3fb-4845-967a-c3e2f5e2a2ec'></a>

BIT 5, 1: Inv 2/Inv 1
The output clocks from CLKOUT1 and CLKOUT2 can be
inverted by setting the appropriate one of these bits high.

<a id='39dc0430-62fa-41ca-998d-851b4b18bd2e'></a>

**BIT 4, 0: Dis 2/Dis 1**
The output clocks from CLKOUT1 and CLKOUT2 can be
disabled and a logic low output is forced by setting the appro-
priate one of these bits high.

<a id='0dcc29ec-0381-4c40-9b91-e0ddf09c7294'></a>

**REGISTER 26–33: AUXILIARY ADC A2/A1/B2/B1**
**AUX ADC A2, A1, B2, B1 Data**
These registers are read only registers that are used for read back of the 10-bit auxiliary ADC. The 10 bits are broken into a two registers, one containing the upper eight bits and the other containing the lower two bits.

<a id='7c33e531-58ea-46b6-b98c-b07d4595b767'></a>

REGISTER 34: AUX ADC CONTROL
BIT 7: Aux SPI (Enable)
One of the Auxiliary ADCs can be controlled through an dedi-
cated Auxiliary Serial Port. Setting this bit high enables this mode.

<a id='d6696ae8-4108-4437-a798-26aef9cb3e44'></a>

BIT 6: Sel BnotA
If the auxiliary Serial port is used, this bit selects which Auxiliary
ADC, A or B, will be using the dedicated Auxiliary Serial port.
The Auxiliary Serial port by default (low setting) controls Auxil-
iary ADC A. Setting this bit high will allow the Auxiliary Serial
Port to control Auxiliary ADC B.

<a id='2b366432-f504-4076-8127-b9adf38ad19d'></a>

BIT 5, 2: Refsel B/A
By default, the auxiliary ADCs use an external reference applied to
the AUX_REF pin. This voltage will act as the full-scale reference
for the selected auxiliary ADC. Either auxiliary ADC can use an
internally generated reference, which is a buffered version of the
analog supply voltage. To enable use of the internal reference for
either of the auxiliary ADCs, the respective Refsel register should
be set high.

<a id='c8b29c19-8bee-4bcf-b2db-f52ef5a8e911'></a>

**BIT 4, 1: Select B/A**
These bits select which of the two inputs will be connected to the respective auxiliary ADC. By default (setting low), the AUX_ADC_A2 pin is connected to Auxiliary ADC A and AUX_ADC_B2 pin is connected to Auxiliary ADC B. Setting the respective bit high will connect the AUX_ADC_A1 pin to Auxiliary ADC A and/or AUX_ADC_B1 pin to Auxiliary ADC B.

<a id='b2370f7f-68a3-4cf4-ae1c-d63303a2e096'></a>

BIT 3, 0: Start B/A
Setting a high bit to either of these registers initiates a conversion
of the respective auxiliary ADC, A or B. The register bit always
reads back a low.

<a id='cdf9c050-e2ba-464d-8d25-6066d8fa9230'></a>

**REGISTER 35: AUX ADC CLOCK**

**BIT 0: CLK/4**

By default (setting low), the auxiliary ADCs are run at the receive ADC conversion rate divided by 2. Setting this bit high will run

<a id='342edaa0-a653-437d-9ffe-5448432a74b2'></a>

the Auxiliary ADCs with a clock that is 1/4 of the receive ADC conversion rate. The conversion rate of the auxiliary ADCs should be less than 20 MHz.

<a id='18317e53-5c03-4704-af9c-21948d6ca71a'></a>

**REGISTER 36, 37, 38: AUX DAC A/B/C**
**Auxiliary DAC A, B, and C Output Control Word**
Three 8-bit, straight binary words are used to control the output of three on-chip auxiliary DACs. The auxiliary DAC output changes take effect immediately after any of the serial write is completed. The DAC output control words have default values of 0. The smaller programmed output controlled words corre-spond to lower DAC output levels.

<a id='73ca8fdc-c9bb-4183-a649-ed8504284c82'></a>

## REGISTER 39: AUX DAC UPDATE
### BIT 7: Slave Enable
A low setting (default) updates the auxiliary DACs after the respective register is written to. To synchronize the auxiliary DAC outputs to each other, a slave mode can be enabled by setting this bit high and then setting a high to the appropriate update registers.

<a id='57cf65b3-ab2a-4b4d-867e-ea3c679a9c91'></a>

BIT 2/1/0: Update C, B, and A
Setting a high bit to any of these registers initiates an update of the respective Auxiliary DAC, A, B, or C, when Slave mode is enabled using the Slave Enable register. The register bit is a one shot and always reads back a low. Note: be sure to keep the Slave Enable bit high when using the auxiliary DAC synchronization option.

<a id='a4df16df-4fe8-44ef-b770-d42ceb348709'></a>

REGISTER 40: AUX DAC POWER-DOWN
BIT 2/1/0: Power Down C, B, and A
Setting any of these bits high will power down the appropriate
auxiliary DAC. By default, these bits are low and the auxiliary
DACs are enabled.

<a id='f7206853-c093-4c6d-8d27-4ae70fe9b3d5'></a>

**REGISTER 41: AUX DAC CONTROL**
**BIT 4, 2, 0: Inv C, B, and A**
Setting any of these bits high will invert the appropriate Auxiliary DAC control word setting. By default, these bits are low and the output control word is decoded as noninverted, straight binary.

<a id='ed2f6f10-1e4f-42d8-b3bb-c334b090fea0'></a>

## REGISTER 42/43: SIGDELT (SIGMA-DELTA)

### Sigma-Delta Output Control Word
A 12-bit straight binary word is used to control the output of an on-chip sigma-delta converter. The sigma-delta output changes take effect immediately after any serial write is completed. The sigma-delta output control words have default values of 0. The smaller programmed output controlled words correspond to lower integrated sigma-delta output levels.

<a id='21f5a0a4-d5e6-429d-9304-c3bfa620ddf9'></a>

**REGISTER 49,50 : RX LOW POWER MODE**
Setting these bits will scale down the bias current to the ADC
analog block when the device is operated at lower speeds. By
default, these bits are low and the bias is at a nominal setting.

<a id='6d2b753b-4704-4a0e-92ee-2eee7df70dd0'></a>

For ADC operation at or below 32 MSPS, Register 49 can be set to 0x03 and Register 50 can be set to 0xEC; this will reduce Rx AVDD power consumption by about 30% relative to nominal.

<a id='313cc789-5858-4e22-89ff-7dd6b5d2c5c2'></a>

For ADC operation at or below 16 MSPS, Register 49 can be set
to 0x03 and Register 50 can be set to 0x9E; this will reduce Rx
AVDD power consumption by about 60% relative to nominal.

<a id='d65280ca-1e52-4e23-bc25-ab88b2169002'></a>

**REGISTER 63: CHIP ID**
**BIT 7–0: Rev ID**
This read only register indicates the revision of the AD9860/AD9862.

<a id='33096183-845a-40a0-8eb2-e9f230bb64e6'></a>

**Reserved Registers**
Reserved registers are held for future development and should never be written to.

<a id='cae44f95-5ff9-4e28-b860-523e74aa506f'></a>

-16-

<a id='1f3e7af0-5cdc-428d-9079-7305f4be8991'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='50a519c7-6b66-4015-95db-9adac27b4e51'></a>

AD9860/AD9862

<a id='a0b584ec-71ed-4598-9bfb-3db21972253a'></a>

## Blank Registers
Blank registers, i.e., the registers with 0 settings and no indicated function, are placeholders used throughout the register map for spacing the AD9860/AD9862 control bits in a logic fashion and, potentially can be used for future development. A low should always be written to these registers if a write needs to take place.

<a id='d4feb441-77b9-4067-a901-ddb6c5ca3911'></a>

## SERIAL PORT INTERFACE
The Serial Port Interface (SPI) is used to write to and read from the AD9860/AD9862 internal programmable registers. The serial interface uses four pins: SEN, SCLK, SDIO, and SDO by default. SEN is a serial port enable pin, SCLK is the serial clock pin, SDIO is a bidirectional data line and SDO is a serial output pin.

<a id='34592307-0233-4ef9-ac09-dbdf307e8776'></a>

SEN is an active low control gating read and write cycles. When
SEN is high, SDO and SDIO are three-stated.

<a id='59b5d41b-bfba-4e1b-9ce2-4dc58a383218'></a>

SCLK is used to synchronize SPI read and writes at a maximum
bit rate of 16 MHz. Input data is registered on the rising edge and
output data transitions on the falling edge. During write opera-
tions, the registers are updated after the 16th rising clock edge
(and 24th rising clock edge for the dual byte case). Incomplete
write operations are ignored.

<a id='d8722369-8181-4de5-b453-ce213e9f2332'></a>

SDIO is an input only by default. Optionally, a 3-pin interface may be configured using the SDIO for both input and output operations and three-stating the SDO pin (see SDIO BiDir register).

<a id='d4fcc488-7a2c-4459-9da1-deb60018ebfe'></a>

SDO is a serial output pin used for read back operations in 4-wire mode and is three-stated when SDIO is configured for bidirectional operation.

<a id='d0de0cea-7a64-4386-b481-7da96b9d4516'></a>

## Instruction Header
Each SPI read or write consists of an instruction header and data. The instruction header is made up of an 8-bit word and is used to set up the register data transfer. The 8-bit word consists of a read/not write bit, R/nW (the MSB), followed by a double/not single bit (2/n1) and the 6-bit register address.

<a id='6a1b0b54-c756-4604-9e65-8723a78a49e9'></a>

### Write Operations
The SPI write operation uses the instruction header to configure a one or two register write using the 2/n1 bit. The instruction byte followed by the register data, is written serially into the device through the SDIO pin on rising edges of the interface clock at SCLK. The data can be transferred MSB first or LSB first depending on the setting of the LSB First register.

<a id='496b94a7-b0cc-4b23-9ea2-5c7463f6645a'></a>

Figure 1 includes a few examples of writing data into the device.
Figure 1a shows a write using 1 Byte and MSB First mode set;
Figure 1b shows an MSB first, 2 Byte write; and Figure 1c
shows an LSB first, 2 Byte write. Note the differences between
LSB and MSB First modes: instruction header and data are
reversed, and in 2 Byte writes, the first data byte is written to
the address in the header, N and the second data byte is written
to the n-1 address. In LSB First mode, the first data byte is still
written to the address in the instruction header, but the second
data byte is written to the N+1 address.

<a id='9fe989bd-89da-4083-b481-b567f2a1b1ab'></a>

<::Timing diagram showing three signals: SEN, SCLK, and SDIO. From left to right:  SEN is initially high, then goes low, and stays low for a period, then goes high again.  SCLK is initially labeled "DON'T CARE", then shows a series of clock pulses (low-high-low transitions), and finally is labeled "DON'T CARE" again.  SDIO is initially labeled "DON'T CARE". After a period, it shows "R/nW", followed by "2/n1". Then, it shows a sequence of address bits "A5", "A4", "A3", "A2", "A1", "A0", which are grouped under the label "INSTRUCTION HEADER". This is followed by data bits "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0", which are grouped under the label "REGISTER DATA". Finally, SDIO is labeled "DON'T CARE" again.  Various timing parameters are indicated with arrows: tS (setup time for SEN), tDH (data hold time), tDS (data setup time), tLO (SCLK low time), tHI (SCLK high time), tCLK (SCLK period), and tH (hold time for SEN).: timing diagram::>

<a id='a6877631-a1ba-4fb9-82cf-8ddcaabf724f'></a>

<::Timing Diagram: This diagram illustrates the timing sequence for SEN, SCLK, and SDIO signals.  

**Signals:**  
*   **SEN:** An active-low signal, initially high, goes low, then high again after a duration tH.  
*   **SCLK:** A clock signal, initially in a "DON'T CARE" state, then shows a series of square waves (clock pulses), and finally returns to a "DON'T CARE" state.  
*   **SDIO:** A data input/output signal, initially in a "DON'T CARE" state, then shows various data bits, and finally returns to a "DON'T CARE" state.  

**Timing Parameters:**  
*   **tS:** Setup time, from the falling edge of SEN to the rising edge of the first SCLK pulse.  
*   **tDS:** Data setup time.  
*   **tDH:** Data hold time.  
*   **tLO:** Low pulse width of SCLK.  
*   **tHI:** High pulse width of SCLK.  
*   **tCLK:** SCLK period.  
*   **tH:** Hold time, from the rising edge of the last SCLK pulse to the rising edge of SEN.  

**SDIO Data Content:**  
*   The first active segment of SDIO contains "R/nW" followed by "2/n1", then address bits "A5", "A4", "A3", "A2", "A1", and "A0". This entire section is labeled as "INSTRUCTION HEADER (REGISTER N)".  
*   The next segment contains data bits "D7", "D6", "D5", "D4", "D3", "D2", "D1", and "D0". This section is labeled as "REGISTER (N) DATA".  
*   The final active segment contains data bits "D7", "D6", "D5", "D4", "D3", "D2", "D1", and "D0". This section is labeled as "REGISTER (N-1) DATA".  

**Overall Flow:**  
The SEN signal initiates the communication. SCLK provides the clock for data transfer. SDIO carries the instruction header, followed by data for Register N, and then data for Register N-1.  
::>

<a id='9dba47a2-b559-4995-a391-745017ac8d87'></a>

<::timing diagram: The diagram shows three waveforms over time for an SPI write operation. The y-axis labels are SEN, SCLK, and SDIO from top to bottom. The x-axis represents time.

**SEN (Slave Enable):** Starts high, goes low for the duration of the data transfer, and then returns high. Timing parameters t_S (setup time) and t_H (hold time) are indicated relative to SEN's falling and rising edges, respectively.

**SCLK (Serial Clock):** Is initially low, then shows a series of clock pulses (square waves) during the active low period of SEN. Timing parameters t_LO (clock low time), t_HI (clock high time), and t_CLK (clock period) are indicated.

**SDIO (Serial Data Input/Output):** Shows data bits being transmitted synchronously with the SCLK pulses. The data bits are labeled sequentially:
- A0, A1, A2, A3, A4, A5 (part of the "INSTRUCTION HEADER (REGISTER N)")
- 2/n1
- R/nW (Read/Not Write)
- D0, D1, D2, D3, D4, D5, D6, D7 (part of "REGISTER (N) DATA")
- D0, D1, D2, D3, D4, D5, D6, D7 (part of "REGISTER (N+1) DATA")
- "DON'T CARE" at the end.

Timing parameters t_DS (data setup time) and t_DH (data hold time) are indicated relative to the SCLK edges and SDIO data transitions.

Below the SDIO line, three sections are labeled:
1. "INSTRUCTION HEADER (REGISTER N)" encompassing A0 through R/nW.
2. "REGISTER (N) DATA" encompassing the first set of D0-D7.
3. "REGISTER (N+1) DATA" encompassing the second set of D0-D7.

Figure 1. SPI Write Examples a. (top) 1 Byte, MSB First Mode; b. (middle) 2 Byte, MSB First Mode; c. (bottom) 2 Byte, LSB First Mode::>

<a id='97173e5d-f814-46a7-84b6-675e39a60482'></a>

REV. 0

<a id='64c48b21-bc3e-47f2-93c8-cc9409317372'></a>

-17-

<!-- PAGE BREAK -->

<a id='70c0606f-5c70-4376-ae38-2c6b285b0b4f'></a>

AD9860/AD9862
<::timing diagram: The diagram shows a timing waveform for the AD9860/AD9862 device with four signal lines: SEN, SCLK, SDIO, and SDO. Various timing parameters are indicated.

**SEN signal**: Starts high, goes low for a duration, then returns high.
  - Timing parameters associated with SEN: t_S (setup time before falling edge), t_H (hold time after rising edge).

**SCLK signal**: Starts with "DON'T CARE", then shows a series of clock pulses (square wave), and ends with "DON'T CARE".
  - Timing parameters associated with SCLK: t_LO (low pulse width), t_HI (high pulse width), t_CLK (clock period).

**SDIO signal**: Starts with "DON'T CARE". During the active clock period, it shows the following data bits: R/nW, 2/n1, A5, A4, A3, A2, A1, A0. This entire segment is labeled "INSTRUCTION HEADER (REGISTER N)". It ends with "DON'T CARE".
  - Timing parameters associated with SDIO: t_DS (data setup time to clock edge), t_DH (data hold time from clock edge).

**SDO signal**: Starts with "DON'T CARE". During a later active clock period, it shows the following data bits: D7, D6, D5, D4, D3, D2, D1, D0. This entire segment is labeled "OUTPUT REGISTER DATA". It ends with "DON'T CARE".
  - Timing parameters associated with SDO: t_DV (data valid delay from clock edge).

The timing parameters t_S, t_DS, t_DH, t_LO, t_HI, t_CLK, t_DV, and t_H are shown with arrows indicating their respective durations relative to the signal transitions.::>


<a id='7c6fcac8-0011-4fd5-8a7e-9fdf5c6d1b67'></a>

<::Timing Diagram: This diagram illustrates the timing relationships between three signals: SEN, SCLK, and SDIO.

**Signals and their waveforms:**
- **SEN**: Starts high, transitions low, remains low for a period, then transitions high again.
- **SCLK**: Starts with "DON'T CARE", followed by a series of clock pulses (square wave), and ends with "DON'T CARE".
- **SDIO**: Starts with "DON'T CARE", then presents data in segments: "R/nW", "2/n1", "A5", "A4", "A3", "A2", "A1", "A0", followed by "D7", "D6", "D5", "D4", "D3", "D2", "D1", "D0", and finally "DON'T CARE".

**Timing Parameters:**
- **t_s**: Setup time for SEN (before falling edge).
- **t_DS**: Data setup time for SDIO (before SCLK rising edge).
- **t_DH**: Data hold time for SDIO (after SCLK falling edge).
- **t_LO**: SCLK low pulse width.
- **t_HI**: SCLK high pulse width.
- **t_CLK**: SCLK clock period.
- **t_DV**: Data valid time for SDIO (after SCLK falling edge).
- **t_H**: Hold time for SEN (after rising edge).

**Data Sections on SDIO:**
- The segment from "R/nW" to "A0" is labeled as **INSTRUCTION HEADER**.
- The segment from "D7" to "D0" is labeled as **OUTPUT REGISTER DATA**.
: timing diagram::>

<a id='8ddd37b7-3e8a-493e-95c1-60857323c8c4'></a>

<::Timing Diagram:SEN: Starts high, goes low, then stays low for a period, and finally goes high. t_S indicates the setup time from the falling edge of SEN to the first rising edge of SCLK. t_H indicates the hold time from the last falling edge of SCLK to the rising edge of SEN.SCLK: Initially "DON'T CARE". After SEN goes low, SCLK starts clocking with alternating high and low pulses. t_HI is the high pulse width, t_LO is the low pulse width, and t_CLK is the clock period. Ends with "DON'T CARE".SDIO: Initially "DON'T CARE". Transmits data bits: A0, A1, A2, A3, A4, A5, 2/n1, R/nW. This entire segment is labeled "INSTRUCTION HEADER". t_DS is the data setup time, and t_DH is the data hold time relative to SCLK edges. Ends with "DON'T CARE".SDO: Initially "DON'T CARE". Transmits data bits: D0, D1, D2, D3, D4, D5, D6, D7. This entire segment is labeled "OUTPUT REGISTER DATA". t_DV is the data valid time after the rising edge of SCLK. Ends with "DON'T CARE".::>

<a id='d3ae234e-ae3d-49cf-bdd8-b8f7db987e79'></a>

Figure 2. SPI Read Examples a. (top) 4-Wire Interface, MSB first; b. (middle) 3-Wire Interface, MSB first;
c. (bottom) 4-Wire Interface, LSB first

<a id='801891ae-03e9-462e-83a7-3effa2b04f59'></a>

## Read Operation
The read back of registers is a single data byte operation. The readback can be configured to use three pins or four pins and can be formatted as MSB first or LSB first. The instruction header is written to the device either MSB or LSB first (depending on the mode) followed by the 8-bit output data (appropriately MSB or LSB justified). By default, the output data is sent to the dedicated output pin (SDO). 3-wire operation can be configured by setting the SDIO BiDir register. In 3-wire mode, the SDIO pin will become an output pin after receiving the 8-bit instruction header with a read back request.

<a id='b38d84c0-e9b8-4244-87aa-cbf23b3f12b2'></a>

Figure 2a shows an MSB first, 4-pin SPI read; Figure 2b shows an MSB first, 3-pin read; and Figure 2c shows an LSB first, 4-pin read.

<a id='0df181b8-8779-4908-8b77-a5c0e152d184'></a>

SYSTEM BLOCK DESCRIPTION
The AD9860/AD9862 integrates transmit and receive paths with
digital signal processing blocks and auxiliary features. The auxiliary

<a id='95a873e6-3013-4f86-bb6a-8b7233c5693d'></a>

features include two auxiliary ADCs, a programmable sigma-delta output, three auxiliary DACs, integrated clock circuitry to generate all internal clocks, and buffered output clocks from a single input reference.

<a id='18f73951-862c-4873-b1e6-784b2f9e87bb'></a>

The AD9860/AD9862 system functionality is described in the following four sections: the Transmit Block, Receive Block, Timing Generation Block, and the Auxiliary Function Block. The following sections provide a brief description of the blocks and applications for the four sections.

<a id='f6ba47fa-cfd1-4300-afa5-6c955886a6e9'></a>

## TRANSMIT SECTION COMPONENTS
The transmit block (Tx) accepts and can process real or complex data. The Tx interface is configurable for a variety of data formats and has special processing options such as interpolation and Hilbert filters. A detailed block diagram of the AD9860/AD9862 transmit path is shown in Figure 3. The transmit block diagram is broken into these stages: DAC (Block A), Coarse Modulation (Block B),

<a id='3dedd375-33f7-44dc-81dc-0263c4f998ac'></a>

-18-

<a id='a0767d02-f972-4ccc-97bd-d4e741cd6ba1'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='3264681b-e45d-40a2-96a1-b42b0e7b3e71'></a>

---
AD9860/AD9862

<a id='c437f2fa-153d-489b-b6ea-b081605370b0'></a>

<::block diagram: flowchart::>BLOCK A: DAC
- Inputs: IOUT+A and IOUT-A, which feed into a PGA (Programmable Gain Amplifier), then to a TxDAC (Transmit Digital-to-Analog Converter).
- Inputs: IOUT+B and IOUT-B, which feed into a PGA, then to a TxDAC.
- Outputs of both TxDACs connect to BLOCK B.

BLOCK B: Bypassable Digital Quadrature Mixer
- Inputs from BLOCK A connect to two multiplexers.
- The outputs of the multiplexers are fed into a mixer (labeled X) and also have connections for I and Q signals.
- Control signals for this block are fs/4 and fs/8.
- Outputs connect to BLOCK C.

BLOCK C: Bypassable Low-Pass Interpolation Filter
- Inputs from BLOCK B.
- Contains two parallel low-pass filter components.
- Outputs connect to BLOCK D.

BLOCK D: Bypassable Digital Quadrature Mixer
- Inputs from BLOCK C connect to two multiplexers.
- The outputs of the multiplexers are fed into a mixer (labeled X) and also have connections for I and Q signals (Q is explicitly labeled).
- Control signal for this block is DDS (Direct Digital Synthesizer).
- Outputs connect to BLOCK E.

BLOCK E: Hilbert Filter
- Inputs from BLOCK D.
- Contains two parallel Hilbert Filter components.
- The outputs of the Hilbert Filters connect to a final output multiplexer.

Output:
- The final multiplexer outputs TxDATA [0:13].

Figure 3. Transmit Section Block Diagram<::>

<a id='937938aa-ce51-420e-87d8-f67e47be8957'></a>

Interpolation Stage (Block C), Fine Modulation Stage (Block D),
Hilbert filter (Block E), and the Latch/Demultiplexing circuitry.

<a id='7c954505-57d7-482e-8117-0f67646158d0'></a>

DAC
The DAC stage of the AD9860/AD9862 integrates a high performance TxDAC core, a programmable gain control through a Programmable Gain Amplifier (TxPGA), coarse gain control, and offset adjustment and fine gain control to compensate for system mismatches.

<a id='7bc0b010-cb9b-4414-94e0-9266e5600dac'></a>

The TxDAC core of the AD9860/AD9862 provides dual, differen-
tial, complementary current outputs generated from the 12-/14-bit
data. The 12-/14-bit Dual DACs support update rates up to
128 MSPS. The differential outputs (i.e., IOUT+ and IOUT-)
of each dual DAC are complementary, meaning they always sum
to the full-scale current output of the DAC, I_{OUTFS}. Optimum
ac performance is achieved with the differential current interface
drives balanced loads or a transformer.

<a id='60c2c279-8e9d-4b70-8b5c-a3aa6b098cca'></a>

The maximum full-scale output current, IOUTF SMAX, is set by the external resistor (RSET), which sets the DAC reference current.
The RSET resistor is connected between the FSADJ Pin to ground.
The relationship between IOUTF SMAX and RSET is:

<a id='44853328-dd4a-4d7f-b98a-86ff2dd05b77'></a>

$$I_{OUTFSMAX} \sim 67 \times \left(\frac{1.23\ V}{R_{SET}}\right)$$

<a id='3829d6c5-0d17-4a84-b3cf-4020c75da296'></a>

Typically, RSET is 4 kΩ, which sets IOUTFSMAX to 20 mA, the optimal dynamic setting for the TxDACs. Increasing RSET by a factor of 2 will proportionally decrease IOUTFSMAX by a factor of 2. IOUTFSMAX of each DAC can be re-scaled either simultaneously with the TxPGA Gain register or independently with DAC A/B Coarse Gain registers.

<a id='e1db17b6-d577-4c00-8191-fd9c9f6d006d'></a>

The TxPGA function provides 20 dB of simultaneous gain
range for both DACs and is controlled by writing to SPI register
TxPGA Gain for a programmable full-scale output of 10% to
100% IOUTFSMAX. The gain curve is linear in dB, with steps of
about 0.1 dB. Internally, the gain is controlled by changing the
main DAC bias currents with an internal TxPGA DAC whose
output is heavily filtered via an on-chip R-C filter to provide
continuous gain transitions. Note, the settling time and band-
width of the TxPGA DAC can be improved by a factor of 2 by
writing to the TxPGA Fast register.

<a id='9bdd2918-32fa-4ac5-84db-5c5ba54c470f'></a>

Each DAC has independent coarse gain control. Coarse gain control can be used to accommodate different IOUTFS from the dual DACs. The coarse full-scale output control can be adjusted using the DAC A/B Coarse Gain registers to 1/2 or 1/11th of the nominal full scale current.

<a id='166fd279-2e0f-4ad9-9c2d-5e4cfdbd23c8'></a>

Fine Gain controls and dc offset controls can be used to compen-sate for mismatches (for system level calibration), allowing improved matching characteristics of the two Tx channels and aiding in suppres-sing LO feedthrough. This is especially useful in image rejection architectures. The 10-bit dc offset control of each DAC can be used independently to provide a 12% IOUTFSMAX of offset to either differential pin, thus allowing calibration of any system offsets. The fine gain control with 5-bit resolution allows the IOUTFSMAX of each DAC to be varied over a 4% range, thus allowing compensation of any DAC or system gain mismatches. Fine gain control is set through the DAC A/B Fine Gain registers and the offset control of each DAC is accomplished using DAC A/B Offset registers.

<a id='68a59e77-14d9-4b85-b5f7-2c2b9acfe63f'></a>

A power-down option allows the user to power down the analog supply current to both DACs or either DAC, individually. A digital power-down is also possible through either the Tx PwrDwn register or the Mode/TxBlank pin.

<a id='6cb81fb5-95e2-4b27-bce5-0acbc03f3cd3'></a>

Coarse Modulator
A digital coarse modulator is available in the transmit path to
shift the spectrum of the input data by fDAC/4 or fDAC/8. If the
input data consists of complex data, the modulator can be con-
figured to perform a complex modulation of the input spectrum.
If the data in the transmit path is not complex, a real mix can be
performed separately on each channel thereby frequency shifting
the real data and images by fDAC/4 or fDAC/8. Real or complex
mixing is configured by setting the Real Mix register.

<a id='ca099544-b647-4015-8d02-e7211357fe8f'></a>

By default, the coarse modulator is bypassed. It can be configured using Coarse Modulation and Neg Coarse Tune registers.

<a id='dd6dde26-3daf-4804-a237-4ee5a84c35d8'></a>

**Interpolation Stage**
Interpolation filters are available for use in the AD9860/AD9862 transmit path, providing 1× (bypassed), 2×, or 4× interpolation.
The interpolation filters effectively increase the Tx data rate while suppressing the original images. The interpolation filters digitally shift the worst case image further away from the desired signal, thus reducing the requirements on the analog output reconstruction filter.

<a id='5144e212-9f3d-4627-83d8-f1fe00557848'></a>

There are two 2x interpolation filters available in the Tx path.
An interpolation rate of 4x is achieved using both interpolation
filters; an interpolation rate of 2x is achieved by enabling only
the first 2x interpolation filter.

<a id='d57eaa80-c31c-41aa-97d3-1a9a42828324'></a>

The first interpolation filter provides 2× interpolation using a 39 tap filter. It suppresses out-of-band signals by 60 dB or more and has a flat passband response (less than 0.1 dB ripple) extending to 38% of the AD9860/AD9862 input Tx data rate (19% of the DAC update rate, f₁₂₃₄). The maximum input data rate is 64 MSPS per channel when using 2× interpolation.

<a id='7ffac80f-eab3-4a1c-8b4a-24e6e98ec9ff'></a>

REV. 0

<a id='78fa9555-5077-411b-83d0-1cfbc541c6fa'></a>

-19-

<!-- PAGE BREAK -->

<a id='40eee5c1-972b-4780-b0c8-950fda618850'></a>

**AD9860/AD9862**

The second interpolation filter will provide an additional 2× interpolation for an overall 4× interpolation. The second filter is a 15 tap filter. It suppresses out-of-band signals by 60 dB or more. The flat passband response (less than 0.1 dB attenuation) is 38% of the Tx input data rate (9.5% of fDAC). The maximum input data rate per channel is 32 MSPS per channel when using 4× interpolation.

<a id='2c21da68-eb33-4220-90ca-004a90a5502d'></a>

The 2× and 4× Interpolation Filter Transfer function plots are shown in Figure 4a and 4b, respectively.

<a id='89e02f6a-0e3b-488e-aab4-39f02503f84d'></a>

<::Graph showing the frequency response of two filters. The x-axis is labeled "NORMALIZED - fS" and ranges from 0 to 1.0. The y-axis is labeled "MAGNITUDE - dB" and ranges from -100 to 10. Two curves are plotted: one labeled "INTERPOLATION FILTER" and another labeled "INCLUDUNG SIN (X)/X". Both curves show a low-pass filter characteristic, with the interpolation filter having a sharper cutoff and more ripple in the stopband compared to the other curve.::>

<a id='ff10e88c-ba29-41e6-bed6-e3e0be20dc34'></a>

<::A line graph titled "Spectral Response" with two curves. The Y-axis is labeled "MAGNITUDE - dB", ranging from 10 dB at the top to -100 dB at the bottom. The X-axis is labeled "NORMALIZED - fs", ranging from 0 to 1.0. Two curves are plotted: one labeled "INTERPOLATION FILTER" and another labeled "INCLUDING SIN (X)/X". Both curves start at 0 dB at X=0. The "INTERPOLATION FILTER" curve drops sharply to below -60 dB around X=0.15 and then shows a stopband with ripples, rising towards 0 dB again as X approaches 1.0. The "INCLUDING SIN (X)/X" curve also drops sharply, slightly earlier than the first, and exhibits a stopband with more pronounced and higher-frequency ripples, also rising towards 0 dB near X=0.9. This graph illustrates the spectral response for 2x and 4x interpolation filters.::>Figure 4. Spectral Response of 2× Interpolation Filter (top) and 4× Interpolation Filter (bottom)

<a id='c8b0f65f-bb80-4aef-ae94-46ef282c5809'></a>

## Fine Modulation Stage
A digital fine modulation stage is available in the transmit path to shift the complex Tx output spectrum using a 24-bit numerically controlled oscillator (NCO). To utilize the Fine Modulation Block, 4× interpolation is required. Therefore, the maximum input data rate is 32 MSPS per channel, which generates a DAC update rate, f_DAC, of 128 MSPS. The NCO can tune up to 1/4 of f_DAC, providing a step resolution of f_DAC/2^26. Since the Fine Modulation Stage precedes the Interpolation Filters, care must be taken to ensure the entire desired signal is placed within the pass band of the Interpolation Filter.

<a id='2658d8ee-04eb-4bd3-9ff2-53482a408bd9'></a>

By default, the Fine Modulation Block is bypassed. To enable it to perform a complex mix of the Tx I and Q data, Register 2's data paths, Fine Mod and Fine, should be configured. The NCO frequency tuning word is set in the three FTW registers.

<a id='af02f61c-85f7-4f71-9405-02d60325b089'></a>

## Hilbert Filter
The Hilbert filter is available to provide a Hilbert transform of "real" input data at a low intermediate frequency (IF) between 12.5% to 38% of the input data rate. The Hilbert filter essentially transforms this "real," single channel input data into a complex representation (i.e., I and Q components) that can be used as part of an image rejection architecture. The complex data can then be processed further using the on-chip digital complex modulators. The Hilbert filter requires 4× interpolation to be enabled and accepts data at a maximum 32 MSPS. Figure 5 shows a spectral plot of the Hilbert filter impulse response.

<a id='87306936-771b-49c3-9eb5-a29e6d679223'></a>

<::chart: spectral plot::>
## Figure 5. Tx Hilbert Filter, Keeping Positive Frequencies Spectral Plot
This spectral plot displays dB (decibels) on the y-axis, ranging from -100 to 100, against FREQUENCY - MHz on the x-axis, ranging from -20 to 20. The plot shows a frequency response with significant attenuation (low dB values) for negative frequencies and frequencies below approximately 3 MHz. There is a prominent bandpass region for positive frequencies, roughly between 4 MHz and 11 MHz, where the response is high, peaking around 80 dB. Beyond this band, the response drops again, showing ripples and lower dB values for frequencies above 11 MHz.
<::>

<a id='3541ff9d-3c1d-49eb-9d7f-f200d1434975'></a>

## Latch/Demultiplexer
The AD9860/AD9862 Tx path accepts dual or single channel data. The dual channel data can represent two independent real signals or a complex signal. Various input data latching schemes relative to one of the output clocks, CLKOUT1 or CLKOUT2, are allowed, including using any combination of rising and falling clock edges.

<a id='1d4a4854-fe15-4300-b56d-b539b0e0cf3a'></a>

Associated Tx timing is discussed in detail in the Clock Overview section of the data sheet.

<a id='676afb7f-467e-4732-86b0-1a139c278276'></a>

**TRANSMIT APPLICATIONS SECTION**
The AD9860/AD9862 transmit path (Tx) includes two, high speed,
high performance, 12-/14-bit TxDACs. Figure 3 shows a detailed
block diagram of the transmit data path and can be referred to
throughout the explanation of the various modes of operation.
The various Tx modes of operation are broken into three parts,
determined by the format of the input data. They are:
1. Single Channel DAC Data
2. Two Independent Real Signal DAC Data (diversity or dual
channel
3. Dual Channel Complex DAC Data (I and Q or Single Sideband)

<a id='27368c94-f2fa-45cf-97d3-0f4d11f4dd9a'></a>

**Single Channel DAC Data**
In this mode, 12-/14-bit single channel Tx data is provided to the AD9860/AD9862 and latched using either CLKOUT1 or CLKOUT2 edges as defined in the Clock Overview section of the data sheet. All Tx digital signal processing blocks can be utilized to address reconstruction filtering at the DAC output and aid in frequency tuning.

<a id='b6c4cd04-459f-4778-b70b-2134a3cc390f'></a>

-20-

<a id='97ecadbc-83bf-4a7c-8b05-ab8496ad70df'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='1abe3ce2-df9a-487d-b5da-1df9aa447ef3'></a>

AD9860/AD9862<::block diagram: The diagram, titled "Receive Section Block Diagram", illustrates the signal processing chain. It is divided into five main conceptual blocks, A through E, outlined by dashed lines.Two parallel input paths, one for A and one for B, are shown.Top Path (A):VIN+A and VIN-A inputs feed into a differential amplifier labeled "1x" (Block A). The output of this amplifier goes into a PGA (Programmable Gain Amplifier) (Block B). The PGA's output then feeds into an ADC (Analog-to-Digital Converter) (Block C). The ADC's output goes into a LOW-PASS DECIMATION FILTER (Block D).Bottom Path (B):VIN+B and VIN-B inputs feed into a differential amplifier labeled "1x" (Block A). The output of this amplifier goes into a PGA (Block B). The PGA's output then feeds into an ADC (Block C). The ADC's output goes into a LOW-PASS DECIMATION FILTER (Block D).After Block D, the outputs from both the top and bottom LOW-PASS DECIMATION FILTERS converge and feed into a single HILBERT FILTER (Block E).The output of the HILBERT FILTER then splits into two paths:One path goes through a series of two multiplexers/selectors to produce "RxA DATA [0:11]".The other path goes through a single multiplexer/selector to produce "RxB DATA [0:11]".Figure 6. Receive Section Block Diagram::>

<a id='7291f2c7-f5fb-4de8-97c3-6568da8526ff'></a>

**RECEIVE SECTION COMPONENTS**
The receive block is configurable to process input signals of different formats and has special features such as an input buffer, gain stage, and decimation filters. The AD9860/AD9862 receive path block diagram is shown in Figure 6. The block diagram can be broken into the following stages: Input Buffer (Block A), RxPGA (Block B), dual, 10-/12-bit, 64 MSPS ADC (Block C), Decimation filter (Block D), Digital Hilbert Block (Block E), and a Data Output Multiplexer. The function of each stage is explained in the following paragraphs.

<a id='7d3c4aed-5c90-438b-a5b3-d7632dc11a1f'></a>

**Input Buffer Stage**
The input buffer stage buffers the input signal on-chip for both receive paths. The buffer stage has two main benefits, providing a constant input impedance and reducing any "kick-back" noise that might be generated on-chip, affecting the analog input signal.

<a id='2f34045e-78ac-4c79-b092-9f4ef0241ef3'></a>

The Rx path sampling mode can be split into two categories,
depending on the frequency of the input signal. When sampling
input signals up to Nyquist of the ADC, the sampling is referred to
as Nyquist sampling. When sampling at rates above ADC Nyquist
rate, the sampling is referred to as IF sampling or undersampling.

<a id='10238e96-9ef5-416f-916b-83674f1c06ab'></a>

For Nyquist sampling, the input buffer provides a constant 200 Ω impedance over the entire input signal range. The constant input impedance accommodates matching networks to ensure proper transfer of signal to the input of the device. The input buffer is self-biased to ~ 2 V, and therefore the input signal should be ac-coupled to the Rx differential input or have a common-mode voltage of about 2 V. If an external buffer is present, the internal input buffer can be bypassed and powered down to reduce power consumption. The input buffer accepts up to a 2 V p-p input signal for maximum SNR performance. Optimal THD performance occurs with 1 V p-p input signal.

<a id='12871680-ae74-4421-9bcc-1e2f75e3505b'></a>

For IF sampling, the input buffer can be used with input signals
up to about 100 MHz, the 3 dB bandwidth of the buffer. When
undersampling the input signal, the output spectrum will contain
an aliased version of the original, higher frequency signal. As was
the case with Nyquist sampling, the input signal should be
ac-coupled to the Rx differential input or have a common-mode
voltage of~2 V. For input signals over 100 MHz to about 250 MHz,
the input buffer needs to be bypassed and an external input
buffer is required. In the case that the input buffer is bypassed,
the input circuit is a switched capacitor network. The switching
input impedance during the sample phase is about 1/(2(π)FC),
where F is the input frequency and C is the input capacitance
(about 4 pF). During hold mode, the input impedance is > 1 MΩ.

<a id='4bb65bf5-58ae-48fc-abae-4bfef5de46d4'></a>

RxPGA
The RxPGA stage has a Programmable Gain Amplifier that can be used to amplify the input signal to utilize the entire input range of the ADC. The RxPGA stage provides a 0 dB to 20 dB gain range in steps of about 1 dB. The Rx channel independent gain control is accomplished through two 5-bit SPI programmable RxPGA A/B registers. The gain curve is linear in dB with a minimum gain setting (0 dB, nominally) of hex00 and a maximum gain setting (20 dB, nominally) of hex14.

<a id='cecb7c5e-130a-49c7-ab93-6243a4054641'></a>

The RxPGA stage can provide up to a 2 V p-p signal to the ADC input.

<a id='3afe1fd6-1b5c-40b1-accd-bf7bad0b5654'></a>

## Analog-to-Digital (A/D) Converter
The analog-to-digital converter (ADC) stage consists of two high performance 10-/12-bit, 64 MSPS analog-to-digital (A/D) converters. The dual A/D converter paths are fully independent, except for a shared internal bandgap reference source, VREF. Each of the A/D converter's paths consists of a front-end sample and hold amplifier followed by a pipelined, switched capacitor, A/D converter. The pipelined A/D converter is divided into three sections, consisting of a 4-bit first stage followed by eight 1.5-bit stages and a final 3-bit flash. Each stage provides sufficient overlap to correct for flash errors in the preceding stages. The quantized outputs from each stage are combined into a final 12-bit result through a digital correction logic block. The pipelined architecture permits the first stage to operate on a new input sample while the remaining stages operate on preceding samples. Sampling occurs on the rising clock edge.

<a id='1d6601c8-c0ca-4b77-a5dc-49110ae3ed2c'></a>

Each stage of the pipeline, excluding the last, consists of a low resolution flash A/D connected to a switched capacitor DAC and interstage residue amplifier (MDAC). The residue amplifier magnifies the difference between the reconstructed DAC output and the flash input for the next stage in the pipeline. One bit of redundancy is used in each one of the stages to facilitate digital correction of flash errors. The last stage simply consists of a flash A/D.

<a id='a0ebfe8f-d725-4a70-b15f-76aae93decf5'></a>

A stable and accurate 1.0 V bandgap voltage reference is built into the AD9860/AD9862 and is used to set a 2 V p-p differential input range. The internally generated reference should be decoupled at the VREF pin using a 10 µF and a 0.1 µF capacitor in parallel to ground. Separate top and bottom references, VRT and VRB, for each converter are generated from VREF and should also be decoupled. Recommended decoupling for the top and bottom references consists of using 10 µF and 0.1 µF capacitors in parallel between the differential reference pins, and a 0.1 µF capacitor

<a id='d6fbfeae-b816-4df7-be04-37febcc6ae06'></a>

-22-

<a id='3a3512d4-ee9d-4304-89c8-05cb98020d04'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='25e2e2ce-1b2b-4424-a6bc-fe3453444e38'></a>

AD9860/AD9862

<a id='5f3d30d3-56af-41a2-909c-b66a7d53ed64'></a>

from each to ground. The internal references can also be disabled (powered down) and driven externally to provide a different input voltage range or low drift reference. If an external VREF reference is used, it should not exceed 1.0 V.

<a id='fb1167d0-6066-479b-80d5-9bf12466cc09'></a>

A Shared Reference mode allows the user to connect the differen-tial references from both ADCs together externally for superior gain matching performance. If the ADCs are to function inde-pendently, then the reference can be left separate and will provide superior isolation between the dual channels. Shared Reference mode can be enabled through the Shared Ref register.

<a id='3841db3c-f072-4efe-83cd-02fb09be1ca5'></a>

A power-down option allows the user to power down both ADCs (sleep mode) or either ADC individually to reduce power consumption.

<a id='2e36558f-fd36-482f-a85e-c31664c50994'></a>

## Decimation Stage
For signals with maximum frequencies less than or equal to 3/16 the ADC sampling rate, fADC, the decimate by 2 filter (or half-band filter) can be used to provide on-chip suppression of out-of- band images and noise. When data is present in frequencies greater than 1/4 fADC, the decimate by 2 filter can be disabled by switching the filter out of the circuit. The decimation filter allows the ADC to oversample the input while decreasing the output data rate by half. The two main benefits are a simplification of the input anti-aliasing filter and a slower data interface rate with the external digital ASIC. The decimation filter is an 11 tap filter and suppresses out of band noise by 38 dB.

<a id='9d0415d4-7fcd-4e50-b498-f7a52887c601'></a>

## Hilbert Block
The Hilbert filter is available to provide a Hilbert Transform of the data from the ADC in Channel B. The Digital Hilbert Transform, in combination with an external complex downconverter, enables a receive image rejection architecture (similar to Hartley image rejection architecture). The Hilbert filter pass-band (< 0.1 dB ripple) is between 25% to 75% of the Nyquist rate of its input data rate. The maximum data rate of the Rx Hilbert filter is 32 MSPS. At ADC rates higher than this, the decimation filters should be enabled. The Hilbert filter transfer function plots are shown in Figure 7.

<a id='9987d598-6108-46b2-a897-327045a0749d'></a>

<::chart: A line graph titled "Figure 7. Rx Hilbert Filter, Keeping Positive Frequencies Response". The y-axis is labeled "MAGNITUDE - dB" and ranges from -120 to 0. The x-axis is labeled "NORMALIZED - f_s" and ranges from -0.5 to 0.5. The graph shows the frequency response of a filter. There is a passband from approximately 0.1 to 0.5 on the positive frequency side and from approximately -0.1 to -0.5 on the negative frequency side, with a stopband centered around 0. The stopband exhibits multiple ripples, reaching magnitudes below -100 dB.::>

<a id='0efd4548-6de0-4b7b-881b-abdfb8ce1644'></a>

**Data Output Multiplexer Stage**
The Rx data output format can be configured for either twos
complement or offset binary. This is controlled by the Rx Twos
Complement register.

<a id='cf3d7ac8-3fee-4aa6-aee5-e76b0bf0dfae'></a>

The output data from the dual ADCs can be multiplexed onto a single 10-/12-bit output bus. The multiplexing is synchronized using the RxSYNC output pin that indicates which channel data is on the output bus.

<a id='0c0546ca-5935-4514-ba91-838c48b167e4'></a>

**RECEIVE APPLICATIONS SECTION**
The AD9860/AD9862 receive path (Rx) includes two high speed,
high performance, 10-/12-bit ADCs. Figure 6 shows a detailed
block diagram of the Rx data path and can be referred to through-
out the explanation of the various modes of operation. The various
Rx modes of operation are broken into three parts determined by
the type of input signal:
1. Single Channel ADC Signal
2. Dual Channel Real ADC Signal (diversity or dual channel)
3. Dual Channel Complex ADC Signal (I and Q or Single
Sideband).

<a id='8b9a463d-fd13-4d97-8022-e62c45b7b4f1'></a>

Each one of these parts is further divided into two cases, sampling
input signals up to Nyquist of the ADC (Nyquist sampling) and
sampling at rates above ADC Nyquist rate (IF sampling or
undersampling).

<a id='8498f8c0-5719-4d1b-a592-6ed6c648e210'></a>

The AD9860/AD9862 uses oversampling and decimation filters to ease requirements on external filtering components. The decimation filters (for both receive paths) can be used or bypassed so as to accommodate different signal bandwidths and provide different output data rates to allow easy integration with several different data processing schemes.

<a id='92a332e7-6fde-4916-ae0a-1cbd0fdeceab'></a>

Nonbaseband data can be used in an effort to avoid the dc offsets in the receive signal path that can cause errors. By receiving nonbaseband data, the requirements of external filtering may be greatly reduced.

<a id='ed4e37c5-915c-435d-8c75-252b32c047d2'></a>

In each of the different receive modes, the input buffer, Program- mable Gain Amplifier (RxPGA), and output multiplexer remain within the receive path.

<a id='0a703740-afd2-431e-abb2-8c994a770189'></a>

**Single Channel ADC Signal**
In this mode, a single input signal to be digitized is connected to the differential input pins, VIN+A and VIN-A. The 10-/12-bit output Rx data is latched using either CLKOUT1 or CLKOUT2 edges as defined in the Clock Overview section. The Rx path available options include bypassing the input buffer, Rx PGA control and using the Decimation Filter. By default, both Rx paths are enabled and the unused one should be powered down using the appropriate bit in the Rx Power-Down register, d1.

<a id='db5bfb11-8dc7-4615-acb7-58594dd38306'></a>

The input buffer description above explains the conditions under which the buffer should be bypassed.

<a id='3c893bdb-e6bc-4c4f-9968-7c6c51146498'></a>

If the input signal, or the undersampled alias signal for the
IF sampling case, falls below 40% of the ADC Nyquist rate, the
decimation filter can be enabled to suppress out-of-band noise and
spurious signals by 40 dB or more. With the decimation filter
enabled, the SNR of the Rx path improves by about 2.3 dB.

<a id='e1941c05-6a14-4f88-a172-38b54b7f45fc'></a>

**Dual Channel Real ADC Signal**
The Dual Channel Real ADC Signal mode is used to receive diversity signals or dual independent channel signals that will be processed independent of each other. In this mode, the two input signals to be digitized are connected to the differential input pins of the AD9860/AD9862, VIN+A, VIN-A, VIN+B, and VIN-B. The two 10-/12-bit Rx outputs can be either interleaved onto a single 10-/12-bit bus or output in parallel on two 10-/12-bit buses.

<a id='317b0a75-8961-406e-96a2-57d80f433a94'></a>

REV. 0

<a id='19ed2c1f-5e36-44c1-b592-ea9a2e568446'></a>

-23-

<!-- PAGE BREAK -->

<a id='098c3b09-f02f-482c-bfbb-1a36f4a38b7c'></a>

AD9860/AD9862
The output will be latched using some configuration of CLKOUT1 or CLKOUT2 edges as defined in the Clock Overview section of the data sheet. The Rx path available options include bypassing the input buffer, RxPGA control and using the decimation filter.

<a id='03caf980-4fd6-4a9c-8651-780202840b77'></a>

The input buffer description above explains the conditions under which the buffer should be bypassed.

<a id='bd2a5374-d6bd-4bed-ada8-6bd355bac85b'></a>

If the input signal, or the undersampled alias signal for the IF sampling case, falls below 40% of the ADC Nyquist rate, the decimation filter can be enabled to suppress out-of-band noise and spurious signals by 40 dB or more. With the decimation filter enabled the SNR of the Rx path improves by about 2.3 dB.

<a id='a42d5229-d5b0-4037-86c2-9e831152075f'></a>

**Dual Channel Complex ADC Signal**
The Dual Channel Complex ADC Signal mode is used to receive
baseband I and Q signals or a single sideband signal at some IF.
In this mode, a complex input signal is generated from an external
quadrature demodulator. The in-phase channel (I channel) is
connected to VIN+A and VIN-A, and the Quadrature Data
(Q channel) is connected to the VIN+B and VIN-B differential
pins. The Rx path available options include bypassing the input
buffer, RxPGA control, the decimation filter, and using the digital
Hilbert filter. Shared Reference mode is also discussed below.

<a id='a94aab3b-c15c-4adb-a336-eadddd74d178'></a>

The RxPGA provides 0 dB to 20 dB gain control for both chan-
nels. The input buffer description above explains the conditions
under which the buffer should be bypassed.

<a id='355e543b-86bd-4e9b-8f46-7e08e54f24ea'></a>

If the input signal, or the undersampled alias signal for the IF sam-
pling case, falls below 40% of the ADC Nyquist rate, the decimation
filter can be enabled to suppress out-of-band noise and spurious
signals by 40 dB or more. With the decimation filter enabled,
the SNR of the Rx path improves by about 2.3 dB.

<a id='5a1360e0-29ae-4f14-91c0-d0635e42f0b5'></a>

A digital Hilbert filter can be enabled to provide a receive image rejection architecture on-chip. The digital Hilbert filter combines the I data and a phase shifted version of the Q data to produce a single combined Rx signal. The filter can provide 50 dB image suppression in the pass band (less than 0.1 dB ripple). The pass band of the filter is from 25% to 75% of Nyquist rate of the data entering the Hilbert filter. Note, the Hilbert filter's maximum input data rate is 32 MSPS, at ADC rates above 32 MSPS. The decimation filter is required to reduce the data rate. With the decimation filter also enabled, the pass band of the Hilbert filter will be 12.5% to 37.5% of the ADC Nyquist rate (still 25% to 75% of the Nyquist rate of the data entering the Hilbert filter).

<a id='b6c6ae5a-68a5-4970-98a3-bae2f8248a67'></a>

An optional Shared Reference mode allows the user to connect the
differential references from the dual ADC together externally for
superior gain matching performance. To enable the Shared Ref-
erence mode, the Shared Ref register (d4, b1) should be set high.

<a id='c6c1e580-3ca1-4732-b8e2-bc4fb54ebc99'></a>

TIMING GENERATION BLOCK
The AD9860/AD9862 Timing Generation block uses a single external clock reference to derive all internal clocks to operate the transmit and receive channels. The input clock reference can consist of either an external single ended clock applied to the OSC1 pin, with the OSC2 pin left floating or an external crystal connected between the clock input pins (OSC1 and OSC2).

<a id='c50b8a15-e1c2-4e34-8147-7ffa8aba03cd'></a>

By default, the AD9860/AD9862 can accept either an external reference clock or a crystal to generate the input clock. The internal oscillator, if not used, should be disabled by setting the Input Control Clock register. The OSC1 input impedance is a relatively high resistive impedance (typically, about 500 KΩ).

<a id='489d7864-eca1-4802-ac6b-b2e076f82a8b'></a>

An internal Delay Lock Loop (DLL) based clock multiplier pro-
vides a low noise, 2× or 4× multiplication of the input clock over
an output frequency range of 32 MHz to 128 MHz. The DLL
Fast register should be used to optimize the DLL performance.
For DLL output frequencies between 32 MHz and 64 MHz, this
bit should be set low. For output frequencies between 64 MHz
to 128 MHz, the Fast bit should be set high (for a 64 MHz out-
put frequency, the register can be set either high or low). The DLL
can be bypassed by setting a 1× multiplication factor in the DLL
Multiplier register. The DLL can be powered down when it is
bypassed for power savings by setting the DLL PwrDwn register.

<a id='327cb9ec-66ff-40b6-87ab-9e5a6133c743'></a>

For applications where an external crystal is desired, the AD9860/
AD9862 internal oscillator circuit and the DLL clock multiplier
enable a low frequency, lower cost quartz crystal to be used to
generate the input reference clock. The quartz crystal would be
connected between the OSC1 and OSC2 pins with parallel
resonant load capacitors as specified by the crystal manufacturer.

<a id='192cd3a2-6f75-41d9-80a9-a62f36af122f'></a>

An internal Duty Cycle Stabilizer (DCS) can be enabled on the
AD9860 by setting the Clk Duty register. This provides a stable
50% duty cycle to the ADC for high speed clock rates between
40 MSPS to 64 MSPS when proper duty cycle is more critical.

<a id='e0bd9614-d155-418c-9592-acba9c3c509a'></a>

**System Clock Distribution Circuitry** There are many variables involved in the timing distribution. External variables include CLKIN, CLKOUT1, CLKOUT2, Rx Data Rate, Tx Data Rate. Internal variables include ADC conversion rate, DAC update rate, interpolation rate, decimation rate, Rx data multiplexing and Tx data demultiplexing. Many of these parameters are interrelated and based on CLKIN. Optimal power versus performance and ease of integration options can be chosen to suit a particular application.

<a id='07af821b-1be2-49da-9aa5-dfd5441968ce'></a>

<::block diagram: Normal Operation Timing Block Diagram. The diagram shows two main data paths (Rx and Tx) and a clock path, with a legend indicating solid lines for CLOCK PATH and dashed lines for DATA PATH. The diagram's components are as follows:1. Rx Data Path (Top):  - An ADC (Analog-to-Digital Converter) feeds into a block labeled "NO DECIMATION, ↓2" which represents a filter. This filter is controlled by "DECIMATE: REG D6 B0".  - The output of the filter goes to a "DATA MUX AND LATCH" block.  - The output of the "DATA MUX AND LATCH" is "Rx DATA [0:23]". Associated controls are "MUX OUT: REG D5 B0" and "Rx RETIME: REG D5 B3".2. Tx Data Path (Bottom):  - A DAC (Digital-to-Analog Converter) feeds into a block labeled "NO INTERP ↑2, ↑4" which represents a filter. This filter is controlled by "INTERPOLATION: REG D19 B0, 1".  - The output of the filter goes to a "DATA LATCH AND DEMUX" block.  - The output of the "DATA LATCH AND DEMUX" is "Tx DATA [0:13]". Associated controls are "2 DATA PATHS: REG D19 B4", "Q/I ORDER: REG D18 B5", and "Tx RETIME: REG D18 B6".3. Clock Path (Horizontal and branching):  - An input labeled "CLKIN" splits into two paths:    - Upper path: A "DIV" block with input options "1x, 1/2x". Its output is "CLKSEL".      - "CLKSEL" connects to the ADC.      - "CLKSEL" also connects to an "INV" (Inverter) block, labeled "NO INVERSION, INVERT", which is controlled by "INV1: REG D25 B1". The output of this inverter is "CLKOUT1".    - Lower path: A "DIV" block with input options "1x, 1/2x". It is controlled by "ADC DIV2: REG D24 B5".      - The output of this DIV block feeds into a "DLL" (Delay-Locked Loop) block with input options "1x, 2x, 4x". It is controlled by "DLL MULTIPLIER: REG D24 B3, 4".      - The output of the DLL splits into two paths:        - One path goes to another "DIV" block with input options "1x, 1/2x, 1/4x". It is controlled by "CLKOUT2 DIV FACTOR: REG 25 B6, 7".        - The other path goes to an "INV" (Inverter) block, labeled "NO INVERSION, INVERT", which is controlled by "INV2: REG D25 B5". The output of this inverter is "CLKOUT2".::>Figure 8. Normal Operation Timing Block Diagram

<a id='f1103d68-c9f6-4b85-bd58-c7d8fcb51ea6'></a>

One of two possible timing operation modes can be selected. The typical timing mode is called Normal Operation mode; a block diagram is shown in Figure 8. The other mode is called Alternative Operation mode, and a block diagram is shown in Figure 12.

<a id='36004a1d-a83f-4bcf-b343-17b696a88032'></a>

-24-

<a id='a8bdb07f-efdc-4bfd-991b-f614b9904693'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='73329e44-c4e7-480d-a810-0654894da652'></a>

--- 

AD9860/AD9862

<a id='4cacc85e-0594-4f1d-bde5-dbe430cbc6cf'></a>

Table I. Rx Data Timing Table

<a id='e371ed75-86cb-42df-9efb-83be3c7e8f6b'></a>

Table Ia. CLKSEL Set Logic Low

<table id="24-1">
<tr><td id="24-2">CLKSEL</td><td id="24-3">ADC Div 2</td><td id="24-4">Decimate</td><td id="24-5">Multiplex</td><td id="24-6">See Figure 8 for Relative Timing</td></tr>
<tr><td id="24-7" rowspan="8">Low</td><td id="24-8" rowspan="4">No Div</td><td id="24-9" rowspan="2">No Decimation</td><td id="24-a">No Mux</td><td id="24-b">Timing No. 4 Rx Data = 2 × CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-c">Mux</td><td id="24-d">Not Allowed</td></tr>
<tr><td id="24-e" rowspan="2">Decimation</td><td id="24-f">No Mux</td><td id="24-g">Timing No. 3 Rx Data = 2 × CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-h">Mux</td><td id="24-i">Timing No. 4 Rx Data (MUXED) = 2 × CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-j" rowspan="4">Div</td><td id="24-k" rowspan="2">NoDecimation</td><td id="24-l">No Mux</td><td id="24-m">Timing No. 3 Rx Data = CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-n">Mux</td><td id="24-o">Timing No. 4 Rx Data(MUXED) = 2 × CLKOUT1 CLOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-p" rowspan="2">Decimation</td><td id="24-q">No Mux</td><td id="24-r">Timing No. 2 Rx Data = 1/2 × CLKOUT1 CLOUT1 = 1/2 × CLKIN</td></tr>
<tr><td id="24-s">Mux</td><td id="24-t">Timing No. 3 Rx Data(MUXED) = CLKOUT1 CLKOUT1 = 1/2 × CLKIN</td></tr>
</table>

<a id='3b6c5d0e-e776-4e08-b163-0346f92bad40'></a>

Table Ib. CLKSEL Set Logic High
<table id="24-u">
<tr><td id="24-v">CLKSEL</td><td id="24-w">ADC Div 2</td><td id="24-x">Decimate</td><td id="24-y">Multiplex</td><td id="24-z">See Figure 8 for Relative Timing</td></tr>
<tr><td id="24-A" rowspan="8">High</td><td id="24-B" rowspan="4">No Div</td><td id="24-C" rowspan="2">No Decimation</td><td id="24-D">No Mux</td><td id="24-E">Timing No. 3 Rx Data = CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-F">Mux</td><td id="24-G">Timing No. 4 Rx Data(MUXED) = 2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-H" rowspan="2">Decimation</td><td id="24-I">No Mux</td><td id="24-J">Timing No. 2 Rx Data = 1/2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-K">Mux</td><td id="24-L">Timing No. 3 Rx Data(MUXED) = CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-M" rowspan="4">Div</td><td id="24-N" rowspan="2">No Decimation</td><td id="24-O">No Mux</td><td id="24-P">Timing No. 2 Rx Data = 1/2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
<tr><td id="24-Q">Mux</td><td id="24-R">Timing No. 3 Rx Data(MUXED) = CLKOUT1 CLOUT1 = CLKIN</td></tr>
<tr><td id="24-S" rowspan="2">Decimation</td><td id="24-T">No Mux</td><td id="24-U">Timing No. 1 Rx Data = 1/4 × CLKOUT1 CLOUT1 = CLKIN</td></tr>
<tr><td id="24-V">Mux</td><td id="24-W">Timing No. 2 Rx Data (MUXED) = 1/2 × CLKOUT1 CLKOUT1 = CLKIN</td></tr>
</table>

<a id='42cb4dce-8254-4a3b-9038-2c5aede39f90'></a>

<::Timing diagram: A timing diagram showing fCLKOUT1 as a square wave clock signal. Below it are four Rx DATA TIMING signals, each with a different frequency relative to CLKOUT. Rx DATA TIMING No. 1 has fRx = CLKOUT ÷ 4, showing one data period (represented by an 'X' transition) over four clock cycles. Rx DATA TIMING No. 2 has fRx = CLKOUT ÷ 2, showing one data period over two clock cycles. Rx DATA TIMING No. 3 has fRx = CLKOUT, showing one data period per clock cycle. Rx DATA TIMING No. 4 has fRx = 2 × CLKOUT, showing two data periods per clock cycle. Vertical lines indicate timing relationships between the signals. Timing parameters tRx1, tRx2, and tRx3 are shown at the bottom, measuring delays and durations relative to the transitions.::>Figure 9. Rx Timing Diagram

<a id='977fc1e4-28e8-4a2e-96eb-2be34fe76073'></a>

<::Block Diagram: Single Tx Timing, Alternative Operation::> CLKIN (input) connects to an 'ADC DIV2' block. Input to ADC DIV2 is labeled 'A'. Inside the block: 0: B = A, 1: B = A/2. The output of ADC DIV2, labeled 'B', connects to a 'DLL MULT' block. Inside the DLL MULT block: 00: C = B, 01: C = B/2, 10: C = B/4. The output of DLL MULT, labeled 'C', connects to a 'CLKOUT2 DIV' block. Inside the CLKOUT2 DIV block: 00: D = C, 01: D = C/2, 10: D = C/4. The output of CLKOUT2 DIV, labeled 'D', connects to an 'INTERP' block. Inside the INTERP block: 00: E = D, 01: E = 2 x D, 10: E = 4 x D. The output of INTERP is labeled 'E' and goes to 'TxDAC UPDATE RATE SINGLE CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)'. There are also outputs from the main signal path: - From CLKIN, an output labeled 'ADC SAMPLE RATE (NOT TO EXCEED 64MHz)'. - From the output of ADC DIV2 (B), an output labeled 'DLL OUTPUT RATE (NOT TO EXCEED 128MHz)'. - From the output of DLL MULT (C), an output labeled 'CLKOUT2'. - From the output of CLKOUT2 DIV (D), an output labeled 'INPUT Tx DATA RATE (SINGLE CHANNEL)'. Figure 10. Single Tx Timing Block Diagram, Alternative Operation

<a id='cdae84f0-6b82-4ba0-9f8f-48508c8255da'></a>

REV. 0

<a id='f490a056-eff6-46b1-b7b3-3e44ce82c4fc'></a>

-25-

<!-- PAGE BREAK -->

<a id='a4a2353b-acb0-46c8-8099-011ecaed73bf'></a>

AD9860/AD9862

For the Normal Operation mode, the Tx timing is based on a clock derived from the DLL output, while the Rx clock is unaffected by the DLL setting.

<a id='0bb37949-9001-4b74-b018-fa08a685cbbc'></a>

The Alternative Operation mode, timing utilizes the output of
the DLL to generate both Rx and Tx clocks. It also sets default
operation of the DLL to 4× mode.

<a id='f6a91e2e-f6ad-4168-b80d-a9b22c237f6a'></a>

Normal Operation is typically recommended because the Rx ADC is more sensitive to the jitter and noise that the DLL may gener- ate, so its performance may degrade. The Mode/TxBlank pin logic level at power up or RESET defines in which mode the device powers up. If Mode/TxBlank is low at power up, the Normal Operation mode is configured. Otherwise, the Alternative Operation mode is configured.

<a id='e08c6693-7740-40d3-94a2-38dddd7ba580'></a>

**Rx Path (Normal Operation)**
The ADC sampling rate, the Rx data output rate, and the rate of
CLKOUT1 (clock used to latch output data) are the parameters
of interest for the receive path data. These parameters in addition
to the data bandwidth are related to CLKIN by decimation filters,
divide by two circuits, data multiplexer logic and retiming latches.
The Rx path timing can be broken into two separate relation-
ships: the ADC sample rate relative to the input clock, CLKIN
and the output data rate relative to CLKOUT1.

<a id='bbf780e4-df05-4417-a822-61874aa7a284'></a>

The ADCs sample rate relative to CLKIN is controlled by the
ADC Div2 register and the sample rate can be equal to or one half
of the input clock rate.

<a id='013db6e2-2b58-4287-95eb-861f7e9f6eab'></a>

The output data relative to CLKOUT1 has many configurations providing a flexible interface. The different options are shown in Figure 8. Table Ia and Ib describe the setup required to obtain the desired data timing. RxSync is available when the Rx data is decimated and multiplexed to identify which channel data is present at the output bus.

<a id='4ff1cc47-b87d-47ad-8cb5-63e7e5b14f46'></a>

The Rx data (unless re-timed using the Rx Retime register) is timed relative to the CLKOUT1 pin output. The Rx output data can be decimated (halving the data rate) or both channels can be multiplexed onto the channel A data bus (doubling the data rate).

<a id='d66a6402-a6e8-4406-9a2f-3436334f9025'></a>

Decimation enables oversampling while maintaining a slower external data transfer rate and provides superior suppression of out of band signals and noise. Multiplexing enables fewer digital output bits to be used to transfer data from the Rx path to the digital ASIC collecting the data.

<a id='80d3ceca-9e77-4e74-916a-8193866a61ad'></a>

When Mux Mode is enabled with an output data rate equal to CLKOUT1 (Timing No. 3 in Figure 9) then the RxSync pin is required to identify which channel's output data is on the output data bus. RxSync output is aligned with the output data, and by default a logic low indicates data from Rx Channel B is currently on the output data bus. If RxSync is logic high, then data from Rx Channel A is currently on the output data bus. The Inv RxSync register can be used to switch this notation.

<a id='ba10500d-b4c4-48d8-a0d1-4966bddd2610'></a>

The CLKOUT1 pin outputs a clock at the frequency of CLKIN or CLKIN/2 depending on the voltage level applied to the CLKSEL pin. If a logic low is applied to CLKSEL, CLKOUT1 will run at half the CLKIN rate, if CLKSEL is set to logic high CLKOUT1 outputs a clock equal to CLKIN.

<a id='1c67e942-243a-4290-93bf-0043aafab997'></a>

This timing flexibility along with the invert option for CLKOUT1,
controlled by the Inv 1 register allow for various methods of latch-
ing data from the Rx path to the digital ASIC, which will process
the data. These options are shown in Table Ia and Ib along with
a timing diagram in Figure 9. Not shown is the option to invert
CLKOUT1, controlled by the Inv 1 register. For this mode, relative
timing remains the same except the opposite edges of CLKOUT1
would be used.

<a id='3130494f-54ba-49e0-baf5-386877249687'></a>

<::block diagram: Dual Tx Timing Block Diagram, Alternative Operation::>ADC DIV2 block. Input is CLKIN (A). Output is B. Operations: 0: B = A, 1: B = A/2. An output line from this block indicates "ADC SAMPLE RATE (NOT TO EXCEED 64MHz)". An arrow points from ADC DIV2 (B) to DLL MULT (B).DLL MULT block. Input is B. Output is C. Operations: 00: C = B, 01: C = 2 × B, 10: C = 4 × B. An output line from this block indicates "DLL OUTPUT RATE (NOT TO EXCEED 128MHz)". An arrow points from DLL MULT (C) to CLKOUT2 DIV (C).CLKOUT2 DIV block. Input is C. Output is D. Operations: 00: D = C, 01: D = C/2, 10: D = C/4. An output line from this block indicates "CLKOUT2". An arrow points from CLKOUT2 DIV (D) to 2 EDGES (D).2 EDGES block. Input is D. Output is E. Operations: 0: E = D, 1: E = 2 × D. An output line from this block indicates "INPUT Tx DATA RATE". An arrow points from 2 EDGES (E) to DUAL CHANNEL FACTOR (E).DUAL CHANNEL FACTOR block. Input is E. Output is F. Operation: F = E/2. An arrow points from DUAL CHANNEL FACTOR (F) to INTERP (F). An output line from F before INTERP indicates "INPUT Tx DATA RATE EACH CHANNEL".INTERP block. Input is F. Output is G. Operations: 00: G = F, 01: G = 2 × F, 10: G = 4 × F. An output line from this block indicates "TxDAC UPDATE RATE EACH CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)".

<a id='1c5adaaa-b3f1-4783-bbb7-2c050fcf9ba0'></a>

<::A timing diagram showing three waveforms. The top waveform is a square wave labeled f_CLKOUT2. Below it is "Tx DATA TIMING No. 1" with f_Tx = CLKOUT2, represented by a series of eye patterns. Below that is "Tx DATA TIMING No. 2" with f_Tx = 2 × CLKOUT2, also represented by eye patterns, but with transitions occurring twice as frequently. Vertical lines indicate timing relationships between the signals. Horizontal double-headed arrows with labels f_Tx1, f_Tx2, f_Tx3, and f_Tx4 denote specific timing intervals between transitions. Figure 12. Tx Timing Diagram::>

<a id='d116bbb6-6feb-461e-ad75-848e62807ce3'></a>

-26-

<a id='68e75879-92dd-4a47-b67b-ffd9b51281e9'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='fcc7f589-1437-4eca-b5ed-ee30cc672379'></a>

AD9860/AD9862

<a id='81ebee92-3dbd-4048-ab3d-8d5fcf53d25f'></a>

Tx Path (Normal Operation)
The DAC update rate, the Tx input data rate, and the rate of
CLKOUT2 (clock used to latch Tx input data) are the parameters
of interest for the transmit path data. These parameters, in addition
to the output signal bandwidth, are related to CLKIN by the settings
of the ADC Div2, the DLL multiplier, the CLKOUT2 Div, the
two edges, and the interpolation registers.

<a id='93093ace-b283-47ac-8905-13e2233c6742'></a>

The Tx data is timed relative to the CLKOUT2 pin (unless it is retimed relative to CLKOUT1 by setting Tx Retime register) and the input Tx data is latched on either each rising edge, each falling edge or both edges (controlled through the Inverse Sample and two edges registers). The timing diagrams for these cases are shown in Figure 12.

<a id='d6e82f48-33e7-4c84-bac7-f3092d9a326a'></a>

The Dual Tx data is multiplexed onto a single bus so that fewer digital bits are necessary to transfer data. Throughout this discus-sion of Tx path timing, Tx digital processing options other than interpolation are ignored because they do not change data timing; Tx data timing reflects whether single or dual channel data is latched into the AD9860/AD9862.

<a id='5cafaf4a-e731-493e-b008-ecf60c15a0a7'></a>

The rates of CLKOUT2 (and the input data rate) are related
to CLKIN by the DLL Multiplier Register, the setting of the
CLKOUT2 Divide Factor Register and the register ADC Div2.
These relationships are shown in Table II.

<a id='cda7a8c1-eaef-436a-aba3-d3f8773c0c26'></a>

Table II. CLKOUT2 Timing Relative to CLKIN
for Normal Operation Mode
<table id="26-1">
<tr><td id="26-2">CLK DIV2</td><td id="26-3">DLL Mult</td><td id="26-4">CLKOUT2 Div Factor</td><td id="26-5">CLKOUT2</td></tr>
<tr><td id="26-6" rowspan="9">No Div</td><td id="26-7" rowspan="3">1×</td><td id="26-8">/1</td><td id="26-9">CLKIN</td></tr>
<tr><td id="26-a">/2</td><td id="26-b">CLKIN/2</td></tr>
<tr><td id="26-c">/4</td><td id="26-d">CLKIN/4</td></tr>
<tr><td id="26-e" rowspan="3">2×</td><td id="26-f">/1</td><td id="26-g">2×CLKIN</td></tr>
<tr><td id="26-h">/2</td><td id="26-i">CLKIN</td></tr>
<tr><td id="26-j">/4</td><td id="26-k">CLKIN/2</td></tr>
<tr><td id="26-l" rowspan="3">4×</td><td id="26-m">/1</td><td id="26-n">4XCLKIN</td></tr>
<tr><td id="26-o">/2</td><td id="26-p">2XCLKIN</td></tr>
<tr><td id="26-q">/4</td><td id="26-r">CLKIN</td></tr>
<tr><td id="26-s" rowspan="9">Div by 2</td><td id="26-t" rowspan="3">1×</td><td id="26-u">/1</td><td id="26-v">CLKIN/2</td></tr>
<tr><td id="26-w">/2</td><td id="26-x">CLKIN/4</td></tr>
<tr><td id="26-y">/4</td><td id="26-z">CLKIN/8</td></tr>
<tr><td id="26-A" rowspan="3">2×</td><td id="26-B">/1</td><td id="26-C">CLKIN</td></tr>
<tr><td id="26-D">/2</td><td id="26-E">CLKIN/2</td></tr>
<tr><td id="26-F">/4</td><td id="26-G">CLKIN/4</td></tr>
<tr><td id="26-H" rowspan="3">4×</td><td id="26-I">/1</td><td id="26-J">2xCLKIN</td></tr>
<tr><td id="26-K">/2</td><td id="26-L">CLKIN</td></tr>
<tr><td id="26-M">/4</td><td id="26-N">CLKIN/2</td></tr>
</table>

<a id='1102a264-bb86-485f-b7e3-59a070a3b9d5'></a>

<::block diagram: Alternative Operation Timing Block Diagram::>CLKIN input feeds into a DLL block labeled "DLL MULTIPLIER: REG D24 B3, 4".The output of the DLL splits into multiple paths.One path goes to a "DIV" block labeled "1x, 2x, 4x" which is connected to CLKSEL.The CLKSEL output connects to another "DIV" block labeled "1x, 1/2x" for ADC. This "DIV" block is further labeled "ADC DIV2: REG D24 B5".The output of this "DIV" block goes to an "ADC" block.The output of the "ADC" block (dashed line, DATA PATH) goes to a filter symbol labeled "NO DECIMATION, ↓2" with "DECIMATE: REG D6 B0".This filter output then goes to a "DATA MUX AND LATCH" block labeled "MUX OUT: REG D5 B0" and "Rx RETIME: REG D5 B3".The output of the "DATA MUX AND LATCH" block is "Rx DATA [0:23]".Another path from the DLL output goes to a "DIV" block labeled "1x, 1/2x".The output of this "DIV" block goes to an "INV" block labeled "NO INVERSION, INVERT" and "INV1: REG D25 B1".The output of this "INV" block is "CLKOUT1".A third path from the DLL output goes to a "DIV" block labeled "1x, 1/2x, 1/4x" and "CLKOUT2 DIV FACTOR: REG 25 B6, 7".The output of this "DIV" block goes to an "INV" block labeled "NO INVERSION, INVERT" and "INV2: REG D25 B5".The output of this "INV" block is "CLKOUT2".Additionally, the CLKIN input feeds into a "DAC" block.The output of the "DAC" block (dashed line, DATA PATH) goes to a filter symbol labeled "NO INTERP, ↑2, ↑4" with "INTERPOLATION: REG D19 B0, 1".This filter output then goes to a "DATA LATCH AND DEMUX" block labeled "2 DATA PATHS: REG D19 B4", "Q/I ORDER: REG D18 B5", and "Tx RETIME: REG D18 B6".The output of the "DATA LATCH AND DEMUX" block is "Tx DATA [0:13]".A legend at the bottom left indicates:"--- CLOCK PATH" (solid line)"--- DATA PATH" (dashed line)Figure 13. Alternative Operation Timing Block Diagram

<a id='ac930a71-66f7-4a55-b875-dcc2ac908e04'></a>

REV. 0

<a id='987e608a-6ef5-4126-b727-736e55c76d37'></a>

-27-

<!-- PAGE BREAK -->

<a id='16cce169-abdc-45e9-90e3-36bdf5e7899e'></a>

AD9860/AD9862

The timing block diagrams in Figures 10 and 11 show how the various clocks of the single and dual Tx path are affected by the various register settings.

<a id='a42f7cb2-ecf5-4fc8-8e4a-9e80cabab83d'></a>

For dual Tx data, an option to redirect demultiplexed data to
either path is available. For example, the AD9860/AD9862 can
accept complex data in the form of I then Q data or Q then I data,
controlled through QI Order register.

<a id='bce8fa1a-ad79-43eb-96f2-7fbe239729a2'></a>

For the dual Tx data cases, the Tx_SYNC Pin input logic level defines what data is currently on the Tx data bus. By default, when Tx_SYNC is low, Channel A data (first of the set) should be on the data bus; if TxSYNC is high, Channel B data (or the second of the set) should be on the Tx bus. This can be reversed be setting the Inv TxSYNC register.

<a id='5430d899-9264-43f1-b6b9-2413346eb8db'></a>

**Rx Path (Alternative Timing Operation)**
The ADC sampling rate, the Rx data output rate and the rate of CLKOUT1 (clock used to latch output data) are the parameters of interest for the receive path data. These parameters, in addition to the data bandwidth, are related to CLKIN by decimation filters, divide by two circuits, data multiplexer logic retiming latches and also the DLL multiplication setting (which is not the case for Normal Operation mode). This mode can be configured by default by forcing the Tx_Blank_In pin to a logic high level during power up.

<a id='aa13c3a5-7407-456e-b3fe-65571664e3f2'></a>

The Rx path timing can be broken into two separate relationships:
the ADC sample rate relative to the input clock, CLKIN and
the output data rate relative to CLKOUT1.

<a id='8165c49b-d84a-41e9-a2e2-84de7a8a026f'></a>

The ADCs sample rate relative to CLKIN is controlled by the ADC Div2 register and the DLL Multiplier register. The sample rate can be equal to or one half of the DLL output clock rate.

<a id='b48d24b6-dd6a-4293-b42e-95d5f3166d1f'></a>

The output data rate relative to CLKOUT1 for the Alternative
Operation Mode has the same configuration options as in the
Normal Operation Mode. The different options are shown in
Figure 9. Table Ia. and Ib. describe the setup required to obtain
the desired data timing.

<a id='3fb16e94-a751-46c9-a374-593799250d96'></a>

The Rx data (unless retimed using the Rx Retime register) is timed relative to the CLKOUT1 pin output. The Rx output data can be decimated (halving the data rate) or both channels can be multiplexed onto the Channel A data bus (doubling the data rate).

<a id='9be4b0bb-5805-4272-a2c1-17893851c5cb'></a>

Decimation enables oversampling while maintaining a slower external data transfer rate and provides superior suppression of out of band signals and noise. Multiplexing enables fewer digital output bits to be used to transfer data from the Rx path to the digital ASIC collecting the data.

<a id='b109bf77-46a3-4f2f-bc82-24c4e7a7424c'></a>

When Multiplexing mode is enabled with an output data rate equal to CLKOUT1 (Timing No. 3 in Figure 9), then the RxSync pin is required to identify which channel's output data is on the output data bus. RxSync output is aligned with the output data and by default, a logic low indicates data from Rx Channel B is currently on the output data bus. If RxSync is logic high, then data from Rx Channel A is currently on the output data bus. The Inv RxSync register can be used to switch this notation.

<a id='a68571d2-1aee-462b-aad3-91756ff77555'></a>

The CLKOUT1 pin outputs a clock at a frequency of CLKIN or CLKIN/2 depending on the voltage level applied to the CLKSEL

<a id='774c3831-4b5b-4e74-b345-361127403f48'></a>

pin. If a logic low is applied to CLKSEL, CLKOUT1 will run at half the CLKIN rate; if CLKSEL is set to logic high, CLKOUT1 outputs a clock equal to CLKIN.

<a id='b5dcba5a-e6a4-4e21-a07d-758f2405d846'></a>

This timing flexibility, along with the invert option for CLKOUT1 controlled by the Inv 1 Register, allows for various methods of latching data from the Rx path to the digital ASIC, which will pro-cess the data. These options are shown in Table Ia and Ib along with a timing diagram in Figure 9. Not shown is the option to invert CLKOUT1, controlled by the Inv 1 register. For this mode, relative timing remains the same except the opposite edges of CLKOUT1 would be used.

<a id='a90d549d-6054-486d-96f4-de17d514c99e'></a>

Overall, relative timing can be found by using the Alternative
Operation Mode Master Timing Guide in Table V and using Rx
timing shown in Figure 9.

<a id='1d660943-67f5-4fa8-9529-ac5d146de8c5'></a>

**Tx Path (Alternative Timing Operation)**
The DAC update rate, the Tx input data rate and the rate of CLKOUT2 (clock used to latch Tx input data) are the parameters of interest for the transmit path data. These parameters in addition to the output signal bandwidth are related to CLKIN by the settings of the DLL multiplier, the CLKOUT2 Div, the two edge and the Interpolation registers (in this mode, the ADC Div2 register does not affect Tx timing).

<a id='98a0be30-b95d-4c1c-ab0e-1bebf8224188'></a>

The Tx data is timed relative to the CLKOUT2 pin (unless it is retimed relative to CLKOUT1 by setting Tx Retime register) and remains the same as it does in Normal Operation Mode. The input Tx data is latched on each rising edge, each falling edge or both edges (controlled through the Inverse Sample and two edge regis- ters). The timing diagrams for these cases are shown in Figure 12.

<a id='483213b5-e948-4447-a683-45283d52290a'></a>

The Dual Tx data is multiplexed onto a single bus so that fewer
digital bits are necessary to transfer data. Throughout this discus-
sion of Tx path timing, Tx digital processing options other than
interpolation are ignored because they do not change data timing;
Tx data timing reflects whether single or dual channel data is
latched into the AD9860/AD9862.

<a id='de6c25a1-9219-41b5-add9-c75fa12aa8b8'></a>

The rates of CLKOUT2 (and the input data rate) are related to CLKIN by the DLL Multiplier register and the setting of the CLKOUT2 Divide Factor register. These relationships are shown in Table III.

<a id='51d68241-ecb4-43b0-b014-b34aa4a75aa5'></a>

Table III. CLKOUT2 Timing Relative to CLKIN
In Alternative Operation Mode
<table id="27-1">
<tr><td id="27-2">DLL Mult</td><td id="27-3">CLKOUT2 Div Factor</td><td id="27-4">CLKOUT2</td></tr>
<tr><td id="27-5">1X</td><td id="27-6">/1</td><td id="27-7">CLKIN</td></tr>
<tr><td id="27-8"></td><td id="27-9">/2</td><td id="27-a">CLKIN/2</td></tr>
<tr><td id="27-b"></td><td id="27-c">/4</td><td id="27-d">CLKIN/4</td></tr>
<tr><td id="27-e">2X</td><td id="27-f">/1</td><td id="27-g">2×CLKIN</td></tr>
<tr><td id="27-h"></td><td id="27-i">/2</td><td id="27-j">CLKIN</td></tr>
<tr><td id="27-k"></td><td id="27-l">/4</td><td id="27-m">CLKIN/2</td></tr>
<tr><td id="27-n">4X</td><td id="27-o">/1</td><td id="27-p">4XCLKIN</td></tr>
<tr><td id="27-q"></td><td id="27-r">/2</td><td id="27-s">2XCLKIN</td></tr>
<tr><td id="27-t"></td><td id="27-u">/4</td><td id="27-v">CLKIN</td></tr>
</table>

<a id='1dd479a8-cb10-41da-96bf-ac1688ab1398'></a>

-28-

<a id='272dac48-e753-4142-b20c-a9d584330d6e'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='cdf9f290-bd0c-4b9c-a6c5-8c0abcac466d'></a>

--- AD9860/AD9862

<a id='479ff7d7-8e40-44f1-b8ef-ba343c6248a9'></a>

Table IV. Normal Operation Mode Master Timing Guide
<table id="28-1">
<tr><td id="28-2" rowspan="3">ADC2</td><td id="28-3" rowspan="3">DLL Mult</td><td id="28-4" rowspan="3">ADC Clock Rate</td><td id="28-5" colspan="4">ADC Data Rate¹ (MSPS)</td><td id="28-6" rowspan="3">DAC Update Rate</td><td id="28-7" rowspan="2" colspan="3">Dual DAC Data Rate² (MSPS)</td><td id="28-8" rowspan="2" colspan="2">CLKOUT1</td><td id="28-9" rowspan="2" colspan="3">CLKOUT2</td></tr>
<tr><td id="28-a" colspan="2">Non-MUX Mode</td><td id="28-b" colspan="2">MUX Mode</td></tr>
<tr><td id="28-c">No Deci</td><td id="28-d">Deci by 2</td><td id="28-e">No Deci</td><td id="28-f">Deci by 2</td><td id="28-g">1X Interp</td><td id="28-h">2X Interp</td><td id="28-i">4X Interp</td><td id="28-j">CLKSEL = Low</td><td id="28-k">CLKSEL = High</td><td id="28-l">CLKDIV = 1X</td><td id="28-m">CLKDIV = 1/2X</td><td id="28-n">CLKDIV = 1/4X</td></tr>
<tr><td id="28-o">0</td><td id="28-p">1X</td><td id="28-q" rowspan="3">CLKIN</td><td id="28-r" rowspan="3">CLKIN</td><td id="28-s" rowspan="3">CLKIN ÷ 2</td><td id="28-t" rowspan="3">2× CLKIN</td><td id="28-u" rowspan="3">CLKIN</td><td id="28-v">CLKIN</td><td id="28-w">2X CLKIN</td><td id="28-x">CLKIN</td><td id="28-y">CLKIN ÷ 2</td><td id="28-z" rowspan="6">CLKIN</td><td id="28-A" rowspan="6">CLKIN ÷2</td><td id="28-B">CLKIN</td><td id="28-C">CLKIN ÷ 2</td><td id="28-D">CLKIN ÷ 4</td></tr>
<tr><td id="28-E">0</td><td id="28-F">2X</td><td id="28-G">2X CLKIN</td><td id="28-H">4X CLKIN</td><td id="28-I">2X CLKIN</td><td id="28-J">CLKIN</td><td id="28-K">2X CLKIN</td><td id="28-L">CLKIN</td><td id="28-M">CLKIN ÷ 2</td></tr>
<tr><td id="28-N">0</td><td id="28-O">4X</td><td id="28-P">4X CLKIN</td><td id="28-Q">8X CLKIN</td><td id="28-R">4X CLKIN</td><td id="28-S">2× CLKIN</td><td id="28-T">4× CLKIN</td><td id="28-U">2× CLKIN</td><td id="28-V">CLKIN</td></tr>
<tr><td id="28-W">1</td><td id="28-X">1X</td><td id="28-Y" rowspan="3">CLKIN ÷ 2</td><td id="28-Z" rowspan="3">CLKIN ÷ 2</td><td id="28-10" rowspan="3">CLKIN ÷ 4</td><td id="28-11" rowspan="3">CLKIN</td><td id="28-12" rowspan="3">CLKIN ÷ 2</td><td id="28-13">CLKIN ÷2</td><td id="28-14">CLKIN</td><td id="28-15">CLKIN ÷2</td><td id="28-16">CLKIN ÷ 4</td><td id="28-17">CLKIN ÷ 2</td><td id="28-18">CLKIN ÷ 4</td><td id="28-19">CLKIN ÷ 8</td></tr>
<tr><td id="28-1a">1</td><td id="28-1b">2X</td><td id="28-1c">CLKIN</td><td id="28-1d">2X CLKIN</td><td id="28-1e">CLKIN</td><td id="28-1f">CLKIN ÷ 2</td><td id="28-1g">CLKIN</td><td id="28-1h">CLKIN ÷ 2</td><td id="28-1i">CLKIN ÷ 4</td></tr>
<tr><td id="28-1j">1</td><td id="28-1k">4X</td><td id="28-1l">2X CLKIN</td><td id="28-1m">4X CLKIN</td><td id="28-1n">2X CLKIN</td><td id="28-1o">CLKIN</td><td id="28-1p">2× CLKIN</td><td id="28-1q">CLKIN</td><td id="28-1r">CLKIN ÷ 2</td></tr>
</table>
NOTES
1 100 MHz rate max.
2 Single DAC data rate = 1/2 dual DAC data rate.

<a id='c091d8d0-ea98-4215-b71d-9eb03dc40cde'></a>

Table V. Alternative Operation Mode Master Timing Guide
<table id="28-1s">
<tr><td id="28-1t" rowspan="3">ADC2</td><td id="28-1u" rowspan="3">DLL Mult</td><td id="28-1v" rowspan="3">ADC Clock Rate</td><td id="28-1w" colspan="4">ADC Data Rate¹ (MSPS)</td><td id="28-1x" rowspan="3">DAC Update Rate</td><td id="28-1y" rowspan="2" colspan="3">Dual DAC Data Rate2 (MSPS)</td><td id="28-1z" rowspan="2" colspan="2">CLKOUT1</td><td id="28-1A" rowspan="2" colspan="3">CLKOUT2</td></tr>
<tr><td id="28-1B" colspan="2">Non-MUX Mode (two buses)</td><td id="28-1C" colspan="2">MUX Mode (one bus)</td></tr>
<tr><td id="28-1D">No Deci</td><td id="28-1E">Deci by 2</td><td id="28-1F">No Deci</td><td id="28-1G">Deci by 2</td><td id="28-1H">1× Interp</td><td id="28-1I">2× Interp</td><td id="28-1J">4X Interp</td><td id="28-1K">CLKSEL = Low</td><td id="28-1L">CLKSEL = High</td><td id="28-1M">CLKDIV = 1X</td><td id="28-1N">CLKDIV = 1/2X</td><td id="28-1O">CLKDIV = 1/4X</td></tr>
<tr><td id="28-1P">0</td><td id="28-1Q">1X</td><td id="28-1R">CLKIN</td><td id="28-1S">CLKIN</td><td id="28-1T">CLKIN ÷ 2</td><td id="28-1U">2× CLKIN</td><td id="28-1V">CLKIN</td><td id="28-1W">CLKIN</td><td id="28-1X">2× CLKIN</td><td id="28-1Y">CLKIN</td><td id="28-1Z">CLKIN ÷ 2</td><td id="28-20">CLKIN</td><td id="28-21">CLKIN ÷ 2</td><td id="28-22">CLKIN</td><td id="28-23">CLKIN ÷ 2</td><td id="28-24">CLKIN ÷4</td></tr>
<tr><td id="28-25">0</td><td id="28-26">2X</td><td id="28-27">2X CLKIN</td><td id="28-28">2X CLKIN</td><td id="28-29">CLKIN</td><td id="28-2a">4× CLKIN</td><td id="28-2b">2× CLKIN</td><td id="28-2c">2× CLKIN</td><td id="28-2d">4× CLKIN</td><td id="28-2e">2× CLKIN</td><td id="28-2f">2x CLKIN</td><td id="28-2g">CLKIN</td><td id="28-2h">CLKIN</td><td id="28-2i">2X CLKIN</td><td id="28-2j">CLKIN</td><td id="28-2k">CLKIN ÷2</td></tr>
<tr><td id="28-2l">0</td><td id="28-2m">4X</td><td id="28-2n">4X CLKIN</td><td id="28-2o">4X CLKIN</td><td id="28-2p">2X CLKIN</td><td id="28-2q">8X CLKIN</td><td id="28-2r">4X CLKIN</td><td id="28-2s">4X CLKIN</td><td id="28-2t">8X CLKIN</td><td id="28-2u">4X CLKIN</td><td id="28-2v">2X CLKIN</td><td id="28-2w">4X CLKIN</td><td id="28-2x">2X CLKIN</td><td id="28-2y">4X CLKIN</td><td id="28-2z">2X CLKIN</td><td id="28-2A">CLKIN</td></tr>
<tr><td id="28-2B">1</td><td id="28-2C">1X</td><td id="28-2D">CLKIN ÷ 2</td><td id="28-2E">CLKIN ÷ 2</td><td id="28-2F">CLKIN ÷ 4</td><td id="28-2G">CLKIN</td><td id="28-2H">CLKIN ÷ 2</td><td id="28-2I">CLKIN</td><td id="28-2J">2X CLKIN</td><td id="28-2K">CLKIN</td><td id="28-2L">CLKIN ÷ 2</td><td id="28-2M">CLKIN</td><td id="28-2N">CLKIN ÷ 2</td><td id="28-2O">CLKIN</td><td id="28-2P">CLKIN ÷ 2</td><td id="28-2Q">CLKIN ÷ 4</td></tr>
<tr><td id="28-2R">1</td><td id="28-2S">2X</td><td id="28-2T">CLKIN</td><td id="28-2U">CLKIN</td><td id="28-2V">CLKIN ÷ 2</td><td id="28-2W">2X CLKIN</td><td id="28-2X">CLKIN</td><td id="28-2Y">2X CLKIN</td><td id="28-2Z">4X CLKIN</td><td id="28-30">2X CLKIN</td><td id="28-31">CLKIN</td><td id="28-32">2x CLKIN</td><td id="28-33">CLKIN</td><td id="28-34">2X CLKIN</td><td id="28-35">CLKIN</td><td id="28-36">CLKIN ÷ 2</td></tr>
<tr><td id="28-37">1</td><td id="28-38">4X</td><td id="28-39">2X CLKIN</td><td id="28-3a">2X CLKIN</td><td id="28-3b">CLKIN</td><td id="28-3c">4X CLKIN</td><td id="28-3d">2X CLKIN</td><td id="28-3e">4X CLKIN</td><td id="28-3f">8X CLKIN</td><td id="28-3g">4X CLKIN</td><td id="28-3h">2X CLKIN</td><td id="28-3i">4X CLKIN</td><td id="28-3j">2X CLKIN</td><td id="28-3k">4X CLKIN</td><td id="28-3l">2X CLKIN</td><td id="28-3m">CLKIN</td></tr>
</table>

<a id='48b75d24-0d14-462a-a93e-cc3b69bc7ba8'></a>

NOTES
1 100 MHz rate max.
2 Single DAC data rate = 1/2 dual DAC data rate.

<a id='63e0cd6f-04a0-4b50-941c-4729b7c3538c'></a>

REV. 0

<a id='bc7765bc-826f-4e31-a058-eb71f4c4b4a0'></a>

-29-

<!-- PAGE BREAK -->

<a id='e6792c3f-d1ce-40c5-a7e7-3a7ed7ea71b3'></a>

## AD9860/AD9862

The timing block diagrams in Figures 14 and 15 show how the various clocks of the single and dual Tx path are affected by the various register settings.

<a id='deca2e16-8177-421c-a9c7-e0e12bb9ca49'></a>

For dual Tx data, an option to redirect demultiplexed data to either path is available. For example, the AD9860/AD9862 can accept complex data in the form of I then Q data or Q then I data, controlled through QI Order register.

<a id='7e319c02-6c3a-4c2e-a748-6d582f2dac1b'></a>

For the dual Tx data cases, the Tx_SYNC pin input logic level defines what data is currently on the Tx data bus. By default, when Tx_SYNC is low, Channel A data (first of the set) should be on the data bus. If TxSYNC is high, Channel B data (or the second of the set) should be on the Tx bus. This can be reversed by setting the Inv TxSYNC register.

<a id='fd902323-45a0-4e4c-990b-5d453a912866'></a>

## ADDITIONAL FEATURES
In addition to the features mentioned above in the transmit, receive and clock paths, the AD9860/AD9862 also integrates components typically required in communication systems. These components include auxiliary analog-to-digital converters (AUX ADC), auxiliary digital-to-analog converters (AUX DAC), and a sigma-delta output.

<a id='4fd0598f-f487-45d9-a139-e363ade0c038'></a>

**Auxiliary ADC**
Two auxiliary 10-bit SAR ADCs are available for various external signals throughout the system, such as a Receive Signal Strength Indicator (RSSI) function or Temperature Indicator. The auxiliary ADCs can convert at rates up to 1.25 MSPS and have a bandwidth of around 200 kHz. The two auxiliary ADCs (AUX ADC A and AUX ADC B) have multiplexed inputs, so that up to four system signals can be monitored.

<a id='864736c9-f351-443a-985e-48f0bd588204'></a>

The AUX ADC A multiplexer controls whether pin AUX_ADC_A1 or pin AUX_ADC_A2 is connected to the input of Auxiliary ADC A. The multiplexer is programmed through Register D34 B1, SelectA. By default, the register is low, which connects the AUX_ADC_A2 Pin to the input. Similarly, AUX ADC B has a multiplexed input controlled by Register D34 B4, SelectB. The default setting for SelectB is low, which connects the AUX_ADC_B2 input pin to AUX ADC B. If the SelectA or SelectB register bit is set high, then the AUX_ADC_A1 Pin or the AUX_ADC_B1 pin is connected to the respective AUX ADC input.

<a id='a03ba7cb-7ade-4bcc-8ded-a43d468d8e3f'></a>

An internal reference buffer provides a full-scale reference for both of the auxiliary ADCs that is equal to the supply voltage for the auxiliary ADCs. An external full-scale reference can be applied to either or both of the AUX ADCs by setting the appropriate bit(s), RefselB for the AUX ADC B and Refsel A for the AUX ADC B in the Register Map. Setting either or both of these bits high will disconnect the internal reference buffer and enable the externally applied reference from the AUX_REF Pin to the respective channel(s).

<a id='e1f105dd-b3a0-4ece-aed6-7f63dc3e1f6a'></a>

Timing for the auxiliary ADCs is generated from a divided down
Rx ADC clock. The divide down ratio is controlled by register
D35 B0, CLK/4 and is used to maintain a maximum clock rate of
20 MHz. By default, CLK/4 is set low dividing the Rx ADC clock
by 2; this is acceptable when running the Rx ADC at rate of
40 MHz or less. At Rx ADC rate greater than 40 MHz, the CLK/4
register bit should be set high and will divide the Rx ADC clock
by 4 to derive the auxiliary ADC Clock. The conversion time,
including setup, takes 16 clock cycles (16 Rx ADC clock cycles);
when CLK/4 is set low, divide by 2 mode, or 32 clock cycles
when CLK/4 is set high.

<a id='52ed9a50-2aee-4026-a99e-ebb69a1e9142'></a>

<::block diagram: Figure 14. Single Tx Timing Block Diagram, Alternative Operation::>
CLKIN input signal branches into two paths:
1. An output labeled "ADC SAMPLE RATE (NOT TO EXCEED 64MHz)"
2. An input to a block labeled "DLL MULT". The DLL MULT block has an input labeled A and an output labeled B. Its internal logic is defined as:
   - 00: B = A
   - 01: B = 2 × A
   - 10: B = 4 × A
The output B from the "DLL MULT" block branches into two paths:
1. An output labeled "DLL OUTPUT RATE (NOT TO EXCEED 128MHz)"
2. An input to a block labeled "CLKOUT2 DIV". The CLKOUT2 DIV block has an input labeled B and an output labeled C. Its internal logic is defined as:
   - 00: C = B
   - 01: C = B/2
   - 10: C = B/4
The output C from the "CLKOUT2 DIV" block branches into two paths:
1. An output labeled "CLKOUT2"
2. An input to a block labeled "INTERP". The INTERP block has an input labeled C and an output labeled D. Its internal logic is defined as:
   - 00: D = C
   - 01: D = 2 × C
   - 10: D = 4 × C
The output D from the "INTERP" block branches into two paths:
1. An output labeled "INPUT Tx DATA RATE (SINGLE CHANNEL)"
2. An output labeled "TxDAC UPDATE RATE SINGLE CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)"

<a id='692f08c5-f9fa-49ef-b49c-3fb753e24d64'></a>

<::block_diagram
CLKIN
|
v
[DLL MULT]
Input: A (from CLKIN)
00: B = A
01: B = 2 × A
10: B = 4 × A
Output: B
|
v
ADC SAMPLE RATE (NOT TO EXCEED 64MHz)
|
v
[CLKOUT2 DIV]
Input: B (from DLL MULT)
00: C = B
01: C = B/2
10: C = B/4
Output: C
|
v
DLL OUTPUT RATE (NOT TO EXCEED 128MHz)
|
v
[2 EDGES]
Input: C (from CLKOUT2 DIV)
0: D = C
1: D = 2 × C
Output: D
|
v
CLKOUT2
|
v
[DUAL CHANNEL FACTOR]
Input: D (from 2 EDGES)
E = D/2
Output: E
|
v
INPUT Tx DATA RATE
|
v
[INTERP]
Input: E (from DUAL CHANNEL FACTOR)
00: F = G
01: F = 2 × G
10: F = 4 × G
Output: F
|
v
INPUT TX DATA RATE EACH CHANNEL
|
v
TxDAC UPDATE RATE EACH CHANNEL (CANNOT EXCEED DLL OUTPUT RATE)
::>
Figure 15. Dual Tx Timing Block Diagram, Alternative Operation

<a id='6da0e656-c045-4686-959d-ed911d793461'></a>

-30-

<a id='b3b698df-8522-4f60-aca4-969ac2161baa'></a>

REV. 0

<!-- PAGE BREAK -->

<a id='af2e06d6-a592-4db5-b861-b49151ecda0c'></a>

AD9860/AD9862

<a id='2bc948e7-c379-4815-9ee6-995ca3b2bbde'></a>

Conversion is initiated by writing a logic high to one or both of the Start register bits, Register D34 B0 (StartA) and D34 B3 (StartB). When the conversion is complete, the straight binary, 10-bit output data of the AUX ADC is written to one of four reserved locations in the register map depending on which auxiliary ADC and which multiplexed input is selected. Because the auxiliary ADCs output 10 bits, two register addresses are needed for each data location.

<a id='021b79e2-2635-4c33-b388-83548a511a08'></a>

Initiating a conversion or retrieving data can also be accomplished either through the standard Serial Port Interface by reading and writing to the appropriate registers or through a dedicated Auxiliary Serial Port Interface (AUX SPI). The AUX SPI can be configured to allow fast access and control of either one of the auxiliary ADCs and is available so that the SPI is not tied up retrieving auxiliary ADC data.

<a id='e1ccd738-0784-4cda-8915-d52f470e4d02'></a>

The AUX SPI can be enabled and configured by setting register AUX ADC CTRL. Setting register use pins high enables the AUX SPI port. Setting register Sel BnotA low connects auxiliary ADC A to the AUX SPI port, while setting it high connects auxiliary ADC B to the AUX SPI port. As mentioned above, setting the appropriate Select bit selects which of the multiplexed input is connected to the auxiliary ADC.

<a id='77443934-40a5-4c3c-8e5d-97eb1028c2d7'></a>

The AUX SPI consists of a chip select pin (AUX_SPI_csb),
a clock pin (AUX_SPI_clk), and a data output pin (AUX_SPI_do).
A conversion is initiated by pulsing the AUX_SPI_csb pin low.
When the conversion is complete, the data pin, AUX_SPI_do,
previously a logic low, will go high. At this point, the user supplies
an external clock, previously tied low, no data is present on the
first rising edge. The data output bit is updated on the falling
edge of the clock pulse and is settled and can be latched on the
next clock rising edge. The data arrives serially, MSB first. The
AUX SPI runs up to a rate of 16 MHz.

<a id='11e92c20-cbed-4d7c-980c-c0d842fabff0'></a>

## AUX DAC
The AD9860/AD9862 has three 8-bit voltage output auxiliary DACs, AUX DACs. The AUX DACs are available for supplying various control voltages throughout the system such as a VCXO voltage control or external VGA gain control and can typically sink or source up to 1 mA.

<a id='da1f0691-d5a3-47b3-88ec-d6a08d1d1b26'></a>

An internal voltage reference buffer provides a full-scale voltage reference for both of the AUX DACs equal to the supply voltage for the AUX DACs. The straight binary input codes are written to the appropriate registers. If the Slave Mode register bit is high, slave mode enabled, the AUX DAC(s) update will occur when the appropriate update register is written to. Otherwise, the update will occur at the conclusion of the data being written to the register. Typical maximum settling time for the auxiliary DAC is around 6 s.

<a id='f583e2c9-7e39-456e-9709-51a0702c7907'></a>

Other optional controls include an invert register control and a
power down option. The invert register control, i.e., instead of
hexFF being high and hex00 being low, hex00 is high, and hexFF
will be minimum setting.

<a id='1acf71b8-468c-480d-82fa-25e7f260c6ff'></a>

## Sigma-Delta
A 12-bit sigma-delta (SD) output is available to provide an additional control voltage. The SD control word is written to Registers D42, 43; SD [11:4] are the 8 MSBs and SD [3:0] are the 4 LSBs. The 12-bit word is processed by a sigma-delta modulator and produces 1-bit data at an oversampled rate equal to 1/8 of the receive ADC's sampling rate (up to 8 MSPS). The 1-bit data then feeds a 1-bit DAC. The 1-bit DAC exhibits perfect linearity. An external low-pass filter at the output should be used to low-pass filter the pulse modulated data to produce a linear output control voltage.

<a id='5ccca1ba-6e70-4d59-aed9-5a3cc0ba3444'></a>

REV. 0

<a id='e51776f7-cfa7-4bc9-a132-82a44f2ed9df'></a>

-31-

<!-- PAGE BREAK -->

<a id='5dc6b908-b8a6-4698-aef2-8064610546e3'></a>

AD9860/AD9862

<a id='c12bf576-6d15-415c-9bc1-2b8e2e6fc8d1'></a>

OUTLINE DIMENSIONS
128-Lead Plastic Quad Flatpack [LQFP]
(ST-128B)
Dimensions shown in millimeters
<::drawing: The drawing illustrates the outline dimensions of a 128-Lead Plastic Quad Flatpack (LQFP), designated as ST-128B, with dimensions in millimeters. It includes three main views: a side profile, a top-down view, and a detailed cross-section of a pin.

**Side Profile View:**
- Shows the package height dimensions: 0.75, 0.60, 0.45 (from top to seating plane), and a maximum overall height of 1.60.
- A "SEATING PLANE" is indicated.
- A circular callout points to "VIEW A", indicating a magnified detail.

**Top View (PINS DOWN):**
- Displays the rectangular package outline with pin numbering around its perimeter.
- Pin numbers are marked at corners: 1, 38, 39, 64, 65, 102, 103, 128.
- Overall width: 16.00 BSC.
- Body width: 14.00 BSC.
- Overall length: 22.00 BSC.
- Body length: 20.00 BSC.
- Pin pitch (distance between pin centers): 0.50 BSC.
- Pin width dimensions: 0.27, 0.22, 0.17.

**VIEW A (ROTATED 90° CCW):**
- This is a detailed cross-sectional view of a pin and its connection to the package body.
- Pin bend height dimensions: 1.45, 1.40, 1.35.
- Angles of the pin bend are specified: 10°, 6°, 2° (for the bend) and 7°, 0° (for the foot).
- Pin foot length dimensions: 0.20, 0.09.
- "SEATING PLANE" is indicated.
- "0.08 MAX COPLANARITY" is noted.

All dimensions are in millimeters, and "BSC" stands for Basic Spacing Concept.::>
COMPLIANT TO JEDEC STANDARDS MS-026BHB

<a id='fe604c30-3403-4343-9902-983343d45b39'></a>

-32-

<a id='530f89ab-d75e-4905-b0af-5f5a34112184'></a>

REV. 0

<a id='01f1d743-02b9-4276-a60f-9be73a3f048d'></a>

C02970-0-11/02(0)

<a id='fa2aef47-3c96-4e16-bfaf-9f8ada060042'></a>

PRINTED IN U.S.A.