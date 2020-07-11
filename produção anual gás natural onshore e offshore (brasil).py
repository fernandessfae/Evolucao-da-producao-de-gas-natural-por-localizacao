import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore X offshore 
    de todos os estados produtores, entre os anos de 2009 a 2018.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

#Separação dos estados produtores de gás natural onshore X offshore
terra, mar = ([] for i in range(2))

for index, row in dados.iterrows():
    if row['Localização'] == 'Terra':
        terra.append(row)
    else:
        mar.append(row)

#Criação da função dos dataframes dos produtores onshore X offshore
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    n = n.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame().reset_index()
    return n

#Transformação das listas em dataframes
terra = novo_dataframe(terra)
mar = novo_dataframe(mar)

#Criação dos histogramas para a produção total offshore e onshore de todos os estados
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    plt.xlabel('Produção Anual')
    plt.ylabel('Total Produção Anual (m³)')
    if x is terra:
        plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'brown')
        plt.title('Produção de gás natural total onshore dos estados produtores')
    elif x is mar:
        plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'blue')
        plt.title('Produção de gás natural total offshore dos estados produtores')

#Visualização dos gráficos
histograma(terra)
histograma(mar)
    
#Fazendo o gráfico para os produtos energéticos e não energéticos
barWidth = 0.3
plt.figure(figsize = (15, 5))
r1 = np.arange(len(terra.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
plt.bar(r1, terra.iloc[:, 1], color = '#8B4513', width = barWidth, label = 'Onshore')
plt.bar(r2, mar.iloc[:, 1], color = '#0000FF', width = barWidth, label = 'Offshore')
plt.ylabel('Quantidade (m³)')
plt.xticks([r + barWidth for r in range(len(terra.iloc[:, 0]))], terra['Ano'])
plt.title('Produção total de gás natural onshore e offshore em todo o território nacional', fontsize = 16, fontweight = 'bold')
plt.legend()
plt.show() 