import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

'''Aqui vamos usar um método de classificação usando o KNN, para saber como o computador irá dizer qual grupo pertence localização das plataformas de gás natural. '''

#Carregamento da base de dados
dados = pd.read_csv('D:\\Meus Documentos\\Downloads\\Banco de dados\\Anuário Estatístico 2019 - Evolução da produção de gás natural, por localização.csv', sep = ';')

#Criaremos uma lista para adicionar os numeros para a variável localização -> terra = 0 , mar = 1
numeros = []

#Aqui foi criado um laço para atribuir um número para o nome terra e mar
for index, column in dados.iterrows():
    if column['Localização'] == 'Terra':
        numeros.append(0)
    else:
        numeros.append(1)

#Criaremos uma nova coluna 'Números da localização' no dataframe 'dados'
dados['Números da localização'] = numeros

#Precisaremos fazer a transformação dos números da coluna 'Produção de gás natural (milhões m3)' para o tipo float, pelo fato do python não reconhecer a ',' como elemento separador de número.
dados['Produção de gás natural (milhões m3)'] = dados['Produção de gás natural (milhões m3)'].str.replace(",", ".").astype(float)

#Multiplicar a coluna ['Produção de gás natural (milhões m3'] por 1000000.
dados['Produção de gás natural (milhões m3)'] = dados['Produção de gás natural (milhões m3)'].mul(1000000)

#Renomear a 'Produção de gás natural (milhões m3)' por ''Produção de gás natural (m3)''
dados = dados.rename(columns = {'Produção de gás natural (milhões m3)' : 'Produção de gás natural (m³)'})

#Criação de uma variável com variáveis independentes(x)
previsores = dados.iloc[:, [0, 3]].values

#Criação de uma variável com variável de resposta(y)
classe = dados.iloc[:, 4].values

#Aqui iremos transformar as colunas categóricas em colunas numéricas
labelencoder = LabelEncoder()
previsores[:, 0] = labelencoder.fit_transform(previsores[:, 0])

#Aqui hávera a divisão dos dados para treinamento e teste passando como parâmetros(variavel independente, variável resposta, a amostra de teste[0 até 1] e divisao da base de dados igual)
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.2, random_state = 0)

#Faz a previsão do algoritmo knn usando a base de teste
knn = KNeighborsClassifier(n_neighbors = 2)
knn.fit(X_treinamento, y_treinamento)

#Faz a previsão do algoritmo knn usando a base de teste
previsoes = knn.predict(X_teste)

#Cria uma matriz de confusão nessa variável
confusao = confusion_matrix(y_teste, previsoes)

#Cria variáveis com a taxa de acerto e erro
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

'''Obs: Para efeito de comparação, decidi ajustar o test_size para ver quais valores seriam melhor para o teste de predição da máquina, e o resultado foi esse:
    
         Como constatado, a taxa de acerto foi 62.5%, com 30% de dados para teste.
         Como constatado, a taxa de acerto foi 61.7%, aproximadamente, com 29% de dados para teste.
         Como constatado, a taxa de acerto foi 62.2%, aproximadamente, com 28% de dados para teste.
         Como constatado, a taxa de acerto foi 63.6%, aproximadamente, com 27% de dados para teste.
         Como constatado, a taxa de acerto foi 66.7%, aproximadamente, com 26% de dados para teste.
         Como constatado, a taxa de acerto foi 65.0%, com 25% de dados para teste.
         Como constatado, a taxa de acerto foi 64.1%, aproximadamente, com 24% de dados para teste.
         Como constatado, a taxa de acerto foi 62.2%, aproximadamente, com 23% de dados para teste.
         Como constatado, a taxa de acerto foi 63.9%, aproximadamente, com 22% de dados para teste.
         Como constatado, a taxa de acerto foi 64.7%, aproximadamente, com 21% de dados para teste.
         Como constatado, a taxa de acerto foi 62.5%, com 20% de dados para teste.
         
         Como constatado, o melhor resultado da máquina foi um valor de 0.26(26%) dos dados para o teste e 0.74(74%) dos dados para treinamento. A conclusão que, nesse caso
         nem sempre a maior quantidade de dados para teste obteve um melhor resultado. Isso mostra que os dados tem que ser ajustados ao ponto máximo da performance dele, nem para mais, nem para menos.'''