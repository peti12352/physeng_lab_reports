Measurement ...: Si wafer testing
Measurement Exercise for Physicist-Engineer Students
Abstract. Charge carrier recombination lifetime is one of the most important electri-
cal parameters for semiconductor materials, especially in photovoltaic applications.
The bulk recombination rate within a silicon wafer is determined by the initial crystal
quality and the density of defects and impurities. Therefore, accurate measurement
of the recombination lifetime provides valuable information about the crystal’s purity.
In industrial production, recombination lifetime measurement is a standard method
for quality control. This measurement practice consists of two parts. First, the iron
concentration in a silicon wafer (suitable for semiconductor industry use) is deter-
mined by performing recombination lifetime measurements in different sample states.
Second, the effect of charge carrier diffusion processes on recombination lifetime is
investigated in silicon wafers used for solar cells.
Warning. The measurement systems used during the practice contain high intensity
light sources, flash lamp and lasers. These sources can emit visible and invisible light
that may be harmful to human eyes. During normal operation there is no risk of
exposure to laser radiation.
The WT-2000 and WT-1200IL systems are designed to be completely safe when op-
erated and maintained by properly trained personnel using procedures described by
Semilab. For a more detailed overview of safety precautions, please refer to the at-
tached device manuals and their Safety Precautions section.
During the measurements, always look out for your own and other people’s safety.
If you are not sure about something, feel free to ask for help from the responsible
professors and assistants present the laboratory and always respect their warnings.
1

Recombination in silicon 2

I
Theoretical summary
1 Recombination in silicon
The recombination lifetime is one of the most important physical parameters of a semicon-
ductor material, as it may provide information about the presence of harmful defects and
contaminants. Even in dark thermal equilibrium, charge carriers are continuously gener-
ated by thermal excitation and recombine with each other through various processes. If
excess electron-hole pairs are generated in the semiconductor instantaneously, the recom-
bination rate increases, and the decay of the charge carrier density can be characterized by
the recombination lifetime. In more general terms, the recombination lifetime is defined
as:
τ =
∆ n
R

(I.1.1)
where∆ n is the excess minority carrier concentration or as it is called in solar cell termi-
nology: injection level, and R is the recombination rate.
The charge carrier diffusion length refers to the average distance that a charge carrier
can diffuse within a semiconductor material before recombination occurs. It is closely
related to recombination lifetime:
L D=

√
D · τ, (I.1.2)
where D is the diffusion coefficient of the minority charge carriers.

1.1 Recombination processes
The rate of most recombination processes depends on the charge carrier density. The exact
dependence ( R (∆ n )) is determined by the number of charge carriers involved in a single
recombination event. The three major recombination mechanisms are summarized and
illustrated in Figure I.1.1. The type of a recombination event relates to the mechanism
how the band gap equivalent energy is emitted during the recombination event.

Figure I.1.1. The main charge carrier recombination processes in semiconductors. A) Radiative
recombination, B) the Auger process, C) the Shockley-Read-Hall mechanism [1].

Typically, the different recombination processes occur simultaneously. In this case, the
total recombination rate is the sum of individual contributions:

Rtotal = Rrad + RAuger + RSRH (I.1.3)
Recombination in silicon Surface recombination 3

Then the effective carrier lifetime, τeff , can be expressed by

1
τeff =
1
τrad +
1
τAuger +
1
τSRH (I.1.4)
In silicon samples for solar cells, the dominant recombination processes are typically defect
related Shockley–Read–Hall (SRH) at low injection levels and Auger recombination at high
injection levels as depicted in Figure I.1.2 with τeff = τbulk as only bulk recombination
processes were considered.

Figure I.1.2. The bulk recombination lifetime is dominated by different recombination mecha-
nisms at low and high injection levels [2].

1.2 Surface recombination
Surface recombination refers to the process in which charge carriers (electrons and holes)
recombine at the surface or interface of a semiconductor material, rather than in the bulk.
This phenomenon is particularly important in semiconductor devices, such as solar cells,
since their thickness is smaller than the diffusion length. Therefore, surfaces often sig-
nificantly influence the overall device performance. The large variety of dangling bonds
on the surface and other structural imperfections manifest in surface states, which have
energy levels located within the band gap of the semiconductor. Therefore, their recombi-
nation properties can be described with the Shockley-Read-Hall model as well. However,
instead of one discrete energy level, there is a spectrum of energy states at the surface. The
practical approach to mathematically handle the surface recombination phenomenon in a
universal way applies the parameter called surface recombination velocity S. Its definition
is similar to the carrier lifetime integrating all recombination events corresponding to the
surface:
S =
Rsurf
∆ nsurf (I.1.5)

