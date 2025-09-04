from flask import Flask, request, jsonify
from flask_cors import CORS
from passwordChecker import PasswordChecker

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def check_password():
    print("received POST /check-password")

    data = request.get_json(force=True)
    print("Raw data:", data)

    if not data or "password" not in data:
        return jsonify({"error": "Missing 'password' in request"}), 400

    password = data["password"]

    checker = PasswordChecker(password)
    score = checker.get_score()

    print("password:", password)
    print("score:", score)

    return jsonify({"score": score})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


