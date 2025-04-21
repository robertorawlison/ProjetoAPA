from copy import deepcopy
from utils import calcular_custo_total

def swap_1_1_interrotas(pistas, dados):
    n = len(pistas)
    menor_custo = calcular_custo_total(pistas, dados)

    # Guarda apenas as informações da melhor troca
    melhor_i, melhor_j = -1, -1
    melhor_idx_a, melhor_idx_b = -1, -1

    for i in range(n):
        for j in range(i + 1, n):
            pista_a = pistas[i]
            pista_b = pistas[j]

            for idx_a in range(len(pista_a.sequencia)):
                for idx_b in range(len(pista_b.sequencia)):
                    nova_pista_a = deepcopy(pista_a)
                    nova_pista_b = deepcopy(pista_b)

                    # Realiza o swap temporário
                    nova_pista_a.sequencia[idx_a], nova_pista_b.sequencia[idx_b] = (
                        nova_pista_b.sequencia[idx_b],
                        nova_pista_a.sequencia[idx_a]
                    )

                    # Calcula o custo parcial
                    custo_temp = 0
                    for k in range(n):
                        if k == i:
                            custo_temp += calcular_custo_total([nova_pista_a], dados)
                        elif k == j:
                            custo_temp += calcular_custo_total([nova_pista_b], dados)
                        else:
                            custo_temp += calcular_custo_total([pistas[k]], dados)

                    # Se for melhor, guarda os índices da troca
                    if custo_temp < menor_custo:
                        menor_custo = custo_temp
                        melhor_i, melhor_j = i, j
                        melhor_idx_a, melhor_idx_b = idx_a, idx_b

    # Se nenhuma troca melhor foi encontrada, retorna o original
    if melhor_i == -1:
        return deepcopy(pistas), menor_custo

    # Agora sim, monta a nova configuração com a melhor troca
    nova_configuracao = []
    for k in range(n):
        if k == melhor_i:
            nova_pista = deepcopy(pistas[k])
            nova_pista.sequencia[melhor_idx_a] = pistas[melhor_j].sequencia[melhor_idx_b]
            nova_configuracao.append(nova_pista)
        elif k == melhor_j:
            nova_pista = deepcopy(pistas[k])
            nova_pista.sequencia[melhor_idx_b] = pistas[melhor_i].sequencia[melhor_idx_a]
            nova_configuracao.append(nova_pista)
        else:
            nova_configuracao.append(deepcopy(pistas[k]))

    return nova_configuracao, menor_custo
