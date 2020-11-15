from flask import Flask, jsonify

from server.routes import user, mail

app = Flask(__name__)

# app.register_blueprint(user.userRoutes, url_prefix="/user")
# app.register_blueprint(mail.mailRoutes, url_prefix="/mail")


@app.route("/")
def handler():
    return "hello"


app.run(host="127.0.0.1", port=8081)
