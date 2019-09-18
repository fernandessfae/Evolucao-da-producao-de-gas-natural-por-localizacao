import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

''' Aqui vamos fazer um histograma com a produção de gás natural total onshore X offshore, entre os anos de 2009 a 2018.'''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';')

'''Agora faremos a separação dos estados produtores onshore X offshore.
   1) Faremos a separação dos estados produtores onshore e offshore usando uma lista para colocarmos num laço.
   2) Iremos ajustar os novos dataframes desmembrado do dataframe inicial
   3) Transformaremos as listas em novos dataframes
   4) Alteração nos nomes das colunas para o mesmo do dataframe inicial'''

# 1º Passo
terra = []
mar = []

# 2º Passo
for index, column in dados.iterrows():
    if column['Localização'] == 'Terra':
        t = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        terra.append(t)
    else:
        m = column['UF'], column['Localização'], column['Ano'], column['Produção de gás natural (milhões m3)']
        mar.append(m)

# 3º Passo
terra = pd.DataFrame(list(terra))
mar = pd.DataFrame(list(mar))

# 4º Passo
terra.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']
mar.columns = ['UF', 'Localização', 'Ano', 'Produção de gás natural (milhões m3)']

# Com ambos os comandos, iremos ver o tipo de cada coluna
print(terra.dtypes)
print(mar.dtypes)

#Precisaremos fazer a transformação dos números da coluna 'produção (m³)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
terra['Produção de gás natural (milhões m3)'] = terra['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)
mar['Produção de gás natural (milhões m3)'] = mar['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
terra['Produção de gás natural (milhões m3)'] = terra['Produção de gás natural (milhões m3)'].mul(1000000)
mar['Produção de gás natural (milhões m3)'] = mar['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
terra = terra.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})
mar = mar.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Agora faremos a soma total da produção de todos os produtos energéticos e não energéticos para cada ano, e transforma-los em dataframe.
terra = terra.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()
mar = mar.groupby(['Ano'])['Produção de gás natural (m³)'].sum().to_frame()

#Adicionar uma coluna com todos os anos, igualando aos valores somados anteriormente
terra['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
mar['Ano'] = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

#Fazendo o gráfico para todos os estados produtores de gás natural onshore
plt.bar(terra.iloc[:, 1], terra.iloc[:, 0], color = 'brown')
plt.xticks(terra['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^9 m³)')
plt.title('Produção de gás natural total onshore dos estados produtores (2009 - 2018)')

#Fazendo o gráfico para todos os estados produtores de gás natural offshore
plt.bar(mar.iloc[:, 1], mar.iloc[:, 0], color = 'blue')
plt.xticks(mar['Ano'])
plt.xlabel('Produção Anual')
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural total offshore dos estados produtores (2009 - 2018)')

'''Explicando os parâmetros para explicar os gráficos acima:
    xticks() - Com ele definimos as labels do eixo X, ele precisa de um parâmetro com tipo de array que determine as labels.
    xlabel() e ylabel() - Com estes dois métodos adicionamos as labels do eixo Y e X, respectivamente.
    title() - adiciona o título do gráfico.
    plt.bar() - este método da lib plt, inicia a construsção do gráfico de barra, e aí começamos a passar os argumentos, que em ordem são:
            x: As coordernadas das barras do eixo X, que no nosso caso são as faixas etárias;
            height: A ‘altura’ das barras, valores que vão dimensionar as mesmas, no nosso caso o array de renda média;
            color: Um argumento opicional que determina a cor das barras.'''

#Fazendo o gráfico para os produtos energéticos e não energéticos
barWidth = 0.4
plt.figure(figsize = (10, 5))
r1 = np.arange(len(terra.iloc[:, 1]))
r2 = [x + barWidth for x in r1]
plt.bar(r1, terra.iloc[:, 0], color = '#8B4513', width = barWidth, label = 'Onshore')
plt.bar(r2, mar.iloc[:, 0], color = '#0000FF', width = barWidth, label = 'Offshore')
plt.xlabel('Produção Anual')
plt.xticks([r + barWidth for r in range(len(terra.iloc[:, 0]))], terra['Ano'])
plt.ylabel('Total Produção Anual (10^10 m³)')
plt.title('Produção de gás natural dos estados produtores onshore e offshore (2009 - 2018)')
plt.legend()
plt.show() 

'''Explicando os parâmetros para plotar o gráfico:
   barwidth - dimensiona o tamanho da largura das barras.
   plt.figure(figsize) - aumenta o gráfico para termos uma melhor visualização dos dados.
   r1, r2 - Com estas variáveis é possível ter uma barra do lado da outra, primeiramente
   é checada a largura da primeira barra e depois de forma incremental se posicionam as 
   outras, pela referência das larguras das anteriores.
   Com este método que é construída a barra, com diferencial que adicionamos as variáveis
   que representam as posições (r1,r2) como argumento, e também a largura das barras (barWidth).
   xticks() - Embora já termos o utilizado para adicionar labels no eixo X, neste tipo de gráfico
   há uma particularidade, há um for loop que distribui as legendas uniformemente em cada um dos grupos.
   title() -  Adiciona o título do gráfico.
   legend() - Cria uma legenda para o gráfico.
   show() - Por fim, show mostra o gráfico na tela.''' 