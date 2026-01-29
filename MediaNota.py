nota1 = float((input)('Dígite sua primeira nota: '))
nota2 = float((input)('Dígite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 9:
    print(f'Sua média é {media} e sua classificação é A.')
elif media >= 8:
    print(f'Sua média é {media} e sua classificação é B.')
elif media >= 7:
    print(f'Sua média é {media} e sua classificação é C.')    
elif media >= 6:
    print(f'Sua média é {media} e sua classificação é D.')
elif media >= 5:
    print(f'Sua média é {media} e sua classificação é E.')
else:
    print(f'Sua média é {media} e sua classificação é F')