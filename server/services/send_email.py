import smtplib


def send_email(email_data):
    toaddr = 'youhaili59@outlook.com'
    cc = ['youhai.li@mail.utoronto.ca']
    bcc = ['youhai.li@mail.utoronto.ca']
    fromaddr = 'youhaili59@outlook.com'
    message_subject = "test title"
    message_text = "test body"
    message = "From: %s\r\n" % fromaddr \
              + "To: %s\r\n" % toaddr \
              + "CC: %s\r\n" % ",".join(cc) \
              + "Subject: %s\r\n" % message_subject \
              + "\r\n" \
              + message_text

    toaddrs = [toaddr] + cc + bcc
    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()
