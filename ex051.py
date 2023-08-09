print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
termo = int(input('Quantos termos você quer: '))
qdt = primeiro + (termo - 1) * razao
for i in range(primeiro, qdt + razao, razao):
    print('{} -> '.format((i)), end='')
print('FIM')