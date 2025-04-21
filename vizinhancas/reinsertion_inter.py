from copy import deepcopy
from utils import calcular_custo_total

def reinsercao_interrotas(pistas, dados):
    melhor_custo = calcular_custo_total(pistas, dados)
    melhor_movimento = None  # (orig_idx, dest_idx, idx_voo, nova_pos)

    n = len(pistas)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            pista_origem = pistas[i]
            pista_destino = pistas[j]

            for idx_voo in range(len(pista_origem.sequencia)):
                voo = pista_origem.sequencia[idx_voo]

                for pos in range(len(pista_destino.sequencia) + 1):
                    # Cria pistas temporárias só com esse movimento específico
                    temp_origem = pista_origem.sequencia[:idx_voo] + pista_origem.sequencia[idx_voo + 1:]
                    temp_destino = pista_destino.sequencia[:pos] + [voo] + pista_destino.sequencia[pos:]

                    pistas_temp = []
                    for k in range(n):
                        if k == i:
                            pistas_temp.append(Alocacao(pista=pistas[i].pista, sequencia=temp_origem))
                        elif k == j:
                            pistas_temp.append(Alocacao(pista=pistas[j].pista, sequencia=temp_destino))
                        else:
                            pistas_temp.append(pistas[k])

                    custo = calcular_custo_total(pistas_temp, dados)

                    if custo < melhor_custo:
                        melhor_custo = custo
                        melhor_movimento = (i, j, idx_voo, pos)

    if melhor_movimento:
        i, j, idx_voo, pos = melhor_movimento
        voo = pistas[i].sequencia.pop(idx_voo)
        pistas[j].sequencia.insert(pos, voo)

    return pistas, melhor_custo
