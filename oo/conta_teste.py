from conta import Conta
from cliente import Cliente

leo = Cliente('Leonardo', 'Santos', '46502686322')
joao = Cliente('João Lucas', 'Santos', '65465644654')

c1 = Conta('123-4', leo, 120.0, 1000.0)
c2 = Conta('123-5', joao, 200, 1000.0)

c1.extrato()
c2.extrato()

c1.deposita(500)
c2.deposita(200)

c1.extrato()
c2.extrato()

c1.saca(100)
c2.saca(1000)

c1.extrato()
c2.extrato()

c1.transfere_para(c2, 500)

c1.extrato()
c2.extrato()

c1.historico.imprime()
c2.historico.imprime()