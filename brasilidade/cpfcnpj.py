from validate_docbr import CPF
from validate_docbr import CNPJ


class DocCPF:
    def __init__(self, documento):
        if self.valido(documento):
            self.documento = documento
        else:
            raise ValueError("Documento Inválido")

    def valido(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def __str__(self):
        mask = CPF()
        return mask.mask(self.documento)


class DocCNPJ:
    def __init__(self, documento):
        if self.valido(documento):
            self.documento = documento
        else:
            raise ValueError("Documento Inválido")

    def valido(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def __str__(self):
        mask = CNPJ()
        return mask.mask(self.documento)


class Documento:
    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
