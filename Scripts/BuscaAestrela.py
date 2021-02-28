# Módulo para Buscas

import Ambiente
import Aspirador
from math import sqrt, pow


def busca_aestrela(aspirador, ambiente, conf_ambiente):
    descobertos = []

    # Pega o número de destinos encontrados na busca em largura
    visitados = len(aspirador[2])
    while visitados > 0:

        # Destino que o aspirador vai procurar
        destino = aspirador[2][0]

        # Calcular a disntcia de todos para o destino
        calc_distancia(destino, conf_ambiente)

        # Criando filhos
        conf_ambiente = criar_filhos(aspirador, conf_ambiente, ambiente, descobertos)

        # Procurando o menor de todos os descobertos
        menor_descobertos, pos_descobertos = encontrar_menor(descobertos)

        # Remove o menor, pois ele irá gerar filhos
        descobertos.pop(pos_descobertos)

        # Procurando o menor de todos os filhos dó nós atual
        menor, pos = encontrar_menor(conf_ambiente[aspirador[0]][aspirador[1]][4])

        # Verifcando se o menor de todos está no nó atual e procurando em qual nó está o menor
        # Tem um menor em outro lugar.O menor da lista está nesse pai?Se não entra
        while menor != menor_descobertos and len(aspirador[2]) != 0:
            if ambiente[aspirador[0]][aspirador[1]] == 1:
                Aspirador.aspirar(aspirador[0], aspirador[1], ambiente)

            pai = conf_ambiente[aspirador[0]][aspirador[1]][1]

            aspirador = Aspirador.andar(aspirador, pai, ambiente)
            Ambiente.imprimir_matriz(ambiente)

            # Após subir na árvore verifica se o menor está no pai
            menor, pos = encontrar_menor(conf_ambiente[aspirador[0]][aspirador[1]][4])

        # O menor está no nó atual
        # Aspirador anda para posição que contém o menor f(n)

        Ambiente.imprimir_matriz(ambiente)
        aspirador = Aspirador.andar(aspirador, conf_ambiente[aspirador[0]][aspirador[1]][2][pos], ambiente)

        # Se aspirador chegou ao destino remove o destino da lista
        if conf_ambiente[aspirador[0]][aspirador[1]][1] == destino:
            print('Aspirador chegou em 1 dos destinos')
            aspirador[2].pop(0)
            visitados = visitados - 1

            # Reiniciando configuarção para iniciar com outro destino
            conf_ambiente = Ambiente.criar_confambiente(ambiente)

        input('Verifique e pressione <enter> para continuar')

    print('Aspirador poercorreu todos os destinos')
    Ambiente.imprimir_matriz(ambiente)
    Ambiente.verificar_limpeza(ambiente)


def calc_distancia(destino, conf_ambiente):
    linha = len(conf_ambiente)
    coluna = len(conf_ambiente[0])

    for i in range(linha):
        for j in range(coluna):
            elemento1 = i - destino[0]
            elemento2 = j - destino[1]
            elemento1 = pow(elemento1, 2)
            elemento2 = pow(elemento2, 2)
            distancia = sqrt(elemento1 + elemento2)
            conf_ambiente[i][j][6] = distancia

    print(f'Destino {destino}')
    return


def encontrar_menor(lista):
    tamanho = len(lista)

    menor = lista[0]

    for i in range(tamanho):
        if lista[i] <= menor:
            menor = lista[i]
            pos = i
    return menor, pos


