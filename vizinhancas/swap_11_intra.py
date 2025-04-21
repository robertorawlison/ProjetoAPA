from copy import deepcopy
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import calcular_multa, calcular_custo_total


def swap_1_1_intrarrotas(pistas, dados):
    pistas_otimizadas = []

    for pista in pistas:
        melhor_pista = deepcopy(pista)
        menor_custo = calcular_custo_total([melhor_pista], dados)

        sequencia = melhor_pista.sequencia
        n = len(sequencia)

        for i in range(n):
            for j in range(i + 1, n):
                nova_pista = deepcopy(pista)
                nova_pista.sequencia[i], nova_pista.sequencia[j] = (
                    nova_pista.sequencia[j],
                    nova_pista.sequencia[i],
                )
                custo = calcular_custo_total([nova_pista], dados)

                if custo < menor_custo:
                    menor_custo = custo
                    melhor_pista = nova_pista

        pistas_otimizadas.append(melhor_pista)

    custo_total = calcular_custo_total(pistas_otimizadas, dados)
    return pistas_otimizadas, custo_total