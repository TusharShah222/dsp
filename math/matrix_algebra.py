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
