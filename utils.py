import sys
from contextlib import contextmanager
import os

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

def print_resultados(pistas, multa_total, dados, tipo):
    output = ""
    for pista in pistas:
        output += f"\n{pista.pista}:\n"
        tempo_atual = 0
        for i,voo in enumerate(pista.sequencia):
            if i==0:
                tempo_atual = max(voo.tempo_liberacao,tempo_atual)
            else:
                anterior = pista.sequencia[i-1].id
                tempo_atual +=dados.tempos_espera[anterior][voo.id]
                tempo_atual = max(voo.tempo_liberacao,tempo_atual)
            
            multa = calcular_multa(tempo_atual,voo)
            output += f"  Voo {voo.nome} (ID: {voo.id}) - Tempo de inicio: {tempo_atual}, Custo: {multa}\n"
            tempo_atual += voo.custo

    output += f"\nCusto total da alocacao_{tipo}: {multa_total}\n"
    return output 


@contextmanager
def silenciar_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout