from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap11_intra import swap_1_1_intrarrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas

def VND(pistas, custo_atual, dados):
    k_max = 3 # número de vizinhancas
    k_atual = 0
    while k_atual < k_max:
        if k_atual == 0:
            solucao_nova, custo_novo = swap_1_1_interrotas(pistas, dados)
        elif k_atual == 1:
            solucao_nova, custo_novo = swap_1_1_intrarrotas(pistas, dados)
        else:
            solucao_nova, custo_novo = reinsertion_interrotas(pistas, dados)
            
        if custo_novo < custo_atual:
            pistas = solucao_nova
            custo_atual = custo_novo
            k_atual = 0
        else:
            k_atual += 1

    # print do custo da nova alocacao
    print(f"\nCusto total da alocação VND: {custo_atual}\n")
    
    return pistas, custo_atual
