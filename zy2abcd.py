import numpy as np


def zy2abcd(z, y, Length, model=None):
    """
    計算傳輸線的 Z、Y 參數與 ABCD 矩陣。

    參數:
        z: 複數, 每單位長度的串聯阻抗 (ohm/unit length)
        y: 複數, 每單位長度的並聯導納 (S/unit length)
        Length: 浮點數, 線長 (length)
        model: 整數, 指定模型 (None=自動判斷短線; 1=中長線; 2=長線)

    回傳:
        Z: 複數, 總串聯阻抗
        Y: 複數, 總並聯導納
        ABCD: 2x2 numpy array, ABCD 參數矩陣
    """
    Z = z * Length
    Y = y * Length

    if np.real(Y) == 0 and np.imag(Y) == 0:
        # Short line model
        A = 1
        B = Z
        C = 0
        D = 1
        ABCD = np.array([[A, B], [C, D]])
        return Z, Y, ABCD

    Zc = np.sqrt(Z / Y)
    Gamal = np.sqrt(Z * Y)

    if model == 2:
        Z = Zc * np.sinh(Gamal)
        Y = 2 * np.tanh(Gamal / 2) / Zc
    elif model not in [1, 2]:
        # 如果未指定模型或錯誤，預設使用中長線模型
        model = 1

    A = 1 + Z * Y / 2
    B = Z
    C = Y * (1 + Z * Y / 4)
    D = A

    ABCD = np.array([[A, B], [C, D]])
    return Z, Y, ABCD

z = complex(0.01, 0.05)  # 每單位長度阻抗，單位: Ohm
y = complex(0, 2e-6)     # 每單位長度導納，單位: S
length = 100             # 線長，單位: km
model = 2                # 長線模型

Z, Y, ABCD = zy2abcd(z, y, length, model)

print("Z =", Z)
print("Y =", Y)
print("ABCD =\n", ABCD)

