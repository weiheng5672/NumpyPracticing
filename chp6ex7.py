import numpy as np

# 複數導納
y12 = 10 - 20j
y13 = 10 - 30j
y23 = 16 - 32j

# 節點 1 電壓
V1 = 1.05 + 0j

# 負載功率
S2 = -2.566 - 1.102j
S3 = -1.386 - 0.452j

# 初始電壓估值
V2 = 1 + 0j
V3 = 1 + 0j

# 迭代
for iter in range(1, 11):
    V2 = (np.conj(S2)/np.conj(V2) + y12 * V1 + y23 * V3) / (y12 + y23)
    V3 = (np.conj(S3)/np.conj(V3) + y13 * V1 + y23 * V2) / (y13 + y23)
    print(f"Iteration {iter}: V2 = {V2:.4f}, V3 = {V3:.4f}")

print(f"V2 = {np.abs(V2):.5f} ∠ {np.degrees(np.angle(V2)):.4f}")
print(f"V3 = {np.abs(V3):.5f} ∠ {np.degrees(np.angle(V3)):.4f}")

# 設定最後的 V2, V3
V2 = 0.98 - 0.06j
V3 = 1 - 0.05j

# 線路電流
I12 = y12 * (V1 - V2)
I21 = -I12

I13 = y13 * (V1 - V3)
I31 = -I13

I23 = y23 * (V2 - V3)
I32 = -I23

# 複功率計算
S12 = V1 * np.conj(I12)
S21 = V2 * np.conj(I21)

S13 = V1 * np.conj(I13)
S31 = V3 * np.conj(I31)

S23 = V2 * np.conj(I23)
S32 = V3 * np.conj(I32)

# 結果顯示
I1221 = [I12, I21]
I1331 = [I13, I31]
I2332 = [I23, I32]

S1221 = [S12, S21, S12 + S13, S12 + S21]
S1331 = [S13, S31, S31 + S32, S13 + S31]
S2332 = [S23, S32, S23 + S21, S23 + S32]

# 格式化輸出
def print_complex_list(name, arr):
    print(f"{name} = [", end="")
    for val in arr:
        print(f"{val:.4f}, ", end="")
    print("]")

print_complex_list("I1221", I1221)
print_complex_list("I1331", I1331)
print_complex_list("I2332", I2332)

print_complex_list("S1221", S1221)
print_complex_list("S1331", S1331)
print_complex_list("S2332", S2332)
