# https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6

# Desafio 14
print('*' * 50)
print('\n\nDesafio 14')
print('Conversor de Celsius para Fahrenheit\n\n')
c = float(input('Insira o valor de Celsius a ser convertido: '))

f = (c*9/5) + 32

print(f'Conversão C to F: \n\n  {c:.2f}°C <--> {f:.2f}°F')


# Desafio 15
print('\n\nDesafio 15')
dias_alugado = int(input('Quantos dias alugado? '))
km_rodado = float(input('Quantos km rodados? '))

diaria = 60
km_valor = 0.15

print(f'O total a pagar é de R${(dias_alugado*diaria) + (km_rodado*km_valor):.2f}')
