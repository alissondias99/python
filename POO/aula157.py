# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
# são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#podem ser iterados para retornar seus membros canônicos na ordem de definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum

#Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA']) não recomendado fazer dessa maneira, porque Direcoes fica definido como any

#Melhor fazer com classe, lembrando que não será um classe normal pois enum tem uma metaclass própria

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = enum.auto() # faz a numeração automaticamente
     
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
print(Direcoes(1).name, Direcoes.ESQUERDA.value)
    #↑ nome do objeto | ↑ numeração do objeto 

def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')
    else:
        print(f'Movendo para {direcao.name}')
        
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
#mover('lado')