"""
Faça um programa que solicita uma
quantidade indefinida de números positivos
(deve parar quando um número negativo for
digitado).
Armazene-os em duas listas:
uma para os números pares;
outra para os números ímpares.
A seguir, mostre a porcentagem de pares e
ímpares digitados.
"""

pares = []
impares = []

while True:
    atual = int(input('Digite um número! Negativo para parar: '))
    if atual < 0: 
        break
    if atual % 2 == 0:
        pares.append(atual)
    else:
        impares.append(atual)
    
print(f'Pares: {pares}')
print(f'Impares: {impares}')

