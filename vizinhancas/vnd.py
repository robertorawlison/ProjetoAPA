from vizinhancas.op2 import two_opt_intra
from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap11_intra import swap_1_1_intrarrotas
from vizinhancas.swap22_inter import swap_2_2_interrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas
from vizinhancas.reinsertion_intra import reinsertion_intrarrotas

def VND(pistas, custo_atual, dados):
    k_max = 5 # número de vizinhancas
    k_atual = 0
    while k_atual < k_max:
        if k_atual == 0:
            solucao_nova, custo_novo = swap_1_1_interrotas(pistas, dados) 
        elif k_atual == 1:
            solucao_nova, custo_novo = two_opt_intra(pistas,dados)
        elif k_atual == 2:
            solucao_nova, custo_novo = reinsertion_intrarrotas(pistas,dados)
        elif k_atual == 3:
            solucao_nova, custo_novo = reinsertion_interrotas(pistas, dados)
        else:
            solucao_nova, custo_novo = swap_2_2_interrotas(pistas, dados)
            
        if custo_novo < custo_atual:
            pistas = solucao_nova
            custo_atual = custo_novo
            k_atual = 0
        else:
            k_atual += 1

    # print do custo da nova alocacao
    print(f"\nCusto total da alocação VND: {custo_atual}\n")
    
    return pistas, custo_atual
