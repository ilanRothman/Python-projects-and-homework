import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

print("question 1")


def Grahm(A) :
    eps = 1e-14
    [r , c] = A.shape
    Q = np.zeros([r , c])
    R = np.zeros([c , c])

    for j in range(c):
        V = A[:, j]
        for i in range(c):
            R[i][j] = np.inner(Q[:, i] , V)
            V = V - R[i][j] * Q[:, i]
        if np.all(np.abs(V) <= eps):
            A = np.delete(A, j, 1)
            R = np.delete(R, j, 1)
            R = np.delete(R, i, 0)
            Q = np.delete(Q, j, 1)
            c = c - 1

        else :
            R[j][j] = np.linalg.norm(V)
            Q[:,j] = V / R[j][j]

    return Q , R


A = np.array([[1 , 1 , 3] ,
              [2 , 1 , 4] ,
              [3 , -1 , 1] ,
              [2 , 1 , 4] ,
              [1 , 0 , 1]])

Q , R = Grahm(A)
print("Q: ", Q)
print("R: ", R)
print("a: ", A)



print("question 2: ")

#part A
def makeChirp(dur , fo , u , fs) :
    L = 1 / fs
    tt = np.arange(0 , dur , L)  # time line
    sigt = np.zeros(tt.shape)
    for i in range(tt.shape[0]) :
        t = tt[i]
        sigt[i] = np.cos(2 * np.pi * fo * t + 2 * np.pi * u * t ** 2)
    return sigt, tt

# part D
def find_chirp(chirp , noise_signal , fs) :
    arr = []
    for i in range(0, noise_signal.shape[0] - chirp.shape[0] , 100) :
        b = noise_signal[i :i + chirp.shape[0]]
        arr.append(np.inner(chirp , b) / (np.linalg.norm(chirp) * np.linalg.norm(b)))
    maxIndex = np.argmax(arr)
    location = maxIndex * 100
    time = location / fs
    return location, time

# part B
sigt , tt = makeChirp(0.7 , 1000 , 550 , 44100)
Fs = 44100
plt.subplot(1 , 2 , 1)
plt.title("first 200")
plt.plot(tt[:200] , sigt[:200])
plt.subplot(1 , 2 , 2)
plt.title("last 200")
plt.plot(tt[-200 :] , sigt[-200 :])
plt.show()
sd.play(sigt,Fs)

# part C:
xxnoise = np.random.randn(15 * Fs)
xxnoise[int(9*Fs):int(9*Fs)+int(0.7*Fs)]  =  xxnoise[int(9*Fs):int(9*Fs)+int(0.7*Fs)] +sigt[:-1]


#partE
chirp = np.load('C:\\Users\\iroth\\PycharmProjects\\shimushit\\chirp.npy')
xnsig = np.load('C:\\Users\\iroth\\PycharmProjects\\shimushit\\xnsig.npy')
print(find_chirp(chirp , xnsig , Fs))
