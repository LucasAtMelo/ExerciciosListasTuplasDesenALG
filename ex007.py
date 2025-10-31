"""
Escreva um programa que solicita que o
usuário digite a altura e o peso de 5 pessoas.
Verifique se pelo menos duas das pessoas
tem a mesma altura e mesmo peso.
"""

pessoas = []
pesos = []
duplicado = False

for c in range(5): 
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    if peso not in pesos:
        pesos.append(peso)
    else:
        duplicado = True

    pessoa = [nome, peso]
    pessoas.append(pessoa)

print(f'Lista de pessoas: {pessoas}')

if duplicado: 
    print('Há mais de uma pessoa com o mesmo peso')
else:
    print('Não há pesos iguais')
