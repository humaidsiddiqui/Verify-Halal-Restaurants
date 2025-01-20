from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__, static_folder='static')

@app.route('/favicon')
def favicon():
    return send_from_directory('static','favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    