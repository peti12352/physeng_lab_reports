preliminary: workstation 1; sample d9 (NV) 

2
We connect the DETECTOR OUT to the back input of the lockin amplifier, which doesn't do any lock-in, it just does VOLMETER. We use it to calibrate.

We move the position of the sample to find the maximum photoluminescence signal. We do not move the mirror.

The background signal (before turning on the laser) is 0.22V

Max Achieved: 1.5 V


3

INFO - TR-ODMR.SR830M - Serial connection detected
WARNING - TR-ODMR.KuhnePLL - Sending command failed, retrying (attempt 1/3).
Setting LO to 2.87 GHz...
Uploading CW sequence to PicoPulse...


the lockin amplifier gives us the difference between the MW excited case and the non excited case:
we got higher difference, we are looking at the R of the lockin

lockin 
Mean Signal R: 0.0181 V
Standard Deviation: 0.0000 V
Mean Phase: -30.82 deg

this was before re-calibrating it.

now we re calibrate position of sample to maximize lockin signal

noise is about 0.1 mV

first run: R=18.5mV was max 

second run: R=18.3mV was max