import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore e offshore por estado, entre os anos de 2009 a 2018.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

#Separação da produção total de gás natural de cada estado (onshore e offshore)
al, am, ba, ce, es, ma, rn, rj, se, sp = ([] for i in range(10))

for index, column in dados.iterrows():
    if column['UF'] == 'Alagoas':
        al.append(column)
    elif column['UF'] == 'Amazonas':
        am.append(column)
    elif column['UF'] == 'Bahia':
        ba.append(column)
    elif column['UF'] == 'Ceará':
        ce.append(column)
    elif column['UF'] == 'Espírito Santo':
        es.append(column)
    elif column['UF'] == 'Maranhão':
        ma.append(column)
    elif column['UF'] == 'Rio Grande do Norte':
        rn.append(column)
    elif column['UF'] == 'Rio de Janeiro':
        rj.append(column)
    elif column['UF'] == 'Sergipe':
        se.append(column)
    elif column['UF'] == 'São Paulo':
        sp.append(column)

#Criação dos dataframes da produção total de cada estado
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    n = n.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame().reset_index()
    return n

#Transformação das listas em dataframe
al = novo_dataframe(al)
am = novo_dataframe(am)
ba = novo_dataframe(ba)
ce = novo_dataframe(ce)
es = novo_dataframe(es)
ma = novo_dataframe(ma)
rn = novo_dataframe(rn)
rj = novo_dataframe(rj)
se = novo_dataframe(se)
sp = novo_dataframe(sp)

#Criação de uma função dos histogramas para a produção total de cada estado
def histograma(x):
        plt.figure(figsize = (10, 5))
        plt.xticks(x['Ano'])
        if x is al:            
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'orange', data = al)
            plt.title('Produção de gás natural total no estado de Alagoas', fontsize = 16, fontweight = 'bold')
        elif x is am:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'brown', data = am)
            plt.title('Produção de gás natural total no estado do Amazonas', fontsize = 16, fontweight = 'bold')
        elif x is ba:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'yellow', data = ba)
            plt.title('Produção de gás natural total no estado da Bahia', fontsize = 16, fontweight = 'bold')
        elif x is ce:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'blue', data = ce)
            plt.title('Produção de gás natural total no estado do Ceará', fontsize = 16, fontweight = 'bold')
        elif x is es:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'red', data = es)
            plt.title('Produção de gás natural total no estado do Espírito Santo', fontsize = 16, fontweight = 'bold')
        elif x is ma:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'green', data = ma)
            plt.title('Produção de gás natural total no estado do Maranhão', fontsize = 16, fontweight = 'bold')
        elif x is rn:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'gray', data = rn)
            plt.title('Produção de gás natural total no estado do Rio Grande do Norte', fontsize = 16, fontweight = 'bold')
        elif x is rj:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'pink', data = rj)
            plt.title('Produção de gás natural total no estado do Rio de Janeiro', fontsize = 16, fontweight = 'bold')
        elif x is se:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'purple', data = se)
            plt.title('Produção de gás natural total no estado de Sergipe', fontsize = 16, fontweight = 'bold')
        elif x is sp:
            sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'black', data = sp)
            plt.title('Produção de gás natural total no estado de São Paulo', fontsize = 16, fontweight = 'bold')

#Visualização dos gráficos
histograma(al)
histograma(am)
histograma(ba)
histograma(ce)
histograma(es)
histograma(ma)
histograma(rn)
histograma(rj)
histograma(se)
histograma(sp)
            
#Fazendo o gráfico com todos os estados produtores de gás natural (offshore e onshore)
barWidth = 0.08
plt.figure(figsize = (15, 5))
r1 = np.arange(len(al.iloc[:, 0]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
r9 = [x + barWidth for x in r8]
r10 = [x + barWidth for x in r9]
plt.bar(r1, al.iloc[:, 1], color = '#2F4F4F', width = barWidth, label = 'AL')
plt.bar(r2, am.iloc[:, 1], color = '#00FA9A', width = barWidth, label = 'AM')
plt.bar(r3, ba.iloc[:, 1], color = '#00FF7F', width = barWidth, label = 'BA')
plt.bar(r4, ce.iloc[:, 1], color = '#98FB98', width = barWidth, label = 'CE')
plt.bar(r5, es.iloc[:, 1], color = '#90EE90', width = barWidth, label = 'ES')
plt.bar(r6, ma.iloc[:, 1], color = '#8FBC8F', width = barWidth, label = 'MA')
plt.bar(r7, rn.iloc[:, 1], color = '#3CB371', width = barWidth, label = 'RN')
plt.bar(r8, rj.iloc[:, 1], color = '#2E8B57', width = barWidth, label = 'RJ')
plt.bar(r9, se.iloc[:, 1], color = '#006400', width = barWidth, label = 'SE')
plt.bar(r10, ba.iloc[:, 1], color = '#008000', width = barWidth, label = 'SP')
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 0]))], al['Ano'])
plt.ylabel('Produção Anual (m³)')
plt.title('Produção de gás natural total (onshore/offshore) entre os estados produtores', fontsize = 16, fontweight = 'bold')
plt.legend(loc = 'upper left')
plt.show()

# Top 5 maiores estados produtores de gás natural do Brasil
dados['Produção de gás natural (milhões m3)'] = dados['Produção de gás natural (milhões m3)'].mul(1000000)
dados = dados.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
dados = dados.groupby(['UF'])['Produção de gás natural (m³)'].sum().reset_index()

plt.figure(figsize = (10, 5))
plt.bar(dados.nlargest(5, 'Produção de gás natural (m³)')['UF'], dados.nlargest(5, 'Produção de gás natural (m³)')['Produção de gás natural (m³)'], color = plt.cm.Set3(np.arange(5)))
plt.title('Os 5 maiores estados brasileiros produtores de gás natural (2009 - 2018)', fontsize = 16, fontweight = 'bold')
plt.ylabel('Quantidade (m³)')
plt.show()
