#!/usr/bin/env python3

from flask import Flask
from flask import render_template
from flask import request
from flask import json
from predictor import Predictor

app = Flask(__name__)

yelpFunny = Predictor('static/net/yelp/model.json', 'static/net/yelp/network.h5')
normFunny = Predictor('static/net/norm/model.json', 'static/net/norm/network.h5')

@app.route("/")
def home():
    return render_template('howFunnyAreYou.html')

@app.route("/updateResult", methods=['POST'])
def updateResult():
    review      = request.form['review'];
    yelpPercent = yelpFunny.getFunny(review)
    normPercent = normFunny.getFunny(review)
    return json.dumps({'yelp' : yelpPercent, 'norm' : normPercent})

if __name__ == "__main__":
    app.run()
