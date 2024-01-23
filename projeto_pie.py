# Importar as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ensinoSuperior.csv', index_col=0, sep=';')

# Apagar linhas em branco do ficheiro
df = df.dropna(how='all')

# Apagar linhas duplicadas
df = df.drop_duplicates()

# apresenta as Areas do ano de 2022
# Quais são as áreas com mais alunos inscritos no ano 2022?-> pergunta
media_areas_anos = df.groupby('Areas')['2022'].sum()

# as 5 maiores areas
cinco_areas = media_areas_anos.nlargest(5)

# colocar cores ao grafico de barras
cores = ['#6e6b63', '#48574b', '#8f9c92', '#b6d6bd', '#848785']

# tamanho da página
plt.figure(figsize=(15, 20))

# crição do gráfico de torta
plt.pie(cinco_areas, labels=cinco_areas.index, autopct='%1.1f%%', startangle=140, colors=cores)

# titulo
plt.title('5 Maiores Áreas de estudo de alunos inscritos no ensino superior em 2022')

plt.show()