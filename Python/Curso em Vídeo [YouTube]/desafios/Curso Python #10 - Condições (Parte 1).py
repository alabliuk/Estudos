# https://www.youtube.com/watch?v=K10u3XIf1-Q&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6

from random import randint

# Desafio 28
print('\n\nDesafio 28')
numUser = int(
    input('Tente adivinhar o numero escolhido pelo computador (Range: 0 a 5): '))
numPc = randint(0, 5)
print(f'Chute: {numUser} \nNumero Gerado: {numPc}')
if(numPc == numUser):
    print('Você Ganhou!')
else:
    print('Você Perdeu!')


# Desafio 29
print('\n\nDesafio 29')
print('Limite de velocidade: 80km/h')
km = int(input('Velocidade do automovel: '))
if(km > 80):
    print(f'Multa: {(km - 80)*7}')
else:
    print('Veiculo não multado')


# Desafio 30
print('\n\nDesafio 30')
n = int(input('NÚMERO --> '))
if(n % 2):
    print('IMPAR')
else:
    print('PAR')


# Desafio 31
print('\n\nDesafio 31')
km = int(input('Distancia em KM da viagem: '))
if(km > 200):
    print(f'Valor por KM: R$0,45 \nValor Total: {km*0.45:.2f}')
else:
    print(f'Valor por KM: R$0,50 \nValor Total: {km*0.50:.2f}')


# Desafio 32
print('\n\nDesafio 32')
ano = int(input('Ano: '))
if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('Ano Bissexto')
else:
    print('Ano NÃO Bissexto')


# Desafio 33
print('\n\nDesafio 33')
print('Digite 3 numeros: ')
n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))

if(n1 > n2):
    if(n1 > n3):
        print(f'Maior numero: {n1}')
        if(n2 > n3):
            print(f'Menor numero: {n3}')
        else:
            print(f'Menor numero: {n2}')
    else:
        print(f'Maior numero: {n3}')
        print(f'Menor numero: {n2}')
elif(n2 > n3):
    print(f'Maior numero: {n2}')
    print(f'Menor numero: {n1}')
else:
    print(f'Maior numero: {n3}')
    print(f'Menor numero: {n1}')


# Desafio 34
print('\n\nDesafio 34')
salario = float(input('Valor do Salario: '))
if(salario > 1200):
    print(
        f'Salario Atual: R${salario:.2f} --> Aumento de 10% R${salario*0.10} --> Salario com o Ajuste R${salario + (salario*0.10):.2f}')
else:
    print(
        f'Salario Atual: R${salario:.2f} --> Aumento de 15% R${salario*0.15} --> Salario com o Ajuste R${salario + (salario*0.15):.2f}')


# Desafio 35
print('\n\nDesafio 35')
n1 = float(input('Valor n1: '))
n2 = float(input('Valor n2: '))
n3 = float(input('Valor n3: '))

if(n1 > n2):
    if(n1 > n3):
        print('Medidas representam UM TRIANGULO' if((n2 + n3) > n1)
              else 'Medidas NÃO representam UM TRIANGULO')
    else:
        print('Medidas representam UM TRIANGULO' if((n2 + n1) > n3)
              else 'Medidas NÃO representam UM TRIANGULO')
elif(n2 > n3):
    print('Medidas representam UM TRIANGULO' if((n1 + n3) > n2)
          else 'Medidas NÃO representam UM TRIANGULO')
else:
    print('Medidas representam UM TRIANGULO' if((n2 + n1) > n3)
          else 'Medidas NÃO representam UM TRIANGULO')
