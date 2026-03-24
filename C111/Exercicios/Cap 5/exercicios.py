import pandas as pd

# 1. Criar as duas Series

seriesAno1 = pd.Series({
    'Java': 16.25,
    'C': 16.04,
    'Python': 9.85
})

seriesAno2 = pd.Series({
    'C': 16.21,
    'Python': 12.12,
    'Java': 11.68
})

print("Series Ano 1:")
print(seriesAno1)

print("\nSeries Ano 2:")
print(seriesAno2)


# 2. Soma das porcentagens por ano

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print("\nTotal Ano 1:", totalAno1)
print("Total Ano 2:", totalAno2)


# 3. Crescimento / declínio

crescimento = seriesAno2 - seriesAno1

print("\nCrescimento / Declínio:")
print(crescimento)


# 4. Mostrar apenas linguagens que cresceram

cresceram = crescimento[crescimento > 0]

print("\nLinguagens que cresceram:")
print(cresceram)


# 5. Projeção para próximos 2 anos

ano3 = seriesAno2 + crescimento
ano4 = ano3 + crescimento

print("\nProjeção Ano 4:")
print(ano4)

maisPopular = ano4.nlargest(1)

print("\nLinguagem mais popular em 2 anos:")
print(maisPopular)


# Criando DataFrame exemplo (tópico 5.3)

df = pd.DataFrame({
    'X': [10, 20, 30, 40, 50],
    'Y': [5, 15, 25, 35, 45],
    'Z': [2, 4, 6, 8, 10]
}, index=['A', 'B', 'C', 'D', 'E'])

print("\nDataFrame:")
print(df)


# 6. Média dos elementos da coluna X menores que 30

media_x = df[df['X'] < 30]['X'].mean()

print("\nMédia de X < 30:", media_x)


# 7. Média linha D (loc) e soma linha E (iloc)

media_D = df.loc['D'].mean()
soma_E = df.iloc[4].sum()

print("\nMédia da linha D:", media_D)
print("Soma da linha E:", soma_E)


# 8. Slicing

slice_df = df.loc[['A','C','E'], ['X','Y']]

print("\nSlicing:")
print(slice_df)

print("\nSoma por linha:")
print(slice_df.sum(axis=1))

print("\nSoma por coluna:")
print(slice_df.sum(axis=0))