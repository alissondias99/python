# Função decoradoras e decoradores de classe

def add_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

class MyReprMixin:
    
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

class Time(MyReprMixin): # ←Essa é a herança
    
    def __init__(self, nome):
        self.nome = nome
  
@add_repr         
class Planeta():# isso é composição
    
    def __init__(self, nome):
        self.nome = nome
            
brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil) #uma classe sem repr, retornaria que o objeto é uma classe e o seu local na memória
print(terra)