from copy import deepcopy
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import calcular_custo_total

def swap_1_1_intrarrotas(pistas, dados):
    pistas_otimizadas = []

    for pista in pistas:
        melhor_seq = pista.sequencia.copy()
        menor_custo = calcular_custo_total([pista], dados)
        n = len(melhor_seq)

        for i in range(n):
            for j in range(i + 1, n):
                nova_seq = melhor_seq.copy()
                nova_seq[i], nova_seq[j] = nova_seq[j], nova_seq[i]

                nova_pista = deepcopy(pista)
                nova_pista.sequencia = nova_seq

                custo = calcular_custo_total([nova_pista], dados)

                if custo < menor_custo:
                    menor_custo = custo
                    melhor_seq = nova_seq

        nova_pista_final = deepcopy(pista)
        nova_pista_final.sequencia = melhor_seq
        pistas_otimizadas.append(nova_pista_final)

    custo_total = calcular_custo_total(pistas_otimizadas, dados)
    return pistas_otimizadas, custo_total

