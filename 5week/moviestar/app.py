from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list')
def star_retreive():
    stars = list(db.mystar.find({}, {'_id': False}))
    return jsonify({
        'result': 'success',
        'stars': stars
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)