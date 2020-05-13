import pandas as pd
import matplotlib.pyplot as plt

''' Aqui faremos um histograma com a produção total de gás natural (onshore/offshore) no Brasil entre 2009 a 2018.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')  

#Criação da função de dataframe nacional
def dataframe(x):
    x['Produção de gás natural (milhões m3)'] = x['Produção de gás natural (milhões m3)'].mul(1000000)
    x = x.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    x = x.groupby(['Ano'])['Produção de gás natural (m³)'].sum().reset_index()

#Alteração do dataframe nacional
dataframe(dados)

#Fazendo o gráfico para a produção anual total
plt.figure(figsize = (15, 5))
plt.bar(dados.iloc[:, 2], dados.iloc[:, 3], color = 'yellow')
plt.xlabel('Produção Anual')
plt.ylabel('Quantidade (m³)')
plt.title('Produção total de gás natural onshore/offshore em território brasileiro (2009 - 2018)')
