# Importar as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ensinoSuperior.csv', index_col=0, sep=';')

df = df.dropna(how='all')
df = df.drop_duplicates()

# Troca das linhas pelas colunas
troca = df.transpose()

# PERGUTA #
# Quantos alunos ficaram inscritos, em História e arqueologia ao longo do anos?

# Selecionamos a Área -> Historia e arqueologia
# Criamos uma lista chamada selecao_coluna que contem a coluna que criamos
# 
selecao_coluna = ['História e arqueologia']
selecao = troca[selecao_coluna]
# print(selecao)

# Converta os valores para o tipo numérico
# errors='coerce' -> significa que se houver algum valor que não possa ser convertido 
# para numérico ele colucará NaN (Not a Number)
selecao = selecao.apply(pd.to_numeric, errors='coerce')

# Criação do gráfico de barras
selecao.plot(kind='barh', color='#6cbd7d', figsize=(15, 20))

# titulo
plt.title('Alunos inscritos no ensino superior')

# legenda horizontal
plt.ylabel('Ano')

# legenda vertical
plt.xlabel('Número de Alunos Inscritos')

plt.show()



# transpose, apply, to_numeric -> pandas