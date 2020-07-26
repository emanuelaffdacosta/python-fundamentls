medida = float(input('Digite um valor em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
#print('O valor de {} em centímetros é {} \nem milímetros é {}'.format (n, (n*100), (n*1000)))
#print('A medida em {}m corresponde a {}cm e {}mm.'.format(medida, cm, mm))
print('A medida de {}m, corresponde a {}km, {}hm, {}dam, {}dm, {}cm e {}mm.'.format(medida, km, hm, dam, dm, cm, mm))
