def cria_conta(numero, titular, saldo, limite):
    """
        Cria uma conta 

        :param numero: Número da conta
        :param titular: Nome do titular da conta
        :param saldo: Saldo da conta
        :param limite: Limite da conta

        :return: Retorna um dict com os dados da conta 
    """
    conta = {"numero": numero, "titular": titular,
             "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    """
        Deposita um valor na conta

        :param conta: Número da conta
        :param valor: Valor a ser depositado na conta
    """
    conta['saldo'] += valor


def saca(conta, valor):
    """
        Saca um valor da conta

        :param conta: Número da conta
        :param valor: Valor a ser sacado da conta
    """
    conta['saldo'] -= valor


def extrato(conta):
    """
        Função para printar o valor disponível na conta

        :param conta: Número da conta
    """
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))



conta = cria_conta('123-7', 'João', 500.0, 1000.0)
deposita(conta, 50.0)
extrato(conta)
#numero: '123-7'
#saldo: 550.0
saca(conta, 20.0)
extrato(conta)
#numero: '123-