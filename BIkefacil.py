from funções import cadastrar, login
while True:
    print("################################\n################################"
          "\n**Bem vindo ao App BIKEFACIL!***\n"
          "Digite 1 para login\n"
          "Digite 2 para cadastrar usuário\n"
          "Digite 3 para Login \n"
          "Digite 4 para sair\n"
          "################################\n################################")

    escolha = int(input())
    if escolha == 1:
        continue
    elif escolha == 2:
        user = input('Digite o usuario\n')
        senha = input('Digite a senha\n')
        cadastrar(user,senha)
    elif escolha == 3:
        user = input('Digite o usuário\n')
        senha = input('Digite a senha\n')
        login(user,senha)

        break
    elif escolha == 4:
        print('Saindo')
        break
    else:
        print('Opção inválida')
        continue