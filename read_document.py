class Dados:
    def __init__(self):
        self.n_voos = 0
        self.n_pistas = 0
        self.tempos_pouso_decolagem = []
        self.custos_operacao = []
        self.penalidades_atraso = []
        self.tempos_espera = []

def ler_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as f:
            linhas = [linha.strip() for linha in f if linha.strip() != '']

        dados = Dados()
        dados.n_voos = int(linhas[0])
        dados.n_pistas = int(linhas[1])

        dados.tempos_pouso_decolagem = list(map(int, linhas[2].split()))
        dados.custos_operacao = list(map(int, linhas[3].split()))
        dados.penalidades_atraso = list(map(int, linhas[4].split()))

        dados.tempos_espera = []
        for linha in linhas[5:5 + dados.n_voos]:
            dados.tempos_espera.append(list(map(int, linha.split())))

        return dados


    except FileNotFoundError:
        print("Erro ao abrir o arquivo!")
        exit(1)
