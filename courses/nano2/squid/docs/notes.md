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