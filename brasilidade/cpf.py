class CPF:
    def __init__(self, documento):
        documento = str(documento)
        if self.valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido")
        pass

    def valido(self, documento):
        return len(documento) == 11

    def format(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return f'{fatia_um}.{fatia_dois}.{fatia_tres}.{fatia_quatro}'

    def __str__(self):
        return self.format()
