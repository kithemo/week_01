from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

client = MongoClient('54.180.90.244', 27017, username="test", password="test")
db = client.dbspartaProject


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def show_books():
    books = list(db.books.find({},{'_id': False}))
    return jsonify({'all_books': books})


# @app.route('/api/like', methods=['POST'])
# def like_star():
#     name_receive = request.form['name_give']
#     target_star = db.mystar.find_one({'name': name_receive})
#     current_like = target_star['like']
#
#     new_like = current_like + 1
#
#     db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
#
#     return jsonify({'msg': '좋아요!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
