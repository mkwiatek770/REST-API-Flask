# GET Requests

from flask import Flask, jsonify, request
app = Flask(__name__)


LANGUAGES = [
    {"name": "Javascript"},
    {"name": "Python"},
    {"name": "C++"},
    {"name": "PHP"}
]


@app.route("/", methods=["GET"])
def test_view():
    return jsonify({"message": "It works!"})


@app.route("/lang", methods=["GET"])
def languages_view():
    return jsonify({"languages": LANGUAGES})


@app.route("/lang/<string:name>", methods=["GET"])
def language_detail_view(name):
    language = [lang for lang in LANGUAGES if lang["name"] == name][0]
    return jsonify({"language": language})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
