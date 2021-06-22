from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_root_page():
    return 'Hello World!'


@app.route('/all_movies', methods=['GET'])
def get_all_movies():
    return jsonify({'id': 1, 'title': 'The Avengers', 'description': 'A great movie!'})


@app.route('/movie/<int:id>', methods=['GET'])
def get_movie_per_id(id):
    return jsonify({'id': id, 'title': 'The Avengers', 'description': 'A great movie!'})


@app.route('/add_movie', methods=['POST'])
def post_movie():
    datas = request.data
    return datas


if __name__ == "__main__":
    app.run(debug=True)
