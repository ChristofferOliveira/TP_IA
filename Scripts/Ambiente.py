# Módulo com as funções do Ambiente

def criar_ambiente():
    # Pegando dimenções do Ambiente
    altura = int(input("Digite a Altura do Ambiente(menor que 20): "))
    largura = int(input('Digite a Largura do Ambiente(menor que 20): '))

    if altura < 20 and largura < 20:
        ambiente = []

        # Criando Matriz para Ambiente
        for y in range(altura):
            linha = []
            for x in range(largura):
                linha.append(0)
            ambiente.append(linha)

        print('ambiente')
        imprimir_matriz(ambiente)

        return ambiente

    else:
        print('Ambiente muito grande')
        return -1


def criar_confambiente(ambiente):
    altura = len(ambiente)
    largura = len(ambiente[0])

    config_ambiente = []

    # Criando matriz que contém informações sobre o Ambiente
    for y in range(altura):
        linha = []
        for x in range(largura):
            coluna = []
            linha.append(coluna)
            for z in range(7):
                # primeira posição representa a posição real no ambiente
                if z == 0:
                    coluna.append((y, x))
                # Segunda posição contém Lista de nós filhos
                elif z == 2 or z == 4:
                    coluna.append([])
                else:
                    coluna.append(0)
        config_ambiente.append(linha)

    # print('Ambiente Aspirador')
    # imprimir_matriz(config_ambiente)

    return config_ambiente


def editar_ambiente(ambiente):
    opcao = 0

    while opcao != 5:
        largura = 0
        altura = 0
        print('Qual alteração será feita?')
        print('1 - Colocar moveis')
        print('2 - Retirar moveis')
        print('3 - Colocar sujeira')
        print('4 - Remover sujeira')
        print('5 - Sair da edição')
        opcao = int(input('Digite opção desejada: '))

        # Colocando Móvel
        if opcao == 1:
            while (altura or largura) != -1:
                print('Qual local do ambiente estará o móvel?(digite -1 para sair): ')
                imprimir_matriz(ambiente)
                altura = int(input('posição em Y(linha): '))
                if altura != -1:
                    largura = int(input('posição em X(Coluna): '))

                    if largura != -1:

                        if ambiente[altura][largura] != -1:
                            ambiente[altura][largura] = -1
                        else:
                            print('local já contém móvel')

        # Retirando Móvel
        elif opcao == 2:
            while (altura or largura) != -1:
                print('Qual local do ambiente não terá móvel?(digite -1 para sair): ')
                imprimir_matriz(ambiente)
                altura = int(input('posição em Y(linha): '))

                if altura != -1:
                    largura = int(input('posição em X(Coluna): '))

                    if largura != -1:

                        if ambiente[altura][largura] == -1:
                            ambiente[altura][largura] = 0
                        else:
                            print('local não contém móvel')

        # Colocando sujeira
        elif opcao == 3:
            while (altura or largura) != -1:
                print('Qual local do ambiente estará a sujeira?(digite -1 para sair): ')
                imprimir_matriz(ambiente)
                altura = int(input('posição em Y(linha): '))

                if altura != -1:
                    largura = int(input('posição em X(Coluna): '))

                    if largura != -1:

                        if ambiente[altura][largura] != 1:
                            ambiente[altura][largura] = 1
                        else:
                            print('local já contém sujeira')

        # Retirando sujeira
        elif opcao == 4:
            while (altura or largura) != -1:
                print('Qual local do ambiente estará limpo?(digite -1 para sair): ')
                imprimir_matriz(ambiente)
                altura = int(input('posição em Y(linha): '))

                if altura != -1:
                    largura = int(input('posição em X(Coluna): '))

                    if largura != -1:

                        if ambiente[altura][largura] == 1:
                            ambiente[altura][largura] = 0
                        else:
                            print('local não contém sujeira')

        elif opcao == 5:
            print('Ambiente Final')
            imprimir_matriz(ambiente)
            return ambiente

        else:
            print('Opção inválida, tente novamente!')


def verificar_limpeza(ambiente):
    linha = len(ambiente)
    coluna = len(ambiente[0])

    for i in range(linha):
        for j in range(coluna):
            if ambiente[i][j] == 1:
                print('Ambiente NÃO está completamente limpo')
                return 0

    print('Ambiente Totalmente Limpo')
    return 1

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
    return
