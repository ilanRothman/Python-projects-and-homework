import random

import numpy as np
import matplotlib.pyplot as plt

#4.a
def num_integral(func , a , b , n , method="simpson") :
    x = np.linspace(a , b , n+1, dtype=complex)
    f = eval(func)
    h = (b - a) / n
    if method == "darboux" :
        return sum(h / 2 * (f[1:] + f[:-1]))
    if method == "trapez" :
        return h / 2 * (f[0] + sum(2 * f[1 :-1]) + f[-1])
    if method == "simpson" :
        return h / 3 * (f[0] + 4 * np.sum(f[1 : -1 : 2]) + 2 * np.sum(f[2 : -2 : 2]) + f[-1])


# 4.b
def getCn(func , a , b , n , N) :
    f = "{} * np.exp(-1j*{}*x*2*np.pi/(b-a))".format(str(func) , str(n))
    ret = (1 / (b - a)) * num_integral(f , a , b , N)
    return ret


def fourierEstComplex(m , N , func , xl , xr) :
    x = np.linspace(xl , xr , N)
    fourier_func = 0
    f = eval(func)
    for n in range(-m , m + 1) :
        fourier_func += getCn(func , xl , xr , n , N) * np.exp((2 * np.pi * 1j * n * x) / (xr - xl))
    plt.plot(x , f)
    plt.plot(x , fourier_func)
    plt.show()



#5
#getting neighbor matrix
def mat_neighbors_update(A):

    up = A[-1: , :]
    up = np.append(up , A[:-1,:] , axis=0)

    down = A[1:,:]
    down = np.append(down , A[:1,:] , axis=0)

    right = A[:,-1:]
    right = np.append(right,  A[:, :-1] , axis=1)

    left = A[:,1:]
    left = np.append(left,  A[:, :1] , axis=1)

    u_left = up[:,1:]
    u_left = np.append(u_left, up[:, :1], axis=1)

    u_right = up[:, -1:]
    u_right = np.append(u_right, up[:, :-1], axis=1)

    d_left = down[:, 1:]
    d_left = np.append(d_left, down[:, :1], axis=1)

    d_right = down[:, -1:]
    d_right = np.append(d_right, down[:, :-1], axis=1)

    return (up + down + left + right + u_left + u_right + d_left + d_right)



#update mat according to neigbors
def evolution(A,B, min , max):
    for i in range(len(A)):
        for j in range(len(A)):
            if B[i,j] == max:
                A[i,j] = 1
            elif B[i,j] > max or B[i,j] < min:
                A[i,j] = 0
    return A

#random choice of where to put 1's
def initiateMat(Live_mat,dens) :
    for i in range(dens):
        row = random.randrange(len(Live_mat[0]))
        col = random.randrange(len(Live_mat))
        if Live_mat[row][col] != 1:
            Live_mat[row][col] = 1
        else:
            dens+= 1
    return Live_mat

        

#5
def game_of_life(min = 2 , max = 3 , dens_0 = 10000):
    size = 256
    Live_mat = np.zeros((size,size))

    Live_mat = initiateMat(Live_mat,dens_0) # initiating the matrix
    Neighbors_mat = mat_neighbors_update(Live_mat) #getting first neighbor matrix
    dens = dens_0

    while(dens > 0 ):
        plt.clf()
        plt.imshow(Live_mat , cmap='hot')
        plt.colorbar()
        plt.show()
        plt.pause(0.01)
        Live_mat = evolution(Live_mat,Neighbors_mat , min, max)
        Neighbors_mat = mat_neighbors_update(Live_mat)
        dens = sum(sum(Live_mat))

    plt.show()


def main():
    # game_of_life()
    # print(fourierEstComplex(150 , 10000 , 'x**2' , -1 , 1))
    a = (np.arange(3)+1)*3
    b = np.array([1,0,5])
    c = np.concatenate(([a],[b]))
    print(np.average(c, axis=0))

main()