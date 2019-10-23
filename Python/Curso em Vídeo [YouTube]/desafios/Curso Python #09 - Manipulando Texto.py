# https://www.youtube.com/watch?v=a7DH88vk2Sk&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6

# Desafio 22
print('\n\nDesafio 22')
nomeCompleto = input('Digite seu nome completo: ')
print(f'letras maiusculas: {nomeCompleto.lower()}')
print(f'letras minusculas: {nomeCompleto.upper()}')
print(
    f'quantidade de letras sem espaço: {len(nomeCompleto.replace(" ", ""))} ')
print(f'quantidade de letras no primeiro nome: {len(nomeCompleto.split()[0])}')


# Desafio 23
print('\n\nDesafio 23')
num = int(input('Digite um número de 0 a 9999: '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print(f'milhar:  {m}')
print(f'centena: {c}')
print(f'dezena:  {d}')
print(f'unidade: {u}')


# Desafio 24
print('\n\nDesafio 24')
cidade = input('Digite o nome da sua cidade: ').strip()
if(cidade[:5].upper() == 'SANTO'):
    print('Sua cidade começa com o nome SANTO')
else:
    print('Sua cidade não começa com o nome SANTO')


# Desafio 25
print('\n\nDesafio 25')
nome = input('Digite seu nome: ').strip()
if(nome.upper().find('SILVA') >= 0):
    print('Seu nome tem Siva')
else:
    print('Seu nome não tem Siva')
# OU
print(f'Existe Silva? {"silva" in nome.lower()}')


# Desafio 26
print('\n\nDesafio 26')
frase = input('Digite uma frase: ').upper().strip()
print(f'Quantidade de vezes que aparece a letra A: {frase.count("A")}')
print(f'Em qual posição apareceu pela primeira vez: {frase.find("A")+1}')
print(f'Em qual posição apareceu pela ultima vez: {frase.rfind("A")+1}')


# Desafio 26
print('\n\nDesafio 27')
nomeCompleto = input('Digite seu nome completo: ').strip()
nome = nomeCompleto.split()
print(f'Primeiro nome: {nome[0]}')
print(f'Ultimo nome: {nome[len(nome)-1]}')
