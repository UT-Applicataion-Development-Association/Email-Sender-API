from server.controllers import mail
from flask import request, Blueprint
from flask_cors import cross_origin

mailRoutes = Blueprint('mailRoutes', __name__)


@mailRoutes.route("/", methods=["POST"], strict_slashes=False)
@cross_origin()
def handler():
    mail.send_email(request.get_json())
    return "Successfully sent"


@mailRoutes.route("/attachmentUpload", methods=["POST"], strict_slashes=False)
@cross_origin()
def attachment_upload_handler():
    return mail.upload_attachment(request.get_json())


@mailRoutes.route("/attachmentList", methods=["GET"], strict_slashes=False)
@cross_origin()
def attachment_list_handler():
    return mail.list_attachments()


@mailRoutes.route("/attachmentDownload/<path>", methods=["GET"], strict_slashes=False)
@cross_origin()
def attachment_download_handler(path):
    return mail.download_attachment(path)
