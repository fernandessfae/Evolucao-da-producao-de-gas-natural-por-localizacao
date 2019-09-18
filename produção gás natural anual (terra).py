import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural onshore (por terra) de cada estado produtor, no Brasil.'''

dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';')

'''Agora faremos a separação dos estados produtores de gás natural onshore.
   1) Faremos a colocação dos estados produtores onshore uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
al = []
am = []
ba = []
ce = []
es = []
ma = []
rn = []
se = []

# 2º Passo
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

# 3º Passo
al = pd.DataFrame(list(al))
am = pd.DataFrame(list(am))
ba = pd.DataFrame(list(ba))
ce = pd.DataFrame(list(ce))
es = pd.DataFrame(list(es))
ma = pd.DataFrame(list(ma))
rn = pd.DataFrame(list(rn))
se = pd.DataFrame(list(se))

# 4º Passo
al.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
am.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
ba.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
ce.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
es.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
ma.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
rn.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
se.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
al['Produção de gás natural (milhões m3)'] = al['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
am['Produção de gás natural (milhões m3)'] = am['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
ba['Produção de gás natural (milhões m3)'] = ba['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
ce['Produção de gás natural (milhões m3)'] = ce['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
es['Produção de gás natural (milhões m3)'] = es['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
ma['Produção de gás natural (milhões m3)'] = ma['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
rn['Produção de gás natural (milhões m3)'] = rn['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
se['Produção de gás natural (milhões m3)'] = se['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
al['Produção de gás natural (milhões m3)'] = al['Produção de gás natural (milhões m3)'].mul(1000000)
am['Produção de gás natural (milhões m3)'] = am['Produção de gás natural (milhões m3)'].mul(1000000)
ba['Produção de gás natural (milhões m3)'] = ba['Produção de gás natural (milhões m3)'].mul(1000000)
ce['Produção de gás natural (milhões m3)'] = ce['Produção de gás natural (milhões m3)'].mul(1000000)
es['Produção de gás natural (milhões m3)'] = es['Produção de gás natural (milhões m3)'].mul(1000000)
ma['Produção de gás natural (milhões m3)'] = ma['Produção de gás natural (milhões m3)'].mul(1000000)
rn['Produção de gás natural (milhões m3)'] = rn['Produção de gás natural (milhões m3)'].mul(1000000)
se['Produção de gás natural (milhões m3)'] = se['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
al = al.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
am = am.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
ba = ba.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
ce = ce.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
es = es.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
ma = ma.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
rn = rn.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
se = se.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Plotando o gráfico da produção onshore do estado de Alagoas
plt.bar(al.iloc[:, 2], al.iloc[:, 3], color = 'blue')
plt.xticks(al['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de gás natural onshore do estado de Alagoas (2009 - 2018)')

#Plotando o gráfico da produção onshore do estado da Amazonas
plt.bar(am.iloc[:, 2], am.iloc[:, 3], color = 'red')
plt.xticks(am['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural onshore do estado da Amazonas (2009 - 2018)')

#Plotando o gráfico da produção onshore do estado da Bahia
plt.bar(ba.iloc[:, 2], ba.iloc[:, 3], color = 'yellow')
plt.xticks(ba['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural onshore do estado da Bahia (2009 - 2018)')

#Plotando o gráfico da produção onshore do estado do Ceará
plt.bar(ce.iloc[:, 2], ce.iloc[:, 3], color = 'orange')
plt.xticks(ce['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (m³)')
plt.title('Produção de gás natural onshore do estado do Ceará (2009 - 2018)') 

#Plotando o gráfico da produção onshore do estado do Espírito Santo
plt.bar(es.iloc[:, 2], es.iloc[:, 3], color = 'green')
plt.xticks(es['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de gás natural onshore do estado do Espírito Santo (2009 - 2018)')

#Plotando o gráfico da produção onshore do estado do Maranhão
plt.bar(ma.iloc[:, 2], ma.iloc[:, 3], color = 'brown')
plt.xticks(ma['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural onshore do estado do Maranhão (2009 - 2018)')

#Plotando o gráfico da produção onshore do estado do Rio Grande do Norte
plt.bar(rn.iloc[:, 2], rn.iloc[:, 3], color = 'black')
plt.xticks(rn['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de gás natural onshore do estado do Rio Grande do Norte (2009 - 2018)')

#Plotando o gráfico da produção onshore do estado de Sergipe
plt.bar(se.iloc[:, 2], se.iloc[:, 3], color = 'purple')
plt.xticks(se['Ano'])
plt.xlabel('Produção gás natural anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de gás natural onshore do estado de Sergipe (2009 - 2018)')

'''Explicando os parâmetros para explicar os gráficos acima:
    xticks() - Com ele definimos as labels do eixo X, ele precisa de um parâmetro com tipo de array que determine as labels.
    xlabel() e ylabel() - Com estes dois métodos adicionamos as labels do eixo Y e X, respectivamente.
    title() - adiciona o título do gráfico.
    plt.bar() - este método da lib plt, inicia a construsção do gráfico de barra, e aí começamos a passar os argumentos, que em ordem são:
            x: As coordernadas das barras do eixo X, que no nosso caso são as faixas etárias;
            height: A ‘altura’ das barras, valores que vão dimensionar as mesmas, no nosso caso o array de renda média;
            color: Um argumento opicional que determina a cor das barras.'''

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

'''Explicando os parâmetros para plotar o gráfico:
   barwidth - dimensiona o tamanho da largura das barras.
   plt.figure(figsize) - aumenta o gráfico para termos uma melhor visualização dos dados.
   r1, r2, r3, r4, r5, r6, r7, r8 - Com estas variáveis é possível ter uma barra do lado
   da outra, primeiramente é checada a largura da primeira barra e depois de forma incremental
   se posicionam as outras, pela referência das larguras das anteriores.
   bar() - Com este método que é construída a barra, com diferencial que adicionamos as variáveis
   que representam as posições (r1,r2, r3, r4, r5, r6, r7, r8) como argumento, e também a largura das barras (barWidth).
   xticks() - Embora já termos o utilizado para adicionar labels no eixo X, neste tipo de gráfico
   há uma particularidade, há um for loop que distribui as legendas uniformemente em cada um dos grupos.
   title() -  Adiciona o título do gráfico.
   legend() - Cria uma legenda para o gráfico.
   show() - Por fim, show mostra o gráfico na tela.'''        