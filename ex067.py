while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 30)
    for i in range(1, 11):
        print(f'{n} X {i} = {n*i}')
    print('-' * 30)
print('Programa tabuada encerrado. volte sempre!')