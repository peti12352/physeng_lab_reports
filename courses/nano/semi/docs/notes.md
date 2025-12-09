
we get 4 lifetime values

- `LT(Sl/1024)`: slope-based lifetime from the transient; the instrument fits the decay slope (log domain) over the tail—Semilab names it “Sl/1024” for that internal fitting window.  
- `LT(1/e)`, `LT(1/e2)`: time it takes the transient to drop to 1/e and 1/e² of the peak (classic decay-level definitions).  
- `slm_transient_us`: lifetime saved in the `.slm` transient block (same values used to render the BMP overlay); it’s the device’s stored per-point lifetime result.


Task 1

We did it and also saved the data to then compare with task 5 when we excite this sample

Task 2

We verified saturation of the lifetime

plot: t2_saturate.png

Task 3

in the lab we did the C and N_Fe using the mean value for tau. first mean tau and then calculate. this way of averaging is not the best. we got

C = 5.614460e+13 cm^3·µs

we got a much smaller value than expected, because the tau values were much smaller than expected
the values we used are averaged (the taus are averaged across the whole sample)
and then we use those, but we should actually first calculate the C for each point and then do the averaging.
first you should calculate C and N_Fe and then do the mean. for this we use the MAP and do it per point, and then mean. we obtained

B2 per-point C stats (cm^3·µs):
count    4.328000e+03
mean     2.840602e+13
std      2.738426e+15

This is even smaller. and also std is huge. This made us realize that the outliers were messing it up. We decided to re-do this analysis using some outlier filtering techniques. We use both the mean and the median. results

table: C
method	value	count	SE	boot_hw
0	raw_mean	2.840602e+13	4328	4.162530e+13	6.762436e+13
1	raw_median	7.025753e+13	4328	3.631816e+11	9.724196e+11
2	filt_mean	7.649321e+13	4165	4.064835e+12	7.534944e+12
3	filt_median	7.145814e+13	4165	3.451062e+11	9.414412e+11
4	trimmed_mean	6.833728e+13	4081	4.901219e+11	9.575934e+11
5	trimmed_median	7.145814e+13	4081	3.378766e+11	9.544343e+11

much nicer value for C. We see how using the median, the values are very consistent, with error being 2 orders of magnitude smaller than the value. Then using C trimmed_median we calculate N_Fe

table: N_Fe
method	value	count	SE	boot_hw
0	raw_mean	6.051527e+10	4294	3.828387e+09	7.492122e+09
1	raw_median	1.780841e+10	4294	3.799657e+08	1.202276e+09
2	filt_mean	8.212931e+10	2906	3.783353e+09	7.452658e+09
3	filt_median	2.812276e+10	2906	2.752516e+08	6.696133e+08
4	trimmed_mean	6.840484e+10	2846	2.723208e+09	5.323969e+09
5	trimmed_median	2.812276e+10	2846	2.701389e+08	6.668192e+08

Here not all the values are not so consistent, but filt_median and trimmed_median are almost identical and the error is small


Task 3 and Task 4 

    error calcualtion method:

- SE (standard error):  
  - Mean: SE_mean = std / sqrt(n) (std is sample std, ddof=1).  
  - Median: SE_med ≈ 1.2533 * MAD / sqrt(n), where MAD is median(|x – median(x)|).  

- boot_hw (bootstrap half-width of 95% CI):  
  - Resample the data with replacement many times (e.g., 10,000).  
  - For mean: take the mean of each resample; for median: take the median of each resample.  
  - Take the 2.5th and 97.5th percentiles of the bootstrap distribution; boot_hw is (upper – lower)/2.  

    filter and trim method

    For C (and N_Fe) we applied two cleanup steps before reporting “filtered” and “trimmed” values:

- Filter: keep only pixels where τ_after > τ_before and both lifetimes are between 20 µs and 1000 µs.  
- Trim: on the filtered set, drop the outer 1% and 99% of the C (or N_Fe) distribution (i.e., keep values between the 1st and 99th percentiles).



Task 5:

here we do the Fe_i(t) and FeB(t) curves based on the Task 1 (before flash) measurement and the 10m separated measurements


Here’s how to get both Fe_i(t) and FeB(t) from the 5-point SLX series without needing N_B:

Key assumptions (from the kinetics and the lab note hint):
- Total Fe is constant: Fe_total = Fe_i(t) + FeB(t).
- Pre-flash (B2_1.slx) is the “paired” state: lifetime is shortest.
- Immediately after the flash (B2_1R.slx) the pairs are dissociated: Fe_i ≈ Fe_total, FeB ≈ 0. Subsequent files B2_2R … B2_5R are 10-minute steps of re-association.
- Use the μPCD iron constant C you already derived (e.g., your robust/trimmed value). This lets us convert lifetimes to Fe_i via Eq. I.2.6: N_Fe = C · (1/τ_before – 1/τ_after).

