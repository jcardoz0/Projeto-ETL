# 🛒 Análise de Vendas com ETL em Python e PostgreSQL

Este projeto realiza um processo completo de Engenharia de Dados: desde a extração e tratamento dos dados até sua análise em banco relacional e visualizações em Python.

---

## 📌 Objetivo

Aplicar os fundamentos da engenharia de dados em um cenário real de vendas. O projeto inclui:

- Extração de dados de um arquivo CSV
- Tratamento e limpeza com **Pandas**
- Visualização de dados com **Matplotlib**
- Armazenamento dos dados tratados no **PostgreSQL**
- Criação de consultas SQL para insights analíticos

---

## 🧠 Habilidades Desenvolvidas

- Manipulação e limpeza de dados com **Pandas**
- Criação de gráficos e relatórios com **Matplotlib**
- Modelagem e carga de dados em bancos relacionais
- Escrita de **consultas SQL analíticas**
- Organização e documentação de projetos de dados

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Pandas  
- Matplotlib  
- PostgreSQL
  
---

## 📂 Fonte dos Dados

- Dataset original disponível no Kaggle:  
🔗 [Sales Forecasting Dataset – por Rohit Sahoo](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting)  
- Arquivo utilizado: `train.csv`

---

## 🔄 Processo de ETL

### 🔹 Extração
- Leitura do arquivo `train.csv` com Pandas (pasta: `base_de_dados/`)

### 🔹 Transformação
- Conversão de colunas de datas
- Criação de colunas auxiliares: mês, ano, dia da semana, tempo de entrega
- Remoção de colunas irrelevantes e tratamento de valores ausentes

### 🔹 Carga
- Criação da tabela `vendas_tratadas` no PostgreSQL
- Inserção dos dados tratados via SQLAlchemy

📄 Script responsável: `tratativas/etl_processo.py`

---

## 📊 Visualizações Geradas

As análises gráficas foram realizadas com **Matplotlib** e estão descritas abaixo.  
O código está na pasta: `codigo_graficos/`  
As imagens geradas estão na pasta: `graficos/`

1. Total de vendas por país  
2. Top 10 cidades com mais vendas  
3. Vendas por mês  
4. Vendas por categoria  
5. Tempo médio de entrega por categoria

---

## 🧾 Consultas SQL no PostgreSQL

As análises foram feitas após a carga no banco de dados.  
O script SQL com as 10 consultas está na pasta: `consultas/`

Consultas realizadas:

- País com maior volume de vendas  
- Meses com mais vendas  
- Produtos mais vendidos  
- Categoria com maior ticket médio  
- Subcategoria mais frequente  
- Tempo médio de entrega por cidade  
- Total de vendas por segmento  
- Dia da semana com maior volume  
- Pedidos por ano  
- Frequência de subcategorias
