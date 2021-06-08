from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbproject

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/memo', methods=['GET'])
def listing():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg':'GET 연결되었습니다!'})

# @app.route('/memo', methods=['POST'])
# def saving():
#     comment_receive = request.form['comment_give']
#     doc = {'comment': comment_receive}
#     db.project.insert_one(doc)
#
#     return jsonify({'msg':'코멘트가 저장되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)