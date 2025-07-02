import matplotlib.pyplot as plt

# 1. Total de vendas por país
vendas_pais = df.groupby('Pais')['Vendas'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
vendas_pais.plot(kind='bar')
plt.title('Total de Vendas por País')
plt.ylabel('Vendas')
plt.xlabel('País')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Top 10 cidades com mais vendas
vendas_cidade = df.groupby('Cidade')['Vendas'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
vendas_cidade.plot(kind='barh')
plt.title('Top 10 Cidades com Mais Vendas')
plt.xlabel('Vendas')
plt.ylabel('Cidade')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 3. Vendas por mês
vendas_mes = df.groupby('Mes')['Vendas'].sum().sort_index()
plt.figure(figsize=(10,6))
vendas_mes.plot(kind='line', marker='o')
plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.xticks(range(1,13))
plt.tight_layout()
plt.show()

# 4. Vendas por categoria
vendas_categoria = df.groupby('Categoria')['Vendas'].sum().sort_values(ascending=False)
plt.figure(figsize=(10,6))
vendas_categoria.plot(kind='bar')
plt.title('Vendas por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Tempo médio de entrega por categoria
tempo_entrega = df.groupby('Categoria')['Tempo_de_Entrega_dias'].mean().sort_values()
plt.figure(figsize=(10,6))
tempo_entrega.plot(kind='bar')
plt.title('Tempo Médio de Entrega por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Dias')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
