#melhore do desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos
#. o programa encerra quando ele disser que quer mostrar 0 termos
print('~o' * 10)
print('GERADOR DE PA')
print('~o' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('quantos termos vocês quer mostrar a mais? '))
print('PA finalizada com {} termos!!'.format(total))
