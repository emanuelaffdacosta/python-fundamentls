#crie um programa que leia dois valores e mostre um menu como o ao lado da tela: 1 SOMAR
#2 MULTIPLICAR 3 MAIOR 4 NOVOS NÚMEROS 5 SAIR DO PROGRAMA
#seu programa deverá realizar a operação solicitada em cada caso.
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opção = int(input('----->>>> Qual é a sua opção? '))
    if opção == 1:
        soma = (a + b)
        print('A soma é {}'.format(soma))
    elif opção == 2:
        produto = (a * b)
        print('O produto é {}'.format(produto))
    elif opção == 3:
        if a > b:
            print('O valor {} é maior'.format(a))
        elif b > a:
            print('O valor {} é maior'.format(b))
    elif opção == 4:
        print('Informe os números novamente: ')
        a = int(input('1º valor: '))
        b = int(input('2ª valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('=~=' * 10)
print('Fim do programa! Até mais!!')
