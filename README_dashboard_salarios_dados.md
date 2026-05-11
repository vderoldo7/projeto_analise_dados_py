# 🎲 Dashboard de Análise de Salários na Área de Dados

Este projeto é uma aplicação web desenvolvida em **Python** com **Streamlit**, voltada para a análise interativa de salários na área de dados.

A aplicação utiliza uma base de dados pública carregada diretamente do GitHub e permite explorar informações salariais por meio de filtros, métricas principais, gráficos interativos e uma tabela detalhada dos registros.

---

## 🚀 Funcionalidades

- Visualização interativa de dados salariais da área de dados.
- Filtros por ano.
- Filtros por senioridade.
- Filtros por tipo de contrato.
- Filtros por tamanho da empresa.
- Exibição de métricas principais, como:
  - Salário médio.
  - Salário máximo.
  - Total de registros.
  - Cargo mais frequente.
- Gráfico com os 10 cargos de maior salário médio.
- Histograma com a distribuição dos salários anuais.
- Gráfico de pizza com a proporção dos tipos de trabalho.
- Mapa mundial com salário médio de Cientista de Dados por país.
- Tabela detalhada com os dados filtrados.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**

---

## 📊 Sobre o projeto

O objetivo deste projeto é analisar salários de profissionais da área de dados de forma visual, simples e interativa.

Com o dashboard, o usuário consegue entender melhor a distribuição salarial da área, comparar cargos, analisar padrões por senioridade, tipo de contrato, tamanho da empresa e localização dos profissionais.

A aplicação foi construída com foco em visualização de dados e análise exploratória, sendo ideal para praticar conceitos importantes de ciência de dados, como:

- Leitura de dados com Pandas.
- Filtragem de DataFrames.
- Criação de KPIs.
- Construção de gráficos interativos.
- Desenvolvimento de dashboards com Streamlit.
- Análise visual de informações salariais.

---

## 📁 Estrutura do projeto

```bash
dashboard-salarios-dados/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📦 Instalação

Antes de executar o projeto, é necessário ter o **Python** instalado na máquina.

Clone este repositório ou baixe os arquivos do projeto:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Acesse a pasta do projeto:

```bash
cd dashboard-salarios-dados
```

Crie um ambiente virtual, se desejar:

```bash
python -m venv venv
```

Ative o ambiente virtual:

No Windows:

```bash
venv\Scripts\activate
```

No Linux/Mac:

```bash
source venv/bin/activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar

Para iniciar a aplicação, execute o comando abaixo no terminal:

```bash
streamlit run app.py
```

Após executar o comando, o Streamlit abrirá automaticamente a aplicação no navegador.

Caso isso não aconteça, acesse manualmente o endereço exibido no terminal, normalmente:

```bash
http://localhost:8501
```

---

## 📄 Arquivo `requirements.txt`

O projeto contém um arquivo `requirements.txt` com as bibliotecas necessárias para execução da aplicação.

Exemplo:

```txt
streamlit
pandas
plotly
```

Para instalar todas as dependências, utilize:

```bash
pip install -r requirements.txt
```

---

## 🔍 Como usar

Ao abrir o dashboard, o usuário encontrará uma barra lateral com filtros interativos.

É possível filtrar os dados por:

- Ano.
- Senioridade.
- Tipo de contrato.
- Tamanho da empresa.

Após selecionar os filtros desejados, todas as métricas, gráficos e a tabela de dados são atualizados automaticamente.

---

## 📈 Gráficos disponíveis

### Top 10 cargos por salário médio

Exibe os cargos com maior média salarial anual em dólar.

### Distribuição de salários anuais

Mostra a frequência dos salários em diferentes faixas salariais.

### Proporção dos tipos de trabalho

Apresenta a distribuição entre os formatos de trabalho disponíveis na base, como remoto, presencial ou híbrido.

### Salário médio de Cientista de Dados por país

Exibe um mapa mundial com a média salarial de profissionais com o cargo de **Data Scientist**, utilizando o código ISO dos países.

---

## 📌 Dataset

Os dados são carregados diretamente de uma base pública hospedada no GitHub.

A leitura é feita no próprio código com o Pandas:

```python
df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
```

Por esse motivo, é necessário estar conectado à internet para que a aplicação consiga carregar os dados corretamente.

---

## 💡 Objetivo educacional

Este projeto foi desenvolvido com o objetivo de praticar análise de dados e construção de dashboards interativos utilizando Python.

Com ele, é possível desenvolver conhecimentos em:

- Manipulação de dados.
- Análise exploratória.
- Visualização de dados.
- Criação de dashboards.
- Uso de bibliotecas populares do ecossistema Python.
- Desenvolvimento de aplicações web simples com Streamlit.

---

## 👨‍💻 Autor

Desenvolvido por **Vitor Viana Carneiro Deroldo**.

---

## 📌 Status do projeto

✅ Projeto funcional

### Possíveis melhorias futuras

- Adicionar botão para download dos dados filtrados.
- Criar novos filtros por país e cargo.
- Adicionar análise de salário mediano.
- Melhorar o tratamento para filtros vazios.
- Criar uma página inicial explicando o dataset.
- Adicionar gráficos comparando evolução salarial por ano.
- Personalizar o visual do dashboard com CSS.
- Hospedar o projeto em uma plataforma como Streamlit Community Cloud.
