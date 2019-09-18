import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore X offshore por estado, entre os anos de 2009 a 2018.'''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';')

'''Agora faremos a separação dos estados produtores onshore X offshore por estado.
   1) Faremos a separação dos estados produtores onshore e offshore usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
al= []
am = []
ba = []
ce = []
es = []
ma = []
rn = []
rj = []
se = []
sp = []

# 2º Passo
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

# 3º Passo
al = pd.DataFrame(list(al))
am = pd.DataFrame(list(am))
ba = pd.DataFrame(list(ba))
ce = pd.DataFrame(list(ce))
es = pd.DataFrame(list(es))
ma = pd.DataFrame(list(ma))
rn = pd.DataFrame(list(rn))
rj = pd.DataFrame(list(rj))
se = pd.DataFrame(list(se))
sp = pd.DataFrame(list(sp))

# 4º Passo
al.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
am.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
ba.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
ce.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
es.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
ma.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
rn.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
rj.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
se.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
sp.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
al['Produção de gás natural (milhões m3)'] = al['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
am['Produção de gás natural (milhões m3)'] = am['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
ba['Produção de gás natural (milhões m3)'] = ba['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
ce['Produção de gás natural (milhões m3)'] = ce['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
es['Produção de gás natural (milhões m3)'] = es['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
ma['Produção de gás natural (milhões m3)'] = ma['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
rn['Produção de gás natural (milhões m3)'] = rn['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
rj['Produção de gás natural (milhões m3)'] = rj['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
se['Produção de gás natural (milhões m3)'] = se['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
sp['Produção de gás natural (milhões m3)'] = sp['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
al['Produção de gás natural (milhões m3)'] = al['Produção de gás natural (milhões m3)'].mul(1000000)
am['Produção de gás natural (milhões m3)'] = am['Produção de gás natural (milhões m3)'].mul(1000000)
ba['Produção de gás natural (milhões m3)'] = ba['Produção de gás natural (milhões m3)'].mul(1000000)
ce['Produção de gás natural (milhões m3)'] = ce['Produção de gás natural (milhões m3)'].mul(1000000)
es['Produção de gás natural (milhões m3)'] = es['Produção de gás natural (milhões m3)'].mul(1000000)
ma['Produção de gás natural (milhões m3)'] = ma['Produção de gás natural (milhões m3)'].mul(1000000)
rn['Produção de gás natural (milhões m3)'] = rn['Produção de gás natural (milhões m3)'].mul(1000000)
rj['Produção de gás natural (milhões m3)'] = rj['Produção de gás natural (milhões m3)'].mul(1000000)
se['Produção de gás natural (milhões m3)'] = se['Produção de gás natural (milhões m3)'].mul(1000000)
sp['Produção de gás natural (milhões m3)'] = sp['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
al = al.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
am = am.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
ba = ba.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
ce = ce.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
es = es.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
ma = ma.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
rn = rn.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
rj = rj.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
se = se.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
sp = sp.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Agora faremos a soma total da produção de todos os produtores onshore e offshore para cada ano, e transforma-los em dataframe.
al = al.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
am = am.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
ba = ba.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
ce = ce.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
es = es.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
ma = ma.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
rn = rn.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
rj = rj.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
se = se.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
sp = sp.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()

#Adicionar uma coluna com todos os anos, igualando aos valores somados anteriormente
al['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
am['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
ba['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
ce['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
es['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
ma['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
rn['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
rj['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
se['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
sp['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

#Fazendo o gráfico para o estado de Alagoas
plt.bar(al.iloc[:, 1], al.iloc[:, 0], color = 'orange')
plt.xticks(al['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de gás natural total no estado de Alagoas (2009 - 2018)')

#Fazendo o gráfico para o estado do Amazonas
plt.bar(am.iloc[:, 1], am.iloc[:, 0], color = 'red')
plt.xticks(am['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total no estado do Amazonas (2009 - 2018)')

#Fazendo o gráfico para o estado da Bahia
plt.bar(ba.iloc[:, 1], ba.iloc[:, 0], color = 'yellow')
plt.xticks(ba['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total no estado da Bahia (2009 - 2018)')

#Fazendo o gráfico para o estado do Ceará
plt.bar(ce.iloc[:, 1], ce.iloc[:, 0], color = 'blue')
plt.xticks(ce['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^7 m³)')
plt.title('Produção de gás natural total no estado da Bahia (2009 - 2018)')

#Fazendo o gráfico para o estado do Espírito Santo
plt.bar(es.iloc[:, 1], es.iloc[:, 0], color = 'green')
plt.xticks(es['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total no estado do Esírito Santo (2009 - 2018)')

#Fazendo o gráfico para o estado do Maranhão
plt.bar(ma.iloc[:, 1], ma.iloc[:, 0], color = 'brown')
plt.xticks(ma['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total no estado de Alagoas (2009 - 2018)')

#Fazendo o gráfico para o estado do Rio Grande do Norte
plt.bar(rn.iloc[:, 1], rn.iloc[:, 0], color = 'black')
plt.xticks(rn['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^8 m³)')
plt.title('Produção de gás natural total no estado do Rio Grande do Norte (2009 - 2018)')

#Fazendo o gráfico para o estado do Rio de Janeiro
plt.bar(rj.iloc[:, 1], rj.iloc[:, 0], color = 'purple')
plt.xticks(rj['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total no estado do Rio de Janeiro (2009 - 2018)')

#Fazendo o gráfico para o estado de Sergipe
plt.bar(se.iloc[:, 1], se.iloc[:, 0], color = 'pink')
plt.xticks(se['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total no estado de Sergipe (2009 - 2018)')

#Fazendo o gráfico para o estado de São Paulo
plt.bar(sp.iloc[:, 1], sp.iloc[:, 0], color = 'violet')
plt.xticks(sp['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total no estado de São Paulo (2009 - 2018)')

'''Explicando os parâmetros para explicar os gráficos acima:
    xticks() - Com ele definimos as labels do eixo X, ele precisa de um parâmetro com tipo de array que determine as labels.
    xlabel() e ylabel() - Com estes dois métodos adicionamos as labels do eixo Y e X, respectivamente.
    title() - adiciona o título do gráfico.
    plt.bar() - este método da lib plt, inicia a construsção do gráfico de barra, e aí começamos a passar os argumentos, que em ordem são:
            x: As coordernadas das barras do eixo X, que no nosso caso são as faixas etárias;
            height: A ‘altura’ das barras, valores que vão dimensionar as mesmas, no nosso caso o array de renda média;
            color: Um argumento opicional que determina a cor das barras.'''
            
#Fazendo o gráfico com todos os estados produtores de gás natural (offshore e onshore)
barWidth = 0.08
plt.figure(figsize = (10, 5))
r1 = np.arange(len(al.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
r6 = [x + barWidth for x in r5]
r7 = [x + barWidth for x in r6]
r8 = [x + barWidth for x in r7]
r9 = [x + barWidth for x in r8]
r10 = [x + barWidth for x in r9]
plt.bar(r1, al.iloc[:, 0], color = '#2F4F4F', width = barWidth, label = 'AL')
plt.bar(r2, am.iloc[:, 0], color = '#00FA9A', width = barWidth, label = 'AM')
plt.bar(r3, ba.iloc[:, 0], color = '#00FF7F', width = barWidth, label = 'BA')
plt.bar(r4, ce.iloc[:, 0], color = '#98FB98', width = barWidth, label = 'CE')
plt.bar(r5, es.iloc[:, 0], color = '#90EE90', width = barWidth, label = 'ES')
plt.bar(r6, ma.iloc[:, 0], color = '#8FBC8F', width = barWidth, label = 'MA')
plt.bar(r7, rn.iloc[:, 0], color = '#3CB371', width = barWidth, label = 'RN')
plt.bar(r8, rj.iloc[:, 0], color = '#2E8B57', width = barWidth, label = 'RJ')
plt.bar(r9, se.iloc[:, 0], color = '#006400', width = barWidth, label = 'SE')
plt.bar(r10, ba.iloc[:, 0], color = '#008000', width = barWidth, label = 'SP')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(al.iloc[:, 0]))], al['Ano'])
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total (onshore/offshore) entre os estados produtores (2009 - 2018)')
plt.legend(loc = 'upper left')
plt.show()

'''Explicando os parâmetros para plotar o gráfico:
   barwidth - dimensiona o tamanho da largura das barras.
   plt.figure(figsize) - aumenta o gráfico para termos uma melhor visualização dos dados.
   r1, r2, r3, r4, r5, r6, r7, r8, r9, r10 - Com estas variáveis é possível ter uma barra do lado da outra, primeiramente
   é checada a largura da primeira barra e depois de forma incremental se posicionam as 
   outras, pela referência das larguras das anteriores.
   Com este método que é construída a barra, com diferencial que adicionamos as variáveis
   que representam as posições (r1, r2, r3, r4, r5, r6, r7, r8, r9, r10) como argumento, e também a largura das barras (barWidth).
   xticks() - Embora já termos o utilizado para adicionar labels no eixo X, neste tipo de gráfico
   há uma particularidade, há um for loop que distribui as legendas uniformemente em cada um dos grupos.
   title() -  Adiciona o título do gráfico.
   legend() - Cria uma legenda para o gráfico.
   show() - Por fim, show mostra o gráfico na tela.'''