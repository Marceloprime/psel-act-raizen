import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

def database():
    """
        This class connect to MongoDB
    """
    uri = os.environ['MONGO_URI']

    client = MongoClient(uri, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client.raizen
    except Exception as e:
        print(e)
