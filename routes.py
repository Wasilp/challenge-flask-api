from flask import Flask
from flask import Flask, request, render_template
import random
app = Flask(__name__)

@app.route('/') 
@app.route('/status') 
def home():
   return render_template("login.html",alive = 'alive!')


@app.route('/login', methods=['GET','POST']) 
def login():
    username = request.form['username']
    print(username)
    password = request.form['password']
    print(password)
    pwd_lenght = len(password)
    return render_template("home.html", username=username,password_lenght=pwd_lenght)



@app.route('/predict', methods=['GET','POST'])
@app.route('/predict/<seller_available>/<month>/<customer_visiting_website>', methods=['GET','POST']) 
def predict(seller_available:int,month:str,customer_visiting_website:int):  
    random_number = random.randint(2000,5000)
    return str(random_number)

if __name__ == '__main__':
   app.run(port=5000)