# https://www.youtube.com/watch?v=oOUyhGNib2Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6

import math
import emoji
import random
print(emoji.emojize('Olá! :smiley:', use_aliases=True))

print('*=' * 50)

# Desafio 16
print('\n\nDesafio 16')
num = float(input('Digite um numero real: '))
print(f'Numero digitado: {num} \nParte inteira: {math.trunc(num)}')


# Desafio 17
print('\n\nDesafio 17') 
cat_oposto = float(input('Insira o valor do cateto oposto: '))
cat_adjacente = float(input('Insira o valor do cateto adjacente: '))
print(
    f'\nCateto oposto: {cat_oposto}\nCateto Adjacente: {cat_adjacente}\nHipotenusa: {math.hypot(cat_oposto, cat_adjacente)}')


# Desafio 18
print('\n\nDesafio 18')
angulo = float(input('Angulo: '))
print(f'Seno: {math.sin(math.radians(angulo)):.2f}\nCosseno: {math.cos(math.radians(angulo)):.2f}\nTangente: {math.tan(math.radians(angulo)):.2f}')


# Desafio 19
print('\n\nDesafio 19')
aluno1 = input('Nome aluno 1: ')
aluno2 = input('Nome aluno 2: ')
aluno3 = input('Nome aluno 3: ')
aluno4 = input('Nome aluno 4: ')
print(f'Aluno escolhido: {random.choice([aluno1, aluno2, aluno3, aluno4])}')


# Desafio 20
print('\n\nDesafio 20')
aluno1 = input('Nome aluno 1: ')
aluno2 = input('Nome aluno 2: ')
aluno3 = input('Nome aluno 3: ')
aluno4 = input('Nome aluno 4: ')
print(
    f'Sequencia escolhida: {random.sample([aluno1, aluno2, aluno3, aluno4], k=4)}')


# Desafio 21
print('\n\nDesafio 21')
# --> Reproduzir mp3
