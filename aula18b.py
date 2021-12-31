# galera = [['João', 19], ['Ana', 19], ['Joaquim', 13], ['Maria', 45]]
# for pessoas in galera:
#     print(f'{pessoas[0]} tem {pessoas[1]} anos de idade!')

lista = list()
dado = list()
cont = 0

for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    cont += 1
    lista.append(dado[:])
    dado.clear()

print(f'Ao todo temos {cont} pessoas cadastradas!\nQue são:')
for pes in lista:
    print(f'{pes[0]} com {pes[1]} anos de idade')
# print(lista)
maior_idade = list()
lista_pessoas = list()
pessoa = list()
contm = 0
for p in lista:
    if p[1] > 20:
        maior_idade.append(p[:])
        p.clear()
        contm += 1

print(f'E {contm} maiores de idade!')
for m in maior_idade:
    print(f'{m[0]} com {m[1]} anos de idade')






