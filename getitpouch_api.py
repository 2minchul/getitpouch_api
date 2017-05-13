from flask import Flask
import pymongo

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

connection = pymongo.MongoClient("mongodb://%s:%d" % (MONGODB_HOST, MONGODB_PORT))
db = connection.db

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return 'Running!'


@app.route('/rank', methods=['POST'])
def rank():
    return ''


@app.route('/scan', methods=['POST'])
def scan():
    return ''


@app.route('/search', methods=['POST'])
def search():
    return ''


@app.route('/my_pouch/list', methods=['POST'])
def my_list():
    return ''


@app.route('/my_pouch/add_item', methods=['POST'])
def pouch_add():
    return ''


@app.route('/my_pouch/delete', methods=['POST'])
def pouch_del():
    return ''


if __name__ == '__main__':
    app.run()
