import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural onshore (por terra) de cada estado produtor, no Brasil.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

# Separação dos estados produtores de gás natural onshore
al = []
am = []
ba = []
ce = []
es = []
ma = []
rn = []
se = []

for index, column in dados.iterrows():
    if column['Localização'] == 'Terra' and column['UF'] == 'Alagoas':
        ala = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        al.append(ala)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Amazonas':
        ama = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        am.append(ama)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Bahia':
        bah = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ba.append(bah)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Ceará':
        cea = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ce.append(cea)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Espírito Santo':
        esp = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        es.append(esp)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Maranhão':
        mar = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        ma.append(mar)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Rio Grande do Norte':
        rio = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        rn.append(rio)
    elif column['Localização'] == 'Terra' and column['UF'] == 'Sergipe':
        ser = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        se.append(ser)

#Criação dos dataframes de cada estado
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    return n

al = novo_dataframe(al)
am = novo_dataframe(am)
ba = novo_dataframe(ba)
ce = novo_dataframe(ce)
es = novo_dataframe(es)
ma = novo_dataframe(ma)
rn = novo_dataframe(rn)
se = novo_dataframe(se)

#Criação dos histogramas para a produção onshore de cada estado
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.bar(x.iloc[:, 2], x.iloc[:, 3], color = 'brown')
    plt.xticks(x['Ano'])
    plt.xlabel('Produção gás natural anual')
    plt.ylabel('Total Produção Anual (m³)')
    plt.title(f'Produção de gás natural onshore {x.iloc[0, 0]} (2009 - 2018)')

histograma(al)
histograma(am)
histograma(ba)
histograma(ce)
histograma(es)
histograma(ma)
histograma(rn)
histograma(se)

#Plotando o gráfico comparando todos os produtores de gás natural onshore entre os anos de 2009 a 2018
barWidth = 0.1
plt.figure(figsize = (10, 5))
r1 = np.arange(len(al.iloc[:, 2]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
plt.bar(r1, al.iloc[:, 3], color = '#BDB76B', width = barWidth, label = 'AL')
plt.bar(r2, am.iloc[:, 3], color = '#DAA520', width = barWidth, label = 'AM')
plt.bar(r3, ba.iloc[:, 3], color = '#B8860B', width = barWidth, label = 'BA')
plt.bar(r4, ce.iloc[:, 3], color = '#8B4513', width = barWidth, label = 'CE')
plt.bar(r5, es.iloc[:, 3], color = '#A0522D', width = barWidth, label = 'ES')
plt.bar(r6, ma.iloc[:, 3], color = '#CD853F', width = barWidth, label = 'MA')
plt.bar(r7, rn.iloc[:, 3], color = '#D2691E', width = barWidth, label = 'RN')
plt.bar(r8, se.iloc[:, 3], color = '#F4A460', width = barWidth, label = 'SE')
plt.xlabel('Produção gás natural (ano)')
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 3]))], al['Ano'])
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural dos estados produtores onshore (2009 - 2018)')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
