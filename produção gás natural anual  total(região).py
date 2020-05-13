import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore e offshore por região, entre os anos de 2009 a 2018.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

#Separação da produção total de gás natural de cada região (onshore e offshore)
nordeste, norte, sudeste = ([] for i in range(3))

for index, column in dados.iterrows():
    if column['UF'] == 'Alagoas' or column['UF'] == 'Bahia' or column['UF'] == 'Ceará' or column['UF'] == 'Maranhão' or column['UF'] == 'Rio Grande do Norte' or column['UF'] == 'Sergipe':
        ne = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        nordeste.append(ne)
    elif column['UF'] == 'Espírito Santo' or column['UF'] == 'Rio de Janeiro' or column['UF'] == 'São Paulo':
        se = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        sudeste.append(se)
    else:
        n = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        norte.append(n)

#Criação  de uma dos dataframes da produção total de cada região
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    n = n.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame().reset_index()
    return n

#Tranformação das listas em dataframes    
nordeste = novo_dataframe(nordeste)
norte = novo_dataframe(norte)
sudeste = novo_dataframe(sudeste)

#Criação da função dos histogramas para a produção total de gás natural
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    plt.xlabel('Produção Anual')
    plt.ylabel('Quantidade (m³)')
    if x is nordeste:
       plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'orange')
       plt.title('Produção de gás natural total na região nordeste')
    elif x is norte:
       plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'green') 
       plt.title('Produção de gás natural total na região norte')
    else:
        plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'yellow')
        plt.title('Produção de gás natural total na região sudeste')

#Visualização dos gráficos        
histograma(nordeste)
histograma(norte)
histograma(sudeste)

#Fazendo o gráfico comparativo da produção total de gás natural de cada região
barWidth = 0.25
plt.figure(figsize = (15, 5))
r1 = np.arange(len(nordeste.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
plt.bar(r1, nordeste.iloc[:, 1], color = '#9370DB', width = barWidth, label = 'Nordeste')
plt.bar(r2, norte.iloc[:, 1], color = '#8A2BE2', width = barWidth, label = 'Norte')
plt.bar(r3, sudeste.iloc[:, 1], color = '#4B0082', width = barWidth, label = 'Sudeste')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(nordeste.iloc[:, 0]))], nordeste['Ano'])
plt.ylabel('Quantidade (m³)')
plt.title('Produção de gás natural total (onshore/offshore) entre as regiões produtoras')
plt.legend()
plt.show()
