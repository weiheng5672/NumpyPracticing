import numpy as np
import matplotlib.pyplot as plt
from fontTools.varLib import VVAR_FIELDS

# 參數設定
Vm = 100         # 電壓振幅
thetav = 0       # 電壓相位（度）
Z = 1.25         # 阻抗大小
gama = 60        # 阻抗相位（度）

thetai = thetav - gama                      # 電流相位（度）
theta = np.radians(thetav - thetai)        # 相位差轉為弧度
Im = Vm / Z                                 # 電流振幅
wt = np.arange(0, 2*np.pi, 0.05)            # wt 從 0 到 2π

# 瞬時電壓與電流
v = Vm * np.cos(wt)
i = Im * np.cos(wt + np.radians(thetai))
p = v * i                                   # 瞬時功率

# 有效值
V = Vm / np.sqrt(2)
I = Im / np.sqrt(2)
P = V * I * np.cos(theta)                   # 平均功率
Q = V * I * np.sin(theta)                   # 虛功率
S = P + 1j * Q                              # 複功率

# 脈動功率項（從教材方程）
pr = P * (1 + np.cos(2 * (wt + np.radians(thetav))))  # Eq. 2.6
px = Q * np.sin(2 * (wt + np.radians(thetav)))        # Eq. 2.8

PP = P * np.ones_like(wt)                  # 均功率線
Vrms = V * np.ones_like(wt)
QQ = Q * np.ones_like(wt)                  # 無功線
xline = np.zeros_like(wt)                  # x 軸基準線

# 轉換成角度方便對照
wt_deg = np.degrees(wt)

# 畫圖
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(wt_deg, v, label='v(t)')
plt.plot(wt_deg, Vrms, 'b--', label='Vrms')
plt.plot(wt_deg, i, label='i(t)')

plt.plot(wt_deg, xline, 'k--')
plt.grid(True)
plt.title(f'v(t) = Vm cos(wt), i(t) = Im cos(wt + {thetai})')
plt.xlabel('wt (degree)')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(wt_deg, p, label='p(t) = v(t)i(t)')
plt.plot(wt_deg, xline, 'k--')
plt.grid(True)
plt.title('p(t) = v(t)i(t)')
plt.xlabel('wt (degree)')

plt.subplot(2, 2, 3)
plt.plot(wt_deg, pr, label='pr(t) Eq. 2.6')
plt.plot(wt_deg, PP, 'r--', label='Average Power P')
plt.plot(wt_deg, xline, 'k--')
plt.grid(True)
plt.title('pr(t) = P[1 + cos(2wt)]')
plt.xlabel('wt (degree)')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(wt_deg, px, label='px(t) Eq. 2.8')
plt.plot(wt_deg, QQ, 'g--', label='Reactive Power Q')
plt.plot(wt_deg, xline, 'k--')
plt.grid(True)
plt.title('px(t) = Q sin(2wt)')
plt.xlabel('wt (degree)')
plt.legend()

plt.tight_layout()
plt.show()
