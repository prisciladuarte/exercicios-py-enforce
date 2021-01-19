#Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um numero e 
# comparar com um conjunto aleatorio de numeros de (0 a 100)) e dizer se o usuário adivinhou

from random import randint

num = randint(0, 100)

print('-----------------------------------------------')

print('Olá, seja bem-vindo(a) a Loteria Magic!' )
nome = input('Qual o seu nome? ')
num =  input('{}, digite o seu número da sorte: '.format(nome))
print('O número que você escolheu foi: {}.'.format(num))
print('Aguarde, estamos verificando se seu número foi sorteado...')

lista = [0, 100]
#list('{}'.format(num))

while True:
    num = randint(0, 100)
    if num in lista:
        print('Você ACERTOU')

#lista de numeros aleatorios

#comparação entre numero digitado (num) e (lista_aleat)


print('---------------------------------------------------------')
print('-------------------BOA SORTE!-----------------------------')
print('--------------------------------------------------------')

