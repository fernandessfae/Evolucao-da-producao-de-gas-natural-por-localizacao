import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose

'''Aqui iremos fazer uma previsão dos estados produtores de gás natural onshore, para os anos de 2019 e 2020'''

#Carregamento da base de dados
onshore = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',', index_col = 'Localização')

#Remoção de linhas e colunas desnecessárias para a série temporal onshore
onshore = onshore.drop(['UF'], axis = 1)
onshore = onshore.drop('Mar')

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
onshore['Produção de gás natural (milhões m3)'] = onshore['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
onshore = onshore.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Agora faremos a soma total da produção de gás natural onshore nacional.
onshore = onshore.groupby(['Ano'])['Produção de gás natural (m³)'].sum().reset_index()

#Tranforma a coluna para o tipo de tempo
onshore['Ano'] = pd.to_datetime(onshore['Ano'].astype(str), format = '%Y')

#Tranforma a coluna temporal em índice
onshore = onshore.set_index('Ano')

#Plotando o gráfico da produção total de gás natural onshore durante os anos de 2009 a 2018
plt.figure(figsize = (10, 5))
plt.title('Produção total de gás natural onshore')
plt.xlabel('Anos')
plt.ylabel('Quantidade (m³)')
plt.plot(onshore)

#Aplicação da decomposição da série temporal
decomposicao = seasonal_decompose(onshore)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
residuo = decomposicao.resid

#Visualização da tendência,sazionalidade e resíduo
plt.figure(figsize = (10, 5))
plt.subplot(4, 1, 1)
plt.plot(onshore, label = 'Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label = 'Tendência')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label = 'Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(residuo, label = 'Residuo')
plt.legend(loc = 'best')
plt.tight_layout()

#cria um modelo para determinar o AUTOARIMA
modelo_auto = auto_arima(onshore, m = 2, seasonal = False, trace = True)

#detalha todos os parâmetros do AUTOARIMA
modelo_auto.summary()

#Fazer uma previsao com auto ARIMA com o número de previsões
proximo_ano = modelo_auto.predict(n_periods = 2)

#Agora será construido o modelo de previsão com o ARIMA escolhido anteriormente e iremos treina-lo   
modelo = ARIMA(onshore, order = [1, 0, 0])
modelo_treinado = modelo.fit()

#visualizar os detalhes/parâmetros do modelo
modelo_treinado.summary()

#Cria uma previsão da série temporal, passando quantas previsoes que queremos adiante (steps)
previsoes = modelo_treinado.forecast(steps = 2)[0]

#Gera um gráfico com as previsoes, comparando com a série original
eixo = onshore.plot()
modelo_treinado.plot_predict('2009-01-01', '2020-01-01', ax = eixo, plot_insample = False)
