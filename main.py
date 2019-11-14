import time 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import logging
import json


# url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'
url = 'https://hipsters.jobs/jobs/?l=Bras%C3%ADlia%20-%20Brasilia%2C%20Federal%20District%2C%20Brazil&p=2'
soup = BeautifulSoup(urlopen(url), "html.parser")

#puxa_titulo
titulo = []
for item in soup.select('.listing-item__title'):
  texto = item.get_text().strip()
  titulo.append(texto)
# titulo

# puxa código
codigo = []
for item in soup.select('.listing-item__title'):
  titulo_vaga = item.get_text().strip()
  numeros = ''
  if(titulo_vaga.find('Cod') > -1 or titulo_vaga.find('Cód') > -1):
    letras = titulo_vaga.rstrip('0123456789')
    numeros = titulo_vaga[len(letras):]    
  else:
    numeros = 'sem código'
  # print(numeros)  
  codigo.append(numeros)
 
#puxa link
links = []
for item in soup.select('.listing-item__title'):
  links.append(item.a.get('href'))


# puxa data
data = []
for item in soup.select('.listing-item__date'):
	data.append(item.get_text().strip())
# data

# puxa empresa
empresa = []
for item in soup.select('.listing-item__info--item-company'):
  texto = item.get_text().strip()
  empresa.append(texto)
# empresa
 
 #puxa localização
locale = []
for item in soup.select('.listing-item__info--item-location'):
  texto = item.get_text().strip()
  locale.append(texto)

#puxador de tipo de contratação
tipo_contratacao = []
for item in soup.select('.listing-item__employment-type'):
  texto = item.get_text().strip()
  tipo_contratacao.append(texto)
# print(tipo_contratacao)

# puxa descricao previa da vaga
desc_vaga = []
for item in soup.select('.visible-xs'):
  texto = item.get_text().strip()
  desc_vaga.append(texto)

# salvar o dicionário gerado em um arquivo JSON
# dicionario_exemplo = {
#   'id': 01,
#   'nome': 'dic_ex'
# }

# convertendo o dicionário para json
# dicionario_json = json.dumps(dicionario_exemplo)

# criando o arquivo json
# arquivo_json = open(dicionario_json,'x')
# arquivo_json.write(dicionario_exemplo)
# arquivo_json.close()
 


