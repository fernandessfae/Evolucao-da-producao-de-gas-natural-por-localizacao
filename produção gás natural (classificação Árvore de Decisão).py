import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

'''Aqui vamos usar um método de classificação usando o Árvore de Decisão, para saber como o computador irá dizer qual a localização das plataformas de gás natural. '''

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
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(previsores, classe, test_size = 0.35, random_state = 0)

#Criação do algoritmo da árvore de decisão, juntamente com o treinamento do algoritmo
arvore = DecisionTreeClassifier()
arvore.fit(X_treinamento, y_treinamento)

#Gera um arquivo de texto no diretório específico onde o código está salvo, copia o texto que foi gerado e cola na aba lá presente no site webgraphviz.com para gerar a árvore.
export_graphviz(arvore, out_file = 'tree.dot')

#Faz as previsões da variável teste.
previsoes = arvore.predict(X_teste)

#Gera uma variável com a matriz de confusão
confusao = confusion_matrix(y_teste, previsoes)

#Gera duas variáveis com as taxas de acertos e erros da árvore de decisão
taxa_acerto = accuracy_score(y_teste, previsoes)
taxa_erro = 1 - taxa_acerto

'''Obs: Para efeito de comparação, decidi ajustar o test_size para ver quais valores seriam melhor para o teste de predição da máquina, e o resultado foi esse:
    
         Como constatado, a taxa de acerto foi 94.6%, aproximadamente, com 35% de dados para teste.
         Como constatado, a taxa de acerto foi 94.5%, aproximadamente, com 34% de dados para teste.
         Como constatado, a taxa de acerto foi 94.3%, aproximadamente, com 33% de dados para teste.
         Como constatado, a taxa de acerto foi 94.2%, aproximadamente, com 32% de dados para teste.
         Como constatado, a taxa de acerto foi 94.0%, com 31% de dados para teste.
         Como constatado, a taxa de acerto foi 93.7%, aproximadamente, com 30% de dados para teste.
         Como constatado, a taxa de acerto foi 93.6%, aproximadamente, com 29% de dados para teste.
         Como constatado, a taxa de acerto foi 93.3%, com 28% de dados para teste.
         Como constatado, a taxa de acerto foi 93.2%, aproximadamente, com 27% de dados para teste.
         Como constatado, a taxa de acerto foi 92.8%, aproximadamente, com 26% de dados para teste.
         Como constatado, a taxa de acerto foi 92.5%, com 25% de dados para teste.
         
         Como constatado, o melhor resultado da máquina foi um valor de 0.35(35%) dos dados para o teste e 0.65(65%) dos dados para treinamento. A conclusão que, nesse caso
         a maior quantidade de dados para teste obteve um melhor resultado. Isso mostra que os dados tem que ser ajustados ao ponto máximo da performance dele, nem para mais, nem para menos.'''