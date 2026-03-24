DOI: 10.1007/s00340-002-0882-z
Appl. Phys. B 74 [Suppl.], S259–S263 (2002)
Lasers and Optics
Applied Physics B
k. varju´ 1
a.p. kovacs ´ 1
g. kurdi2
k. osvay1,✉
High-precision measurement of angular
dispersion in a CPA laser
1 Department of Optics and Quantum Electronics, University of Szeged, P.O. Box 406, Szeged 6701, Hungary
2 HAS Research Group on Laser Physics, University of Szeged, Dom t ´ er 9, Szeged 6720, Hungary ´
Received: 15 September 2001/
Revised version: 20 December 2001
Published online: 27 June 2002 • © Springer-Verlag 2002
ABSTRACT Angular dispersion is measured with the accuracy
of 0.2 µrad/nm by a new method based on spectrally resolved
interferometry. It is linear, simple and allows for real-time alignment of the stretcher-compressor system of CPA lasers.
PACS 42.60.v; 42.65.Re; 95.75.Kk
1 Introduction
In a complex optical system, such as a short pulse
chirped pulse amplification (CPA) laser [1], there are various
causes of angular dispersion. The prism pair in the oscillator may have a slightly different apex angle or, more significantly, non-parallel refractive surfaces. Slightly wedged
optical components, like the output coupler, the laser crystals,
or glass filters, also cause angular dispersion, not to mention
the non-parallelism of the gratings in the stretcher or compressor [2, 3].
One of the most crucial alignment procedures of CPA
lasers is the accurate setting of the stretcher-compressor system [2–5]. Although the effect of non-parallelism of the gratings on the phase modulation of the compressed pulse can
be partially compensated for by changing the grating separation, the residual angular dispersion results in a tilted pulse
front [6–9], and hence leads to an increased pulse duration
and reduced intensity when the beam is focused onto a target [10, 11]. Since the effect of residual angular dispersion
becomes increasingly important at shorter pulse duration,
sub-20 fs laser systems call for more accurate and in situ diagnostics than existing systems can provide [2, 11–13]. Previous techniques such as using a spatially reversed Mach–
Zender [11] and Michelson [13] interferometer, or a tilted
pulse-front autocorrelator [12], allow for measurement with
the accuracy of several µrad/nm. A further disadvantage of
the first two methods is that they require multiple-shot measurements. The method of Sacks et al. [12] is suitable for simultaneous monitoring of pulse length and angular dispersion,
but requires high intensities for the second harmonic gener-
✉ Fax: +36-62/544658, E-mail: osvay@physx.u-szeged.hu
ation, and therefore it is not sensitive enough for measuring
the stretched pulse.
In this paper, we propose a new single-shot method based
on spectrally resolved interference (SRI) [14–16] to measure
the residual angular dispersion of a laser beam. The technique
is very simple, linear and allows for high-precision real-time
monitoring of angular dispersion.
2 Theory
Let us assume two monochromatic waves
E1=E1 cos
k1 r +ϕ1

E2=E2 cos
k2 r +ϕ2
 (1)
travelling in the directions k1, k2 at a small angle ε = ε2–ε1 to
each other, and interfering on a vertical plane that is observed
along the y-axis (see Fig. 1). The interference is constructive,
when the interference term

E1 E2

∝ cosk2 −k1

r + ∆ϕ

= cos 
2π
λ
ε y + ∆ϕ

(2)
has a maximum, where ∆ϕ = ϕ2–ϕ1. In (2) small-angle approximation has been used. We define the distance between
two consecutive bright fringes as the line-separation Λ. This
definition is equivalent to
cos 
2π
λ ε (y+Λ)+ ∆ϕ

= cos 
2π
λ
ε y+ ∆ϕ