How to extract the time series from 5-point SLX files
1) Choose a per-point τ_pair (before): for each of the 5 positions, take τ_before = LT(Sl/1024) from B2_1.slx.
2) Choose the “after flash t0” per-point τ_flash: for the same positions, take τ_t0 from B2_1R.slx.
3) Compute total Fe per point (this is your Fe_total):
   Fe_total_point = C · (1/τ_pair – 1/τ_t0)
   (Use your chosen C; ideally the robust/trimmed value from earlier.)
4) For each later time t (B2_2R, B2_3R, B2_4R, B2_5R):
   Fe_i_point(t) = C · (1/τ_pair – 1/τ_t)
   FeB_point(t) = Fe_total_point – Fe_i_point(t)
5) Average over the 5 points (mean or median) to get Fe_i(t) and FeB(t) time series; plot vs. time (0, 10, 20, 30, 40 min).
6) Because Fe_total_point is computed per position, small position-to-position differences in τ_pair and τ_t0 are handled; averaging the concentrations at the end is more robust than averaging lifetimes first.

Notes/why this is consistent:
- We use τ_pair from the paired (before-flash) state and τ_t0 from the first dissociated measurement to lock in Fe_total per point. That avoids needing N_B.
- Later τ(t) directly gives Fe_i(t) relative to the same τ_pair and the same C.
- Then FeB(t) = Fe_total – Fe_i(t) by conservation.
- If any point yields negative Fe_i or FeB because τ_t ≤ τ_pair (noise/outlier), drop that point for that timestamp.

plot: task5.png

we fit the curve to obtain R
Fitted R: 3.047e-03 1/min  (5.078e-05 1/s)
R^2 (log-fit): 0.9822

I need the N_B boron concentration (or the resistivity, which could be used to estimate the N_B) but we dont have it. so we will calculate D0 for a couple possible values of N_B 


NB_cm^-3	D0_cm2_per_s
0	1.000000e+15	0.000479
1	3.000000e+15	0.000160
2	1.000000e+16	0.000048
3	3.000000e+16	0.000016
4	1.000000e+17	0.000005

this values for D0 are so high, i was expecting values like

1.1434158384943333e-14 (Isobe/Nakashima 1989)
or
8.149159900147657e-15 (Nakashima/Isobe 1988)


from here onwards tasks 6-13 use notes.ipynb

Task 6: 

wafer_num, voltage:

w, v, res, l
5, 1.255, 0.701, 250.56
4, 1.222, 3.28, 273.78
3, 1.216, 6.28, 249.62
2, 1.215, 13.79, 266.74
1, 1.215, 20.62, 346.68

sigma_sheet = 1/(Resistance / Thickness) = l / res


-> (v\*2e-5) (scaling for report)

sigma(v)
check notes.ipynb
for slope and r2

originally we had measured the voltage offset to be 1.225V (the dc level). however this didnt give great results. the way we determined the v_offset was by the numerical fit

plot: task6.png
Slope     = 0.8375 S/V
  Intercept = -1.0153 S
  V_offset  = 1.2123 V (Baseline Voltage)
  R²: 0.9985


Task 7: about 2% error in the v measurement

res in ohm\*cm
l in micrometers

id, voltage:

i, v, res
D030, 1.232, 21
V42, 1.326, 4.32
china, 1.574, 1
S9, 1.753, 0.37
l1_p, 1.639, 0.685
feri, 1.882, 0.147
ing1, 1.382, 3.018

plot: task7_fit.png
Slope: -0.69947
Intercept: 1.39666
R^2: 0.99862
we fit a linear function and excluded the first two datapoints

Task 8: no measurement doing

Task 9 and 10:

For the upcoming tau(∆n) calculations we created a mobility calculator by copying the method from https://www2.pvlighthouse.com.au/calculators/mobility%20calculator/mobility%20calculator.aspx 
We validated that we obtained the same outputs for the same inputs
This mobility calculator was used to iteratively calculate the value for ∆n using equation
$$\Delta n = \frac{\sigma_s/W - N_{dop}\mu_{maj}(N_{dop}, \Delta n)}{e \mu_{sum}(N_{dop}, \Delta n)} \quad \text{(Eq. 1)}$$

we used tolerance=1e-3 (much smaller than ∆n which is order of magnitudes higher). all converged.

solar_cell:
high lifetime HJT n-type

decay has to reach noise level -> saturation --------
smoothen curve by using averaging. we found that
different laser powers to find appropriate saturation point
1. avg_num = 8 (too noisy)

2. avg_num = 512 (better using built in smoothing -> report: manually smoothing and derivate calculation)

I.)
kx64-b1-#449
thickness: 151 micrometers
doping: 2.78e15 cm^-3

data path: folder second


II.)
kx64-b1-615:
thickness: 153 micrometers
doping: 1.70e15 cm^-3

data path: folder third

figure
plot the following four
tau_t_second_different_intensity.png
tau_t_third_different_intensity.png
tau_dn_second_different_intensity.png
tau_dn_third_different_intensity.png



Task 12:

For the tau(∆n), we need to differentiate the ∆n curve. we use a savgol_filter with a polynomial of order 3 and a windo_length of 21 (which corresponds to 420ns, as we found this gave the best results)

kx78

