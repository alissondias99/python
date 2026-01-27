# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception): # cria uma mensagem de error personalizada
    ...
    
class OutroError(Exception): # cria uma mensagem de error personalizada
    ...
    
def levantar():
    exception_ = MeuError('Erros 1, 2 e 3 no sistema') 
    raise exception_

try:
    
    levantar()
except (MeuError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError('Erros 1, 2 e 3 no sistema')
    exception_.add_note('Nota do erro, facilita a manutenção')
    raise exception_ 