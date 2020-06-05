"""Crie um programa que leia o nome completo de uma
pessoa e mostre : O nome com todas as  letras maiúsculas,
o nome com todos minúsculas, quantas letras ao td (sem considerar espaços)
e quantas letras tem o primeiro nome"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome completo têm {} letras'.format(len(nome) - nome.count(' ')))
sespaco = nome.split()
print('Semeu primeiro nome têm {} letras'.format(len(sespaco[0])))

