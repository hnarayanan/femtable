# Compute dofs for FEEC elements
# Anders Logg 2013-09-16

from operator import mul

print_latex = True

nCk = lambda n, k: int(round(reduce(mul, (float(n-i)/(i+1) for i in range(k)), 1)))

nmax = 4
qmax = 7

num_facets_s = {(1, 0): 2,
                (1, 1): 1,
                (2, 0): 3,
                (2, 1): 3,
                (2, 2): 1,
                (3, 0): 4,
                (3, 1): 6,
                (3, 2): 4,
                (3, 3): 1}


# P_r^- L^k
print "Space P_r^- L^k"
print "==============="
print
for n in range(1, nmax + 1):
    for i, k in enumerate(range(n + 1)):
        if n % 2 == 0:
            print "<tr>"
        else:
            print '<tr class="pure-table-odd">'
        if i == 0:
            print "<td>n = %d</td>" % n
        else:
            print "<td></td>"
        print "<td>k = %d</td>" % k
        for r in range(1, qmax + 1):
            dofs = []
            dim = nCk(r + n, r + k)*nCk(r + k - 1, k)
            print "<td>%d</td>" % dim
        print "</tr>"
    print


# # P_r L^k
# print "Space P_r L^k"
# print "============="
# print
# for n in range(1, nmax + 1):
#     print "n = %d" % n
#     print "=====\n"
#     for k in range(n + 1):
#         print "k = %d:" % k,
#         for r in range(1, qmax + 1):
#             dofs = []
#             dim = nCk(r + n, r + k)*nCk(r + k, k)
#             print dim,
#         print
#     print

# # Q_r^- L^k
# print "Space Q_r^- L^k"
# print "==============="
# print
# for n in range(1, nmax + 1):
#     print "n = %d" % n
#     print "=====\n"
#     for k in range(n + 1):
#         print "k = %d:" % k,
#         for r in range(1, qmax + 1):
#             dofs = []
#             latex = []
#             dim = nCk(n, k)*(r**k)*((r + 1)**(n - k))
#             print dim,
#         print
#     print

# # S_r L^k
# print "Space S_r L^k"
# print "============="
# print
# for n in range(1, nmax + 1):
#     print "n = %d" % n
#     print "=====\n"
#     for k in range(n + 1):
#         print "k = %d:" % k,
#         for r in range(1, qmax + 1):
#             dofs = []
#             latex = []
#             dim = sum([(2**(n - dd))*nCk(n, dd)*nCk(r - dd + 2*k, dd)*nCk(dd, k) \
#                            for dd in range(k, min(n, r/2 + k) + 1)])
#             print dim,
#         print
#     print
