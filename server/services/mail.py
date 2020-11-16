from flask_mail import Message
import server


def send(email_data):
    msg = Message(sender='dinolii1220@gmail.com',
                  recipients= email_data['to'] + email_data['cc']
                              + email_data['bcc'])
    msg.body = "From: \r\n dinolii1220@gmail.com"  \
               + "To: %s\r\n" % email_data['to'] \
               + "CC: %s\r\n" % ",".join(email_data['cc']) \
               + "\r\n" \
               + email_data['body']
    if email_data['attachment'] != '':
        with server.app.open_resource(email_data['attachment']) as fp:
            msg.attach(email_data['attachment'], fp.read())

    server.email.send(msg)
