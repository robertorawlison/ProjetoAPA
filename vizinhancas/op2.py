from copy import deepcopy
from utils import calcular_custo_total  # Ou ajuste para onde estiver sua função
# Certifique-se de passar os dados corretamente quando chamar esta função

def two_opt_intra(pistas, dados):
    melhor_config = None
    menor_custo = float('inf')

    for pista in pistas:
        sequencia = pista.sequencia
        n = len(sequencia)

        for i in range(n - 1):
            for j in range(i + 1, n):
                nova_sequencia = deepcopy(sequencia)
                nova_sequencia[i:j+1] = reversed(nova_sequencia[i:j+1])  # Inverte o trecho i até j

                nova_pista = deepcopy(pista)
                nova_pista.sequencia = nova_sequencia

                nova_config = []
                for outra in pistas:
                    if outra.pista == pista.pista:
                        nova_config.append(nova_pista)
                    else:
                        nova_config.append(deepcopy(outra))

                custo = calcular_custo_total(nova_config, dados)
                if custo < menor_custo:
                    menor_custo = custo
                    melhor_config = nova_config

    return melhor_config, menor_custo
