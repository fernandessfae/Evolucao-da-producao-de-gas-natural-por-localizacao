import pandas as pd
import matplotlib.pyplot as plt

''' Aqui faremos um histograma com a produção total de gás natural (onshore/offshore) no Brasil
    entre 2009 a 2018.'''

#Carregamento da base de dados
dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')  

#Conversão de milhôes m³ para m³
dados['Produção de gás natural (milhões m3)'] = dados['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomeação da coluna
dados = dados.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Soma de toda a produção de cada ano
dados = dados.groupby(['Ano'])['Produção de gás natural (m³)'].sum()

dados = dados.reset_index()

#Fazendo o gráfico para a produção anual total
plt.figure(figsize = (10, 5))
plt.bar(dados.iloc[:, 0], dados.iloc[:, 1], color = 'yellow')
plt.xticks(dados['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção total de gás natural onshore/offshore em território brasileiro (2009 - 2018)')     
