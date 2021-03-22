from flask import request, Blueprint
from flask_cors import cross_origin
from server.controllers import template

templateRoutes = Blueprint('templateRoutes', __name__)


@templateRoutes.route("/", methods=["GET"], strict_slashes=False)
@cross_origin()
def template_list_handler():
    return template.list_templates()


