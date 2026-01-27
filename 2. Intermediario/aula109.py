# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import *

def combinar(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Anna', 'Carlos', 'Julia']

camisas = [
    ['Branca', 'Preta'],
    ['p', 'm', 'g', 'gg'],
    ['Faminino', 'Masculino', 'Unisex'],
    ['Algodão', 'Dryfit', 'Poliéster ']
]

#combinar(combinations(pessoas, 3))
#combinar(permutations(pessoas, 3)) # faz todas as combinações possíveis (cria repetições)

combinar(product(*camisas))

