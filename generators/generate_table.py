import os
import jinja2

loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates"))
templates = jinja2.Environment(loader=loader)
table_template = templates.get_template("table.html")


    # "": {
    #     "label": "",
    #     "dimension": ,
    #     "image": "",
    #     "weight_functions": "",
    #     "exterior_calc": "",
    #     "code": 'FiniteElement()',
    #     "code_alt": 'FiniteElement()',
    #     "color": "",
    #     "citation": ""
    # },

Pm = {
    "P1_interval": {
        "label": "\mathsf{P}_\mathsf{1}",
        "dimension": 2,
        "image": "P1_interval.png",
        "weight_functions": "\dof{2}{0}{0}{0}{1} = 2",
        "exterior_calc": "\Pm{1}{0}{1}",
        "code": 'FiniteElement("P", "interval", 1)',
        "code_alt": '',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_interval": {
        "label": "\mathsf{P}_\mathsf{2}",
        "dimension": 3,
        "image": "P2_interval.png",
        "weight_functions": "\dof{2}{1}{0}{0}{1} \pl \dof{1}{0}{1}{1}{1} = 3",
        "exterior_calc": "\Pm{2}{0}{1}",
        "code": 'FiniteElement("P", "interval", 2)',
        "code": 'FiniteElement()',
        "code_alt": '',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_interval": {
        "label": "\mathsf{P}_\mathsf{3}",
        "dimension": 4,
        "image": "P3_interval.png",
        "weight_functions": "\dof{2}{2}{0}{0}{1} \pl \dof{1}{1}{1}{1}{2} = 4",
        "exterior_calc": "\Pm{3}{0}{1}",
        "code": 'FiniteElement("P", "interval", 3)',
        "code_alt": 'FiniteElement()',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "dP0_interval": {
        "label": "\mathsf{dP}_\mathsf{0}",
        "dimension": 1,
        "image": "dP1_interval.png",
        "weight_functions": "\dof{1}{0}{0}{1}{1} = 1",
        "exterior_calc": "\Pm{1}{1}{1}",
        "code": 'FiniteElement("DG", "interval", "0")',
        "code_alt": 'FiniteElement()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP1_interval": {
        "label": "\mathsf{dP}_\mathsf{1}",
        "dimension": 2,
        "image": "dP1_interval.png",
        "weight_functions": "\dof{1}{1}{0}{1}{2} = 2",
        "exterior_calc": "\Pm{2}{1}{1}",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement("DG", "interval", "1")',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_interval": {
        "label": "\mathsf{dP}_\mathsf{2}",
        "dimension": 3,
        "image": "dP2_interval.png",
        "weight_functions": "\dof{1}{2}{0}{1}{3} = 3",
        "exterior_calc": "\Pm{3}{1}{1}",
        "code": 'FiniteElement("DG", "interval", "2")',
        "code_alt": 'FiniteElement()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "P2_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "P3_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "RT1_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "RT2_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "RT3_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "dP0_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "dP1_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "dP2_triangle": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "P1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "P2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "P3_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "N1e1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "N1e2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "N1e3_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "N1f1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "N1f2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "N1f3_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "dP0_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "dP1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
    "dP2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": 'FiniteElement()',
        "code_alt": 'FiniteElement()',
        "color": "",
        "citation": ""
    },
}

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
            [Pm["P1_tetrahedron"], Pm["N1e1_tetrahedron.png"], Pm["N1f1_tetrahedron.png"], Pm["dP0_tetrahedron"]],
            [Pm["P2_tetrahedron"], Pm["N1e2_tetrahedron.png"], Pm["N1f2_tetrahedron.png"], Pm["dP1_tetrahedron"]],
            [Pm["P3_tetrahedron"], Pm["N1e3_tetrahedron.png"], Pm["N1f3_tetrahedron.png"], Pm["dP2_tetrahedron"]],
        ]
    ]
]}

generated = table_template.render(table_data)
print generated
