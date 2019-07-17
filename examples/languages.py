from flask import Flask, request, jsonify
app = Flask(__name__)


LANGUAGES = [
    {"name": "Javascript"},
    {"name": "Python"},
    {"name": "C++"},
    {"name": "PHP"}
]


@app.route("/languages", methods=["GET"])
def languages():
    return jsonify({"languages": LANGUAGES})


@app.route("/languages/<string:name>", methods=["GET"])
def language(name):
    language = [lang for lang in LANGUAGES if lang["name"] == name]
    if language:
        return jsonify({
            "language": language
        })
    return jsonify({"status": 404})


@app.route("/languages", methods=["POST"])
def create_language():
    new_language = {"name": request.json["name"]}
    LANGUAGES.append(new_language)
    return jsonify({"languages": LANGUAGES})


@app.route("/languages/<string:name>", methods=["PUT"])
def update_language(name):
    language = [lang for lang in LANGUAGES if lang["name"] == name]
    if language:
        language[0]["name"] = request.json["name"]
        return jsonify({"language": language[0]})
    return jsonify({"status": 404})


@app.route("/languages/<string:name>", methods=["DELETE"])
def delete_language(name):
    language = [lang for lang in LANGUAGES if lang["name"] == name]
    if language:
        LANGUAGES.remove(language[0])
        context = {"status": 204}
    else:
        context = {"status": 404}
    return jsonify(context)


# @app.route("")
if __name__ == "__main__":
    app.run(debug=True, port=8000)
