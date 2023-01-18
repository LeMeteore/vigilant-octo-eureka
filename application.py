import os
import random

# from flask import jsonify
from flask import Flask, request  # type:ignore

app = Flask(__name__)


@app.route("/patrick")  # si jamais l'utilisateur tape /patrick dans son url
def foobarbaz():
    return "Salut je m'appelle Pck"


@app.route("/nicolas")  # si jamais l'utilisateur tape /patrick dans son url
def foobarbaz2():
    return "Salut je m'appelle Nicolas"


@app.route("/")  # /
def index():  # fonction qui sera executée dès que je tape http://127.0.0.1/5000 dans mon navigateur
    return "Bienvenue sur la page d'accueil de Alioune"


@app.route("/generate")  # je définis l'url / une route /
def generate():  # et à cette route, j'associe une fonction
    # renvoyer un nombre entier aleatoire compris entre 10, et 50
    return str(random.randint(10, 50))


@app.route("/gen")
def generate2():
    # génération nombre aléatoire + transformation en chaine de car
    nombre = str(random.randint(1, 1000))

    # concaténation du nombre généré + phrase d'intro
    phrase = f"Le nombre généré est {nombre}"

    # affichage
    return phrase


@app.route("/profile/")  # je peux associer une route
@app.route("/profile/<username>")  # puis une autre route
def profile(username=None):  # à la même fonction
    if username is not None:
        return f"Hello {username.capitalize()}"
    else:
        return "Hello anonymous"


@app.route("/address/")
@app.route(
    "/address/<ad>"
)  # demander à l'utilisateur de saisir une adresse (optionnellement)
def address(ad=None):
    if ad is None:  # si je ne reçois pas d'adresse
        return "Vous habitez un endroit inconnu"
    elif ad == "dakar":  # si adresse est egale à dakar
        return "Veuillez vous rendre à DIT"
    else:  # pour toutes les autres adresses qui ne sont pas dakar
        return "Veuillez vous connecter à Zoom"


@app.route("/multiple/<foo>")
@app.route("/multiple/<foo>/<bar>/<baz>")
def multiple(foo, bar=None, baz=None):

    if foo is not None and bar is None and baz is None:
        return f"foo is {foo}, bar and baz are None"

    if foo == "foo":
        if bar == "bar":
            if baz == "baz":
                return "vous avez trouvé l'url secrete"
    else:
        return "Essayez encore"


@app.route("/register/")
@app.route("/register/<lang>")  # <-- register c'est le path
def register(lang=None):
    # la query string commence après le path
    # et à partir du point d'interrogation
    # recuperer une clé nommée username dans la query string

    username = request.args.get("username")
    # recuperer une clé nommée password dans la query string
    password = request.args.get("password")

    if password is None:
        return "Merci de fournir un mot de passe valide"

    if lang == "fr":
        return f"Vos identifiants sont {username} et {password} votre langage préféré est  {lang}"
    else:
        return f"Your credentials are {username} and {password} your prefered language is {lang}"


# Only GET params /example?user=foo&pass=bar
@app.route("/example", methods=["GET"])
def example():  # la fonction ne répondra qu'à une requête de type GET
    # print(request.args) # affiche moi la query string
    # print("le verbe http est: ", request.method) # affiche moi le verbe http

    # si le verbe http est GET
    if request.method == "GET":
        foo = request.args.get("user")
        bar = request.args.get("pass")
    return f"Your credentials are {foo} and {bar}"


# # Only GET params /register?user=foo&pass=bar
# @app.route('/example', methods=['POST'])
# def baz():
#     username = request.args.get('user')
#     password = request.args.get('pass')
#     return f"Your credentials are {username} and {password}"


@app.route("/current_user")
def get_current_user():
    return jsonify(username="username", email="email", uid="identification")


foo = """
<!DOCTYPE html>
<html>
<head>Ceci est une entête</head>
<body>

<h2>Formulaire DIT </h2>

<form action="/form" method=post>

  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value=""><br>

  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value=""><br><br>

<label for="msg">Message :</label>
<textarea id="msg" name="user_message"></textarea><br>
  <input type="submit" value="Envoyer"><br>
</form>

</body>
</html>
    """


@app.route("/form", methods=["GET", "POST"])
def form():

    # si le verbe http est POST
    if request.method == "POST":

        lastname = request.form["lname"]
        firstname = request.form["fname"]
        user_message = request.form["user_message"]
        # recuperer les informations du formulaire
        # enregistrer le tout dans une base de données
        # faire une prediction en fonction des données reçues
        # renvoyer le resultat de cette prediction
        print(request.form)

        return (
            f"Votre nom est {lastname}, {firstname}. Votre message est: {user_message}"
        )

    else:  # la requête n'est pas de type POST, alors, je vais afficher le formulaire
        return foo  # < --- renvoyer le formul


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
