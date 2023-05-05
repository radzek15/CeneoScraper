from scraper import Scraper
from flask import Flask, render_template, request
from store import Store
import jsonpickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
