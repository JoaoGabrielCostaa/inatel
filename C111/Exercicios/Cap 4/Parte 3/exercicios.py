import csv
import os
import numpy as np


def carregar_dados(caminho):
    dados = []

    with open(caminho, encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=';')

        for linha in leitor:
            registro = {chave.strip(): (valor.strip() if valor else '') for chave, valor in linha.items()}
            dados.append(registro)

    return dados


def extrair_colunas(dados):
    status = np.array([d['Status Mission'] for d in dados])
    local = np.array([d['Location'] for d in dados])
    empresa = np.array([d['Company Name'] for d in dados])
    detalhe = np.array([d['Detail'] for d in dados])

    custos = []

    for d in dados:
        valor = d.get('Cost', d.get(' Cost', ''))

        try:
            valor = float(valor.replace(' ', '')) if valor != '' else np.nan
        except:
            valor = np.nan

        custos.append(valor)

    custos = np.array(custos, dtype=float)

    return status, local, empresa, detalhe, custos


def calcular_sucesso(status):
    mask = np.char.lower(status) == "success"
    percentual = (mask.sum() / len(status)) * 100
    return percentual, mask.sum()


def media_custos(custos):
    validos = (custos > 0) & np.isfinite(custos)
    if validos.any():
        return np.mean(custos[validos])
    return 0


def missoes_eua(local):
    mask = np.char.find(np.char.lower(local), "usa") >= 0
    return mask.sum()


def missao_mais_cara_spacex(empresas, detalhes, custos):
    filtro = np.char.lower(empresas) == "spacex"

    if not filtro.any():
        return None, None

    custos_spacex = custos[filtro]

    if not np.isfinite(custos_spacex).any():
        return None, None

    indice = np.nanargmax(custos_spacex)

    return detalhes[filtro][indice], custos_spacex[indice]


def contar_empresas(empresas):
    nomes, qtd = np.unique(empresas, return_counts=True)
    ordem = np.argsort(qtd)[::-1]

    return nomes[ordem], qtd[ordem]


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAMINHO_CSV = os.path.join(BASE_DIR, "space.csv")

dados = carregar_dados(CAMINHO_CSV)

status, local, empresas, detalhes, custos = extrair_colunas(dados)

percentual, total_sucesso = calcular_sucesso(status)
media = media_custos(custos)
qtd_eua = missoes_eua(local)
nome_missao, custo_missao = missao_mais_cara_spacex(empresas, detalhes, custos)

lista_empresas, contagem = contar_empresas(empresas)


print(f"\n1) Taxa de sucesso das missões: {percentual:.2f}% ({total_sucesso}/{len(status)})")

print(f"\n2) Média de custos das missões com valor disponível: ${media:.2f}")

print(f"\n3) Total de missões realizadas pelos EUA: {qtd_eua}")

if nome_missao:
    print(f"\n4) Missão mais cara da SpaceX: {nome_missao} - ${custo_missao:.2f}")
else:
    print("\n4) Não foi possível encontrar dados válidos da SpaceX.")

print("\n5) Empresas e quantidade de missões realizadas:")

for nome, qtd in zip(lista_empresas, contagem):
    print(f"{nome} -> {qtd}")