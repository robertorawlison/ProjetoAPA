import os
from alocacao import alocar_voos, Construcao
from vizinhancas.vnd import VND
from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap11_intra import swap_1_1_intrarrotas
from vizinhancas.swap22_inter import swap_2_2_interrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas
from vizinhancas.reinsertion_intra import reinsertion_intrarrotas
from utils import calcular_custo_total

def grasp(instancia, alpha, grasp_max):
    melhor_solucao = None
    melhor_custo = float('inf')

    for _ in range(grasp_max):
        # Fase de construção com critério alpha
        solucao, dados = Construcao(instancia, alpha)

        # Fase de busca local (VND)
        solucao = VND(solucao, dados)  # VND é chamada aqui

        # Avalia a solução
        custo_atual = calcular_custo_total(solucao, dados)

        if custo_atual < melhor_custo:
            melhor_solucao = solucao
            melhor_custo = custo_atual

    return melhor_solucao, melhor_custo

PASTA_INSTANCIAS = "instancias_teste"
ARQUIVO_SAIDA = "resultados_comparacao.csv"

with open(ARQUIVO_SAIDA, "w") as f_saida:
    f_saida.write("instancia;guloso;vnd\n")

    for nome_arquivo in sorted(os.listdir(PASTA_INSTANCIAS)):
        if nome_arquivo.endswith(".txt"):
            caminho = os.path.join(PASTA_INSTANCIAS, nome_arquivo)

            print(f"📄 Processando {nome_arquivo}...")
            
            try:
                # Executa o algoritmo guloso
                pistas_gulosas, custo_guloso, dados = alocar_voos(caminho)

                # Executa o VND
                pistas_vnd, custo_vnd = VND(pistas_gulosas, custo_guloso, dados)

                # Executa o GRASP
                melhor_solucao, melhor_custo = grasp(dados, 0.1, 1000)

                # Escreve os resultados no arquivo de saída
                f_saida.write(f"{nome_arquivo},{custo_guloso},{custo_vnd}, {melhor_custo}\n")
                
                print(f"✅ Resultados salvos para {nome_arquivo}.")

            except Exception as e:
                print(f"❌ Erro ao processar {nome_arquivo}: {e}")                

