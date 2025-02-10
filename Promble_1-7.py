import numpy as np
from sympy import Rational

# 定義三個向量
A = np.array([2, 8, 7])
B = np.array([4, 6, 8])

AB = B - A
print("AB：", AB)

magnitude = np.linalg.norm(AB)
print("magnitude of N：", magnitude)

AB_fraction = np.array([Rational(int(x), 1) for x in AB])  # AB轉換為分數
magnitude_fraction = Rational(int(magnitude), 1)  # 範數轉換為分數

# 計算單位向量並顯示
unit_AB = AB_fraction / magnitude_fraction
print("單位向量：", unit_AB)