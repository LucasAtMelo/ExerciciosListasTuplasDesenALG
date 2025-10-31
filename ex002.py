"""
Escreva um programa que aplica a função
módulo a todos os elementos e uma lista.
"""

lista_numeros = [3, 2, -10, 5, 2]

for c in range(len(lista_numeros)):
    lista_numeros[c] = abs(lista_numeros[c])
    
print(f'Resultado: {lista_numeros}')
