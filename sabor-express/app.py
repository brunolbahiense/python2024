import os

restaurantes = ["🍕 Pizza Hut", "🔔 Taco Bell", "☕ Starbucks"]
def nome_programa():
    print('𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨 🍜 \n')

def finalizar():
    os.system('cls')
    print('Sair')

def voltar_ao_menu():
    input(' \nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_titulo(texto):
    os.system('cls')
    print(f'{texto} \n')

def opcao_invalida(opcao_escolhida):
    print(f'a opção "{opcao_escolhida}" é invalida!')
    voltar_ao_menu()


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante ')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    exibir_titulo('Cadastro de restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!')
    voltar_ao_menu()
    

def listar_restaurantes():
    exibir_titulo('Nossos restaurantes')
    for restaurante in restaurantes:
        print(restaurante)
    voltar_ao_menu()

def escolher_opcao():
    opcao_escolhida = input('Escolha uma opção: ')
    try:
        opcao_escolhida = int(opcao_escolhida)
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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