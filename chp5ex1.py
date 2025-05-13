import cmath
import math

# 給定資料
V_r_line = 220e3  # 負載端線電壓 (V)
S_total = 381e6  # 負載總視在功率 (VA)
pf = 0.8  # 功率因數
length_km = 40  # 傳輸線長度 (km)
r_per_km = 0.15  # 每公里電阻 (ohm/km)
l_per_km = 1.3263e-3  # 每公里電感 (H/km)
f = 60  # 頻率 (Hz)

# 線路參數
R = r_per_km * length_km
X = 2 * math.pi * f * l_per_km * length_km
Z = complex(R, X)

# 負載端相電壓
V_r_phase = V_r_line / math.sqrt(3)

# 負載視在功率 (每相)
S_phase = S_total / 3


def calculate(pf, leading=False):
    if leading:
        angle = -math.acos(pf)
    else:
        angle = math.acos(pf)

    # 負載電流（相）
    I_r = cmath.rect(S_phase / V_r_phase, -angle)

    # 送端電壓（相）
    V_s_phase = V_r_phase + I_r * Z

    # 送端功率
    S_s_total = 3 * V_s_phase * I_r.conjugate()

    # 電壓調整率
    VR = (abs(V_s_phase) - abs(V_r_phase)) / abs(V_r_phase) * 100

    # 效率
    efficiency = (S_total * pf) / (S_s_total.real) * 100

    # 回傳結果
    return {
        '送端相電壓 (kV)': abs(V_s_phase/1000),
        '送端線電壓 (kV)': abs(V_s_phase/1000) * math.sqrt(3),
        '送端總有功功率 (MW)': S_s_total.real/1e6,
        '送端總虛功功率 (Mvar)': S_s_total.imag/1e6,
        '電壓調整率 (%)': VR,
        '效率 (%)': efficiency
    }


# (a) Lagging PF
result_a = calculate(pf, leading=False)

# (b) Leading PF
result_b = calculate(pf, leading=True)

# 印出結果
print("=== (a) 負載為 0.8 lagging ===")
for key, value in result_a.items():
    print(f"{key}: {value:.2f}")

print("\n=== (b) 負載為 0.8 leading ===")
for key, value in result_b.items():
    print(f"{key}: {value:.2f}")
