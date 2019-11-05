# https://www.youtube.com/watch?v=1OFp_-R2B2A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye

from random import randint

# # Desafio 66
# print('\n\nDesafio 66')
# soma = 0
# c = 0
# while(True):
#     valor = int(input('Digite um valor (999 para sair) --> '))
#     soma += valor
#     if(valor == 999):
#         print(f'A soma dos {c} valores foi de {soma -999}!')
#         break
#     c += 1


# # Desafio 67
# print('\n\nDesafio 67')
# while(True):
#     print('-'*20)
#     tabuada = int(input('Tabuada a ser renderizada --> '))
#     if(tabuada > 0):
#         for c in range(1, 11):
#             print(f'{tabuada} x {c:2} = {tabuada*c:3}')
#     else:
#         break


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
        num_maq = randint(0, 10)
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


# # Desafio 69
# print('\n\nDesafio 69')

# idade = 0
# sexo = ''
# continua = ''
# count_idade = 0
# count_homens = 0
# count_mulheres_abaixo_vinte = 0

# while(True):
#     print('-'*20)
#     print('Cadastre uma Pessoa')
#     print('-'*20)

#     while(True):
#         idade = int(input('Idade: '))
#         if(idade > 0):
#             if(idade > 18):
#                 count_idade += 1
#             break

#     while(True):
#         sexo = input('Sexo [M/F]: ').upper()
#         if(sexo in 'MF'):
#             if(sexo == 'M'):
#                 count_homens += 1
#             elif(sexo == 'F' and idade < 20):
#                 count_mulheres_abaixo_vinte += idade
#             break

#     while(True):
#         continua = input('Deseja continuar? [S/N]: ').upper()
#         if(continua in 'S'):
#             break
#         elif(continua == 'N'):
#             print('Apuração dos dados:\n')
#             print(f'Total de pessoas com mais de 18 anos: {count_idade}')
#             print(f'Total de Homens Cadastrados: {count_homens}')
#             print(
#                 f'Total de mulheres com menos de 20 anos: {count_mulheres_abaixo_vinte}')

#             break

#     if(continua == 'N'):
#         break


# Desafio 70
print('\n\nDesafio 70')

