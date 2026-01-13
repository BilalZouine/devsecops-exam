from flask import Flask, request
import hashlib
import subprocess

app = Flask(__name__)

#  Mot de passe en dur (Bandit: hardcoded_password)
ADMIN_PASSWORD = "123456"

#  Cryptographie faible (Bandit: weak_hash_md5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route("/login")
def login():
    #  Données sensibles via GET
    username = request.args.get("username")
    password = request.args.get("password")

    #  Authentification faible
    if username == "admin" and hash_password(password) == hash_password(ADMIN_PASSWORD):
        return "Logged in"

    return "Invalid credentials"

@app.route("/ping")
def ping():
    #  Entrée utilisateur non filtrée
    host = request.args.get("host")

    #  Injection de commande (Bandit: subprocess_shell)
    output = subprocess.check_output(
        "ping -c 1 " + host,
        shell=True
    )
    return output

@app.route("/hello")
def hello():
    #  XSS réfléchi (CodeQL)
    name = request.args.get("name")
    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    #  Debug activé en production
    app.run(debug=True)
