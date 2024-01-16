import os
import logging
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

load_dotenv()

def database():
    """
        This class connect to MongoDB
    """
    uri = os.environ['MONGO_URI']
    client = MongoClient(uri, server_api=ServerApi('1'))
    logger.info("Database client:", client)

    try:
        logger.info("Connected to MongoDB")
        return client.raizen
    except Exception as e:
        print(e)
