"""
Faça um programa que solicita uma
quantidade indefinida de números positivos
(deve parar quando um número negativo for
digitado).
Armazene todos os números digitados em
uma lista, sem repetição.
"""

numeros = []

while True: 
    numero = int(input('Digite um número! Negativo pra parar: '))
    if numero < 0:
        break
    if numero not in numeros:
        numeros.append(numero)

print(f'Lista de números: {numeros}')
