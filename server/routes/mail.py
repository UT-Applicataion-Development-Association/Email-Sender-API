from flask import Blueprint, request
from server.controllers import mail

mailRoutes = Blueprint("mailRoutes", __name__)


@mailRoutes.route("/", methods=["POST"])
def handler():
    return mail.send_email(request.json)
