totvalor = totmil = menor = cont = 0
barato = ' '
print('-' * 25) 
print('{:-^40}'.format(' Lojinha.com.br'))
while True:    
    print('-' * 25) 
    Produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    totvalor += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = Produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
    
print('{:-^40}'.format(' Fim da compra '))
print(f'O total da compra foi R${totvalor:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
    