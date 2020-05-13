import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore e offshore por estado, entre os anos de 2009 a 2018.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

#Separação da produção total de gás natural de cada estado (onshore e offshore)
al, am, ba, ce, es, ma, rn, rj, se, sp = ([] for i in range(10))

for index, column in dados.iterrows():
    if column['UF'] == 'Alagoas':
        ala = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        al.append(ala)
    elif column['UF'] == 'Amazonas':
        ama = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        am.append(ama)
    elif column['UF'] == 'Bahia':
        bah = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ba.append(bah)
    elif column['UF'] == 'Ceará':
        cea = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ce.append(cea)
    elif column['UF'] == 'Espírito Santo':
        esp = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        es.append(esp)
    elif column['UF'] == 'Maranhão':
        mar = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ma.append(mar)
    elif column['UF'] == 'Rio Grande do Norte':
        rnn = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        rn.append(rnn)
    elif column['UF'] == 'Rio de Janeiro':
        rje = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        rj.append(rje)
    elif column['UF'] == 'Sergipe':
        ser = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        se.append(ser)
    elif column['UF'] == 'São Paulo':
        sao = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        sp.append(sao)

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
        plt.xlabel('Produção gás natural anual')
        plt.ylabel('Total Produção Anual (m³)')
        if x is al:            
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'orange')
            plt.title('Produção de gás natural total no estado de Alagoas')
        elif x is am:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'brown')
            plt.title('Produção de gás natural total no estado do Amazonas')
        elif x is ba:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'yellow')
            plt.title('Produção de gás natural total no estado da Bahia')
        elif x is ce:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'blue')
            plt.title('Produção de gás natural total no estado do Ceará')
        elif x is es:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'red')
            plt.title('Produção de gás natural total no estado do Espírito Santo')
        elif x is ma:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'green')
            plt.title('Produção de gás natural total no estado do Maranhão')
        elif x is rn:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'gray')
            plt.title('Produção de gás natural total no estado do Rio Grande do Norte')
        elif x is rj:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'pink')
            plt.title('Produção de gás natural total no estado do Rio de Janeiro')
        elif x is se:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'purple')
            plt.title('Produção de gás natural total no estado de Sergipe')
        else:
            plt.bar(x.iloc[:, 0], x.iloc[:, 1], color = 'black')
            plt.title('Produção de gás natural total no estado de São Paulo')

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
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 0]))], al['Ano'])
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total (onshore/offshore) entre os estados produtores (2009 - 2018)')
plt.legend(loc = 'upper left')
plt.show()
