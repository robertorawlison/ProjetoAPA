from copy import deepcopy
from utils import calcular_custo_total

from copy import deepcopy
from itertools import combinations

def trocar_pares(seq1, seq2, idx1, idx2):
    nova_seq1 = seq1[:]
    nova_seq2 = seq2[:]
    nova_seq1[idx1:idx1+2], nova_seq2[idx2:idx2+2] = seq2[idx2:idx2+2], seq1[idx1:idx1+2]
    return nova_seq1, nova_seq2

def swap_2_2_interrotas(pistas, dados):
    melhor_vizinho = pistas
    menor_custo = calcular_custo_total(pistas, dados)

    for i, j in combinations(range(len(pistas)), 2):
        pista_a, pista_b = pistas[i], pistas[j]
        seq_a, seq_b = pista_a.sequencia, pista_b.sequencia

        if len(seq_a) < 2 or len(seq_b) < 2:
            continue

        for idx_a in range(len(seq_a) - 1):
            for idx_b in range(len(seq_b) - 1):
                nova_seq_a, nova_seq_b = trocar_pares(seq_a, seq_b, idx_a, idx_b)

                nova_config = pistas[:]
                nova_config[i] = deepcopy(pista_a)
                nova_config[i].sequencia = nova_seq_a
                nova_config[j] = deepcopy(pista_b)
                nova_config[j].sequencia = nova_seq_b

                custo = calcular_custo_total(nova_config, dados)

                if custo < menor_custo:
                    menor_custo = custo
                    melhor_vizinho = deepcopy(nova_config)

    return melhor_vizinho, menor_custo

                        



