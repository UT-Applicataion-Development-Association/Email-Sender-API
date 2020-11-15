from flask import abort
from server.services import send_email


def process_email(mail_data):
    if not mail_data:
        abort(400, description="Request body must be non-empty.")
    # ensure all fields exist
    if 'subject' not in mail_data:
        abort(400, description="Request body must contain subject.")
    if 'recipient' not in mail_data:
        abort(400, description="Request body must contain recipient.")
    if 'cc' not in mail_data:
        abort(400, description="Request body must contain ccs.")
    if 'bcc' not in mail_data:
        abort(400, description="Request body must contain bccs.")
    if 'body' not in mail_data:
        abort(400, description="Request body must contain body.")
    # parse email parameters
    confirmed_mail_data = {
        'subject': mail_data['subject'],
        'recipient': mail_data['recipient'],
        'cc': mail_data['cc'],
        'bcc': mail_data['bcc'],
        'body': mail_data['body']
    }
    # call send email
    return send_email.send_email(confirmed_mail_data)
