import requests
from busca_endereco import BuscaEndereco


cep = "01001000"
objeto_cep = BuscaEndereco(cep)

print(objeto_cep.acessa_via_cep())
