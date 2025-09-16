import math
import cmath
import numpy as np
import matplotlib.pyplot as plt

# Step 1: 基本資料
S = 15000 # 額定功率(VA)
V1 = 2300  # 高壓側額定電壓(V)
V2 = 230   # 低壓側額定電壓(V)
a = V1 / V2  # 變比

# 低壓側進行開路試驗
Voc = 230 # 施加額定電壓(V)
Ioc = 2.1 # 開路電流 (A)
Poc = 50 # 開路損耗 (W)

theta_oc = math.acos(Poc/(Voc*Ioc))
Y_m = cmath.rect(Ioc/Voc , -theta_oc) # 漏電抗(ohm)
X_m_exact = -1/Y_m.imag
R_c_exact = 1/Y_m.real

X_m_approx = Voc / Ioc # 勵磁電抗(ohm)
R_c_approx  = (Voc**2) / Poc # 鐵芯損失電阻(ohm)

# 高壓側進行短路試驗
Isc = 6 # 施加額定電流(A)
Vsc = 47 # 短路電壓(V)
Psc = 160 # 短路損耗(W)

theta_sc = math.acos(Psc/(Vsc*Isc))
Z_eq = cmath.rect(Vsc/Isc , theta_sc) # 漏電抗(ohm)
X_eq_approx = Vsc / Isc # 漏電抗(ohm)
R_eq_approx = Psc / (Isc**2) # 銅損電阻(ohm)

print("(a)反映到高壓側的等效電路參數：")
print(f"精確計算漏電抗 X_eq = {Z_eq.imag:.2f} Ohm")
print(f"精確計算銅損電阻 R_eq = {Z_eq.real:.2f} Ohm")
print(f"近似計算漏電抗 X_eq = {X_eq_approx :.2f} Ohm")
print(f"近似計算銅損電阻 R_eq = {R_eq_approx :.2f} Ohm")
print(f"精確計算勵磁電抗 X_m = {X_m_exact*(a**2)/1000:.2f} kOhm")
print(f"精確計算鐵芯損失電阻 R_m = {R_c_exact*(a**2)/1000:.2f} kOhm")
print(f"近似計算勵磁電抗 X_m = {X_m_approx*(a**2)/1000:.2f} kOhm")
print(f"近似計算鐵芯損失電阻 R_m = {R_c_approx*(a**2)/1000:.2f} kOhm\n")

print("(b)反映到低壓側的等效電路參數：")
print(f"精確計算漏電抗 X_eq = {Z_eq.imag/(a**2):.4f} Ohm")
print(f"精確計算銅損電阻 R_eq = {Z_eq.real/(a**2):.4f} Ohm")
print(f"近似計算漏電抗 X_eq = {X_eq_approx/(a**2):.4f} Ohm")
print(f"近似計算銅損電阻 R_eq = {R_eq_approx/(a**2):.4f} Ohm")
print(f"精確計算勵磁電抗 X_m = {X_m_exact:.2f} Ohm")
print(f"精確計算鐵芯損失電阻 R_m = {R_c_exact:.2f} Ohm")
print(f"近似計算勵磁電抗 X_m = {X_m_approx:.2f} Ohm")
print(f"近似計算鐵芯損失電阻 R_m = {R_c_approx:.2f} Ohm\n")

# 計算電壓調整率，以低壓側
I2_rate = S/V2
I_lag = cmath.rect( I2_rate , -math.acos(0.8) )
I_leading = cmath.rect( I2_rate , math.acos(0.8) )

VR_lag = (  abs(V2+I_lag*(Z_eq/a**2)) - V2 )*100 /V2
VR = (  abs(V2+I2_rate*(Z_eq/a**2)) - V2 )*100 /V2
VR_leading = (  abs(V2+I_leading*(Z_eq/a**2)) - V2 )*100 /V2

print(f"(c)滿載電流的電壓調整率：")
print(f"0.8落後功因：{VR_lag:.4f}%")
print(f"1.0功因：{VR:.4f}%")
print(f"0.8超前功因：{VR_leading:.4f}%")

print(f"(d)電壓調整率-負載電流曲線圖：")

print(f"(e)滿載電流，0.8落後功因，變壓器效率：")
P_out = V2*I2_rate*0.8
P_Cu = (I2_rate**2)*(Z_eq.real/(a**2))
P_core = abs(V2+I2_rate*(Z_eq/a**2))**2/R_c_approx

efficiency= P_out*100/(P_Cu+P_core+P_out)
print(f"銅損：{P_Cu}")
print(f"鐵芯損失：{P_core}")
print(f"變壓器效率：{efficiency}%")

# Current values (A)
amps = np.arange(0, 65.2 + 1e-6, 6.52)

# Power factor cases (lagging, unity, leading)
# 0.8 ± j*0.6 代表功率因數角
I_lagging = amps * (0.8 - 1j * 0.6)
I_unity   = amps * (1.0 + 0j)
I_leading = amps * (0.8 + 1j * 0.6)

# 組成矩陣方便計算
I = np.vstack([I_lagging, I_unity, I_leading])

# 計算 Vp/a
Vpa = V2 + I*Z_eq/(a**2)

# 計算電壓調整率 VR (%)
VR = (np.abs(Vpa) - V2) / V2 * 100

# 繪圖
plt.plot(amps, VR[0, :], 'b-', label='0.8 PF lagging')
plt.plot(amps, VR[1, :], 'k-', label='1.0 PF')
plt.plot(amps, VR[2, :], 'r-', label='0.8 PF leading')

plt.title('Voltage Regulation Versus Load')
plt.xlabel('Load (A)')
plt.ylabel('Voltage Regulation (%)')
plt.legend()
plt.grid(True)
plt.show()

