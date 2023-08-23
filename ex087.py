matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_impar = 0
maior = 0
soma_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite para a posição [{l} x {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        elif matriz[l][c] % 2 == 1:
            soma_impar += matriz[l][c]
    print() 
print('=-' * 30)
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores ímpares é {soma_impar}')
print('=-' * 30)
for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda é {maior}.')
