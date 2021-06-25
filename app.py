from flask import Flask
from flask_restful import Api

from resources.DbConnection import DbConnection
from services.MovieService import AllMovies, MoviePerId, Movie
from services.RootService import Root


app = Flask(__name__)
api = Api(app)
db = DbConnection.instanceMongoDb(app)


# root
api.add_resource(Root, '/')
# movies
api.add_resource(AllMovies, '/all_movies')
api.add_resource(MoviePerId, '/movie/<ObjectId:id>')
api.add_resource(Movie, '/create_movie')


if __name__ == '__main__':
    app.run(debug=True)
