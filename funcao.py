from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import logging
import json
url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'
soup = BeautifulSoup(urlopen(url), "html.parser")

# funcao puxador tiluto da vaga
def puxa_titulo(soup):
  
  titulo = []
  for item in soup.select('.listing-item__title'):
    texto = item.get_text().strip()
    titulo.append(texto)
  print(titulo) 

#funcao puxa  link da vaga
def puxa_link(soup):
  links = []
  for item in soup.select('.listing-item__title'):
    links.append(item.a.get('href'))
  return links

#fucao puxa data
def puxa_data(soup):
  data = []
  for item in soup.select('.listing-item__date'):
    data.append(item.get_text().strip())
  return data

#funcao puxa descricao previa da vaga
def puxa_desc_vaga(soup):
  desc_vaga = []
  for item in soup.select('.visible-xs'):
    texto = item.get_text().strip()
    desc_vaga.append(texto)
  return desc_vaga

 # funcao que puxa o tipo de contratação
def puxa_tip_contratacao(soup):
  tipo_contratacao = []
  for item in soup.select('.listing-item__employment-type'):
    texto = item.get_text().strip()
    tipo_contratacao.append(texto)
  return tipo_contratacao

#funcao puxa a localização da empresa contaratante
def puxa_locale(soup):
  locale = []
  for item in soup.select('.listing-item__info--item-location'):
    texto = item.get_text().strip()
    locale.append(texto)
  return locale


# puxa código da vaga
def puxa_codigo(soup):
  codigo = []
  for item in soup.select('.listing-item__title'):
    titulo = item.get_text().strip()
    numeros = ''
    if(titulo.find('Cod:.')):
      letras = titulo.rstrip('0123456789')
      numeros = titulo[len(letras):]    
    else:
      numeros = 'sem código'
    #print(numeros)   
    codigo.append(numeros)
  return codigo

#funcao puxa data de publicao da vaga
def puxa_data(soup):
    data = []
  for item in soup.select('.listing-item__date'):
      data.append(item.get_text().strip())
  return data
    

if __name__ == '__main__':
  puxa_titulo()