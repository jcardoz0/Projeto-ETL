import pandas as pd

# Extraindo os dados do CSV
df = pd.read_csv('C:/Users/jc579/Videos/ETL/ETL2/train.csv', encoding='latin1')

# Mostrando todas as colunas no output
pd.set_option('display.max_columns', None)

# Função para traduzir nomes de colunas para português
def traduzir_colunas(df):
    return df.rename(columns={
        'Row ID':'ID_linha',
        'Order ID':'ID_pedido',
        'Order Date': 'Data_do_pedido',
        'Ship Date': 'Data_de_envio',
        'Ship Mode': 'Modo_de_envio',
        'Customer ID': 'ID_do_cliente',
        'Customer Name': 'Nome_do_cliente',
        'Segment': 'Segmento',
        'Country': 'Pais',
        'City': 'Cidade',
        'State': 'Estado',
        'Postal Code':'codigo_postal',
        'Region': 'Regiao',
        'Product ID': 'ID_do_produto',
        'Category': 'Categoria',
        'Sub-Category': 'Subcategoria',
        'Product Name': 'Nome_do_produto',
        'Sales': 'Vendas'
    })

# Aplicando a função de tradução
df = traduzir_colunas(df)

# Convertendo colunas de data (corrigido o nome das colunas)
df['Data_do_pedido'] = pd.to_datetime(df['Data_do_pedido'], errors='coerce', dayfirst=True)
df['Data_de_envio'] = pd.to_datetime(df['Data_de_envio'], errors='coerce', dayfirst=True)

# Removendo linhas com dados ausentes
df = df.dropna()

# Criando nova coluna com o tempo de entrega
df['Tempo_de_Entrega_dias'] = (df['Data_de_envio'] - df['Data_do_pedido']).dt.days

# Padronizando capitalização e removendo espaços extras
df['Pais'] = df['Pais'].str.strip().str.title()
df['Cidade'] = df['Cidade'].str.strip().str.title()
df['Categoria'] = df['Categoria'].str.strip().str.title()  # Corrigido: nome da coluna estava minúsculo

# Filtrando entregas com valores negativos de tempo (dados inconsistentes)
df = df[df['Tempo_de_Entrega_dias'] >= 0]

# Criando colunas de data adicionais
df['Ano'] = df['Data_do_pedido'].dt.year
df['Mes'] = df['Data_do_pedido'].dt.month
df['Dia_da_semana'] = df['Data_do_pedido'].dt.day_name()

# Garantindo que a data de envio seja igual ou posterior à data do pedido
df = df[df['Data_de_envio'] >= df['Data_do_pedido']]

# Removendo outliers na coluna de vendas com base no IQR (método interquartil)
Q1 = df['Vendas'].quantile(0.25)
Q3 = df['Vendas'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df['Vendas'] < limite_inferior) | (df['Vendas'] > limite_superior)]
print(f'Total de outliers removidos: {len(outliers)}')

df = df[(df['Vendas'] >= limite_inferior) & (df['Vendas'] <= limite_superior)]

# Salvando o dataframe tratado em CSV
df.to_csv('dados_tratados.csv', index=False)

# Exibindo o resultado final
print(df)