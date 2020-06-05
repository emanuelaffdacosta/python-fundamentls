from datetime import date
anoatual = date.today().year
totalmaior = 0
totalmenor = 0
for ind in range(1, 8):
    ano = int(input('Que ano a {}ª pessoa nasceu? '.format(ind)))
    idade = anoatual - ano
    if idade >= 21:
        totalmaior += 1
    elif idade <= 21:
        totalmenor += 1
print('há {} pessoas maiores de idade'.format(totalmaior))
print('E menores de idade foram {}'.format(totalmenor))
