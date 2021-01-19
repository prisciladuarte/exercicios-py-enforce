
print('-------------------------------------------------------------')

#Saudação inicial
print('Olá! Seja bem-vindo(a) a Biblioteca Nacional Machado de Assis')

#Perguntar nome
nome = input('Qual seu nome? ')

#Printar nome e dizer que vai mostrar os livros
print('Certo, {}! Agora escolha o número do livro que deseja emprestar:'.format(nome))

print('----------------------------------------------------------------')

#Mostrar opções de livros na tela
print(' 0 - Dom Casmurro - Machado de Assis,\n 1 - Dom Quixote - Miguel de Cervantes,\n 2 - Cem Anos de Solidão - Gabriel Garcia Marquez,\n 3 - Revolução dos Bichos -  George Orwell,\n 4 - Hamlet - William Shakespeare,\n 5 - Orgulho e Preconceito - Jane Austen,\n 6 - O Pequeno Principe - Antoine de Saint-Exupéry')

#Mostrar opção de livros
lista_de_livros = ["Dom Casmurro - Machado de Assis", "Dom Quixote - Miguel de Cervantes", 
"Cem Anos de Solidão - Gabriel Garcia Marquez", "Revolução dos bichos -  George Orweel",
 "Hamlet - William Shakspeare", "Orgulho e Preconceito - Jane Austen", "O pequeno Principe - Antoine de Saint-Exupéry"]

#Entrada de dados para buscar por número da posição e escolher o livro
opção = int(input('Qual é a sua opção? '))

#Busca por posição na lista e troca por titulo do livro
if opção == 0:
    print('Você escolheu o livro: ', lista_de_livros[0])
elif opção == 1:
    print('Você escolheu o livro: ', lista_de_livros[1])
elif opção == 2:
    print('Você escolheu o livro: ', lista_de_livros[2])
elif opção == 3:
    print('Você escolheu o livro: ', lista_de_livros[3])
elif opção == 4:
    print('Você escolheu o livro: ', lista_de_livros[4])
elif opção == 5:
    print('Você escolheu o livro: ', lista_de_livros[5])
elif opção == 6:
    print('Você escolheu o livro: ', lista_de_livros[6])
else:
    print('Essa opção é inválida')

#Retorno dizendo o nome da pessoa e o livro que escolheu
print('Boa leitura, {}! Não esqueça de devolver no prazo correto'.format(nome))

print('-------------------------------------------------------------')

