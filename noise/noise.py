from noise_utils import *
from tqdm import tqdm

Time = "1"
SNR = 0
path = r"D:path/to/wav"
save_path = r"path/to/save"
os.makedirs(save_path, exist_ok=True)
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]
savefiles = os.listdir(save_path)
savefiles = [f.split("noise_%dDB_" % SNR)[1] for f in savefiles if f.endswith('.wav')]
if __name__ == '__main__':
    for i in tqdm(range(len(files))):
        FileName = files[i]
        origin_name = os.path.basename(FileName)
        if origin_name not in savefiles:
            clean, a_sr = librosa.load(FileName, sr=8000)
            # '''加入背景噪声'''
            noise, b_sr = librosa.load('./data/noise.wav', sr=8000)
            start = random.randint(0, noise.shape[0] - clean.shape[0])  # 随机取一段噪声 长度和纯净语音长度一致
            slice_noise = noise[int(start):int(start) + clean.shape[0]]  # 切片
            mix = add_noise(clean, slice_noise, SNR)
            sf.write(save_path + "noise_%dDB_" % SNR + origin_name, mix, 8000)
