import numpy as np

# 給定參數
V = 200  # 電壓，rms值
Z1 = 100
Z2 = 10 + 20j
f = 60  # 頻率

# 計算電流
I1 = V / Z1
I2 = V / Z2

# 計算複功率
S1 = V * np.conj(I1)
S2 = V * np.conj(I2)

# 總電流與總功率
I = I1 + I2
S = S1 + S2

# 有功功率與無功功率
P = np.real(S)
Q = np.imag(S)

# 功率因數與角度
PF = np.cos(np.angle(S))

# 目標功率因數 0.8 → 計算對應角度與所需無功功率
thd = np.arccos(0.8)
Qd = P * np.tan(thd)

# 補償無功功率與補償電容
Sc = -1j * (Q - Qd)
Zc = np.abs(V)**2 / np.conj(Sc)
C = 1 / (2 * np.pi * f * abs(Zc))

# 補償後的功率與電流
Sd = P + 1j * Qd
Id = np.conj(Sd) / np.conj(V)

# 輸出結果
print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"Total S = {S}")
print(f"P = {P}")
print(f"Q = {Q}")
print(f"PF = {PF:.2f}")
print(f"Target Qd = {Qd:.2f}")
print(f"Reactive compensation Sc = {Sc:.2f}")
print(f"Capacitor impedance Zc = {Zc:.2f}")
print(f"Capacitance C_μF = {C * 1e6:.2f} μF")
print(f"Compensated power Sd = {Sd:.2f}")
print(f"Compensated current Id = {np.abs(Id)}")
print(f"Original current I = {np.abs(I)}")
