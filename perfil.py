from art import ascii_art


usuario_logado = None
def profile():
    while True:
        km_percorridos = 0
        awards = 0
        amigos = 0 #Cara, isso é muito triste!
        print(f'{ascii_art}')
        print(f'Olá {usuario_logado}\n'
              f'KM PERCORRIDOS: {km_percorridos}\n'
              f'TROFÉUS: {awards}\n'
              f'Amigos: {amigos}\n')
        escolha = int(input('1. Retornar ao Menu anterior'))
        if escolha == 1:
            break
        else:
            print('Opção inválida')









































