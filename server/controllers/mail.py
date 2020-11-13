from flask import abort
from server.services import send_email


def send_email(mail_data):
    # ensure all fields exist
    if 'sender' not in mail_data:
        abort(400, description="Request body must contain subject.")
    if 'recipients' not in mail_data:
        abort(400, description="Request body must contain recipients.")
    if 'cc' not in mail_data:
        abort(400, description="Request body must contain ccs.")
    if 'bcc' not in mail_data:
        abort(400, description="Request body must contain bccs.")
    if 'body' not in mail_data:
        abort(400, description="Request body must contain body.")
    # ensure types are correct
    if len(mail_data['recipients']) == 0:
        abort(400, description="Recipients should be non-empty.")
    # parse email parameters
    confirmed_mail_data = {
        'subject': mail_data['subject'],
        'recipients': mail_data['recipients'],
        'cc': mail_data['cc'],
        'bcc': mail_data['bcc'],
        'body': mail_data['body']
    }
    # call send email
    send_email(confirmed_mail_data)

