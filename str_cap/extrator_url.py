import re


class ExtratorURL:
    def __init__(self, url):
        self.url = url
        self.url = self.sanitiza_url()
        self.valida_url()
        pass

    def sanitiza_url(self) -> str:
        if self.url:
            return self.url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A url não é valida")

    def get_url_base(self) -> str:
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self) -> str:
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        url_parametro = self.get_url_parametros()
        indice_parametro = url_parametro.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_parametro.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = url_parametro[indice_valor:]
        else:
            valor = url_parametro[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros:" + self.get_url_parametros() + "\n" + "URL base:" + self.get_url_base()

    def __eq__(self, obj):
        return self.url == obj.url


dolar = 5.5
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
print("Tamanho url", len(extrator_url))
print(extrator_url)
quantidade = extrator_url.get_valor_parametro("quantidade")
origem = extrator_url.get_valor_parametro("moedaOrigem")
destino = extrator_url.get_valor_parametro("moedaDestino")
print(quantidade)
print(origem)
print(destino)

if origem == 'real':
    resultado = float(quantidade)/dolar
else:
    resultado = float(quantidade)*dolar

print(resultado)
# extrator_url = ExtratorURL("    ")


