from flask import Blueprint, request
from flask_cors import cross_origin

from server.controllers import template

templateRoutes = Blueprint('templateRoutes', __name__)


@templateRoutes.route("/", methods=["GET"], strict_slashes=False)
@cross_origin()
def template_handler():
    templateName = request.args.get('templateName')
    if templateName:
        return template.get_template(templateName)
    else:
        return template.list_templates()


@templateRoutes.route("/mail", methods=["POST"], strict_slashes=False)
@cross_origin()
def mail_handler():
    template.send_template_mail(request.get_json())
    return "Successfully sent"
