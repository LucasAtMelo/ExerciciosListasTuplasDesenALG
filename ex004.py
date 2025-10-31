"""
Faça um programa que solicita uma
quantidade indefinida de notas de uma
prova (deve parar quando um número
negativo for digitado).
Armazena em uma lista.
Após isso, o programa deve mostrar a média
das notas.
"""

notas = []
media = 0
cont = 0

while True:
    nota = float(input('Digite a nota atual! Negativo para sair: '))
    if nota < 0:
        break
    notas.append(nota)
    cont += 1

media = sum(notas) / cont
print(f'A média de notas é {media}')