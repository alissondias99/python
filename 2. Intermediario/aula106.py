
# Ordem dos decoradores
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='1')
@parametros_decorador(nome='2')
@parametros_decorador(nome='3')
@parametros_decorador(nome='4')
@parametros_decorador(nome='5')

def soma(x, y):
    return x + y
#Quando a função soma é chamada, os decoradores são executados de cima para baixo.
#Cada decorador envolve a função decorada anterior, criando um efeito de "camadas".
dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)