# Módulo main

import Ambiente
import Aspirador
import BuscaProfundidade
import BuscaAestrela

def main():
    opcao = 0

    ambiente = Ambiente.criar_ambiente()
    config_ambiente = Ambiente.criar_confambiente(ambiente)

    if ambiente == -1:
        print('Programa encerrado')
        return
    Ambiente.editar_ambiente(ambiente)
    Ambiente.verificar_limpeza(ambiente)
    aspirador = Aspirador.criar_aspirador(ambiente)

    while opcao != 3:
        print('Qual busca será realizada: ')
        print('1 - Busca em Profundidade')
        print('2 - Busca A*')
        print('3 - Sair')
        opcao = int(input('Digite opção desejada: '))

        if opcao == 1:
            BuscaProfundidade.busca_profundidade(aspirador, ambiente, config_ambiente)
            # Ambiente.editar_ambiente(ambiente)

        elif opcao == 2:
            BuscaProfundidade.busca_profundidade(aspirador, ambiente, config_ambiente)
            if ambiente == -1:
                print('Programa encerrado')
                return

            # Restaurando configuração do Ambiente do aspirador
            config_ambiente = Ambiente.criar_confambiente(ambiente)

            print('Destinos encontrados')
            print(aspirador[2])

            print('Coloque novas sujeiras no ambiente.')
            Ambiente.editar_ambiente(ambiente)

            BuscaAestrela.busca_aestrela(aspirador, ambiente, config_ambiente)

        elif opcao == 3:
            return

        else:
            print('Opção invalida')


main()

