real = float(input('Qunato você tem para comverter? R$'))
dolar = real / 5.00
euro = real / 5.40
print('Com {:.2f} você pode converter para US${:.2f} dolares'. format(real, dolar))
print('Com {:.2f} você pode converter para EUR${:.2f} euros'.format(real, euro))