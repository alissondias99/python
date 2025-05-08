#problemas com parâmetros mutáveis em funções

def add_client(nome, lista=None):
    if(lista is None):
        lista= []
    lista.append(nome)
    return lista

cliente1 = []
add_client('Maria', cliente1)
add_client('Clara', cliente1)

cliente2 = add_client('Anna')
add_client('Clara', cliente2)
add_client('João', cliente2)


print(f'Lista cliente1: {cliente1}')
print(f'Lista cliente2: {cliente2}')
