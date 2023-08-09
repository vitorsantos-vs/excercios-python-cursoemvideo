print('* Limite de valocidade 80KM/h *')
velocidade = float(input('Qual a velocidade do veicilo: '))
km = velocidade - 80.0
multa = 7.00 * km

if velocidade > 80.0:
    print('Você foi multado por estar {}km/h, no valor de R${:.2f}'.format(velocidade, multa))
print('Você passou {}km/h, e esta dentro do limite de velocidade'.format(velocidade))