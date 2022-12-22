from datetime import  datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_ano = [
            'janeiro', 'fevereiro', 'março',
            'abril', 'maio', 'junho',
            'julho', 'agosto', 'setembro',
            'outubro', 'novembro', 'dezembro'
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_ano[mes_cadastro-1]

    def dia_semana(self):
        dias_semana = [
            'segunda', 'terça', 'quarta',
            'quinta', 'sexta', 'sábado', 'domingo'
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def format_data(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return self.format_data()
