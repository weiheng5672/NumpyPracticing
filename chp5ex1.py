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

# 以上計算電壓調整率有一個細節，那就是公式和課文中提到的是不一樣的
# 但要這樣算才會是對的
# 先回顧一下課文中的公式
# VR = (abs(V_no-load) - abs(V_full-load)) / abs(V_full-load) * 100
# 也就是說，課文中是以滿載為基準，計算滿載時，相較於無載時，電壓下降了多少
# 但本題中的計算卻是
# (abs(V_s_phase) - abs(V_r_phase)) / abs(V_r_phase) * 100
# 其中，V_r_phase是無載時的一次側電壓，而V_s_phase是滿載時的一次側電壓
# 也就是說，我用無載時為基準，計算滿載時，相較於無載時，電壓提高了多少
# 為什麼會有這種差別?
# 這是因為課文中的定義，是假設一次側電壓不變，接上負載後二次側會下降了多少
# 但本題中卻是假設二次側電壓是固定的，這其實不太真實，但它就是這麼假設
# 這種情況下，我們就要回歸電壓調整率的精神，而不是機械式套用公式
# 電壓調整率就是想知道接上負載後，電壓會下降多少
# 即便本題中，沒有接上負載的電壓是比較低的，但那是因為我們固定二次側電壓
# 那分母是以誰為準，以我們要維持的那個，一般就是用戶
# 請整理以上的說法