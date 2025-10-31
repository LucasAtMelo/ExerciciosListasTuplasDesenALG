"""
Escreva um programa que apaga todos os
elementos negativos de uma lista.
"""

lista_real = [-4, -2, 3, 4, -1, 0]
lista_natural = []

for i, item in enumerate(lista_real):
    if item >= 0:
        lista_natural.append(item)

print(lista_natural)