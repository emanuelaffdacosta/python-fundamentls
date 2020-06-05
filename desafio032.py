#FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUQER E MOSTRE SE ELE É BISSEXTO
ano = int(input('Olá, em que ano você está? Coloque 0 para analisar o ano atual: '))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
