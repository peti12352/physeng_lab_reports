Physicist-Engineer Nanotechnology and Quantum Applications
Specialization Laboratory Measurement 2:
Ultrashort pulse processing
Abstract. Ultrashort laser pulses are important tools in many technologies involving
lasers: material processing, telecommunication, laser microscopy, surgery and medical
applications, etc. These pulses have high peak energy and duration at least ten times
shorter than the minimum integration time of the fastest laser detectors. This imposes
the need for special techniques for pulse length measurement such as autocorrelators
or spectrally resolved interferometry. The frequency bandwidth of these pulses implies
special techniques to maintain the temporal length during propagation through the
optical system leading from the source to the target. The present laboratory exercise
makes spectral and temporal measurement and dispersion compensation techniques
familiar to the practicing students and gives the practical basis for ultrashort laser
pulse processing in possible future applications.
I
Introduction
1 Need for advanced use of ultrashort laser pulses
The generation and manipulation of ultrashort laser pulses play a central role in modern
optics, spectroscopy, and nonlinear optical applications. When femtosecond laser pulses
propagate through optical components, their temporal characteristics are strongly influenced by the wavelength-dependent refractive index of the materials involved. This effect,
known as material dispersion, leads to temporal pulse broadening and phase distortions,
which must be carefully controlled in high-precision experiments.
In many practical optical systems, dispersive elements such as laser crystals, lenses,
optical windows, and modulators introduce positive dispersion, resulting in an increased
pulse duration without a significant reduction in spectral bandwidth. To recover the shortest possible pulse duration at the point of application, dispersion compensation techniques
are required.
The aim of this laboratory experiment is to study the physical origin of material dispersion and to demonstrate its compensation using a prism-based pulse compressor. By
1
adjusting the geometry of a two-prism compressor, negative dispersion can be introduced
to counterbalance the positive dispersion accumulated in optical components. The effectiveness of the compensation is evaluated by measuring the temporal pulse width using an
autocorrelator and comparing the experimental results with theoretical expectations.
2 Laser Safety Considerations
Strict adherence to laser safety regulations is essential during the experiment. The lasers
used typically operate in the wavelength range of 760–800 nm, where the human eye sensitivity is very low. This can create the false impression that the emitted optical power is
small. In reality, the measured laser powers are significantly higher than those of commonly
used He–Ne laboratory lasers.
Furthermore, the lasers operate in an ultrashort pulse regime, which means that exFigure I.1.1. Ultrashort pulsed laser. The laser uses an amplifier crystal, T.sapphire, which
has an extra high bandwidth of more than 400 nm optical wavelength, between 650 nm and 1100
nm, in the red and near infrared regime of the spectrum. It is pumped by a 5.2 W frequency
doubled Nd:YLF laser, at 532 nm wavelength. The pulses generated in the laser are transfrom
limited, when quit the laser due to the built in prism compressor
2
Theoretical Background 3
tremely high peak intensities are present even at moderate average power levels.
II Theoretical Background
3 Generation and measurement of ultrashort pulses
3.1 Ultrashort Laser Pulses
The investigation of rapidly evolving physical processes is a fundamental objective in many
areas of natural science. Modern laser systems are capable of generating pulses with durations of only a few optical cycles. In some cases, even shorter pulses can be produced
using advanced techniques.
A fundamental challenge in measuring such ultrashort laser pulses is that the physical process used for the measurement must be faster than the pulse itself. Conventional
detector-based techniques therefore cannot directly measure ultrashort pulses. When a fast
photodetector and oscilloscope are used, the measured signal width is determined by the
response time of the detection system rather than by the actual pulse duration. Typically,
such measurements yield apparent pulse widths on the order of nanoseconds, even though
the true pulse duration may be in the picosecond or femtosecond range.
3.2 Mode Locking
Ultrashort pulses are generated using a technique known as mode locking. Mode locking requires a laser resonator and gain medium capable of supporting a large number of
longitudinal modes simultaneously.
During mode locking, the phases of the longitudinal modes are synchronized, meaning
that the phase differences between the different frequency components are fixed. Mathematically, it can be shown that the superposition of many sinusoidal waves with fixed phase
relationships results in the formation of short pulses.
A large number of longitudinal modes also implies that the laser emits radiation over
a broad spectral bandwidth. From this spectral width, an estimate can be made of the
shortest possible pulse duration assuming perfect phase synchronization. This theoretical
minimum pulse duration is known as the transform-limited pulse duration.
3.3 Transform-Limited Pulses and Time–Bandwidth Product
The transform-limited pulse duration depends on assumptions regarding the spectral and
temporal shape of the pulse, which are generally not known exactly in practice.
For different pulse shapes, a theoretical relationship exists between the spectral bandwidth and the minimum achievable pulse duration. This relationship is expressed by the
time–bandwidth product:
∆t · ∆f = constant (II.3.1)
Typical values for different pulse shapes are:
• Gaussian pulse: ∆t∆f = 0.441
• Sech2 pulse: ∆t∆f = 0.315
• Lorentzian pulse: ∆t∆f = 0.142
Theoretical Background Autocorrelation Function 4
Since these pulse shapes are often very similar, their autocorrelation traces are also
nearly indistinguishable. Therefore, autocorrelation measurements alone cannot uniquely
determine the exact pulse shape.
3.4 Autocorrelation Function
The autocorrelation function is defined as:
ACF(τ ) = Z ∞
−∞
x(t) x(t + τ ) dt (II.3.2)
In optical autocorrelation measurements, the function x(t) may represent either the
electric field or the intensity of the pulse. When field autocorrelation is calculated, the
Fourier transform of the optical spectrum is obtained, forming the basis of Fourier-transform
spectroscopy.
4 Ultrashort pulse propagation through optical elements
4.1 Material Dispersion
In optical materials, the refractive index depends on the wavelength of the propagating
light. For most transparent materials used in optics, this dependence is such that the
refractive index decreases with increasing wavelength, a behavior referred to as normal
(positive) material dispersion. As a consequence, different spectral components of a short
laser pulse propagate with different phase velocities.
For ultrashort pulses, which inherently possess a broad spectral bandwidth, this wavelengthdependent phase accumulation leads to temporal broadening and distortion of the pulse.
The effect becomes increasingly significant as the pulse duration decreases and the optical
path length through dispersive media increases.
Figure II.3.1. Autocorrelator. In this method, the pulse is correlated with a delayed
replica of itself, and the pulse duration is estimated from the resulting autocorrelation trace. An
optical autocorrelator typically operates by splitting the incoming laser pulse into two beams
using a beam splitter. A variable optical path difference is introduced between the two beams,
creating a controllable temporal delay. After recombination, the beams are focused into a nonlinear
crystal, where second-harmonic generation (SHG) occurs. The intensity of the generated secondharmonic signal is detected as a function of delay. This technique enables the measurement of
both picosecond and femtosecond pulses, even at high repetition rates.
Theoretical Background Frequency-Dependent Phase Accumulation 5
4.2 Frequency-Dependent Phase Accumulation
The propagation of a laser pulse through an optical system introduces a frequency-dependent
phase shift to its spectral components. This phase can be expressed as a Taylor expansion
around the central angular frequency ω0 of the pulse spectrum:
ϕ(ω) = ϕ0 +
dϕ
dω




