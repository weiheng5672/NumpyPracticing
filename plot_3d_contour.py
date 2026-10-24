import matplotlib.pyplot as plt
import numpy as np


# 1. 定義函數
def f(x, y):
    # 計算分母
    denominator = x**2 + y**2

    # 使用 np.where 處理 (0, 0) 的情況，避免除以零 (0/0)
    # 當 x^2 + y^2 == 0 時設為 0，否則計算 2xy / (x^2 + y^2)
    return np.where(denominator == 0, 0, (2 * x * y) / denominator)


# 2. 建立 x 和 y 的網格點 (Meshgrid)
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# 3. 計算 Z 值
Z = f(X, Y)

# 4. 繪圖設定
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# 繪製 3D 曲面
surf = ax.plot_surface(
    X, Y, Z, cmap="viridis", edgecolor="none", alpha=0.85, rstride=2, cstride=2
)

# 繪製底部等高線投影 (zdir='z', offset 指導投影落在哪個 z 軸平面上)
cset = ax.contour(
    X,
    Y,
    Z,
    zdir="z",
    offset=-1.2,
    cmap="viridis",
    levels=15,
    linewidths=1.5,
)

# 5. 設定座標軸標籤與範圍
ax.set_xlabel("X ", fontsize=12)
ax.set_ylabel("Y ", fontsize=12)
ax.set_zlabel("Z  f(x,y)", fontsize=12)
ax.set_title(
    r"$f(x,y) = \frac{2xy}{x^2+y^2}$ ", fontsize=14
)

ax.set_zlim(-1.2, 1.2)  # 固定 Z 軸範圍以展示投影

# 新增顏色條 (Colorbar)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="f(x, y)")

plt.show()