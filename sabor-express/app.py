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

def escolher_opcoes():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida == 4:
        finalizar()
    else:
        print(f'opcao {opcao_escolhida} invalida!')

def main():
    nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()