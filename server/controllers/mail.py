from flask import abort
from server.services import mail


def send_email(mail_data):
    # ensure all fields exist
    if 'to' not in mail_data:
        abort(400, description="Request body must contain recipients.")
    if 'cc' not in mail_data:
        abort(400, description="Request body must contain ccs.")
    if 'bcc' not in mail_data:
        abort(400, description="Request body must contain bccs.")
    if 'body' not in mail_data:
        abort(400, description="Request body must contain body.")
    # ensure types are correct

    # if len(mail_data['recipients']) == 0:
    #   abort(400, description="Recipients should be non-empty.")

    # parse email parameters
    confirmed_mail_data = {
        'to': mail_data['to'],
        'cc': mail_data['cc'],
        'bcc': mail_data['bcc'],
        'body': mail_data['body'],
        'attachment': ''
    }
    if mail_data['attachment']:
        confirmed_mail_data['attachment'] = mail_data['attachment']

    # call send email
    mail.send(confirmed_mail_data)

