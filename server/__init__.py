from flask import Flask
from flask_mail import Mail
from server.routes import user, mail

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dinolii1220@gmail.com'
app.config['MAIL_PASSWORD'] = 'jsqnxtglzlcfstyp'

email = Mail(app)

# app.register_blueprint(user.userRoutes, url_prefix="/user")
app.register_blueprint(mail.mailRoutes, url_prefix="/mail")


@app.route("/")
def handler():
    return "hello"


@app.route('/mail')
def manager():
    return "mail page"


app.run(host="127.0.0.1", port=8081)
