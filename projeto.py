# Importar as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ensinoSuperior.csv', index_col=0, sep=';')

df = df.dropna(how='all')
df = df.drop_duplicates()
df = df.rename(columns=lambda x: x.strip())

# colocar cores ao grafico de barras
#cores = ['pink', 'lightcoral', 'skyblue', 'lightskyblue', 'lightpink']



plt.show()