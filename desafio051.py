#desenvola um progama que leia o primeiro termo e a razão de uma PA. No final,
#mostre os 10 primeiro termos
#dessa progressão
print('~-' * 20)
print('DESVENDANDO OS 10 TERMOS DE UMA PA')
print('~-' * 20)
primeiro = int(input('primeiro termo: '))
r = int(input('Razão: '))
decimo = primeiro + (10 - 1) * r
for c in range(primeiro, decimo, r):
    print(c, end='-> ')
print('fim')
