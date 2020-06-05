#CRIE UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA
#MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
# MÉDIA ABAIXO DE 5.0: REPROVADO / MÉDIO ENTRE 5.0 E 6.9 CECUPERAÇÃO / MÉDIA 7.0 OU SUPERIO APROVADO
a = float(input('Digite a primeira nota: '))
b = float(input('Digite a segunda nota: '))
md = (a + b) / 2
if md >= 7:
   print('Parabéns você foi {} APROVADO{}, sua média foi {}{:.1f}{}'.format('\033[1;34m', '\033[m', '\033[1;30;44m', md, '\033[m'))
elif md < 7 and md >= 5: #ou 7 > md >=5:
    print('Você ficou de {} RECUPERAÇÃO{}, sua média foi {}{:.1f}{}'.format('\033[1;33m','\033[m','\033[1;33m', md, '\033[m)'))
elif md < 5:
    print('Você foi {}REPROVADO{}! Com a média {}{:.1f}{}'.format('\033[1;31m', '\033[m', '\033[1;31;40m', md, '\033[m'))
print('\033[1;30m''As provas estão na coordenação!! :)''\033[m')