where∆ nsurf is the surface excess carrier density and Rsurf is the recombination rate on
the surface. S has dimensions of m/s (the majority of the literature uses cm/s), which
stems from the fact that Rsurf is a surface quantity with dimensions of m−^2 s−^1.
For the measurement of thin wafers with thickness W < L D, a surface recombination
lifetime, τ surfcan be defined:

Recombination lifetime measurement principles 4

τ surf≈
W
2 S

- W^2
  π^2 D
  . (I.1.6)
  where W is the thickness of the wafer and D is the diffusion coefficient.

In two limiting cases, the expression can be further simplified. First, in the case
of passivated surface, which reduces the surface recombination velocity. Passivating the
surface involves coating the sample with materials (such as silicon dioxide, silicon nitride,
or organic layers) that reduce the density of surface states, thereby lowering the surface
recombination velocity.

τ surf( S −→0) =
W
2 S
. (I.1.7)
While in the opposite case ( S −→∞):

τ surf( S −→∞) =
W^2
π^2 D
. (I.1.8)
This is the so-called diffusion-limited case, typically observed in as-cut or polished surfaces,
when the surface recombination is limited by the minority carrier diffusion process.

This expression enables us to categorize recombination processes according to the lo-
cation where they occur:
1
τeff

=
1
τbulk

- 1
  τsurf
  . (I.1.9)
  2 Recombination lifetime measurement principles
  Recombination lifetime is a local property of the silicon crystal. However, due to the
  movement of charge carriers, its effect on devices is not localized to where the recombina-
  tion occurs. During carrier lifetime characterization, an apparent effective carrier lifetime
  ( τeff ) is measured, which in some cases provides direct information regarding the electrical
  performance of the final device (e.g. measurement on solar cell structures before metalliza-
  tion). In other cases, the measurement procedure must be adjusted or additional sample
  treatments have to be applied to obtain the information of interest. Such treatment is the
  surface passivation of the sample in order to obtain the carrier lifetime within the wafer.

To evaluate and understand the recombination dynamics in silicon materials and de-
vices, several experimental techniques have been developed. They are essential for opti-
mizing the material quality and the device performance, especially for photovoltaic appli-
cations. Technically, any carrier lifetime characterization technique is based on the same
phenomenon: the injection of excess charge carriers, and the monitoring of their actual
density∆ n. To simplify the discussion, the average of the carrier density in the depth

is taken, so∆ naverage ( t ) =

∫ W
0 ∆ n ( x,t ) dx
W. Using the formulas for τeff in Equation I.1.9,
the impact of surface recombination and diffusion process can be handled mathematically
using a single τeff value. Therefore, we get a simple approximate formula for∆ nav ( t ):

∂ ∆ nav ( t )
∂t
= G − R (∆ nav ( t )) = G −
∆ nav ( t )
τeff (∆ n )
(I.2.1)
where G is the generation rate of the optical injection and R (∆ n )is the total recombination
rate of the carriers. Rearranging this equation, the general expression of the carrier lifetime

Recombination lifetime measurement principles μPCD measurement 5

measurement can be determined:

τeff (∆ nav ) =
∆ nav
G − ∂ ∆ ∂tnav
. (I.2.2)
From this point, to simplify the equations,∆ n := ∆ nav always refers to the average
injection level, while if the local carrier density needs to be applied, it will be indicated as
∆ n ( x ).
There are two main methods to measure the charge carrier lifetime. The steady state
(SS) and the transient method, which is realized using the photoconductance decay (PCD)
technique in practice.
In the SS method, the charge carriers are excited optically – with laser in our case

until the injection level reaches the steady state. In the steady state case ∂∂t ∆ n = 0,
therefore, equation I.2.2 simplifies as:
τ (∆ n ) =∆ n
G
(I.2.3)
The PCD method starts with a laser – or other optical – excitation. After instanta-
neously switching off the excitation laser, injection level and the measured signal relaxes
back to the equilibrium state. During the decay, the excitation is zero ( G = 0) and the
lifetime can be determined in the function of∆ n :

