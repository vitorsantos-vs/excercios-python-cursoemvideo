print('{:=^40}'.format(' LOJAS VS '))
preco = float(input('Preco das compras: R$'))
print('''FORMAS DE PAGMENTO
[ 1 ] à vsta dinheiro
[ 2 ] à vista cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será pacelada em 2X de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input('Quantas vezes quer pagar? : '))
    parcela = total / total_parcelas
    print('Sua compra será pacelada em {}X de R${:.2f} COM JUROS' .format(total_parcelas, parcela))
else:
    total = preco
    print('Opção inválida. Tente novamente.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.' .format(preco, total))

