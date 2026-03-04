import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))

print("Matriz 4x4:")
print(matriz)

media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

print("\nMédia de cada linha:")
print(media_linhas)

print("\nMédia de cada coluna:")
print(media_colunas)

print("\nMaior média das linhas:", np.max(media_linhas))
print("Maior média das colunas:", np.max(media_colunas))

valores, contagens = np.unique(matriz, return_counts=True)

print("\nQuantidade de aparições de cada número:")
for v, c in zip(valores, contagens):
    print(f"Número {v} aparece {c} vez(es)")

print("\nNúmeros que aparecem exatamente 2 vezes:")
for v, c in zip(valores, contagens):
    if c == 2:
        print(v)