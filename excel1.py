#Author: Raphael Campos Squilaro
#Project: Excel painel analytics with python and imported of pandas and openpyxl

#realizing the imports for analytics
import pandas as pd

#read the excel's painel
planilha = pd.read_excel('ocupacao.xlsx')

#Group by name
resultado = planilha.groupby(["Registro" , "Nome"])["Horas"].sum()

#loop to display results

for (registro,nome), horas in resultado.items():
    print(f'O registro {registro} de {nome} têm {horas} horas de ocupação no SENAI')