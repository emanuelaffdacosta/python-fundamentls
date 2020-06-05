#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE
# A MÉDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. O PROGRAMA
# DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.
num = 0
total = 0
soma = 0
maior = menor = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite mais um valor: '))
    resp = str(input('Quer continuar [S/N]? '))
    if num != 999:
        soma += num
        total += 1
        média = soma / total
    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Você forneceu {} numeros e a soma entre eles é {}, e média de {:.2f} !!'.format(total, soma, média))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
print('fim!')
