import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA

'''Aqui iremos fazer uma previsão dos estados produtores de gás natural offshore, para os anos de 2019 e 2020'''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';')

'''Agora faremos a separação dos estados produtores offshore.
   1) Faremos a separação dos estados produtores de gás natural offshore usando uma lista para colocarmos num laço.
   2) Iremos ajustar o novo dataframe desmembrado do dataframe inicial
   3) Transformaremos as listas em novo dataframe
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
offshore = []

# 2º Passo
for index, column in dados.iterrows():
    if column['Localização'] == 'Mar':
        m = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        offshore.append(m)

# 3º Passo
offshore = pd.DataFrame(list(offshore))

# 4º Passo
offshore.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']

#Precisaremos fazer a transformação dos números da coluna 'Produção de gás natural (milhões m3)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
offshore['Produção de gás natural (milhões m3)'] = offshore['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
offshore['Produção de gás natural (milhões m3)'] = offshore['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
offshore = offshore.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Agora faremos a soma total da produção de todos os produtos energéticos e não energéticos para cada ano.
offshore = offshore.groupby(['Ano'])['Produção de gás natural (m³)'].sum()

#Transformar os números de cada série anual numa lista com a produção anual
offshore = [float(i) for i in offshore]

#Tranformar a lista num dataframe
offshore = pd.DataFrame(list(offshore))

#Renomear a coluna 0 por 'Produção Anual'
offshore = offshore.rename(columns = {0 : 'Produção Anual'})

#Adiciona uma nova coluna com os anos correspondentes a sua produção.
offshore['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

#Vamos exportar esse novo dataframe para transforma-lo em arquivo CSV
offshore.to_csv(r'D:\Meus Documentos\Desktop\Projetos Cientista de Dados\G2.08 - Evolução da produção de gás natural, por localização (terra e mar) – 2009 a 2018\Produção_gas_natural_offshore_serie_temporal.csv')

#Novo banco de dados com os estados produtores de gás natural onshore de 2009 a 2018
dados2 = pd.read_csv('D:\Meus Documentos\Desktop\Projetos Cientista de Dados\G2.08 - Evolução da produção de gás natural, por localização (terra e mar) – 2009 a 2018\Produção_gas_natural_offshore_serie_temporal.csv')

print(dados2.dtypes)

#Precisamos transformar o ano do tipo 'object' para o ano tipo data para ser aplicada na série temporal
dateparse = lambda dates:pd.datetime.strptime(dates, '%Y')

dados2 = pd.read_csv('D:\Meus Documentos\Desktop\Projetos Cientista de Dados\G2.08 - Evolução da produção de gás natural, por localização (terra e mar) – 2009 a 2018\Produção_gas_natural_offshore_serie_temporal.csv',
                     parse_dates = ['Ano'], index_col = 'Ano', date_parser = dateparse)

#Remover a primeira coluna do dataframe
dados2 = dados2.drop('Unnamed: 0', axis = 1)

#cria o gráfico da série temporal original
plt.plot(dados2)

#cria um modelo para determinar o ARIMA
modelo_auto = auto_arima(dados2, m = 2, seasonal = False, trace = True)

#detalha todos os parâmetros do ARIMA
modelo_auto.summary()

#Fazer uma previsao com auto ARIMA com o número de previsões
proximo_ano = modelo_auto.predict(n_periods = 2)

'''Criar uma variavel com o parâmetros do ARIMA adquiridos com o auto arima, passando o banco de dados e ajustando no modelo
   Lembrando que o auto ARIMA determina varios parâmetros, e maquina escolhe o mais apropriado para ela, entretanto é importante
   testar outros parâmetros para ver como se sai o gráfico da série temporal.'''
   
modelo = ARIMA(dados2, order = [2, 0, 0])
modelo_treinado = modelo.fit()

#visualizar os detalhes/parâmetros do modelo
modelo_treinado.summary()

#Cria uma previsão da série temporal, passando quantas previsoes que queremos adiante (steps)
previsoes = modelo_treinado.forecast(steps = 2)[0]

#Gera um gráfico com as previsoes, comparando com a série original
eixo = dados2.plot()
modelo_treinado.plot_predict('2009-01-01', '2020-01-01', ax = eixo, plot_insample = False)

''' Obs¹: tanto a váriavel 'proximo_ano' e 'previsoes' irao fazer as previsoes posteriores
    e poderão dar valores diferentes, em virtude do AUTO ARIMA já utilizar algumas configurações
    extras para utilizar no seu modelo.
    
    Obs²: no gráfico há a linha do gráfico real e da previsão da máquina, e como a base de dados
    tem poucos dados, é normal as linhas ficarem um pouco distantes.'''