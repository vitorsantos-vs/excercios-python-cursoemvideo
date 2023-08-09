from datetime import date
atual = date.today().year
sexo = str(input('Qual o seu sexo [M/F]: ')).upper()

if sexo == 'M':   
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano     
    if idade == 18:
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
        print('Você tem que se alsitar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
        print('Ainda faltam {} anos para seu alistamento'.format(saldo))
        print('seu alistamentoserá em {}.'.format(atual + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
        print('Você já deveria ter se alista há {} anos.'.format(saldo))
        print('Seu alistamento foi em {}.'.format(atual - saldo))
else:
    print('Mulher não tem alistamento obrigatório!')