frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''invertido = ''
for letra in range(len(junto) - 1, -1, -1):
    invertido += junto[letra]'''
invertido = junto [::-1] #pode ter essa solução tb
print(junto, invertido)
if junto == invertido:
    print('é palíndromo')
elif junto != invertido:
    print('não é palíndromo')
