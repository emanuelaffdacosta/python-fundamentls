algo = input('Digite algo: ')
print('O tipo primitivo de {} é '.format(algo), type(algo))
print('Só tem espaço? ', algo.isspace())
print('É numérico? ', algo.isnumeric())
print('É alfa numerico? ', algo.isalnum())
print('Está em caixa alta? ', algo.isupper())
print('Está em minúscula? ', algo.islower())
print('Ela está capitalizada? ', algo.istitle())