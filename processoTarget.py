import json

# Leitura dos dados do faturamento mensal a partir de um arquivo json
with open('faturamento.json') as file:
    faturamento_mensal = json.load(file)

# Remoção dos dias sem faturamento do vetor
faturamento_diario = [faturamento_mensal[i] for i in range(len(faturamento_mensal)) if faturamento_mensal[i] > 0]

# Cálculo da média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Cálculo do menor valor de faturamento diário
menor_valor = min(faturamento_diario)

# Cálculo do maior valor de faturamento diário
maior_valor = max(faturamento_diario)

# Cálculo do número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = len([f for f in faturamento_diario if f > media_mensal])

# Exibição dos resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento diário acima da média mensal:", dias_acima_da_media)
