import heapq
from dataclasses import dataclass
from typing import List
from utils import calcular_multa
from read_document import ler_dados

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
