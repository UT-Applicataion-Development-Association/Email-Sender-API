from flask import Blueprint

from server.controllers import user

userRoutes = Blueprint("userRoutes", __name__)


@userRoutes.route("/", methods=["GET"])
def handler():
    return user.getName()
