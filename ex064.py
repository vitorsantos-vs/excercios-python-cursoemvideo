num = cont = soma = 0
num = int(input('Digite um nummero [Ou 999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um nummero [Ou 999 para parar]: '))
print('Foram digitados {} numeros e a soma deles é {}.'.format(cont, soma))