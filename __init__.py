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
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>/<string:key>')
def encryptage(valeur, key):
    try:
        fernet = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = fernet.encrypt(valeur_bytes)
        token_b64 = base64.urlsafe_b64encode(token).decode()
        return f"Valeur encryptée (base64) : {token_b64}"
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt/<string:valeur>/<string:key>')
def decryptage(valeur, key):
    try:
        fernet = Fernet(key.encode())
        token_bytes = base64.urlsafe_b64decode(valeur)
        valeur_bytes = fernet.decrypt(token_bytes)
        return f"Valeur décryptée : {valeur_bytes.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
