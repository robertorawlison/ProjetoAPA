import os
from alocacao import alocar_voos, Construcao
from read_document import ler_dados
from vizinhancas.vnd import VND
from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap11_intra import swap_1_1_intrarrotas
from vizinhancas.swap22_inter import swap_2_2_interrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas
from vizinhancas.reinsertion_intra import reinsertion_intrarrotas
from utils import calcular_custo_total
import math
import sys
from contextlib import contextmanager

@contextmanager
def silenciar_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout
        

def GRASP(instancia, max_iter=50, alpha=0.3):
    melhor_solucao = None
    melhor_custo = float('inf')

    for _ in range(max_iter):
        # Fase de construção com aleatoriedade e alpha
        pistas, custo_total, dados = Construcao(instancia, alpha)

        # Fase de melhoria com VND
        pistas_vnd, custo_vnd = VND(pistas, custo_total, dados)

        # Verifica se a solução melhorou
        if custo_vnd < melhor_custo:
            melhor_custo = custo_vnd
            melhor_solucao = pistas_vnd

    return melhor_solucao, melhor_custo


PASTA_INSTANCIAS = "instancias_teste"
ARQUIVO_SAIDA = "resultados_comparacao.txt"

# Abre o arquivo para escrita (cria ou substitui)
with open(ARQUIVO_SAIDA, "w") as f_saida:
    f_saida.write("╔════════════════════════════════════════════════════╗\n")
    f_saida.write("║              RESULTADOS DAS INSTÂNCIAS             ║\n")
    f_saida.write("╠════════════════════════════════════════════════════╣\n")
    f_saida.write("║ Instância           │  Guloso  │   VND   │  GRASP  ║\n")
    f_saida.write("╠═════════════════════╪══════════╪═════════╪═════════╣\n")

    for nome_arquivo in sorted(os.listdir(PASTA_INSTANCIAS)):
        if nome_arquivo.endswith(".txt"):
            caminho = os.path.join(PASTA_INSTANCIAS, nome_arquivo)

            try:
                with silenciar_stdout():
                    # Executa o algoritmo guloso
                    pistas_gulosas, custo_guloso, dados = alocar_voos(caminho)

                    # Executa o VND
                    pistas_vnd, custo_vnd = VND(pistas_gulosas, custo_guloso, dados)

                    # Executa o GRASP
                    melhor_solucao, melhor_custo = GRASP(caminho)

                # Grava os resultados no arquivo
                f_saida.write(f"║ {nome_arquivo:<20}│ {custo_guloso:>8} │ {custo_vnd:>7} │ {melhor_custo:>7} ║\n")

            except Exception as e:
                f_saida.write(f"❌ Erro ao processar {nome_arquivo}: {e}\n")

    f_saida.write("╚════════════════════════════════════════════════════╝\n")

