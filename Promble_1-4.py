import numpy as np
from sympy import Rational

# 定義三個向量
A = np.array([1, 0, 0])
B = np.array([0, 2, 0])
C = np.array([0, 0, 3])

# 計算 B-A 和 C-A
AB = B - A
AC = C - A

print("AB：", AB)
print("AC：", AC)

# 計算叉積 N = AB x AC
N = np.cross(AB, AC)

# 顯示 N 向量
print("N：", N)

# 計算 N 的範數
magnitude = np.linalg.norm(N)

# 顯示範數
print("magnitude of N：", magnitude)

# 將向量和範數轉換為分數表示
N_fraction = np.array([Rational(int(x), 1) for x in N])  # 叉積結果轉換為分數
magnitude_fraction = Rational(int(magnitude), 1)  # 範數轉換為分數

# 計算單位向量並顯示
unit_N = N_fraction / magnitude_fraction
print("單位向量：", unit_N)
