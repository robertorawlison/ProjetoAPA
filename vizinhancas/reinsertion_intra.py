from copy import deepcopy
from utils import calcular_custo_total

def reinsertion_intrarrotas(pistas, dados):
    melhor_vizinho = deepcopy(pistas)
    menor_custo = calcular_custo_total(pistas, dados)

    n = len(pistas)

    for i in range(n):
        pista_mudanca = pistas[i]
        for idx_voo in range(len(pista_mudanca.sequencia)):
            for pos in range(len(pista_mudanca.sequencia) + 1):
                if idx_voo == pos:
                    continue
                nova_pista = deepcopy(pista_mudanca)

                # Remove voo da origem
                nova_pista.sequencia.pop(idx_voo)
                # Adiciona voo na nova posição
                nova_pista.sequencia.insert(pos, pista_mudanca.sequencia[idx_voo])

                # Monta nova configuração
                nova_configuracao = []
                for k in range(n):
                    if k == i:
                        nova_configuracao.append(nova_pista)
                    else:
                        nova_configuracao.append(deepcopy(pistas[k]))

                custo = calcular_custo_total(nova_configuracao, dados)

                if custo < menor_custo:
                    menor_custo = custo
                    melhor_vizinho = nova_configuracao
        
        return melhor_vizinho, menor_custo

                