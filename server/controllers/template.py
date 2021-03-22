from server.services import template
from flask import abort, jsonify


def list_templates():
    return jsonify(template.list_all_templates())
