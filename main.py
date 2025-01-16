import numpy as np

# 建立一個 NumPy 陣列
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", array)

# 計算陣列的平方
array_squared = array ** 2
print("Squared Array:", array_squared)

# 創建一個 2D 陣列
matrix = np.array([[1, 2], [3, 4]])
print("2D Matrix:\n", matrix)

# 矩陣乘法
result = np.dot(matrix, matrix)
print("Matrix Multiplication Result:\n", result)

# 生成隨機數陣列
random_array = np.random.rand(3, 3)
print("Random Array:\n", random_array)
