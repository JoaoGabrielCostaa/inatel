import pandas as pd

df = pd.read_csv("paises.csv")

america_norte = df[df['Region'] == 'NORTHERN AMERICA']

print("Quantidade de países da América do Norte:", len(america_norte))