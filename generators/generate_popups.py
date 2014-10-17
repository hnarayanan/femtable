import os
import jinja2

from element_families.Pm import Pm
from element_families.P import P
from element_families.Qm import Qm
from element_families.S import S


def equation_size(value):
    terms = value.count("\dof")
    if terms == 1:
        return "normal"
    elif terms == 2:
        return "small"
    elif terms == 3:
        return "tiny"
    elif terms == 4:
        return "really-tiny"

def is_code_breaking(value):
    if 'quadrilateral' in value and ('BDMC' in value or 'RTC' in value or 'DQ' in value or 'Q' in value):
        return True
    else:
        return False


loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
templates = jinja2.Environment(loader=loader)
templates.filters['equation_size'] = equation_size
templates.filters['is_code_breaking'] = is_code_breaking
popup_template = templates.get_template("popups.html")

elements_list = {"elements": Pm.items() + P.items() + Qm.items() + S.items()}

generated = popup_template.render(elements_list)
print generated