τ (∆ n ) =− ∂ ∆∆ nn
∂t
(I.2.4)
2.1 μ PCD measurement
The microwave induced photoconductance decay ( μ PCD) method is the most common way
of measuring minority carrier lifetime in semiconductors. This method excels due to its
reliability, good reproducibility, and the short measurement time that permits recording
lifetime maps with high resolution.
The pulse of an infrared semiconductor laser generates free electron-hole pairs under
the illuminated area on the sample (Figure I.2.1). Since the penetration depth of the 904
nm wavelength light is about 30μm in silicon, the free carriers are generated close to the
front surface of the sample.

Figure I.2.1. Laser excitation
Since the free electrons and holes recombine, their concentration and so the conduc-
Recombination lifetime measurement principles μPCD measurement 6

tivity of the sample decreases after the excitation. The decaying conductivity can be
monitored by detecting the microwave reflectivity, because the reflected microwave power
depends on the conductivity of the sample (Figure I.2.2). It is measured as a function of
time.

Figure I.2.2. Detection by microwave
The ring-shaped microwave antenna is operated near to its resonance frequency, in the
range of 10.0 GHz – 10.5 GHz. The sample and the antenna above it, compose a resonator,
that’s resonance curve can be seen on Figure I.2.3, red line. As the conductivity of the
sample increases due to the excess carriers generated by the illumination, the resonance
curve shifts and gets deformed (Figure I.2.3, blue line). As the excess carriers recombine,
the conductivity of the sample returns to equilibrium, and the resonance curve gets back
to its original state. During measurement, the microwave frequency is set to a predefined
frequency (vertical, green, broken line on Figure I.2.3). As the curve gets back to the
original state, the measured signal of the antenna changes.

Figure I.2.3. Resonance curves of the microwave probe with a sample underneath. When the
sample is in equilibrium, the curve is the red line. When the sample is injected, excess carriers are
generated by the illumination, the conductivity and reflectance is changed, the curve is the blue
line. The vertical green line shows the frequency used during the measurement, which is tuned so
that the change of the signal is maximal.

For this technique, the measured signal is assumed to be proportional to the number
of excess carriers, and the recombination rate is assumed to be constant. Therefore, the
recombination time is determined by fitting an exponential decay function to the recorded

Recombination lifetime measurement principles Iron contamination measurement 7

decaying signal. (Figure I.2.4):

∆ n = const ·exp(− t/τeff ) (I.2.5)
Figure I.2.4. Transient, measured on a sample. As the carriers return to equilibrium exponen-
tially, the signal changes accordingly.

The μ PCD measurement technique will be used in the WT-2000 system, which is
capable to perform high resolution carrier lifetime maps.

2.2 Iron contamination measurement
The most often detected contaminant in silicon is iron. In p-type silicon iron is present as
an iron-boron (Fe-B) pair. This pair is a very effective recombination center. The Fe-B pair
dissociates to interstitial iron (Fei) and boron after heat treatment (200◦C for 10 minutes
with fast quenching after the treatment) or upon high-intensity illumination. This unique
behavior enables its identification because the recombination efficiency of the Fe-B pair and
that of the Fe i is different. At high injection level, which is used in the μ PCD technique, the
Fe-B pair causes lower lifetime than the Fe i , so during the dissociation process, the lifetime
increases. This can be recorded by in situ lifetime measurement (see Figure I.2.5). Once
iron is separated from boron an association process takes place even at room temperature
which results in decreasing lifetime. Its time constant can be some hours or days depending
on the boron concentration (i.e. the resistivity) of the wafer under test.
Figure I.2.5 shows a typical sequence. The sample was illuminated with fast repeated
laser pulses to break the Fe-B pairs. After switching the laser on, the lifetime increases
quickly at the beginning then more slowly to a saturation value. After switching the illu-
mination off, the interstitial iron again forms a pair with boron, and the lifetime decreases
with a given time constant to the original value. The Fe concentration can be calculated
from the lifetime measured before and after the dissociation with the following formula:

NFe = CμPCD
(
1
τbefore
−
1
τafter
)
(I.2.6)
where CμPCD [ μ s/cm^3 ]is the iron constant. The association kinetics of Fe-B pairs is given
by [7]

R =
e^2
εε 0 kBT
NBD 0 exp
(
−
Emig
kBT
)
, (I.2.7)
Recombination lifetime measurement principles ePCD measurement 8

