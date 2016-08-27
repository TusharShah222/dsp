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


#print Alpha* u



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
