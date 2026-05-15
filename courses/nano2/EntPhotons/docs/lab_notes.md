# Entangled Photons Lab Notes

## Phase I: Optics

* alignment -> pump beam position calibrated -> pump spatially centered on BBO crystal
* geometry -> measured source-detector distance $L = 1.35 \pm 0.01$ m
* optomechanics -> flip-mount stability evaluated -> "upflipped" state confirmed mechanically stable -> "downflipped" state exhibits instability -> enforcing "upflipped" configuration for both detectors
* ang res ($\Delta\theta$) -> primarily constrained by detector aperture ($D = 0.005$ m) and distance ($L$) -> geometric limit: $\Delta\theta \approx D/L$ -> $0.005 / 1.35 \approx 3.70 \times 10^{-3}$ rad ($\approx 0.21^\circ$) -> *Note: empirical resolution will also be slightly degraded by the finite pump beam waist (source size) at the crystal.*

## Analysis: Next Procedural Steps

* SPDC Search -> enable pump laser -> initiate coarse angular scans ($\theta_1, \theta_2$) -> localize degenerate SP    DC phase-matching cones
* Singles Optimization -> fine-tune detector alignment on SPDC emission peaks -> maximize single-photon count rates ($N_1, N_2$) -> minimize background/dark counts
* Coincidence Calibration -> route outputs to coincidence electronics / time-tagger -> scan relative angles to satisfy transverse momentum conservation ($-\vec{k}_{i,\text{idler}} = \vec{k}_{i,\text{signal}}$) -> maximize coincidence rate ($N_c$)
* Polarization Analysis -> insert waveplates and polarizers -> characterize correlation visibility in rectilinear (H/V) and diagonal (D/A) bases -> prepare setup for Bell's Inequality (CHSH) measurement

460k global max in counting closest to Grego
440k global max further away from Grego (symmetric)

plus minus 3 deg - tilt crystal -> extra ordinary n changes -> influences phase matching cond -> peak moves

we need to maximize the eff of the down conversion

rotating the half wave plate to find max

then tilting crystal to find max for both detectors


count rate dark count
1: 485
2: 462

1 coincidence every 200 seconds


------------------------------------------

furthest, closest, coinc_count
7.15, 7.1, [199, 212, 211]
7.15, 7.3, [193,182,189]
7.15, 7.5, [163,152, 138]
7.15, 7.6, [129, 142, 121]
7.15, 7.7, [144, 151, 160]
7.15, 7.8, [152, 139, 150]
7.15, 7.9, [151, 130, 147]
7.15, 8.0, [115, 108, 143]
7.15, 8.2, [125, 104, 118]
7.15, 8.4, [119, 113, 113]
7.15, 8.7, [93, 82, 83]
7.15, 8.9, [56, 72, 75]
7.15, 9.0, [72,46,53]
7.15, 9.1, [38, 32, 30]
7.15, 9.2, [6, 9, 11]
7.15, 9.3, [10, 6, 5]
7.15, 9.4, [4, 3, 6]
7.15, 9.5, [7, 8, 9]
7.15, 9.6, []

-------------------------------------------
-------------------------------------------

6.7 (furtest fixed)

6, [1,2,1]
6.3, [1,1,2]
6.5, [2,3,2]
6,75, [6,1,6]
7.0, [5,4,5]
7.2, [1,7,1]
7.4, [5,4,6]
7.8, [3,5,0]
8.2, [2,2,1]
8.6, [0,1,0]
9.1, [0,1,0]





--------------

6.85 (furtest fixed)

9.25, [2,1,1]
8.7, [1,3,6]
8.4, [5,7,7]
8.1, [11, 8, 8]
7.8, [4,3,6]
7.6, [3,5,6]
7.4, [14, 6,7]
7.2, [3, 5, 8]
6.9, [6,4,2]
6.6, [9, 4, 6]
6.3, [1,3,2]
6, [2,0,1]



--------------------


7.0 (furtest fixed)

10, [0,1,1]
9.7, [1,2,1]
9.4, [1,0,0]
9.1, [1,2,3]
8.8, [5,3,4]
8.5, [9,7,13]
8.2, [17, 18, 22]
7.9, [23, 25, 22]
7.7, [24,22,23]
7.4, [27, 19, 21]
7.1, [22, 38, 16]
6.8, [32, 34, 26]
6.5, [20,23,20]
6.2, [11,15,8]
6, [6,1,2]



7.15 (furthest fixed):

5.2, [6, 11, 5]
5.7, [21, 7, 12]
5.9, [13, 6, 12]
6.1, [46, 32, 41]
6.2, [40, 42, 35]
6.35, [102, 80,72]
6.5, [198, 218,223]
6.6, [240, 252, 248]
6.8, [239, 228, 258]
7, [246, 243, 245]
7.3, [219, 196, 205]
7.5, [162, 182,160]
7.6, [149, 187, 152]
7.8, [139,147,155]
8, [110, 106, 137]
8.1, [126, 114, 121]
8.3, [117, 101, 124]
8.4, [105, 106,89]
8.5, [90, 87, 88]
8.8, [64, 63, 84]
9, [57, 41, 35]
9.2, [23, 24, 21]
9.5, [10, 10, 12]
9.75, [10,8,6]
10, [5,8,5]
10.2, [4,5,9]
10.5, [6,5,7]
11, [1,7,6]

-------------

7.3 (furthest fixed)

