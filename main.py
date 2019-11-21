import minerador
import bot_telegram

# url = 'https://hipsters.jobs/jobs/?q=&l=Bras%C3%ADlia+-+Brasilia%2C+Federal+District%2C+Brazil'

soup = minerador.gerar_sopa('https://hipsters.jobs/jobs/?l=Bras%C3%ADlia%20-%20Brasilia%2C%20Federal%20District%2C%20Brazil&p=2')

lista_codigo_titulo = minerador.puxa_titulo_e_codigo(soup)

titulos = lista_codigo_titulo[0]
codigos = lista_codigo_titulo[1]
links = minerador.puxa_link(soup)
datas = minerador.puxa_data(soup)
descricao_previa = minerador.puxa_descricao_da_vaga(soup)
tipos_de_contrato = minerador.puxa_tipo_de_contratacao(soup)
localizacoes = minerador.puxa_local_da_vaga(soup)
empresas = minerador.puxa_empresa(soup)
tipos_de_contrato = minerador.puxa_tipo_de_contratacao(soup)

# criando dicionário
dicionario_de_vagas = minerador.criar_dicionario(datas, titulos, codigos, descricao_previa, links,
                                                 tipos_de_contrato, empresas, localizacoes)

minerador.criar_arquivo_json('vagas.json', dicionario_de_vagas)

bot_telegram.executar_bot(-1001383791263,"ok, funcionando!")

