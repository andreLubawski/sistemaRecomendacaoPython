avaliacoes = {'Ana':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Norbit': 2.5,
                   'Star Wars': 3.0},

              'Marcos':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 3.5,
                   'Star Trek': 1.5,
                   'Exterminador do Futuro': 5.0,
                   'Star Wars': 3.0,
                   'Norbit': 3.5},

              'Pedro':
                  {'Freddy x Jason': 2.5,
                   'O Ultimato Bourne': 3.0,
                   'Exterminador do Futuro': 3.5,
                   'Star Wars': 4.0},

              'Claudia':
                  {'O Ultimato Bourne': 3.5,
                   'Star Trek': 3.0,
                   'Star Wars': 4.5,
                   'Exterminador do Futuro': 4.0,
                   'Norbit': 2.5},

              'Adriano':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Trek': 2.0,
                   'Exterminador do Futuro': 3.0,
                   'Star Wars': 3.0,
                   'Norbit': 2.0},

              'Janaina':
                  {'Freddy x Jason': 3.0,
                   'O Ultimato Bourne': 4.0,
                   'Star Wars': 3.0,
                   'Exterminador do Futuro': 5.0,
                   'Norbit': 3.5},

              'Leonardo':
                  {'O Ultimato Bourne': 4.5,
                   'Norbit': 1.0,
                   'Exterminador do Futuro': 4.0}
              }
"""print(avaliacoes['Ana'])
print(avaliacoes['Ana']['Exterminador do Futuro'])"""

"distância euclidiana"

print(pow(3-3, 2))
print(pow(3.5-4, 2))

from math import sqrt
print(sqrt(pow(3-3, 2) + pow(3.5-4, 2)))
"""distância entre ana e e cláudia, considerando star trek no eixo x e exterminador no eixo y"""

"""funcao distância euclidiana"""
def euclidiana (user1, user2):
    similaridade = {}
    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]:
            similaridade[item] = 1
    if len(similaridade) == 0 : return 0

    soma = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item], 2)
                for item in avaliacoes[user1] if item in avaliacoes[user2]])
    return 1/(1+sqrt(soma))


"""######testanto a função##########"""
print(euclidiana('Leonardo', 'Ana'))
print(euclidiana('Marcos', 'Claudia'))
"""###############################"""

"""função que retorna a similaridade entre um usuário e todos os outros"""
def getSimilares(usuario):
    similaridade2 = [(euclidiana(usuario, outros), outros)
                     for outros in avaliacoes if outros != usuario]
    similaridade2.sort()
    """ordena em ordem crescente de similaridade"""
    similaridade2.reverse()
    return similaridade2

print(getSimilares('Ana'))