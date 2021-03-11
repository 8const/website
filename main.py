from flask import render_template

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def text():
    return render_template("1.html") 

@app.route('/lol')
def text2():
    return render_template("1.html") 

if __name__ == '__main__':
    app.run(debug = True)
