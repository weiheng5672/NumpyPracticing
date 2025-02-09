import numpy as np
import matplotlib.pyplot as plt


# 參數設置
N = 50  # 網格大小 (50x50)
max_iter = 1000  # 最大迭代次數
tolerance = 1e-4  # 收斂條件

# 創建 NxN 網格，初始值為 0
V = np.zeros((N, N))

# 設定邊界條件
x = np.linspace(0, np.pi, N)
V[0, :] = np.sin(x)  # 頂部邊界值 sin(x), x從0到pi
V[-1, :] = 0  # 底部邊界值 0
V[:, 0] = 0  # 左邊界值 0
V[:, -1] = 0  # 右邊界值 0

# 迭代計算 (Jacobi Method)
for iteration in range(max_iter):
    V_new = V.copy()  # 創建副本來存放新值
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            V_new[i, j] = (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1]) / 4

    # 檢查是否收斂
    if np.max(np.abs(V_new - V)) < tolerance:
        print(f"收斂於 {iteration} 次迭代")
        break
    V = V_new  # 更新網格值

# 生成 3D 圖形
x = np.linspace(0, N - 1, N)
y = np.linspace(0, N - 1, N)
X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V, cmap='coolwarm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential V')
ax.set_title("Laplace's Equation Solution (3D)")
plt.show()
