import os
import jinja2

from element_families.Pm import Pm
from element_families.P import P
from element_families.Qm import Qm
from element_families.S import S


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
    ],
    # P Family
    [
        # n = 1
        [
            [P["P1_interval"], P["dP1_interval"], None, None],
            [P["P2_interval"], P["dP2_interval"], None, None],
            [P["P3_interval"], P["dP3_interval"], None, None],

        ],
        # n = 2
        [
            [P["P1_triangle"], P["BDM1_triangle"], P["dP1_triangle"], None],
            [P["P2_triangle"], P["BDM2_triangle"], P["dP2_triangle"], None],
            [P["P3_triangle"], P["BDM3_triangle"], P["dP3_triangle"], None],
        ],
        # n = 3
        [
            [P["P1_tetrahedron"], P["N2e1_tetrahedron"], P["N2f1_tetrahedron"], P["dP1_tetrahedron"]],
            [P["P2_tetrahedron"], P["N2e2_tetrahedron"], P["N2f2_tetrahedron"], P["dP2_tetrahedron"]],
            [P["P3_tetrahedron"], P["N2e3_tetrahedron"], P["N2f3_tetrahedron"], P["dP3_tetrahedron"]],
        ]
    ],
    # Q- Family
    [
        # n = 1
        [
            [Qm["Q1_interval"], Qm["dQ0_interval"], None, None],
            [Qm["Q2_interval"], Qm["dQ1_interval"], None, None],
            [Qm["Q3_interval"], Qm["dQ2_interval"], None, None],

        ],
        # n = 2
        [
            [Qm["Q1_quadrilateral"], Qm["RTc1_quadrilateral"], Qm["dQ0_quadrilateral"], None],
            [Qm["Q2_quadrilateral"], Qm["RTc2_quadrilateral"], Qm["dQ1_quadrilateral"], None],
            [Qm["Q3_quadrilateral"], Qm["RTc3_quadrilateral"], Qm["dQ2_quadrilateral"], None],
        ],
        # n = 3
        [
            [Qm["Q1_hexahedron"], Qm["Nce1_hexahedron"], Qm["Ncf1_hexahedron"], Qm["dQ0_hexahedron"]],
            [Qm["Q2_hexahedron"], Qm["Nce2_hexahedron"], Qm["Ncf2_hexahedron"], Qm["dQ1_hexahedron"]],
            [Qm["Q3_hexahedron"], Qm["Nce3_hexahedron"], Qm["Ncf3_hexahedron"], Qm["dQ2_hexahedron"]],
        ]
    ],
    # S Family
    [
        # n = 1
        [
            [S["S1_interval"], S["dPc1_interval"], None, None],
            [S["S2_interval"], S["dPc2_interval"], None, None],
            [S["S3_interval"], S["dPc3_interval"], None, None],

        ],
        # n = 2
        [
            [S["S1_quadrilateral"], S["BDMc1_quadrilateral"], S["dPc1_quadrilateral"], None],
            [S["S2_quadrilateral"], S["BDMc2_quadrilateral"], S["dPc2_quadrilateral"], None],
            [S["S3_quadrilateral"], S["BDMc3_quadrilateral"], S["dPc3_quadrilateral"], None],
        ],
        # n = 3
        [
            [S["S1_hexahedron"], S["AAe1_hexahedron"], S["AAf1_hexahedron"], S["dPc1_hexahedron"]],
            [S["S2_hexahedron"], S["AAe2_hexahedron"], S["AAf2_hexahedron"], S["dPc2_hexahedron"]],
            [S["S3_hexahedron"], S["AAe3_hexahedron"], S["AAf3_hexahedron"], S["dPc3_hexahedron"]],
        ]
    ]
]}

generated = table_template.render(table_data)
print generated


# run with
# python generate_table.py > foo.html &&  sed  's/\^{\\mathsf{\[e\/f\]}}//g' foo.html > bar.html
# and paste bar.html into index.html
