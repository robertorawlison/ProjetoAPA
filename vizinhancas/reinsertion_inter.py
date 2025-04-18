from copy import deepcopy
from utils import calcular_custo_total

def reinsertion_interrotas(pistas, dados):
    melhor_vizinho = deepcopy(pistas)
    menor_custo = calcular_custo_total(pistas, dados)

    n = len(pistas)

    for i in range(n):  # pista origem
        for j in range(n):  # pista destino
            if i == j:
                continue

            pista_origem = pistas[i]
            pista_destino = pistas[j]

            for idx_voo in range(len(pista_origem.sequencia)):
                for pos in range(len(pista_destino.sequencia) + 1):
                    nova_pista_origem = deepcopy(pista_origem)
                    nova_pista_destino = deepcopy(pista_destino)

                    # Remove voo da origem
                    voo_removido = nova_pista_origem.sequencia.pop(idx_voo)

                    # Insere na posição 'pos' da pista destino
                    nova_pista_destino.sequencia.insert(pos, voo_removido)

                    # Monta nova configuração
                    nova_configuracao = []
                    for k in range(n):
                        if k == i:
                            nova_configuracao.append(nova_pista_origem)
                        elif k == j:
                            nova_configuracao.append(nova_pista_destino)
                        else:
                            nova_configuracao.append(deepcopy(pistas[k]))

                    custo = calcular_custo_total(nova_configuracao, dados)

                    if custo < menor_custo:
                        menor_custo = custo
                        melhor_vizinho = nova_configuracao

    return melhor_vizinho, menor_custo
