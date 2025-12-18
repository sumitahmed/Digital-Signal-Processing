# 🔹 7. INVERSE Z-TRANSFORM USING COEFFICIENTS
# Given

# X(z) = 1 − z^(-2) + 3z^(-3)

# Key Idea

# Coefficients directly represent x[n].

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

coeff = [1,0,-1,3]

n = np.arange(len(coeff))

plt.stem(n, coeff)
plt.show()