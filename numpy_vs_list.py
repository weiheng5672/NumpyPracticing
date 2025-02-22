import numpy as np
import time

N = 100_000  # 產生10萬個數值
loop = 1000  # 重複加總的次數

# 生成數據
nd_array = np.random.rand(N)
py_list = list(nd_array)  # 轉換為普通 list

# 測試 NumPy ndarray 計算總和
start_time = time.time()
for _ in range(loop):
    sum_1 = np.sum(nd_array)
numpy_time = time.time() - start_time

# 輸出結果
print(f"NumPy 計算總和時間: {numpy_time:.9f} 秒")

# 測試 Python list 計算總和
start_time = time.time()
for _ in range(loop):
    sum_2 = sum(py_list)
list_time = time.time() - start_time

# 輸出結果
print(f"Python list 計算總和時間: {list_time:.9f} 秒")
