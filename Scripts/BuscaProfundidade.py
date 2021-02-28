# Módulo para Buscas

import Ambiente
import Aspirador


def busca_profundidade(aspirador, ambiente, conf_ambiente):
    visitados = 0
    conf_ambiente[aspirador[0]][aspirador[1]][3] = 'marcado'
    base = (aspirador[0], aspirador[1])

    while not visitados:
        Ambiente.imprimir_matriz(ambiente)

        if criar_filhos(aspirador, conf_ambiente, ambiente):
            aspirador = Aspirador.andar(aspirador, conf_ambiente[aspirador[0]][aspirador[1]][2][0], ambiente)

        else:
            if ambiente[aspirador[0]][aspirador[1]] == 1:
                Aspirador.aspirar(aspirador[0], aspirador[1], ambiente)

            # Na base ele não tem pai, e para o processo.
            if (aspirador[0], aspirador[1]) != base:
                # Chegou em um nó folha, retorna para o pai.
                pai = conf_ambiente[aspirador[0]][aspirador[1]][1]
                aspirador = Aspirador.andar(aspirador, pai, ambiente)

                # Retira o nó 'visitado' de filho dó pai
                conf_ambiente[pai[0]][pai[1]][2].pop(0)
            else:
                print('Aspirador voltou para a base')
                Ambiente.imprimir_matriz(ambiente)
                Ambiente.verificar_limpeza(ambiente)

        visitados = verifcar_visitados(conf_ambiente, ambiente)
        input('Verifique e pressione <enter> para continuar')


def criar_filhos(aspirador, conf_ambiente, ambiente):
    # Frente
    # Verifica se está na parede
    if aspirador[0] + 1 != len(conf_ambiente):
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        if conf_ambiente[aspirador[0] + 1][aspirador[1]][3] == 0:
            # Verifica se tem móvel
            if ambiente[aspirador[0] + 1][aspirador[1]] != -1:
                # Marca sendo pai do próximo nó
                conf_ambiente[aspirador[0] + 1][aspirador[1]][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
                # Marca o próximo nó 'marcado'
                conf_ambiente[aspirador[0] + 1][aspirador[1]][3] = 'marcado'
                # Adiociona o proximo no na lista de filhos
                conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0] + 1][aspirador[1]][0])

    # Direita
    # Verifica se está na parede
    if aspirador[1] + 1 != len(conf_ambiente[0]):
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        if conf_ambiente[aspirador[0]][aspirador[1] + 1][3] == 0:
            # Verifica se tem móvel
            if ambiente[aspirador[0]][aspirador[1] + 1] != -1:
                # Marca sendo pai do próximo nó
                conf_ambiente[aspirador[0]][aspirador[1] + 1][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
                # Marca o próximo nó 'marcado'
                conf_ambiente[aspirador[0]][aspirador[1] + 1][3] = 'marcado'
                # Adiociona o proximo no na lista de filhos
                conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0]][aspirador[1] + 1][0])

    # tras
    # Verifica se está na parede
    if aspirador[0] != 0:
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        if conf_ambiente[aspirador[0] - 1][aspirador[1]][3] == 0:
            # Verifica se tem móvel
            if ambiente[aspirador[0] - 1][aspirador[1]] != -1:
                # Marca sendo pai do próximo nó
                conf_ambiente[aspirador[0] - 1][aspirador[1]][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
                # Marca o próximo nó 'marcado'
                conf_ambiente[aspirador[0] - 1][aspirador[1]][3] = 'marcado'
                # Adiociona o proximo no na lista de filhos
                conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0] - 1][aspirador[1]][0])

    # Esquerda
    # Verifica se está na parede
    if aspirador[1] != 0:
        # Verifica se já é filho de alguém 0 = !marcado && !visitado
        if conf_ambiente[aspirador[0]][aspirador[1] - 1][3] == 0:
            # Verifica se tem móvel
            if ambiente[aspirador[0]][aspirador[1] - 1] != -1:
                # Marca sendo pai do próximo nó
                conf_ambiente[aspirador[0]][aspirador[1] - 1][1] = conf_ambiente[aspirador[0]][aspirador[1]][0]
                # Marca o próximo nó 'marcado'
                conf_ambiente[aspirador[0]][aspirador[1 - 1]][3] = 'marcado'
                # Adiociona o proximo no na lista de filhos
                conf_ambiente[aspirador[0]][aspirador[1]][2].append(conf_ambiente[aspirador[0]][aspirador[1] - 1][0])

    # Se não conseguir criar filho nenhum, marque como visitado
    if len(conf_ambiente[aspirador[0]][aspirador[1]][2]) == 0:
        conf_ambiente[aspirador[0]][aspirador[1]][3] = 'visitado'
        return 0
    else:
        return 1


def verifcar_visitados(conf_ambiente, ambiente):
    linha = len(conf_ambiente)
    coluna = len(conf_ambiente[0])

    for i in range(linha):
        for j in range(coluna):
            if ambiente[i][j] != -1:
                if conf_ambiente[i][j][3] != 'visitado':
                    print('Ambiente NÃO está completamente verificado')
                    return 0

    print('Ambiente Totalmente verificado')
    return 1