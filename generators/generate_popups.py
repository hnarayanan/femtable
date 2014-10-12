import os
import jinja2

from element_families.Pm import Pm
from element_families.P import P
from element_families.Qm import Qm
from element_families.S import S

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
templates = jinja2.Environment(loader=loader)
popup_template = templates.get_template("popups.html")

elements_list = {"elements": Pm.items() + P.items() + Qm.items() + S.items()}

generated = popup_template.render(elements_list)
print generated