Figure I.2.5. Fe-B dissociation and association over time
where ε is the dielectric constant of silicon, e is the unit charge, kB is the Boltzmann’s
constant, T is the absolute temperature, NB is the concentration of boron, D 0 is the iron
diffusion constant and Emig = 0*.* 64 ± 0*.* 01 eV [8] is the activation energy of Fe + i migration.

2.3 ePCD measurement
The eddy-current based Photoconductance Decay (ePCD) measurement is developed for
investigating thick silicon samples. For this purpose, a longer wavelength infrared laser is
used with deeper photogeneration. It also applies light pulses to generate free electron-hole
pairs deep in the bulk under the illuminated area on the sample (Figure I.2.6/a).

Figure I.2.6. The operating principle of eddy current measurements.
For the accurate detection of the deeply generated charge carriers, the eddy-current
technique is used (Figure I.2.6/b). This is based on the interaction between an alternating
magnetic field and free charges (electrons or holes) in a conductive material. An oscillating
magnetic field near the material surface induces circulating currents (eddy currents) within
the material. These currents generate their own magnetic fields, which oppose the original
magnetic field according to Lenz’s law. The magnitude of eddy currents and their interac-

Recombination lifetime measurement principles Evaluation of ePCD curves 9

tion with the magnetic field is influenced by the electrical conductivity (or resistivity) of
the material as well as its thickness and other electromagnetic properties.

In Semilab systems, an alternating current (AC) is passed through a coil placed near
the sample, and the response of the eddy currents is measured through changes in the
impedance of the coil. The depth at which the electromagnetic field penetrates and induces
eddy currents depends on the skin depth, determined by the electrical resistivity of the
material and the frequency of the applied magnetic field:

δ =
√
2 ρ
μω
, (I.2.8)
where ρ is the resistivity of the material, μ is the permeability (for silicon, it is almost
equal to vacuum permeability), and ω is the angular frequency of the applied field. The
resistivity of silicon typically used in solar cell applications (≈1 Ωcm) results in a skin
depth of around 1 cm, which implies that the entire depth of thin wafers ( W < 200 μ cm)
can be properly sensed, while it is questionable for thick samples, ingots.

2.4 Evaluation of ePCD curves
While certain applications, such as rapid silicon wafer mapping, may utilize a simplified
approach of extracting a single lifetime value through exponential function fitting, more
sophisticated analyses of recombination properties necessitate the determination of the
excess-carrier-concentration-dependent recombination lifetime function, τ (∆ n ).
The importance of obtaining the τ (∆ n )function is particularly pronounced when ex-
amining exotic sample types, where recombination lifetime can exhibit order-of-magnitude
variations during decay, primarily due to charge carrier trapping phenomena. This func-
tion provides crucial insights into the complex recombination dynamics occurring within
the material.

The objective of this evaluation procedure is to derive the τ (∆ n )function from the
observed decay curve. In the standard PCD measurement protocol, multiple sequential ex-
citation pulses are typically employed to enhance measurement accuracy. The subsequent
signal decay curves are averaged, resulting in a significant improvement in the signal-to-
noise ratio. The number of averages is typically optimized based on the measured carrier
lifetime and the signal magnitude to balance the measurement time and the accuracy. The
equilibrium state signal is recorded prior to excitation as it provides the conductivity and
doping level.

The determination of carrier lifetime necessitates the numerical differentiation of the
decay curve. With regard of the sensitivity of numerical differentiation to noise, the elimi-
nation of external disturbances is crucial for an accurate evaluation (e.q. blue triangles in
Figure I.2.7a.).

The subsequent phase in the evaluation process involves the computation of excess
charge carrier concentration (∆ n ) decay from the averaged signals as it is presented in
Figure I.2.7b. For eddy current measurement techniques, the measured signal can be easily
calibrated to the sheet conductance ( σ s) of silicon wafers. To avoid the inaccuracies, cali-
bration wafers of similar thickness to the sample under investigation need to be employed.

The standard formula to calculate the density of excess carriers from the sheet con-
Figure I.2.7. a) measured signal during an ePCD measurement, b)∆ n ( t )curve of the decay, c)
τ ( t )curve of the decay, d) τ (∆ n )lifetime curve of the ePCD measurement.

ductance is:
∆ n = ∆ σ s
W · e · μ sum(∆ n,N dop)

