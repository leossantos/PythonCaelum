from historico import Historico

class Conta:
    
    def	__init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def	deposita(self, valor):
        self.historico.transacoes.append("depositou {}".format(valor))
        self.saldo += valor
   
    def	saca(self,	valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque	de {}".format(valor))
            return True

    def	extrato(self):
        print("Nome: {} {}".format(self.titular.nome, self.titular.sobrenome))
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def	transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True


