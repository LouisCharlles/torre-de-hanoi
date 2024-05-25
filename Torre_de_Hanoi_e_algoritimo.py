objetos = [" ", "_", "__", "___", "____", "_____", "______", "_______", "________", "_________", "__________"]
total_movimentos = 0
fisica = []


def novojogo():
    global total_movimentos
    global fisica
    total_movimentos = -1

    n_discos = int(input("Digite o número de discos: "))

    if n_discos < 3:
        print("O número de discos deve ser pelo menos 3.")
        return

    fisica.clear()
    fisica.extend([list(range(n_discos, 0, -1)), [], []])
    printtorres()


def printtorres():
    global total_movimentos
    total_movimentos += 1
    linha = ""

    for discos in range(len(fisica[-1]), -1, -1):
        for coluna in range(3):
            try:
                linha += objetos[fisica[coluna][discos]].center(7)
            except IndexError:
                linha += objetos[0].center(7)
        print(linha)
        linha = ""

    if len(fisica[-1]) == len(fisica[0]):
        print('Você realizou até este momento {} movimentos.'.format(total_movimentos))


def torre_hanoi(n, origem, auxiliar, destino):
    global total_movimentos
    if n == 1:
        total_movimentos += 1
        printtorres()
        print(f'Mova o disco 1 de {origem} para {destino}')
        return
    torre_hanoi(n - 1, origem, destino, auxiliar)
    total_movimentos += 1
    printtorres()
    print(f'Mova o disco {n} de {origem} para {destino}')
    torre_hanoi(n - 1, auxiliar, origem, destino)


def resolver_jogo():
    novojogo()
    torre_hanoi(len(fisica[0]), 'A', 'B', 'C')


play = "Sim"
while play.lower() == "sim":
    resolver_jogo()
    play = input("Você gostaria de tentar jogar novamente? [Sim/Não]: ")
