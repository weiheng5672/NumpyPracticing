
import math
import cmath

# Step 1: 基本資料
N1 = 2400  # 高壓側匝數
N2 = 240   # 低壓側匝數
a = N1 / N2  # 匝比

# Step 2: 非理想參數（實際量測或資料）
R1 = 0.2   # 初級電阻 (Ohm)
X1 = 0.45   # 初級漏抗 (Ohm)
R2 = 0.002  # 次級電阻 (Ohm)
X2 = 0.0045   # 次級漏抗 (Ohm)
Rc = 1000  # 勵磁支路 Rc (Ohm)
Xm = 1500  # 勵磁支路 Xm (Ohm)

# Step 3: 等效反映次級參數（反映到高壓側）
R2_eq = R2 * a**2
X2_eq = X2 * a**2

# Step 4: 合併漏阻抗
Req = R1 + R2_eq
Xeq = X1 + X2_eq

# Step 5: 並聯勵磁阻抗（僅供參考，電壓調整率計算通常忽略）
Z_eq_series = complex(Req, Xeq)
Z_magnetizing = 1 / (1/complex(Rc) + 1/complex(0, Xm))  # 並聯組合

print("反映到高壓側的等效電路參數：")
print(f"等效漏阻抗 Z_eq = {Z_eq_series:.4f} Ohm")
print(f"勵磁支路阻抗 Z_mag = {Z_magnetizing:.2f} Ohm\n")

# 通用計算電壓調整率的函數
def calc_voltage_regulation(S_mag, pf, leading=False):
    theta = math.acos(pf)
    if leading:
        theta = -theta  # 對 Leading，相角為正 => 電流超前

    S = cmath.rect(S_mag, theta)
    V2_rated = 240  # 額定電壓
    I2 = S.conjugate() / V2_rated
    I1 = I2 / a
    V_drop = I1 * Z_eq_series
    V1_no_load = V2_rated * a
    V1_full_load = V1_no_load + V_drop
    VR = (abs(V1_full_load) - abs(V1_no_load)) / abs(V1_no_load) * 100

    return {
        "pf_type": "Leading" if leading else "Lagging",
        "S_kVA": S / 1000,
        "I2": I2,
        "V1_no_load": V1_no_load,
        "V1_full_load": abs(V1_full_load),
        "Voltage_Regulation_%": VR
    }

# 模擬兩種情況
S_mag = 150_000  # 150 kVA
pf = 0.8

result_lagging = calc_voltage_regulation(S_mag, pf, leading=False)
result_leading = calc_voltage_regulation(S_mag, pf, leading=True)

# 印出結果
for result in [result_lagging, result_leading]:
    print(f"--- PF {result['pf_type']} ---")
    print(f"S = {result['S_kVA']:.2f} kVA")
    print(f"次側電流 I2 = {result['I2']:.2f} A")
    print(f"一次側空載電壓 = {result['V1_no_load']:.2f} V")
    print(f"一次側負載電壓 = {result['V1_full_load']:.2f} V")
    print(f"電壓調整率 = {result['Voltage_Regulation_%']:.3f} %\n")
