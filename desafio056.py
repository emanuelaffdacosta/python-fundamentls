somaidade = 0
médiaidade = 0
maioridadehomem = 0
menoridademlr = 0
nomevelho = ''
totalmlr20 = 0
nomemlr = 0
for pessoa in range(1, 5):
    print('======={}ª PESSOA======'.format(pessoa))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]? ')).strip()
    somaidade = somaidade + idade
    if pessoa == 1 and sexo in 'Mm': #aqui o in foi utilizado como segunda opção do uso do upper.
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmlr20 +=1
        menoridademlr = idade
        nomemlr = nome
médiaidade = somaidade / 4
print('a soma das idades é {} e a MÉDIA DO GRUPO é {:.0f}'.format(somaidade, médiaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadehomem))
print('Há {} MLRs com menos de 20 anos se chama {} e tem {} anos'.format(totalmlr20, nomemlr, menoridademlr))
