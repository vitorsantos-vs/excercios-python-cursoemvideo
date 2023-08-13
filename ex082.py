lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))  
    continua = ' '      
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ' )).strip().upper()
    if continua == 'N':
        break   
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)    
    elif v % 2 == 1:
        impar.append(v)
print('=-' * 30)
print(f'lista completa {lista}')
print(f'Lista par {par}')
print(f'Lista impar {impar}')