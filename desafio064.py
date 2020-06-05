#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI
# PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA.
#NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES
#(DESCONSIDERANDO O FLAG)
n = 0
total = 0
soma = 0  #posso fazer assim, ou assim, como está descrito logo abaixo
# n = total = soma = 0
while n != 999:
    n = int(input('Digite um valor, [se qusier parar digite [999]: '))
    if n != 999:
        soma += n
        total +=1
print('Foram digitados {} a soma deles é {} números!'.format(total,  soma))
print('fim!!')
