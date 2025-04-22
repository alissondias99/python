# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.

def criar_funcao(func): # função decoradora usada para decorar a função inverte_string, adcionando novas funcionalidades sem alterar seu código inicial
    def interna(*args, **kwargs): #args e kwargs são usados respectivamente para permitir entrada de dados posicionais e argumentos nomeados em quantidades indefinidas. O simbolo * em args é usado para agrupar os argumentos posicionais em tuplas, já ** em kwargs coloca os argumentos nomeados em dicionarios. Nesse caso kwargs poderia ser removidos totalmente pois não há argumentos nomeados no código
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')
    
inverte_string_check_param = criar_funcao(inverte_string)
invertida = inverte_string_check_param('123') #argumentos posicionais somente, um exemplo de argumentos nomeado seria (string='123')
print(f'Resultado {invertida}')