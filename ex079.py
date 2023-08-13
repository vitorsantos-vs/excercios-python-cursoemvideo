lista = []
while True:
    l = (int(input('Digite um valor: ')))
    if l not in lista:
        lista.append(l)
        print('\033[1;42mValor adicionado com sucesso!\033[m')           
    else :
        print('\033[1;31mValor duplicado! Não posso adicionar...\033[m')         
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ' )).strip().upper()
    if continua == 'N':
        break   
print('=-' * 30) 
lista.sort()
print(f'Voce digitou os valores {lista}')