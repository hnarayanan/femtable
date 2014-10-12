# -*- coding: utf-8 -*-
from scipy.special import binom
from numpy import floor

feecsymb = 'S'
feeccodesymb = 'S'

def bnm(a, b):
    return int(binom(a, b))

def nface(d, n):
    # number of d-faces in the n-cube
    return 2**(n-d) * bnm(n, d)

def dimP(n, k, r):
    return bnm(r+n, r+k) * bnm(r+k, k)
    
def dimS(n, k, r):
    s = 0
    for d in range(k, min(n, int(floor(r/2.)) + k) + 1):
        s += 2**(n-d) * bnm(n, d) * bnm(r-d+2*k, d) * bnm(d, k)
    return s

def dim(n, k, r):
    return dimS(n, k, r)

def shape(n):
    if n == 1:
        return 'interval'
    elif n == 2:
        return 'quadrilateral'
    elif n == 3:
        return 'hexahedron'
    else:
        return 'ERROR'

def symb(n, k):
    if k == 0:
        return 'S'
    elif k == n:
        return 'dPc'
    elif k == 1 and n == 2:
        return 'BDMc'
    elif k == 1 and n == 3:
        return 'AAe'
    elif k == 2 and n == 3:
        return 'AAf'
    else:
        return 'ERROR'

def symbl(n, k):
    # return symbol in uppercase with "BDMC[E,F]" for "BDMC"
    sy = symb(n, k).upper()
    if k == 1 and n == 2:
        sy += '[E,F]'
    return sy

def deg(n, k, r):
    return r

def name(n, k, r):
    return symb(n, k) + str(deg(n, k, r)) + '_' + shape(n)

def label(n, k):
    if k == 0:
        return '\mathsf{S}'
    elif k == n:
        return '\mathsf{dP}'
    elif k == 1 and n == 2:
        return '\mathsf{BDMc}^{\mathsf{[e/f]}}'
    elif k == 1 and n == 3:
        return '\mathsf{AA}^{\mathsf{e}}'
    elif k == 2 and n == 3:
        return '\mathsf{AA}^{\mathsf{f}}'
    else:
        return 'ERROR'

def image(n, k, r):
    if k == 1 and n == 2:
        return 'placeholder-square.png'
    else:
        return symb(n, k) + str(deg(n, k, r)) + '_' + shape(n) + '.png'

def weight_functions(n, k, r):
    val = '\dof'
    val += '{' + str(nface(k, n)) + '}' + '{' + str(r) + '}{0}{' + str(k) + '}{' + str(dimP(k, 0, r)) + '}'
    tdim = nface(k, n) * dimP(k, 0, r)
    for d in range(k+1, n+1):
        if dimP(d, d-k, r-2*(d-k)) > 0:
            val += ' \pl \dof{' + str(nface(d, n)) + '}' + '{' + str(r-2*(d-k)) + '}{' + str(d-k) +  '}{' + str(d) + '}{' + str(dimP(d, d-k, r-2*(d-k))) + '}'
            tdim += nface(d, n) * dimP(d, d-k, r-2*(d-k))
        else:
            break
    val += ' = ' + str(tdim)
    if tdim != dim(n, k, r):
        print "DIMENSION ERROR {} {} {}".format(n, k, r)
    return val

def color(n, k):
    if k == 0:
        return 'green'
    elif k == n:
        return 'blue'
    elif k == 1 and n == 2:
        return 'orange'
    elif k == 1 and n == 3:
        return 'red'
    elif k == 2 and n == 3:
        return 'yellow'
    else:
        return 'ERROR'
    
def citation(n, k):
    if k == 0:
        return '""'
    elif k == n:
        return '""'
    elif k == 1 and n == 2:
        return '"Brezzi, Douglas, and Marini, Numer. Math. 47 (1985)"'
    elif k == 1 and n == 3:
        return '"Arnold and Awanou, Math. Comp. 83 (2014)"'
    elif k == 2 and n == 3:
        return '"Arnold and Awanou, Math. Comp. 83 (2014)"'
    else:
        return 'ERROR'
    
c = '# -*- coding: utf-8 -*-\n\nPm = {\n'

for n in range(1, 4):
    for k in range(0, n+1):
        for r in range(1, 4):
            c +=  '    "' + name(n, k, r) +  '": {\n' + \
                  '        "label": "' + label(n, k)  + '_{\mathsf{' + str(deg(n, k, r)) + '}}'+ '",\n' + \
                  '        "dimension": ' + str(dim(n, k, r)) + ',\n' + \
                  '        "image": "' + image(n, k, r) + '",\n' + \
                  '        "weight_functions": "' + weight_functions(n, k, r) + '",\n' + \
                  '        "exterior_calc": "\\' + feecsymb + '{' + str(r) + '}{' + str(k) + '}{' + str(n) + '}",\n' + \
                  '        "code": \'("' + symbl(n, k) + '", ' + shape(n) + ', ' + str(deg(n, k, r)) + ')\',\n' + \
                  '        "code_alt": \'("' + feeccodesymb + '", ' + shape(n) + ', ' + str(r) + ', ' + str(k) + ')\',\n' + \
                  '        "color": "' + color(n, k) + '",\n' + \
                  '        "citation": ' + citation(n, k)  + '\n    },\n'

print c[:-2] + '\n}'
