#Atributos de classe

class Pessoa:
    #attr = 'Valor'
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        return Pessoa.ano_atual - self.idade
        
p1 = Pessoa('Alisson', 22)

#Pessoa.ano_atual = 1 como ano_atual é um atributo de classe, esssa mudança afeta todos os objetos

print(p1.get_ano_nasc())