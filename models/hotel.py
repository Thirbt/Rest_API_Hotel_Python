from sql_alchemy import banco

class HotelModel(banco.Model):
    __tablename__ = 'hoteis'
    
    hotel_id = banco.Column(banco.String, primary_key = True)
    nome = banco.Column(banco.String(80))
    estrelas = banco.Column(banco.Float(precision = 1))
    valorDiaria = banco.Column(banco.Float(precision = 2))
    cidade = banco.Column(banco.String(40))
    
    def __init__(self, hotel_id, nome, estrelas, valorDiaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.valorDiaria = valorDiaria
        self.cidade = cidade
    
    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'valorDiaria': self.valorDiaria,
            'cidade': self.cidade
        }