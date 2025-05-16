import numpy as np

def rlc2abcd(r, L, C, g, f, Length):
    j = 1j
    z = r + j * 2 * np.pi * f * L / 1000      # L in mH
    y = g + j * 2 * np.pi * f * C / 1_000_000 # C in μF
    Z = z * Length
    Y = y * Length
    A = 1 + Z * Y / 2
    B = Z
    C_ = Y * (1 + Z * Y / 4)
    D = A
    ABCD = np.array([[A, B], [C_, D]])
    return Z, Y, ABCD

# 輸入參數
r = 0.036         # ohm/km
L = 0.8           # mH/km
C = 0.0112        # μF/km
g = 0             # siemens/km
f = 60            # Hz
Length = 130      # km
VR3ph = 325       # kV (L-L receiving voltage)
VR = VR3ph / np.sqrt(3)  # kV (phase voltage)
VR = VR + 0j      # make it complex

# ABCD參數
Z, Y, ABCD = rlc2abcd(r, L, C, g, f, Length)

# Receiving power
S_apparent = 270  # MVA
pf = 0.8
theta = np.arccos(pf)
SR = S_apparent * (np.cos(theta) + 1j * np.sin(theta))  # MVA

# Receiving current (line-to-neutral)
IR = np.conj(SR) / (3 * np.conj(VR))  # kA

# 發送端電壓電流
VsIs = ABCD @ np.array([[VR], [IR]])
Vs = VsIs[0, 0]  # phase voltage
Is = VsIs[1, 0]

Vs3ph = np.sqrt(3) * abs(Vs)  # kV (line-to-line)
Is_amp = 1000 * abs(Is)       # A
pfs = np.cos(np.angle(Vs) - np.angle(Is))
Ss = 3 * Vs * np.conj(Is)     # MVA

# 計算 Voltage Regulation
A = ABCD[0, 0]
VR_NL = abs(Vs3ph / abs(A))   # 預期空載時 receiving voltage（以 Vs3ph/A 估算）
REG = (VR_NL - VR3ph) / VR3ph * 100

# 印出結果
print(f"Is = {Is_amp:.3f} A, pf = {pfs:.6f}")
print(f"Vs = {Vs3ph:.3f} kV (L-L)")
print(f"Ps = {Ss.real:.3f} MW, Qs = {Ss.imag:.3f} Mvar")
print(f"Voltage Regulation = {REG:.5f} %")
