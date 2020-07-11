import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

''' Aqui vamos fazer um histograma com a produção de gás natural onshore (por terra) de cada estado produtor, no Brasil.'''

dados = pd.read_csv('Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';', decimal = ',')

# Separação dos estados produtores de gás natural onshore
al, am, ba, ce, es, ma, rn, se = ([] for i in range(8))
    
for index, row in dados.iterrows():
    if row['Localização'] == 'Terra' and row['UF'] == 'Alagoas':
        al.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Amazonas':
        am.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Bahia':
        ba.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Ceará':
        ce.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Espírito Santo':
        es.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Maranhão':
        ma.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Rio Grande do Norte':
        rn.append(row)
    elif row['Localização'] == 'Terra' and row['UF'] == 'Sergipe':
        se.append(row)

#Criação da função de dataframe de cada estado
def novo_dataframe(n):
    n = pd.DataFrame(list(n))
    n.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
    n['Produção de gás natural (milhões m3)'] = n['Produção de gás natural (milhões m3)'].mul(1000000)
    n = n.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
    return n

#Tranformação das listas em dataframes
al = novo_dataframe(al)
am = novo_dataframe(am)
ba = novo_dataframe(ba)
ce = novo_dataframe(ce)
es = novo_dataframe(es)
ma = novo_dataframe(ma)
rn = novo_dataframe(rn)
se = novo_dataframe(se)

#Criação da função de histogramas para a produção onshore de cada estado
def histograma(x):
    plt.figure(figsize = (10, 5))
    plt.xticks(x['Ano'])
    if x is al:        
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'brown', data = al)
        plt.title('Produção total de gás natural onshore no estado de Alagoas', fontsize = 16, fontweight = 'bold')
    elif x is am:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'blue', data = am)
        plt.title('Produção total de gás natural onshore no estado do Amazonas', fontsize = 16, fontweight = 'bold')
    elif x is ba:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'yellow', data = ba)
        plt.title('Produção total de gás natural onshore no estado da Bahia', fontsize = 16, fontweight = 'bold')
    elif x is ce:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'red', data = ce)
        plt.title('Produção total de gás natural onshore no estado do Ceará', fontsize = 16, fontweight = 'bold')
    elif x is es:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'green', data = es)
        plt.title('Produção total de gás natural onshore no estado do Espírito Santo', fontsize = 16, fontweight = 'bold')
    elif x is ma:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'gray', data = ma)
        plt.title('Produção total de gás natural onshore no estado do Maranhão', fontsize = 16, fontweight = 'bold')
    elif x is rn:
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'pink', data = rn)
        plt.title('Produção total de gás natural onshore no estado do Rio Grande do Norte', fontsize = 16, fontweight = 'bold')
    elif x is se:      
        sns.barplot(x = 'Ano', y = 'Produção de gás natural (m³)', color = 'purple', data = se)
        plt.title('Produção de gás natural onshore no estado de Sergipe', fontsize = 16, fontweight = 'bold')
    plt.show()

#Visualização dos gráficos        
histograma(al)
histograma(am)
histograma(ba)
histograma(ce)
histograma(es)
histograma(ma)
histograma(rn)
histograma(se)

#Plotando o gráfico comparando todos os produtores de gás natural onshore
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
plt.bar(r1, al.iloc[:, 3], color = '#BDB76B', width = barWidth, label = 'AL')
plt.bar(r2, am.iloc[:, 3], color = '#DAA520', width = barWidth, label = 'AM')
plt.bar(r3, ba.iloc[:, 3], color = '#B8860B', width = barWidth, label = 'BA')
plt.bar(r4, ce.iloc[:, 3], color = '#8B4513', width = barWidth, label = 'CE')
plt.bar(r5, es.iloc[:, 3], color = '#A0522D', width = barWidth, label = 'ES')
plt.bar(r6, ma.iloc[:, 3], color = '#CD853F', width = barWidth, label = 'MA')
plt.bar(r7, rn.iloc[:, 3], color = '#D2691E', width = barWidth, label = 'RN')
plt.bar(r8, se.iloc[:, 3], color = '#F4A460', width = barWidth, label = 'SE')
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 3]))], al['Ano'])
plt.ylabel('Quantidade (m³)')
plt.title('Produção de gás natural dos estados produtores onshore', fontsize = 16, fontweight = 'bold')
plt.legend(loc = 'best')
plt.tight_layout()
plt.show()
