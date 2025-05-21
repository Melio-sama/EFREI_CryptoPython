from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

@app.route('/decrypt/<string:valeur>/<string:key>')
def decryptage(valeur, key):
    try:
        fernet = Fernet(key.encode())
        valeur_bytes = fernet.decrypt(valeur.encode())
        return f"Valeur décryptée : {valeur_bytes.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
