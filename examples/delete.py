from flask import Flask, request, jsonify
app = Flask(__name__)

LANGUAGES = [
    {"name": "Javascript"},
    {"name": "Python"},
    {"name": "C++"},
    {"name": "PHP"}
]


@app.route("/lang/<string:name>", methods=["DELETE"])
def delete_language(name):
    language = [lang for lang in LANGUAGES if lang["name"] == name][0]
    LANGUAGES.remove(language)

    return jsonify({"lanugages": LANGUAGES})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
