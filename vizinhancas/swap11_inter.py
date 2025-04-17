from copy import deepcopy
from utils import calcular_custo_total

def swap_1_1_interrotas(pistas, dados):
    melhor_vizinho = deepcopy(pistas)
    menor_custo = calcular_custo_total(pistas, dados)

    n = len(pistas)

    for i in range(n):
        for j in range(i + 1, n):
            pista_a = pistas[i]
            pista_b = pistas[j]

            for idx_a in range(len(pista_a.sequencia)):
                for idx_b in range(len(pista_b.sequencia)):
                    nova_pista_a = deepcopy(pista_a)
                    nova_pista_b = deepcopy(pista_b)

                    # Realiza o swap entre os voos
                    nova_pista_a.sequencia[idx_a], nova_pista_b.sequencia[idx_b] = (
                        nova_pista_b.sequencia[idx_b],
                        nova_pista_a.sequencia[idx_a]
                    )

                    # Monta a nova configuração de pistas
                    nova_configuracao = []
                    for k in range(n):
                        if k == i:
                            nova_configuracao.append(nova_pista_a)
                        elif k == j:
                            nova_configuracao.append(nova_pista_b)
                        else:
                            nova_configuracao.append(deepcopy(pistas[k]))

                    # Calcula o custo total da nova configuração
                    custo = calcular_custo_total(nova_configuracao, dados)

                    # Verifica se essa é a melhor configuração até agora
                    if custo < menor_custo:
                        menor_custo = custo
                        melhor_vizinho = nova_configuracao

    return melhor_vizinho, menor_custo
