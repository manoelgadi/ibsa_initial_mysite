# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# HTTP

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def seach():
    q = request.args.get('q') 
    return "received query string={} <br> Because they wanted a framework that was lightweight, just like their morning coffee!".format(q)


if __name__ == '__main__':
    app.run()
