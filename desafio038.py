a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print('{} O primeiro valor é o maior!'.format('\033[30;1m'))
elif b > a:
    print('{} O segundo valor é maior!'.format('\033[32;1m'))
elif a == b: #nesse caso pode-se usar o else tb.
    print('{}Os valores são iguais!'.format('\033[36;1m'))
