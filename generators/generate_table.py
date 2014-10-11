import os
import jinja2

from element_families import Pm

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
templates = jinja2.Environment(loader=loader)
table_template = templates.get_template("table.html")

table_data = { "table" : [
    # P- Family
    [
        # n = 1
        [
            [Pm["P1_interval"], Pm["dP0_interval"], None, None],
            [Pm["P2_interval"], Pm["dP1_interval"], None, None],
            [Pm["P3_interval"], Pm["dP2_interval"], None, None],

        ],
        # n = 2
        [
            [Pm["P1_triangle"], Pm["RT1_triangle"], Pm["dP0_triangle"], None],
            [Pm["P2_triangle"], Pm["RT2_triangle"], Pm["dP1_triangle"], None],
            [Pm["P3_triangle"], Pm["RT3_triangle"], Pm["dP2_triangle"], None],
        ],
        # n = 3
        [
            [Pm["P1_tetrahedron"], Pm["N1e1_tetrahedron"], Pm["N1f1_tetrahedron"], Pm["dP0_tetrahedron"]],
            [Pm["P2_tetrahedron"], Pm["N1e2_tetrahedron"], Pm["N1f2_tetrahedron"], Pm["dP1_tetrahedron"]],
            [Pm["P3_tetrahedron"], Pm["N1e3_tetrahedron"], Pm["N1f3_tetrahedron"], Pm["dP2_tetrahedron"]],
        ]
    ]
]}

generated = table_template.render(table_data)
print generated