, (I.2.9)
where e is the electron charge,∆ σs is the excess sheet conductance, and μ sum= μ e+ μ his
the sum of electron and hole mobilities.

The charge carrier mobility is not a constant parameter but rather a function of the
dopant atom concentration and the excess charge carrier density. Consequently, an iterative
calculation is used to accurately determine∆ n. The mobility shift of dopant-related free
carriers also contributes to the observed conductance in the injected case. Considering this
effect, the expression for∆ n is modified as follows:

∆ n =
σs/W − N dop· e · μ maj( N dop , ∆ n )
e · μ sum( N dop , ∆ n )
, (I.2.10)
where N dopis the doping concentration and μ majis the mobility of majority charge carriers.

Numerous theoretical and empirical models are available to determine the mobility of
electrons and holes in silicon. Among these, Klaassen’s semi-empirical model is used, which
not only accounts for carrier concentration but also incorporates temperature dependence,
providing a more accurate representation of charge carrier mobility across a wide range of
operating conditions. For the sake of ease, a data sheet is provided with the corresponding
mobility.

The concluding phase of the evaluation process involves the numerical differentiation of
the∆ n ( t )curve, followed by the computation of the recombination lifetime corresponding
to each data point based on Equation I.2.4 (Figure I.2.7c and d).

10

11
II
Measurement tools
WT-
The WT-2000 system is a platform that can be equipped with a variety of measuring
options. This allows characterization of silicon wafers in diverse ways. It is a useful tool
for incoming wafer inspection, quality control and process monitoring in the wafer and IC
manufacturing processes. In this measurement exercise the prepared measurement option
is the μ PCD. The system contains the below mentioned parts:

WT-2000 main unit with scanning capability
Sample stage
Indexer for automatic wafer handling from a wafer cassette
Two computers, including a Measuring computer (System 1, DOS) and a User com-
puter (System2, Windows)
Peripherals including keyboard, mouse, LCD monitor
μ PCD head for lifetime and Fe concentration measurements
Flash unit for whole wafer, providing high intensity illumination (for Fe measurement)
Figure II.2.8. Semilab WT-2000 charge carrier lifetime mapping tool.
WT-1200IL
The WT-1200IL is a single-point non-contact carrier lifetime measuring device capable of
monitoring defects and contamination both in the bulk and in the surface region of silicon
ingots. It is primarily optimized for the investigation and quality control of ingots, but can
also be used with wafers and solar cells.

Measurement tasks 12

Laser unit box with measuring head
Industrial PC (Windows operation system)
Peripherals (keyboard, mouse, LCD monitor)
μ PCD cable
Serial cable
Power cable
Main cord for industrial PC
Main cord for laser control box
Main cord for monitor
Figure II.2.9. WT-1200IL hand-held recombination lifetime measurement tool
This device is capable to perform both ePCD and SS measurements on wafers and ingots.

3 Measurement tasks
3.1 Measurement of the dynamics of iron contamination in silicon
3.1.1 Investigation of the association of Fe-B pairs

The iron concentration is proportional to the difference of reciprocal recombination lifetime
between the FeB and Feistates (eq. I.2.6). In this first task, determine the proportionality
factor (iron constant) on a sample with known [Fe] (B2).

Task 1. Load the measurable wafer (B2) into the WT-2000 system and run a mapping
measurement. Use the "Autosetting" function to set suitable measuring parameters
and save the results. Use 2mm measurement raster. Use these settings when further
examining this sample.
Task 2. Perform light flashes on the wafer to completely dissociate the FeB pairs.
Check the lifetime value in a single point after each flash session to ensure its satura-
tion.
Task 3. Repeat the mapping measurement on the sample. How did the charge carrier
lifetime change during the flashes? Calculate the iron constant of the system.
Measurement tasks Injection level dependent lifetime determination 13

3.1.2 Investigation of Fe-B dissociation

Task 4. Load the measurable wafer (No.3) in the WT-2000 system, and repeat the
iron concentration measurement used on the previous sample. Determine the iron
concentration using the previously measured iron constant.
3.1.3 Determination of iron diffusion constant

Task 5. Load the first sample back into the system and perform lifetime mapping
every 10 minutes. Determine the D 0 iron dissociation constant (Equation I.2.7) from
the relaxation of τ ( t ).
Hint for the Lab Notes. Let us assume that the dissociation of FeB pairs is negligible
and ∂ [ FeB∂t ]= R ·([ Fe ] total −[ FeB ]).
3.2 Injection level dependent lifetime determination
3.2.1 Calibration tasks

