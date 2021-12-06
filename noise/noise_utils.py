import numpy as np
import soundfile as sf
import librosa
import random
import os
import numpy as np
from scipy import signal
from numpy.linalg import norm
import wave


# sum_s = np.sum(a ** 2)
# sum_n = np.sum(n_b ** 2)
# # 信噪比为-5dB时的权重
# x = np.sqrt(sum_s / (sum_n * pow(10, -0.5)))
def add_noise(clean, noise, snr):  # 带噪
    # if len(noise) > len(clean):
    #     noise = noise[:len(clean)]
    # else:
    #     times = len(clean) // len(noise)
    #     noise = np.tile(noise, times)
    #     padding = [0] * (len(clean) - len(noise))
    #     noise = np.hstack([noise, padding])
    noise = noise / norm(noise) * norm(clean) / (10.0 ** (0.05 * snr))
    mix = clean + noise
    return mix


def add_echo(clean, beta=0.5, delay=0.2, sample_rate=8000):  # 回声
    mix = clean.copy()
    shift = int(delay * sample_rate)
    for i in range(shift, len(clean)):
        mix[i] = beta * clean[i] + (1 - beta) * clean[i - shift]
    return mix


def add_reverberation(clean, alpha=0.8, R=2000):  # 混响
    b = [0] * (R + 1)
    b[0], b[-1] = alpha, 1
    a = [0] * (R + 1)
    a[0], a[-1] = 1, 0.5
    mix = signal.filtfilt(b, a, clean)
    return mix


def add_howl(clean, K=0.2):  # 啸叫
    g = np.loadtxt("./data/path.txt")
    c = np.array([0, 0, 0, 0, 1]).T
    h = np.zeros(201)
    h[100] = 1

    xs1 = np.zeros(c.shape[0])
    xs2 = np.zeros(g.shape)
    xs3 = np.zeros(h.shape)

    mix = np.zeros(len(clean))
    temp = 0

    for i in range(len(clean)):
        xs1[1:] = xs1[: - 1]
        xs1[0] = clean[i] + temp
        mix[i] = K * np.dot(xs1.T, c)

        xs3[1:] = xs3[: - 1]
        xs3[0] = mix[i]
        mix[i] = np.dot(xs3.T, h)

        mix[i] = min(1, mix[i])
        mix[i] = max(-1, mix[i])

        xs2[1:] = xs2[: - 1]
        xs2[0] = mix[i]
        temp = np.dot(xs2.T, g)
    return mix


def get_info(wavpath):
    f = wave.open(wavpath, 'rb')
    params = f.getparams()  # 读取音频文件信息
    nchannels, sampwidth, framerate, nframes = params[:4]  # 声道数, 量化位数, 采样频率, 采样点数
    print("声道数=%d, 量化位数=%d, 采样频率=%d, 采样点数=%d" % (nchannels, sampwidth, framerate, nframes))


if __name__ == '__main__':
    # 原始语音
    clean, a_sr = librosa.load('./data/clean.wav', sr=8000)
    '''加入背景噪声'''
    noise, b_sr = librosa.load('./data/noise.wav', sr=8000)
    start = random.randint(0, noise.shape[0] - clean.shape[0])  # 随机取一段噪声 长度和纯净语音长度一致
    slice_noise = noise[int(start):int(start) + clean.shape[0]]  # 切片
    mix = add_noise(clean, slice_noise, 5)
    '''加入回声'''
    # mix = add_echo(clean)
    '''加入混响'''
    # mix = add_reverberation(clean)
    sf.write('./data/mix.wav', mix, 8000)
