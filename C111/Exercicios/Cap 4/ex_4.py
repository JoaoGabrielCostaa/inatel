import numpy as np

matriz = np.random.randint(0, 10, (3, 5))

print("Matriz:")
print(matriz)

linhas, colunas = matriz.shape

total_elementos = linhas * colunas

print("\nLinhas:", linhas)
print("Colunas:", colunas)
print("Total de elementos:", total_elementos)

if total_elementos % 2 == 0:
    print("A matriz pode se tornar um vetor unidimensional com número PAR de elementos.")
else:
    print("A matriz pode se tornar um vetor unidimensional com número ÍMPAR de elementos.")