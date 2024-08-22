from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id' : 'alpha',
        'nome' : 'Alpha hotel',
        'estrelas' : 4.3,
        'valorDiaria' : 420.34,
        'cidade' : 'Rio de Janeiro'
    },
    {
        'hotel_id' : 'bravo',
        'nome' : 'Bravo hotel',
        'estrelas' : 4.4,
        'valorDiaria' : 380.90,
        'cidade' : 'Santa Catarina'
    },
    {
        'hotel_id' : 'charlie',
        'nome' : 'Charlie hotel',
        'estrelas' : 3.9,
        'valorDiaria' : 320.20,
        'cidade' : 'Santa Catarina'
    }
]


        

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    argumentos =  reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('valorDiaria')
    argumentos.add_argument('cidade')
    
    def findHotel(hotel_id):
        for hotel in hoteis :
            if hotel['hotel_id'] == hotel_id :
                return hotel
        return None
    
    def get(self, hotel_id):
        hotel = Hotel.findHotel(hotel_id)
        if hotel:
            return hotel
        return {'message' : 'Hotel not Found.'}, 404 #not found
    
    def post(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotelObjeto = HotelModel(hotel_id, **dados)
        novoHotel = hotelObjeto.json()
        # novoHotel = {'hotel_id' : hotel_id, **dados}
        hoteis.append(novoHotel)
        return novoHotel, 201 #created
    
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        hotelObjeto = HotelModel(hotel_id, **dados)
        novoHotel = hotelObjeto.json()
        # novoHotel = {'hotel_id': hotel_id, **dados}
        hotel = Hotel.findHotel(hotel_id)
        if hotel:
            hotel.update(novoHotel)
            return novoHotel, 200 #OK
        
        return {'message' : 'Hotel not Found to update.'}
    
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message' : 'Hotel Deleted.'}, 200 #OK



    