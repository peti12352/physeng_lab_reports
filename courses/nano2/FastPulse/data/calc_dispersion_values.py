import numpy as np

# Sellmeier for 823nm
lam = 0.823 # um
K = [1.038, 0.231, 1.01]
L = [0.006, 0.02, 103.56]

def calc_n(l):
    l2 = l**2
    n2 = 1.0
    for k, li in zip(K, L):
        n2 += (k * l2) / (l2 - li)
    return np.sqrt(n2)

def calc_dn_dl(l):
    n = calc_n(l)
    l2 = l**2
    sum_terms = 0
    for k, li in zip(K, L):
        # derivative of k*l2/(l2-L) is -2*l*k*L / (l2-L)**2
        sum_terms += (k * li) / ((l2 - li)**2)
    return - (l / n) * sum_terms

def calc_d2n_dl2(l):
    # n' = - (l/n) * S  where S = sum(k*L / (l2-L)^2)
    # n'' = - [(1*n - l*n')/n^2] * S - (l/n) * S'
    # S' = sum(k*L * (-2) * (l2-L)^-3 * 2*l) = sum(-4*l*k*L / (l2-L)^3)
    n = calc_n(l)
    dn = calc_dn_dl(l)
    l2 = l**2
    S = 0
    Sp = 0
    for k, li in zip(K, L):
        S += (k * li) / ((l2 - li)**2)
        Sp += (-4 * l * k * li) / ((l2 - li)**3)
    
    term1 = ((n - l*dn) / n**2) * S
    term2 = (l / n) * Sp
    return - term1 - term2

n_val = calc_n(lam)
dn_val = calc_dn_dl(lam) # in um^-1
d2n_val = calc_d2n_dl2(lam) # in um^-2

# Prism angles (assume min deviation for calculation)
alpha = np.radians(60)
# sin(theta_e) = n * sin(alpha/2)
theta_e = np.arcsin(n_val * np.sin(alpha/2))

# dtheta/dn = 1 / cos(theta_e) if symmetric ?? No. 
# Generalized: dtheta/dn = sin(alpha) / (cos(theta_t1) * cos(theta_e))
theta_t1 = alpha / 2
dtheta_dn = np.sin(alpha) / (np.cos(theta_t1) * np.cos(theta_e))

# 1st order angular dispersion [rad/um]
D1_rad_um = dtheta_dn * dn_val
# Convert to urad/nm: (rad * 1e6) / (um * 1e3) = urad/nm
D1_urad_nm = D1_rad_um * 1000

# 2nd order angular dispersion d^2theta/dlambda^2
# theta' = f(n) * n'
# theta'' = f'(n) * (n')^2 + f(n) * n''
# f(n) = dtheta/dn
# Since we assume theta_e(n), we need d/dn (dtheta_e/dn)
# d/dn ( sin(alpha) / (cos(theta_t1) * cos(theta_e(n))) )
# Since theta_t1 = alpha/2 (fixed), cos(theta_t1) is constant.
# cos(theta_e) = sqrt(1 - n^2 sin^2(alpha/2))
# d/dn [ (1 - n^2 s^2)^-1/2 ] = -1/2 (1 - n^2 s^2)^-3/2 * (-2 n s^2) = n s^2 (1 - n^2 s^2)^-3/2
# f'(n) = sin(alpha)/cos(theta_t1) * n * sin^2(alpha/2) / cos^3(theta_e)

s = np.sin(alpha/2)
fp_n = (np.sin(alpha) / np.cos(alpha/2)) * (n_val * s**2) / (np.cos(theta_e)**3)
D2_rad_um2 = fp_n * (dn_val**2) + dtheta_dn * d2n_val
# Convert to urad/nm^2: (rad * 1e6) / (um^2 * 1e6) = urad/nm^2
D2_urad_nm2 = D2_rad_um2

print(f"n: {n_val:.4f}")
print(f"dn/dlam: {dn_val:.6f} um^-1")
print(f"d2n/dlam2: {d2n_val:.6f} um^-2")
print(f"dtheta/dn: {dtheta_dn:.4f}")
print(f"D1: {D1_urad_nm:.4f} urad/nm")
print(f"D2: {D2_urad_nm2:.4f} urad/nm^2")
