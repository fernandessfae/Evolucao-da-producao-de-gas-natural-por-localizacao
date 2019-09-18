import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore X offshore por região, entre os anos de 2009 a 2018.'''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';')

'''Agora faremos a separação dos estados produtores onshore X offshore por região.
   1) Faremos a separação dos estados produtores onshore e offshore usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
nordeste= []
norte = []
sudeste = []

# 2º Passo
for index, column in dados.iterrows():
    if column['UF'] == 'Alagoas' or column['UF'] == 'Bahia' or column['UF'] == 'Ceará' or column['UF'] == 'Maranhão' or column['UF'] == 'Rio Grande do Norte' or column['UF'] == 'Sergipe':
        ne = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        nordeste.append(ne)
    elif column['UF'] == 'Espírito Santo' or column['UF'] == 'Rio de Janeiro' or column['UF'] == 'São Paulo':
        se = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        sudeste.append(se)
    else:
        n = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        norte.append(n)

# 3º Passo
nordeste = pd.DataFrame(list(nordeste))
norte = pd.DataFrame(list(norte))
sudeste = pd.DataFrame(list(sudeste))

# 4º Passo
nordeste.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
norte.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
sudeste.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']

# Com ambos os comandos, iremos ver o tipo de cada coluna
print(nordeste.dtypes)
print(norte.dtypes)
print(sudeste.dtypes)

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
nordeste['Produção de gás natural (milhões m3)'] = nordeste['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
norte['Produção de gás natural (milhões m3)'] = norte['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
sudeste['Produção de gás natural (milhões m3)'] = sudeste['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
nordeste['Produção de gás natural (milhões m3)'] = nordeste['Produção de gás natural (milhões m3)'].mul(1000000)
norte['Produção de gás natural (milhões m3)'] = norte['Produção de gás natural (milhões m3)'].mul(1000000)
sudeste['Produção de gás natural (milhões m3)'] = sudeste['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
nordeste = nordeste.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
norte = norte.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
sudeste = sudeste.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Agora faremos a soma total da produção de todos os produtores onshore e offshore para cada ano, e transforma-los em dataframe.
nordeste = nordeste.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
norte = norte.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
sudeste = sudeste.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()

#Adicionar uma coluna com todos os anos, igualando aos valores somados anteriormente
nordeste['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
norte['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
sudeste['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

#Fazendo o gráfico para a região nordeste
plt.bar(nordeste.iloc[:, 1], nordeste.iloc[:, 0], color = 'orange')
plt.xticks(nordeste['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total na região nordeste (2009 - 2018)')

#Fazendo o gráfico para a região norte
plt.bar(norte.iloc[:, 1], norte.iloc[:, 0], color = 'green')
plt.xticks(nordeste['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total na região norte(2009 - 2018)')

#Fazendo o gráfico para a região sudeste
plt.bar(sudeste.iloc[:, 1], sudeste.iloc[:, 0], color = 'yellow')
plt.xticks(nordeste['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total na região sudeste (2009 - 2018)')

'''Explicando os parâmetros para explicar os gráficos acima:
    xticks() - Com ele definimos as labels do eixo X, ele precisa de um parâmetro com tipo de array que determine as labels.
    xlabel() e ylabel() - Com estes dois métodos adicionamos as labels do eixo Y e X, respectivamente.
    title() - adiciona o título do gráfico.
    plt.bar() - este método da lib plt, inicia a construsção do gráfico de barra, e aí começamos a passar os argumentos, que em ordem são:
            x: As coordernadas das barras do eixo X, que no nosso caso são as faixas etárias;
            height: A ‘altura’ das barras, valores que vão dimensionar as mesmas, no nosso caso o array de renda média;
            color: Um argumento opicional que determina a cor das barras.'''

#Fazendo o gráfico para os produtos energéticos e não energéticos
barWidth = 0.25
plt.figure(figsize = (10, 5))
r1 = np.arange(len(nordeste.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
plt.bar(r1, nordeste.iloc[:, 0], color = '#9370DB', width = barWidth, label = 'Nordeste')
plt.bar(r2, norte.iloc[:, 0], color = '#8A2BE2', width = barWidth, label = 'Norte')
plt.bar(r3, sudeste.iloc[:, 0], color = '#4B0082', width = barWidth, label = 'Sudeste')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(nordeste.iloc[:, 0]))], nordeste['Ano'])
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total (onshore/offshore) entre as regiões produtoras (2009 - 2018)')
plt.legend()
plt.show() 

'''Explicando os parâmetros para plotar o gráfico:
   barwidth - dimensiona o tamanho da largura das barras.
   plt.figure(figsize) - aumenta o gráfico para termos uma melhor visualização dos dados.
   r1, r2, r3 - Com estas variáveis é possível ter uma barra do lado da outra, primeiramente
   é checada a largura da primeira barra e depois de forma incremental se posicionam as 
   outras, pela referência das larguras das anteriores.
   Com este método que é construída a barra, com diferencial que adicionamos as variáveis
   que representam as posições (r1,r2, r3) como argumento, e também a largura das barras (barWidth).
   xticks() - Embora já termos o utilizado para adicionar labels no eixo X, neste tipo de gráfico
   há uma particularidade, há um for loop que distribui as legendas uniformemente em cada um dos grupos.
   title() -  Adiciona o título do gráfico.
   legend() - Cria uma legenda para o gráfico.
   show() - Por fim, show mostra o gráfico na tela.'''
