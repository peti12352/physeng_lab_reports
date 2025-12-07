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

v(sigma)
linear fit coeffs on (l/res) vs voltage:
Slope: 1.192184e+00
Intercept: 1.212277
R²: 0.9985


sigma(v)
Fit slope: 4.187684e+01
Fit intercept: -1.015311e+00
R²: 0.9985

Task 7: about 2% error

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

Task 8: no measurement doing

Task 9 and 10:

multiply by -0.003

DC level 1.225V (transform later)

decay has to reach noise level -> saturation
smoothen curve
different laser powers to find appropriate saturation point

solar_cell:
high lifetime HJT n-type

I.)
kx64-b1-#449
thickness: 151 micrometers
doping: 2.78e15 cm^-3

data path: folder second

experiments:

1. avg_num = 8 (too noisy)

2. avg_num = 512 (better using built in smoothing -> report: manually smoothing and derivate calculation)

3. P > 50W is ok

II.)
kx64-b1-615:
thickness: 153 micrometers
doping: 1.70e15 cm^-3

data path: folder third

experiments:

III.)
kx64-b3-600 X (didn't do it)

Task 12:

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

Task 13:

4.
5.
6.