, (3)
FIGURE 1 Interference of two monochromatic waves travelling at angles
to the z-axis. The line separation Λ is determined by the angle of beams
S260 Applied Physics B – Lasers and Optics
thus the angle of the two beams and the line separation is related by
ε = λ
Λ . (4)
For a broadband beam the superposition of the interference patterns belonging to each spectral component leaves
a blurred image with poor fringe visibility [15]. However,
with the help of spectral resolution of the pattern, the two interfering beams can be regarded as a collection of independent
monochromatic waves “placed” side-by-side. As a result of
the interference of two broadband waves propagating at an
angle ε, the position of the nth intensity maximum is then
given by
y(λ) =
	
n − ∆ϕ(λ)
2π

 λ
ε . (5)
When no angular dispersion is present in the beam, this
equation describes straight lines splayed out towards the
longer wavelength side of the spectrum. The line-separation is
given as
Λ(λ) = |yn(λ)− yn−1(λ)| = λ
|ε|
. (6)
Thus, spectral resolution of the interference pattern allows for
determining the angle of two broadband beams.
To incorporate angular dispersion into the model, we
should consider a more general case. Two beams travelling at
arbitrary angles, measured from the z-axis counter-clockwise,
interfere in the x–y plane. When angular dispersion is present
in a beam, its spectral components travel in different directions, i.e. ε = ε(λ). As the wavelength-dependence is usually
small, we shall consider the Taylor expansion around the central wavelength λ0:
ε(λ) = ε2(λ)−ε1(λ)
= ε2 (λ0)−ε1 (λ0)+
ε
2 (λ0)−ε
1 (λ0)

(λ−λ0)
+

ε
2 (λ0)−ε
1 (λ0)

2 (λ−λ0)
2 +..., (7)
where ε1(λ0) and ε2(λ0) are the signed angles of the central wavelength component of each beam with the z-axis,
ε
1 (λ0), ε
2 (λ0) are the first, ε
1 (λ0), ε
2 (λ0) are the second
derivatives with respect to wavelength at the central wavelength. Equation (6) is then replaced by
λ
Λ(λ) =




ε (λ0)+ε
(λ0) (λ−λ0)+
ε (λ0)
2 (λ−λ0)
2 +...



 ,
(8)
where ε(λ) = ε2(λ)–ε1(λ).
The effect of angular dispersion on spectrally resolved interference fringes is demonstrated via numerical simulations
along (2) with (8). The interference of two beams was calculated in the spectral range 750–850 nm. As (8) determines
only the sum of the dispersions in the two beams, for simplicity we have restricted angular dispersion into beam 1 (ε
1 = 0,
ε
2 = 0 and ε
1 = ε
2 = 0).
For the case of no angular dispersion (Fig. 2a), the lines in
the pattern are virtually parallel, as expected from (5). When
angular dispersion is present in the beam, the interference
fringes are curved and become more distinctively splayed
(Fig. 2b). With angular dispersion of the opposite sign, lines
are splayed out towards the other end of the wavelength range
(Fig. 2c).
We should note here that chirp, represented by ∆ϕ(λ) in
(5), also causes a distortion of the spectrally resolved interference pattern (see [14, 16] for details), but it has no effect
on line-separation. In the simulation above, all beams had
zero chirp. On the other hand, it is important to see that
the line spacing is unaffected by the dispersion of the beam
(see (6)).
Figure 2d shows the λ

