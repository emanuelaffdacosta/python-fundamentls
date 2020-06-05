#Crie um programa que leia um nome o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite um nome completo: ')).strip()
print('Seu nome tem Silva? {}'. format('Silva' in nome.title()))
