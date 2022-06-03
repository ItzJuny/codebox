#使用bat执行ffmpeg指令
import os
import numpy as np

# ffmpeg -i XX/1.wav -f s16le XX/1.pcm

if __name__ == '__main__':
    wav_path = "path/to/wavfiles"
    pcm_path = "path/to/save/pcmfiles"
    bat_file = "path/to/batfile"
    os.makedirs(pcm_path,exist_ok=True)
    files = os.listdir(wav_path)
    for i, name in enumerate(files):
        old_name = os.path.join(wav_path, name)
        new_name = os.path.join(pcm_path, name[:-4])
        line = "ffmpeg -i " + old_name + " -f s16le " + new_name + ".pcm"
        #print(line)
        with open(bat_file, 'a+') as f:
            f.write(line + '\n')
