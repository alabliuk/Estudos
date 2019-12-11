from random import randint

print('-=-'*20)
print('\t\tMega Sena Generator')
print('-=-'*20)

jogos = int(input('\nQuantidade de jogos --> '))

for n in range(jogos):
    print(f'\n\nJogo {n+1}')

    for x in range(6):
        print(randint(1, 60), end=' ')
