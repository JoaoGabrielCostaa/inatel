import numpy as np

pares1 = np.arange(0, 52, 2)

pares2 = np.arange(100, 49, -2)

concatenado = np.concatenate((pares1, pares2))

ordenado = np.sort(concatenado)

print("Array 1:", pares1)
print("Array 2:", pares2)
print("Concatenado:", concatenado)
print("Ordenado:", ordenado)