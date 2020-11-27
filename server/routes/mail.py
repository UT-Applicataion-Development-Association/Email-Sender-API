from server.controllers import mail
from flask import request, Blueprint
from flask_cors import cross_origin

mailRoutes = Blueprint('mailRoutes', __name__)


@mailRoutes.route("/", methods=["POST"], strict_slashes=False)
@cross_origin()
def handler():
    mail.send_email(request.get_json())
    return "Successfully sent"


@mailRoutes.after_app_request
def add_cors(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


