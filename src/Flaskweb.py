import json

from flask import Flask, request, jsonify
import nltk
from TermProject import *
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/search", methods=["POST"])
@cross_origin()
def Searchwebsite():
    return jsonify(MultiThreadCrawler.searchwebsite(request.json['query']))


@app.route('/data', methods=['GET'])
def song_title():
    return jsonify(get_data())


if __name__ == '__main__':
    app.run()
