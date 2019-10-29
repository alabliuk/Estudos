# https://www.youtube.com/watch?v=LH6OIn2lBaI&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye

from random import randint

# Desafio 57
print('\n\nDesafio 57')
sexo = 'x'
while(sexo not in 'MmFf'):
    sexo = input('Digite seu sexo [M/F]: ').strip()
    if(sexo in 'MmFf'):
        print(f'Vc digitou o sexo {sexo}')
    else:
        print(f'Sexo invalido! Tente novamente')


# Desafio 58
print('\n\nDesafio 58')
numPc = randint(0, 10)
numUser = 99
tentativas = 0
while(numUser != numPc):
    numUser = int(
        input('Tente adivinhar o numero escolhido pelo computador (Range: 0 a 10): '))
    tentativas += 1
    if(numPc != numUser):
        print('Você não acertou! Tente novamente!\n')

print('Você Ganhou!')
print(f'Tentativas: {tentativas} \nNumero Gerado: {numPc}')


# Desafio 59
print('\n\nDesafio 59')
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
menu = 1
while(0 < menu < 5):
    menu = int(input(
        '\n[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5] SAIR DO PROGRAMA\n\n--> '))
    if(menu == 1):
        print(f'\n{n1} + {n2} = {n1+n2}')
    elif(menu == 2):
        print(f'\n{n1} * {n2} = {n1*n2}')
    elif(menu == 3):
        if(n1 > n2):
            print(f'O maior numero é {n1}')
        elif(n1 == n2):
            print(f'Os dois numeros são iguais')
        else:
            print(f'O maior numero é {n2}')
    elif(menu == 4):
        n1 = int(input('Insira o primeiro numero: '))
        n2 = int(input('Insira o segundo numero: '))
    elif(menu == 5):
        print('Encerrando...')
    else:
        print('Opção invalida!')


# Desafio 60
print('\n\nDesafio 60')
fatorial = int(input('Insira um numero para o calculo fatorial: '))
count = fatorial
calc = 1
while(count >= 1):
    calc = calc * count
    count -= 1
print(f'{fatorial}! = {calc}')


# Desafio 61
print('\n\nDesafio 61')
p1 = int(input('Insira o valor do primeiro elemento: '))
razao = int(input('Insira a razao da progressão: '))
aux = 0
c = 10
while(c > 0):
    print(f'{p1}', end=' -> ')
    p1 += razao
    c -= 1
print('Fim')


# Desafio 62
print('\n\nDesafio 62')
p1 = int(input('Insira o valor do primeiro elemento: '))
razao = int(input('Insira a razao da progressão: '))
aux = 0
c = 10
while(c > 0):
    print(f'{p1}', end=' -> ')
    p1 += razao
    c -= 1
    if(c == 0):
        c = int(input(
            '\nDigite a quantidade adicional de termos a ser exibida, caso deseje sair digite 0.\n--> '))
print('Fim')


# Desafio 63
print('\n\nDesafio 63')
fibo_max = int(input('Digite o limite da sequencia de Fibonacci: '))
c = 1
print('0 -> 1 -> ', end='')
while(fibo_max > c):
    print(c, end=' -> ')
    c += c
print('Fim')


# Desafio 64
print('\n\nDesafio 64')
x = 0
soma = 0
inputs = 0
while(x != 999):
    x = int(input('Insira um numero inteiro: '))
    if(x != 999):
        inputs += 1
        soma += x
print(f'\nTotal de inputs = {inputs}\nSoma: {soma}')


# Desafio 65
print('\n\nDesafio 65')
z = 1
soma = 0
inputs = 0
maior = 0
menor = 0
while(z != 2):
    ns = int(input('Insira um valor: '))
    z = int(input('\nContinuar?\n[1] SIM\n[2] NAO\n--> '))
    soma += ns
    if(maior == menor == 0):
        maior = ns
        menor = ns
    else:
        if(ns > maior):
            maior = ns
        if(ns < menor):
            menor = ns
    inputs += 1

print(
    f'A media dos elementos são: {soma/inputs}\nMaior elemento: {maior}\nMenor elemento: {menor}')
