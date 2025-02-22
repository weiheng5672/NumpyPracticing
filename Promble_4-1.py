# 一個氫原子（玻爾半徑約為 0.5 Å）位於兩塊相距 1 mm 的金屬板之間，
# 這兩塊金屬板分別連接到一個 500 V 的電池的正負極。

# 目標：
# 1. 計算電場造成的原子位移 d，相較於原子半徑的比例。
# 2. 估算使氫原子電離所需的電壓。

# 提示：使用表 4.1 中的 α 值來進行估算。
# 氫原子的 atomic polarizability / 4*pi*epsilon_0 = 0.667e-30，單位是米立方(m^3)。

# 結論：即使在原子尺度上，這些位移也是極為微小的。

from scipy.constants import pi, epsilon_0, elementary_charge

# 電壓 500 V
V = 500

# 金屬板間距 10^-3 m
a = 1e-3

# 氫原子極化常數，SI標準單位
alpha = 0.667e-30*4*pi*epsilon_0

# 電場造成的原子位移，米
d = (alpha*V)/(elementary_charge*a)

# 相較於原子半徑的比例
ratio_d = d/0.5e-10

print("計算電場造成的原子位移 d，相較於原子半徑的比例")
print(f"d/原子半徑 = {ratio_d:.1e}")

# 估算使氫原子電離所需的電壓
V_ionize = (0.5e-10*a*elementary_charge)/alpha
print(f"電壓:{V_ionize:.2e} 伏特")
