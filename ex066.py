cont = soma = 0
while True: 
    num = int(input('Digite um número [OU 999 para parar!]: '))
    if num == 999:
        break 
    cont += 1   
    soma += num    
print(f'Foram digitados {cont} números e a soma deles é {soma}.')
