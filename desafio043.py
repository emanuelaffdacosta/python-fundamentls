#desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule sei IMC e mostre seu status, de acordo com a tabela abaixo
#abaixo de 18.5 = abaixo do peso / entre 18.5 e 25 = peso ideal / 25 até 30= sobrepeso/
#30 até 40: obesidade / acima de 40 = obesidade mórbida
peso = float(input('Digite o valor de seu peso: Kg '))
altura = float(input('Digite o valor de sua altura: m '))
IMC = peso / (altura * altura)
print('O IMC dessa pessoa é de {}{:.1f}{}'.format('\033[1;30m', IMC, '\033[m'))
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

