import numpy as np
from sympy import Rational

# 定義三個向量
A = np.array([1, 2, 2])
B = np.array([2, 1, -2])
C = np.array([1, -1, 1])

a = np.cross(A, np.cross(B, C))
print("(a)：", a)

b = np.cross(B, np.cross(C, A))
print("(b)：", b)

c = np.cross(C, np.cross(A, B))
print("(c)：", c)

