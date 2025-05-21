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
def hello_world():
    generated_key = Fernet.generate_key().decode()
    return render_template('hello.html', generated_key=generated_key)

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    # encode en base64 url-safe pour pouvoir passer en URL
    token_b64 = base64.urlsafe_b64encode(token).decode()
    return f"Valeur encryptée (base64) : {token_b64}"

@app.route('/decrypt/<string:valeur>/<string:key>')
def decryptage(valeur, key):
    try:
        fernet = Fernet(key.encode())
        # décoder base64 url-safe avant décryptage
        token_bytes = base64.urlsafe_b64decode(valeur)
        valeur_bytes = fernet.decrypt(token_bytes)
        return f"Valeur décryptée : {valeur_bytes.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
