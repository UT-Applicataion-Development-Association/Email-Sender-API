import unittest
from server import app
from flask import json
from smtplib import SMTPAuthenticationError
from unittest.mock import patch


class FlaskTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_config = {"MAIL_USERNAME": 'test@gmail.com'}
        app.config.update(self.mock_config)
        self.tester = app.test_client(self)
        self.mock_data = {"sender": "test@gmail.com",
                          "to": ["test@me.com"],
                          "subject": "Test Email",
                          "recipients": ["test@gmail.com"],
                          "cc": [],
                          "bcc": [],
                          "body": "Test email",
                          "attachment": []}

    def tearDown(self) -> None:
        self.tester = app.test_client(self)

    def assertConfig(self, exp_config, server_config):
        for key, val in exp_config.items():
            self.assertEqual(val, server_config[key],
                             'Correct {} of server should be {} not {}'.format(key, val, server_config[key]))

    @patch('smtplib.SMTP')
    def test_invalid_credential(self, mock_smtp):
        """
        This test is used to test whether you handle the case when the user credential is invalid
        """
        mock_smtp.side_effect = SMTPAuthenticationError(535, 'Invalid Credential')
        response = self.tester.post('/mail', data=json.dumps(self.mock_data), content_type='application/json')
        self.assertEqual(401, response.status_code, 'You need to handle the case where the user credential is invalid')

    @patch('flask_mail.Mail.send')
    def test_correct_port(self, mock_send):
        """
        This test is used to test the correct configuration of smtp
        """
        mock_send.return_value = None
        response = self.tester.post('/mail', data=json.dumps(self.mock_data), content_type='application/json')
        self.assertTrue(response.status_code == 200,
                        'The correct status code for successfully sending a email should be 200')
        server_config = self.tester.application.config
        self.assertConfig({'MAIL_SERVER': 'smtp.gmail.com',
                           'USE_TLS': True,
                           'MAIL_PORT': 587}, server_config)

    @patch('flask_mail.Mail.send')
    def test_correct_port_2(self, mock_send):
        """
        This test is used to test the correct configuration of smtp
        """
        mock_send.return_value = None
        app.config.update({"MAIL_USERNAME": 'test@mail.utoronto.ca'})
        self.mock_data.update({"sender": 'test@mail.utoronto.ca'})
        response = self.tester.post('/mail', data=json.dumps(self.mock_data), content_type='application/json')
        self.assertTrue(response.status_code == 200,
                        'The correct status code for successfully sending a email should be 200')
        server_config = self.tester.application.config
        self.assertConfig({'MAIL_SERVER': 'smtp.office365.com',
                           'USE_TLS': True,
                           'MAIL_PORT': 587}, server_config)


if __name__ == '__main__':
    unittest.main()
