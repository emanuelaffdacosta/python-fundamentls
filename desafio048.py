#faça um programa que calcule a soma de todos os números ímpares que são múltipols
# de três e que se encontram no intervalo de 1 até 500
soma = 0 #nesse caso devo fazer um acumulador
contador = 0 #para contar os números que existem no intervalo
for num in range(1, 501, 2):
    if num % 3 == 0:
        soma += num
        contador += 1
print('A soma dos {} termos é {}'.format(contador, soma))
print('FINISH')
