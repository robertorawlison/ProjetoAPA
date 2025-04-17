from copy import deepcopy
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import calcular_multa, calcular_custo_total

#Função pra exibir solução, apenas testei ela
"""def exibir_solucao(pistas, dados):
    for pista in pistas:
        print(f"{pista.pista}:")
        tempo_pista = 0
        for i, voo in enumerate(pista.sequencia):
            # Se não for o primeiro voo, consideramos o tempo de espera entre os voos
            if i == 0:
                tempo_pista = max(voo.tempo_liberacao, tempo_pista)
            else:
                anterior = pista.sequencia[i - 1].id
                tempo_pista += dados.tempos_espera[anterior][voo.id]
                tempo_pista = max(voo.tempo_liberacao, tempo_pista)
            
            multa = calcular_multa(tempo_pista, voo)
            print(f"  {voo.nome} (Início: {tempo_pista}, Multa: {multa})")
            
            tempo_pista += voo.custo
"""

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

