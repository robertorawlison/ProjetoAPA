import pandas as pd
import os
import time
from alocacao import alocar_voos
from vizinhancas.vnd import VND
from GRASP import GRASP

def gap(solucao, solucao_otima):
    return ((solucao - solucao_otima) / solucao_otima) * 100 if solucao_otima > 0 else -1.0

def gera_tabela_gap(df_otimo, caminho_saida='gap.csv'):
    # Verifica se o arquivo já existe para evitar recriar o cabeçalho
    if os.path.exists(caminho_saida):
        df_gap = pd.read_csv(caminho_saida)
    else:
        df_gap = pd.DataFrame()

    for nome_arquivo in sorted(os.listdir('instancias_teste')):
            if nome_arquivo.endswith(".txt"):
                caminho = os.path.join('instancias_teste', nome_arquivo)
                print(f"Processando arquivo: {caminho}")
                
                otimo_val = df_otimo.loc[df_otimo['Instancia'] == nome_arquivo, 'Otimo'].values[0]
                tag_otimo = df_otimo.loc[df_otimo['Instancia'] == nome_arquivo, 'Tag otimo'].values[0]
                # Executa o algoritmo guloso
                inicio_guloso = time.time()
                pistas_gulosas, custo_guloso, dados = alocar_voos(caminho)
                fim_guloso = time.time()
                gap_guloso = gap(custo_guloso, df_otimo.loc[df_otimo['Instancia'] == nome_arquivo, 'Otimo'].values[0])


                # Executa o VND
                inicio_vnd = time.time()
                pistas_vnd, custo_vnd = VND(pistas_gulosas, custo_guloso, dados)
                fim_vnd = time.time()
                gap_vnd = gap(custo_vnd, df_otimo.loc[df_otimo['Instancia'] == nome_arquivo, 'Otimo'].values[0])

                # Executa o GRASP
                inicio_grasp = time.time()
                melhor_solucao, melhor_custo, media = GRASP(caminho)
                fim_grasp = time.time()
                gap_grasp = gap(melhor_custo, df_otimo.loc[df_otimo['Instancia'] == nome_arquivo, 'Otimo'].values[0])



                nova_linha = pd.DataFrame([{
                'Instancia': nome_arquivo,
                'Otimo': otimo_val,
                'Tag otimo': tag_otimo,
                'Solucao (HC)': custo_guloso,
                'Tempo (HC)(s)': (fim_guloso - inicio_guloso),
                'Gap (HC)': round(gap_guloso, 2),
                'Solucao (VND)': custo_vnd,
                'Tempo (VND)(s)': (fim_vnd - inicio_vnd),
                'Gap (VND)': round(gap_vnd, 2),
                'Solucao (GRASP)': melhor_custo,
                'Tempo (GRASP)(s)': (fim_grasp - inicio_grasp),
                'Gap (GRASP)': round(gap_grasp, 2),
                'Solucao Media (GRASP)': media,
                }])
                df_gap = pd.concat([df_gap, nova_linha], ignore_index=True)

    df_gap.to_csv('gap.csv',sep=',',index=False)


otimo = pd.DataFrame({
    'Instancia' : ['n3m10A.txt','n3m10B.txt','n3m10C.txt','n3m10D.txt',
                   'n3m10E.txt','n3m20A.txt','n3m20B.txt','n3m20C.txt',
                   'n3m20D.txt','n3m20E.txt','n3m40A.txt','n3m40B.txt',
                   'n3m40C.txt','n3m40D.txt','n3m40E.txt','n5m50A.txt',
                   'n5m50B.txt','n5m50C.txt','n5m50D.txt','n5m50E.txt'],
    'Otimo' : [7483,1277,2088,322,3343,8280,1820,855,4357,3798,
              112,880,1962,263,1192,0,0,0,0,0],
    'Tag otimo' : ["opt","opt","opt","opt","opt", "LB","LB","LB","opt","opt",
                   "LB","LB","LB","LB","LB","LB","LB","LB","LB","LB",]
                   })

gera_tabela_gap(otimo)
