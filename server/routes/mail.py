from flask import Blueprint, request

from server.controllers import mail

mailRoutes = Blueprint("mailRoutes", __name__)


@mailRoutes.route("/send", methods=["POST"])
def post_handler():
    return mail.process_email(request.json)


@mailRoutes.route("/", methods=["GET"])
def get_handler():
    return "SEND EMAIL"
