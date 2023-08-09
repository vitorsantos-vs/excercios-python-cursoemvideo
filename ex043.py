peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (M) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25.0:
    print('PARABÉNS, você está na faixa de PESO NORMAL!')
elif 25.0 <= imc < 30.0:
    print('Você está em SOBREPESO.')
elif 30.0 <= imc < 40.0:
    print('Você está com OBESIDADE.')
elif imc >= 40:
    print('Você está OBESIDADE MÓBIDA.')

