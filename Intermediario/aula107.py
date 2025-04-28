
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def unir_listas(lista_cidade):
    def decorador(func):
        def unir(*args, **kwargs):
            lista_estado = func(*args, **kwargs)
            return list(zip(lista_estado, lista_cidade)) #zip é uma função responsavel por criar pares de elementos com o mesmo indice em duas listas
        return unir
    return decorador

@unir_listas(['BA', 'SP', 'MG', 'RJ'])
def lista_cidade():
    return ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Tijuca']

res = lista_cidade()
print(res)