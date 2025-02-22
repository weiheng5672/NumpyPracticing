import numpy as np
import matplotlib.pyplot as plt

# 參數設置
N = 50  # 網格大小 (50x50)
max_iter = 1000  # 最大迭代次數
tolerance = 1e-4  # 收斂條件
omega = 1.5  # 鬆弛因子 (1.0 = Gauss-Seidel, 1.5 是超鬆弛 SOR)

# 創建 NxN 網格，初始值為 0
V = np.zeros((N, N))

# 設定邊界條件
x = np.linspace(0, np.pi, N)
V[0, :] = np.sin(x)  # 頂部邊界值 sin(x), x從0到pi
V[-1, :] = 0  # 底部邊界值 0
V[:, 0] = 0  # 左邊界值 0
V[:, -1] = 0  # 右邊界值 0

# Gauss-Seidel + SOR 迭代
for iteration in range(max_iter):
    max_diff = 0  # 記錄最大變化量
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            new_value = (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1]) / 4
            diff = new_value - V[i, j]
            V[i, j] += omega * diff  # 直接就地更新
            max_diff = max(max_diff, abs(diff))

    # 檢查收斂
    if max_diff < tolerance:
        print(f"收斂於 {iteration} 次迭代")
        break

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
ax.set_title("Laplace's Equation Solution (Gauss-Seidel + SOR)")
plt.show()
