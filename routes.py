from flask import Flask
from flask import Flask, request, render_template
import random
import os

app = Flask(__name__)

"""[Home route]

Returns:
    [View]: [login page]
"""


@app.route("/")
@app.route("/status")
def home():
    return render_template("login.html", alive="alive!")


"""[login route]

Returns:
    [view]: [homepage for logged user]
"""


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form["username"]
    print(username)
    password = request.form["password"]
    print(password)
    pwd_lenght = len(password)
    return render_template("home.html", username=username, password_lenght=pwd_lenght)


"""[Predit route]

Returns:
    [str]: [random number between 2000 & 5000]
"""


@app.route("/predict", methods=["GET", "POST"])
@app.route(
    "/predict/<seller_available>/<month>/<customer_visiting_website>",
    methods=["GET", "POST"],
)
def predict(seller_available: int, month: str, customer_visiting_website: int):
    random_number = random.randint(2000, 5000)
    return str(random_number)


if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
