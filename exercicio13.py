print('-----------------------------------------------------------------------------------------------')

#mensagem de boas vindas
print('Seja bem-vindo(a) ao Travel Enterprises!\nVerificamos que este é o seu primeiro acesso, então vamos realizar o seu cadastro ')

#entrada do nome do usuario
nome = input('Digite o seu primeiro nome: ')

#imprime o nome de usuario na tela e dá instruções
print('Muito bem {}! Agora, entre as opções abaixo, escolha o seu destino:'.format(nome))

#Lista para ser mostrada na tela
print(' 0 - Juquitiba-SP\n 1 - Dirce Reis - SP\n 2 - Trabiju - SP\n 3 - Dolcinopolis - SP\n 4 - Sagres - SP\n 5 - Zacarias - SP\n 6 - Taquaral - SP')

#lista para busca interna
lista_de_cidades = ["Juquitiba-SP", "Dirce Reis - SP", "Trabiju - SP", "Dolcinopolis - SP", "Sagres - SP", "Zacarias - SP", "Taquaral - SP"]

#Entrada de dados para buscar por número da posição e escolher a cidade
opção = int(input('Qual é o numero da cidade que deseja? '))

#Busca por posição na lista e troca por nome da cidade
if opção == 0:
    print('Você escolheu', lista_de_cidades[0])
elif opção == 1:
    print('Você escolheu', lista_de_cidades[1])
elif opção == 2:
    print('Você escolheu', lista_de_cidades[2])
elif opção == 3:
    print('Você escolheu', lista_de_cidades[3])
elif opção == 4:
    print('Você escolheu', lista_de_cidades[4])
elif opção == 5:
    print('Você escolheu', lista_de_cidades[5])
elif opção == 6:
    print('Você escolheu', lista_de_cidades[6])
else:
    print('Essa opção é inválida')

#Retorno dizendo o nome da pessoa e a frutacidade que escolheu
print('Boa viagem, {}! Não esqueça de levar seus documentos pessoais para o embarque.'.format(nome))

print('-----------------------------------------------------------------------------------------------')
