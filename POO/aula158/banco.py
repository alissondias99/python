import contas
import pessoas


class Banco():
    def __init__(
            self,
            # isso é tipagem, é util porque definindo o que o objeto vai receber, o código tem um desempenho melhor
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_cliente(self, cliente):  # verifica se o cliente tem conta no banco
        if cliente in self.clientes:
            return True
        return False

    def _checa_agencia(self, conta):  # verifica se a agencia pertence ao banco
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_conta(self, conta):  # verifica se a conta pertence ao banco
        if conta in self.contas:
            return True
        return False

    def autencar(self, cliente, conta):  # verifica se a conta pertence ao cliente
        return self._checa_agencia(conta) and self._checa_cliente(cliente) and self._checa_conta(conta)
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}), ({self.clientes!r}), ({self.contas!r})'
        return f'{class_name}{attrs}'
    
if __name__ == '__main__':
    
    import contas  
    
    c1 = pessoas.Cliente('Alisson', 22)
    cc1 = contas.Contacorrente(111, 222, 0, 0)
    c1.conta = cc1
    banco = Banco()
    banco.clientes.extend([c1])
    banco.contas.extend([cc1])
    banco.agencias.extend([111])
    print(banco.autencar(c1, cc1))