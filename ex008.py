medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('Em Quilômetro {} é igual a {} Quilômetro'.format(medida, km))
print('Em Hectômetro {} é igual a {} Hectômetro'.format(medida, hm))
print('Em Decâmetro {} é igual a {} Decâmetro'.format(medida, dam))
print('Em decímetro {} é igual a {:.0f} decímetro'.format(medida, dm))
print('Em cintimetos {} é igual a {:.0f} centimetos'.format(medida, cm))
print('Em milimetros {} é igual a {:.0f} milimetros'.format(medida, mm))