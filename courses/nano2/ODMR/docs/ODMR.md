1
Physicist-Engineer Nanotechnology and Quantum Applications
Specialization Laboratory Measurement 1:
Qubit Manipulation in NV Diamond System
This development was carried
out within the framework of
the project ’Practice-Oriented
Higher Education Infrastructure and Skills Development at
BME’ (Project ID: RRF-2.1.2-
21-2022-00005), supported by a
non-refundable grant from the
Recovery and Resilience Facility
funded by the European Union
and the Government of Hungary.
The development of this lab exercise was funded by Faulhorn
Zrt.
Abstract. Qubits are the fundamental building blocks of quantum technologies, enabling the coherent control and manipulation of quantum states for sensing and information processing applications. Among solid-state platforms, the nitrogen-vacancy
(NV) center in diamond offers optical initialization and readout combined with long
coherence times under ambient conditions.
In this measurement, you will encounter microwave-driven spin manipulation and
optical detection techniques to investigate coherent dynamics, relaxation processes,
and decoherence mechanisms. In particular, Rabi oscillations and relaxation times are
measured to characterize the controllability and coherence properties of the system.
Warning. This measurement makes use of a high power laser and a micorwave amplifier. These devices pose a significant safety risk if handled incorrectly. Carefully read
the safety instructions found in Chapter IV before entering the lab and follow them
at all times. Consult the lab instructor if in doubt and follow their instructions.
Warning. It is recommended to bring your own laptop for this measurement. The
required software is detailed in Prerequisites.
I
Introduction
1 Quantum bits as basis for future computing
The semiconductor industry has had a profound impact over the last several decades. Consequently, improvements in this field have been heavily pursued, leading to the formulation
of the well-known Moore’s law, which predicts a rapid increase in transistor density over
time. However, in recent years the progress has begun to deviated from this expected
trend, as modern devices approach the physical limitations of classical computation. The
smallest commercially developed transistors are 2 nm wide. At this scale, classical physics
can no longer describe the physical systems accurately. As a result, quantum mechanics
must be incorporated into both the theoretical description and practical design of such
systems. This naturally raises an interesting question: why should we stick with conventional transistor architectures? Why shouldn’t we utilize the intrinsic quantum mechanical
properties of nature to achieve fundamentally new computational capabilities?
Figure I.1.1. Difference between
classical and quantum bits.
The foundation of quantum computational systems are quantum bits or qubits, that
are similar to classical bits in a sense that we require them to be in just two states when
measured. But an important distinction between them is that while a classical bit can only
be in either the 0 or the 1 state all the time, a qubit can also be in a coherent superposition
of both. Operations on a qubit affect both states simultaneously while its in superposition.
So, an operation on N qubits would extend on 2
N values, therefore exponentially increasing
the parallelism and similarly decreasing the computational time. Important to note, that
not every two state quantum system is suitable to be a qubit. There are certain conditions
that need to be met in order to create a proper quantum computer. These are described
by the DiVincenzo criteria [1].
Information may be physically realized in a variety of ways. One prominent platform
is superconducting circuits, where microwave resonators and Josephson junctions are fabricated to form effective two-level systems. In trapped ions and neutral atoms, internal
atomic states are utilized, while in photonic systems the qubit is typically encoded in the
polarization of light. There are also options to implement a qubit in solid-state platforms.
One such approach is based on semiconductor qubits, most commonly realized using quantum dots, whose quantum states are controlled by electrostatic gate voltages. Alternatively,
qubits can be formed from crystal lattice defects in solids. These atomic-scale defects –
also known as point defects – occur in wide-bandgap crystals, where the unique electronic
structure of the localized defect states enables their use as qubits. Such point defects are
the focus of this laboratory measurement. In particular, you will become acquainted with
nitrogen-vacancy centers in a diamond environment.
2
Diamond embedded nitrogen-vacancy centers 3
2 Diamond embedded nitrogen-vacancy centers
2.1 Formation of NV centers
Diamonds are well known for being mechanically robust and having a very stable crystal
structure. These properties make them desirable for a wide range of applications, but
the high price of natural diamonds has limited their widespread use. Fortunately, artificial
diamonds can now be produced easily and reliably, so much so, that these can be more pure
– have less imperfections – than the naturally formed crystals. Because diamond growth
techniques are now well-developed, it is possible not only to grow high-quality crystals but
also to control what kind and how much imperfections can form in the crystal lattice.
During the growth process, nitrogen is introduced in the growth chambers which slowly
builds in to the tetragonal carbon structure resulting in nitrogen point defects. Most
commonly a nitrogen atom substitutes a carbon atom and bonds with the neighboring
four carbon atoms, leaving one unpaired electron. To form nitrogen-vacancy (NV) centers,
the crystal needs an additional type of defect: a vacancy, which is an empty lattice site.
Vacancies are created by damaging the crystal in a controlled way, for example by exposing
them to high-energy particles such as ion beams or neutron radiation from reactors. This
step is followed by a heat treatment at around 800 ◦C. In the annealing process, the crystal
heals itself and the vacancies become mobile, meaning they can move through the lattice.
With a finite probability, a vacancy can reach a nitrogen atom and become trapped next
to it, an NV center is formed. At the treatment temperatures, it is energetically favorable
for the vacancy to remain beside the nitrogen rather than continue hopping around the
lattice sites. This makes the NV center a stable defect, which can exist even at relatively
high temperatures.
Figure I.2.1. Illustration of a
negatively charged NV center [2].
Interestingly, this neutral NV center is not focus of most research. The charge-neutral
state (NV0
) does not exhibit the unique properties that make it suitable as a qubit. What
is usually referred to as the NV center is the one-times negatively charged state. The
additional negative charge comes from the ionization of a substitutional nitrogen atom.
The released electron becomes mobile and can be captured by the NV center, thereby
forming the NV− state. In most experimental conditions, the NV center is stabilized in
this negatively charged state (NV−), which is the charge state related to quantum control
and optical readout. As this is the experimentally relevant configuration, any reference to
an NV center in the following (and in general) will implicitly refer to the negatively charged
state.
2.2 Energy states and spin polarization
The NV center effectively is a six-electron-system: 3 electrons come from the unpaired
electrons of the three carbon atoms near the vacancy, 2 from the lone electron pair of the
nitrogen atom and 1 from the ionized substitutional nitrogen. Due to symmetries of the
crystal, they essentially create an electron system with a total spin number S = 1. So, the
ground state of the NV center is a spin triplet with an energy level that would be three
times degenerate. However, in electron systems with S ≥ 1 arises an interaction between
electrons called zero-field splitting. The result of this effect is that the states with different
Sz components will split without the presence of outside magnetic field caused by the spinorbit coupling and dipole-dipole interactions. In case of the NV center, the energy levels
relating to the |Sz = 0⟩ = |0⟩ and the |Sz = ±1⟩ = |±1⟩ states will separate with an energy
difference of D = 2.87 GHz.
Diamond embedded nitrogen-vacancy centers Energy states and spin polarization 4
Figure I.2.2. Absorption and emission spectrum of the negatively charged nitrogen-vacancy
center [3].
What makes the NV center unique is its optical cycle. From the spectra shown on
Fig. I.2.2, it can be seen that the defect predominantly absorbs photons in the green
region of the visible spectrum, while it emits mostly red light through a photoluminescence
process. From an energy-level perspective, green light excites electrons from the ground
state to a higher-lying excited state. From there, the electrons can relax back to the
ground state via two different pathways: radiative decay (fluorescence) or a non-radiative
intersystem crossing. These processes can be followed on Fig. I.2.3. An intersystem crossing
corresponds to a transition from a triplet state to a singlet state. This singlet has only
one possible spin projection, whose wavefunction is noted with |0
′
⟩. The |0⟩ triplet state
can decay into the |0
′
⟩ singlet state without changing its spin projection, whereas the |±1⟩
states must have a spin transition as well, increasing or decreasing its Sz quantum number.
This spin-changing transition is forbidden to first order, but there is a finite transition rate
contributing to this event. In reality, the |±1⟩ → |0
′
⟩ transition has a higher probability
than the |0⟩ → |0
′
⟩ one, leading to an effective depletion of the |±1⟩ states. From the singlet
state, a second intersystem crossing is required to return to the triplet ground state. This
transition is also spin selective, the |0
′
⟩ state is more likely to relax into the |0⟩ ground
state than into the |±1⟩ states. Consequently, during an optical cycle a |±1⟩ particle is
likely converted into a |0⟩ state. After many such cycles — corresponding to prolonged
green-light excitation — the NV center is highly likely to be found in the |0⟩ ground state.
This process effectively polarizes the electron spin into a well-defined Sz sublevel.
Remark. The decay between singlet states may
emit infrared radiation.
This is filtered out in the
setup.
Triplet
ground state
|0⟩
|±1⟩
Triplet
excited state
|0⟩
|±1⟩
Singlet
states
520 nm
637 nm
1042 nm
Non-radiative transition
Intersystem crossing
Figure I.2.3. Energy scheme of the negatively charged nitrogen-vacancy center [4].
Optically Detected Magnetic Resonance technique 5
The asymmetry of spin-sublevels is not only reflected in the intersystem crossing rates,
but also in the fluorescence intensity. Since optical transitions are spin-state preserving,
no spin flip occurs during the optical excitation and radiative decay. Because the excited
|±1⟩ states are more likely to decay into the singlet manifold, the probability of radiative
decay — and thus the emission of a red photon — is reduced for these states. Essentially
this means, that an NV center in the |0⟩ state emit - on average - more photons than when
it is in the |±1⟩ states.
We conclude that we can initialize the spin-sublevel to the |0⟩ state by extended laser
excitation and read out the current spin-state by probing the fluorescence signal with a short
laser pulse. High fluorescence indicates the |0⟩ sub-state and low fluorescence indicates the
|±1⟩ sub-state.
3 Optically Detected Magnetic Resonance technique
While magnetic resonance is concerned with transitions between states that differ in their
Sz spin quantum numbers, optical transitions occur between states that differ in their electronic configuration. Although magnetic resonance techniques have been well established
for more than seventy years, their sensitivity is relatively low when compared to optical
spectroscopic methods. In cases where the sensitivity of conventional magnetic resonance
is insufficient, it is often possible to increase the population difference between the different
magnetic sublevels by optical pumping. In optically detected magnetic resonance (ODMR)
the aim is to combine magnetic resonance with laser spectroscopy in order to significantly
improve sensitivity and to access additional information about the spin system. [5]
The central idea of ODMR is that magnetic resonance transitions are detected indirectly through changes in the optical signal. When a magnetic resonance condition is
fulfilled, the redistribution of spin populations leads to a measurable change in photoluminescence intensity. This way, spin-state transitions can be observed with optical sensitivity.
Regarding the NV center, ODMR is realized by combining optical readout of the spinstate (|0⟩ or |±1⟩) with the energy splitting of spin-levels (zero-field splitting, Zeeman
effect) in the gigahertz-range.
II Measurement Methods
1 Theoretical Description
It is well known that measuring a quantum state without modifying it in the process is often
impossible, the electron system of NV centers are no different. As described before, there is
difference in photoluminescence intensity for photons emitted from different spin-sublevels,
this means that we could potentially differentiate for which state the NV center is in.
For one NV center (one physical qubit), one electron excitation would accompany one red
photon emission, thus intensity difference would manifest as an average from multiple shots.
As single photon detection goes beyond the scope of this lab course, the measurements will
be done on a diamond sample that is dense with NV centers. This guarantees a large
photon flux that can be measured with common photosensors, in hindsight, this NV center
ensemble will only act as a pseudo-qubit.
An important part of qubits is the initialization, i.e. setting the initial state with the
utmost precision, so that the time evolution of system is from a well-defined position. In
NV qubits, the initial state is the |0⟩ state. Unfortunately, both initialization and readout
are performed by the same action: optical excitation. As such, we cannot read out the
state without also pushing it towards the |0⟩ state; meaning, a continuous readout will erase
any information about the time-evolved state. This effectively eliminates the possibility of
simply hooking the system up to an oscilloscope and measuring the transient signal.
1.1 Relaxation Time
Remark. Larmor precession: An outside B0 magnetic field causes the spin
dipole moments to precess
around the B0 field vector
with an angular frequency
of ωLarmor = γB0.
In order to obtain information about the system, it must be probed for a controlled
period of time; therefore, a pulsed laser scheme is required. The initialization pulse must
be sufficiently long for the optical cycle to be repeated many times, ensuring that the NV
centers are polarized into the |0⟩ state. The readout pulse, on the other hand, should
be short enough to minimize disturbance of the system, yet long enough to generate a
sufficient number of photons to produce a measurable signal. Let us denote the time delay
between the initialization and readout pulses by τ . As the delay is increased, the detected
signal during the readout period decreases. This is due to relaxation processes that drive
the polarized system back toward thermal equilibrium, where the electron populations
are developed according to the Boltzmann distribution. Starting from the fully polarized
state (with the NV centers predominantly in |0⟩), thermal excitations gradually repopulate
the |±1⟩ states. The decay – or relaxation – of the polarized state typically follows an
exponential behavior with a characteristic time denoted by T1. This is the timescale over
which the spin system retains its polarization.
Figure II.1.1. Spin relaxation in
the lab frame.
When a lock-in amplifier (see Lock-in Amplifier) is used, the T1 measurement scheme is
slightly modified (Fig II.1.2). Without a lock-in amplifier, the absolute fluorescence signal
is detected. In contrast, a lock-in amplifier measures the difference (or contrast) between
two alternating conditions. This is achieved by applying the readout pulse during one half
of the lock-in reference period and omitting it during the other half. A contrast can only be
meaningful, if the conditions are the same for both cases, i.e. there must be an initialization
pulse at the beginning of both half-cycles. With this differential detection technique, only
the signal modulation needs to match the timescale of the measured relaxation process,
6
Theoretical Description Continuous Wave ODMR 7
while the lock-in amplifier enhances sensitivity by rejecting uncorrelated background noise.
Figure II.1.2. Pulse sequence for measuring the T1 relaxation time [6]. After the initializing
laser pulses, the qubit states are in |0⟩. Leaving the system freely evolve in time, the states relax
back to their equilibrium state: (rougly) the same number of |0⟩ and |1⟩ states. However, if this
propagation is interrupted with the readout pulse, then the fluorescence signal intensity coming
from an intermediate state is related to its relaxation process.
1.2 Continuous Wave ODMR
Figure II.1.3. Effect of a MW
pulse in the lab frame.
Figure II.1.4. Effect of a MW
pulse in the rotating frame.
Remark. In lab frame,
the disturbed spin rotates
around the z-axis due to
Larmor precession. This
constant rotating movement can be transformed
out, giving a simpler
picture in the rotating
frame.
You may have noticed that in the T1 measurement no microwave (MW) field was
applied. This is because we did not yet intentionally drive transitions between the spin
states. Although the measurement still provides information about the spin system, it
arises purely from the optical cycle, which polarizes into the |0⟩ state. When a microwave
field is applied, it can induce transitions between spin sublevels. In this sense, the MW
can be regarded as a field that causes spin-flips, since absorption of a microwave photon
changes the Sz spin projection by ±1. This is demonstrated on Fig. II.1.4, the state vector
is rotated from |0⟩ into |1⟩. So, the microwave acts as a driving force on the system: its
phase determines the rotation axis, while its amplitude (or power) determines the rotation
rate. The duration of the MW pulse controls the rotation angle, so spin-flip is not an
instantaneous event, but rather a continuous transition between the two states.
The term Continuous Wave (CW) refers to the fact that the MW excitation is applied
continuously rather than in pulses. In parallel, the laser is also kept on, providing constant
optical excitation and spin polarization. In this situation, three processes compete with
one another: the MW that would rotate the states; the optical pumping into |0⟩ and
the T1 relaxation that drives the system toward equilibrium. Depending on the relative
timescale of these processes, a steady state is formed in which the photoluminescence signal
is constant. When the MW is turned off, the signal is maximal as the steady state becomes
the |0⟩ state. As the MW power (or in case of MW pulses, the pulse length) is increased,
the |1⟩ state gets more and more mixed into the NV centers’ state. This results in the
decrease of the photoluminescence signal due to the lower photon emission rate of the |1⟩
state.
One essential property of the microwave field is its ωMW angular frequency. Efficient
rotation of spin states occur only under resonance conditions, when the microwave photon
energy matches the energy difference between the spin sublevels. In the presence of an
external magnetic field B0, the Zeeman interaction contributes to the level splitting:
∆E = ℏωMW = γℏB0,
Theoretical Description Rabi Oscillation 8
where γ is the gyromagnetic ratio of electrons and ℏ is the reduced Planck constant. Resonances may arise from the zero-field splitting, the Zeeman interaction, or hyperfine coupling. Whenever the resonance condition is satisfied, a dip appears in the fluorescence
intensity. By sweeping the MW frequency, the resonant spin transitions can be mapped
out. The transition lines are revealed as valleys.
When using a lock-in amplifier, the basic principle remains the same. Now the key information is from to MW resonance, thus the MW field needs to be modulated on and off
during the two lock-in half period, while the laser remains continuously on. The lock-in amplifier then detects the fluorescence contrast between the MW-on and MW-off conditions,
significantly improving sensitivity.
1.3 Rabi Oscillation
The Rabi cycle describes the cyclic evolution of a two-level quantum system in the presence
of an oscillatory driving field. In the case of the NV center, a microwave field plays this
exact role of the driving field. When applied on resonance, the MW field coherently rotates
the NV spin state within the two-level subspace. The system is driven in and out of the
pure basis states, and the populations oscillate harmonically between them. The inverse of
one oscillation period defines the Rabi frequency, which scales linearly with the amplitude
of the driving field: ωRabi = γB1. To measure this effect experimentally, microwave pulses
of varying duration are applied in order to see how long it takes for the system to rotate
from |0⟩ to |1⟩. The resulting oscillatory fluorescence signal reveals the Rabi oscillations.
Figure II.1.5. Pulse sequence for observing Rabi oscillations [6]. The initializing pulses also serve
as the readout and create the measured signal. The first pulse, without a preceding MW rotation,
provides the baseline signal. In the second half-cycle, a MW pulse rotates the spin state before
the laser pulse, the resulting change in the initial fluorescence yields the contrast. The disparity
is enhanced when repeating the respective pulses in each half-cycles multiple times.
With help of the lock-in amplifier, the pulse sequence can be modified to directly
measure contrast (Fig. II.1.5). Since lock-in detection requires two alternating conditions,
one half of the reference period contains the MW pulse sequence, while the other half
does not. In both half-cycles, an initialization pulse is applied to ensure identical starting
conditions. However, a readout pulse is not strictly necessary as it turns out, it can be
replaced by the second half’s initialization pulse. You can look at this as if we were to shift
the sequence in a way that the initialization pulses were at the end of the half periods. In
other words, the readout effectively occurs at the beginning of the next initialization pulse,
where the short-time fluorescence reflects the rotated spin state. The difference between the
Experimental Setup 9
two half-cycles create the lock-in contrast and reveals the strength of the microwave-driven
rotation. Since the T1 relaxation typically takes place on a much longer timescale than the
Rabi oscillations and because lock-in detection suppresses slow background variations, the
MW and laser pulses can be repeated multiple times within one half-cycle. This significantly
enhances the signal-to-noise ratio and reduces the total measurement time.
Although it may seem that the Rabi cycle can be measured for arbitrarily long MW
pulse durations, it is not the case. If the time between two laser pulses becomes comparable
to the T1, relaxation processes begin to limit the measurable signal contrast. Moreover,
additional decoherence mechanisms reduce the visibility of the oscillations. The spatial
inhomogeneity of the driving MW field causes different NV centers to rotate at slightly
different rates, conceptually resulting in incoherent rotations. Another important process
is the transverse relaxation, or dephasing, characterized by the time constant T2. This relaxation mechanism describes the loss of phase coherence in the transverse (x–y) plane and
is directly connected to qubit information retention time. As a result, the Rabi oscillations
are not perfectly sustained but exhibit an exponentially decaying envelope governed by the
relevant (effective) coherence times.
2 Experimental Setup
Magnet
Objective
Dichroic mirror
532 nm LPF
800 nm SPF
CPW
PD
LD
Mirror
Microcontroller IQ modulator
MW source
MW Amplifier
Lock-in
amplifier
I/V converter
Computer
Figure II.2.1. Block diagram of the experimental setup.
Remark. The detector
and the objective are
mounted to an optical
cage, so they do not need
to be aligned manually.
2.1 Optics
Optical excitation is provided by a 520 nm green laser diode (ThorLabs L520P50), which
is rated for a continuous output of 50 mW and can be modulated at up to 3 MHz by interrupting its power supply with a 2N7000 n-channel MOSFET (although higher frequencies
are possible with a more sophisticated driver circuit). The diode’s output is collimated and
is reflected by an adjustable mirror (which serves to give extra degrees of freedom for alignment) onto a fixed dichroic mirror. This mirror element is highly reflective below a cutoff
wavelength, while being transparent above it. The green light is focused onto the sample
Experimental Setup Microwave Setup 10
by a microscope objective, and the produced photoluminescence is collected through the
same objective as well. The collimated beam of red light passes through the dichroic mirror
without reflection and is filtered to the desired wavelength range of 532 nm - 800 nm by a
short and a long pass filter before hitting the detector.
2.2 Microwave Setup
The required microwave radiation is generated by a Kuhne MKU LO 8-13 PLL-2 oscillator,
which has a variable output frequency. This signal is then fed into a Texas Instruments
TRF370417EVM quadrature modulator (IQ modulator), which can do one of three things:
either block the signal, let it through in-phase (I) or with a 90◦ phase shift (Q). This
modulated signal then optionally goes through a Kuhne KU PA 270330-10A microwave
amplifier, which can output up to 10 W power. Finally, the microwave enters an antenna
called a coplanar waveguide. The sample is mounted on this waveguide. The microwaves
that were not absorbed by the sample or radiated away are converted to heat by a 30 dB
high power attenuator, while a 50 Ω termination eliminates reflections.
2.3 Detection
Figure II.2.2. PDAPC1 photodiode with integrated I/V converter.
Thorlabs, Inc.
The photoluminescence signal from the sample is detected by a Thorlabs PDAPC1 photodetector. This device includes a photodiode and the required I/V conversion circuits, all
on a single PCB. The gain is adjustable, but changing it during the measurement will not
be required. The detector’s signal is connected to a Stanford Research Systems SR830M
lock-in amplifier with an added 50 Ω termination.
2.4 Lock-in Amplifier
The measurement techniques (like the T1 measurement) work fine on their own only if you
have high-sensitivity sensors with low noise characteristics. Even if you have a state-of-theart setup, getting as high of a signal-to-noise ratio is worth the while. That is why ODMR
is usually complemented with a lock-in amplifier, in this setup we use a SR830M model
from Stanford Research Systems. It acts as a band-pass filter, the decreased bandwidth
also decreasing the shot noise. It can also extract small changes or transient signals that
carry the relevant information of the fluorescence process. The first and second half of the
lock-in period time naturally introduce a contrast feature between the two halves, as the
first half is collected with a positive sign and the second half with a negative sign. The
short photoluminescence process makes it possible to repeat the measurement frequently,
utilizing that the amplifier integrates the incoming signal over a longer period of time
(conversion time). Thus more measurements can be collected in one data point yielding a
higher signal, while also decreasing its noise.
2.5 Computer Control
Figure II.2.3. Raspberry Pi Pico
2 microcontroller.
Raspberry Pi Ltd.
The control of the experimental setup is done via a Raspberry Pi Pico 2 microcontroller,
which has been flashed with a custom firmware. This firmware allows it to synthesize
precisely timed and synchronized pulse sequences on up to 5 channels. The device is used
to generate a reference signal for the lock-in amplifier and for the modulation of the laser
and the two microwave channels. The measurement control computer interfaces with the
microcontroller and the lock-in amplifier to set up measurements and read the results.
III Measurement Tools
and Programming
List of Measurement Tools.
1. Custom measurement control board, including:
• Pulse sequence generator (Raspberry Pi Pico 2 with pico-pulse firmware)
• Quadrature modulator (Texas Instruments TRF370417EVM)
• Laser power supply and modulator
2. Lock-in amplifier (Stanford Research Systems SR830M)
3. Photodiode with I/V converter (Thorlabs PDAPC1)
4. Lab bench power supply
5. Microwave assembly:
• Microwave oscillator (KUHNE MKU LO 8-13 PLL-2, Oscillator)
• Microwave amplifier (KUHNE KU PA 270330-1)
A python library has been created to help interface with the measurement devices.
This library is available on GitHub. The Devices subdirectory contains the relevant device
drivers and working experimental code is found in Experiments. While the latter is available
for use should it be necessary, students are expected to write their own code, as it will
contribute to the lab notes score.
1 Prerequisites
To be able to interface with the measurement setup using the provided drivers, make sure
your laptop has:
• A copy of the driver code. Clone the GitHub repository locally or download the zip
file from the website.
• A Python environment of your choice. Jupyter notebooks are recommended, as you
can write your lab notes in them as well.
• A VISA driver, either NI-VISA or the pyvisa−py package
• The following python packages (also included in a requirements.txt file in the provided
code):
– pyvisa – interfacing with instruments
– pyvisa−py – standalone VISA driver, strongly recommended for Linux
– numpy – math
11
Pulse Sequence Generator 12
– pandas – tabular data
– pyserial – serial communication
– matplotlib – plotting
– tqdm – progress bars
2 Pulse Sequence Generator
The heart of the setup is the pulse generator. It is responsible for generating the modulation
signal for the laser and microwave excitation, as well as providing the reference clock for
the lock-in amplifier. This enables the use of stroboscopic techniques and makes the timeresolved probing of the system possible.
The device itself is a cheap, off-the-shelf Raspberry Pi Pico 2 microcontroller. The
custom firmware makes use of the PIO (programmable input/output) coprocessors of the
RP2350 chip (for which the Pico 2 serves as a carrier board) to generate synchronized pulses
on up to 5 channels with a precision of 1 CPU cycle. In case of the slightly overclocked
devices included in the setup, this corresponds to a temporal resolution of 5 ns. Due to
how the PIO units obtain data and generate the pulses, the shortest pulse is 4 cycles long.
Note that the device will automatically round everything up to 4 and down to the nearest
integer number of cycles, but does so silently. Make sure you do not send invalid durations,
as this will cause a discrepancy between what you requested and the the impulse sequence
that was actually generated.
The PicoPulse class is provided in Device.PicoPulse for ease of use. Most importantly, the sendSequence method takes a pandas DataFrame with columns time and ch1
to ch5, decodes it and uploads it to the device. If no keyword arguments are supplied,
the time is interpreted in nanoseconds and the sequence will be repeated indefinitely. On
the control board, ch1 corresponds to the lock-in reference, ch2 to the quadrature and ch3
to in-phase channel of the modulator, and ch4 to the laser’s modulation (ch5 is unused).
If you pass a pin definition dictionary to the PicoPulse constructor you can also use the
defined names instead of the channels. For example, to produce a 1 MHz square wave
on the lock-in output (ch1) and a 2 MHz square wave on the laser output (ch4), use the
following code:
import pandas as pd
import pyvisa
from Devices. PicoPulse import PicoPulse
pico_pins = {
’lockin’: ’ch1’,
’Q’: ’ch2’,
’I’: ’ch3’,
’laser’: ’ch4’
}
seq = pd. DataFrame (
columns = [’time’, ’lockin’, ’laser’],
data = [
[250 , 0, 0],
[250 , 0, 1],
Lock-in Amplifier 13
[250 , 1, 0],
[250 , 1, 1]
]
)
rm = pyvisa. ResourceManager ()
pico = PicoPulse (rm , ’ASRL3::INSTR’, pico_pins )
pico. sendSequence (seq)
rm.close ()
To help with constructing pulse sequences, Utilities.SequenceVisualizer contains two
helpful function. visSeqProportional(seq) draws the sequence as a function of time,
while visSeqEquidistant(seq) will stretch everything to be the same width, but add
duration labels.
3 Lock-in Amplifier
The SR830M class from Devices.LockIn provides functions for interfacing with the lock-in
amplifier at a high level. Notably, the snapshot method takes a list of up to 6 strings
with the desired channel names and returns the aptured values. The multiRead method
helps capture a time series using the internal sampling capabilities of the lock-in amplifier.
This is especially useful for taking multiple readings from the same experiment in order to
take an average and to calculate noise. Note that the device can only store the currently
displayed metric, so exactly two channels are available with the options listed under the
corresponding display (i.e. X-Y is possible, but X-R isn’t, as they’re on the same display).
Most front panel settings also have corresponding methods, exhaustive documentation of
which can be found in the source file. The following code demonstrates how to read data
from the device using the library:
from Devices.LockIn import SR830M
rm = pyvisa. ResourceManager ()
lockin = SR830M(rm , ’GPIB0::8::INSTR’)
# Read s i n g l e v a l u e s
x, y, r, theta = lockin.snapshot ([’x’, ’y’, ’r’, ’theta’])
reference , aux1 = lockin.snapshot ([’ref’, ’aux1’])
# Sample X and Y f o r 8 sec on d s w i t h an a u t om a t ic sample r a t e
# ( c a l c u l a t e d from t ime c o n s t a n t )
xs , ys = lockin. multiRead (’x’, ’y’, 8)
# Sample AUX4 f o r 10 sec on d s a t 4 Hz
# S e t t i n g c h annel 1 t o None s p e e d s up r e a d o u t
_, aux4s = lockin. multiRead (None , ’aux4’, 10, 4)
rm.close ()
Microwave Source 14
4 Microwave Source
The device class KuhnePLL is included in Devices.LO, with the only notable method being
setGHz(val). The microwave cannot be disabled from the oscillator itself, and as such the
quadrature modulator must be used to block it if you do not wish to use it. This device
uses raw serial communication instead of VISA for communication, so the destructor must
be called properly after the device is no longer needed. Instantiating the device without
first destructing the previous instance will result in a permission error, which can be cleared
by power cycling the device. A working example can be seen below:
from device.LO import KuhnePLL
osc = KuhnePLL(’COM4’)
osc.setGHz (2.87)
del osc
# or
osc = None
IV Measurement Tasks
Warning. This experiment involves the use of a class IIIb laser diode with 100 mW
peak power. Direct or reflected beams will cause permanent eye damage. Diffuse
reflections can cause pain and should only be viewed for short periods of time.
Mandatory safety precautions:
• Do not look into the direct or reflected beam.
• Remove reflective accessories (e.g. rings, bracelets and watches) before adjusting
the setup.
• Keep your head above the optical plane at all times.
• Do not adjust the laser’s power supply. Laser diodes are nonlinear components,
so even a small increase in voltage may result in dangerously high brightness
and a burnt out diode.
• If unsure, consult the lab supervisor.
Warning. This experiment uses high power microwave radiation (up to 10 W). Improper use may result in bodily harm and the destruction of equipment.
Mandatory safety precautions:
• Microwaves should always be absorbed by 50 Ω terminations. Standard terminations are sufficient on their own for low powers, but use them in conjunction
with a high power attenuator for anything after the amplifier.
• Always unpower the amplifier before modifying the connections. High power
reflections will damage the amplifier.
• Avoid exposure to microwave radiation. Do not touch the coplanar waveguide
during operation.
Warning. The photodiode’s output must be terminated with 50 Ω. The lock-in amplifier has a high input impedance, so a parallel termination is required. Remove the
parallel termination when connecting the photodiode to a device which already has
a 50 Ω input impedance, as a double-termination may result in unacceptably high
current through the system.
15
Continuous Wave Experiments 16
1 Preparation
Task 1. Assemble and verify the setup.
Remark. The lab instructor may have prepared
this for you in advance.
In that case, simply check
that everything is connected as it should be.
Connect the laser to the control board using the 2 pole connector. Attach the BNC output
of the control board to the reference input of the lock-in amplifier. Connect the photodiode
to the lock-in’s input with a BNC cable. Power up the control board by plugging a 9V
power supply into the barrel jack.
Set the lab power supply to 12 V and 0.15 A on both channels. Connect the positive output
of CH1 and the negative output of CH2 to the ground potential using the included cable.
The green banana jack should be connected to the ground potential, the black one to the
negative output of CH1 (-12 V) and the red one to the positive output of CH2 (12 V). Ask
for the supervisor’s approval before enabling the outputs!
Figure IV.1.1. Correct settings
and wiring for the photodiode’s
power supply. Your exact power
supply may be different, but the
same principle applies in all cases.
Connect the AUX output of the oscillator (found on the microwave assembly) to the one
of the differential LO inputs of the quadrature modulator, while terminating the other
one with 50 Ω. For now, connect the output of the quadrature modulator directly to
the coplanar waveguide, skipping the amplifier (for CW measurements a lower microwave
power is desired). Make sure the other port of the waveguide is connected to a high power
attenuator and then a 50 Ω termination.
Task 2. Adjust the setup to maximize the photoluminescence signal.
Connect to the control board and enable the laser with the help of the example code in
notebook.ipynb. Use one of the Aux In ports of the lock-in amplifier as a voltmeter.
Hint for the Lab Notes. Make sure to note your achieved signal levels. This will be
useful later on as a point of reference.
2 Continuous Wave Experiments
Task 3. Implement CW sequence and optimize for lock-in signal.
Remark. Feel free to ask
the lab instructor for hints
on how to construct the
measurement code. If
needed, the reference code
is available for use, although this will reduce
the maximum score you
can achieve on the lab
notes, as the code is taken
into account when grading.
Ensure that the detector’s output is connected to the main input of the lock-in on the
front panel. Implement the pulse sequence (see Pulse Sequence Generator). We’re only
interested in the absolute change in signal caused by the microwave excitation, so it is
recommended to use the R − Θ mode of the lock-in. Adjust the sample stage to get the
best lock-in signal.
Hint for the Lab Notes. Compare your ODMR signal level to the photoluminescence
signal.
Hint for the Lab Report. Did you need to to move the focus spot on the diamond to
get a better signal? If yes, why are the photoluminescence and ODMR signal maxima
at different locations?
Task 4. Sweep the microwave spectrum and record the ODMR signal in zero magnetic
field.
Continuous Wave Experiments 17
Figure IV.2.1. CW pulse sequence scheme.
Using the previously constructed sequence, repeat the measurement with different microwave frequencies. Measuring between 2.85 GHz and 2.9 GHz is a good start. Refine the
range and produce a spectrum with at least 100 points.
Hint for the Lab Notes. How many peaks do you see? Which transitions do they
correspond to?
Hint for the Lab Report. Extract the zero filed splitting parameters D and E. D
corresponds to the average frequency, while E is half the distance between the peaks.
Task 5. Sweep the microwave spectrum and record the ODMR signal with an arbitrary
magnetic field.
Repeat the previous measurement with a magnet placed near the sample. For optimal
results, ensure that the magnetic field is not parallel to any of the possible NV center
orientations (the face of the sample is normal to the [111] direction). Note that you will
need to greatly increase your frequency range; 2.6 GHz to 3.1 GHz is a good start.
Hint for the Lab Notes. How many peaks do you see? Note that there are 4 possible
orientations for an NV center in the lattice, and they are all present in equal numbers
in most samples.
Hint for the Lab Report. Explain why you see the number of peaks that you do.
Remark. The spectrum may be a bit “wobbly”, this is expected and completely fine.
The microwave oscillator in the setup was designed to power a radio beacon, not to
serve as a scientific instrument, and as such the output power is not stabilized. As
the frequency is varied the power will fluctuate by an order of magnitude. This is
somewhat compensated by the quadrature modulator, but is still very noticeable in
the resulting spectrum.
Rabi Oscillation 18
3 Rabi Oscillation
Task 6. Measure Rabi oscillations.
Warning. This measurement makes use of a microwave amplifier. This device can
produce up to 10 W of radiation and should be handled accordingly. The included
attenuator is not rated to continuously absorb this power, so care must be taken to
keep the microwave’s duty cycle below 10% when the amplifier is enabled.
Ask for the supervisor’s approval before enabling the amplifier!
Remark. Averaging may
be useful for this measurement. Functions are
provided in the chapter
Lock-in Amplifier to
automatically perform repeated measurements on
the lock-in. The resulting
data series can be used to
calculate the mean signal
and its standard error.
Connect the amplifier between the output of the quadrature modulator and the coplanar
waveguide to produce a higher B1 field and thus faster oscillations. With the external
magnetic field still present, tune into a prominent resonance peak.
Implement the pulse sequence. Choose the value of tpad such that τ + tpad ≪ T1 ≈ 1 ms
and τ + tpad = const. for all values of τ . Experience shows that the highest value of τ that
provides any insight is 2 µs, and the laser should be on for around 40 µs.
If time permits, insert attenuators between the modulator and amplifier to reduce output
power and repeat the measurement.
Figure IV.3.1. Rabi pulse sequence scheme. When varying τ , make sure the total length of the
sequence remains constant by also adjusting tpad. Each half of the sequence has been repeated
twice here, but it’s recommended to repeat it 10-100 times for best effect.
Hint for the Lab Notes. Plot the signal as a function of microwave excitation time.
What do you see? If you repeated the measurement with different powers, what did
it change?
Hint for the Lab Report. Extract the Rabi frequency from the measurements. Experience shows that the textbook formula is a bad fit, so it needs to be modified.
T1 Relaxation 19
A linear term is added to account for microwave heating. The exponential envelope
is replaced with a stretched exponential with empirical parameter β to account for
inhomogeneity.
VR(τ ) = Ae−(τ/T eff
2
)
β
sin (ωRabiτ + ϕ) + Bτ + C (IV.3.1)
Hint for the Lab Report. If you repeated the measurement with different microwave
powers, compute the Rabi frequency for all measurements. Is there a correlation
between power and frequency? Does this support the claim that you were measuring
Rabi oscillations and not some unrelated phenomenon?
4 T1 Relaxation
Task 7. Measure T1 relaxation.
Implement the T1 pulse sequence. Choose the value of tpad such that τ ≪ tpad and
τ + tpad = const. for all values of τ . Test values of τ between 20 ns and 3 ms. tinit = 50 µs,
tread = 10 µs and τ + tpad = 10ms.
Figure IV.4.1. T1 pulse sequence scheme.
Hint for the Lab Notes. Note how long your initialization and readout pulses were.
Plot the signal level as a function of τ .
Hint for the Lab Report. Recover the T1 characteristic time by fitting the signal with
the following model:
VR(τ ) = Ae−τ/T1 + C (IV.4.1)
T1 Relaxation 20
Hint for the Lab Report. Determine the contrast between the signal level of the polarized and relaxed states. For reference, the best contrast achieved on the prototype
measurement setup corresponded to a 13 % increase in lock-in signal when the system
was in an initialized state compared to the equilibrium.
REFERENCES REFERENCES 21
Contribution
The measurement device was developed by Bence Göblyös based on a setup described in
literature [6] under the supervision of Prof. Ferenc Simon and Robin Kucsera. The lab
instructions were written by Robin Kucsera and Bence Göblyös. Samples were provided
by Dr. Sándor Kollarics.
This lab exercise was developed with funding and consultation from Faulhorn Zrt.
Please contact Bence Göblyös at bence@goblyos.dev if you have any questions regarding
the experimental setup or the driver code.
References
[1] David P DiVincenzo. Topics in quantum computers. NATO ASI Series E Applied
Sciences-Advanced Study Institute, 345:657, 1997.
[2] A. Gali. Ab initio theory of the nitrogen-vacancy center in diamond. Nanophotonics,
8(11):1907–1943, 2019.
[3] Victor Marcel Acosta. Optical magnetometry with nitrogen-vacancy centers in diamond. Phd
thesis, University of California, Berkeley, 2011.
[4] Sándor Kollarics. Magneto-optical spectroscopy on qubit candidate solid state systems. PhD
thesis, Budapesti Műszaki és Gazdaságtudományi Egyetem, 2023.
[5] Dieter Suter. Optical detection of magnetic resonance. Magnetic Resonance Discussions,
2020:1–47, 2020.
[6] Vikas K. Sewani, Hyma H. Vallabhapurapu, Yang Yang, Hannes R. Firgau, Chris
Adambukulam, Brett C. Johnson, Jarryd J. Pla, and Arne Laucht. Coherent control of nvcenters in diamond in a quantum teaching lab. American Journal of Physics,
88(12):1156–1169, 12 2020.