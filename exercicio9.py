# 9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.

raio = float(input('Digite o valor do raio, para obter a área e o perímetro de um círculo: '))

area = 3.14 * raio ** 2
perimetro = 2 * 3.14 * raio 

print('A área do círculo corresponde a: {:.2f}'.format(area))
print('O perimetro do círculo corresponde a: {:.2f}'.format(perimetro))
