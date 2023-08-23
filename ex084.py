temp = []
princ = []
maior = 0
menor = 0
while True:
    temp.append(str(input('Digite o nome: ')))  
    temp.append(float(input('Digite o peso: ')))  
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    continua = ' '      
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ' )).strip().upper()
    if continua == 'N':
        break   
print('=-' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')    
print(f'O maior peso foi de {maior}KG. Peso de ', end='')
for p in princ:
    if p[1] == maior:   
        print(f'[{p[0]}] ', end='')
print('')
print(f'O menor peso foi de {menor}KG. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print('')

