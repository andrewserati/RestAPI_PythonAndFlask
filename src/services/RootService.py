from flask_restful import Resource

from src.resources.Messages import welcome_message


class Root(Resource):
    def get(self):
        return welcome_message
