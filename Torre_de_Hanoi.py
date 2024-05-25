objetos = [" ", "__", "____", "______"]
total_movimentos = 0

def novojogo():
    global fisica
    global total_movimentos
    total_movimentos = 0
    fisica = [[3, 2, 1], [], []]
    printtorres()

def printtorres():
    linha = ""
    print("~" * 7 * 3)
    for discos in range(2, -1, -1):
        for coluna in range(3):
            try:
                linha += objetos[fisica[coluna][discos]].center(7)
            except IndexError:
                linha += objetos[0].center(7)
        print(linha)
        linha = ""

def gameEngine():
    global total_movimentos
    while True:
        jogador = input("Qual das peças você quer mover e pra onde você a gostaria de mover? [1 3]")
        move = [int(i) - 1 for i in jogador.split()]
        if len(fisica[move[0]]):
            if len(fisica[move[1]]):
                if fisica[move[0]][-1] < fisica[move[1]][-1]:
                    fisica[move[1]].append(fisica[move[0]][-1])
                    fisica[move[0]].pop()
                    total_movimentos += 1
                    printtorres()
                else:
                    print("Não pode ser movido")
            else:
                fisica[move[1]].append(fisica[move[0]][-1])
                fisica[move[0]].pop()
                total_movimentos += 1
                printtorres()
        else:
            print('Nada pra mover aqui!')

        if len(fisica[2]) == 3:
            print("Você realizou {} movimentos".format(total_movimentos))
            break

play = "Sim"
while play.lower() == "sim":
    novojogo()
    gameEngine()
    play = input("Você gostaria de tentar jogar? [Sim/Não]")