thickest1 thickness: 2.40 cm
thickest2 thickness: 0.92 cm
thickest3 thickness: 0.74 cm
thickest4 thickness: 0.64 cm

data path: folder kx78-R (R means thickest one)

dc voltage 1.696V -> calc base level of conductance

we also measured the smaller ones

kx77

data path: folder kx77

dc voltage 1.373V -> calc base level of conductance

thickest1 thickness: 2.52 cm
thickest2 thickness: 0.99 cm
thickest3 thickness: 0.64 cm
thickest4 thickness: 0.70 cm

figure:
plot these four
dn_t_kx77_first_different_intensity.png
dn_t_kx77_first_different_width.png
dn_t_kx78_first_different_intensity.png
dn_t_kx78_first_different_width.png

figure:
plot these two
tau_dn_k78_different_intensity.png
tau_dn_k78_different_width.png

figure:
plot thse four
tau_t_kx77_different_width.png
tau_t_kx77_first_different_intensity.png
tau_t_kx78_different_width.png
tau_t_kx78_first_different_intensity.png


Task 13:

4.
5.
6.




The primary purpose of passivation is to suppress surface recombination so that the measured effective lifetime (τeff) accurately reflects the bulk recombination lifetime (τbulk), which is crucial for determining material quality and contamination


EXTRA

List of all equations:

$$\frac{U(t)}{U_0} = O + A \cdot \left(1 - \frac{t}{t_0}\right)^n \cdot \exp\left(-\frac{t}{\tau}\right)$$
$$\tau = \frac{\Delta n}{R} \quad \text{(I.1.1)}$$
$$L_D = \sqrt{D \cdot \tau} \quad \text{(I.1.2)}$$
$$R_{total} = R_{rad} + R_{Auger} + R_{SRH} \quad \text{(I.1.3)}$$
$$\frac{1}{\tau_{eff}} = \frac{1}{\tau_{rad}} + \frac{1}{\tau_{Auger}} + \frac{1}{\tau_{SRH}} \quad \text{(I.1.4)}$$
$$S = \frac{R_{surf}}{\Delta n_{surf}} \quad \text{(I.1.5)}$$
$$\tau_{surf} \approx \frac{W}{2S} + \frac{W^2}{\pi^2 D} \quad \text{(I.1.6)}$$
$$\tau_{surf}(S \to 0) = \frac{W}{2S} \quad \text{(I.1.7)}$$
$$\tau_{surf}(S \to \infty) = \frac{W^2}{\pi^2 D} \quad \text{(I.1.8)}$$
$$\frac{1}{\tau_{eff}} = \frac{1}{\tau_{bulk}} + \frac{1}{\tau_{surf}} \quad \text{(I.1.9)}$$
$$\frac{\partial\Delta n_{av}(t)}{\partial t} = G - R(\Delta n_{av}(t)) = G - \frac{\Delta n_{av}(t)}{\tau_{eff}(\Delta n)}$$
$$\tau_{eff} (\Delta n_{av}) = \frac{\Delta n_{av}}{G - \frac{\partial\Delta n_{av}}{\partial t}} \quad \text{(I.2.2)}$$
$$\tau(\Delta n) = \frac{\Delta n}{G} \quad \text{(I.2.3)}$$
$$\tau(\Delta n) = - \frac{\Delta n}{\frac{\partial\Delta n}{\partial t}} \quad \text{(I.2.4)}$$
$$\Delta n = \text{const} \cdot \exp \left( - \frac{t}{\tau_{eff}} \right) \quad \text{(I.2.5)}$$
$$N_{Fe} = C_{\mu PCD} \left( \frac{1}{\tau_{before}} - \frac{1}{\tau_{after}} \right) \quad \text{(I.2.6)}$$
$$R = \frac{e^2}{\epsilon \epsilon_0 k_B T} N_B D_0 \exp\left( \frac{-E_{mig}}{k_B T} \right) \quad \text{(I.2.7)}$$
$$\delta = \sqrt{\frac{2\varrho}{\mu\omega}} \quad \text{(I.2.8)}$$
$$\Delta n = \frac{\Delta \sigma_s}{W \cdot e \cdot \mu_{sum}(\Delta n, N_{dop})} \quad \text{(I.2.9)}$$
$$\Delta n = \frac{\sigma_s/W - N_{dop} \cdot e \cdot \mu_{maj}(N_{dop}, \Delta n)}{e \cdot \mu_{sum}(N_{dop}, \Delta n)} \quad \text{(I.2.10)}$$
$$d_{sense} = \frac{\varrho}{\sigma_{sh,app}} \quad \text{(II.3.1)}$$
$$\frac{\partial[\text{FeB}]}{\partial t} = R \cdot ([\text{Fe}]_{\text{total}} - [\text{FeB}])$$
$$\frac{1}{\tau_{meas}} = \frac{1}{\tau_{bulk}} + \frac{1}{\tau_{diff}} + \frac{1}{\tau_{surface}}$$
$$\tau_{diff} = \frac{d^2}{\pi^2 D_{n,p}}$$
$$\tau_{surf} = \frac{d}{2S}$$