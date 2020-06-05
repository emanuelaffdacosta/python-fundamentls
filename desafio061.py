#REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA,
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE
print('~=' * 10)
print('GERADOR DE PA!!')
print('~=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razão
    contador += 1
print('fim!')
