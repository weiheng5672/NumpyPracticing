import matplotlib.pyplot as plt
import numpy as np

# 1. 擴大 x 和 y 的數值範圍（從 -10 到 10），讓馬鞍構造更開闊、明顯
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)

# 2. 建立網格資料
X, Y = np.meshgrid(x, y)

# 3. 計算對應的 z 值 (z = xy)
Z = X * Y

# 4. 建立 3D 圖形視窗
fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection='3d')

# 5. 繪製 3D 曲面圖 (加上 alpha 透明度，讓視覺更有層次)
surf = ax.plot_surface(
    X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.85
)

# 6. 在底部投影等高線圖 (zdir='z'，offset 設定在 Z 軸的最下方)
ax.contour(
    X, Y, Z, zdir='z', offset=np.min(Z) * 1.1, cmap='viridis', levels=20
)

# 7. 設定圖表標題與座標軸標籤
ax.set_title('Saddle Surface (z = xy) with Contours', fontsize=14)
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis', fontsize=12)
ax.set_zlabel('Z Axis', fontsize=12)

# 8. 加入顏色對照條 (Colorbar)
fig.colorbar(surf, shrink=0.5, aspect=5, label='Z Value')

# 9. 顯示圖形
plt.show()