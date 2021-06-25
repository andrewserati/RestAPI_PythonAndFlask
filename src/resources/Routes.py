from src.services.MovieService import AllMovies, MoviePerId, Movie
from src.services.RootService import Root


def load_routes(api):
    # root
    api.add_resource(Root, '/')
    # movies
    api.add_resource(AllMovies, '/all_movies')
    api.add_resource(MoviePerId, '/movie/<ObjectId:id>')
    api.add_resource(Movie, '/create_movie')
