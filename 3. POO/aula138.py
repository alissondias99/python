# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print(f'{self.__class__.__name__}: {self.nome} {self.sobrenome}')
        
class Cliente(Pessoa):
    ...
    
class Aluno (Pessoa):
    ...
    
p1 = Cliente('Luiz', 'Otavio')
p1.falar_nome_classe()
p2 = Aluno('Alisson', 'Dias')
p2.falar_nome_classe()
