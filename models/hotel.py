class HotelModel:
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