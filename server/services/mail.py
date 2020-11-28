from flask_mail import Message
import server


def send(email_data):
    msg = Message(subject=email_data['subject'],
                  sender='dinolii1220@gmail.com',
                  recipients=email_data['to'],
                  cc=email_data['cc'],
                  bcc=email_data['bcc'])
    msg.body = "From: \r\n dinolii1220@gmail.com" \
               + "Subject: %s\r\n" % email_data['subject'] \
               + "To: %s\r\n" % email_data['to'] \
               + "CC: %s\r\n" % ",".join(email_data['cc']) \
               + "\r\n" \
               + email_data['body']

    if email_data['attachment']:
        for item in email_data['attachment']:
            with server.app.open_resource(item) as fp:
                msg.attach(item, fp.read())
    # config = dict(DEBUG=True,
    #               MAIL_SERVER='smtp.gmail.com',
    #               MAIL_USERNAME='dinolii1220@gmail.com',
    #               MAIL_PASSWORD='jsqnxtglzlcfstyp')
    # if platform.system().upper() == 'WINDOWS':
    #     config['MAIL_PASSWORD'] = 'zcbxvyxocpagjxtw'
    # server.app.config.update(config)
    server.app.config.from_object('server.config.GmailConfig')
    server.email.init_app(server.app)
    server.email.send(msg)
