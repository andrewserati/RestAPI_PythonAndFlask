import os

from dotenv import load_dotenv
from flask_pymongo import PyMongo

load_dotenv()


class DbConnection:
    def instanceMongoDb(app):
        app.config[
            "MONGO_URI"] = 'mongodb+srv://{user}:{password}@cluster0.smhsf.mongodb.net/{database}?retryWrites=true&w=majority'.format(
            user=os.getenv('MONGODB_USER'),
            password=os.getenv('MONGODB_PASSWORD'),
            database=os.getenv('MONGODB_DATABASE'),
        )
        mongodb_client = PyMongo(app, tls=True, tlsAllowInvalidCertificates=True)
        return mongodb_client.db
