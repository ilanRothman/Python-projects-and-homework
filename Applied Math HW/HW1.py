import numpy as np
import matplotlib.pyplot as plt
print("question 1.a:")

A = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
X = np.array([[1], [2], [-2]])
B = np.array([[1, -1, 1], [-1, 0, 1], [3, 2, 1]])
Y = np.array([2, -1, 3])
C = np.zeros((3, 2), dtype=complex)
C[0][0], C[0][1], C[1][0], C[1][1], C[2][1] = 1, '-j', -1, 'j', '2j'

print("A*Yt = " , "\n", np.matmul(A,Y.transpose()))
print("X*A*Xt is not allowed")
print("y*B = ", np.matmul(Y, B))
print("y*A*x = ", np.matmul(np.matmul(Y, B), X))
print("y*x = ", np.matmul(Y, X))

print("question 1.b: ")

print("first way of sum of all numbers in A*B is: ", np.sum(np.matmul(A,B)))


print("second way of sum of all numbers in A*B is: ", (sum([sum(i) for i in np.matmul(A, B)])))


print("question 2: ")

def innerProd(vec1, vec2):
    if len(vec1) != len(vec2):
        return "vectors are different length"

    return np.sum((vec1 * vec2))


U = np.array([[2], [5], [3], [-1], [8]])
V = np.array([[1], [2], [-2], [1], [5]])
W = np.array([[2], [2], [-3], [1], [9]])


print("<u,2v> = ", innerProd(U,2*V))

print("<2v,u+5w> = ", innerProd(2*V, U+5*W))


print("question 3: ")
Ts = 1/10000
x = np.arange(0,1-Ts,Ts)
y1 = np.cos(2*np.pi*1*x)
plt.plot(x,y1)
y2 = np.cos(2*np.pi*2*x)
plt.plot(x,y1,'b',x,y2,'g')
plt.show()

print("inner product of y1 and y2:")
print("first way:")
print(y1@y2)
inner = 0
for i in range(len(y1)):
    inner += y1[i]*y2[i]
print("second way:")
print(inner)