In the following tasks you have to calibrate the eddy signal and the light intensity, which
are the basics of the accurate ePCD measurement and evaluation.

Task 6. Measure the signal of the calibration wafers with known resistivity. The
parameters of the calibration set can be found in the data sheet. Create the V eddy σ sh
function and fit the data points with a polynomial function.
Task 7. Repeat the previous task with thick silicon slugs. Calculate the apparent
sheet conductance using the wafer calibration σ sh,app. Define the sensitivity depth as
follows:
d sense= ρσ sh,app , (II.3.1)
where ρ is the sample resistivity, given in the data sheet. Create the V eddy d sense
function and fit it with a suitable function.
Task 8. Measure the power of the excitation laser with a THORLABS light power
measurement tool in a wide power range. Measure the diameter of the illumination
window. Calculate the photon flux of the 1064 nm laser source.
3.2.2 Comparison of steady-state and PCD measurements on wafers and ingots

Task 9. Measure the given passivated silicon wafer with the ePCD measuring head.
Use long enough pulses to achieve steady-state condition before the laser is terminated.
Calculate the τ SSvalue and the τ (∆ n )curve from the measured signal using the results
of the calibrations.
Task 10. Repeat the measurement with variable pulse energy at the same measure-
ment point. Compare the results of the different methods to each other. How the
measurement methods effect the τ (∆ n )curve in case of passivated samples?
Task 11. Repeat the previous two tasks on an unpassivated silicon slug sample. Use
d senseas the sample thickness to calculate the injection level. What have you ob-
served? Compare the results of the different methods to each other. How the surface
REFERENCES REFERENCES 14
recombination effect the τ (∆ n )curve in the different measurement methods?
3.2.3 Investigation of surface and bulk lifetime on Si ingots

Task 12. Determine the τ (∆ n )curves of ingots with varying thickness!
Task 13. Determine the τ (∆ n )curves of ingots with varying thickness. Separate the
τbulk (∆ n )and the τsurface (∆ n ).
References
[1] S. Sadhukhan, S. Acharya, T. Panda, N. C. Mandal, S. Bose, A. Nandi, G. Das, S. Maity, S.
Chakraborty, P. Chaudhuri, and H. Saha, “Chapter 4 - evolution of high efficiency passivated
emitter and rear contact (perc) solar cells,” in Sustainable Developments by Artificial
Intelligence and Machine Learning for Renewable Energies, K. Kumar, R. S. Rao, O.
Kaiwartya, M. S. Kaiser, and S. Padmanaban, Eds. Elsevier, 2022, pp. 63–129. [Online].
Available: https://www.sciencedirect.com/science/article/pii/B

[2] S. Rein, Lifetime Spectroscopy—A Method of Defect Characterization in Silicon for
Photovoltaic Applications. Springer Berlin, Heidelberg, 2005.

[3] F. Dannhäuser, “Die abhängigkeit der trägerbeweglichkeit in silizium von der konzentration
der freien ladungsträger—i,” Solid-State Electronics, vol. 15, no. 12, pp. 1371–1375, 1972.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/

[4] J. Krausse, “Die abhängigkeit der trägerbeweglichkeit in silizium von der konzentration der
freien ladungsträger—ii,” Solid-State Electronics, vol. 15, no. 12, pp. 1377–1381, 1972.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/

[5] D.B.M. Klaassen, A unified mobility model for device simulation—I. Model equations and
concentration dependence , Solid-State Electronics, 35 (1992), Pages 953-959.
https://doi.org/10.1016/0038-1101(92)90325-7.

[6] D.B.M. Klaassen, A unified mobility model for device simulation—II. Temperature
dependence of carrier mobility and lifetime. Solid-State Electronics, Volume 35, Issue 7, 1992,
Pages 961-967,https://doi.org/10.1016/0038-1101(92)90326-8.

[7] Xiaodong Zhu, Xuegong Yu, Xiaoqiang Li, Peng Wang, Deren Yang, Quantification of
characteristic parameters for the dissociation kinetics of iron–boron pairs in Czochralski
silicon, Scripta Materialia, 2011, https://doi.org/10.1016/j.scriptamat.2010.10.021.

[8] E.R. Weber, Appl. Phys. A Mater. Sci. Process. 30 (1983) 1
