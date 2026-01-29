nome = (input('Dígite o seu nome: '))
print(f'Seja bem vindo(a), {nome}!')
doacao = float(input('Qual valor você deseja doar: '))
if doacao < 10:
    print(f'Você fez uma doação no valor de R${doacao}, obrigado pela doação.')
elif doacao < 40:
    print(f'Você fez uma doação no valor de R${doacao}, sua doação é muito importante. Você receberá um brinde por isso.')
else:
    print(f'Você fez uma doação no valor de R${doacao}, nós agradecemos imensamente sua doação. Você receberá um prêmio por isso!')        
