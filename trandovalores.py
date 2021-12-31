salario = list()
cont = 0
maior_salario = 0
for funcionario in range(0, 5):
    salario.append(int(input('Digite seu salário: ')))
    cont += 1

for valor in salario:
    if valor > maior_salario:
        maior_salario = valor
print(f'Ao todo {cont} digitaram seu salário\nE o maior salário digitado foi {maior_salario}')

