import heapq
from dataclasses import dataclass
from typing import List
from utils import calcular_multa
from read_document import ler_dados
from random import choice

@dataclass
class Voo:
    nome:str
    id:int
    custo:int
    tempo_liberacao:int
    penalidade:int

@dataclass
class Alocacao:
    pista:str
    sequencia:List[Voo]

def alocar_voos(instancia):
    dados = ler_dados(instancia)
    voos = [
        Voo(
            nome=f"QUICK{i+1}",
            id=i,
            custo=dados.custos_operacao[i],
            tempo_liberacao = dados.tempos_pouso_decolagem[i],
            penalidade = dados.penalidades_atraso[i]
        )
        for i in range(dados.n_voos)
    ]

    voos.sort(key=lambda v: v.tempo_liberacao)
    heap = [(0,i) for i in range(dados.n_pistas)]
    heapq.heapify(heap)

    pistas = [Alocacao(pista=f"Pista {i+1}", sequencia=[]) for i in range(dados.n_pistas)]
    tempo_pistas = [0] * dados.n_pistas
    ultimo_voo_pista = [-1] * dados.n_pistas
    custo_total = 0

    for voo in voos:
        tempo_disponivel, pista_id = heapq.heappop(heap)

        if ultimo_voo_pista[pista_id] != -1:
            anterior = ultimo_voo_pista[pista_id]
            tempo_disponivel +=dados.tempos_espera[anterior][voo.id]
        
        inicio_real = max(tempo_disponivel,voo.tempo_liberacao)

        multa = calcular_multa(inicio_real,voo)
        custo_total+=multa

        pistas[pista_id].sequencia.append(voo)
        tempo_pistas[pista_id] = inicio_real + voo.custo
        ultimo_voo_pista[pista_id] = voo.id

        heapq.heappush(heap,(tempo_pistas[pista_id],pista_id))
    
    for pista in pistas:
        print(f"{pista.pista}")
        tempo_atual = 0
        for i,voo in enumerate(pista.sequencia):
            if i==0:
                tempo_atual = max(voo.tempo_liberacao,tempo_atual)
            else:
                anterior = pista.sequencia[i-1].id
                tempo_atual +=dados.tempos_espera[anterior][voo.id]
                tempo_atual = max(voo.tempo_liberacao,tempo_atual)
            
            multa = calcular_multa(tempo_atual,voo)
            print(f"  {voo.nome}  (Início: {tempo_atual}, Multa: {multa})")
            tempo_atual+=voo.custo  
    
    print(f"\nCusto total da alocação: {custo_total}\n")
    return pistas, custo_total, dados

# função da fase de construção do GRASP
def Construcao(instancia, alpha=0.7):
    dados = ler_dados(instancia)
    
    voos_disponiveis = [
        Voo(
            nome=f"QUICK{i+1}",
            id=i,
            custo=dados.custos_operacao[i],
            tempo_liberacao=dados.tempos_pouso_decolagem[i],
            penalidade=dados.penalidades_atraso[i]
        )
        for i in range(dados.n_voos)
    ]
    
    pistas = [Alocacao(pista=f"Pista {i+1}", sequencia=[]) for i in range(dados.n_pistas)]
    tempo_pistas = [0] * dados.n_pistas
    ultimo_voo_pista = [-1] * dados.n_pistas
    custo_total = 0

    while voos_disponiveis:
        # Ordena voos por critério guloso (tempo de liberação)
        voos_disponiveis.sort(key=lambda v: v.tempo_liberacao)
        min_val = voos_disponiveis[0].tempo_liberacao
        max_val = voos_disponiveis[-1].tempo_liberacao
        limite = min_val + alpha * (max_val - min_val)

        # Cria LCR com voos cujo tempo de liberação <= limite
        LCR = [v for v in voos_disponiveis if v.tempo_liberacao <= limite]

        # Seleciona aleatoriamente um voo da LCR
        voo = choice(LCR)
        voos_disponiveis.remove(voo)

        # Escolhe a melhor pista (com menor tempo disponível)
        melhor_pista = -1
        melhor_inicio = float('inf')
        menor_multa = float('inf')

        for i in range(dados.n_pistas):
            tempo_disponivel = tempo_pistas[i]

            if ultimo_voo_pista[i] != -1:
                anterior = ultimo_voo_pista[i]
                tempo_disponivel += dados.tempos_espera[anterior][voo.id]

            inicio_real = max(tempo_disponivel, voo.tempo_liberacao)
            multa = calcular_multa(inicio_real, voo)

            if multa < menor_multa:
                melhor_pista = i
                melhor_inicio = inicio_real
                menor_multa = multa

        # Aloca o voo na melhor pista
        pistas[melhor_pista].sequencia.append(voo)
        tempo_pistas[melhor_pista] = melhor_inicio + voo.custo
        ultimo_voo_pista[melhor_pista] = voo.id
        custo_total += menor_multa

    # Exibição final
    for pista in pistas:
        tempo_atual = 0
        for i, voo in enumerate(pista.sequencia):
            if i == 0:
                tempo_atual = max(voo.tempo_liberacao, tempo_atual)
            else:
                anterior = pista.sequencia[i-1].id
                tempo_atual += dados.tempos_espera[anterior][voo.id]
                tempo_atual = max(voo.tempo_liberacao, tempo_atual)

            multa = calcular_multa(tempo_atual, voo)
            tempo_atual += voo.custo  

    return pistas, custo_total, dados
