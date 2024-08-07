# CdS Photocell light measurement

The round component with two radial leads is a CdS
[photocell](https://resources.perkinelmer.com/corporate/cmsresources/images/44-6551app_photocellapplicationnotes.pdf).
This particular photocell is an
[Advanced Photonix PDV-P8103](https://www.advancedphotonix.com/wp-content/uploads/2015/07/DS-PDV-P8103.pdf).
A key specification of a photocell is the resistance in darkness vs. bright light.
For the PDV-P8103, the dark resistance is specified as minimum 500k ohm and the illuminated resistance is specified between 16k ohm and 33k ohm.

There is also a
[10k ohm 1/8 watt resistor](https://www.seielect.com/catalog/sei-cf_cfm.pdf)
with axial leads provided.

A typical means of measuring light with a photocell using a microcontroller is to use the photocell as one resistor in a voltage divider circuit.
The voltage divider circuit center point is connected to an analog-to-digital converter (ADC) input of the microcontroller.
The ADC measures the voltage at the junction of the two resistors.
By calibrating the photocell measurement vs. a known intensity of light, the photocell voltage divider input the ADC can converted to a light level.

A voltage source is needed for the voltage divider circuit, which on the Pi Pico can be taken from the "3V3 OUT" pin.
