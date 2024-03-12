import os

restaurantes = [
    {
        'nome':'Pizza Hut', 
        'icone': '🍕',
        'status': False
    },
    {
        'nome':'Taco Bell',
        'icone': '🔔',
        'status': True
    },
    {
        'nome':'Starbucks',
        'icone': '☕',
        'status': True
    },
    {
        'nome':'Aoi',
        'icone': '🍜',
        'status': False
    },

]


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
    icone = input('Digite o icone do restaurante: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'icone': icone, 'status': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante "{icone} {nome_do_restaurante}" foi cadastrado com sucesso!')
    voltar_ao_menu()
    
def ativar_restaurante():
    exibir_titulo('Alternar o status')
    nome_do_restaurante = input('Digite o nome do restaurante a ter o status alterado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status'] 
            print('Status alterado com sucesso')
            status = '🔴 Inativo'
            if restaurante['status']: 
                status = '🟢 Ativo'
            print(f'{restaurante['icone']} {restaurante['nome'].ljust(12)}  Status: {status}')
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_titulo('Nossos restaurantes')
    for restaurante in restaurantes:
        status = '🔴 Inativo'
        if restaurante['status']: 
            status = '🟢 Ativo'
        print(f'{restaurante['icone']} {restaurante['nome'].ljust(12)}  Status: {status}')
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
            ativar_restaurante()
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