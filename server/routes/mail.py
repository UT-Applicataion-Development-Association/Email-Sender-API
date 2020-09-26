from flask import Blueprint, request

from server.controllers import mail as mailController

mailRoutes = Blueprint("mailRoutes", __name__)


print("\033[93m" + "server/routes/mail.py" + "Registering the handler for speicific route /mail" + "\033[0m")
@mailRoutes.route("", methods=["GET", "POST"])
def handler():
    if request.method == "GET":
        print("\033[93m" + "server/routes/mail.py" + "GET request received at /mail" + "\033[0m")
        id = request.args['id']
        return mailController.getEmail(id)
    elif request.method == "POST":
        print("\033[93m" + "server/routes/mail.py" + "POST request received at /mail" + "\033[0m")
        recipient = request.form.get("recipient", None)
        text = request.form.get("text", None)
        return mailController.sendEmail(recipient, text)
