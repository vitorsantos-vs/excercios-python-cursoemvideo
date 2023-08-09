np1 = float(input('Primeira nota: '))
np2 = float(input('Segunda nota: '))
media = (np1 + np2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(np1, np2, media))
if media < 5.0:    
    print('Está REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('Está RECUPERAÇÃO!')
else:
    print('Está APROVADO!')