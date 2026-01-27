# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'C:\\Users\\dias9\\Desktop\\python\\Intermediario\\criando_arquvio\\'
caminho_arquivo += 'arquivo.txt'

# with open(caminha_arquivo, 'x') as arquivo:
#     print('Arquivo criado e fechado')

with open(camincaminho_arquivoha_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n'))
    
    arquivo.seek(0,0)
    print(arquivo.read())

    print('Lendo linha a linha')
    arquivo.seek(0,0)
    print(arquivo.readline(), end='') # maneiras de remover os espaços extras
    print(arquivo.readline().strip()) # maneiras de remover os espaços extras
    print(arquivo.readline().strip())
    print((arquivo.readline()))# readlines extras não geram erro

import os
os.remove(caminho_arquivo) # ou unlink
# os.rename(caminho_arquivo, 'aula116-2.txt')