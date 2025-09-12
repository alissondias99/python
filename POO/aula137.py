# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    
    def __init__(self, nome) -> None:
        self.nome = nome
        self._motor = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor

class Motor:
    
    def __init__(self, nome):
        self.nome = nome

    def ligar(self):
        return f'{self.nome} está ligando'

class Fabricante:
    
    def __init__(self, nome) -> None:
        self.nome = nome
        self._carro = None

    @property
    def carro(self):
        return self._carro
    
    @carro.setter
    def carro(self, carro):
        self._carro = carro

c = Carro('Pálio')
m = Motor('V5')
f = Fabricante('Honda')

c.motor = m

print(f'O fabricante {f.nome} fez o carro {c.nome} com o motor {m.nome}')