ω0
(ω − ω0) + 1
2
d
2ϕ
dω2




ω0
(ω − ω0)
2 + · · · (II.4.1)
The zeroth-order term represents a constant phase shift, while the first-order term
corresponds to a temporal delay and does not alter the pulse shape. The second-order
term, known as group delay dispersion (GDD), leads to temporal pulse broadening and
the formation of a frequency chirp. Higher-order terms, such as third-order dispersion
(TOD), become relevant for extremely short pulses and cause more complex distortions of
the temporal pulse profile.
4.3 Dispersion Compensation
In ultrafast laser systems, dispersion effects must be compensated in order to maintain
short pulse durations. Dispersion compensation is achieved by introducing optical elements
that impose a frequency-dependent phase shift of opposite sign to that accumulated in the
system.
One of the most widely used dispersion compensation schemes is the prism-pair compressor. In such a configuration, the different spectral components of the pulse are spatially
separated by the first prism and experience different optical path lengths between the two
prisms. Upon recombination at the second prism, a controllable negative dispersion is
introduced.
By properly adjusting the distance between the prisms and the position of the retroreflecting mirror, the negative dispersion of the compressor can be tuned to compensate the
positive dispersion introduced by optical materials. When the compensation is optimal, the
pulse duration reaches its minimum value, approaching the transform-limited pulse width.
Figure II.4.1. Prism compressor setup used in the measurement. Scheme of the prism
compressor
Theoretical Background Dispersion Compensation 6
In general, a single dispersion-compensating element can compensate only one specific
dispersion term, corresponding to a given order in the Taylor expansion of the frequencydependent phase. Therefore, the overall optical system must be designed by taking all
dispersive contributions into account. For femtosecond laser pulses, compensation of the
second-order derivative, known as group delay dispersion (GDD), is typically required,
while for pulses shorter than approximately 30 fs, the effects of third-order dispersion
(TOD) must also be considered.
The most commonly used dispersion-compensating elements are prism pairs. In a prism
compressor, material dispersion spatially separates the spectral components of the pulse.
Due to the wavelength-dependent optical path length between the prisms, the relative
phase of the individual spectral components can be shifted in either a positive or negative
frequency direction. In this way, the phase distortions accumulated in the gain medium
and on the resonator mirrors can be effectively compensated.
In laser resonators, specially designed multilayer mirrors are also widely employed
for dispersion control. In these mirrors, different spectral components of the pulse are
reflected from different penetration depths depending on their frequency, resulting in a
frequency-dependent phase shift. The mirrors used in resonators must be designed such
that the phase shift they introduce precisely compensates the frequency-selective phase
accumulation occurring in the gain medium.
With proper optical design, the application of anti-reflection coatings, and operation at
the Brewster angle, both prisms and mirrors can exhibit low optical losses. As a result, they
can be integrated into laser resonators without significantly reducing the extractable pulse
energy. In contrast, diffraction gratings may also be used for dispersion compensation, but
typically only outside the resonator or in high-gain fiber laser systems, since their optical
losses are considerably higher.
Nonlinear optical effects play a crucial role in shaping the temporal and spatial characteristics of ultrashort laser pulses. These effects arise from the intensity dependence of
the refractive index in various materials within the resonator and the propagation medium,
leading to intensity-dependent phase shifts experienced by different parts of the pulse. The
most common nonlinear effect is the Kerr effect, in which the refractive index n depends
linearly on the optical intensity I:
n = n0 + n2I. (II.4.2)
As a consequence of nonlinear effects, laser pulses become distorted both transversely in
space and temporally. The high-intensity regions of the pulse, corresponding to its spatial
and temporal peak, experience a larger phase delay than the pulse wings. The resulting
temporal distortion is known as self-phase modulation (SPM).
The spatial effect of the Kerr nonlinearity forms the basis of one of the most successful
passive mode-locking techniques, Kerr-lens mode locking (KLM). Furthermore, the combined temporal effects of dispersion and nonlinearity can lead to soliton formation, in which
the two effects mutually compensate each other. This mechanism is generally more complex, as both second-order and higher-order dispersion terms can interact with nonlinear
effects.
A fundamental soliton is formed when the second-order dispersion (GDD) and the Kerr
effect have opposite signs and comparable magnitudes over one round trip in the resonator.
In this case, the pulse remains stable both spatially and temporally, preserving its shape
and duration during propagation, while accumulating only a nonlinear phase shift. In the
presence of higher-order dispersion, higher-order solitons may form, for which the pulse
Theoretical Background Dispersion Compensation of External Optical Elements 7
shape and duration vary periodically along the propagation direction.
The generation of pulses shorter than approximately 100 fs is only possible through
soliton formation, as optical switching elements with sufficiently fast response times do not
exist, even in passive implementations.
Solitons formed outside the laser resonator are particularly important for long-distance
optical communication, primarily in optical fibers. Although soliton formation in free space
is highly unlikely, it has been observed in exceptional cases. Optical fibers provide favorable
conditions for self-phase modulation, and their intrinsic dispersion can be tailored through
material composition and doping.
4.4 Dispersion Compensation of External Optical Elements
External optical components, such as acousto-optic crystals or lenses, introduce additional
dispersion that stretches the pulse duration without significantly reducing its spectral bandwidth. This dispersion must be compensated in such a way that, at the point of application,
the original transform-limited pulse corresponding to the available bandwidth is restored.
The simplest and experimentally adequate method for this purpose is the use of a twoprism compressor. In this configuration, the laser beam passes through the prism pair
twice, and due to the dispersion introduced by the prisms, it experiences a negative group
delay dispersion that counteracts the positive dispersion accumulated in the crystals and
other optical elements. The compressor is correctly adjusted when the distance between
the prisms and the retroreflecting mirror is such that the introduced negative dispersion
compensates the total positive dispersion of the system.
Figure II.4.2. Two pass prism compressor. Photograph of a two-pass prism compressor.
The angular dispersion and spatial lateral spectral shift after the first propagation through the
prism pair is removed during the second, reversed propagation through the pair.Therefore it is
very important that the two propagation tracks are strictly parallel
Theoretical Background 8
This adjustment must be verified during the measurement and modified if necessary
in order to achieve optimal pulse compression.
5 Angular Dispersion and Spectral Interferometry
6 Evaluation of Spectrally Resolved Interferograms
6.1 Principle of Spectral Interferometry
Spectrally resolved interferometry is a high-precision measurement technique suitable for
determining the dispersion of optical elements. In this method, an interferometer containing
the sample under investigation is illuminated by a broadband light source (e.g., a halogen
lamp or a Ti:sapphire laser).
When the reference arm length is properly adjusted, interference fringes appear at
the interferometer output. These fringes are spectrally resolved by a spectrometer. By
placing a linear detector array or camera in the image plane of the spectrograph, the
recorded interferograms can be analyzed numerically. The frequency-dependent intensity
distribution at the spectrometer output can be written as
I(ω) = IR(ω) + IT (ω) + 2p
IR(ω)IT (ω) cos [∆ϕ(ω)] , (II.6.1)
where IR(ω) and IT (ω) are the spectral intensities of the reference and test arms,
respectively, and ∆ϕ(ω) denotes the phase difference between the two interferometer arms.
The frequency-dependent phase term can be expressed as
∆ϕ(ω) = ϕ(ω) + ωτ, (II.6.2)
where ϕ(ω) is the spectral phase introduced by the sample and τ is the temporal delay
corresponding to the air-path difference between the interferometer arms.
6.2 Constant Phase Point
To determine the extrema of the normalized interferogram, we examine the derivative of
the phase term with respect to frequency. An extremum occurs when
d
dω ∆ϕ(ω) = 0. (II.6.3)
At the frequency satisfying this condition, the so-called constant phase point is formed.
Around this frequency, the phase varies only slowly with respect to ω, and the fringe spacing
locally becomes larger.
Changing the delay τ shifts the position of the constant phase point along the spectrum.
Substituting Eq. (II.6.2) into Eq. (II.6.3), we obtain
dϕ(ω)
dω + τ = 0. (II.6.4)
Since dϕ/dω corresponds to the group delay introduced by the sample, the position of
the constant phase point provides information about the sign and magnitude of the group
delay.
6.3 Minimum–Maximum Evaluation Method
The extrema of the interferogram occur when
Theoretical Background Minimum–Maximum Evaluation Method 9
sin [∆ϕ(ω)] = 0, (II.6.5)
which corresponds to phase values that are integer multiples of π:
∆ϕ(ωm) = mπ, (II.6.6)
where m is an integer index assigned to successive maxima and minima.
In practice, the measured and normalized interferogram is differentiated numerically,
and the zero-crossings of the derivative (sign changes) are identified to locate the extrema
frequencies ωm. By assigning integer indices m to the extrema (with m = 0 at the constant phase point if present within the measured spectral range), the spectral phase values
corresponding to each extremum can be reconstructed.
Plotting mπ as a function of ωm yields a discrete representation of the spectral phase
function. By fitting a polynomial to this curve, one effectively fits the Taylor expansion of
the phase:
ϕ(ω) = ϕ0 + ϕ1(ω − ω0) + 1
2
ϕ2(ω − ω0)
2 +
1
6
ϕ3(ω − ω0)
3 + . . . (II.6.7)
The coefficients correspond to:
• ϕ1 – group delay,
• ϕ2 – group delay dispersion (GDD),
Figure II.6.1. Phase as a function of frequency. Phase values obtained from the minimummaximum fitting
Theoretical Background Angular Dispersion 10
• ϕ3 – third-order dispersion (TOD).
If a second-order polynomial is fitted, only the GDD is obtained. Including a thirdorder term allows extraction of the TOD as well. The order of the polynomial that can
be reliably fitted depends on the number of measured extrema and the noise level of the
interferogram. A broader spectrum yields a larger number of extrema and therefore allows
higher-order dispersion terms to be determined more accurately.
The precision of the method can be improved by increasing the delay between the
interferometer arms, which results in a denser fringe pattern. A broader spectral bandwidth
also increases the measurement accuracy.
A limitation of the minimum–maximum method is the potentially laborious identification of extrema, especially in the presence of noise.
6.4 Angular Dispersion
One possible source of pulse distortion is the material dispersion of optical components,
whose temporal effects can be efficiently compensated using pulse compressors. However,
pulse distortion may also occur due to angular dispersion introduced by optical elements.
Figure II.6.2. Interferometer setup. A typical Michelson interferometer used for measuring
spectrally resolved interferograms of ultrashort pulses
Theoretical Background Physical Interpretation of Angular Dispersion 11
Angular dispersion arises when the different spectral components of a pulse propagate
in different directions after passing through an optical element. Typical elements that
introduce angular dispersion include prisms, diffraction gratings, acousto-optic deflectors,
as well as pulse stretchers or compressors that are not perfectly aligned.
6.5 Physical Interpretation of Angular Dispersion
In the case of material dispersion, pulse broadening occurs because monochromatic components of different wavelengths propagate in the same direction but accumulate different
phase shifts due to wavelength-dependent phase velocities.
A phase difference may also arise when the spectral components propagate at the same
speed but in different directions. This situation occurs when a pulse passes through an
element with frequency-dependent refraction (such as a prism) or reflection angle (such as
a diffraction grating), and subsequently propagates in a low-dispersion medium such as air.
Outside dispersive media, angular dispersion can exist without temporal chirp, while
inside materials both effects may occur simultaneously.
Figure II.6.3. Concept of angular dispersion created by
prism. The different colors represent different frequency components of a fs pulsed. In reality their frequency doesn’t differ
enough to cause real color difference, since the full bandwidth is
of about 20 nm
6.6 Definitions of Angular Dispersion
In practice, two different definitions of angular dispersion are used.
The first definition describes angular dispersion as the frequency dependence of the
propagation direction of the light beam:
dθ
dω , (II.6.8)
which is referred to as propagation-direction angular dispersion.
The second definition describes the frequency dependence of the angle between the
phase fronts of monochromatic components:
dϕ
dω , (II.6.9)
known as phase-front angular dispersion.
For plane waves, these two definitions yield identical results. However, for beams
with curved phase fronts, such as Gaussian beams, the two quantities differ. The phasefront angular dispersion manifests as pulse-front tilt, while propagation-direction angular
dispersion results in combined spatial and temporal phase modulation.
6.7 Measurement of Dispersion Using Spectral Interferometry
Spectrally resolved interferometry is a high-precision measurement technique that can be
used to determine the dispersion of optical components. In this method, an interferometer
Figure II.6.4. Ultrashort pulsed laser. The two definitions of the angular dispersion yield
different behavior of the spatial dispersion in the case of plane waves and Gaussian beams
Theoretical Background Measurement of Propagation-Direction Angular Dispersion 12
containing the sample under investigation is illuminated with a broadband light source,
such as a halogen lamp or a Ti:sapphire laser.
Interference fringes appearing at the interferometer output are spectrally resolved using a spectrometer. By placing a linear detector array at the spectrometer image plane,
the recorded interferograms can be analyzed computationally to extract dispersion information. The frequency-dependent intensity distribution of the recorded interferogram can
be expressed as:
I(ω) = I1(ω) + I2(ω) + 2p
I1(ω)I2(ω) cos [∆ϕ(ω)] , (II.6.10)
where ∆ϕ(ω) denotes the frequency-dependent phase difference between the interferometer arms.
6.8 Measurement of Propagation-Direction Angular Dispersion
The propagation-direction angular dispersion is measured using a spectrograph. The investigated beam is focused onto the entrance slit of the spectrograph using a focusing element
such as an achromatic lens or a concave mirror.
Due to angular dispersion, the spectral components of the pulse propagate in slightly
different directions. Consequently, they are focused onto different vertical positions at the
slit plane. Inside the spectrograph, the slit image is projected onto a CCD camera, while
the diffraction grating introduces wavelength-dependent horizontal dispersion.
As a result, the recorded spectrum appears tilted on the CCD detector. The tilt angle
is proportional to both the angular dispersion and the focal length of the focusing lens.
By selecting appropriate spectrograph parameters, angular dispersion can be measured
with an accuracy better than 0.2 rad/nm. This method enables real-time measurements and
Figure II.6.5. Ultrashort pulsed laser. The angularly dispersed beam is simply focused to
the spectrometer input slit by a 200 mm focal length lens
Theoretical Background Measurement of Phase-Front Angular Dispersion 13
is therefore particularly suitable for alignment of pulse stretchers and compressors. During
the measurement, the tilted spectral image is recorded with the camera. The saved image
is analyzed using numerical software such as MATLAB or Excel. Vertical intensity profiles
are extracted at different wavelengths, and the vertical positions of intensity maxima are
determined.
Considering the pixel size and the magnification of the spectrograph imaging system,
the ratio of vertical displacement to wavelength change can be calculated. Since the angular
deviations are small, the angular dispersion can be approximated by:
dθ
dλ ≈
y
f ∆λ
, (II.6.11)
where f denotes the focal length of the focusing lens. The software - Fringer - associated
to the spectrometer also measures this angular dispersion. This can serve as control for
the evaluation with other software, as listed between the measurement tasks.
6.9 Measurement of Phase-Front Angular Dispersion
Figure II.6.6. Interference
pattern without angular dispersion. The interference stripes
are parallel
Figure II.6.7. Interference
pattern with strong angular
dispersion. The interference
stripes are strongly curved
Phase-front angular dispersion is measured using the same spectrograph combined with a
Mach–Zehnder interferometer. The interferometer is adjusted such that one beam undergoes an additional reflection compared to the other, resulting in overlapping beams at the
spectrograph entrance slit.
Figure II.6.8. Mach-Zehnder interferometer combined with a spectrometer. The
interferometer produces interference between laterally spatially dispersed beams. One of the arms
contains one reflection more than the other, hence different frequency beam portions are overlapped, when lateral spatial dispersion is in the beams
By slightly tilting one of the interferometer mirrors, interference fringes perpendicular
to the slit direction are generated. If angular dispersion is present, the interference fringes
become curved in the spectrally resolved interferogram.
Quantitative determination of angular dispersion is achieved by analyzing the wavelength dependence of the fringe spacing. If the spectral components are parallel, the fringe
period varies linearly with wavelength. Deviations from linearity indicate the presence of
angular dispersion.
7 Investigation of Ultrashort Laser Pulses Using an Autocorrelator
7.1 Preliminary Verification
First, verify using a fast photodetector that the pulse duration is shorter than the temporal resolution limit of the available detector. This confirms that conventional electronic
measurement techniques are insufficient for direct pulse duration determination.
7.2 Laser Initialization and Spectral Characterization
Start the femtosecond laser system. If a tunable laser is used (e.g., a Ti:sapphire laser),
select the desired operating wavelength using the spectrometer. Establish communication
between the spectrometer and the computer, and if required, between the laser and the
control software.
Measure the output optical power and record the spectral profile of the laser emission. Use neutral density filters or beam sampling plates if necessary to prevent detector
saturation.
7.3 Determination of Transform-Limited Pulse Duration
Using the measured spectral bandwidth, estimate the transform-limited pulse duration
assuming different pulse shapes, such as Gaussian and Sech2 profiles.
7.4 Autocorrelator Setup and Direct Pulse Measurement
Determine the maximum permissible input power of the autocorrelator based on its sensitivity specifications. Adjust the input power accordingly using beam samplers or attenuators.
Align and calibrate the autocorrelator, and measure the pulse duration of the beam directly exiting the laser, ensuring that the beam propagates through as few optical elements
as possible.
Determine the pulse duration under different pulse-shape assumptions by:
• direct readout from the autocorrelator display,
• numerical evaluation using computational tools such as MATLAB.
14
Measurement Tasks 15
Compare the measured pulse duration with the previously calculated transform-limited
value.
III Measurement Tasks
8 Dispersion Compensation Using a Prism Compressor
8.1 Experimental Equipment
The following equipment is used during the experiment:
• Femtosecond laser system (average power ∼ 400 mW, pulse duration ∼ 50 fs, spectral
FWHM ∼ 12 nm)
• Avantes spectrometer operating in the 500–1000 nm wavelength range
• Coherent optical power meter
• APE autocorrelator
• glass plate for outcoupling part of the power for measurement
• Prism compressor aligned with the beam path:
– first prism on translation stage
– second prism on translational and rotational stage
• mounted mirror for outcoupling after the compressor
• dispersive samples of different materials
• computer software to evaluate autocorrelator traces
8.2 Measurement Procedure
Objective of the Measurement The aim of this task is to gain practical experience in
the positioning and operation of an optical autocorrelator, as well as in the routine use of
a spectrometer and optical power meter. The students perform autocorrelation measurements of ultrashort laser pulses and apply various experimental techniques necessary for
the successful execution of the measurement.
An additional objective is the numerical calculation of autocorrelation functions using
computer software and the critical evaluation of the obtained experimental results.
1. Laser startup and mode-locking verification.
Switch on the Ti:sapphire laser by tuning the pump laser to maximum power. Verify
that the output power exceeds 400 mW using the power meter. Turn on pulsing by pushing
the enable button of the acousto-optic modelocker.
Start the spectrometer software (AVASOFT) and display it in full-screen mode. Direct
the spectrometer fiber input toward a visible scattered spot from a mirror and observe the
spectrum on the screen. If necessary, optimize the output power and spectral shape by
adjusting the end mirrors and intracavity prisms while continuously monitoring both the
spectrum and the output power. At the final stage, initiate stable pulsed operation by
rapidly adjusting the prism micrometer.
Measurement Tasks Measurement Procedure 16
2. Spectral measurement.
Use the spectrometer to confirm that the laser operates in mode-locked pulse regime.
The laser is considered to operate properly in pulsed mode if the spectral bandwidth exceeds
10 nm. With the cursor measure the wavelength full width half maximum of the spectrum.
Save the recorded spectrum for later evaluation.
3. Initial pulse duration measurement.
Extract a small fraction of the laser beam using a glass plate and direct the reflected
beam (which does not pass through the glass and is therefore approximately transformlimited) into the autocorrelator.
Align the autocorrelator using the crosshair reference and adjust its position until an
optimal signal amplitude is obtained. Ensure that the autocorrelator housing is perpendicular to the incident beam.
Measure and record the temporal pulse shape and pulse duration of the laser output.
4. Prism compressor alignment.
Using the appropriate mirror, guide the laser beam into the prism compressor. Adjust
the prisms to operate at Brewster angle such that the intensity of the beam reflected from
the first prism surface is minimized. This can be checked visually on a screen or more
precisely with the power meter.
The rear mirror of the compressor vertically displaces the incoming and outgoing
beams. Ensure that both beams pass entirely through the prisms and that the outgoing beam exits directly above the incoming beam. The exiting beam must pass above the
coupling mirror without obstruction.
5. Pulse measurement after compressor.
Use a glass plate to sample the compressed beam and direct the reflected portion into
the autocorrelator. Measure both the pulse duration and the corresponding spectrum.
6. Compensation of additional dispersion (glass plate).
Insert a prepared 1 cm thick glass plate between the compressor output mirror and the
beam-sampling plate.
Realign the autocorrelator to obtain maximum signal. If the measured pulse duration
exceeds 300 fs, replace the plate with a thicker glass block.
Using the translation stage, adjust the position of the second prism in the compressor
to minimize the pulse duration measured by the autocorrelator. Ensure that the outgoing
beam remains directly above the incoming beam and that the beam is not clipped by prism
edges. This can be achieved by fine adjustment of the second prism in both translational
directions.
Record:
• the autocorrelation trace,
• the pulse duration assuming a Sech2 pulse shape,
• the distance between the two prisms,
• the distance between the second prism and the retroreflecting mirror.
7. Measurement with glass cube.
Replace the thin glass plate with a glass cube. Adjust the compressor again to minimize
the pulse duration measured by the autocorrelator (realign the autocorrelator if necessary).
Record:
Measurement Tasks 17
• the autocorrelation signal,
• the emission spectrum,
• the pulse duration (Sech2 assumption),
• prism separation distances with a tape measure.
8. Comparison and analysis.
Compare the measured pulse durations for the beam transmitted through the glass
plate and the glass cube. Compare the corresponding prism separations in the compressor
with the physical lengths of the glass samples along the propagation direction.
If the ratios of glass thickness and compressor length adjustment differ, provide a
physical explanation for the discrepancy.
9. Compensation of dispersion introduced by an acousto-optic element.
Insert an acousto-optic filter between the compressor output mirror and the beamsampling plate.
Adjust the prism separation and relative prism positions to minimize the pulse duration
measured by the autocorrelator. If the travel range of the second prism is insufficient,
release the mechanical mounting screws and reposition the second prism assembly relative
to the first prism, then secure it again.
Record the autocorrelation trace, pulse duration (Sech2
), prism separation, and the
distance between the second prism and the retroreflecting mirror.
9 Experimental Setup and Measurement Procedure for spectral interferometry
9.1 Experimental Equipment
The following equipment is used during the experiment:
• He-Ne laser for preliminary adjustment of the model interferometer
• Model interferometer for adjustment training
• Femtosecond laser system (average power ∼ 800 mW, pulse duration ∼ 50 fs, spectral
FWHM ∼ 16 nm)
• Avantes spectrometer operating in the 500–1000 nm wavelength range
• Optical power meter
• Two interferometric setups mounted on linear translation stages:
– Michelson interferometer
– Mach–Zehnder-type interferometer (one arm containing one additional reflection)
• Each interferometer includes:
– at least two angle-adjustable mirrors,
– at least one beam splitter cube,
– input and output apertures
Measurement Tasks Spectral Interferometry Measurement 18
• All mirrors are mounted on linear translation stages enabling displacement perpendicular to the mirror surface
• BK7 glass cube for dispersion measurements
• glass prism for generating angular dispersion
• High-resolution spectrograph with CCD camera for interferogram acquisition
• Computer running the FRINGER evaluation software
• MATLAB or Excel for numerical analysis
9.2 Spectral Interferometry Measurement
1. Adjusting the model interferometer Switch on the He-Ne laser and verify the
beam path through the beam expander. Verify that the beam propagates parallel to the
optical table before the interferometer using a mounted variable aperture. Adjust the beam
direction and the mirrors of the interferometer until the beams at the output are completely
overlapping. Observe the interference pattern on a screen and the change of the stripes
when the reflection angle of one of the mirrors is adjusted.
2. fs laser characterization. Switch on the laser if it is not already running and
verify both the output power and the emission spectrum. Estimate the spectral bandwidth (FWHM). If the bandwidth is below 10 nm, adjust the laser (with the instructor’s
assistance) to ensure proper mode-locked operation.
3. Michelson interferometer alignment. Set up the Michelson interferometer
such that the two output beams overlap along the entire propagation path from the beam
splitter to the spectrometer. Adjust the arm lengths to be approximately equal using a
measuring tape.
4. Spectrometer alignment. Insert the spectrometer and align the beams onto the
entrance slit. Observe the spatial overlap of the two beams in the non-dispersed direction on
the CCD camera. Once interference fringes appear, optimize fringe sharpness and contrast
using mirror adjustments and fine (micrometer-resolution) linear translation stages. A
single line distance corresponds to 0.2 micrometers on the finer translation stage.
5. Interferogram acquisition. Record interferograms at several different arm-length
differences. Additionally, record the individual intensity spectra of the reference and sample
arms (without interference), which are required for normalization. With the light blocked,
measure the background signal and enable automatic background subtraction.
Figure III.9.1. Typical interference pattern. The interference stripes are shifted with the
ssample introduced into the beam
path
6. Measurement with dispersive sample. Insert the BK7 glass cube into the sample arm and adjust the interferometer to restore equal arm lengths. Record interferograms
at several delays. Again, measure the individual spectra of both interferometer arms and
record the background before starting the acquisition.
7. Dispersion extraction. If the data quality permits, register interferogram for
both the empty interferometer and the configuration including the dispersive sample. Determine the group delay dispersion (GDD) introduced by the sample from the shift of the
interferogram due to the sample, and if the signal-to-noise ratio allows, also extract the
third-order dispersion (TOD).
9.3 Angular Dispersion Measurement
8. Generation of angular dispersion. Guide the laser beam through the prism ensuring
incidence at Brewster angle at the first prism face. Direct the diffracted beam through
Measurement Tasks Control Questions 19
the Mach–Zehnder interferometer. At the interferometer output aperture, ensure spatial
overlap of the beams.
9. Adjustment of the spectrometer and interferometer Position the spectrometer after the interferometer, parallel to the interferometer axis. Insert the mirror-based
beam steering and polarization control system between the interferometer output and the
spectrometer entrance slit. Adjust mirror angles and heights to achieve proper alignment
and visible interference fringes on the CCD camera.
Adjust the optical path difference using the linear translation stage until interference
fringes appear. Ensure that the optical path between the interferometer and the spectrometer is at least 300 mm.
10. Propagation-direction angular dispersion measurement. Block one interferometer arm. Insert a focusing lens (f = 100 mm or f = 200 mm) before the spectrometer
to focus the beam onto the entrance slit.
Record the tilted spectrum on the CCD camera. Fit a straight line to the tilted spectral
trace according to the theoretical relation:
dθ
dλ ≈
y
f∆λ
, (III.9.1)
and determine the value of propagation-direction angular dispersion.
11. Software comparison. Compare the manually calculated angular dispersion
with the corresponding value obtained from the FRINGER software fitting procedure.
12. Interferometric verification. Remove the beam block and allow both beams to
propagate through the interferometer and spectrometer. Record interferograms at several
arm-length differences and evaluate them using FRINGER. Compare the results with those
obtained from the direct angular-dispersion measurement.
9.4 Control Questions
1. What is meant by the term spectral interferometry?
2. What ensures temporal coherence necessary for the formation of interference fringes?
3. What determines the position of a constant-phase point in the spectrum?
4. How does the minimum–maximum method for interferogram evaluation work?
5. Sketch the main difference between interferometric setups used to measure angular
dispersion and those used to measure temporal pulse broadening (material dispersion).