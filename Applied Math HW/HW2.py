import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def normip(v , p) :
    """
    function to compute the natural norm of an input vector.
    Inputs: v - a numpy array (n dim vector)
    Outputs: natural norm of v"""
    s_return = 0
    for i in v :
        s_return += np.power(np.abs(i), p)
    return np.power(s_return,(1/p))


print("task 1.a:")
v = np.array([1, -2j, 3, 1, 5])
print("norm for vector v is: ", normip(v, 2))


# print("---------------------------------------------------------------")
#
# print("task 1.b:")
# v = np.array([1, 5, 2, -2j, -1, 7])
# normV = normip(v, 2)
# print(v*(1/normV))
#
# print("---------------------------------------------------------------")
#
# print("task 1.c")
# v = np.array([0,7,-1j, 2, 7])
# u = np.array([1,3,-2j, -3, 5])
# print("the distance between v and u is: ", normip(v-u,2))
#
#
# print("---------------------------------------------------------------")

print("task 2.a: ")
def createX(fr , to, freq):
    fs = 44100
    Ts = 1 / fs
    t = np.arange(fr , to , Ts)
    x = np.cos(2 * np.pi * freq * t)
    return x


print("task 2.b: ")

def drawCoSo():
    for i in range(500, 20000, 500):
        x = createX(0, 1, i)
        t = np.arange(0, 1, 1/10000)
        sd.play(x , 10000)
        plt.plot(t[:100], x[:100])
        plt.grid(axis='both')
        stitle = 'cosine function with freq = ' + str(i)
        plt.title(stitle)
        plt.show()

#
# drawCoSo()

print("---------------------------------------------------------------")


print("task 2.c: ")

def crompty():
    j = 440
    while j < 20000 :
        x = createX(0 , 1 , j)
        t = np.arange(0 , 1 , 1 / 10000)
        sd.play(x , 10000)
        plt.plot(t[:100] , x[:100])
        plt.grid(axis='both')
        stitle = 'cosine function with freq = ' + str(j)
        plt.title(stitle)
        plt.show()
        j = j * 2 ** (1 / 12)



# crompty()


print("---------------------------------------------------------------")


print("task3.a: ")

X = np.zeros([8,8])
X[ 1, 1:3 ] = 1
X[ 1, 5:7 ] = 1
X[ 3, 3:5 ] = 1
X[ 5:7, 1::5 ] = 1
X[6,2:6] = 1
plt.imshow(X, cmap = 'gray')
plt.show()

X1 = np.zeros([8,8])
X1[ 1, 1:3 ] = 1
X1[ 1, 5:7 ] = 1
X1[ 3, 3:5 ] = 1
X1[ 5:7, 1::5 ] = 1
X1[6,2:6] = 1
for i in range(len(X1)):
    for j in range(len(X1[i])):
        if X1[i][j] == 1:
            X1[i][j] = 0
        else:
            X1[i][j] = 1

plt.grid(axis='both')
plt.imshow(X1, cmap = 'gray')
plt.show()

print("---------------------------------------------------------------")


print("task 3.b: ")

def checkSim(mat1, mat2):
    iner = sum(mat1.flatten()*mat2.flatten())
    normM1 = normip(mat1.flatten(),2)
    normM2 = normip(mat2.flatten(),2)
    p = iner/(normM1*normM2)

    return p


print(checkSim(X1,X1))

print("---------------------------------------------------------------")


print("task 3.c:")

L = 8
X = np.zeros([L,L])

X[1,1:3] = 1
X[1,5:7] = 1
X[3,3:5] = 1
X[6,2:6] = 1
plt.imshow(X, cmap="gray")
plt.show()

ipN = 0
Th = 0.7
j = 0
while ipN < Th:
    Xtest = np.zeros([L, L])
    Xtest[1:L-1, 1:L-1] = np.random.randint(0, 2, [L-2, L-2])
    ipN = checkSim(Xtest,X)
    plt.subplot(1, 2, 1)
    plt.imshow(Xtest,cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(X,cmap='gray')
    plt.show()
    j += 1

plt.show()
print("ACCESS GRANTED! after ", j, " attempts.")





