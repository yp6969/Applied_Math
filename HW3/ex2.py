import numpy as np
import matplotlib.pyplot as plt
# import time
# import sounddevice as sd

'''
ex 1
ars: time , start friqunce , constant U , signal friqunce
'''
def chirp(t=0.5,f0=1000,u=500,fs=44100):
    tt = np.linspace(0,t,int(t*fs))
    sig = np.cos((2 * np.pi * f0 * tt) + (2 * np.pi * u * tt ** 2))
    return tt , sig




'''
ex 2
ars: time , start friqunce , constant U , signal friqunce
'''

def testSig(t=0.5,f0=1000,u=500,fs=44100):
    tt,sig = chirp(t,f0,u,fs) # create signal
    plt.subplot(1,2,1)
    plt.plot(tt[:200], sig[:200])
    plt.subplot(1,2,2)
    plt.plot(tt[:200] + tt[-200], sig[:200] + sig[-200])
    plt.show()




"""
ex 3
find the chirp
return the place of the chirp signal
"""

def create_noise(t=10,f0=1000,u=500,fs=44100):
    tt, sig = chirp()
    Nsig = int(fs * t)
    noise = np.random.randn(Nsig)
    t = np.linspace(0, t, Nsig)

    chirp_place = 8
    signal = int(chirp_place * fs)
    noise = np.copy(noise)


    noise[signal: signal + int(0.5 * fs)] += (0.3 * sig)
    return sig, noise


create_noise()
"""
ex 4
find the chirp
return the place of the chirp signal
"""
def search_chirp(noise, sig):
    return
