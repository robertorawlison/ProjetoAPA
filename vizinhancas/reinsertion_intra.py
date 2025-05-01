from copy import deepcopy
from utils import calcular_custo_total

from copy import deepcopy

def reinsertion_intrarrotas(pistas, dados):
    melhor_vizinho = deepcopy(pistas)
    menor_custo = calcular_custo_total(pistas, dados)
    n = len(pistas)

    for i in range(n):
        pista = pistas[i]
        seq = pista.sequencia
        m = len(seq)

        for idx_voo in range(m):
            voo = seq[idx_voo]
            for pos in range(m + 1):
                if pos == idx_voo or pos == idx_voo + 1:
                    continue  # Ignora posições equivalentes ou consecutivas

                nova_seq = seq[:idx_voo] + seq[idx_voo+1:]
                nova_seq = nova_seq[:pos if pos < idx_voo else pos - 1] + [voo] + nova_seq[pos if pos < idx_voo else pos - 1:]

                nova_configuracao = []
                for k in range(n):
                    if k == i:
                        nova_pista = deepcopy(pista)
                        nova_pista.sequencia = nova_seq
                        nova_configuracao.append(nova_pista)
                    else:
                        nova_configuracao.append(pistas[k])  # Sem deepcopy aqui

                custo = calcular_custo_total(nova_configuracao, dados)
                if custo < menor_custo:
                    menor_custo = custo
                    melhor_vizinho = deepcopy(nova_configuracao)

    return melhor_vizinho, menor_custo


                