import numpy as np


def rlc2abcd(r=None, L=None, C=None, g=None, f=None, Length=None):
    """
    This function returns the pi model's parameters and ABCD constants
    when r (ohms/unit), L (mH/unit), C (uF/unit), g (S/unit), f (Hz), and Length are specified.
    """
    j = 1j  # complex unit

    # Prompt for input if not provided
    if r is None:
        r = float(input("Enter line resistance in ohms per unit length, r = "))
    if L is None:
        L = float(input("Enter line inductance in millihenry per unit length, L = "))
    if C is None:
        C = float(input("Enter line capacitance in microfarad per unit length, C = "))
    if g is None:
        g = float(input("Enter line conductance in siemens per unit length, g = "))
    if f is None:
        f = float(input("Enter frequency in Hz = "))
    if Length is None:
        Length = float(input("Enter line length = "))

    z = r + j * 2 * np.pi * f * L / 1000  # Convert mH to H
    Z = z * Length
    R = Z.real
    X = Z.imag
    y = g + j * 2 * np.pi * f * C / 1e6  # Convert uF to F
    Y = y * Length

    if g == 0 and C == 0:
        print("\nShort line model\n----------------")
        print(f"Z = {Z.real} + j{Z.imag} ohms")
        Y = 0 + 0j
        Zc = 0 + 0j
    else:
        Zc = np.sqrt(Z / Y)
        Gamma = np.sqrt(Z * Y)

        model = None
        while model not in [1, 2]:
            model = int(input("Enter 1 for Medium line or 2 for Long line --> "))
            if model not in [1, 2]:
                print("Enter 1 or 2")

        if model == 2:
            Z = Zc * np.sinh(Gamma)
            Y = 2 * np.tanh(Gamma / 2) / Zc
            print("\nEquivalent pi model\n-------------------")
            print(f"Z' = {Z.real} + j{Z.imag} ohms")
            print(f"Y' = {Y.real} + j{Y.imag} siemens")
            print(f"Zc = {Zc.real} + j{Zc.imag} ohms")
            print(f"alpha*l = {Gamma.real} neper")
            print(f"beta*l = {Gamma.imag} radian = {Gamma.imag * 180 / np.pi}°")
        elif model == 1:
            print("\nNominal pi model\n----------------")
            print(f"Z = {R} + j{X} ohms")
            print(f"Y = {Y.real} + j{Y.imag} Siemens")

    # ABCD parameters
    A = 1 + Z * Y / 2
    B = Z
    C_param = Y * (1 + Z * Y / 4)
    D = A
    ABCD = np.array([[A, B], [C_param, D]])

    print("\nABCD =")
    print(f"{A.real:>11.5g} + j{A.imag:<11.5g}   {B.real:>11.5g} + j{B.imag:<11.5g}")
    print(f"{C_param.real:>11.5g} + j{C_param.imag:<11.5g}   {D.real:>11.5g} + j{D.imag:<11.5g}\n")

    return Z, Y, ABCD


ABCD = rlc2abcd(r=0.036, L=0.8, C=0.0112, g=0, f=60, Length=130)