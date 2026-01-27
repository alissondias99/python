#sys.argv executa os arquivo com argumentos do sistema

import sys

argumentos = sys.argv # argumentos são qualquer texto que for passado junto do comando de executar o arquivo
qtd_argumentos = len(argumentos)

if qtd_argumentos <=1 :
    print('Você não passou argumentos')
else:
    print(argumentos)