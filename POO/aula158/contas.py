import abc

class Conta(abc.ABC):

    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor_saque):
        ...

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.detalhes(f'Depósito de R${valor_deposito}')

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('---')
        
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}), ({self.conta!r}), ({self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor_saque):
        valor_pos_saque = self.saldo - valor_saque

        if valor_pos_saque >= 0: #lógica: se o valor_pos_saque for maior ou igual a 0 quer dizer que saldo da conta acabou
            self.saldo -= valor_saque
            self.detalhes(f'Saque de R${valor_saque}')
            return self.saldo

        print('Não foi possível realizar o saque')
        self.detalhes(f'Saque no valor de R${valor_saque} negado')


class Contacorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor_saque):
        valor_pos_saque = self.saldo - valor_saque
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo: #lógica: o valor_pos_saque não pode ser maior que o valor de limite_maximo, se for o limite foi atingido 
            self.saldo -= valor_saque
            self.detalhes(f'Saque de R${valor_saque}')
            return self.saldo

        print('Não foi possível realizar o saque')
        print('Seu limite é', -self.limite)
        self.detalhes(f'Saque no valor de R${valor_saque} negado')
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}), ({self.conta!r}), ({self.saldo!r}), ({self.saldo!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    #cp1 = ContaPoupanca(111, 222)
    #cp1.sacar(1)
    #cp1.depositar(100)
    #cp1.sacar(1)
    print('##')
    cc1 = Contacorrente(111, 222, 0 ,100)
    cc1.sacar(100)
    cc1.depositar(1)
    cc1.sacar(2) # informa que não foi possivel realizar o saque, o valor excede o limite_maximo (100)