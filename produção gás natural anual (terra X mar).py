import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore X offshore de todos os estados produtores, entre os anos de 2009 a 2018.'''

#Carregamento da base de dados
dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

#Separação dos estados produtores de gás natural onshore X offshore
terra = []
mar = []

for index, column in dados.iterrows():
    if column['Localização'] == 'Terra':
        t = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        terra.append(t)
    else:
        m = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        mar.append(m)

#Criação dos dataframes dos produtores onshore X offshore
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    n = n.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
    n = n.reset_index()
    return n

terra = novo_dataframe(terra)
mar = novo_dataframe(mar)

#Fazendo o gráfico para todos os estados produtores de gás natural onshore
plt.figure(figsize = (10, 5))
plt.bar(terra.iloc[:, 0], terra.iloc[:, 1], color = 'brown')
plt.xticks(terra['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total onshore dos estados produtores (2009 - 2018)')

#Fazendo o gráfico para todos os estados produtores de gás natural offshore
plt.figure(figsize = (10, 5))
plt.bar(mar.iloc[:, 0], mar.iloc[:, 1], color = 'blue')
plt.xticks(mar['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total offshore dos estados produtores (2009 - 2018)')

#Fazendo o gráfico para os produtos energéticos e não energéticos
barWidth = 0.4
plt.figure(figsize = (10, 5))
r1 = np.arange(len(terra.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
plt.bar(r1, terra.iloc[:, 1], color = '#8B4513', width = barWidth, label = 'Onshore')
plt.bar(r2, mar.iloc[:, 1], color = '#0000FF', width = barWidth, label = 'Offshore')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(terra.iloc[:, 0]))], terra['Ano'])
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural dos estados produtores onshore e offshore (2009 - 2018)')
plt.legend()
plt.show() 
