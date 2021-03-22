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
    TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
    if not validate_template(template_name):
        abort(400, description="Template is invalid or does not exist!")
    """read template content"""
    with open(os.path.join(TEMPLATE_DIRECTORY, template_name + ".txt")) as f:
        contents = f.read()
    """read fill-ins"""
    try:
        workbook = xlrd.open_workbook(
            os.path.join(TEMPLATE_DIRECTORY, template_name + ".xlsx"))
        sheet = workbook.sheet_by_index(0)
        fillins = []
        for i in range(sheet.ncols):
            fillins.append(sheet.cell_value(0, i))
        return {"template_name": template_name, "content": contents,
                "fillin": fillins}
    except (IndexError, xlrd.biffh.XLRDError):
        abort(400, desciption="Failed to read fill-ins")


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
    TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
    fill_ins = find_fill_ins()
    """verify that the template has a corresponding fill-in"""
    if template_name not in fill_ins:
        return False
    """verify that fill-in file is valid and the counts of fill-ins = blanks"""
    with open(os.path.join(TEMPLATE_DIRECTORY, template_name + ".txt")) as f:
        contents = f.read()
        blank_count = contents.count("[]")
    """hide all errors from client since it's GET ALL request"""
    try:
        workbook = xlrd.open_workbook(
            os.path.join(TEMPLATE_DIRECTORY, template_name + ".xlsx"))
        contents = workbook.sheet_by_index(0).row(0)
        fill_count = len(contents)
    except (IndexError, xlrd.biffh.XLRDError):
        return False
    return blank_count == fill_count
