# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod #define o quem vem a seguir como um método interno da classe    
    def metodo_de_classe(cls, nome): # recebe a propria classe como parametro
        #print(f'Hey {nome}')
        return cls(nome, 22)


p1 = Pessoa('João', 34)
print(p1.nome)

p2 = Pessoa.metodo_de_classe('Alisson') #não é mais necessario criar todos os atributos manualmente
print(p2.nome, p2.idade)