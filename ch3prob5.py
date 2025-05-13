import numpy as np
import math

S_mag = 150_000
pf = 0.8
theta = math.acos(pf)

S = complex( S_mag*math.cos(theta) , S_mag*math.sin(theta) )

print(f"S={S/1000:.2f} kVA")


