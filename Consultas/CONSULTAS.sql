--  CONSULTAS DO PROJETO

-- 1 Qual país teve o maior total de vendas?
SELECT "Pais", SUM("Vendas") AS total_vendas
FROM vendas_tratadas
GROUP BY "Pais"
ORDER BY total_vendas DESC
LIMIT 1;

-- 2 Quais são os 5 meses com mais vendas totais?
SELECT "Mes", SUM("Vendas") AS vendas_totais
FROM vendas_tratadas
GROUP BY "Mes"
ORDER BY vendas_totais DESC
LIMIT 5;

-- 3 Quais são os 3 produtos mais vendidos em volume de vendas?
SELECT "Nome_do_produto", SUM("Vendas") AS mais_vendido
FROM vendas_tratadas
GROUP BY "Nome_do_produto"
ORDER BY mais_vendido DESC
LIMIT 3;

-- 4 Qual categoria teve o maior valor médio de vendas por pedido?
SELECT "Categoria", AVG("Vendas") AS media_vendas
FROM vendas_tratadas
GROUP BY "Categoria"
ORDER BY media_vendas DESC
LIMIT 1;

-- 5 Quantos pedidos foram realizados por cidade? Mostre as 10 maiores.
SELECT "Cidade", COUNT(*) AS total_Pedido
FROM vendas_tratadas
GROUP BY "Cidade"
ORDER BY total_Pedido DESC
LIMIT 10;

--6 Qual é o tempo médio de entrega dos pedidos?
SELECT "Cidade", AVG("Tempo_de_Entrega_dias") AS tempo_medio_entrega
FROM vendas_tratadas
GROUP BY "Cidade"
ORDER BY tempo_medio_entrega DESC
LIMIT 1;

-- 7 Qual é o total de vendas por segmento de cliente?
SELECT "Segmento", SUM("Vendas") as total_vendas
FROM vendas_tratadas
GROUP BY "Segmento"
ORDER BY total_vendas
LIMIT 1;

-- 8 Em que dia da semana ocorrem mais vendas?
 SELECT "Dia_da_semana", SUM("Vendas") AS semana_mais_vendas
 FROM vendas_tratadas
 GROUP BY "Dia_da_semana"
 ORDER BY semana_mais_vendas
 LIMIT 1;

 -- 9 Quantos pedidos foram feitos em cada ano?
 SELECT "Ano", SUM("Vendas") AS pedido_por_ano
 FROM vendas_tratadas
 Group BY "Ano"
 ORDER BY pedido_por_ano
 LIMIT 1;

 -- 10 Qual subcategoria aparece com mais frequência nos pedidos?
SELECT "Subcategoria", COUNT(*) AS pedido_com_frequencia
FROM vendas_tratadas
GROUP BY "Subcategoria"
ORDER BY pedido_com_frequencia DESC
LIMIT 1;