Λ(λ) functions corresponding to
the simulated SRI patterns. The plots are linear, as the beams
possess no higher-order angular dispersion. The slope of the
lines gives the value of angular dispersion.
We must add here that the sign of angular dispersion depends upon the choice of beam 1 and 2. With the interchange
of beams, angular dispersion changes sign, as expected from
(7). For determination of the sign of angular dispersion, see
Sect. 4.
FIGURE 2 Simulated SRI fringes for pulses a without angular dispersion
of b ε
1 = 10.0 µrad/nm and c ε
1 = −10.0 µrad/nm, and d the corresponding λ/Λ(λ) plot
3 Experimental
For the measurements, the spectrally resolved interferograms from a Mach–Zender interferometer were used
(see Fig. 3). Angular dispersion has been introduced into the
800-nm beam of our 72-MHz repetition rate Ti:S oscillator
by a 45◦ fused-silica prism. The 20-fs pulses with a 55-nm
bandwidth (FWHM) enter the interferometer through a beamsplitter plate, then in one arm fall onto an aluminium mirror
which ensures constant reflectivity through the spectral range
at a non-specific angle. In the other arm, by means of two mirrors at 45◦ to each other, the left and right sides of the beam are
VARJU´ et al. High-precision measurement of angular dispersion in a CPA laser S261
FIGURE 3 Experimental setup
interchanged, therefore we measure the angular dispersion of
the beam twice, since
ε1(λ) = ε1 (λ0)+ε
1 (λ0) (λ−λ0)+
ε
1 (λ0)
2 (λ−λ0)
2 +...
ε2(λ) = ε2 (λ0)−ε
1 (λ0) (λ−λ0)− ε
1 (λ0)
2 (λ−λ0)
2 +....
(9)
This arrangement also ensures that, while the mirrors are
translated along the bisector, when changing delay-time, the
output beam leaves in the same direction. The interferometer should be set with equal arm lengths with the precision of 100 fs to see any interference at all [15]; otherwise,
the change in delay has no effect on fringe spacing, therefore no effect on the result. We emphasize that this setup
also eliminates the effect of chirp on interference patterns,
as the two interfering beams have no relative chirp to each
other; therefore, the setup will work with strongly chirped
pulses.
The interference image is resolved by a home-made grating spectrograph (600 mm−1), with the entrance slit parallel to
the table, i.e. the plane in which the two sides of the beam has
been interchanged. The spectrally resolved interference pattern is recorded by a CCD camera (EDC1000-HR Electrim
Corp., 244×753 pixels). The low dynamic range of the CCD
chip (8 bits) and the 10-ms integration time slightly smoothes
the recorded pictures.
Spectrally resolved interference patterns of the same incoming beam have been recorded at different settings of the
FIGURE 5 SRI pattern
when phase fronts are parallel for certain wavelengths
(indicated by dotted lines)
FIGURE 4 SRI patterns recorded at different delay times (∆τ = 30 fs) and
tilt angles (εa,b = 0.81 mrad, εc,d = −1.02 mrad) of the interferometer mirrors. For the measurement results, see Table 1
interferometer (see Fig. 4). These settings are: ε0 = 0.84 mrad
for patterns a and b and ε0 = −1.02 mrad for c and d. The relative delay between left and right pictures is 30 fs.
One may notice the following: in the top pictures the
fringes are splayed towards the shorter wavelengths, and in the
bottom pictures towards the longer wavelengths; as expected,
the corresponding tilt angles have opposite signs. The fringes
are more frequent in the bottom pictures, as the magnitude of
the tilt angle is larger. On changing the delay time between the
two arms of the interferometer, the pattern shifts vertically, as
was indicated in [15].
4 Evaluation
4.1 Coarse method
As mentioned above, the line separation is inversely proportional to the angle of the two beams, so it
becomes infinite for parallel phase fronts. When angular dispersion is present in a beam, it may be that phase fronts are
parallel only in a certain wavelength. In this case, the spectrally resolved interference fringes become hyperbola-like
(see Fig. 5), and with a calibrated spectrograph the wavelength of parallel phase fronts can be easily determined. On
S262 Applied Physics B – Lasers and Optics
tilting the reference mirror by angle ∆α around an axis perpendicular to y, the interferogram shifts as different wavelengths satisfy the parallel phase front criteria.
We observe that the pattern originally splayed towards the
short-wavelength side changes into being splayed towards the
long-wavelength side. This is caused by the sign change of the
relative angle of the two beams. In Fig. 6 the relative tilt angle
∆α of the reference mirror is plotted against the wavelength.
As before, the slope of the function directly gives the value of
first-order angular dispersion. We note that this procedure has
a limited precision (∼ 5 µrad/nm), but yields a quick qualitative evaluation. The method is effective for angular dispersion
larger than 10 µrad/nm, up to 300 µrad/nm. The lower limit
is defined by the precision of the tilting mount: while the pattern shifts along the spectral range, the tilt of the mirror must
be determinable. The measurement also has an upper limit:
for a large angular dispersion the hyperbolas of the pattern
become too frequent to be resolved.
The sign of the angular dispersion is determined as follows: it is positive if the hyperbola-like pattern shifts toward
the longer wavelength range when the mirror is tilted counterclockwise.
FIGURE 6 Relative tilt angle of reference mirror and the corresponding
wavelength of parallel phasefronts
4.2 Fine method
With the aid of data processing using the digital image of the CCD camera, a more precise evaluation
is possible. Each vertical section of the interference image
is considered to be the result of the interference of two
monochromatic beams, producing an intensity function of
cos 
2πy

