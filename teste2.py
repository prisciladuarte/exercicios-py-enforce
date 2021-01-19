#Saudação innicial
#perguntar nome
#printar nome e dizer que vai mostrar os livros
#mostrar opçoes de livros ccom numeros de opções ********* menu de opções
#escolher numero do livro ********* busca por posição
#printar nome da pessoa e nome do livro escolhido ******** retorno

def busca(lista, elem)
    """Retorna o índice do elemento se ele estiver na lista ou None caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
        return i
    return None

lista_estranha = [8,"5", 32, 0, "python", 11]
elemento = 32

indice = busca(lista_estranha, elemento)

if indice is not None:
    print('O indice do elemento {} é {}'.format(elemento, indice))
else:
    print('O elemento {} não se encontra na lista'.format(elemento))