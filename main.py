from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import logging
import json

url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'
soup = BeautifulSoup(urlopen(url), "html.parser")

#puxa_titulo
titulo = []
for item in soup.select('.listing-item__title'):
  texto = item.get_text().strip()
  titulo.append(texto)
titulo
 
#puxa link
links = []
for item in soup.select('.listing-item__title'):
  links.append(item.a.get('href'))
links

# puxa data
data = []
for item in soup.select('.listing-item__date'):
	data.append(item.get_text().strip())
data

# for i in range(0,len(lista_vagas)):
#     lista_vagas = {data: (titulo[i], links[i])} 
#     print(lista_vagas)
    





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






