import time 
from bs4 import BeautifulSoup
from urllib.request import urlopen
# import requests
# import logging
# import json


# url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'
url = 'https://hipsters.jobs/jobs/?l=Bras%C3%ADlia%20-%20Brasilia%2C%20Federal%20District%2C%20Brazil&p=2'
soup = BeautifulSoup(urlopen(url), "html.parser")

# puxa código e título
titulo = []
codigo = []
for item in soup.select('.listing-item__title'):
  titulo_vaga = item.get_text().strip()
  numeros = ''

  # se título possui código...
  if(titulo_vaga.find(':') > -1):

    # extraindo o título e o código
    texto = slice(0, titulo_vaga.find(':')-4, 1) #título
    numeros = slice((titulo_vaga.find(':')+2), 99, 1) #código

    titulo.append(titulo_vaga[texto])
    codigo.append(titulo_vaga[numeros].strip())

  else:
    numeros = 'sem código'
    titulo.append(titulo_vaga)
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

for i in codigo:
  print(i)


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
 


