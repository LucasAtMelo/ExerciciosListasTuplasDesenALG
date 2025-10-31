"""
Faça um programa que solicita que o
usuário digite o nome e a idade de diversas
pessoas (o programa deve parar quando
um nome vazio for informado).
Retorne o nome da pessoa mais velha.
"""

pessoas = []
mais_velha = ''
idade_mais_velha = 0

while True:
    nome = input('Digite o nome da pessoa! Vazio para parar: ')
    if nome == '':
        break
    idade = int(input('Digite a idade: '))
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        mais_velha = nome

    pessoa = [nome, idade]
    pessoas.append(pessoa)

print(f'Lista de pessoas: {pessoas}')
print(f'A pessoa mais velha foi: {mais_velha} com {idade_mais_velha} anos!')
