import numpy as np
import matplotlib.pyplot as plt
import time
import sounddevice as sd


def chirp(t,f0,u,fs):





fs = 10000
dur = 10
L = int(fs*dur)
tt = np.linspace(0,dur,L)
xxnoise = np.random.randn(L)
plt.subplot(2,2,1)
plt.plot(tt,xxnoise)
sd.play(xxnoise,fs)
plt.show(block= False)
plt.pause(1)

tsig = 0.5
Nsig  = int(tsig*fs)
ttsig = np.linspace(0,tsig,Nsig)
f0 = 1000
sig = np.cos(2*np.pi*f0*ttsig)

plt.subplot(2,2,2)
plt.plot(ttsig[:100],sig[:100])
sd.play(sig,fs)
plt.show(block= False)
plt.pause(1)

tstart = 7
nstart = int(tstart*fs)
xnsig = np.copy(xxnoise)

xnsig[nstart:nstart+Nsig] += 0.1*sig
plt.subplot(2,2,3)
plt.plot(tt,xnsig)
plt.show(block= False)
sd.play(xnsig[nstart:nstart+Nsig],fs)
plt.pause(10)

# new detect the signal
frame = Nsig #farame work
j=0
step = 100
iplen = int((L-frame)/step)
ip = np.zeros(iplen)

for j in range(iplen):
    xtest = xnsig[j*step:j*step+frame]


plt.show(block= False)
sd.play(xnsig[nstart:nstart+Nsig], fs)
plt.pause(1)

