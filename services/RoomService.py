from flask_restful import Resource

class AllRooms(Resource):
    def get(self):
        return 'All Rooms retorned'