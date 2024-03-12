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
    os.system('cls')
    print('Sair')

def cadastrar_novo_restaurante():
    pass

def opcao_invalida(opcao_escolhida):
    print(f'a opção {opcao_escolhida} invalida!')
    input('Digite uma tecla para voltar ao menu principal')
    main()
               
def escolher_opcoes_match():
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
            print(f'opcao {opcao_escolhida} invalida!')


def main():
    os.system('cls')
    nome_programa()
    exibir_opcoes()
    escolher_opcoes_match()

if __name__ == '__main__':
    main()