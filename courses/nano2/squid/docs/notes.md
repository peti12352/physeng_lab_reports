Notes

1. V-I characteristics of a single junction

drive_I = 120 microA
R = 10 kohm

V = I * R = 120 * 10^-6 * 10^4 = 1.2 V
V_pp = 2.4 V

we use a triangular square wave to create a current bias mode using the R, we use a triangular wave to have a linear sweep.


L = h_bar / (2 * e * I_c) = h_bar / (2 * e * I_0 * cos(phi))


down.txt we started with cold (SC) and than we took it out (non-SC)
adaptive gain is applied manually in the oscilloscope to keep the signal in range

we dont measure the temperature, but we can calculate the temperature
big delta caracterizes the suoerconducting regime, big delta is the energy gap, related to binding energy of electrons
the binding energy depends on the temperature
big delta is proportional to T_c * sqrt(1 / (T_c/ T))
cooper pairs
the DOS(E) curve has a threshold, and that is big delta, you can then see the T dependence
with measuring T dependent I-V curve we can extract microscopic parameters of the junction like T_c, I_c, R_N etc.


magentic - tune flux - tune crit current 

2. SQUID I-V characteristics

R = 10 kohm
flux bias current I_b = plusminus 300 microA

V_out = I_b * R = 300 * 10^-6 * 10^4 = 3 V
V_pp = 6 V 

V_bias = 1.2 V

we get cosine curve (response of the SQUID to mag flux phi_ext)

we use 41Hz for triangle sig for mag field -> freq of response 400Hz plus minus 100Hz

21 hz driving freq -> 150 plus minus 70 Hz response freq

-> periodicity (from data to be calculated)

3. SQUID flux response

M = h_reduced / (2 * e * I_c) = h_reduced / (2 * e * I_0 * cos(phi))

phi_0 = h_reduced / (2 * e) = 2.06783383 * 10^-15 Wb


data:
a) 
manual grego calculation
I_c = 82 microA

M = phi_0 / I_c = 2.06783383 * 10^-15 / 82 * 10^-6 = 2.52 * 10^-11 H = 25.2 pH

b)
also calculated using the data with gaussian smoothing and peek detection

Number of periods analyzed: 14
Avg. Bias Voltage Period (Delta V_ref): 0.829272 V
Avg. Bias Current Period (Delta I_flux): 82.927 uA
Calculated Mutual Inductance M: 2.4936e-11 H
Calculated Mutual Inductance M: 0.0249 nH



Task 4: Shapiro steps


goal: phase lockin the josephson junction to external microwave field

estimation of voltage step: 
f = 10 GHz
w = 2 * pi * f = 2 * pi * 10 * 10^9 = 6.28 * 10^10 rad/s

V_DC = (h_bar * w) / (2 * e) = (1.054571817 * 10^-34 * 6.28 * 10^10) / (2 * 1.602176634 * 10^-19) = 20.5 microV

and we use R = 10 kohm

oscilloscope evolution:

all of them


Task 5: sweep freq

freqs = [8, 9, 9.5, 10, 11, 11.5, 12] GHz

analysis: 
Task 5: Frequency Dependence of Shapiro Steps
Objective: Verify delta V = (h/2e) * nu = Phi_0 * nu

1. experimental setup
- swept microwave freq nu: 8 GHz to 12 GHz
- expected linear scaling of voltage steps delta V with nu
- applied scaling: V_squid / 1000 to account for specific SQUID hardware diff amp gain

2. data processing
- removed standard data sorting algorithms; AD/DAC interleaving induced artificial noise
- utilized direct parametric derivative (dV/dt) / (dI/dt) in time domain
- applied peak-prominence criteria to derivatives for robust edge detection

3. results
- plotted raw sweep, differential resistance (dV/dI), and voltage histogram for representative frequencies
- generated delta V vs freq plot

4. err analysis and discrepancies
- measured phi_0 deviates from theoretical 2.0678e-15 Wb
- causes: 
  - high frequency impedance mismatching and parasitic resonances distorting V-I curves at >8 GHz
  - non-flat transfer function of the diff amp at varied input amps
  - large thermal noise floor inherent to cryogenic experimental limits obscuring exact plateau quantization
- observation of quantized steps across multiple macroscopic regimes validates the AC josephson effect despite noise


Task 6: sweep power

freq = 10 GHz

analysis: 
Task 6: Power Dependence of Shapiro Steps
Objective: Characterize delta V behavior under varied microwave power levels.

1. Experimental Setup
* Fixed microwave frequency: 10 GHz.
* Varied power iteratively across 8 distinct anchor levels: [-26.1, -10.4, -5.5, -1.1, 1.8, 4.6, 7.5, 11.7] dBm.
* 28 discrete step measurements obtained. 

2. Data Processing
* Linearly interpolated driving power onto the 28 measurements against the N=[0..28] anchor indices.
* Standardized 10 GHz V_squid extraction utilizing derivative prominence methodology.
* Applied a least-squares polynomial fit (n=3) across mapped data.

3. Quantitative and Qualitative Results
* Extracted quantitative 3rd-order polynomial map $P(N) = a_3 N^3 + a_2 N^2 + a_1 N + a_0$.
* Coefficients: $a_3 \approx 3.7760\times 10^{-3}$, $a_2 \approx -1.9747\times 10^{-1}$, $a_1 \approx 3.9027$, $a_0 \approx -25.22$.
* Fit Verification: Residual Sum of Squares (RSS) $\approx 7.5312$, indicating robust mapping stability across the anchor points without exhibiting Runge's phenomenon or high-frequency over-oscillation.
* Analysis: Plotted continuous power levels alongside $\Delta V$; observed quantised step magnitude dependence verifying reliable microwave absorption up to \SI{11.7}{dBm}.
