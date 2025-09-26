import requests, bs4
res = requests.get('lista.mercadolivre.com.br/playstation')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
for link in noStarchSoup.select('a'):
    print(str(link))
tag = noStarchSoup.select('a')[0]
tag.attrs