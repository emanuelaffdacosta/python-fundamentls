#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
#SE ELE AINDA VAI SE ALISTAR AO SERVÇO MILITAR / SE ESTÁ NA HORA DE SE ALISTAR / SE JÁ PASSOU DO
# TEMPO DO ALISTAMENTO
#SEU PROGRAMA TAMBÉM DEVERÁ MPOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO
from datetime import date #Foi explicado na aula 8, essa função ativa o ano atual!
anoatual = date.today().year
anonasc = int(input('Ano de Nascimento: '))
sexo = str(input('Qual seu sexo? ')).strip().title()
idade = anoatual - anonasc
print('Quem nasceu em {} tem {} anos em {}'.format(anonasc, idade, anoatual))
if sexo == 'Masculino':
    print('Olá Jovem, seja bem vindo a junta militar!')
    if idade == 18:
        print('Você deve se alistar {}IMEDIATAMENTE{}!!!'.format('\033[1;31m', '\033[m'))
    elif idade < 18:
        falta = 18 - idade
        print('Falta(m) {}{}{} ano(s) para seu alistamento!'.format('\033[1;34m', falta, '\033[m'))
        ano = anoatual + falta
        print('O ano de seu alistamento será em {}'.format(ano))
    elif idade > 18:
        falta = idade - 18
        ano = anoatual - falta
        print('Passou(aram) {}{}{} ano(s) de seu alistamento. Regulazire sua situação!!!'.format('\033[1;31m', falta, '\033[m'))
        print('O ano de seu alistamento foi {}.'.format(ano))
else: #aqui pode ser elif tb.
    print('Alistamento {}NÃO OBRIGATÓRIO{}, para mulheres!'.format('\033[1;31m', '\033[m'))
