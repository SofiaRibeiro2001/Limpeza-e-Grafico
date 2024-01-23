# Importar as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# carrega todos os dados do ficheiro para a variavel df
# encoding='latin1' -> intrepreta a leitura do ficheiro
df = pd.read_csv('QuadroResumo.csv', encoding='latin1', sep=';')

# Apagar linhas em branco do ficheiro
df = df.dropna(how='all')

# Apagar linhas duplicadas do ficheiro
df = df.drop_duplicates()

# Apagar espaços em branco no inicio e do fim das colunas
df = df.rename(columns=lambda x: x.strip())

#print(df.head())
#print(df.columns)

# LIMPEZA DA COLUNA AREAS #
# df['Areas']-> seleciono a coluna 'Areas' do ficheiro guardado na variavel
# replace(to_replace=r'[\d.]'-> método replace para substituir qualquer dígito 
#                   (\d) ou ponto (.) na coluna 'Areas' por uma string vazia ('')
# regex=True-> permite a substituição da string, usando expressões regulares
# str.strip()-> função strip remove espaços em branco no início e no final de uma string.
df['Areas'] = df['Areas'].replace(to_replace=r'[\d.]', value='', regex=True).str.strip()


# LIMPEZA DO RESTO DAS COLUNAS #
# Remover os espaços nos números
# iloc->  usado para acessar um grupo de linhas e colunas por meio de posições inteiras.
# [:, 1:]-> é posição/seleção de todas as colunas exceto a primeira.
# [:, 1:]-> [linhas, colunas] | Selecenionar todas as linhas, a partir da 2 coluna

# applymap -> usado  para aplicar uma função a cada elemento de um DataFrame
# (lambda x: ''.join(x.split()) if isinstance(x, str) else x)
# x -> É o argumento da função, que representa um elemento individual do ficheiro
# ''.join -> junta as palavras sem espaços
# x.split()-> Separa a string em uma lista de palavras
# isinstance(x, str) else x -> Verifica se x é uma string aplica a operação de remoção 
#                           de espaços; caso contrário, mantém o elemento inalterado

df.iloc[:, 1:] = df.iloc[:, 1:].applymap(lambda x: ''.join(x.split()) if isinstance(x, str) else x)

# selecionar as linhas a serem usadas
linhas = df.iloc[:15]

# selecionar as colunas a serem usadas
df = linhas[['Areas', '2022', '2021', '2020', '2019', '2018']]

# ficheiro novo
# Dados dos alunos inscritos no ensino superior por áreas de estudo
df.to_csv('ensinoSuperior.csv', index=False, sep=';')

print(df)





# replace, applymap, to_csv -> biblioteca pandas
# strip, join, split -> função de string padrão do python
# isinstance -> padrão do python 
