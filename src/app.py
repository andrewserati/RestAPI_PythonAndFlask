from flask import Flask
from flask_restful import Api

from resources.DbConnection import DbConnection
from resources.Routes import load_routes


app = Flask(__name__)
api = Api(app)
db = DbConnection.instanceMongoDb(app)
load_routes(api)


# if __name__ == '__main__':
#     app.run(debug=True)
