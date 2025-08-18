import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



with open('POO/aula127.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)

p1 = Pessoa(**pessoa) #passa os dados do dicionário depois de recuperar o arquivo json

print(p1.nome)