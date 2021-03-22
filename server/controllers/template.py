from flask import jsonify, abort

from server.services import template, mail


def list_templates():
    return jsonify(template.list_all_templates())


def get_template(template_name):
    return jsonify(template.get_template(template_name))


def send_template_mail(mail_data):
    if 'subject' not in mail_data:
        abort(400, description="Request body must contain subject.")
    if 'sender' not in mail_data:
        abort(400, description="Request body must contain sender.")
    if 'to' not in mail_data or not isinstance(mail_data['to'], list):
        abort(400, description="Request body must contain an array of recipients")
    if 'template_name' not in mail_data:
        abort(400, description="Request body must contain template_name")
    if 'fillin' not in mail_data or not isinstance(mail_data['fillin'], list):
        abort(400, description="Request body must contain an array of fillins")
    if len(mail_data['to']) != len(mail_data['fillin']):
        abort(400, description="Recipients must be same length with fillins")

    bodies = template.process_template_mail(mail_data['template_name'], mail_data['fillin'])
    for i in range(len(mail_data['to'])):
        mail.send({
            "to": [mail_data['to'][i]],
            'subject': mail_data['subject'],
            'cc': [],
            'bcc': [],
            'body': bodies[i],
            'attachment': []
        })


