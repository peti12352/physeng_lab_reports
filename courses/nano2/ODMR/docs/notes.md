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


So, in the photoluminescence case task 2, what you were trying to find is the location that has the highest density of nitrogen vacancy sites, because those are the photoluminescence emitting sites. And then, in the microwave case, because you are measuring the lock-in signal, which measures the difference in photoluminescence between the microwave excitation time and the non-microwave excitation time, then what you are trying to find is the space that has both the highest concentration of nitrogen vacancies, but also the highest intensity of the microwave field. And here we need to remember that both in this sample is inhomogeneous in space in the density and concentration of nitrogen vacancies, and the microwave is inhomogeneous in intensity because of the design.

4

time const is used from the lockin to calcuate the sampling rate

for task 2 and 3 we used 10ms, for task for onwards we use 30ms


we see two resonance peaks.

the center between the two peaks is D
the distance between the center and each peak is 2*E
the distance between peaks is 2E

5

we expect to get 8 resonances. there are 4 possible directions for the magentic field, and each has 2 resonance peaks.


2 groups of 4;














D
D (zero-field splitting)
Meaning: intrinsic splitting between 
m
s
=
0
m 
s
​
 =0 and 
m
s
=
±
1
m 
s
​
 =±1 even when 
B
=
0
B=0.
Origin: spin-spin interaction in the NV triplet ground state.
Relevance: sets the central ODMR frequency scale; it is the baseline resonance and a key calibration parameter.
E
E (transverse splitting / strain parameter)
Meaning: lifts degeneracy between the two 
m
s
=
±
1
m 
s
​
 =±1 branches at zero magnetic field.
Origin: local symmetry breaking (strain/electric-field effects).
Relevance: determines the doublet separation around 
D
D, reflects crystal/environment quality, and affects line positions and fitting.









The formula you are using is a modified version of the standard Rabi decay model. [cite_start]Your lab manual recommends this specific stretched exponential formula to account for the physical realities of your experimental setup, such as imperfect driving fields and thermal effects[cite: 576, 577].

Here is the physical breakdown of each fitting parameter in your equation:

* [cite_start]**(Effective Transverse Relaxation Time):** Noted as $T_2^*$ in your lab manual's formula[cite: 578], this represents the dephasing time of the ensemble. [cite_start]It describes the timescale over which the NV spins lose their phase coherence in the transverse ($x-y$) plane[cite: 289, 290]. [cite_start]As the spins interact with their local environment (like the fluctuating magnetic fields from $^{13}$C nuclear spins) and experience slightly different local microwave field strengths, their rotations fall out of sync, causing the macroscopic Rabi oscillations to dampen and wash out[cite: 288, 290].
* [cite_start]**$\beta$ (Stretching Exponent):** This is an empirical parameter used to account for inhomogeneity[cite: 577]. In a perfect, single-qubit measurement, the decay envelope is typically a simple exponential ($\beta = 1$). [cite_start]In an ensemble measurement, the spatial inhomogeneity of the driving microwave field causes different NV centers to rotate at slightly different rates[cite: 288]. [cite_start]The stretching parameter corrects the envelope for these compounded, incoherent rotations[cite: 288, 577].
* [cite_start]**$\omega_{\text{Rabi}}$ (Rabi Frequency):** This represents the angular frequency at which the spin state is coherently driven back and forth between the $|0\rangle$ and $|1\rangle$ states[cite: 244, 245]. [cite_start]It scales linearly with the amplitude of the driving microwave magnetic field ($B_1$)[cite: 246]. 
* **$A$ (Amplitude):** This defines the signal contrast (the depth of the oscillation). Physically, it is determined by the population difference created by the optical initialization pulse and the collection efficiency of your photodetector setup.
* **$\phi$ (Phase Offset):** This parameter accounts for any initial phase shift in the oscillation. It corrects for the system not starting at exactly zero rotation at $\tau = 0$, which can be caused by finite rise times of the microwave pulses or minor signal propagation delays in the electronics.
* [cite_start]**$B$ (Linear Slope):** This linear term is explicitly added to account for microwave heating[cite: 576]. [cite_start]As the microwave pulse duration ($\tau$) gets longer, the high-power microwave radiation (up to 10 W in your setup) physically heats the waveguide and diamond sample[cite: 324, 326, 548]. This temperature shift slightly alters the background fluorescence, introducing a linear drift in the baseline signal.
* [cite_start]**$C$ (Background Offset):** This is the baseline photoluminescence signal (the unmodulated DC component of the fluorescence)[cite: 578].


attenuation = [0, 6, 10] # dB
f_Rabi = [2.48, 2.17, 1.46]


