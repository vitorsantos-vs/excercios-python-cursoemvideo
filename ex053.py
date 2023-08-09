frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
invero = ''
for letra in range(len(junto) -1, -1, -1):
    invero += junto[letra]
print('O inverso de {} é {}'.format(junto, invero))
if invero == junto:
    print('A frase é um palíndromo')
else:
    print("A frase não é um palindromo")