Λ(λ)
(see (2) and (6)), where y is the conjugate
coordinate to y. Thus, after normalization of an interference
pattern, a cosine function is fitted to each vertical section of
the image to obtain the line spacing function: Λ = Λ(λ) (see
Fig. 7). Then we plot the λ

(2Λ(λ)) function that gives the
wavelength-dependent angle of the beams, providing information on angular dispersion. We found, that the relatively
wide spectrum required quadratic approximation, therefore
first- and second-order angular dispersion (ε
, ε) has been
determined, i.e. in (7) and onwards, second-order Taylor expansion is used. Figure 8 shows the evaluation result of the
pattern in Fig. 4a, plotting only every 25th data point for clarity. A fairly good agreement with the quadratic fit is found.
FIGURE 7 Fine evaluation method I. step: Fitting cosine functions to each
vertical section of the normalised pattern of Fig. 4a
FIGURE 8 Fine evaluation method II. step: Quadratic fit to the the λ/Λ(λ)
data of pattern Fig. 4a
The deviation of data points from the quadratic fit is plotted on
the same figure, and is magnified by a factor of 20.
The analysis has been carried out on the patterns shown in
Fig. 4. First- and second-order angular dispersion coefficients
at 800 nm were determined, and are shown in Table 1.
On the accuracy of the measurement we note the following. The noise of the CCD camera has been found to cause
a discrepancy less than 0.01 µrad/nm, and the fitting algorithm is accurate to 0.2 µrad/nm. When the measurements
have been repeated, the standard deviation was always below
0.2 µrad/nm (see Table 1), confirming that the main limitation is due to the fitting procedure. Accuracy could be further enhanced by using a higher-resolution camera, at the
cost of a longer processing time. Experimental data shows
that second-order angular dispersion could be determined
with the accuracy of 10 nrad/nm2. We have found that the
method is effective for angular dispersion in the range of
0.2–40 µrad/nm, where the upper limit is set by the resolution
problem of the high spatial frequency of the fringes.
The accuracy already demonstrated is adequate for controlling or improving the performance of current CPA laser
systems. To illustrate this, we add a few examples of optical setups causing angular dispersion of 0.2 µrad/nm at
Fig. 4a Fig. 4b Fig. 4c Fig. 4d
ε
(µrad/nm) 11.7 11.8 12.0 11.9
ε(nrad/nm2) −32.6 −35.2 −45.2 −41.0
TABLE 1 Values of first- and second-order angular dispersion for the SRI
patterns shown in Fig. 4
VARJU´ et al. High-precision measurement of angular dispersion in a CPA laser S263
FIGURE 9 Angular dispersion caused by a prism at different angles
incidence
the central wavelength of 800 nm. A plane-parallel plate
in the laser system (glass filters, Ti:S and nonlinear crystals), with a slight non-parallelism of 13 for glass SF10,
25 for sapphire or 39 for silica, causes this amount of
angular dispersion. A pair of identical fused-silica prisms
with Brewster angle at minimum deviation in the compressor configuration leaves a residual angular dispersion
of 0.2 µrad/nm in the beam if the parallelism alignment
is off by 0.257◦. Similarly, for a stretcher of 1200 mm−1
gratings in Littrow configuration, the corresponding value
is 0.015◦.
To test our method, we have measured the angular dispersion of a 45◦ fused-silica prism as a function of angle
of incidence (Fig. 9). The data points are in good agreement
with the theoretical calculations, where the Gaussian nature
of the incident beam has also been taken into account. As is
known [17], the angular dispersion of a Gaussian beam decreases with distance travelled. The lower values of angular
dispersion measured in Fig. 4. were achieved using the same
prism, but at a different position [18].
5 Conclusions
In this paper we have presented a new method
for the measurement of angular dispersion which is based
on a spectrally resolved, inverted-side Mach–Zender interferometer. The coarse evaluation of the interferograms is
quick, simple and effective for angular dispersion between
10 and 300 µrad/nm, but provides a limited precision only.
For the final and most precise alignment of a stretcher-grating
system, a more sensitive evaluation method was developed,
which has further advantages: it is single-shot and allows
for real-time monitoring. Accuracy as high as 0.2 µrad/nm
has been achieved for angular dispersion in the range of
0.2–40 µrad/nm.
ACKNOWLEDGEMENTS This work was supported by FKFP
0170/2001 and OTKA #33018.
REFERENCES
1 D. Strickland, G. Mourou: Opt. Comm. 56, 219 (1985)
2 K. Osvay, I.N. Ross: Opt. Comm. 105, 271 (1994)
3 C. Fiorini, C. Sauteret, C. Rouyer, N. Blanchot, S. Seznec, A. Migus:
IEEE J. Quant. Electron. QE-30, 1662 (1994)
4 C.M. Gonzalez Inchauspe, O.E. Martinez: Opt. Lett. ´ 22, 1186 (1997)
5 O.E. Martinez, P. Thiagarajan, M.C. Marconi, J.J. Roca: IEEE J. Quantum Electron. QE-25, 2124 (1989)
6 O.T. Zhang, M. Yonemura, Y. Kato: Opt. Comm. 152, 436 (1998)
7 Z. Bor, B. Racz: Opt. Comm. ´ 54, 165 (1985)
8 Z. Bor, B. Racz, G. Szab ´ o, M. Hilbert, H.A. Hazim: Opt. Eng. ´ 32, 2501
(1993)
9 J. Hebling: Opt. Quant. Electron. 28, 1759 (1996)
10 Z.L. Horvath, K. Osvay, Z. Bor: Opt. Comm. ´ 111, 478 (1994)
11 G. Pretzler, A. Kasper, K.J. Witte: Appl. Phys. B70, 1 (2000)
12 Z. Sacks, G. Mourou, R. Danielius: Opt. Lett. 26, 462 (2001)
13 P. Simon, H. Gerhardt, S. Szatmari: Opt. Quant. Electr. ´ 23, 73 (1991)
14 A.P. Kovacs, K. Osvay, Z. Bor, R. Szipöcs: Opt. Lett. ´ 20, 788 (1995)
15 A.P. Kovacs, K. Varj ´ u, K. Osvay, Z. Bor: Am. J. Phys. ´ 66, 985 (1998)
16 D. Meshulach, D. Yelin, Y. Silberberg: JOSA B14, 2095 (1997)
17 O.E. Martinez: JOSA B3, 929 (1986)
18 K. Varju, A.P. Kov ´ acs, G. Kurdi, K. Osvay: Evolution of angular disper- ´
sion in a Gaussian beam of femtosecond pulses, submitted to Opt. Lett.