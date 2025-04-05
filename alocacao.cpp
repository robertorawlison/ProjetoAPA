#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include "read_document.h"

struct Voo {
    std::string nome;
    int id;
    int custo;
    int tempo_liberacao;
    int penalidade;
    bool alocado = false;
};

struct Alocacao {
    std::string pista;
    std::vector<Voo> sequencia;
};

int calcularMulta(int inicio_real, const Voo& v) {
    int atraso = std::max(0, inicio_real - v.tempo_liberacao);
    return atraso * v.penalidade;
}

int main() {
    Dados dados = lerDados("document/instace.txt");

    std::vector<Voo> voos;
    for (int i = 0; i < dados.n_voos; ++i) {
        voos.push_back({"QUICK" + std::to_string(i + 1), i,
                        dados.custos_operacao[i],
                        dados.tempos_pouso_decolagem[i],
                        dados.penalidades_atraso[i]});
    }

    // Ordena por tempo de início (tempo_liberacao)
    std::sort(voos.begin(), voos.end(), [](const Voo& a, const Voo& b) {
        return a.tempo_liberacao < b.tempo_liberacao;
    });

    std::vector<Alocacao> pistas = { {"Pista 1", {}}, {"Pista 2", {}} };
    std::vector<int> tempo_pistas(2, 0);
    std::vector<int> ultimo_voo_pista(2, -1);

    int custo_total = 0;

    for (Voo& v : voos) {
        int melhor_pista = -1;
        int melhor_inicio = INT_MAX;

        for (int p = 0; p < 2; ++p) {
            int tempo_disponivel = tempo_pistas[p];
            if (ultimo_voo_pista[p] != -1)
                tempo_disponivel += dados.tempos_espera[ultimo_voo_pista[p]][v.id];

            int tempo_inicio = std::max(tempo_disponivel, v.tempo_liberacao);
            if (tempo_inicio < melhor_inicio) {
                melhor_inicio = tempo_inicio;
                melhor_pista = p;
            }
        }

        int multa = calcularMulta(melhor_inicio, v);
        custo_total += multa;

        pistas[melhor_pista].sequencia.push_back(v);
        tempo_pistas[melhor_pista] = melhor_inicio + v.custo;
        ultimo_voo_pista[melhor_pista] = v.id;
    }

    for (auto& pista : pistas) {
        std::cout << pista.pista << ":\n";
        int tempo_pista = 0;
        for (size_t i = 0; i < pista.sequencia.size(); ++i) {
            Voo& v = pista.sequencia[i];
            if (i == 0) {
                tempo_pista = std::max(v.tempo_liberacao, tempo_pista);
            } else {
                int anterior = pista.sequencia[i - 1].id;
                tempo_pista += dados.tempos_espera[anterior][v.id];
                tempo_pista = std::max(v.tempo_liberacao, tempo_pista);
            }
            int multa = calcularMulta(tempo_pista, v);
            std::cout << "  " << v.nome << " (Início: " << tempo_pista << ", Multa: " << multa << ")\n";
            tempo_pista += v.custo;
        }
    }

    std::cout << "\nCusto total da heurística baseada no tempo de início: " << custo_total << "\n";
    return 0;
}
