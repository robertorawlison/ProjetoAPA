def calcular_multa(inicio_real, voo):
    atraso = max(0,inicio_real - voo.tempo_liberacao)
    return atraso*voo.penalidade

def calcular_custo_total(pistas, dados):
    custo_total = 0

    for pista in pistas:
        tempo_pista = 0
        for i, voo in enumerate(pista.sequencia):
            if i == 0:
                tempo_pista = max(voo.tempo_liberacao, tempo_pista)
            else:
                anterior = pista.sequencia[i - 1].id
                tempo_pista += dados.tempos_espera[anterior][voo.id]
                tempo_pista = max(voo.tempo_liberacao, tempo_pista)
            multa = calcular_multa(tempo_pista, voo)
            custo_total += multa
            tempo_pista += voo.custo

    return custo_total