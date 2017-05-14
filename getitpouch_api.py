from flask import Flask,jsonify,request
import pymongo
from tool import glowpickAPI

import json

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

connection = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
db = connection.db

pouch = db.pouch

app = Flask(__name__)

@app.route('/')
def index():
    return 'Running!'


@app.route('/rank', methods=['POST', 'GET'])
def rank():
    print(request.form)
    categry_name = request.form.get('category')
    gp_api = glowpickAPI.glowpickAPI()
    r = gp_api.rank(category=categry_name)
    if not r:
        return 'bad category',404
    print(r)

    return jsonify( {'item':r} )


@app.route('/scan', methods=['POST'])
def scan():
    return ''


@app.route('/search', methods=['POST'])
def search():
    return ''


@app.route('/my_pouch/list', methods=['POST','GET'])
def my_list():
    items = []
    for dic in pouch.find():
        item={ky:dic[ky] for ky in ["name", "product_id", "status", "image_url", "brand_name", "d_day", "purchase_time"]}
        items.append(item)
    print(items)

    return jsonify({'item':items})


@app.route('/my_pouch/add_item', methods=['POST'])
def pouch_add():
    return ''


@app.route('/my_pouch/delete', methods=['POST'])
def pouch_del():
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11022)
