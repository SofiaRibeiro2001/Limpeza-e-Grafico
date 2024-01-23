import pandas as pd

df= pd.read_csv('ensinoSuperior.csv', sep=';')

# melt()-> função pandas
# transformar um DataFrame com muitas colunas/largo para um formato mais longo
# id_vars-> coluna usadas como variaveis identificadoras 


df_alterado = pd.melt(df, id_vars=['Areas'], var_name='Ano', value_name='Valores')

df_alterado.to_csv('novoFicheiro.csv', index=False)