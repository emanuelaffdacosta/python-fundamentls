nome = input('Digite seu nome: ')
print('Olá {}, é um prazer receber você em nossa loja!!'.format(nome))
preço = float(input('Qual valor da mercadoria escolhida? R$ '))
avista = preço - (preço*20/100)
aprazo = preço + (preço*25/100)
pagamento = input('Como deseja pagar, a vista ou a prazo? ')
tipo = input('Qual bandeira do cartão? ')
recarga = input('Vamos recarregar o telefone hoje? ')
troco = input('aceita bala de troco? ')
print('Sua compra no valor de R${:.2f}, sairá por {:.2f} a vista e {:.2f} a prazo!!'.format(preço, avista, aprazo))
