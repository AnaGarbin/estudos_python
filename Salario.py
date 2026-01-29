nome = (input('Qual o seu nome: '))
print(f'Bem vindo(a), {nome}!')
salario = float(input('Qual o seu sálario: '))
dependentes = int(input('Quantas pessoas dependem desse sálario: '))
if dependentes == 0:
    novosalario = salario + (salario * 5/100)
    print(f'Seu novo sálario é R${novosalario}')
elif dependentes < 3:
    novosalario = salario + (salario * 10/100)
    print(f'Seu novo sálario é R${novosalario}')
else:
    novosalario = salario + (salario * 15/100)
    print(f'Seu novo sálario é R${novosalario}')
    
 