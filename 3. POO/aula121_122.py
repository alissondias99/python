# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Alisson'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome): # o self é uma convensão (pode ter qualquer outro nome) obrigatoria e sempre tem que ser o primeiro parâmetro dos métodos, é usado para refenciar o objeto em outros métodos ou funções
        self.nome = nome # = p1.nome = 'Alisson' se fosse definir manualmente
        self.sobrenome = sobrenome

p1 = Pessoa('Alisson', 'Dias')

#print(p1.nome, p1.sobrenome) 

class  Carro:
    def __init__(self, nome): #←Isso é um parametro
        #self.nome = 'Fusca' # isso é hard coded (escrito diretamente no código)
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} acelerou')

c1 = Carro('Fusca')

print(c1.nome)
c1.acelerar()