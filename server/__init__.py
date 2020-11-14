from flask import Flask

from server.routes import user, mail

app = Flask(__name__)

app.register_blueprint(user.userRoutes, url_prefix="/user")
app.register_blueprint(mail.mailRoutes, url_prefix="/mail")


app.run(host="127.0.0.1", port=8000)
