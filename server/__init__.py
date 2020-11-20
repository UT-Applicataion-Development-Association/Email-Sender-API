from flask import Flask
from flask_mail import Mail
from server.routes import user, mail

app = Flask(__name__)
email = Mail()

# app.register_blueprint(user.userRoutes, url_prefix="/user")
app.register_blueprint(mail.mailRoutes, url_prefix="/mail")


@app.route("/")
def handler():
    return "hello"


@app.route('/mail')
def manager():
    return "mail page"
