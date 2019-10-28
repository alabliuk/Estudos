# https://www.youtube.com/watch?v=j9bYDjaAYzw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&t=0s

from datetime import date
from random import choice
from time import sleep

# Desafio 36
print('\n\nDesafio 36')
valor = float(input('Valor do imovel: '))
salario = float(input('Salario: '))
parcelas = int(input('Parcelas: '))

parcela_limite = salario * 0.30

if(parcela_limite > valor/parcelas):
    print('Financiamento Aprovado!')
else:
    print('Financiamento REPROVADO!')


# Desafio 37
print('\n\nDesafio 37')
valor = int(input('Digite um numero: '))
menu = int(input(
    f'Converter o numero {valor} para: \n1 - Binario\n2 - Octal\n3 - Hexadecimal\n\nConversão escolhida --> '))

if(menu == 1):
    print(f'Conversão Binaria: {valor} --> {valor:b}')
elif(menu == 2):
    print(f'Conversão Octal: {valor} --> {valor:o}')
elif(menu == 3):
    print(f'Conversão Hexadecimal: {valor} --> {valor:x}')


# Desafio 38
print('\n\nDesafio 38')
n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))

if(n1 > n2):
    print(f'{n1} (n1) é MAIOR que {n2} (n2)')
elif(n1 == n2):
    print(f'{n1} (n1) é IGUAL a {n2} (n2)')
else:
    print(f'{n1} (n1) é MENOR que {n2} (n2)')


# Desafio 39
print('\n\nDesafio 39')
nasc = int(input('Ano de nascimento: '))
anoCorrente = date.today().year
idade = anoCorrente - nasc
print(f'Idade: {idade}')
if(idade < 18):
    print(
        f'Seriço militar: Ainda não é necessario o alistamento || Restam {18 - idade} anos para o alistamento')
elif(idade == 18):
    print('Seriço militar: Voce precisa se alistar')
else:
    print(
        f'Seriço militar: Voce perdeu o prazo de alistamento || Foi excedido {idade - 18} anos para o alistamento')


# Desafio 40
print('\n\nDesafio 40')
n1 = float(input('Insira a nota 01: '))
n2 = float(input('Insira a nota 02: '))
media = (n1+n2)/2
print(f'Media: {media}')
if(media < 5):
    print('REPROVADO')
elif(media >= 7):
    print('APROVADO')
else:
    print('RECUPERAÇÃO')


# Desafio 41
print('\n\nDesafio 41')
nasc = int(input('Ano de nascimento: '))
anoCorrente = date.today().year
idade = anoCorrente - nasc
print(f'Idade: {idade}')
if(idade <= 9):
    print('Categoria: MIRIM')
elif(idade <= 14):
    print('Categoria: INFANTIL')
elif(idade <= 19):
    print('Categoria: JUNIOR')
elif(idade <= 25):
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')


# Desafio 42
print('\n\nDesafio 42')
n1 = float(input('Valor n1: '))
n2 = float(input('Valor n2: '))
n3 = float(input('Valor n3: '))

if(n1 == n2 == n3):
    print('Triangulo EQUILATERO')
elif(n1 == n2 or n2 == n3 or n3 == n1):
    print('Triangulo ISOCELES')
elif((n1 != n2 != n3 != n1) and (n1 + n2 > n3 and n2 + n3 > n1 and n3 + n1 > n2)):
    print('Triangulo ESCALENO')
else:
    print('Não é um Triangulo')


# Desafio 43
print('\n\nDesafio 43')
print('IMC')
peso = float(input('[KG] - Insira seu peso: '))
altura = float(input('[M] - Insira sua altura: '))
imc = peso / (altura**2)
print(f'IMC: {imc:.1f}')
if(imc < 18.5):
    print('Abaixo do Peso')
elif(imc < 25):
    print('Peso Ideal')
elif(imc < 30):
    print('Sobrepeso')
elif(imc < 40):
    print('Obesidade')
else:
    print('Obesidade Morbida')


# Desafio 44
print('\n\nDesafio 44')
valor_produto = float(input('Valor do produto: '))
print('\nFORMAS DE PAGAMENTO:')
menu = int(input('1 - Pagamento a Vista no Dinheiro/Cheque\n2 - Pagamento a Vista no Cartão\n3 - Pagamento em 2x no cartão\n4 - Pagamento em 3x ou mais\n\n--> '))

if(menu == 1):
    print(
        f'Valor Original: {valor_produto:.2f}\nValor com 10% de desconto: {valor_produto - (valor_produto * 0.10):.2f}')
elif(menu == 2):
    print(
        f'Valor Original: {valor_produto:.2f}\nValor com 5% de desconto: {valor_produto - (valor_produto * 0.05):.2f}')
elif(menu == 3):
    print(
        f'Valor Original: {valor_produto:.2f}\nValor em 2x Sem Juros: {valor_produto/2:.2f}')
elif(menu == 4):
    print(
        f'Valor Original: {valor_produto:.2f}\nValor total com 20% de juros: {valor_produto + (valor_produto * 0.20):.2f}')
else:
    print('Digito Invalido!')


# Desafio 45
print('\n\nDesafio 45')
print('Jokenpô')
user = int(input('\nEscolha:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\n--> '))

itens = ['Pedra', 'Papel', 'Tesoura']
pc = choice(itens)

if(0 < user <= 3):
    print('\nJO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(0.5)

    print(f'\nJogador escolheu: {itens[user-1]}')
    print(f'Computador escolheu: {pc}')

    if(user == 1 and pc != 'Papel'):
        if(pc != 'Pedra'):
            print('Você ganhou!')
        else:
            print('Empate!')
    elif(user == 2 and pc != 'Tesoura'):
        if(pc != 'Papel'):
            print('Você ganhou!')
        else:
            print('Empate!')
    elif(user == 3 and pc != 'Pedra'):
        if(pc != 'Tesoura'):
            print('Você ganhou!')
        else:
            print('Empate!')
    else:
        print('Você Perdeu!')

else:
    print('Opção Inválida!')
