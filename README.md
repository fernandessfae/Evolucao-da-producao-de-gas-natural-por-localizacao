# Evolução da produção de gás natural, por localização, no Brasil
Evolução da produção de gás natural, por localização entre os anos de 2009 a 2018, no território brasileiro, divididos em estados, regiões e federação.

## Análise Exploratória
Sabemos que a produção de gás natural é um forte indicador para saber como está a produção de petroléo num estado, região ou país. Sem contar a importância que o gás natural tem em função de ser um gás muito versátil para muitas finalidades. Sabendo disso, pegaremos os dados presentes, disponibilizados pela ANP [aqui](http://dados.gov.br/dataset/g2-08-anuario-estatistico-2019-evolucao-da-producao-de-gas-natural-por-localizacao), para entender melhor a dinâmica do setor petrolífero durante esses e anos, e tentar fazer previsões para esse setor. Os dados também estarão presentes nesse repositório.

### Visualização em gráfico de barras

#### Produção total de Gás Natural por Estados (Onshore)
![gás natural anual onshore (estados)](https://user-images.githubusercontent.com/48027825/87231344-d5eae400-c38c-11ea-958a-75e300bdac70.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20anual%20g%C3%A1s%20natural%20onshore%20(estados).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Estados%20produtores%20de%20g%C3%A1s%20natural%20onshore.ipynb) para maior detalhamento dos gráficos de cada estado.

#### Produção total de Gás Natural por Estados (Offshore)
![gás natural anual offshore (estados)](https://user-images.githubusercontent.com/48027825/87231345-d7b4a780-c38c-11ea-9eb2-426044bd95c0.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20anual%20g%C3%A1s%20natural%20offshore%20(estados).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Estados%20produtores%20de%20g%C3%A1s%20natural%20offshore.ipynb) para maior detalhamento dos gráficos de cada estado.

#### Produção total de Gás Natural por Estado (Onshore e Offshore) 
![gás natural anual total (estados)](https://user-images.githubusercontent.com/48027825/87231347-dbe0c500-c38c-11ea-93e7-86b939678b33.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20anual%20total(estado).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Estados%20produtores%20de%20g%C3%A1s%20natural%20offshore%20e%20onshore.ipynb) para maior detalhamento dos gráficos de cada estado.

#### Produção total de Gás Natural por Região (Onshore e Offshore) 
![gás natural anual total (regiões)](https://user-images.githubusercontent.com/48027825/87231348-ddaa8880-c38c-11ea-8be0-17fdfea41ca0.png)

#### Produção total de Gás Natural Nacional (Onshore X Offshore)
![gás natural anual onshore e offshore (brasil)](https://user-images.githubusercontent.com/48027825/87231542-6544c700-c38e-11ea-9fc7-c971946d43ba.png)

#### Produção total de Gás Natural Nacional (Onshore e Offshore) 
![gás natural anual total (brasil)](https://user-images.githubusercontent.com/48027825/87231354-e4390000-c38c-11ea-9c53-5d1d088c94d1.png)

## Utilização de séries temporais

**1)Decomposição série temporal Produção de Gás Natural Onshore Nacional entre os anos de 2009 a 2018**
![Figure_1](https://user-images.githubusercontent.com/48027825/76637691-f794a580-6529-11ea-9a00-7f1d232e715a.png)

**2)Decomposição série temporal Produção de Gás Natural Offshore Nacional entre os anos de 2009 a 2018**
![Figure_2](https://user-images.githubusercontent.com/48027825/76637696-f8c5d280-6529-11ea-9188-66a448d0e605.png)

**3)Decomposição série temporal Produção de Gás Natural Total Nacional entre os anos de 2009 a 2018**
![Figure_1](https://user-images.githubusercontent.com/48027825/76637970-6c67df80-652a-11ea-9cad-fb38d8b7567a.png)

**4)Previsão Produção de Gás Natural Onshore Nacional para os anos de 2019 e 2020 (AUTOARIMA)**
![produção gás natural onshore (serie temporal)](https://user-images.githubusercontent.com/48027825/65178397-009b3300-da2f-11e9-8ff7-aea8e79e4e16.png)

**5)Previsão Produção de Gás Natural Offshore Nacional para os anos de 2019 e 2020 (AUTOARIMA)**
![produção gás natural offshore (serie temporal)](https://user-images.githubusercontent.com/48027825/65178415-0abd3180-da2f-11e9-9c85-e41f2fdf6762.png)

**6)Previsão Produção de Gás Natural Total (Onshore X Offshore) Nacional para os anos de 2019 e 2020 (AUTOARIMA)**
![produção gás natural offshore onshore total (serie temporal)](https://user-images.githubusercontent.com/48027825/65178462-26283c80-da2f-11e9-9ea7-9f2bd6e68b28.png)
