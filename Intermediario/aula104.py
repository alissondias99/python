# Decoradores são syntax sugar (açúcar sintático)

def criar_funcao(func): 
    def interna(*args, **kwargs): 
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@criar_funcao

def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')
    
inverte_string_check_param = criar_funcao(inverte_string)
invertida = inverte_string_check_param('123') #argumentos posicionais somente, um exemplo de argumentos nomeado seria (string='123')
print(f'Resultado {invertida}')