distancia = float(input('Qual é a distância da sua viagem? '))
print('Você quer viajar {}km.'.format(distancia))
if distancia <= 200.0:
    preco = distancia * 0.50
    print('Sua viagem vai custar R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Sua viagem vai custar R${:.2f}'.format(preco))
    
'''
preco = distancia * 0.50 if distancia <= 200.0 else distancia * 0.45
print('Sua viagem vai custar R${:.2f}'.format(preco))
'''    