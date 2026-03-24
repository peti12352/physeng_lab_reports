
first occasion

first we started by extensively talking about the measurement setup and the tricks of measuring fast pulses.

1. 
20w --- 5.2w (pump) (each photon is twice as energetic, half wavelength as previous. uses SHG) --- 0.34w pulse generator (red)
P = 0.340 W



2
pulse operation: more modes than in continuous waves, so broader spectrum in pulse
we dont want fluoresemce  (spontaneous, random phase and freq) (no laser), so this is supressed, resonance (sync phase and fix freq) (stimulated induced emission)

if risetime for a detector or measurement device is higher than pulse duration, you get triangle wave. dirac --- triangle



tsunami pulse generator length
c*12.14ns/2

  (SpeedOfLight × (12.14 nanoseconds)) / 2 ≈ 1.819740220 m

this agrees with the device specifications

time between pulses (round trip along device): 12.14ns

in a measurement chain, alsways the slowest device (less resolution) determines the error
the width of the pulse in oscilloscope is arounf 2ns, because the oscilloscope is 500GHz



3
we measure with spectrometer the output of the pulse. we have the intensity as a function of frequency. file: "first"
we measure the bandwith 
bandwidth: 784.15
about 6950 is the half for the counts 13929 is the total amplitude (irrelevant tho)
bandwidth * pulse_time = constant 


lambda_1 = 778 nm -> f_1 = 385.3373496 THz
lambda_2 = 792.5 nm -> f_2 = 378.2870132 THz

delta_lambda = 14.5 nm (bandwith) -> delta_f = 7.0503364 THz

assuming gaussian pulse -> const = 0.441 
-> pulse_time = 0.441/delta_f = 62.55020682 fs (good approx, assuming no dispersion)

zhis is the best we can do in pulse duration

sqrt(power) gives the spectral amplitude (i think amplitude of E field). we assume the phase to be fixed.
then this is the fourier transform of the time domain E (i think)

amplifiers reduce the spectrum bandwidth (makes pulse longer). to compensate, a nonlinear crystal is used (compressor) that widens the spectrum, and narrows the time duration of the pulse.


autocorr1:

semi conductor forces the laser to operate in pulse mode

amp lets the pulse pass but not the noise. it doesnt provide amplification, it only absorbs noise. if it is a high bandwith amp, then it doesnt mess up your signal. SESAM


differential equ: 
- saturable absorber mirror -> gaussian
- 

for the sech solution, the differential equation has a complex solution which is this sech

we measured and saved gaussian and sechfit for the pulse. gives the time duration

data/first_occassion/autocorr1_61fs_leftpulse_sech2
data/first_occassion/autocorr1_68fs_leftpulse_gauss
data/first_occassion/autocorr1_119fs_rightpulse_sech2
data/first_occassion/autocorr1_138fs_rightpulse_gauss

we did this procedure by taking the laser pulse, using a 1cm thick glass relfector. we get 2 reflections, one of them doesnt go through the glass, and the other traverses it twice (at an angle ofc), this it has some dispersion, and then the pulse becomes wider. we repeate the measurement and fit, and we can immediatly see that the measurement for the second reflection is wider

for the first reflection we call it LEFT, for second, we call it RIGHT

then we measure these two but using spectrometer so we check that they have the same spectral

we do see differences between the left and right measurements, here it would be great to compare the two side by side.
Also show this both using the "gauss" fit and the "sech2" fit.




compressor

sf10 high dispersion glass prism, that induces a diffferent phase difference (linearly) for dofferent frequencies omega. high refractive index. used for compressor. compresses the pulse time, and it will not alter the bandwith of the intensity spectrum, but the phase of the light changes.

phase is k * d
űk = 2pi over lambda


compressor ccompensates the effect of the materials 


now we add a 20mm = 2cm glass cube and measure, to see the change. we saved both fits.




Telur dioxide (teo2)
best crystal for deflectors. acustooptics. high dispersion.

decreases the pulse time by around 4 times. 

first we used a 3cm thick sample,

then we kept the 3cm sample, and added a 1cm sample in series. commutativ. this decreases the time pulse by a factor of like 5, even though we added a small addition. 

the signal becomes too short (the pulse time is too short)  so we cant even measure it. we need to change scanning range of the measurement device, for better time resolution. all good. the time pulse now like 65 fs, which shows how it is used to perfectly compensate the dispersion of 4cm of teo2




we then added the glass again, but we then shifted the compressor prism so that the laser goes through a thicker part of it (the prism is like a triangle so by moving it we can achieve it), doing this, we could compensate for the dispersing effect of the glass, and we recover the same pulse shape. ish.
this proves the operation of the compressor prism to compensate for the dispersion of other optical elements (materials)
shifted-prism


data/spektrum_grego_peti.txt is the spectrum after crystal and glass cube ( 30 mm TeO2 crystal and 20 mm BK7 glass) + compressor



second occasion:

power of laser (same as last time) P=0.355W

same pulse as meas last time

angular dispersion caused by small prism

higher wavlength slower

trying to get symmetric

calculate angular dispersion

we have prism wit 60-60-60 degree angles

(we took photo of formula - paper)

calculste n

use refractive formula to calculate the angle of the reflected beam, then compsre with screenshot
rad/nm is the dispersion

compare with:

lambda -> refractive index -> reflection rule -> how lambda is spread

angular dispersion causes diff spectral components to propagate in varying directions -> pulse-front tilt





In the next task what we did is created an interference pattern with a michelson interferometer. then we displaced the mounted mirror with a micrometer translator and measured the points where we stop getting interference. We repeated this a couple times, the latter times being more accurate


x_init=17608 micrometer 

x1=18480 micrometer (no interference)
x2=17540 micrometer (no interference)

delta x = x1-x2 = 18480-17540 = 940 micrometer

(high because of spectrally decomposition  )
(this was probably wrong)

same a prev but repeat

x1 = 17660 micrometer (no interference)
x2 = 11590 micrometer (no interference)


same repetition:

here we repeated the measurement more carefully and robustly. we measured twice and obtained that
240 micrometers range
this is the best measurement value

1.5nm resolution (what does this mean here? help)



Bandwidth of the laser (you see it from the spectral information) = 20 or 25 nm

The pulse length
70 fento seconds * c_light = 20 micrometer 

The limits in the interference Vs not interference was 240 micro meter

25nm* 20micrometer /240 micrometer = 2.083 nm

but what does this mean? I know that there is one calculation involving these values: pulse length = 70 fs, range of interference = 240 micrometer, and bandwidth of laser = 20 or 25 nm

