import uuid
from datetime import datetime
from raizen.database.conn import database

class Account:
    """
        This class is responsible for account management
    """
    def __init__(self):
        pass

    def create(self,  nome, email):
        conn = database()
        collection = conn['accounts']
        id = str(uuid.uuid4())

        document = {
            'id': id,
            'nome': nome,
            'email': email
        }

        result = collection.insert_one(document)

        print('Inserted document with ID:', result.inserted_id)

        return id
    
    def get_account(self, email):
        conn = database()
        collection = conn['accounts']
        cursor = collection.find({'email': email})
        cursor = list(cursor)
        return {'id': cursor[0]['id'], 'nome': cursor[0]['nome'], 'email': cursor[0]['email']}


class Weather:
    """
        This class is responsible for weather data
    """

    def __init__(self):
        pass

    def create(self, city, forecast, account_id) :
        conn = database()
        collection = conn['weather']
        document = {
            'city': city,
            'forecast': forecast,
            'date': datetime.now(),
            'account_id': account_id
        }
        result = collection.insert_one(document)
        print('Inserted document with ID:', result.inserted_id)

    def get_history(self, account_id):
        conn = database()
        collection = conn['weather']
        cursor = collection.find({'account_id': account_id})
        return list(cursor)

