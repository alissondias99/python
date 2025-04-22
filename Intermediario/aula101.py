# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y

def mult(x, y):
    return x * y

def executa(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma5 = executa(soma, 5)
multiplica10 = executa(mult, 10)

print(soma5(5))
print(multiplica10(5))
