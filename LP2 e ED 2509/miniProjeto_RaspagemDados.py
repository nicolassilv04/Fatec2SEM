'''
CRIAÇÃO DE UM WEB SCRAPING COMO VISTO NA AULA
PARA ESSE PROJETO FOI USADO O MERCADO LIVRE POR CONTER UMA GRANDE VARIEDADE DE ITENS

COMO FUNCIONA:
É PASSADO O NOME DO PRODUTO PARA O FINAL DA URL (CONCATENAÇÃO), APÓS ISSO É FEITO UM REQUEST POR ISSO
E SÃO RETORNADOS OS RESULTADOS BASEADOS NO CODIGO HTML DO SITE
OS ITENS RETORNADOS SÃO ANALISADOS, ENTRAM PARA UMA LISTA DE DICIONARIO E PODEM SER PRINTADOS

'''

import requests
from bs4 import BeautifulSoup
import csv

lista_produtos = []

def converter_preco(preco_str):
    # Remove R$, espaços e substitui vírgula por ponto
    preco_str = preco_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
    return float(preco_str)

def pesquisa_mercado_livre(produto):
    if ' ' in produto:
        produto = produto.replace(' ','-')


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    url = 'https://lista.mercadolivre.com.br/'
    pagina = requests.get(url + produto, headers=headers)

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

    nome_arquivo = 'produtos_mercado_livre_novo.csv'
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        colunas = ['DESCRIÇÃO', 'PREÇO', 'LINK']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)

        escritor.writeheader()
        escritor.writerows(lista_produtos)

    print(f"\nOs dados foram salvos com sucesso no arquivo '{nome_arquivo}'!")
    return nome_arquivo

pesquisa_mercado_livre('xbox series s')#insira seu produto aqui


