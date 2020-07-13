# Evolução da produção de gás natural, por localização, no Brasil
Evolução da produção de gás natural, por localização entre os anos de 2009 a 2018, no território brasileiro, divididos em estados, regiões e federação.

## Análise Exploratória
Sabemos que a produção de gás natural é um forte indicador para saber como está a produção de petroléo num estado, região ou país. Sem contar a importância que o gás natural tem em função de ser um gás muito versátil para muitas finalidades. Sabendo disso, pegaremos os dados presentes, disponibilizados pela ANP [aqui](http://dados.gov.br/dataset/g2-08-anuario-estatistico-2019-evolucao-da-producao-de-gas-natural-por-localizacao), para entender melhor a dinâmica do setor petrolífero durante esses e anos, e tentar fazer previsões para esse setor. Os dados também estarão presentes nesse repositório.

### Visualização em gráfico de barras

#### Produção total de Gás Natural por Estados (Onshore)
![gás natural anual onshore (estados)](https://user-images.githubusercontent.com/48027825/87231344-d5eae400-c38c-11ea-958a-75e300bdac70.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20anual%20g%C3%A1s%20natural%20onshore%20(estados).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Estados%20produtores%20de%20g%C3%A1s%20natural%20onshore.ipynb) para maior detalhamento dos gráficos de cada estado produtor onshore.

#### Produção total de Gás Natural por Estados (Offshore)
![gás natural anual offshore (estados)](https://user-images.githubusercontent.com/48027825/87231345-d7b4a780-c38c-11ea-9eb2-426044bd95c0.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20anual%20g%C3%A1s%20natural%20offshore%20(estados).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Estados%20produtores%20de%20g%C3%A1s%20natural%20offshore.ipynb) para maior detalhamento dos gráficos de cada estado produtor offshore.

#### Produção total de Gás Natural por Estado (Onshore e Offshore) 
![gás natural anual total (estados)](https://user-images.githubusercontent.com/48027825/87231347-dbe0c500-c38c-11ea-93e7-86b939678b33.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20anual%20total(estado).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Estados%20produtores%20de%20g%C3%A1s%20natural%20offshore%20e%20onshore.ipynb) para maior detalhamento dos gráficos de cada estado produtor onshore e offshore.

#### Produção total de Gás Natural por Região (Onshore e Offshore) 
![gás natural anual total (regiões)](https://user-images.githubusercontent.com/48027825/87231348-ddaa8880-c38c-11ea-8be0-17fdfea41ca0.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20anual%20%20total(regi%C3%A3o).py) o script com os códigos para gerar esse gráfico, e [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Regi%C3%B5es%20produtoras%20de%20g%C3%A1s%20natural%20onshore%20e%20offshore.ipynb) para maior detalhamento dos gráficos de cada região produtora onshore e offshore.

#### Produção total de Gás Natural Nacional (Onshore X Offshore)
![gás natural anual onshore e offshore (brasil)](https://user-images.githubusercontent.com/48027825/87231542-6544c700-c38e-11ea-9fc7-c971946d43ba.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20anual%20g%C3%A1s%20natural%20onshore%20e%20offshore%20(brasil).py) o script com os códigos para gerar esse gráfico.

#### Produção total de Gás Natural Nacional (Onshore e Offshore) 
![gás natural anual total (brasil)](https://user-images.githubusercontent.com/48027825/87231354-e4390000-c38c-11ea-9c53-5d1d088c94d1.png)

Acesse [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20anual%20total(brasil).py) o script com os códigos para gerar esse gráfico.

## Previsão dos próximos anos
Após uma análise nos gráficos de toda a produção estadual, regional e nacional, iremos fazer a previsão da produção total nacional, utilizando o ARIMA.

#### Decomposição da série temporal e previsão da produção de Gás Natural Onshore Nacional para os anos de 2019 e 2020
![Figure_1](https://user-images.githubusercontent.com/48027825/76637691-f794a580-6529-11ea-9a00-7f1d232e715a.png)
![produção gás natural onshore (serie temporal)](https://user-images.githubusercontent.com/48027825/65178397-009b3300-da2f-11e9-8ff7-aea8e79e4e16.png)

Acesso ao script para a geração desses gráficos [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20onshore%20(s%C3%A9rie%20temporal).py)

#### Decomposição da série temporal e previsão da produção de Gás Natural Offshore Nacional para os anos de 2019 e 2020
![Figure_2](https://user-images.githubusercontent.com/48027825/76637696-f8c5d280-6529-11ea-9188-66a448d0e605.png)
![produção gás natural offshore (serie temporal)](https://user-images.githubusercontent.com/48027825/65178415-0abd3180-da2f-11e9-9c85-e41f2fdf6762.png)

Acesso ao script para a geração desses gráficos [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20offshore%20(s%C3%A9rie%20temporal).py)

#### Decomposição da série temporal e previsão da produção de Gás Natural Total Nacional para os anos de 2019 e 2020
![Figure_1](https://user-images.githubusercontent.com/48027825/76637970-6c67df80-652a-11ea-9cad-fb38d8b7567a.png)
![produção gás natural offshore onshore total (serie temporal)](https://user-images.githubusercontent.com/48027825/65178462-26283c80-da2f-11e9-9ea7-9f2bd6e68b28.png)

Acesso ao script para a geração desses gráficos [aqui](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/produ%C3%A7%C3%A3o%20g%C3%A1s%20natural%20onshore%20offshore%20total%20(s%C3%A9rie%20temporal).py)

## Informações adicionais sobre esses dados
Tudo que foi exposto acima, em termo de gráfico e previsão, será abordado de uma forma mais detalhada com mais informações sobre a produção de gás natural em cada estado, região e país, juntamente com a sua previsão futura.

- Estados
  - [Alagoas](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Informa%C3%A7%C3%B5es%20adicionais%20sobre%20o%20estado%20de%20Alagoas.ipynb)
  - [Amazonas](https://github.com/fernandessfae/Evolucao-da-producao-de-gas-natural-por-localizacao/blob/master/Informa%C3%A7%C3%B5es%20adicionais%20sobre%20o%20estado%20do%20Amazonas.ipynb)
  - [Bahia]()
  - [Ceará]()
  - [Espírito Santo]()
  - [Maranhão]()
  - [Rio Grande do Norte]()
  - [Rio de Janeiro]()
  - [Sergipe]()
  - [São Paulo]()
- Regiões
  - [Nordeste]()
  - [Norte]()
  - [Sudeste]()
- País
  - [Brasil]()
