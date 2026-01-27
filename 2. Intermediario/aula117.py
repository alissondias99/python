import json
# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'r') as arquivo:
#     json.dump(
#         pessoa, arquivo,
#         ensure_ascii=False,
#         indent=2)
#↑cria o arquivo json com os dados do dicionario python↑

#↓carrega os dados dos arquivos json↓
with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])
