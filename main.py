import numpy as np
import sympy

# 顯示 sympy 版本
print("SymPy Version:", sympy.__version__)
print("\n")  # 分隔

# 建立一個一維 NumPy 陣列
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)
print("Type of NumPy Array:", type(array))
print("Shape of NumPy Array:", array.shape)
print("\n")  # 分隔

# 計算陣列的平方
array_squared = array ** 2
print("Squared Array:", array_squared)
print("\n")  # 分隔

# 創建一個 2D 陣列（矩陣）
matrix = np.array([[1, 2], [3, 4]])
print("2D Matrix:\n", matrix)
print("Type of 2D Matrix:", type(matrix))
print("Shape of 2D Matrix:", matrix.shape)
print("\n")  # 分隔

# 進行矩陣乘法
result = np.dot(matrix, matrix)
print("Matrix Multiplication Result:\n", result)
print("\n")  # 分隔

# 生成一個隨機數字的 4x2 陣列
random_array = np.random.rand(4, 2)
print("Random Array:\n", random_array)
print("Type of Random Array:", type(random_array))
print("Shape of Random Array:", random_array.shape)
