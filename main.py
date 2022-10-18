from flask import Flask
from flask_restful import Api, Resource
import json
from db_connections import *

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        db = connect_db()
        cursor = db.cursor()
        query = "SELECT * FROM users"
        cursor.execute(query)
        all_users = cursor.fetchall()
        db.commit()
        cursor.close()
        db.close()
        return {"data": all_users}


api.add_resource(Users, "/api/users")
