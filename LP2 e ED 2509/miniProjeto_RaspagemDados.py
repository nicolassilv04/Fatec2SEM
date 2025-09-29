'''
CRIAÇÃO DE UM WEB SCRAPING COMO VISTO NA AULA
PARA ESSE PROJETO FOI USADO O MERCADO LIVRE POR CONTER UMA GRANDE VARIEDADE DE ITENS

COMO FUNCIONA:
É PASSADO O NOME DO PRODUTO PARA O FINAL DA URL (CONCATENAÇÃO), APÓS ISSO É FEITO UM REQUEST POR ISSO
E SÃO RETORNADOS OS RESULTADOS BASEADOS NO CODIGO HTML DO SITE
OS ITENS RETORNADOS SÃO ANALISADOS, ENTRAM PARA UMA LISTA DE DICIONARIO E PODEM SER PRINTADOS

POR CONTA DO PRINT SER CONFUSO NESSE CASO, OS ITENS SÃO CONVERTIDOS PARA CSV E POSTERIOMENTE VISUALIZADOS PELO PANDAS
'''

import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

lista_produtos = []

produto_pesquisa = input('Insira qual produto deseja pesquisar: ')
if ' ' in produto_pesquisa:
    produto_pesquisa = produto_pesquisa.replace(' ','-')


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
url = 'https://lista.mercadolivre.com.br/'
pagina = requests.get(url + produto_pesquisa, headers=headers)

dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

procura_titulo = dados_pagina.find_all('h3', class_='poly-component__title-wrapper')
procura_precos = dados_pagina.find_all('span', class_ = 'andes-money-amount__fraction')
procura_link = dados_pagina.find_all('a', class_='poly-component__title')

for titulo, preco, link in zip (procura_titulo, procura_precos, procura_link):
    produto_dicionario = {
        'DESCRIÇÃO': titulo.text,
        'PREÇO': preco.text,
        'LINK': link['href']
    }
    lista_produtos.append(produto_dicionario)

lista_ordenada = sorted(lista_produtos, key=lambda produto: int(produto['PREÇO'].replace('.', '')))

nome_arquivo = 'produtos_mercado_livre.csv'
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    colunas = ['DESCRIÇÃO', 'PREÇO', 'LINK']
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

    escritor.writeheader()
    escritor.writerows(lista_ordenada)

print(f"\nOs dados foram salvos com sucesso no arquivo '{nome_arquivo}'!")


df = pd.read_csv(nome_arquivo)
print(df)



