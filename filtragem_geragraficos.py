import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head(10) #Meio que printa a tabela

df.info() #Traz a tabela em um outro formato

df.describe() #Essa ferramenta consegue te trazer um pouco de estatística mostrando dados numéricos

df.shape  #Tamanho da base (linha, coluna)

linhas, colunas = df.shape[0], df.shape[1] #O df.shape(0), pega o primeiro número de linhas e o outro pega o número de colunas
print("linhas :", linhas)
print("colunas :", colunas)

df.columns  #Pega as colunas (nome delas)

renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=renomear_colunas, inplace=True)
df.columns

df["senioridade"].value_counts() #Calcula a frequências de cada categoria dos valores

df['contrato'].value_counts()

df["remoto"].value_counts()

df["tamanho_empresa"].value_counts()

senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

df["senioridade"] = df["senioridade"].replace(senioridade)
df["senioridade"].value_counts()

contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'FL': 'Freela',
    'CT': 'Contrato'
}

df["contrato"] = df["contrato"].replace(contrato)
df["contrato"].value_counts()

tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Media',
    'L': 'Grande'
}

df["tamanho_empresa"] = df["tamanho_empresa"].replace(tamanho_empresa)
df["tamanho_empresa"].value_counts()

remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
df['remoto'] = df['remoto'].replace(remoto)
df['remoto'].value_counts()

df.head()

df.describe(include="object")

df.describe()

df.isnull()

df.isnull()

df.head()

df.isnull().sum() #Somando tudo nulo

df['ano'].unique()

df[df.isnull().any(axis=1)] #Fazendo um filtro para pegar todos os anos nulos

import numpy as np
#Criando um DataFrame de teste
df_salarios= pd.DataFrame({
    'nome' : ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    'salario' : [4000, np.nan, 5000, np.nan, 100000]
})
# Adicionando uma nova coluna da nossa base, colocando a média dos salários
df_salarios['salario_media']=df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
# Adicionando uma nova coluna da nossa base, colocando a mediana dos salários -> Mediana é melhor
df_salarios['salario_mediana']=df_salarios['salario'].fillna(df_salarios['salario'].median())


df_salarios

df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
df_temperaturas

df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()
df_temperaturas

df_cidades=pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
    "Cidade" : ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

df_cidades["cidade_preenchida"]=df_cidades["Cidade"].fillna("Não Informado")
display(df_cidades)

#Voltando a parte da base original com salários
#Removando dados nulos
df_limpo=df.dropna()

df_limpo.isnull().sum()

df_limpo.head()

df_limpo.info()

# Mudando o tipo do dado ano para int64
df_limpo = df_limpo.assign(ano=df_limpo["ano"].astype("int64"))

df_limpo.head()

# Área de gráficos
# Contar as colunas seionidade
df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição de Senioridade')

import seaborn as sns

sns.barplot(data=df_limpo, x='senioridade', y='usd')

import matplotlib.pyplot as plt    # Vai nos ajudar a colocar título e outras coisas mais legais do gráfico

#Definindo o tamanho da imagem
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd')
#Título do gráfico
plt.title('Salário médio por senioridade')
#Nome dos eixos
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()  #Manda rodar o gráfico

# Utilizando o group by do pandas (O sns já fazia isso na hora de montar o gráfico)
# O objetivo era ordenar essa parte
df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True)

ordem=df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
ordem

#Utilizando a variável ordem para montar gráfico
plt.figure(figsize=(8,5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
#Título do gráfico
plt.title('Salário médio por senioridade')
#Nome dos eixos
plt.xlabel("Senioridade")
plt.ylabel("Salário médio anual (USD)")
plt.show()  #Manda rodar o gráfico

# Outro tipo de gráfico (histograma)
plt.figure(figsize=(8,4)) #Definindo o tamanho
sns.histplot(data=df_limpo['usd'], bins=50, kde=True)
#Título do gráfico
plt.title('Distribuição dos salários anuais')
#Nome dos eixos
plt.xlabel("Salário em USD")
plt.ylabel("Frequência")
plt.show()  #Manda rodar o gráfico

# Gráfico bloxplot
plt.figure(figsize=(8,5)) #Definindo o tamanho
sns.boxplot(x=df_limpo['usd'])
#Título do gráfico
plt.title('Boxplot salário')
#Nome dos eixos
plt.xlabel("Salário em USD")

ordem_senioridade=['Junior','Pleno','Senior','Executivo']
plt.figure(figsize=(8,5)) #Definindo o tamanho
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
#Título do gráfico
plt.title('Boxplot da distribuição por senioridade')
#Nome dos eixos
plt.xlabel('Salário em USD')
plt.show() # Manda rodar

# Mudando as cores do gráfico
ordem_senioridade=['Junior','Pleno','Senior','Executivo']
plt.figure(figsize=(8,5)) #Definindo o tamanho
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
#Título do gráfico
plt.title('Boxplot da distribuição por senioridade')
#Nome dos eixos
plt.xlabel('Salário em USD')
plt.show() # Manda rodar

# Gráficos interativos
import plotly.express as px

# prompt: Crie um gráfico de média salarial por senioridade em barras usando o plotly

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.bar(senioridade_media_salario,
             x='senioridade',
             y='usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})

fig.show()

remoto_contagem=df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns=['tipo_trabalho','quantidade']
remoto_contagem

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho')

fig.show()

remoto_contagem=df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns=['tipo_trabalho','quantidade']
remoto_contagem

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho',
             hole=0.5)

fig.show()

remoto_contagem=df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns=['tipo_trabalho','quantidade']
remoto_contagem

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos tipos de trabalho',
             hole=0.5)
fig.update_traces(textinfo='percent+label')
fig.show()