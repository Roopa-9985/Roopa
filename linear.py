import numpy as np
A=np.array(input("Enter the first matrix"))
B=np.array(input("Enter another secound matrix"))
C=np.add(A,B)
D=np.subtract(A,B)
E=np.divide(A,B)
F=np.multiply(A,B)
G=np.mod(A,B)
H=np.linalg.det(A)
I=np.linalg.det(B)
J=np.linalg.eig(A)
K=np.linalg.eig(B)
L=np.linalg.matrix_rank(A)
M=np.linalg.matrix_rank(B)
O=np.diagonal(A)
N=np.diagonal(B)
print "The addition of two matrices is",C
print "The subtraction of two matrices is",D
print "The division of two matrices is",E
print "The multiplication of two matrices is",F
print "The moduls of given matrices are",G
print "The deteriminats of given matrices are",H,",",I
print "The eigen matrices of given matrices are",J,",",K
print "The rank of the given matrices are",L,",",M
print "The diagonal elements of the given matrices are",O,",",N




