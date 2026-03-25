import math
K1, L1 = 1.038, 0.006
K2, L2 = 0.231, 0.02
K3, L3 = 1.01, 103.56
lam = 0.823
l2 = lam**2
n2 = 1 + K1*l2/(l2-L1) + K2*l2/(l2-L2) + K3*l2/(l2-L3)
n = math.sqrt(n2)
dn2_dlam = 2*lam*K1/(l2-L1) - 2*lam*l2*K1/((l2-L1)**2) + 2*lam*K2/(l2-L2) - 2*lam*l2*K2/((l2-L2)**2) + 2*lam*K3/(l2-L3) - 2*lam*l2*K3/((l2-L3)**2)
dn_dlam = dn2_dlam / (2*n)

alpha = math.pi / 3
# Brewster's angle
theta_i = math.atan(n)
sin_t1 = math.sin(theta_i)/n
theta_t1 = math.asin(sin_t1)
theta_i2 = alpha - theta_t1
theta_t2 = math.asin(n * math.sin(theta_i2))

dtheta_dn = math.sin(alpha) / (math.cos(theta_t1)*math.cos(theta_t2))
disp = dtheta_dn * dn_dlam

print(f"n: {n:.4f}")
print(f"dn_dlam: {dn_dlam:.6f}")
print(f"dtheta_dn: {dtheta_dn:.4f}")
print(f"Dispersion: {disp * 1000 :.6f} urad/nm")
