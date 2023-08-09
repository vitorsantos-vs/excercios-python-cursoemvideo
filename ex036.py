casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite quantos anos de financiamento?: '))

prestacao = casa / (anos * 12) 
minimo = salario * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
if prestacao <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
    


