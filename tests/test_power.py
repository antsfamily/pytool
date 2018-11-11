from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

fs = 10e3
N = 1024
amp = 2
freq = 100
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time) + 1j*amp*np.cos(1*np.pi*freq*time)
# x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

plt.figure()
plt.plot(x)
plt.title("signal")

# np.fft.fft
freqs = np.fft.fftfreq(time.size, 1/fs)
idx = np.argsort(freqs)
ps = np.abs(np.fft.fft(x))**2

print(np.sum(ps))

plt.figure()
plt.plot(freqs[idx], ps[idx])
plt.title('Power spectrum (np.fft.fft)')

# signal.welch
f, Pxx_spec = signal.welch(x, fs, 'flattop', 1024, scaling='spectrum')
plt.figure()
plt.semilogy(f, np.sqrt(Pxx_spec))
plt.xlabel('frequency [Hz]')
plt.ylabel('Linear spectrum [V RMS]')
plt.title('Power spectrum (scipy.signal.welch)')
plt.show()