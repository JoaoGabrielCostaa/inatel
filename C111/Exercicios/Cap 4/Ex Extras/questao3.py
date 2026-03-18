import pandas as pd

df = pd.read_csv("paises.csv")

media = df['Literacy (%)'].mean()

print("Taxa média de alfabetização:", media)