from vizinhancas.op2 import two_opt_intra
from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap22_inter import swap_2_2_interrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas
from vizinhancas.reinsertion_intra import reinsertion_intrarrotas

def VND(pistas, custo_atual, dados):
    vizinhancas = [
        swap_1_1_interrotas,
        reinsertion_intrarrotas,
        two_opt_intra,
        reinsertion_interrotas,
        swap_2_2_interrotas
    ]
    
    k_max = len(vizinhancas)
    k = 0
    while k < k_max:
        nova_solucao, novo_custo = vizinhancas[k](pistas, dados)
        if novo_custo < custo_atual:
            pistas = nova_solucao
            custo_atual = novo_custo
            k = 0
        else:
            k += 1

    print(f"\nCusto total da alocação VND: {custo_atual}\n")
    return pistas, custo_atual
