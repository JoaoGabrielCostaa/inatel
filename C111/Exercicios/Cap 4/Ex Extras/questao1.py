import pandas as pd

df = pd.read_csv("paises.csv")

resultado = df[['Country', 'Region', 'Population', 'Area (sq. mi.)']]

print(resultado)