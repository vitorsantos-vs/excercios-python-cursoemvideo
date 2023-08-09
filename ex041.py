from datetime import date
atual = date.today().year
ano = int(input('Qual a sua data de nascimento: '))
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria MIRIM')
elif idade <= 14:
    print('Você está na categoria INFANTIL')
elif idade <= 19:
    print('Você está na categoria JÚNIOR')
elif idade <= 25:
    print('Você está na categoria SÊNIOR') 
else:
    print('Você está na categoria MASTER')
    