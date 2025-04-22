from alocacao import Construcao
from vizinhancas.vnd import VND

def GRASP(instancia, max_iter=5, alpha=0.7):
    melhor_solucao = None
    melhor_custo = float('inf')

    sum_custo_vnd = 0

    for i in range(max_iter):
        # Fase de construção com aleatoriedade e alpha
        pistas, custo_total, dados = Construcao(instancia, alpha)

        # Fase de melhoria com VND
        pistas_vnd, custo_vnd = VND(pistas, custo_total, dados)

        sum_custo_vnd += custo_vnd

        # Verifica se a solução melhorou
        if custo_vnd < melhor_custo:
            melhor_custo = custo_vnd
            melhor_solucao = pistas_vnd

    media_custo_vnd = sum_custo_vnd / max_iter

    return melhor_solucao, melhor_custo, media_custo_vnd