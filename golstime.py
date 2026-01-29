time1 = (input('Qual o nome do primeiro time: '))
time2 = (input('Qual o nome do segundo time: ' ))

golstime1 = int(input(f'Quantos gols o {time1} fez: '))
golstime2 = int(input(f'Quantos gols o {time2} fez: '))

diferencagols = golstime1 - golstime2

if diferencagols == 0:
    print(f'A partida resultou em um *empate* entre {time1} e {time2}!')
elif diferencagols <= 3:
    print(f'A partida resultou em um *jogo normal* entre {time1} e {time2}!')
else:
    print(f'O jogo resultou em uma *goleada* entre {time1} e {time2}!')