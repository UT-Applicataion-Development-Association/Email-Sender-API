from flask import abort, jsonify
from server.services import mail, attachment


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

    parse_recipient = lambda recipient_list: [email_dict['email'] for email_dict in recipient_list]
    # parse email parameters
    confirmed_mail_data = {
        'subject': mail_data['subject'],
        'to': parse_recipient(mail_data['to']),
        'cc': parse_recipient(mail_data['cc']),
        'bcc': parse_recipient(mail_data['bcc']),
        'body': mail_data['body'],
        'attachment': []
    }
    # if mail_data['attachment']:
    #     confirmed_mail_data['attachment'].extend(mail_data['attachment'])

    # call send email
    mail.send(confirmed_mail_data)


def upload_attachment(attachment_data):
    if 'filename' not in attachment_data:
        abort(400, description="Request body must contain filename.")
    if "/" in attachment_data['filename']:
        abort(400, description="No sub-directories are allowed..")
    if 'content' not in attachment_data:
        abort(400, description="Request body must contain content.")
    if attachment_data["filename"] in attachment.list_files():
        abort(400, description="Duplicated Filename")
    return attachment.upload(attachment_data)


