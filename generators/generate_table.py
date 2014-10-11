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
    #     "code": '()',
    #     "code_alt": '()',
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
        "code": '("P", interval, 1)',
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
        "code": '("P", interval, 2)',
        "code": '()',
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
        "code": '("P", interval, 3)',
        "code_alt": '()',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "dP0_interval": {
        "label": "\mathsf{dP}_\mathsf{0}",
        "dimension": 1,
        "image": "dP1_interval.png",
        "weight_functions": "\dof{1}{0}{0}{1}{1} = 1",
        "exterior_calc": "\Pm{1}{1}{1}",
        "code": '("DG", interval, 0)',
        "code_alt": '()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP1_interval": {
        "label": "\mathsf{dP}_\mathsf{1}",
        "dimension": 2,
        "image": "dP1_interval.png",
        "weight_functions": "\dof{1}{1}{0}{1}{2} = 2",
        "exterior_calc": "\Pm{2}{1}{1}",
        "code": '()',
        "code_alt": '("DG", interval, 1)',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_interval": {
        "label": "\mathsf{dP}_\mathsf{2}",
        "dimension": 3,
        "image": "dP2_interval.png",
        "weight_functions": "\dof{1}{2}{0}{1}{3} = 3",
        "exterior_calc": "\Pm{3}{1}{1}",
        "code": '("DG", 2, interval)',
        "code_alt": '()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_triangle": {
        "label": "\mathsf{P}_\mathsf{1}",
        "dimension": 3,
        "image": "P1_triangle.png",
        "weight_functions": "\dof{3}{0}{0}{0}{1} = 3",
        "exterior_calc": "\Pm{1}{0}{2}",
        "code": '("P", triangle, 1)',
        "code_alt": '()',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P2_triangle": {
        "label": "\mathsf{P}_\mathsf{2}",
        "dimension": 6,
        "image": "P2_triangle.png",
        "weight_functions": "\dof{3}{1}{0}{0}{1} \pl \dof{3}{0}{1}{1}{1} = 6",
        "exterior_calc": "\Pm{2}{0}{2}",
        "code": '("P", triangle, 2)',
        "code_alt": '()',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "P3_triangle": {
        "label": "\mathsf{P}_\mathsf{3}",
        "dimension": 10,
        "image": "P3_triangle.png",
        "weight_functions": "\dof{3}{2}{0}{0}{1} \pl \dof{3}{1}{1}{1}{2} \pl \dof{1}{0}{2}{2}{1} = 10",
        "exterior_calc": "\Pm{3}{0}{2}",
        "code": '("P", triangle, 3)',
        "code_alt": '()',
        "color": "green",
        "citation": "Courant, Bull. Amer. Math. Soc. (1943)"
    },
    "RT1_triangle": {
        "label": "\mathsf{RT}_\mathsf{1}^{\mathsf{[e/f]}}",
        "dimension": 3,
        "image": "RT1_triangle.png",
        "weight_functions": "\dof{3}{0}{0}{1}{1} = 3",
        "exterior_calc": "\Pm{1}{1}{2}",
        "code": '("RT[e,f]", triangle, 1)',
        "code_alt": '()',
        "color": "orange",
        "citation": "Raviart and Thomas, Lecture Notes in Math. 606 (1977)"
    },
    "RT2_triangle": {
        "label": "\mathsf{RT}_\mathsf{2}^{\mathsf{[e/f]}}",
        "dimension": 8,
        "image": "RT2_triangle.png",
        "weight_functions": "\dof{3}{1}{0}{1}{2} \pl \dof{1}{0}{1}{2}{2} = 8",
        "exterior_calc": "\Pm{2}{1}{2}",
        "code": '("RT[e,f]", triangle, 2)',
        "code_alt": '()',
        "color": "orange",
        "citation": "Raviart and Thomas, Lecture Notes in Math. 606 (1977)"
    },
    "RT3_triangle": {
        "label": "\mathsf{RT}_\mathsf{3}^{\mathsf{[e/f]}}",
        "dimension": 15,
        "image": "RT3_triangle.png",
        "weight_functions": "$\dof{3}{2}{0}{1}{3} \pl \dof{1}{1}{1}{2}{6} = 15$",
        "exterior_calc": "\Pm{3}{1}{2}",
        "code": '("RT[e,f]", triangle, 3)',
        "code_alt": '()',
        "color": "orange",
        "citation": "Raviart and Thomas, Lecture Notes in Math. 606 (1977)"
    },
    "dP0_triangle": {
        "label": "\mathsf{dP}_\mathsf{0}",
        "dimension": 1,
        "image": "dP0_triangle.png",
        "weight_functions": "\dof{1}{0}{0}{2}{1} = 1",
        "exterior_calc": " \Pm{1}{2}{2}",
        "code": '("DG", triangle, 0)',
        "code_alt": '()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP1_triangle": {
        "label": "\mathsf{dP}_\mathsf{1}",
        "dimension": 3,
        "image": "dP1_triangle.png",
        "weight_functions": "\dof{1}{1}{0}{2}{3} = 3$",
        "exterior_calc": " \Pm{2}{2}{2}",
        "code": '("DG", triangle, 1)',
        "code_alt": '()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "dP2_triangle": {
        "label": "\mathsf{dP}_\mathsf{2}",
        "dimension": 6,
        "image": "dP2_triangle.png",
        "weight_functions": "\dof{1}{2}{0}{2}{6} = 6",
        "exterior_calc": " \Pm{3}{2}{2}",
        "code": '("DG", triangle, 2)',
        "code_alt": '()',
        "color": "blue",
        "citation": "Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"
    },
    "P1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "P2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "P3_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "N1e1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "N1e2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "N1e3_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "N1f1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "N1f2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "N1f3_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "dP0_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "dP1_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
        "color": "",
        "citation": ""
    },
    "dP2_tetrahedron": {
        "label": "\mathsf{}_\mathsf{}",
        "dimension": ,
        "image": ".png",
        "weight_functions": "",
        "exterior_calc": "",
        "code": '()',
        "code_alt": '()',
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
