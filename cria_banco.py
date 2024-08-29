import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

# Em python para qubrar um texto eu posso colocar um contra barra "\"
cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
    nome text, estrelas real, valorDiaria real, cidade text)"
    
cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha hotel', 4.3, 420.34, 'Rio de Janeiro')"
    
cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()
