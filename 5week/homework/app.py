from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def order_create():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    db.candle.insert_one({
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    })

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
