
# API de Hotéis

Esta é uma API RESTful desenvolvida em Python utilizando o framework Flask-RESTful. A API permite realizar operações de CRUD (Create, Read, Update, Delete) para gerenciar uma lista de hotéis.

## Endpoints

### 1. Listar Todos os Hotéis
**Endpoint:** `/hoteis`  
**Método:** `GET`  
**Descrição:** Retorna uma lista com todos os hotéis cadastrados.

**Resposta:**
```json
{
    "hoteis": [
        {
            "hotel_id": "alpha",
            "nome": "Alpha hotel",
            "estrelas": 4.3,
            "valorDiaria": 420.34,
            "cidade": "Rio de Janeiro"
        },
        {
            "hotel_id": "bravo",
            "nome": "Bravo hotel",
            "estrelas": 4.4,
            "valorDiaria": 380.90,
            "cidade": "Santa Catarina"
        }
    ]
}
```

### 2. Buscar um Hotel Específico
**Endpoint:** `/hotel/<hotel_id>`  
**Método:** `GET`  
**Descrição:** Retorna os dados de um hotel específico baseado no `hotel_id`.

**Resposta de Sucesso:**
```json
{
    "hotel_id": "alpha",
    "nome": "Alpha hotel",
    "estrelas": 4.3,
    "valorDiaria": 420.34,
    "cidade": "Rio de Janeiro"
}
```

**Resposta de Erro:**
```json
{
    "message": "Hotel not Found."
}
```

### 3. Adicionar um Novo Hotel
**Endpoint:** `/hotel/<hotel_id>`  
**Método:** `POST`  
**Descrição:** Adiciona um novo hotel à lista.

**Body de Requisição:**
```json
{
    "nome": "Delta Hotel",
    "estrelas": 4.7,
    "valorDiaria": 450.50,
    "cidade": "São Paulo"
}
```

**Resposta:**
```json
{
    "hotel_id": "delta",
    "nome": "Delta Hotel",
    "estrelas": 4.7,
    "valorDiaria": 450.50,
    "cidade": "São Paulo"
}
```

### 4. Atualizar um Hotel Existente
**Endpoint:** `/hotel/<hotel_id>`  
**Método:** `PUT`  
**Descrição:** Atualiza os dados de um hotel existente.

**Body de Requisição:**
```json
{
    "nome": "Alpha Hotel Renovado",
    "estrelas": 4.5,
    "valorDiaria": 430.00,
    "cidade": "Rio de Janeiro"
}
```

**Resposta de Sucesso:**
```json
{
    "hotel_id": "alpha",
    "nome": "Alpha Hotel Renovado",
    "estrelas": 4.5,
    "valorDiaria": 430.00,
    "cidade": "Rio de Janeiro"
}
```

**Resposta de Erro:**
```json
{
    "message": "Hotel not Found to update."
}
```

### 5. Deletar um Hotel
**Endpoint:** `/hotel/<hotel_id>`  
**Método:** `DELETE`  
**Descrição:** Remove um hotel da lista.

**Resposta:**
```json
{
    "message": "Hotel Deleted."
}
```

## Como Rodar o Projeto

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/sua-api-hoteis.git
    ```

2. Entre no diretório do projeto:
    ```bash
    cd sua-api-hoteis
    ```

3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/Mac
    .\venv\Scripts\activate    # Windows
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Inicie o servidor:
    ```bash
    python app.py
    ```

6. Acesse a API via `http://127.0.0.1:5000/`

## Dependências

- Flask
- Flask-RESTful

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).