5.2, [2,1,1]
5.4, [1,2,1]
5.6, [1,0,1]
6.0, [2,0,3]
6.5, [12, 17, 9]
6.8, [10, 11, 6]
7, [11, 12, 4]
7.2, [12, 6, 14]
7.4, [6, 7, 13]
7.6, [4, 6, 8]
7.8, [9, 12, 14]
8, [13, 12, 13]
8.2, [13, 17, 7]
8.6, [18, 17, 21]
9, [11, 22, 17]
9.2, [14, 8, 5]
9.4, [3, 7, 4]
9.7, [1, 2, 1]

--------------

7.4 (furthes fixed)


9.4, [8, 3, 5]
9.6, [4,5,5]
9.9, [3, 2, 3]
9.2, [12, 13, 9]
8.9, [15, 11, 19]
8.7, [20, 17,18]
8.5, [24, 18, 20]
8.2, [19, 16, 8]
8, [16, 21, 13]
7.8, [8, 9, 13]
7.5, [9, 10, 7]
7.2, [14, 12, 18]
6.8, [13, 17, 19]



7.6 (furthest fixed)

10, [6,7,7]
10.3, [5,3,4]
9.8, [5,8,10]
9.6, [11, 17, 11]
9.4, [16,11,12]
9.2, [7, 13, 12]
9, [18, 14, 12]
8.8, [11, 13, 8]
8.6, [13,6,11]
8.3, [10,6,8]
8, [4, 5, 2]
7.7, [2,1,7]
7.4, [8,2,4]


7.7 furthes fixed

7.4, [3,1,2]
7.65, [1,0,4]
7.9, [3,1,3]
8.2, [3,1,3]
8.75, [3,10,8]
10.5, [4,4,3]
10.2, [5,2,7]
10, [10,7,5]
9.8, [6,9,8]
9.5, [8,10,15]
9.2, [11,16,8]
9, [7,10,11]


-----------------

coninciedence_window, count
1,14
2,35
3,130
4,150
5,190
6,190
7,205
8,215
9,225
10,230
11,240
12,240
15,275
20,295
25,340
30,360
35,385
40,420
45,435
50,470
55,485
60,520
80,620
100,710
120,790
150,960
200,1150
250,1400
300,1600
350,1820
400,2110
500,2520
600,3000
700,3500
800,4000
900,4350
1000,4750
1500,6800
2500,11000



------------

-------
---------

marginal:

furthest
7.2, 256000
7.9, 178000
7.5, 230000
8.3, 160000
9, 130000
6.8,156000
6.5,80050
6,36000
5.5,30500
4.9,27000
4,26500




task 7:

NewFile1: sweep long pulse
NewFile2: short pulse - 230ns (as we were expecting)

1 and 2 we were using AC coupling, there is shit

below we set DC coupling. good. god
NewFile3: low freq 1hz-80hz using long pulse 
NewFile4: low freq 1hz-80hz using short pulse 

NewFile5: full freq 1hz-20khz using short pulse 
NewFile6: full freq 1hz-4khz using long pulse 



pulse width 230 ns

f = [1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 35, 45, 60, 70, 85, 100, 150, 200, 300, 500, 800, 1400, 2000, 5000, 10000, 15000, 16000, 17000, 20000] Hz
V = [9.2, 9.4, 9.7, 9.9, 10.0, 10.3, 11.0, 12.3, 13.2, 14.3, 16.6, 18.9, 22.0, 24.6, 28.1, 31.1, 42.2, 53.3, 75.5, 119.7, 186.2, 319.5, 451, 1114, 2221, 3461, 3753, 3873, 3894] mV

upper limit (saturation) because of power rail (5V) minus the part used by amplifier (sprox 1V), this causes the saturation to be around 4V. it is a voltage limit, not a frequency one

lower limit is determined by the integration time of the integrator. T_int =1*1e6*22*1e-9
f_int = 1/T_int = 45.45 Hz which is aprox what we observed

SWEEEEEEEP TAKE PHOTO OF PARAMETERS

task 8:

1. 

f = 500hz

We set Ch1 and Ch2 to identical values, we connect both to the AND gate. if we use no pulse shaping, then the overlap coincidence is 230ns, but if we apply pulse shaping the coincidence is 2.25 us


- What is the shortest noticeable delay? 

- What is the longest delay at which a coincidence signal can still be measured? 

- How do these relate to the characteristics of the counting electronics? 


sweep time was too high -> better results ? from 1 to 80 hz

ch2 from AC to DC (capcitance from ac coupling)

it discharges to R_3 while measuring (low limit cause)

task 9:

fine tune duty cycle

duty sweep:
f = 500 Hz

duty = 10, 20, 30, 40, 50, 60, 70, 80, 90 %
V = 120, 220, 330, 400, 550, 700, 800, 920, 1000 mV

freq sweep:
duty 50%

f =


task 10

marginal short pulse length setting
coincidence (joint) ling pulse length setting (no overlap problem)



square signal f=1khz -> no integration time (aliasin) problems
-> record diff count rates for individ ch, by changin gthe duty cycle
meas coincidence rates

we are chan

SPAD1: 40, 50, 85, 110
SPAD2: 34, 60, 90, 120
JOINT: 11.7, 11.4, 11.5, 11.5















SPAD1: 0.08, 2, 0.78, 1.1, 3.2, 0.045, 2.1, 3.2, 2.15 V
SPAD2: 0.07, 0.13, 0.06, 0.42, 0.65, 0.037, 0.230, 2.75, 1.75 V
JOINT: 18, 40, 15, 90, 210, 13.5, 57, 700, 340 mV



plus 1)
so much time passed in the lab that we have to comensate for the light effects from the sun which has a sinusoidal time function here

