num = int(input('Digite um número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisível por {} vezes.'.format(num,tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('Porém não pode ser PRIMO!')