elements = [
    {
        "id": "P1_tetrahedron",
        "color": "green",
        "dimension": 4,
        "symbol": "\mathrm{P}_1",
        "html_symbol": "P<sub>1</sub>",
        "weight_functions": "\dof{4}{0}{0}{0}{1} = 4",
        "exterior_calc": "\Pm{1}{0}{3}",
        "code": '("P", tetrahedron, 1)'
    },
    {
        "id": "P2_tetrahedron",
        "color": "green",
        "dimension": 10,
        "symbol": "\mathrm{P}_2",
        "html_symbol": "P<sub>2</sub>",
        "weight_functions": "\dof{4}{1}{0}{0}{1} \pl \dof{6}{0}{1}{1}{1} = 10",
        "exterior_calc": "\Pm{2}{0}{3}",
        "code": '("P", tetrahedron, 2)'
    },
    {
        "id": "P3_tetrahedron",
        "color": "green",
        "dimension": 20,
        "symbol": "\mathrm{P}_3",
        "html_symbol": "P<sub>3</sub>",
        "weight_functions": "\dof{4}{2}{0}{0}{1} \pl \dof{6}{1}{1}{1}{2} \pl \dof{4}{0}{2}{2}{1} = 20",
        "exterior_calc": "\Pm{3}{0}{3}",
        "code": '("P", tetrahedron, 3)'
    },
    # {
    #     "id": "",
    #     "color": "",
    #     "dimension": ,
    #     "symbol": "",
    #     "html_symbol": "",
    #     "weight_functions": "",
    #     "exterior_calc": "",
    #     "code": ''
    # },
]


for element in elements:
    print """
      <!-- %(id)s detail  -->
      <div class="modal fade" id="%(id)s" tabindex="-1" role="dialog">
        <div class="modal-dialog">
          <div class="modal-content %(color)s">
            <div class="modal-body">
              <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">&times;</span><span class="sr-only">Close</span></button>
              <div class="row">
                <div class="col-xs-10">
                  <img src="images/large/%(id)s.png" alt="%(id)s element" class="img-responsive">
                </div>
                <div class="col-xs-2">
                  <p class="text-left"><strong>%(dimension)d</strong></p>
                </div>
              </div>
              <div class="row">
                <div class="col-xs-6">
                  <p>$$%(symbol)s$$</p>
                </div>
                <div class="col-xs-6">
                  <p>$$%(exterior_calc)s$$</p>
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-xs-12">
                  <p>$$%(weight_functions)s$$</p>
                </div>
              </div>
              <hr>
              <div class="row">
                <div class="col-xs-12">
                  <p class="text-center"><code>%(code)s</code></p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>""" % element
