# https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6

# Desafio 22
print('\n\nDesafio 22')
nome = input('Digite seu nome completo: ')
print(f'letras maiusculas: {nome.lower()}')
print(f'letras minusculas: {nome.upper()}')
print(f'quantidade de letras sem espaço: {nome.replace(" ", "")} ')
print(f'quantidade de letras no primeiro nome: {len(nome.split()[0])}')
