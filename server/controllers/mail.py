from server.services import mail as mailService

def getEmail(id):
    print("\033[93m" + "server/controllers/mail.py" + " => getEmail controller invoked to handle the request parsed" + "\033[0m")
    return "Mail-id "+id+" is invalid", 404

def sendEmail(recipient, text):
    print("\033[93m" + "server/controllers/mail.py" + " => sendEmail controller invoked to handle the request parsed" + "\033[0m")
    if recipient == None or text == None:
        print("\033[93m" + "server/controllers/mail.py" + " => sendEmail controller receives incompleted request body" + "\033[0m")
        return "Bad Request", 400
    
    mailService.send(recipient, text)
    return "OK", 200
    