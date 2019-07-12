from flask import Flask, jsonify, request
app = Flask(__name__)


LANGUAGES = [
    {"name": "Javascript"},
    {"name": "Python"},
    {"name": "C++"},
    {"name": "PHP"}
]


@app.route("/lang", methods=["POST"])
def createLanguage():
    language = {"name": request.json["name"]}
    LANGUAGES.append(language)

    return jsonify({"languages": LANGUAGES})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
