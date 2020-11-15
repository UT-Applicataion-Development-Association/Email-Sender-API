from server.controllers import mail
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def handler():
    return mail.send_email(request.json)

