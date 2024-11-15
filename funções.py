import perfil

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
                        print('1. Retornar à tela de login\n'
                              '2. Visualizar Perfil\n'
                              '3. Planejar rota\n'
                              '4. Formar Grupo')
                        while True:
                            escolha = int(input())
                            if escolha == 1:
                                return
                            else:
                                print('Comando inválido')
                                continue
            print('Usuário ou senha incorretos. Tente novamente.')
    except FileNotFoundError:
        print("O arquivo de usuários não foi encontrado.")




