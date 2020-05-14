import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose

''' Aqui faremos um histograma com a produção total de gás natural (onshore/offshore) no Brasil
    entre 2009 a 2018, e a sua previsão para 2019 e 2020.'''

#Carregamento da base de dados
total = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',', index_col = 'Localização') 

#Remoção de coluna desnecessária para a série temporal total
total = total.drop(['UF'], axis = 1)

#Conversão de milhões m³ para m³
total['Produção de gás natural (milhões m3)'] = total['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomeação da coluna
total = total.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Soma de toda a produção de cada ano
total = total.groupby(['Ano'])['Produção de gás natural (m³)'].sum().reset_index()

#Tranforma a coluna para o tipo de tempo
total['Ano'] = pd.to_datetime(total['Ano'].astype(str), format = '%Y')

#Tranforma a coluna temporal em índice
total = total.set_index('Ano')

#Plotando o gráfico da produção total de gás natural offshore durante os anos de 2009 a 2018
plt.figure(figsize = (10, 5))
plt.title('Produção total de gás natural offshore/onshore')
plt.xlabel('Anos')
plt.ylabel('Quantidade (m³)')
plt.plot(total)

#Aplicação da decomposição da série temporal
decomposicao = seasonal_decompose(total)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
residuo = decomposicao.resid

#Visualização da tendência,sazionalidade e resíduo
plt.figure(figsize = (10, 5))
plt.subplot(4, 1, 1)
plt.plot(total, label = 'Original')
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
modelo_auto = auto_arima(total, m = 2, seasonal = False, trace = True)

#detalha todos os parâmetros do AUTOARIMA
modelo_auto.summary()

#Fazer uma previsao com auto ARIMA com o número de previsões
proximo_ano = modelo_auto.predict(n_periods = 2)

#Agora será construido o modelo de previsão com o ARIMA escolhido anteriormente e iremos treina-lo   
modelo = ARIMA(total, order = [2, 0, 0])
modelo_treinado = modelo.fit()

#visualizar os detalhes/parâmetros do modelo
modelo_treinado.summary()

#Cria uma previsão da série temporal, passando quantas previsoes queremos adiante (steps)
previsoes = modelo_treinado.forecast(steps = 2)[0]

#Gera um gráfico com as previsoes, comparando com a série original
eixo = total.plot()
modelo_treinado.plot_predict('2009-01-01', '2020-01-01', ax = eixo, plot_insample = False)
