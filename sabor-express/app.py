import os
def nome_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨 🍜 \n')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante ')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# def é a forma de declarar funções
def finalizar():
    os.system('clear')
    print('Sair')

def opcao_invalida():
    print('opcao invalida!\n')
    input('digite uma tecla para retornar ao menu principal')
    main()

# def escolher_opcoes_if():
#     try:
#         opcao_escolhida = int(input('Escolha uma opção: '))

#         if opcao_escolhida == 1:
#             print('Cadastrar restaurante')
#         elif opcao_escolhida == 2:
#             print('Listar restaurante')
#         elif opcao_escolhida == 3:
#             print('Ativar restaurante')
#         elif opcao_escolhida == 4:
#             finalizar()
#         else:
#             opcao_invalida()
#     except:
#         opcao_invalida()
        
def escolher_opcoes_match():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                print('Cadastrar restaurante')
            case 2:
                print('Listar restaurante')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('clear')
    nome_programa()
    exibir_opcoes()
    escolher_opcoes_match()

if __name__ == '__main__':
    main()