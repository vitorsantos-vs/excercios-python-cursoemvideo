salario = float(input('Digite o salario atual do funcionario? R$:'))
if salario <= 1250.0:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Quem ganha R${:.2f} vai passar a ganhar R${:.2f} agora'.format(salario, aumento))