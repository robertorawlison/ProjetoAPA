import os
from alocacao import alocar_voos
from vizinhancas.vnd import VND
from vizinhancas.swap11_inter import swap_1_1_interrotas
from vizinhancas.swap11_intra import swap_1_1_intrarrotas
from vizinhancas.swap22_inter import swap_2_2_interrotas
from vizinhancas.reinsertion_inter import reinsertion_interrotas
from vizinhancas.reinsertion_intra import reinsertion_intrarrotas


'''Script para comparar o desempenho do algoritmo 
guloso e do VND na alocação de voos em pistas de aeroporto.
So precisa rodar se mudar algumca coisa no arquivo do vnd.py
Ele roda todas as instancias que tem na pasta instancias_teste
e salva os resultados em um arquivo csv'''

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

                # Escreve os resultados no arquivo de saída
                f_saida.write(f"{nome_arquivo},{custo_guloso},{custo_vnd}\n")
                
                print(f"✅ Resultados salvos para {nome_arquivo}.")

            except Exception as e:
                print(f"❌ Erro ao processar {nome_arquivo}: {e}")                




