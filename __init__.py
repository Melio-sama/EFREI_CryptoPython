from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("hello.html")

@app.route('/encrypt/', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data.get('text')
    key = data.get('key')

    if not text or not key:
        return jsonify({"error": "Veuillez fournir 'text' et 'key'."}), 400

    try:
        f = Fernet(key.encode())
        token = f.encrypt(text.encode())
        return jsonify({"encrypted": token.decode()})
    except Exception as e:
        return jsonify({"error": f"Erreur de chiffrement : {str(e)}"}), 400

@app.route('/decrypt/', methods=['POST'])
def decrypt():
    data = request.get_json()
    token = data.get('text')
    key = data.get('key')

    if not token or not key:
        return jsonify({"error": "Veuillez fournir 'text' et 'key'."}), 400

    try:
        f = Fernet(key.encode())
        decrypted = f.decrypt(token.encode()).decode()
        return jsonify({"decrypted": decrypted})
    except Exception as e:
        return jsonify({"error": f"Erreur de déchiffrement : {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
