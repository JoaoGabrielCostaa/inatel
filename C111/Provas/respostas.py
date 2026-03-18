import numpy as np
path = 'C:/www/inatel/C111/Provas/chocolate_sales_2025.csv'
data = np.genfromtxt(path, delimiter=',', names=True, dtype=None, encoding='utf-8')

# Questao 1
# Qual a média de preço de um chocolate ao leite segundo este dataset?
milk_prices = data['Price_USD'][data['Product_Type'] == 'Milk Chocolate']
q1 = milk_prices.mean()
print('Questao 1:', q1)

# Questao 2
# Qual o país com maior número de registros de chocolates neste dataset?
countries, counts = np.unique(data['Country'], return_counts=True)
idx2 = np.argmax(counts)
q2_country, q2_count = countries[idx2], int(counts[idx2])
print('Questao 2:', q2_country, q2_count)

# Questao 3
# 5% de todas as vendas feitas com cartão de crédito vão para as operadoras de cartão.
# Baseado nos dados deste dataset, quanto as operadoras de cartão faturaram?
card_revenue = data['Revenue_USD'][data['Payment_Method'] == 'Card'].sum()
q3 = card_revenue * 0.05
print('Questao 3:', q3)

# Questao 4
# Mostre o nome da marca de chocolates com maior número de registros (linhas) nos
# supermercados deste dataset
mask_supermarket = data['Sales_Channel'] == 'Supermarket'
brands, brand_counts = np.unique(data['Brand'][mask_supermarket], return_counts=True)
idx4 = np.argmax(brand_counts)
q4_brand, q4_count = brands[idx4], int(brand_counts[idx4])
print('Questao 4:', q4_brand, q4_count)

# Questão 5
# Qual a quantidade total de unidades de chocolates vendidas segundo este dataset?
q5 = data['Units_Sold'].sum()
print('Questao 5:', q5)