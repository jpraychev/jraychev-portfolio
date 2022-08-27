from flask import Flask, render_template
from flask import request
import json

app = Flask(__name__)



@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html")

@app.route('/about/')
def about():
    if request.method == 'GET':
        with open('db/about.json') as f:
            about_data = json.load(f)
        return render_template('about.html', context=about_data)

@app.route('/services/')
def services():
    if request.method == 'GET':
        with open('db/services.json') as f:
            service_data = json.load(f)
        return render_template('services.html', context=service_data)

@app.route('/experiences/')
def experiences():
    if request.method == 'GET':
        with open('db/experiences.json') as f:
            experience_data = json.load(f)
        return render_template('experiences.html', context=experience_data)


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )