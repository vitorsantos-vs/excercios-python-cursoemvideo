numero = int(input('Digite um numero para verificar se ele é (PAR ou IMPAR): '))
resultador = numero % 2
if resultador == 0:
    print('O numero {} é PAR'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))
    