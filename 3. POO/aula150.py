# Context manager com função
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print("Error", e)
    finally:
        print("Fechando arquivo")
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    arquivo.writelines('Criando e Encrevendo no arquivo')
    print('WITH', arquivo)