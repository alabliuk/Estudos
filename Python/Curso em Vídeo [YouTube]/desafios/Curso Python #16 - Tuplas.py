# https://www.youtube.com/watch?v=0LB3FSfjvao&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH

from random import randint

# # Desafio 72
# print('\n\nDesafio 72')
# num_name = ('zero', 'um', 'dois', 'tres', 'quatro',
#             'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
#             'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
#             'dezessete', 'dezoito', 'dezenove', 'vinte')
# while(True):
#     num = int(input('Digite um numero entre  0 e 20: '))
#     if(num >= 0 and num <= 20):
#         print(f'Você digitou o numero {num_name[num]}')
#         break


# # Desafio 73
# print('\n\nDesafio 73')
# times = ('FLAMENGO', 'PALMEIRAS', 'SANTOS', 'GRÊMIO', 'SÃO PAULO', 'ATHLETICO', 'INTERNACIONAL', 'CORINTHIANS', 'BAHIA',
#          'GOIÁS', 'VASCO', 'ATLÉTICO-MG', 'FORTALEZA', 'BOTAFOGO', 'CEARÁ', 'CRUZEIRO', 'FLUMINENSE', 'CSA', 'CHAPECOENSE', 'AVAÍ')

# print(f'Lista de  times  do Brasileirão: {times}')
# print(f'Os 5 primeirossão: {times[0:5]}')
# print(f'Os 4 ultimos são: {times[-4]}')
# print(f'Times em orderm alfabetica: {sorted(times)}')
# # print(f'A chapecoence está na: {}ª posição')


# Desafio 74
print('\n\nDesafio 74')
teste = (randint(0, 9), randint(0, 9), randint(
    0, 9), randint(0, 9), randint(0, 9))
print(type(teste))
print(teste)
print(f'O maior valor foi: {sorted(teste)}')
print(f'O maior valor foi: {sorted(teste, reverse=True)}')
