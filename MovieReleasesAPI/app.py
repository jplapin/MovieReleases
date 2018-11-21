from flask import Flask
from flask import jsonify
from imdb_scrape import scrape

app = Flask(__name__)


@app.route('/')
def index():
    # return jsonify(Movies=scrape())
    return jsonify(Dates=scrape())


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
