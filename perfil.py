from art import ascii_art
lista_amigos = []#CARA, ISSO É MUITO TRISTE!
usuario_logado = None
total_km = 0
total_award = 0

'''add_km e add_award são funções que irão lidar com variáveis globais que armazenarão o desempenho do usuário
como kms percorridos e troféus, a cada 10km percorridos o usuário recebe um award em seu perfil, 
inflará o seu ego tanto quanto um like naquele seu story do insta, mas em adicional você também irá emagrecer =)'''

def mostra_amigos():
    if not lista_amigos:
        return 'Nenhum amigo adicionado :('

    enumerar_amigos = [f"{index + 1}. {amigo}" for index, amigo in enumerate(lista_amigos)]
    return '\n'.join(enumerar_amigos)


def add_km(km):
    global total_km
    total_km += km

def add_award(award):
    global total_award
    total_award += award / 14

def profile():
    while True:
        print(f'{ascii_art}')
        print(f'Olá {usuario_logado}\n'
              f'KMs PERCORRIDOS: {total_km}\n'
              f'TROFÉUS: {total_award:.2f}\n'
              f'Amigos:\n{mostra_amigos()}\n')
        escolha = int(input('1. Retornar ao Menu anterior'))
        if escolha == 1:
            break
        else:
            print('Opção inválida')









































