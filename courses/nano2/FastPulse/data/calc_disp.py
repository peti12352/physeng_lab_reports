import numpy as np

# Sellmeier coefficients
K1, L1 = 1.038, 0.006
K2, L2 = 0.231, 0.02
K3, L3 = 1.01, 103.56

def n2(lam):
    # lam in micrometers
    l2 = lam**2
    return 1 + (K1*l2)/(l2 - L1) + (K2*l2)/(l2 - L2) + (K3*l2)/(l2 - L3)

def n(lam):
    return np.sqrt(n2(lam))

def dn_dlam(lam):
    l2 = lam**2
    term1 = 2*lam*K1/(l2 - L1) - 2*lam*K1*l2/(l2 - L1)**2
    term2 = 2*lam*K2/(l2 - L2) - 2*lam*K2*l2/(l2 - L2)**2
    term3 = 2*lam*K3/(l2 - L3) - 2*lam*K3*l2/(l2 - L3)**2
    dn2_dlam = term1 + term2 + term3
    return dn2_dlam / (2 * n(lam))

lam0 = 0.823 # um
print(f"n(823nm) = {n(lam0)}")
print(f"dn/dlam(823nm) = {dn_dlam(lam0)} / um")

# Assume minimum deviation for a 60-degree prism
alpha = np.radians(60)
theta_e = np.arcsin(n(lam0) * np.sin(alpha/2))
dtheta_dn = 2 * np.sin(alpha/2) / np.cos(theta_e)
print(f"Angle of emergence = {np.degrees(theta_e)} deg")
print(f"dtheta/dn = {dtheta_dn}")

dispersion_rad_per_um = dtheta_dn * dn_dlam(lam0)
dispersion_urad_per_nm = dispersion_rad_per_um * 1e6 / 1e3 # urad / nm
print(f"Angular dispersion (min deviation) = {dispersion_urad_per_nm} urad/nm")

# What if angle of incidence is Brewster's angle?
theta_i_brewster = np.arctan(n(lam0))
theta_t1 = np.arcsin(np.sin(theta_i_brewster)/n(lam0))
theta_i2 = alpha - theta_t1
theta_t2 = np.arcsin(n(lam0)*np.sin(theta_i2))

dtheta_dn_general = np.sin(alpha) / (np.cos(theta_t1)*np.cos(theta_t2))
disp_brewster = dtheta_dn_general * dn_dlam(lam0) * 1e3
print(f"Angular dispersion (Brewster) = {disp_brewster} urad/nm")

