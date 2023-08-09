n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for i in range(1, 11, 1):
    print('{} X {:2} = {}'.format(n, i, (n * i)))
print('-' * 12)