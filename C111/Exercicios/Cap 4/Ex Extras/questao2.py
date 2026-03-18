import pandas as pd

df = pd.read_csv("paises.csv")

regioes = df['Region'].unique()

print("Regiões diferentes:")
print(regioes)
print("Total de regiões:", len(regioes))