import pandas as pd

df = pd.read_csv("paises.csv")

latin = df[df['Region'] == 'LATIN AMER. & CARIB']

maior = latin.loc[latin['GDP ($ per capita)'].idxmax()]

print("País:", maior['Country'])
print("GDP per capita:", maior['GDP ($ per capita)'])