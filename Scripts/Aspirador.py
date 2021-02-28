# Módulo que contém as funções do aspirador de pó


def criar_aspirador(ambiente):
    posicionado = 0
    while posicionado == 0:
        print('Em qual posição o aspirador de pó começará?(Não pode coloca-lo em um móvel)')
        y = int(input(print('Posição em Y(linha): ')))
        x = int(input(print('Posição em X(Coluna): ')))

        if ambiente[y][x] == -1:
            print('Aspirador não pode iniciar em um móvel. Tente novamente')
        else:
            posicionado = 1

    # Aspirador primeira posição Y, Segunda X, terceira representa uma lista de destinos para busca A estrela.
    aspirador = [0, 0, []]
    ambiente[aspirador[0]][aspirador[1]] = 'A'
    return aspirador


def aspirar(altura, largura, ambiente):

    if ambiente[largura][altura] == 1:
        ambiente[largura][altura] = 0
        print('Sujeira removida')
    else:
        print('Posição não contém sujeira')


# Realiza o movimento do aspirador
def andar(aspirador, direcao,ambiente):

        # Verificando se há móvel na direção
        if ambiente[direcao[0]][direcao[1]] != - 1:
            ambiente[aspirador[0]][aspirador[1]] = 0
            aspirador[0] = direcao[0]
            aspirador[1] = direcao[1]
        else:
            print('Móvel impedindo movimento, realizando outro movimento')

        # Se houver sujeira na posição que se moveu aspira
        if ambiente[aspirador[0]][aspirador[1]] == 1:
            print('Encontrada sujeira, andando e aspirando')
            aspirar(aspirador[0], aspirador[1], ambiente)

            # Armazenando o destino para busca A estrela
            destino = (aspirador[0], aspirador[1])
            aspirador[2].append(destino)

        # Aspirador movido
        ambiente[aspirador[0]][aspirador[1]] = 'A'
        print('Aspirador, movido')
        return aspirador