def criar_filhos(aspirador, conf_ambiente, ambiente, descobertos):
    # Frente
    # Verifica se está na parede
    if aspirador[0] + 1 != len(conf_ambiente):
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        # if conf_ambiente[aspirador[0] + 1][aspirador[1]][3] == 0:
        # Verifica se tem móvel
        if ambiente[aspirador[0] + 1][aspirador[1]] != -1:
            # Marca sendo pai do próximo nó
            conf_ambiente[aspirador[0] + 1][aspirador[1]][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
            # Adiociona o proximo no na lista de filhos
            conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0] + 1][aspirador[1]][0])
            # Coloca o g(n) no próximo nó
            conf_ambiente[aspirador[0] + 1][aspirador[1]][5] = conf_ambiente[aspirador[0]][aspirador[1]][3] + 1
            # Coloca o h(n) + g(n) do próximo nó, no pai
            conf_ambiente[aspirador[0]][aspirador[1]][4].append(conf_ambiente[aspirador[0] + 1][aspirador[1]][5] +
                                                                conf_ambiente[aspirador[0] + 1][aspirador[1]][6])
            # Coloca o valor de f(n) na lista de descobertos
            descobertos.append(conf_ambiente[aspirador[0] + 1][aspirador[1]][5] +
                               conf_ambiente[aspirador[0] + 1][aspirador[1]][6])

    # Direita
    # Verifica se está na parede
    if aspirador[1] + 1 != len(conf_ambiente[0]):
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        # if conf_ambiente[aspirador[0]][aspirador[1] + 1][3] == 0:
        # Verifica se tem móvel
        if ambiente[aspirador[0]][aspirador[1] + 1] != -1:
            # Marca sendo pai do próximo nó
            conf_ambiente[aspirador[0]][aspirador[1] + 1][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
            # Adiociona o proximo no na lista de filhos
            conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0]][aspirador[1] + 1][0])
            # Coloca o g(n) no próximo nó
            conf_ambiente[aspirador[0]][aspirador[1] + 1][5] = conf_ambiente[aspirador[0]][aspirador[1]][3] + 1
            # Coloca o h(n) + g(n) do próximo nó, no pai
            conf_ambiente[aspirador[0]][aspirador[1]][4].append(conf_ambiente[aspirador[0]][aspirador[1] + 1][5] +
                                                                conf_ambiente[aspirador[0]][aspirador[1] + 1][6])
            # Coloca o valor de f(n) na lista de descobertos
            descobertos.append(conf_ambiente[aspirador[0]][aspirador[1] + 1][5] +
                               conf_ambiente[aspirador[0]][aspirador[1] + 1][6])

    # tras
    # Verifica se está na parede
    if aspirador[0] != 0:
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        # if conf_ambiente[aspirador[0] - 1][aspirador[1]][3] == 0:
        # Verifica se tem móvel
        if ambiente[aspirador[0] - 1][aspirador[1]] != -1:
            # Marca sendo pai do próximo nó
            conf_ambiente[aspirador[0] - 1][aspirador[1]][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
            # Adiociona o proximo no na lista de filhos
            conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0] - 1][aspirador[1]][0])
            # Coloca o g(n) no próximo nó
            conf_ambiente[aspirador[0] - 1][aspirador[1]][5] = conf_ambiente[aspirador[0]][aspirador[1]][3] + 1
            # Coloca o h(n) + g(n) do próximo nó, no pai
            conf_ambiente[aspirador[0]][aspirador[1]][4].append(conf_ambiente[aspirador[0] - 1][aspirador[1]][5] +
                                                                conf_ambiente[aspirador[0] - 1][aspirador[1]][6])
            # Coloca o valor de f(n) na lista de descobertos
            descobertos.append(conf_ambiente[aspirador[0] - 1][aspirador[1]][5] +
                               conf_ambiente[aspirador[0] - 1][aspirador[1]][6])

    # Esquerda
    # Verifica se está na parede
    if aspirador[1] != 0:
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        # if conf_ambiente[aspirador[0]][aspirador[1] - 1][3] == 0:
        # Verifica se tem móvel
        if ambiente[aspirador[0]][aspirador[1] - 1] != -1:
            # Marca sendo pai do próximo nó
            conf_ambiente[aspirador[0]][aspirador[1] - 1][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
            # Adiociona o proximo no na lista de filhos
            conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0]][aspirador[1] - 1][0])
            # Coloca o g(n) no próximo nó
            conf_ambiente[aspirador[0]][aspirador[1] - 1][5] = conf_ambiente[aspirador[0]][aspirador[1]][3] + 1
            # Coloca o h(n) + g(n) do próximo nó, no pai
            conf_ambiente[aspirador[0]][aspirador[1]][4].append(conf_ambiente[aspirador[0]][aspirador[1] - 1][5] +
                                                                conf_ambiente[aspirador[0]][aspirador[1] - 1][6])
            # Coloca o valor de f(n) na lista de descobertos
            descobertos.append(conf_ambiente[aspirador[0]][aspirador[1] - 1][5] +
                               conf_ambiente[aspirador[0]][aspirador[1] - 1][6])

    # Se não conseguir criar filho nenhum, marque como visitado
    if len(conf_ambiente[aspirador[0]][aspirador[1]][2]) == 0:
        conf_ambiente[aspirador[0]][aspirador[1]][3] = 'visitado'
        return 0
    else:
        return conf_ambiente
