from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template
import base64


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>/<string:key>')
def encrypt(valeur, key):
    try:
        f = Fernet(key.encode())
        token = f.encrypt(valeur.encode())
        token_base64 = base64.urlsafe_b64encode(token).decode()
        return f"Valeur encryptée : {token_base64}"
    except Exception as e:
        return f"Erreur d'encryptage : {str(e)}"

@app.route('/decrypt/<string:valeur>/<string:key>')
def decrypt(valeur, key):
    try:
        f = Fernet(key.encode())
        token = base64.urlsafe_b64decode(valeur)
        original = f.decrypt(token).decode()
        return f"Valeur décryptée : {original}"
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
