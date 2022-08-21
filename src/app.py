from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html")

@app.route('/about/')
def about():
    if request.method == 'GET':
        return render_template('about.html')


if __name__ == "__main__":
    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )