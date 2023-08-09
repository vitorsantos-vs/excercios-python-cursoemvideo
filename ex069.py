tot18 = totH = totM20 = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()
    print('-' * 25)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1        
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar [S/N]: ' )).strip().upper()
    if continua == 'N':
        break
print(f'Total de pessoas maior de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrado.')
print(f'E temos {totM20} mulheres com menos de 20 anos.')
    
