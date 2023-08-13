lista = []
while True:
    lista.append(int(input('Digite um valor: ')))  
    continua = ' '      
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ' )).strip().upper()
    if continua == 'N':
        break   
print('=-' * 30) 
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente são {lista}')
if 5 in lista:
    print ("O valor 5 faz parte da lista!")
else:
    print ('O valor 5 não foi encontrado na lista!')
    