# https://www.youtube.com/watch?v=Vw6gLypRKmY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&t

# Desafio 05
print('\n\nDesafio 05')
x = int(input('Digite um numero --> '))
print(f'{x-1} <-- {x} --> {x+1}')

# Desafio 06
print('\n\nDesafio 06')
x = int(input('Digite um numero --> '))
print(f'Numero: {x}, Dobro: {x*2}, Triplo: {x*3}, Raiz Quadrada {x**(1/2)}')

# Desafio 07
print('\n\nDesafio 07')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
print(f'Média: {(n1+n2)/2}')

# Desafio 08
print('\n\nDesafio 08')
metros = float(input('metros: '))
print(f'centimetros: {metros * 100}')
print(f'milimetros: {metros * 1000}')

# Desafio 09
print('\n\nDesafio 09')
tab = int(input('Exibir a tabuada do numero: '))
aux = int(0)
while aux <= 10:
    print(f'{tab} x {aux} = {tab*aux}')
    aux += 1

# Desafio 10
print('\n\nDesafio 10')
real = float(input('R$: '))
valorDolar = float(3.27)
print(
    f'Conversão: BRL {real} --> USD {real * valorDolar} || Cotação Dolar: {valorDolar}')

# Desafio 11
print('\n\nDesafio 11')
altura = float(input('Altura: '))
largura = float(input('Largura: '))

area = largura * altura

print(f'Altura: {altura} x Largura: {largura} = Area: {area}')
print(
    f'Será necessario {area/2:.2f} litros de tinta || 1 litro de tinta = 2 metros')

# Desafio 12
print('\n\nDesafio 12')
preco = float(input('Preço Produto: '))
print(
    f'Preço original: {preco:.2f} || Preço com 5% de desconto: {preco - (5 * (preco/100)):.2f} ')

# Desafio 13
print('\n\nDesafio 13')
sal = float(input('Salario: '))
print(
    f'Salario atual: {sal} || Salario com aumento de 15%: {sal + (15 * (sal/100)):.2f}')
