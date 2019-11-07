# https://www.youtube.com/watch?v=1OFp_-R2B2A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye

from random import randint

# Desafio 66
print('\n\nDesafio 66')
soma = 0
c = 0
while(True):
    valor = int(input('Digite um valor (999 para sair) --> '))
    soma += valor
    if(valor == 999):
        print(f'A soma dos {c} valores foi de {soma -999}!')
        break
    c += 1


# Desafio 67
print('\n\nDesafio 67')
while(True):
    print('-'*20)
    tabuada = int(input('Tabuada a ser renderizada --> '))
    if(tabuada > 0):
        for c in range(1, 11):
            print(f'{tabuada} x {c:2} = {tabuada*c:3}')
    else:
        break


# Desafio 68
print('\n\nDesafio 68')
print('-= JOGO do PAR ou IMPAR =-')
c = 1
num_user = 0
esc_user = ''
num_maq = 0
plac_maq = 0
plac_user = 0

itens = ['Par', 'Impar']

while(True):
    print(f'Rodada {c}')
    num_user = int(input('Digite um valor (0 a 10) --> '))
    esc_user = input('Par [P] ou Impar [I] --> ').upper()

    if(esc_user in 'PI' and num_user >= 0 and num_user <= 10):
        num_maq = randint(0, 11)
        print(f'\nJogada:\nVoce {num_user} x {num_maq} Máquina')
        print(f'TOTAL: {num_user + num_maq} -->', end=' ')

        calc = (num_user + num_maq) % 2

        if(esc_user == 'P'):
            if(calc == 0):
                print('Resultado: PAR')
                plac_user += 1
            else:
                print('Resultado: IMPAR')
                plac_maq += 1
                break
        else:
            if(calc == 0):
                print('Resultado: PAR')
                plac_maq += 1
                break
            else:
                print('Resultado: IMPAR')
                plac_user += 1
    else:
        plac_maq += 1
        print('Entrada Invalida!')
        break

    c += 1
    print(f'\nPlacar:\nVocê {plac_user} x {plac_maq} Máquina\n')

print(f'\nPlacar:\nVocê {plac_user} x {plac_maq} Máquina\n')

if(plac_maq >= 1):
    print('\nFim de Jogo!')


# Desafio 69
print('\n\nDesafio 69')

idade = 0
sexo = ''
continua = ''
count_idade = 0
count_homens = 0
count_mulheres_abaixo_vinte = 0

while(True):
    print('-'*20)
    print('Cadastre uma Pessoa')
    print('-'*20)

    while(True):
        idade = int(input('Idade: '))
        if(idade > 0):
            if(idade > 18):
                count_idade += 1
            break

    while(True):
        sexo = input('Sexo [M/F]: ').upper()
        if(sexo in 'MF'):
            if(sexo == 'M'):
                count_homens += 1
            elif(sexo == 'F' and idade < 20):
                count_mulheres_abaixo_vinte += 1
            break

    while(True):
        continua = input('Deseja continuar? [S/N]: ').upper()
        if(continua in 'S'):
            break
        elif(continua == 'N'):
            print('Apuração dos dados:\n')
            print(f'Total de pessoas com mais de 18 anos: {count_idade}')
            print(f'Total de Homens Cadastrados: {count_homens}')
            print(
                f'Total de mulheres com menos de 20 anos: {count_mulheres_abaixo_vinte}')
            break

    if(continua == 'N'):
        break


# Desafio 70
print('\n\nDesafio 70')

soma_preco = 0
itens_maior_mil = 0
preco_produto_mais_barato = 0
nome_produto_mais_barato = ''
continuar = ''

while(True):
    produto = input('Nome do produto: ')
    preco = float(input('Preço do Produto: R$ '))
    soma_preco += preco

    if(preco > 1000):
        itens_maior_mil += 1

    if(preco_produto_mais_barato == 0 or preco_produto_mais_barato >= preco):
        preco_produto_mais_barato = preco
        nome_produto_mais_barato = produto

    while(True):
        continuar = input('Cadastrar mais produtos [S/N] ? --> ').upper()
        if(continuar == 'S'):
            break
        elif(continuar == 'N'):
            print('\nApuração dos dados:\n')
            print(f'Preço total: R$ {soma_preco}')
            print(f'Produtos que custam acima de R$1000: {itens_maior_mil}')
            print(f'Nome do produto mais barato: {nome_produto_mais_barato}')
            break

    if(continuar == 'N'):
        break


#Desafio 71
print('\n\nDesafio 71')
print('-=-'*20)
print('\t\tCaixa Eletronico - SAQUE')
print('-=-'*20)

valor_saque = int(input('\nQual é o valor a ser sacado? R$ '))
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas01 = 0

while(valor_saque > 0):
    if(valor_saque % 50 == 0):
        valor_saque -= 50
        cedulas50 += 1
    elif(valor_saque % 20 == 0):
        valor_saque -= 20
        cedulas20 += 1
    elif(valor_saque % 10 == 0):
        valor_saque -= 10
        cedulas10 += 1
    elif(valor_saque % 1 == 0):
        valor_saque -= 1
        cedulas01 += 1

print(f'Total de {cedulas50} cedulas de R$ 50')
print(f'Total de {cedulas20} cedulas de R$ 20')
print(f'Total de {cedulas10} cedulas de R$ 10')
print(f'Total de {cedulas01} cedulas de R$ 1')


print('-=-'*20)
print('\t\tCaixa Eletronico II - SAQUE')
print('-=-'*20)

valor_saque = int(input('\nQual é o valor a ser sacado? R$ '))
cedula = 50
c = 0

while(True):
    if(valor_saque >= cedula):
        valor_saque -= cedula
        c += 1
    else:
        if(c != 0):
            print(f'Total de {c} cedulas de R$ {cedula}')
        c = 0
        if(cedula == 50):
            cedula = 20
        elif(cedula == 20):
            cedula = 10
        elif(cedula == 10):
            cedula = 1
        else:
            break       
        