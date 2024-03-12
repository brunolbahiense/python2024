import os
def nome_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨 🍜 \n')
    
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante ')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def finalizar():
    os.system('cls')
    print('Sair')

def opcao_invalida(opcao_escolhida):
    print(f'a opção "{opcao_escolhida}" é invalida!')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():
    opcao_escolhida = input('Escolha uma opção: ')
    try:
        opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            print('Cadastrar restaurante')
        elif opcao_escolhida == 2:
            print('Listar restaurante')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar()
        else:
            opcao_invalida(opcao_escolhida)
    except:
        opcao_invalida(opcao_escolhida)
       
def main():
    os.system('cls')
    nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()