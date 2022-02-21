import json

from flask import Flask, request, jsonify
import nltk
from TermProject import *
from flask_cors import cross_origin

app = Flask(__name__)


@app.route("/search", methods=["POST"])
@cross_origin()
def Searchwebsite():
    return jsonify(searchwebsite(request.json['query']))


if __name__ == '__main__':
    app.run()
