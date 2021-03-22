import os
import server
import xlrd


def list_all_templates():
    ret = []
    templates = find_templates()
    for template in templates:
        if validate_template(template):
            ret.append({"template_name": template})
    return {"templates": ret}


def find_templates():
    TEMPLATE_DIRECTORY = server.app.config["TEMPLATE_DIR"]
    templates = []
    for filename in os.listdir(TEMPLATE_DIRECTORY):
        path = os.path.join(TEMPLATE_DIRECTORY, filename)
        if os.path.isfile(path):
            if filename.endswith(".txt"):
                templates.append(filename[:-4])
    return templates


def find_fill_ins():
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
    if template_name not in fill_ins:
        return False
    with open(os.path.join(TEMPLATE_DIRECTORY, template_name+".txt")) as f:
        contents = f.read()
        blank_count = contents.count("[]")

    try:
        workbook = xlrd.open_workbook(os.path.join(TEMPLATE_DIRECTORY, template_name+".xlsx"))
        contents = workbook.sheet_by_index(0).row(0)
        fill_count = len(contents)
    except (IndexError, xlrd.biffh.XLRDError):
        return False

    return blank_count == fill_count




