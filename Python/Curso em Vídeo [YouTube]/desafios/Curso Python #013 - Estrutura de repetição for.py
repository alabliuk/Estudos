# https://www.youtube.com/watch?v=cL4YDtFnCt4&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye

from time import sleep
from datetime import date

# Desafio 46
print('\n\nDesafio 46')
print('Contagem regressiva de 10 a 0')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Fogos!')


# Desafio 47
print('\n\nDesafio 47')
print('Contagem de numeros pares de 1 a 50')
for c in range(0, 51, 2):
    print(c, end = ' - ')
print('Fim')


# Desafio 48
print('\n\nDesafio 48')
print('Soma dos numeros impares de 1 a 500 que são multipos de 3')
s = 0
for c in range(1, 501, 2):
    if(c % 3 == 0):
        s += c
        print(c)

print(f'TOTAL: {s}')


# Desafio 49
print('\n\nDesafio 49')
tab = int(input('Tabuada desejada: '))
for c in range(0, 11):
    print(f'{tab} x {c:2} = {tab*c:3}')


# Desafio 50
print('\n\nDesafio 50')
s = 0
for c in range(1, 7):
    x = int(input(f'{c} - Insira um numero inteiro: '))
    if(x % 2 == 0):
        s += x
print(f'Soma dos numeros pares: {s}')


# Desafio 51
print('\n\nDesafio 51')
print('Progressão Aritmetica')
p1 = int(input('Insira o valor do primeiro elemento: '))
razao = int(input('Insira a razao da progressão: '))
decimo = p1 + (10 - 1) * razao
for c in range(p1, decimo + razao, razao):
    print(c, end = ' -> ')
print('Fim')


# Desafio 52
print('\n\nDesafio 52')
print('Validador de Numero Primo')
valida_primo = int(input('Numero a ser validado: '))
aux = 0
for c in range(1, valida_primo):
    if(valida_primo % c == 0):
        aux += 1

if(aux == 1):
    print(f'O numero {valida_primo} É um numero primo!')
else:
    print(f'O numero {valida_primo} NÃO é um numero primo!')


# Desafio 53 [INCOMPLETO]
print('\n\nDesafio 53')
print('Validador de frase palindromo')
frase = input('Digite sua frase: ')

aux = frase.strip().upper().replace(' ', '')
print(aux)


# Desafio 54
print('\n\nDesafio 54')
qtd_maior = 0
qtd_menor = 0
for c in range (1, 8):
    y = int(input(f'{c} - Digite o ano de nascimento: '))
    if(date.today().year - 21 >= y):
        print('Já atingiu a maioridade de 21 anos!')
        qtd_maior += 1
    else:
        print('Ainda não atingiu a maioridade de 21 anos!')
        qtd_menor += 1

print(f'\nQuantidade de Pessoas acima de 21 anos: {qtd_maior}')
print(f'Quantidade de Pessoas abaixo de 21 anos: {qtd_menor}')


# Desafio 55
print('\n\nDesafio 55')
peso_maior = 0
peso_menor = 1000
for c in range(1, 6):
    peso = float(input(f'{c} - Digite seu peso: '))
    if(peso > peso_maior):
        peso_maior = peso
    if(peso < peso_menor):
        peso_menor = peso

print(f'Maior peso: {peso_maior:.2f}\nMenor peso: {peso_menor:.2f}')


# Desafio 56
print('\n\nDesafio 56')
media_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menor_vinte_anos = 0
for c in range(0, 4):
    nome = input('Digite seu nome:')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: ')
    print('\n')

    # soma das idades
    media_idade += idade

    # salva o homem mais velho
    if(sexo.upper().strip() == 'M' and idade > idade_homem_mais_velho):
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    # quantidade de mulheres abaixo de vinte anos
    if(sexo.upper().strip() == 'F' and idade < 20):
        mulheres_menor_vinte_anos += 1

print(f'Media de idade: {media_idade/4}')
print(f'Nome do homem mais velho: {nome_homem_mais_velho}')
print(f'Mulheres abaixo de 20 anos: {mulheres_menor_vinte_anos}')
