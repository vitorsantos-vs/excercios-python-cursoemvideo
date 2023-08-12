times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
          'Flamengo', 'Vasco', 'Chapecoense', 'Atletico', 'Botafogo',
          'Atletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sporte Recife',
          'EC Vitoria', 'Coritiba', 'Avai', 'Ponte Preta', 'Atletico-GO')
cont = 1
pos = 1

'''Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
A)Apenas os primeiros 5 colocados.
B)Os últimos 4 colocados
C)Uma lista com os times em ordem alfabética
D)Em que posição na tabela está o time da Chapecoense'''
print('+-+'*15)
print(f'Lista de times do Brasileirão: {times}')
print('+-+'*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('+-+'*15)
print(f'Os 4 últimos são: {times [-4:]}')
print('+-+'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('+-+'*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição') 