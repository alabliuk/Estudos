# https://www.youtube.com/watch?v=tHYxjJxtJko&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=11

var = input('Digite algo --> ')

print(f'O tipo primitivo desse valor é {type(var)}')
print(f'Só tem espaços? {var.isspace()}')
print(f'É um número? {var.isnumeric()}')
print(f'É alfabético {var.isalpha()}')
print(f'É alfanumérico {var.isalnum()}')
print(f'Está em maiúsculas? {var.isupper()}')
print(f'Está em minúsculas {var.islower()}')
print(f'Esta capitalizada {var.istitle()}') # Capitalizada = primeira letra em maiusculo (Ex: Python, Andre, Olá)
