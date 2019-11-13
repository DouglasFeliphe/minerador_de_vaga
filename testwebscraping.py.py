from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import logging

url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'
soup = BeautifulSoup(urlopen(url), "html.parser")

#busca os titulos das vagas
def pegaTitulo(soup):
  titulo = []
for item in soup.select('.listing-item__title'):
	texto = item.get_text().strip()
	titulo.append(texto)
return(titulo)

#busca os links das vagas
def pegaLink(soup):
  links = []
for item in soup.select('.listing-item__title'):
	links.append(item.a.get('href'))
return(links)

#busca a data em que a vaga foi publicada
def pegaData(soup):
  data = []
for item in soup.select('.listing-item__date'):
	data.append(item.get_text().strip())
return(data)

#busca a descrição da vaga
def buscavaga():
  descricao = []
  for item in soup.select('.listing-item__desc'):
	descricao.append(item.get_text().strip())
print(descricao)