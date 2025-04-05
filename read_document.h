#ifndef LEITURA_DADOS_H
#define LEITURA_DADOS_H

#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>

struct Dados {
    int n_voos;
    int n_pistas;
    std::vector<int> tempos_pouso_decolagem;
    std::vector<int> custos_operacao;
    std::vector<int> penalidades_atraso;
    std::vector<std::vector<int>> tempos_espera;
};

Dados lerDados(const std::string& caminhoArquivo) {
    std::ifstream arquivo(caminhoArquivo);
    if (!arquivo) {
        std::cerr << "Erro ao abrir o arquivo!" << std::endl;
        exit(1);
    }

    Dados dados;
    arquivo >> dados.n_voos >> dados.n_pistas;
    arquivo.ignore();

    std::string linha;
    std::getline(arquivo, linha); // Linha vazia

    dados.tempos_pouso_decolagem.resize(dados.n_voos);
    dados.custos_operacao.resize(dados.n_voos);
    dados.penalidades_atraso.resize(dados.n_voos);
    dados.tempos_espera.resize(dados.n_voos, std::vector<int>(dados.n_voos));

    std::getline(arquivo, linha);
    std::istringstream ss1(linha);
    for (int i = 0; i < dados.n_voos; i++) {
        ss1 >> dados.tempos_pouso_decolagem[i];
    }

    std::getline(arquivo, linha);
    std::istringstream ss2(linha);
    for (int i = 0; i < dados.n_voos; i++) {
        ss2 >> dados.custos_operacao[i];
    }

    std::getline(arquivo, linha);
    std::istringstream ss3(linha);
    for (int i = 0; i < dados.n_voos; i++) {
        ss3 >> dados.penalidades_atraso[i];
    }

    std::getline(arquivo, linha); // Ignora linha vazia

    for (int i = 0; i < dados.n_voos; i++) {
        for (int j = 0; j < dados.n_voos; j++) {
            arquivo >> dados.tempos_espera[i][j];
        }
    }

    arquivo.close();
    return dados;
}

#endif
