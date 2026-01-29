num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print('\nEscolha a operação:')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = input('\nDigite o número da operação desejada: ')

if opcao == '1': 
    resultado = num1 + num2
    print(f'O resultado da soma é: {resultado}')
elif opcao == '2':
    resultado = num1 - num2
    print(f'O resultado da subtraçaõ é: {resultado}')
elif opcao == '3':
    resultado = num1 * num2
    print(f'O resultado da multiplicação é: {resultado}')
elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f'O resultado da muiltiplicação é: {resultado}')
    else:
        print('ERRO: divisão por zero não é permitida')
else:
        print('Opção inválida. Escolha entre 1 e 4.')
