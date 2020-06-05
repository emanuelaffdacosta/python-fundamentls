num = int(input('Digite um valor: '))
total = 0
for x in range(1, num + 1):
    if num % x == 0:
        print('\033[1;34m', end='')
        total += 1
    else:
        print('\033[1;35m', end='')
    print('{}'.format(x), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('PRIMO')
else:
    print('NÃO É PRIMO')
