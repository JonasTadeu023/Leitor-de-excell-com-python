#importando as libs necessarias
import pandas as pd

#importar arquivo excel 
dados = pd.read_excel('dados.xlsx', sheet_name='Massa')

#pegar variaveis para o filtro
tonalidade = input("Qual a tonalidade do material? ")
dureza = input("Qual a Dureza do Material? ")
caracteristica = input("Qual a Característica do Material? ")
elastomero = input("Qual o tipo de Elastômero? ")
area =  input("Qual a área? ")
#transforma a area em um float
area1 = float(area)

#filtro
df1 = dados.loc[dados['Tonalidade'] == tonalidade]
df2 = df1.loc[dados['Dureza'] == dureza]
df3 = df2.loc[dados['Caracteristicas'] == caracteristica]
df4 = float(df3.loc[dados['Tipo Elastomero'] == elastomero]['Densidade (g/cm3)'])
df5 = float(df3.loc[dados['Tipo Elastomero'] == elastomero]['Mistura'])

#mostrando na tela a mistura com o peso do perfil
print("Mistura: ");print(df5)
print("Peso do perfil/metro: ");print(df4*area1)