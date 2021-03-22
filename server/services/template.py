import os

import xlrd
from flask import abort

import server


def list_all_templates():
    """return all valid templates"""
    ret = []
    templates = find_templates()
    for template in templates:
        if validate_template(template):
            ret.append({"template_name": template})
    return {"templates": ret}


def get_template(template_name):
    if not validate_template(template_name):
        abort(400, description="Template is invalid or does not exist!")
    return {"template_name": template_name,
            "content": read_template(template_name),
            "fillin": read_fillin(template_name)}


def process_template_mail(template_name, fillins):
    if not validate_template(template_name):
        abort(400, description="Template is invalid or does not exist!")
    verified_fillins = []
    for fillin in fillins:
        if not validate_fillin(fillin, template_name):
            abort(400, description="Some fillins are invalid!")
        verified_fillins.append(list(fillin.values()))
    mail_bodies = []
    for fillin in verified_fillins:
        content = read_template(template_name)
        for val in fillin:
            content = content.replace("[]", val, 1)
        mail_bodies.append(content)
    return mail_bodies


def find_templates():
    """get all template file names"""
    TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
    templates = []
    for filename in os.listdir(TEMPLATE_DIRECTORY):
        path = os.path.join(TEMPLATE_DIRECTORY, filename)
        if os.path.isfile(path):
            if filename.endswith(".txt"):
                templates.append(filename[:-4])
    return templates


def find_fill_ins():
    """get all fill-in file names"""
    TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
    fill_ins = []
    for filename in os.listdir(TEMPLATE_DIRECTORY):
        path = os.path.join(TEMPLATE_DIRECTORY, filename)
        if os.path.isfile(path):
            if filename.endswith(".xlsx"):
                fill_ins.append(filename[:-5])
    return fill_ins


def validate_template(template_name):
    try:
        fill_ins = find_fill_ins()
        """verify that the template has a corresponding fill-in"""
        if template_name not in fill_ins:
            return False
        """verify that fill-in file is valid and the counts of fill-ins = blanks"""
        blank_count = read_template(template_name).count("[]")
        fill_count = len(read_fillin(template_name))
        return blank_count == fill_count
    except IOError:
        return False


def validate_fillin(fillin, template_name):
    try:
        model = read_fillin(template_name)
        actual = list(fillin.keys())
        return model == actual
    except IOError:
        return False


def read_template(template_name):
    try:
        TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
        with open(
                os.path.join(TEMPLATE_DIRECTORY, template_name + ".txt")) as f:
            contents = f.read()
        return contents
    except (IndexError, IOError):
        """hide all errors from client since it's GET ALL request"""
        raise IOError("Failed to read template")


def read_fillin(template_name):
    TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
    try:
        workbook = xlrd.open_workbook(
            os.path.join(TEMPLATE_DIRECTORY, template_name + ".xlsx"))
        sheet = workbook.sheet_by_index(0)
        fillins = []
        for i in range(sheet.ncols):
            fillins.append(sheet.cell_value(0, i))
        return fillins
    except (IndexError, xlrd.biffh.XLRDError):
        """hide all errors from client since it's GET ALL request"""
        raise IOError("Failed to read fill-in")
