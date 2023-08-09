from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    ano = int(input('Qual a data de nascomento da {}° pessoa? '.format(i)))
    idade = atual - ano
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemso {} pessoas mairoes de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))
