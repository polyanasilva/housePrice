# Projeto House Prices do Kaggle

import pandas as pd

base = pd.read_csv('train.csv')

# print(base.head(5))

# print(base.shape)

# print(base.isnull().sum()/base.shape[0])
# print((base.isnull().sum()/base.shape[0]).sort_values(ascending=False).head(20))

# print(base.isnull().sum()/base.shape[0] > 0.1)

# base = base.columns[base.isnull().sum()/base.shape[0] > 0.1]

# base = base.drop(eliminar, exis=1)

# colunas = base.columns[base.dtypes != 'object'] # seleciona apenas o que nao é objeto

# base = base.loc[:, colunas]

# base.fillna


# Retornando o shape da base
base.shape

# E as informações
base.info()

# Visualizando quantidade de valores vazios
(base.isnull().sum()/base.shape[0]).sort_values(ascending=False).head(20)

# Podemos eliminar as colunas com mais de 10% de valores vazios
eliminar = base.columns[(base.isnull().sum()/base.shape[0]) > 0.1]

# Eliminando essas colunas
base = base.drop(eliminar,axis=1)

# Selecionando apenas as colunas numéricas
colunas = base.columns[base.dtypes != 'object']

# E criar uma nova base com esses valores
base2 = base.loc[:,colunas]
base2.head(5)

# Verificando os valores vazios
base2.isnull().sum().sort_values(ascending=False).head(5)

# Substituindo os valores vazios por -1
base2 = base2.fillna(-1)

