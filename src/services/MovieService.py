from bson.json_util import dumps
from flask import request
from flask_restful import Resource

from src.resources.Messages import exclude_success_message, post_success_message, nodatas_message, update_success_message

import json


class AllMovies(Resource):
    def get(self):
        from src.app import db
        movies = json.loads(dumps(list(db['movies'].find())))
        if movies is None:
            return nodatas_message
        return movies


class MoviePerId(Resource):
    def get(self, id):
        from src.app import db
        movie = json.loads(dumps(db['movies'].find_one({"_id": id})))
        if movie is None:
            return nodatas_message
        return movie

    def put(self, id):
        from src.app import db
        title = request.json['title']
        description = request.json['description']
        movie = db['movies'].update_one({"_id": id}, {"$set": {"title": title, "description": description}})
        print(movie.raw_result)
        if movie.raw_result['n'] == 0:
            return nodatas_message
        return update_success_message

    def delete(self, id):
        from src.app import db
        movie = db['movies'].delete_one({"_id": id})
        print(movie.raw_result)
        if movie.raw_result['n'] == 0:
            return nodatas_message
        return exclude_success_message


class Movie(Resource):
    def post(self):
        from src.app import db
        title = request.json['title']
        description = request.json['description']
        db.movies.insert({"title": title, "description": description})
        return post_success_message
