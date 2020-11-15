from flask_mail import Mail, Message
from server.routes import mail


email = Mail(mail.app)


def send(email_data):
    msg = Message(email_data['subject'],
                  sender='youhaili59@outlook.com',
                  # default sender?
                  recipients=[email_data['to'] + email_data['cc']
                              + email_data['bcc']])
    msg.body = "From: \r\n youhaili59@outlook.com"  \
               + "To: %s\r\n" % email_data['to'] \
               + "CC: %s\r\n" % ",".join(email_data['cc']) \
               + "Subject: %s\r\n" % email_data['subject'] \
               + "\r\n" \
               + email_data['body']
    with mail.app.open_resource(email_data['attachment']) as fp:
        msg.attach(email_data['attachment'], fp.read())

    email.send(msg)
