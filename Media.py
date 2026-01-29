nota1 = float(input('Dígite sua primeira nota: '))
nota2 = float(input('Dígite sua segunda nota: '))
media = (nota1 + nota2) / 2
if (media <= 4.9):
 print(f'Sua média é: {media}')
 print('Você está REPROVADO!')
elif (media <= 6.9):
    print(f'Sua média é: {media}')
    print('Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média é: {media}')
    print('Parabéns, você está APROVADO!')