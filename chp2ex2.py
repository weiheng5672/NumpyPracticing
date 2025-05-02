import numpy as np

# 定義參數
V = 1200  # 電壓
Z1 = 60
Z2 = 6 + 12j
Z3 = 30 - 30j

# 計算電流
I1 = V / Z1
I2 = V / Z2
I3 = V / Z3

# 計算複功率
S1 = V * np.conj(I1)
S2 = V * np.conj(I2)
S3 = V * np.conj(I3)

# 總複功率
S = S1 + S2 + S3

# 輸出結果
print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"S3 = {S3}")
print(f"Total S = {S}")
