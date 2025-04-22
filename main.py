import os
from alocacao import alocar_voos
from vizinhancas.vnd import VND
from GRASP import GRASP
from utils import print_resultados, silenciar_stdout

PASTA_INSTANCIAS = "instancias_teste"

for nome_arquivo in sorted(os.listdir(PASTA_INSTANCIAS)):
    if nome_arquivo.endswith(".txt"):
        caminho = os.path.join(PASTA_INSTANCIAS, nome_arquivo)

        with open(f"resultados/{nome_arquivo}", "w") as f_saida:
            try:
                with silenciar_stdout():
                    # Executa o algoritmo guloso
                    pistas_gulosas, custo_guloso, dados = alocar_voos(caminho)
                    saida = print_resultados(pistas_gulosas, custo_guloso, dados, "Guloso")
                    f_saida.write(saida)

                    # Executa o VND
                    pistas_vnd, custo_vnd = VND(pistas_gulosas, custo_guloso, dados)
                    saida = print_resultados(pistas_vnd, custo_vnd, dados, "VND")
                    f_saida.write(saida)

                    # Executa o GRASP
                    pistas_grasp, custo_grasp, media = GRASP(caminho)
                    saida = print_resultados(pistas_grasp, custo_grasp, dados, "GRASP")
                    f_saida.write(saida)

            except Exception as e:
                f_saida.write(f"Erro ao processar {nome_arquivo}: {e}\n")






