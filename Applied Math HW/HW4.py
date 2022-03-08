import numpy as np
import  matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

"""question 5 part a"""
def fourierSythesis(func,N,m):
    """

    :param func: string representing the function to evaluate the fourier series of.
    :param N: the amount of samples to be taken from the x axis.
    :param m: the amount of sums to be added to the series
    :return: the partial sum in a numpy array.
    """

    x = np.linspace(-np.pi,np.pi, N)
    f = eval(func)
    a0 = interect(-np.pi, np.pi, func, N)
    Sm = np.zeros(x.size) + (1/np.pi)*a0/2
    for n in range(1,m):
        a_n = "{}*np.cos({}*x)".format(func, n)
        b_n = "{}*np.sin({}*x)".format(func ,n)                     
        f_an = (1/np.pi)*interect(-np.pi , np.pi , a_n , N)
        f_bn = (1/np.pi)*interect(-np.pi , np.pi , b_n , N)
        Sm += f_an *np.cos(n*x) + f_bn*np.sin(n*x)
        plt.figure(2)
        plt.title("{}  partial sum amount: {}".format(func,n))
        plt.plot(x, f)
        plt.plot(x, Sm)
        plt.show()

    return x,Sm

def interect(a, b, func, n):
    x = np.linspace(a,b,n)
    f = eval(func) #eval uses x for the func and the result is in the array.
    y = (b-a)/n *np.sum(f[:-1])
    return y


def interectComplex(a , b , func , n) :
    interval = (b - a) / n
    y = interval * np.sum(func[:-1],dtype=complex)
    return y

"""question 5 part d"""
def fourierComplex(func , N , m):
    x = np.linspace(-np.pi , np.pi , N,dtype= complex)
    f = eval(func)
    Sm = np.zeros(x.size,dtype="complex")
    for n in range(0, m+1) :
        f_cn = interectComplex(-np.pi ,np.pi ,f*np.exp(-1j*n*x), N)/(2* np.pi)
        f_mincn = interectComplex(-np.pi ,np.pi ,f*np.exp(1j*n*x), N)/(2* np.pi)
        Sm += f_cn* np.exp(1j*n*x) + (f_mincn * np.exp(-1j*n*x))
        plt.figure(2)
        plt.title("{}  partial sum amount: {}".format(func , n))
        plt.plot(x , f)
        plt.plot(x , Sm)
        plt.show()

    return x , Sm

"""question 5 part b"""

x1, sm1 = fourierSythesis("x",10000,20)
x2, sm2 = fourierSythesis("abs(x)",10000,30)
x1, sm1 = fourierComplex("x",10000,20)



"""question 5 part c:
we can see that abs(x) converges a lot quicker than x
"""






