import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

''' Aqui vamos fazer um histograma com a produção de gás natural offshore (por mar) de cada estado produtor, no Brasil.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

# Separação dos estados produtores de gás natural offshore
al, ba, ce, es, rn, rj, se, sp = ([] for i in range(8))

for index, row in dados.iterrows():
    if row['Localização'] == 'Mar' and row['UF'] == 'Alagoas':
        al.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'Bahia':
        ba.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'Ceará':
        ce.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'Espírito Santo':
        es.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'Rio Grande do Norte':
        rn.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'Rio de Janeiro':
        rj.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'Sergipe':
        se.append(row)
    elif row['Localização'] == 'Mar' and row['UF'] == 'São Paulo':
        sp.append(row)

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
    if x is al:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'blue', data = al)
        plt.title('Produção total de gás natural offshore no estado de Alagoas', fontsize = 16, fontweight = 'bold')
    elif x is ba:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'yellow', data = ba)
        plt.title('Produção total de gás natural offshore no estado da Bahia', fontsize = 16, fontweight = 'bold')
    elif x is ce:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'brown', data = ce)
        plt.title('Produção total de gás natural offshore no estado do Ceará', fontsize = 16, fontweight = 'bold')
    elif x is es:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'red', data = es)
        plt.title('Produção total de gás natural offshore no estado do Espírito Santo', fontsize = 16, fontweight = 'bold')
    elif x is rn:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'green', data = rn)
        plt.title('Produção total de gás natural offshore no estado do Rio Grande do Norte', fontsize = 16, fontweight = 'bold')
    elif x is rj:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'gray', data = rj)
        plt.title('Produção total de gás natural offshore no estado do Rio de Janeiro', fontsize = 16, fontweight = 'bold')
    elif x is se:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'purple', data = se)
        plt.title('Produção total de gás natural offshore no estado de Sergipe', fontsize = 16, fontweight = 'bold')
    elif x is sp:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'pink', data = sp)
        plt.title('Produção total de gás natural offshore no estado de São Paulo', fontsize = 16, fontweight = 'bold')

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
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 3]))], al['Ano'])
plt.ylabel('Quantidade (m³)')
plt.title('Produção total de gás natural dos estados produtores offshore', fontsize = 16, fontweight = 'bold')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show() 
