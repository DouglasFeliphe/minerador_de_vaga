import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
# import requests
# import logging
import os.path
import json

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
    if (titulo_vaga.find(':') > -1):

        # extraindo o título e o código
        texto = slice(0, titulo_vaga.find(':') - 4, 1)  # título
        numeros = slice((titulo_vaga.find(':') + 2), 99, 1)  # código

        titulo.append(titulo_vaga[texto])
        codigo.append(titulo_vaga[numeros].strip())

    else:
        numeros = 'sem código'
        titulo.append(titulo_vaga)
        codigo.append(numeros)

# puxa descricao prévia da vaga
descricao_da_vaga = []
for item in soup.select('.visible-xs'):
    texto = item.get_text().strip()
    descricao_da_vaga.append(texto)

# puxa link
link = []
for item in soup.select('.listing-item__title'):
    link.append(item.a.get('href'))

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

# puxa localização
localizacao = []
for item in soup.select('.listing-item__info--item-location'):
    texto = item.get_text().strip()
    localizacao.append(texto)

# puxador de tipo de contratação
tipo_de_contratacao = []
for item in soup.select('.listing-item__employment-type'):
    texto = item.get_text().strip()
    tipo_de_contratacao.append(texto)

# criando dicionário
lista_de_vagas = []
for i in range(0, len(titulo)):
    vaga = {
        data[i]: (titulo[i],
                  codigo[i],
                  descricao_da_vaga[i],
                  link[i],
                  tipo_de_contratacao[i],
                  empresa[i],
                  localizacao[i],
                  )
    }
    lista_de_vagas.append(vaga)

# salvar o dicionário gerado em um arquivo JSON

arquivo_json = 'vagas.json'
#cria o arquivo json
dados_json = json.dumps(lista_de_vagas, ensure_ascii=False, indent=2) # converte o dicionário para json
arquivo = open(arquivo_json, 'w')
arquivo.write(dados_json) # salva o dicionário no arquivo json
arquivo.close()
