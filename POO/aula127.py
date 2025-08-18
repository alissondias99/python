# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados

import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Alisson', 22)

# Gravando a string JSON em um arquivo
with open("aula127.json", "w") as arquivo:
    json.dump(p1.__dict__, arquivo,)
