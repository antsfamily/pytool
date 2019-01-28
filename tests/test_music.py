import numpy as np
import pytool as pyt
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


Ts = 99
Ns = 1000
Fs = Ns / Ts

# generates signal data
t = np.linspace(0, Ts, Ns)
noise = np.random.randn(len(t))

print(t.shape, noise.shape)

x1 = np.sin(np.pi / 3 * t) + 2 * np.sin(np.pi / 4 * t) + noise
x2 = np.exp(1j * np.pi / 2 * t) + \
    2 * np.exp(1j * np.pi / 4 * t) + \
    np.exp(1j * np.pi / 3 * t) + noise


plt.figure()


# orignal signal
plt.subplot(221)
plt.plot(t, x1, '-r')
plt.xlabel('Time/s')
plt.ylabel('Amplitude')
plt.title('orignal signal x(t)')


# ------------FFT---------
y = np.fft.fft(x1)
ypsd = np.conjugate(y) * y
ypower = np.log10(ypsd)
f = np.linspace(0, Ns, Ns)
f = Fs / f
print(f.shape, f)

plt.subplot(222)
# plt.plot(f, ypsd)
plt.plot(f, ypower)
# plt.psd(x1, NFFT=Ns, Fs=Fs, window=mlab.window_none,
#         noverlap=75, pad_to=512, scale_by_freq=True)
plt.xlabel('Frequency/Hz')
plt.ylabel('Power/dB')
plt.title('FFT of signal x(t)')


# ------------MUSIC-------
plt.subplot(223)
# R = pyt.corrmtx(x1, 12, 'mod')

# Estimate the correlation matrix using the modified covariance method.
# pyt.pmusic(R, 3, 'whole')  # Uses the default NFFT of 256.

plt.subplot(224)
# pyt.pmusic(R, 4, 'whole')  # Use twice the signal space dimension


plt.show()
