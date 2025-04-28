# Decoradores com parâmetros

def fabrica_de_decoradores(a=33, b='ç', c=False):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada (*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    return x+ y

decoradora = fabrica_de_decoradores() #decora a função multiplica e os parametros default são usados
multiplica = decoradora(lambda x, y: x*y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10,5)
print(dez_mais_cinco)
print(dez_vezes_cinco)