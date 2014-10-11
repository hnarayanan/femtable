import os
import jinja2

from element_families import Pm

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
templates = jinja2.Environment(loader=loader)
popup_template = templates.get_template("popups.html")

elements_list = {"elements": Pm.items()}

generated = popup_template.render(elements_list)
print generated
