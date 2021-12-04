import os
import numpy as np


# ffmpeg -i XX/1.wav -f s16le XX/1.pcm

def create_fold(path):
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)


if __name__ == '__main__':
    for time in np.arange(0.1, 1, 0.1):
    # for time in range(2, 11):
        wav_path = "F:\\data\\AMR_NB_WAV\\%.1fs" % time
        pcm_path = "F:\\data\\AMR_NB_PCM\\%.1fs" % time
        txt_file = "F:\\data\\AMR_NB_PCM\\wav2pcm_%.1fs.txt" % time
        create_fold(pcm_path)
        files = os.listdir(wav_path)
        for i, name in enumerate(files):
            old_name = os.path.join(wav_path, name)
            new_name = os.path.join(pcm_path, name[:-4])
            line = "ffmpeg -i " + old_name + " -f s16le " + new_name + ".pcm"
            print(line)

            with open(txt_file, 'a+') as f:
                f.write(line + '\n')
        bat_file = "F:\\data\\AMR_NB_PCM\\wav2pcm_%.1fs.bat" % time
        os.rename(txt_file, bat_file)
