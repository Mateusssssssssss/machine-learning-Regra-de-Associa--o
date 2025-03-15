import pandas as pd
#O Apriori é um algoritmo de mineração de regras de associação, muito utilizado em análises de cestas de compras. 
#Ele identifica padrões frequentes.
from apyori import apriori
import numpy as np
#Ler arquivo
# header=None: pandas considerará todas as linhas como dados e não interpretará nenhuma como cabeçalho.
dados = pd.read_csv('transacoes.txt', header=None)
print(dados.head())
# Trensformação para o formato lista, que é exigido pela bilbioteca apyori, 6 é a quantidade de itens da base de dados.
# convertendo os dados carregados do arquivo para uma estrutura de listas de listas, 
# que é o formato esperado pelo algoritmo Apriori
transacoes = dados.astype(str).values.tolist()
    
#min_support: Define o suporte mínimo para considerar um item frequente.
#min_confidence: Define a confiança mínima para aceitar uma regra.
#min_lift: Define o lift mínimo para considerar uma regra relevante.
# min_length=2: significa que a regra precisa conter pelo menos 2 itens.
regras = apriori(transacoes, min_support=0.5, min_confidence= 0.5, min_length=2)

#Resultado
resultado = list(regras)
print(resultado[0])
print(resultado)

# Para melhor visualização
resultado2 = [list(x) for x in resultado]
print(resultado2)

#Para melhor visualização
resultado3 = []
for j in range(0,7):
    resultado3.append([list(x) for x in resultado2[j][2]])

