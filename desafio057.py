# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
#Caso esteja errado, peça a digitação novamente até ter um valor correto
# Questão sobre validação de dados!
nome= str(input('Digite seu nome: ')).strip().upper()
sexo = str(input('\033[1;30m''Digite Seu sexo [M/F]: ''\033[m')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('\033[1;31m''Dado inválido! Digite seu sexo corretamente [M/F]: ''\033[m')).upper().strip()
print('\033[1;36m''OLÁ SEU, CADASTRO FOI FINALIZADO!''\033[m')
print('{}'.format(nome))
print('\033[1;36m''TENHA UM ÓTIMO DIA!''\033[m')
