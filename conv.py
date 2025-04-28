import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])  # 長度 5 的信號
h = np.array([1, -1, 1])        # 長度 3 的濾波器

# 計算卷積範圍
nx = np.arange(len(x))
nh = np.arange(len(h))
ny = np.arange(nx[0] + nh[0], nx[-1] + nh[-1] + 1)

# 預先算好卷積結果
y = np.convolve(x, h)

# 畫圖設定
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 8))

# 初始畫出 x[n]
ax1.stem(nx, x, basefmt="k-", linefmt="b-", markerfmt="bo")
ax1.set_title('Input x[n]')
ax1.grid(True)
ax1.set_xlim(-1, 20)

# 初始畫出 h[-k]
h_flip = h[::-1]
nk = -nh[::-1]  # h[-k] 的座標（翻轉）
ax2.stem(nk, h_flip, basefmt="k-", linefmt="g-", markerfmt="go")
ax2.set_title('Flipped h[-k]')
ax2.grid(True)
ax2.set_xlim(-1, 20)

# 初始畫出累積的 y[n]，此時先給定空的資料範圍
ax3.stem([0], [0], basefmt="k-", linefmt="r-", markerfmt="ro")  # 使用 [0], [0] 來初始化
ax3.set_title('Convolution y[n]')
ax3.grid(True)
ax3.set_xlim(-1, 20)
ax3.set_ylim(0, max(y) + 1)

plt.tight_layout()

# 手動動畫
current_n = ny[0]
accumulated_y = []

while current_n <= ny[-1]:
    # 計算現在 n 對應的 h[n-k]
    shifted_h = np.zeros_like(x, dtype=float)
    products = []

    for i, k in enumerate(nx):
        idx = current_n - k
        if 0 <= idx < len(h):
            shifted_h[i] = h[idx]
            product = x[i] * shifted_h[i]
            products.append(product)

    y_now = np.sum(products)
    accumulated_y.append((current_n, y_now))

    # 更新第二張圖：移動 h[-k]
    ax2.cla()
    ax2.stem(nk + current_n, h_flip, basefmt="k-", linefmt="g-", markerfmt="go")

    # 顯示乘積結果：在 h[n-k] 的位置標註每個乘積
    for i, prod in enumerate(products):
        ax2.text(nx[i] + current_n, h_flip[i], f'{prod:.2f}', color="red", fontsize=10, ha='center')

    ax2.set_title(f'Shifted h[n-k], n={current_n}')
    ax2.grid(True)
    ax2.set_xlim(-1, 20)

    # 更新第三張圖：目前累積的 y[n]
    ys = np.array([v for _, v in accumulated_y])
    ns = np.array([n for n, _ in accumulated_y])
    ax3.cla()
    ax3.stem(ns, ys, basefmt="k-", linefmt="r-", markerfmt="ro")
    ax3.set_title('Convolution y[n]')
    ax3.grid(True)
    ax3.set_xlim(-1, 20)
    ax3.set_ylim(-1, max(y) + 1)

    plt.pause(0.01)
    print(f"n={current_n}, sum={y_now}")

    # 等待使用者按鍵
    print("按一下進到下一步...")
    plt.waitforbuttonpress()

    current_n += 1

plt.show()
