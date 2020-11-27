from os import environ, path
from dotenv import load_dotenv
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = environ.get('DEBUG').upper() == 'TRUE'
    MAIL_PORT = int(environ.get('MAIL_PORT'))
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS').upper() == 'TRUE'
    MAIL_USE_SSL = environ.get('MAIL_USE_SSL').upper() == 'TRUE'


class GmailConfig(object):
    MAIL_SERVER = environ.get('GMAIL_SERVER')
    MAIL_USERNAME = environ.get('GMAIL_USER')
    MAIL_PASSWORD = environ.get('GMAIL_PASSWORD')


