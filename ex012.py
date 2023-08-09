valor = float(input('Valor de produto sem desconto R$'))
desconto = valor - (valor * 5 / 100)
print('O produto de R${:.2f}, com desconto de 5% é: {:.2f}'.format(valor, desconto))