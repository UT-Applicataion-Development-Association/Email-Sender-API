import os
import base64
import server
from flask import send_from_directory


def post_attachment(attachment_data):
    UPLOAD_FILE_DIRECTORY = server.app.config["UPLOAD_DIR"]

    if not os.path.exists(UPLOAD_FILE_DIRECTORY):
        os.makedirs(UPLOAD_FILE_DIRECTORY)

    myblob = base64.b64decode(attachment_data['content'])
    with open(os.path.join(UPLOAD_FILE_DIRECTORY, attachment_data['filename']), "wb") as fp:
        fp.write(myblob)

    return "File Uploaded Successfully", 201


def list_attachments():
    UPLOAD_FILE_DIRECTORY = server.app.config["UPLOAD_DIR"]
    files = []
    for filename in os.listdir(UPLOAD_FILE_DIRECTORY):
        path = os.path.join(UPLOAD_FILE_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def get_attachment(attachment_path):
    UPLOAD_FILE_DIRECTORY = server.app.config["UPLOAD_DIR"]
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir, UPLOAD_FILE_DIRECTORY), attachment_path, as_attachment=True)


def delete_attachment(attachment_path):
    UPLOAD_FILE_DIRECTORY = server.app.config["UPLOAD_DIR"]
    root_dir = os.getcwd()
    os.remove(os.path.join(root_dir, UPLOAD_FILE_DIRECTORY, attachment_path))




