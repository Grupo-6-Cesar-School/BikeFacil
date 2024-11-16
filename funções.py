import perfil
from art import ascii_art2, ascii_art3
from perfil import profile
import time

#Como esse ap não utilizará GPS
locais_recife = {
    "Marco Zero": 0,
    "Shopping Riomar": 3.6,
    "Shopping Boa Vista": 2.0,
    "Shopping Recife":  7.3,



}
def apertei_enter_sem_querer(prompt):
    """#Estava apertando enter sem querer muitas vezes na hora de testar o código
    então criei esse código que impede isso + umas frescurinhas"""
    while True:
        user_input = input(prompt)
        if user_input.strip():
            try:
                return int(user_input)
            except ValueError:
                print("Por favor, insira um número válido.")
        else:
            print("Input não pode estar vazio. Por favor, tente novamente.")

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f'Retornando ao menu anterior em {i}...')
        time.sleep(1)

def escrever_arquivo(nome_arquivo):
    entrada = input('Digite...\n' )
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(entrada + "\n")

def cadastrar(usuario, senha):
    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
            for linha in usuarios:
                dados = linha.strip().split(',')
                if len(dados) == 2:
                    existing_username, _ = dados
                    if existing_username == usuario:
                        print('Usuário já existe. Por favor, escolha um nome de usuário diferente.')
                        countdown(3)
                        return

        # If the user does not exist, add them to the file
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")
        print("Cadastro realizado com Sucesso!!!")

    except FileNotFoundError:
        # If the file does not exist, create it and add the user
        with open('usuarios.txt', 'w') as arquivo:
            arquivo.write(f"{usuario},{senha}\n")
        print("Cadastro realizado com Sucesso!!!")

    print('Digite 1 para retornar à tela de login')
    while True:
        escolha = int(input())
        if escolha == 1:
            break
        else:
            print('Comando inválido')
            continue


def login(usuario, senha):
    try:
        with open('usuarios.txt', 'r') as arquivo:
            usuarios = arquivo.readlines()
            for linha in usuarios:
                dados = linha.strip().split(',')
                if len(dados) == 2:
                    catch_usuario, catch_senha = dados
                    if catch_usuario == usuario and catch_senha == senha:
                        perfil.usuario_logado = usuario  # Update the global variable
                        print(f'Bem vindo {usuario}')
                        while True:
                            print('--- MENU ---\n'
                                   '1. Visualizar Perfil\n'
                                   '2. Planejar Rota\n'
                                   '3. Fromar Grupo\n'
                                   '4. Sair.\n')
                            escolha = apertei_enter_sem_querer("")
                            if escolha == 1:
                                profile()
                            elif escolha == 2:
                                rota()
                            elif escolha == 3:
                                print('Under construction')
                            elif escolha == 4:
                                print(ascii_art2)
                                exit()
                            else:
                                print('Comando inválido')
                                continue
            print('Usuário ou senha incorretos. Tente novamente.')
            countdown(3)
    except FileNotFoundError:
        print("O arquivo de usuários não foi encontrado.")




def rota():
    print(ascii_art3)
    while True:
        print('--- * ---\n'
              '1. Usar localização atual\n'
              '2. Digitar localização manualmente\n'
              '3. Retornar ao menu anterior \n')
        escolha = apertei_enter_sem_querer('...\n')
        if escolha == 1:
            print('Utilizaremos a localização atual do GPS')
        elif escolha == 2:
            local = str(input('Digite o ponto de partida.'))
        elif escolha == 3:
            countdown(3)
            break
        else:
            print('Comando inválido')