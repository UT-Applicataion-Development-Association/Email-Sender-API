# How to use this version

## Gmail set up

1. Allow less secure apps: ON. (https://myaccount.google.com/lesssecureapps)

2. Allow Display Unlock Captcha. (https://accounts.google.com/DisplayUnlockCaptcha)

3. Enable IMAP Access (https://mail.google.com/mail/#settings/fwdandpop)

## Testing

1. run flask app

2. configure Postman to send "POST" request to http://localhost:8000/mail/send end point

3. configure raw JSON input as:

{
    "subject": "EMAIL SUBJECT STRING",
    "recipient": "RECIPIENT EMAIL ADDR",
    "cc": ["CC EMAIL ADDR"],
    "bcc": ["BCC EMAIL ADDR"],
    "body": "EMAIL BODY STRING"
}



# Email-Sender-Server
Online Mailing Service (Server) for University of Toronto Application Development Association

## Setup & Installation
Please ensure your local environment has Python and Pipenv installed. Python 3.6 or higher version is required.
At the root level of project directory, run the following command
```
$ pipenv shell
$ pipenv install
```

## Quick Start
For development, flask can directly run the server and support hot-reload on changed code. Run the following command to start the server, then access APIs via localhost:8081
```
$ python app.py
```

## Documentation
Task assignments are saved in [Github Project Board](https://github.com/orgs/UT-Applicataion-Development-Association/projects/1)
Guide and tutorial are saved in [repository wiki](https://github.com/UT-Applicataion-Development-Association/Email-Sender-Server/wiki)

## Contributing
For more details, please refer to [UTADA’s contribution guideline](https://github.com/UT-Applicataion-Development-Association/Contribution-Guidelines).
