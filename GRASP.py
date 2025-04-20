import os
from alocacao import alocar_voos, Construcao
from vizinhancas.vnd import VND
from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap11_intra import swap_1_1_intrarrotas
from vizinhancas.swap22_inter import swap_2_2_interrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas
from vizinhancas.reinsertion_intra import reinsertion_intrarrotas
from utils import calcular_custo_total

def grasp(instancia, alpha, grasp_max):
    melhor_solucao = None
    melhor_custo = float('inf')

    for _ in range(grasp_max):
        # Fase de construção com critério alpha
        solucao, dados = Construcao(instancia, alpha)

        # Fase de busca local (VND)
        solucao = VND(solucao, dados)  # VND é chamada aqui

        # Avalia a solução
        custo_atual = calcular_custo_total(solucao, dados)

        if custo_atual < melhor_custo:
            melhor_solucao = solucao
            melhor_custo = custo_atual

    return melhor_solucao, melhor_custo