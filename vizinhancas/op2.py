from copy import deepcopy
from utils import calcular_custo_total  

import random
from copy import deepcopy

def gerar_subsequencia_indices(n, min_len=2):
    """Gera início e fim para uma subsequência de tamanho >= min_len"""
    i = random.randint(0, n - min_len - 1)
    j = random.randint(i + min_len, n - 1)
    return i, j

def two_opt_inter_random(pistas, dados, tentativas=100):
    melhor_config = None
    menor_custo = float('inf')
    num_pistas = len(pistas)

    for _ in range(tentativas):
        idx1, idx2 = random.sample(range(num_pistas), 2)
        pista1 = pistas[idx1]
        pista2 = pistas[idx2]
        seq1, seq2 = pista1.sequencia, pista2.sequencia
        n1, n2 = len(seq1), len(seq2)

        if n1 < 3 or n2 < 3:
            continue  # Não dá pra formar subsequências não triviais

        i, j = gerar_subsequencia_indices(n1)
        k, l = gerar_subsequencia_indices(n2)

        sub1 = seq1[i:j+1]
        sub2 = seq2[k:l+1]

        nova_seq1 = seq1[:i] + sub2[::-1] + seq1[j+1:]
        nova_seq2 = seq2[:k] + sub1[::-1] + seq2[l+1:]

        nova_pistas = []
        for p in pistas:
            if p.pista == pista1.pista:
                nova = deepcopy(p)
                nova.sequencia = nova_seq1
                nova_pistas.append(nova)
            elif p.pista == pista2.pista:
                nova = deepcopy(p)
                nova.sequencia = nova_seq2
                nova_pistas.append(nova)
            else:
                nova_pistas.append(deepcopy(p))

        custo = calcular_custo_total(nova_pistas, dados)
        if custo < menor_custo:
            menor_custo = custo
            melhor_config = nova_pistas

    return melhor_config, menor_custo
