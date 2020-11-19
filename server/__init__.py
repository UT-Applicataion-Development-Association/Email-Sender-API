from flask import Flask
from flask_mail import Mail
from server.routes import user, mail
import platform
app = Flask(__name__)
config = dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'dinolii1220@gmail.com',
    MAIL_PASSWORD = 'jsqnxtglzlcfstyp',
)
if platform.system().upper() == 'WINDOWS':
    config['MAIL_PASSWORD'] = 'zcbxvyxocpagjxtw'
app.config.update(config)


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
