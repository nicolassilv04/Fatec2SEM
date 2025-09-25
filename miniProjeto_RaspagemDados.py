import webbrowser
from bs4 import BeautifulSoup

#FAZENDO A PESQUISA DO ITEM
pesquisa = str(input('O que deseja pesquisar: '))
webbrowser.open('lista.mercadolivre.com.br/' + pesquisa)


