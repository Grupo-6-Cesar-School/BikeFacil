import perfil
from funções import cadastrar, login
from art import ascii_art2

def print_usuario_logado():
    if perfil.usuario_logado:
        print(f'Usuário logado: {perfil.usuario_logado}')
    else:
        print("Nenhum usuário está logado atualmente")

while True:
    print("--- BikeFacil --- \n"
          "1. para Login\n"
          "2. para Cadastrar usuário\n"
          "3. para sair\n"
          "Escolha uma opção\n")

    escolha = int(input())
    if escolha == 1:
        user = input('Digite o usuário\n')
        senha = input('Digite a senha\n')
        login(user, senha)
        print_usuario_logado()
    elif escolha == 2:
        user = input('Digite o usuario\n')
        senha = input('Digite a senha\n')
        cadastrar(user, senha)
        continue

    elif escolha == 3:
        print(ascii_art2)
        break
    else:
        print('Opção inválida')
        continue
