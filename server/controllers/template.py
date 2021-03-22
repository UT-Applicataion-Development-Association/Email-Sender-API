from flask import jsonify

from server.services import template


def list_templates():
    return jsonify(template.list_all_templates())


def get_template(template_name):
    return jsonify(template.get_template(template_name))
