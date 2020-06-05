soma = 0
c = 0
for cont in range(1, 7):
    num = int(input('digite um valor: '))
    if num % 2 == 0: #nesse caso com a ajuda do if você já obtem o resultado esperado, logo não é necessa´rio utilizar o elif
        soma += num
        c += 1
print('A soma dos {} números pares foi de {}'.format(c, soma))
