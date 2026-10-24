import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    denominator = x**2 + y**2
    return np.where(denominator == 0, 0, (2 * x * y) / denominator)


x = np.linspace(-3, 3, 500)
y = np.linspace(-3, 3, 500)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(8, 6))

# 繪製填色等高線圖 (Contourf)
contour_filled = plt.contourf(X, Y, Z, levels=20, cmap="coolwarm")
plt.colorbar(contour_filled, label="f(x,y)")

# 繪製等高線線條 (Contour) 並標示數值
contour_lines = plt.contour(
    X, Y, Z, levels=10, colors="black", linewidths=0.8
)
plt.clabel(contour_lines, inline=True, fontsize=8)

plt.xlabel("X")
plt.ylabel("Y")
plt.title(r"$f(x,y) = \frac{2xy}{x^2+y^2}$ ")
plt.grid(True, linestyle="--", alpha=0.5)
plt.axis("equal")  # 保持 X, Y 軸比例相同

plt.show()