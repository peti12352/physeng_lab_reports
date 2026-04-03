import math
K1=1.038
L1=0.006
K2=0.231
L2=0.02
K3=1.01
L3=103.56
lam=0.823
l2=lam**2
n2 = 1 + K1*l2/(l2-L1) + K2*l2/(l2-L2) + K3*l2/(l2-L3)
n = math.sqrt(n2)
dn2_dlam = 2*lam*K1/(l2-L1) - 2*lam*l2*K1/((l2-L1)**2) + 2*lam*K2/(l2-L2) - 2*lam*l2*K2/((l2-L2)**2) + 2*lam*K3/(l2-L3) - 2*lam*l2*K3/((l2-L3)**2)
dn_dlam = dn2_dlam / (2*math.sqrt(n2))

alpha = math.pi / 3
# At minimum deviation:
dtheta_dn = 2 * math.sin(alpha/2) / math.sqrt(1 - (n * math.sin(alpha/2))**2)
ang_disp = dtheta_dn * dn_dlam # rad / um
print("n =", n)
print("dn/dlam =", dn_dlam, "um^-1")
print("dtheta/dn =", dtheta_dn)
print("ang_disp =", ang_disp, "rad/um")
print("ang_disp =", ang_disp * 1000, "urad/nm")
