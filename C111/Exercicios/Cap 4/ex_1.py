import numpy as np

array1 = np.ones(8, dtype=int)
array2 = np.random.randint(0, 10, 8)

array3 = array1 + array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Array Resultante:", array3)

soma_total = np.sum(array3)
print("Soma total:", soma_total)

if soma_total >= 40:
    matriz = array3.reshape(4, 2)
else:
    matriz = array3.reshape(2, 4)

print("Matriz remodelada:")
print(matriz)