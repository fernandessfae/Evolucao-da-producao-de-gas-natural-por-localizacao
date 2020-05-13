import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural offshore (por mar) de cada estado produtor, no Brasil.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

# Separação dos estados produtores de gás natural offshore
al, ba, ce, es, rn, rj, se, sp = ([] for i in range(8))

for index, column in dados.iterrows():
    if column['Localização'] == 'Mar' and column['UF'] == 'Alagoas':
        ala = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        al.append(ala)
    elif column['Localização'] == 'Mar' and column['UF'] == 'Bahia':
        bah = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ba.append(bah)
    elif column['Localização'] == 'Mar' and column['UF'] == 'Ceará':
        cea = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ce.append(cea)
    elif column['Localização'] == 'Mar' and column['UF'] == 'Espírito Santo':
        esp = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        es.append(esp)
    elif column['Localização'] == 'Mar' and column['UF'] == 'Rio Grande do Norte':
        rng = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        rn.append(rng)
    elif column['Localização'] == 'Mar' and column['UF'] == 'Rio de Janeiro':
        rio = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        rj.append(rio)
    elif column['Localização'] == 'Mar' and column['UF'] == 'Sergipe':
        ser = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        se.append(ser)
    elif column['Localização'] == 'Mar' and column['UF'] == 'São Paulo':
        sao = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        sp.append(sao)

#Criação da função de dataframe de cada estado
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    return n

#Tranformação das listas em dataframes
al = novo_dataframe(al)
ba = novo_dataframe(ba)
ce = novo_dataframe(ce)
es = novo_dataframe(es)
rn = novo_dataframe(rn)
rj = novo_dataframe(rj)
se = novo_dataframe(se)
sp = novo_dataframe(sp)

#Criação dos histogramas para a produção offshore de cada estado
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    plt.xlabel('Produção gás natural anual')
    plt.ylabel('Quantidade (m³)')
    if x is al:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'blue')
        plt.title('Produção total de gás natural offshore no estado de Alagoas')
    elif x is ba:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'yellow')
        plt.title('Produção total de gás natural offshore no estado da Bahia')
    elif x is ce:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'brown')
        plt.title('Produção total de gás natural offshore no estado do Ceará')
    elif x is es:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'red')
        plt.title('Produção total de gás natural offshore no estado do Espírito Santo')
    elif x is rn:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'green')
        plt.title('Produção total de gás natural offshore no estado do Rio Grande do Norte')
    elif x is rj:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'gray')
        plt.title('Produção total de gás natural offshore no estado do Rio de Janeiro')
    elif x is se:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'purple')
        plt.title('Produção total de gás natural offshore no estado de Sergipe')
    else:
        plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'pink')
        plt.title(f'Produção total de gás natural offshore no estado de São Paulo')

#Visualização dos gráficos
histograma(al)
histograma(ba)
histograma(ce)
histograma(es)
histograma(rn)
histograma(rj)
histograma(se)
histograma(sp)

#Plotando o gráfico comparando todos os produtores de gás natural offshore
barWidth = 0.1
plt.figure(figsize = (15, 5))
r1 = np.arange(len(al.iloc[:, 2]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
plt.bar(r1, al.iloc[:, 3], color = '#00008B', width = barWidth, label = 'AL')
plt.bar(r2, ba.iloc[:, 3], color = '#0000CD', width = barWidth, label = 'BA')
plt.bar(r3, ce.iloc[:, 3], color = '#0000FF', width = barWidth, label = 'CE')
plt.bar(r4, es.iloc[:, 3], color = '#6495ED', width = barWidth, label = 'ES')
plt.bar(r5, rn.iloc[:, 3], color = '#4169E1', width = barWidth, label = 'RN')
plt.bar(r6, rj.iloc[:, 3], color = '#1E90FF', width = barWidth, label = 'RJ')
plt.bar(r7, se.iloc[:, 3], color = '#00BFFF', width = barWidth, label = 'SE')
plt.bar(r8, sp.iloc[:, 3], color = '#87CEFA', width = barWidth, label = 'SP')
plt.xlabel('Produção gás natural anual')
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 3]))], al['Ano'])
plt.ylabel('Quantidade (m³)')
plt.title('Produção total de gás natural dos estados produtores offshore')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
