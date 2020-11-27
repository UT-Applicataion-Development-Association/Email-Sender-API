from flask import abort
from server.services import mail


def send_email(mail_data):
    # ensure all fields exist
    if 'subject' not in mail_data:
        abort(400, description="Request body must contain subject.")
    if 'to' not in mail_data:
        abort(400, description="Request body must contain recipients.")
    if 'cc' not in mail_data:
        abort(400, description="Request body must contain ccs.")
    if 'bcc' not in mail_data:
        abort(400, description="Request body must contain bccs.")
    if 'body' not in mail_data:
        abort(400, description="Request body must contain body.")
    # if 'attachment' not in mail_data:
    #     abort(400, description="Request body must contain attachment list.")

    # parse email parameters
    confirmed_mail_data = {
        'subject': mail_data['subject'],
        'to': [mail_data['to'][0]['email']],
        'cc': mail_data['cc'],
        'bcc': mail_data['bcc'],
        'body': mail_data['body'],
        'attachment': []
    }
    # if mail_data['attachment']:
    #     confirmed_mail_data['attachment'].extend(mail_data['attachment'])

    # call send email
    mail.send(confirmed_mail_data)

