from flask import Flask
from flask_restful import Api

from services.MovieService import MoviePerId, AllMovies
from services.RootService import Root

main = Flask(__name__)
api = Api(main)

api.add_resource(Root, '/')
api.add_resource(MoviePerId, '/movie/<int:id>')
api.add_resource(AllMovies, '/all_movies')

if __name__ == '__main__':
    main.run(debug=True)
