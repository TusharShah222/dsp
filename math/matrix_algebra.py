# Matrix Algebra

PLACE YOUR CODE HERE

1.  Matrix Dimensoins


mport numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")



Check all dimensions
print a.shape
print b.shape
print c.shape
print d.shape
print u.shape
print w.shape

"""
1.1. (2, 3)
1.2  (2, 2)
1.3  (3, 2)
1.4  (2, 3)
1.5  (1, 4)
1.6  (4, 1)
"""

2.1
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
tranza = a.getT()


#prints u + v
print u + v

"""
2.1  [[ 9  7 -4  9]]

"""

2.2)
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
tranza = a.getT()


#print u - v
print u - v

"""
[[ 3 -3 -2  1]]

"""


2.3)

import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)


#print alpha* u

"""
[[ 36  12 -18  30]]
"""

2.4)
diffeent dimensions..


2.5)
Determinates only exist for square matrices


print alpha * u


Matrix Operations

3.1)DOE different dimensions

3.2 (A - C^T)
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)

"""
[[-4 -7 -3]
 [ 3  6  4]]

"""



#print 
print a - c.getT()

3.3)

import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)

print c.getT() + 3 * d

"""

[[14  3  3]
 [ 2  7  9]]

"""


3.4)  BA

import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)


#print BA
print b * a 

"""
[[-1 -5 -1]
 [ 2  7  4]]

"""

3.5) BA^T

After transpose incompatable dimensions

3.6 ) Different Dimmensions

3.7)
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)


#CB
print c * b

"""
[[ 5 -6]
 [ 9 -8]
 [ 6 -6]]

"""

3.8)B^4
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)

print b * b * b * b
#print np.power(a, 4)

"""
[[   1   16   81]
 [  16 2401  256]]
"""


3.9)AA^T
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)

print a * a.getT()

"""
[[14 28]
 [28 69]]
"""

3.10)D^TD
import numpy as np

a = np.matrix("1 2 3; 2 7 4")
b = np.matrix("1 -1; 0 1")
c = np.matrix("5 -1; 9 1; 6 0")
d = np.matrix("3 -2 -1; 1 2 3")
u = np.matrix("6 2 -3 5")
v = np.matrix("3 5 -1 4")
w = np.matrix("1; 8; 0; 5")
alpha = int(6)



print d.getT() * d

""""
[[10 -4  0]
 [-4  8  8]
 [ 0  8 10]]

"""

