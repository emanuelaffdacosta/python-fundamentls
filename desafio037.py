
n1 = int(input('digite um valor inteiro: '))
print('''Escolha a conversão dos números
[1] BINÁRIO
[2] OCTAL 
[3] HEXADECIMAL''')
opção = int(input('Escolha sua opção: '))
if opção == 1:
    print('O valor {} convertido em binário {}'.format(n1, bin(n1)[2:]))
elif opção == 2:
    print('O valor {} convertido em octal é {}'.format(n1, oct(n1)[2:]))
elif opção == 3:
    print('O valor {} convertido em hexadecimal {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção inválida, tente novamente')

