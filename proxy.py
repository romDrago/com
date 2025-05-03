from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/posts')
def proxy():
    service = request.args.get('service')
    creator_id = request.args.get('id')
    offset = request.args.get('o', '0')
    url = f"https://coomer.su/api/v1/{service}/user/{creator_id}?o={offset}"
    response = requests.get(url)
    return jsonify(response.json())

# 🔹 New route to fetch details of a single post
@app.route('/api/post_detail')
def post_detail():
    service = request.args.get('service')
    creator_id = request.args.get('id')
    post_id = request.args.get('post_id')
    url = f"https://coomer.su/api/v1/{service}/user/{creator_id}/post/{post_id}"
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)