#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LAIA O ANO DE NASCIMENTO DE UM ATLETA
# E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE: ATÉ 9 ANOS = MIRIM
#ATÉ 14 : INFANTIL / ATÉ 19 JUNIOR/ ATÉ 25: SÊNIOR/ ACIMA: MASTER
from datetime import date
from time import sleep
atual = date.today().year
print('~~'*20)
print('{} OLÁ, SEJAM BEM VINDOS AO AQUASHOW !!!{}'.format('\033[1;30;44m', '\033[m'))
print('~~'*20)
ask = str(input('Deseja fazer nosso teste das categorias? '))
print('PROCESSANDO...')
sleep(2)
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print('Verificando os dados informados... Aguarde')
sleep(2)
if idade <= 9:
    print('Você tem {} anos e se encaixa na categoria {}MIRIM!{}'.format(idade, '\033[1;30m', '\033[m'))
elif idade <= 14:
    print('Você tem {} anos e se encaixa na categoria {}INFANTIL{}'.format(idade, '\033[1;30m', '\030[m'))
elif idade <= 19:
    print('Você tem {} anos e se encaixa na categoria {}JÚNIOR{}'.format(idade, '\033[1;30m', '\033[m'))
elif idade <= 25:
    print('Você tem {} anos e se encaixa na categoria {}SÊNIOR{}'.format(idade, '\033[1;30m', '\033[m'))
elif idade > 25:
    print('Você tem {} anos e se encaixa na categoria {}MASTER{}'.format(idade, '\033[1;30m', '\033[m'))
    