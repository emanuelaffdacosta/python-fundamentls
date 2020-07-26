#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = alt * larg
print('A sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².'.format(larg, alt, área))
tinta = área / 2
print('Sua parede deverá usar {}L de tinta '.format(tinta))
