# Variaveis livres + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        #print(locals())
        return a
    return dentro

dentro = fora(10)
dentro2 = fora(20)

#print(dentro())
#print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final # define a variavel valor final como uma variavel não local, isso permite alterar o valor da variavel diretamente sem causar erros
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))