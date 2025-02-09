import numpy as np
from sympy import Rational

# 定義三個向量
A = np.array([3, 2, 1])
B = np.array([1, 1, -1])
C = np.array([1, 2, 3])

a = A+B-4*C
magnitude_a = np.linalg.norm(a)
magnitude_a_fraction = Rational(int(magnitude_a), 1)  # 範數轉換為分數
print("(a)：", magnitude_a_fraction)

b = A+2*B-C
magnitude_b = np.linalg.norm(b)

b_fraction = np.array([Rational(int(x), 1) for x in b])  # 將向量轉換為分數表示
magnitude_b_fraction = Rational(int(magnitude_b), 1)  # 範數轉換為分數

# 計算單位向量並顯示
unit_b = b_fraction / magnitude_b_fraction
print("(b)：", unit_b)

c = np.dot(A, C)
print("(c)：", c)

d = np.cross(B, C)
print("(d)：", d)

e = np.dot(A, np.cross(B, C))
print("(e)：", e)

