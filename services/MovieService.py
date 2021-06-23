from flask import request
from flask_restful import Resource

from resources.Messages import excluded_message
from models.MovieModel import list_movies

import json


class MoviePerId(Resource):
    def get(self, id):
        try:
            response = list_movies[id - 1]
        except IndexError:
            response = {"message": "There are no movie with id {}, sorry :/".format(id)}
        except Exception:
            response = {"message": "Unknown Error. Sooo bad...."}
        return response

    def put(self, id):
        datas = json.loads(request.data)
        list_movies[id] = datas

    def delete(self, id):
        list_movies.pop(id)
        return excluded_message


class AllMovies(Resource):
    def get(self):
        return list_movies
