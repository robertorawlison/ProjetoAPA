from copy import deepcopy
from utils import calcular_custo_total

import random
from copy import deepcopy

def reinsertion_interrotas_random(pistas, dados, tentativas=100):
    melhor_vizinho = deepcopy(pistas)
    menor_custo = calcular_custo_total(pistas, dados)
    n = len(pistas)

    for _ in range(tentativas):
        # Escolhe duas pistas diferentes
        i, j = random.sample(range(n), 2)
        pista_origem = pistas[i]
        pista_destino = pistas[j]

        if not pista_origem.sequencia:
            continue  # Evita erro se a pista estiver vazia

        # Sorteia voo da origem e posição de inserção na destino
        idx_voo = random.randint(0, len(pista_origem.sequencia) - 1)
        pos = random.randint(0, len(pista_destino.sequencia))

        voo = pista_origem.sequencia[idx_voo]

        nova_seq_origem = pista_origem.sequencia[:idx_voo] + pista_origem.sequencia[idx_voo+1:]
        nova_seq_destino = pista_destino.sequencia[:pos] + [voo] + pista_destino.sequencia[pos:]

        nova_configuracao = []
        for k in range(n):
            pista = deepcopy(pistas[k])
            if k == i:
                pista.sequencia = nova_seq_origem
            elif k == j:
                pista.sequencia = nova_seq_destino
            nova_configuracao.append(pista)

        custo = calcular_custo_total(nova_configuracao, dados)
        if custo < menor_custo:
            menor_custo = custo
            melhor_vizinho = nova_configuracao

    return melhor_vizinho, menor_custo

