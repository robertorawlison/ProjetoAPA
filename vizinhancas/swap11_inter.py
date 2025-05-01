from copy import deepcopy
from utils import calcular_custo_total

import random

def swap_1_1_interrotas_aleatorio(pistas, dados, tentativas=100):
    melhor_vizinho = deepcopy(pistas)
    menor_custo = calcular_custo_total(pistas, dados)
    n = len(pistas)

    for _ in range(tentativas):
        i, j = random.sample(range(n), 2)
        pista_a = pistas[i]
        pista_b = pistas[j]

        if not pista_a.sequencia or not pista_b.sequencia:
            continue

        idx_a = random.randint(0, len(pista_a.sequencia) - 1)
        idx_b = random.randint(0, len(pista_b.sequencia) - 1)

        nova_seq_a = pista_a.sequencia.copy()
        nova_seq_b = pista_b.sequencia.copy()
        nova_seq_a[idx_a], nova_seq_b[idx_b] = nova_seq_b[idx_b], nova_seq_a[idx_a]

        nova_configuracao = []
        for k in range(n):
            pista = deepcopy(pistas[k])
            if k == i:
                pista.sequencia = nova_seq_a
            elif k == j:
                pista.sequencia = nova_seq_b
            nova_configuracao.append(pista)

        custo = calcular_custo_total(nova_configuracao, dados)
        if custo < menor_custo:
            menor_custo = custo
            melhor_vizinho = deepcopy(nova_configuracao)

    return melhor_vizinho, menor_custo
