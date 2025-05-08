
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json
def todo(tarefa, lista=None):
    if (lista is None):
        lista = []
    lista.append(tarefa)
    return lista
#↑função para criar uma lista nova se necessario e insere o item na lista↑

tarefas = []
todo('Fazer café', tarefas)
todo('Caminhar', tarefas)
# print(tarefas)

def remove_e_move(origem, destino):
    if origem:
        destino.append(origem.pop())
#↑Remove o último elemento de 'origem' e insere em 'destino'↑

original = tarefas
removidos = []

remove_e_move(original, removidos)

# print(original)
# print(removidos)

remove_e_move(original, removidos)

# print(original)
# print(removidos)

def restore_last(origem, removidos):
    if removidos:
        origem.append(removidos.pop())
#↑funçaõ para devolver o item removido a lista original↑

restore_last(tarefas, removidos)
print(original)
print(removidos)

restore_last(tarefas, removidos)
print(original)
print(removidos)


with open('aula119.json', 'w', encoding='utf8') as arquivo:
    json.dump(tarefas, arquivo)