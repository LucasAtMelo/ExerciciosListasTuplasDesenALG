""""
Escreva um programa que solicita que o
usuário digite 5 números inteiros e os coloca
em uma lista.
Quando terminar, imprima a lista.
"""

lista = []

for c in range(0, 5): 
    numero_atual = int(input(f'Digite o {c+1} número a ser colocado na lista:  '))
    lista.append(numero_atual)

print(f'A lista digitada foi: {lista}')
