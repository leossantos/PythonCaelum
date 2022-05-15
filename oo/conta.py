from oo.historico import Historico


class Conta:
    identificador = 0
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_identificador']

    # Construtor
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._identificador = Conta.identificador
        Conta.identificador += 1

    def __str__(self):
        return f'<< Conta: {self._numero} Saldo: {self._saldo} >>'

    @staticmethod
    def codigo_banco():
        return '001'

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        if (limite < 0):
            print("limite não pode ser negativo")
        else:
            self._limite = limite

    @property
    def historico(self):
        return self._historico

    @property
    def id(self):
        return self._identificador

    def deposita(self, valor):
        self.historico.transacoes.append("depositou {}".format(valor))
        self.saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self._saldo + self._limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque	de {}".format(valor))
            return True

    def extrato(self):
        print("Nome: {} {}".format(self.titular.nome, self.titular.sobrenome))
        print("id: {}   numero: {} \nsaldo: {}".format(self.id, self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True
