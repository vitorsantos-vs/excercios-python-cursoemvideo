from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior número
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    escolha = int(input('>>>>> Escolha uma opção: '))
    if escolha == 1:
        soma = num1 + num2
        print('A soma entre {} + {} = {}'.format(num1, num2, soma))
    elif escolha == 2:
        produto = num1 * num2
        print('A multiplicação entre {} x {} = {}'.format(num1, num2, produto))
    elif escolha == 3:
        maior_numero = max([num1, num2])
        #alternativa
        '''
        if num1 > n2:
            maior_numero = num1
        else:
            maior_numero = num2
        '''
        print('Entre {} e {} o maior valor é {}'.format(num1, num2, maior_numero))
    elif escolha == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Novo primeiro valor:'))
        num2 = int(input('Novo segundo valor:'))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')