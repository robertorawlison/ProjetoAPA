import os
from alocacao import alocar_voos, Construcao
from vizinhancas.vnd import VND
from utils import silenciar_stdout
from statistics import mean

def GRASP(instancia, max_iter=5, alpha=0.7):
    melhor_solucao = None
    melhor_custo = float('inf')

    sum_custo_vnd = 0

    for i in range(max_iter):
        # Fase de construção com aleatoriedade e alpha
        pistas, custo_total, dados = Construcao(instancia, alpha)

        # Fase de melhoria com VND
        pistas_vnd, custo_vnd = VND(pistas, custo_total, dados)

        sum_custo_vnd += custo_vnd

        # Verifica se a solução melhorou
        if custo_vnd < melhor_custo:
            melhor_custo = custo_vnd
            melhor_solucao = pistas_vnd

    media_custo_vnd = sum_custo_vnd / max_iter

    return melhor_solucao, melhor_custo, media_custo_vnd

'''# Configurações
PASTA_INSTANCIAS = "instancias_teste"
alphas = [0.7, 0.8]

# Cabeçalho
print("╔════════════════════════════════════════════════════════════════════════════════════╗")
print("║              RESULTADOS DAS INSTÂNCIAS PARA DIFERENTES VALORES DE ALPHA            ║")
print("╠════════════════════════════════════════════════════════════════════════════════════╣")
print("║ Instância           │  Guloso  │   VND   │  GRASP  │ Alpha │                       ║")
print("╠═════════════════════╪══════════╪═════════╪═════════╪═══════╪═══════════════════════╣")

# Dicionário para acumular custos por alpha
custos_por_alpha = {alpha: [] for alpha in alphas}

# Loop pelos alphas
for alpha in alphas:
    for nome_arquivo in sorted(os.listdir(PASTA_INSTANCIAS)):
        if nome_arquivo.endswith(".txt"):
            caminho = os.path.join(PASTA_INSTANCIAS, nome_arquivo)
            try:
                with silenciar_stdout():
                    pistas_gulosas, custo_guloso, dados = alocar_voos(caminho)
                    pistas_vnd, custo_vnd = VND(pistas_gulosas, custo_guloso, dados)
                    _, custo_grasp, media = GRASP(caminho, alpha=alpha)
                custos_por_alpha[alpha].append(custo_grasp)

                print(f"║ {nome_arquivo:<20}│ {custo_guloso:>8} │ {custo_vnd:>7} │ {custo_grasp:>7} │ {alpha:>5.2f} │")
            except Exception as e:
                print(f"❌ Erro ao processar {nome_arquivo} com alpha {alpha}: {e}")

print("╚════════════════════════════════════════════════════════════════════════════════════╝\n")

# Cálculo das médias
print("╔════════════╦══════════════════════╗")
print("║   Alpha    ║ Média do GRASP       ║")
print("╠════════════╬══════════════════════╣")
melhor_alpha = None
melhor_media = float('inf')

for alpha, custos in custos_por_alpha.items():
    if custos:
        media = mean(custos)
        print(f"║   {alpha:<6.2f}   ║ {media:>20.2f} ║")
        if media < melhor_media:
            melhor_media = media
            melhor_alpha = alpha
    else:
        print(f"║   {alpha:<6.2f}   ║     Sem dados       ║")

print("╚════════════╩══════════════════════╝")
print(f"\n🏆 Melhor alpha com menor média de custo GRASP: **{melhor_alpha:.2f}** (média = {melhor_media:.2f})")'''