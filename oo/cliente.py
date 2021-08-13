class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.sobrenome.title()

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def cpf(self):
        return self.cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
