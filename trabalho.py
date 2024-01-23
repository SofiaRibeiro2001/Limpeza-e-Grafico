# Importar as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregar ficheiro
# encoding='latin1' -> intrepreta a leitura do ficheiroi
df = pd.read_csv('QuadroResumo.csv', sep=';', encoding='latin1')

# Apagar linhas em branco do ficheiro
df = df.dropna(how='all')

# Apagar linhas duplicadas do ficheiro
df = df.drop_duplicates()

# Apagar espaços em branco no inicio e do fim
df = df.rename(columns=lambda x: x.strip())

#print(df.head())
#print(df.columns)

# remover os espaços, os  numeros e os pontos finais
# a função replace remove tudo que não for letra
# r'[\d\s.]' -> uma string para encontrar e substituir padroes em string (\d -> para digitos)
# regex=True -> permite a substituição da string
# .str.strip() -> para remover os espaços a esquerda que tem no ficheiro
df['Areas'] = df['Areas'].replace(to_replace=r'[\d.]', value='', regex=True).str.strip()

# Remover os espaços nos números
# tranformar em inteiros
df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x: ''.join(x.split()) if isinstance(x, str) else x)

# selecionar as linhas a serem usadas
linhas = df.iloc[:15]

# selecionar as colunas a serem usadas
df = linhas[['Areas', '2022', '2021', '2020', '2019', '2018']]

# ficheiro novo
# Dados dos alunos inscritos no ensino superior por áreas de estudo
df.to_csv('ensinoSuperior.csv', index=False, sep=';')

print(df)