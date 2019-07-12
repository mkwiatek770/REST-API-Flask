from flask import Flask, jsonify, request
app = Flask(__name__)

LANGUAGES = [
    {"name": "Javascript"},
    {"name": "Python"},
    {"name": "C++"},
    {"name": "PHP"}
]


@app.route("/lang/<string:name>", methods=["PUT"])
def update_language(name):
    language = [lang for lang in LANGUAGES if lang["name"] == name][0]
    language["name"] = request.json["name"]

    return jsonify({"languages": LANGUAGES})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
