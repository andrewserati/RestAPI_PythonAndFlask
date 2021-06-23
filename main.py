from flask import Flask, jsonify, request
import json

app = Flask(__name__)

list_movies = [
    {
        "id": 1,
        "title": "Star Wars: The Force Awakens",
        "actors": ["Mark Hammil", "Harrison Ford", "Carrie Fisher"],
        "description": "........."
    },
    {
        "id": 2,
        "title": "Avengers: Infinity War",
        "actors": ["Robert Downey Jr.", "Scarlett Johansson", "Chris Evans"],
        "description": "The best movie of UCM"
    }
]

excluded_message = {
    "message": "Movie excluded successfully!"
}


@app.route('/', methods=['GET'])
def get_root_page():
    return {"message": "Welcome to CinemaManager API. We're not the IDMb, but we're almost there ;)",
            "status": "This API is working!"
            }


@app.route('/all_movies', methods=['GET'])
def get_all_movies():
    return jsonify(list_movies)


@app.route('/movie/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def get_movie_per_id(id):

    if request.method == 'GET':
        try:
            response = list_movies[id-1]
        except IndexError:
            response = {"message": "There are no movie with id {}, sorry :/".format(id)}
        except Exception:
            response = {"message": "Unknown Error. Sooo bad...."}
        return jsonify(response)

    elif request.method == 'PUT':
        datas = json.loads(request.data)
        list_movies[id] = datas
        return jsonify(datas)
    elif request.method == 'DELETE':
        list_movies.pop(id)
        return jsonify(excluded_message)


@app.route('/add_movie', methods=['POST'])
def post_movie():
    datas = json.loads(request.data)
    list_movies.append(datas)
    return {"message": "Movie created successfully"}


if __name__ == "__main__":
    app.run(debug=True)
