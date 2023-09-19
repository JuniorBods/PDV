# Lista de métricas
metricas = ["totaldevendas", "lucrobruto", "custoproduto", "ticketmedio"]
metricas_nome = ["Total de Vendas", "Lucro Bruto", "Custo de Produto", "Ticket Médio"]

# Calcular a diferença percentual para cada métrica usando um loop for
for metrica, nome in zip(metricas, metricas_nome):
    print(nome, metrica)