dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM rodados? '))
valor = (60 * dias) + (0.15 * km)
print('O total a pagar é de R${:.2f}'.format(valor))