from noise_utils import *
from tqdm import tqdm

Time = "10"
path = r"D:path/to/wav"
save_path = r"path/to/save"
os.makedirs(save_path, exist_ok=True)
files = os.listdir(path)
files = [path + "\\" + f for f in files if f.endswith('.wav')]

if __name__ == '__main__':
    for i in tqdm(range(len(files))):
        if i < 8000:
            FileName = files[i]
            origin_name = os.path.basename(FileName)
            clean, a_sr = librosa.load(FileName, sr=8000)
            mix = add_echo(clean)
            sf.write(save_path + "echo_" + origin_name, mix, 8000)
