import os
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder

import json
from pprint import pprint

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, '../')

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def get(self, data_type, division):
        with open('data/division{DIV}_{TYPE}.json'.format(DIV = division, TYPE = data_type)) as data_file:    
            data = json.load(data_file)
        return data
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient
 
api.add_resource(Data, '/<string:data_type>/<string:division>')

if __name__ == '__main__':
     app.run()