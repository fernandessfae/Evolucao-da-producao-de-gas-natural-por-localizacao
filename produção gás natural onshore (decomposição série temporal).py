import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

'''Decomposiçãp da série temporal para o produção total onshore de gás natural'''

#Preparação do dataframe para a decomposição temporal
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y')
data = pd.read_csv('Produção_gas_natural_total_onshore_serie_temporal.csv',
                   parse_dates = ['Ano'], index_col = 'Ano', date_parser = dateparse)

data = data.drop('Unnamed: 0', axis = 1)

#Visualização do gráfico da série temporal
ts = data['Produção de gás natural (m³)']

plt.figure(figsize = (10, 5))
plt.xlabel('Anos')
plt.ylabel('Produção de gás natural (m³)')
plt.plot(ts)

#Aplicação da decomposição da série temporal
decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
residuo = decomposicao.resid

plt.plot(tendencia)
plt.plot(sazonal)
plt.plot(residuo)

plt.figure(figsize = (10, 5))
plt.subplot(4, 1, 1)
plt.plot(ts, label = 'Original')
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