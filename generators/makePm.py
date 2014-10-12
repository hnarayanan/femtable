# -*- coding: utf-8 -*-
from scipy.special import binom

feecsymb = 'Pm'
feeccodesymb = 'P-'

def bnm(a, b):
    return int(binom(a, b))

def nface(d, n):
    # number of d-faces in an n-simplex
    return bnm(n+1, d+1)

def dimPm(n, k, r):
    return bnm(r+n, r+k) * bnm(r+k-1, k)

def dimP(n, k, r):
    return bnm(r+n, r+k) * bnm(r+k, k)
    
def dim(n, k, r):
    return dimPm(n, k, r)

def shape(n):
    if n == 1:
        return 'interval'
    elif n == 2:
        return 'triangle'
    elif n == 3:
        return 'tetrahedron'
    else:
        return 'ERROR'

def symb(n, k):
    if k == 0:
        return 'P'
    elif k == n:
        return 'dP'
    elif k == 1 and n == 2:
        return 'RT'
    elif k == 1 and n == 3:
        return 'N1e'
    elif k == 2 and n == 3:
        return 'N1f'
    else:
        return 'ERROR'

def symbl(n, k):
    # return symbol in uppercase with "RT[E,F]" for "RT"
    sy = symb(n, k).upper()
    if k == 1 and n == 2:
        sy += '[E,F]'
    return sy

def deg(n, k, r):
    # P^-_r Lambda^n = dP_{r-1}
    if k == n:
        return r-1
    else:
        return r

def name(n, k, r):
    return symb(n, k) + str(deg(n, k, r)) + '_' + shape(n)

def label(n, k):
    if k == 0:
        return '\mathsf{P}'
    elif k == n:
        return '\mathsf{dP}'
    elif k == 1 and n == 2:
        return '\mathsf{RT}^{\mathsf{[e/f]}}'
    elif k == 1 and n == 3:
        return '\mathsf{N1}^{\mathsf{e}}'
    elif k == 2 and n == 3:
        return '\mathsf{N1}^{\mathsf{f}}'
    else:
        return 'ERROR'

def image(n, k, r):
    if k == 1 and n == 2:
        return 'placeholder-square.png'
    else:
        return symb(n, k) + str(deg(n, k, r)) + '_' + shape(n) + '.png'

def weight_functions(n, k, r):
    val = '\dof'
    val += '{' + str(nface(k, n)) + '}' + '{' + str(r-1) + '}{0}{' + str(k) + '}{' + str(dimP(k, 0, r-1)) + '}'
    tdim = nface(k, n) * dimP(k, 0, r-1)
    for d in range(k+1, n+1):
        if dimP(d, d-k, r+k-d-1) > 0:
            val += ' \pl \dof{' + str(nface(d, n)) + '}' + '{' + str(r+k-d-1) + '}{' + str(d-k) +  '}{' + str(d) + '}{' + str(dimP(d, d-k, r+k-d-1)) + '}'
            tdim += nface(d, n) * dimP(d, d-k, r+k-d-1)
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
        return '"Courant, Bull. Amer. Math. Soc. (1943)"'
    elif k == n:
        return '"Reed and Hill, Los Alamos Report LA-UR-73-479 (1973)"'
    elif k == 1 and n == 2:
        return '"Raviart and Thomas, Lecture Notes in Math. 606 (1977)"'
    elif k == 1 and n == 3:
        return 'u"Nédélec, Numer. Math. 35 (1980)"'
    elif k == 2 and n == 3:
        return 'u"Nédélec, Numer. Math. 35 (1980)"'
    else:
        return 'ERROR'
    
c = '# -*- coding: utf-8 -*-\n\nPm = {\n'

for n in range(1, 4):
    for k in range(0, n+1):
        for r in range(1, 4):
            c +=  '    "' + name(n, k, r) +  '": {\n' + \
                  '        "label": "' + label(n, k)  + '_{\mathsf{' + str(deg(n, k, r)) + '}}'+ '",\n' + \
                  '        "dimension": ' + str(dimPm(n, k, r)) + ',\n' + \
                  '        "image": "' + image(n, k, r) + '",\n' + \
                  '        "weight_functions": "' + weight_functions(n, k, r) + '",\n' + \
                  '        "exterior_calc": "\\' + feecsymb + '{' + str(r) + '}{' + str(k) + '}{' + str(n) + '}",\n' + \
                  '        "code": \'("' + symbl(n, k) + '", ' + shape(n) + ', ' + str(deg(n, k, r)) + ')\',\n' + \
                  '        "code_alt": \'("' + feeccodesymb + '", ' + shape(n) + ', ' + str(r) + ', ' + str(k) + ')\',\n' + \
                  '        "color": "' + color(n, k) + '",\n' + \
                  '        "citation": ' + citation(n, k)  + '\n    },\n'

print c[:-2] + '\n}'
