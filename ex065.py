quant = soma = maior = menor = media = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
media = soma / quant
print('Você digitou {} e a media entre eles é {}'.format(quant, media))
print('O maior número é {} e o menor número é {}'.format(maior, menor))
