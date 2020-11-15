import smtplib


def send_email(mail_data):
    gmail_user = 'YOUR GMAIL ADDR'
    gmail_password = 'YOUR GMAIL PASSWORD'

    to_addr = mail_data['recipient']
    cc = mail_data['cc']
    bcc = mail_data['bcc']
    from_addr = gmail_user
    message_subject = mail_data['subject']
    message_text = mail_data['body']
    message = "From: %s\r\n" % from_addr \
              + "To: %s\r\n" % to_addr \
              + "CC: %s\r\n" % ",".join(cc) \
              + "Subject: %s\r\n" % message_subject \
              + "\r\n" \
              + message_text
    to_addrs = [to_addr] + cc + bcc

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(from_addr, to_addrs, message)
        server.quit()
        return 'Email sent!'
    except smtplib.SMTPException:
        return 'Something went wrong...'
