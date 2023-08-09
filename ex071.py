print('=' * 30)
print('{:^30}'.format('Caixa Eletrônico'))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
cedula = 50
totalcdl = 0 
while True:
    if total >= cedula:
        total -= cedula
        totalcdl +=1
    else:
        if totalcdl > 0:    
            print(f'Total de {total} notas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20: 
            cedula = 10 
        elif cedula == 10:  
            cedula = 1
        totalcdl = 0  
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao banco VS!')
