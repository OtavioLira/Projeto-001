import os 

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.environ["MONGODB_URI"]

def get_database():
    try:
        client = MongoClient(
            MONGODB_URI,
            tls = True,
            tlsAllowInvalidCertificates = True
        )
        db = client.get_database("cid_database")
        print("Conectado ao MongoDB")
        return db
    except Exception as e:
        print(f"Error: {e}")