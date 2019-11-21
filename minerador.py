import time
from bs4 import BeautifulSoup
from urllib.request import urlopen
# import requests
# import logging
import os.path
import json


# url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'
# soup = BeautifulSoup(urlopen(url), "html.parser")

# gerar sopa
def gerar_sopa(url):
    return BeautifulSoup(urlopen(url), "html.parser")


# puxa código e título
def puxa_titulo_e_codigo(soup):
    """retorna uma lista contendo as listas de título e código."""
    titulo = []
    codigo = []
    lista_titulo_e_codigo = []
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
    lista_titulo_e_codigo.append(titulo)
    lista_titulo_e_codigo.append(codigo)
    return lista_titulo_e_codigo


# funcao puxa  link da vaga

def puxa_link(soup):
    """
        puxa os links das vagas
       :param soup:
       :return: lista de todos os links da vaga
    """
    link = []
    for item in soup.select('.listing-item__title'):
        link.append(item.a.get('href'))
    return link


# fucao puxa data
def puxa_data(soup):
    data = []
    for item in soup.select('.listing-item__date'):
        data.append(item.get_text().strip())
    return data


# funcao puxa descricao previa da vaga
def puxa_descricao_da_vaga(soup):
    desc_vaga = []
    for item in soup.select('.visible-xs'):
        texto = item.get_text().strip()
        desc_vaga.append(texto)
    return desc_vaga


# puxa empresa
def puxa_empresa(soup):
    empresa = []
    for item in soup.select('.listing-item__info--item-company'):
        texto = item.get_text().strip()
        empresa.append(texto)
    return empresa


# funcao que puxa o tipo de contratação
def puxa_tipo_de_contratacao(soup):
    tipo_contratacao = []
    for item in soup.select('.listing-item__employment-type'):
        texto = item.get_text().strip()
        tipo_contratacao.append(texto)
    return tipo_contratacao


# funcao puxa a localização da empresa contaratante
def puxa_local_da_vaga(soup):
    local = []
    for item in soup.select('.listing-item__info--item-location'):
        texto = item.get_text().strip()
        local.append(texto)
    return local


# funcao puxa data de publicao da vaga
def puxa_data(soup):
    data = []
    for item in soup.select('.listing-item__date'):
        data.append(item.get_text().strip())
    return data

def criar_dicionario(data,titulo,codigo,descricao_da_vaga,link,tipo_de_contratacao,empresa,localizacao):
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
    return lista_de_vagas

# salvar o dicionário gerado em um arquivo JSON
def criar_arquivo_json(nome_arquivo,dicionario_de_vagas):
    arquivo_json = nome_arquivo
    #cria o arquivo json
    dados_json = json.dumps(dicionario_de_vagas, ensure_ascii=False, indent=2) # converte o dicionário para json
    arquivo = open(arquivo_json, 'w') # abre o aquivo
    arquivo.write(dados_json) # salva o dicionário no arquivo json
    arquivo.close()


if __name__ == '__main__':
    puxa_titulo_e_codigo()
    puxa_link()
    puxa_descricao_da_vaga()
    puxa_local_da_vaga()
    puxa_tipo_de_contratacao()
    puxa_titulo_e_codigo()
    puxa_data()
    gerar_sopa()
    criar_dicionario()
