from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/v1/cards")
def get_cards():
    with open('./data/cards.json', 'r') as file:
        data = json.load(file)
    return jsonify(data), 200

@app.route("/v1/favs")
def get_favs():
    with open('./data/favorites.json', 'r') as file:
        data = json.load(file)
    return jsonify(data), 200

@app.route("/v1/content")
def get_content():
    with open('./data/content.json', 'r') as file:
        data = json.load(file)
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True)