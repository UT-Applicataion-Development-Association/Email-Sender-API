from server.controllers import mail
from flask import request, Blueprint

mailRoutes = Blueprint('mailRoutes', __name__)


@mailRoutes.route("/mail", methods=["POST"])
def handler():
    mail.send_email(request.get_json())
    return "Successfully sent"


