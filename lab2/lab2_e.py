
import numpy as np
import matplotlib.pyplot as plt

z = np.random.randint(10, size=(5, 5)) + np.random.randint(10, size=(5, 5)) * 1j


print("Real")
for i in range(5):
    for j in range(5):
        print(z.real)
print()
print("Image")

for i in range(5):
    for j in range(5):
        print(z.imag)