import os,wave
import numpy as np
# def wav2pcm(audio_in_path,audio_out_path):
#     for file in os.listdir(path):
#     data = 0
#     f = open(os.path.join(path,file))
#     f.seek(0)
#     f.read(44)
#     data = np.fromfile(f, dtype=np.int16)
#     dataname = file.rstrip('wav')+'pcm'
#     data.tofile(os.path.join(pcm_path, dataname))
def pcm2wav(in_pcm,out_wav):
    f=open(in_pcm,'rb')
    str_data=f.read()
    wave_out=wave.open(out_wav,'wb')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(8000)
    wave_out.writeframes(str_data)

path=r"path/to/pcmfiles"

for dirname, _, filenames in os.walk(path):
    for filename in filenames:
        file=os.path.join(dirname, filename)
        newfile=file.rsplit(".pcm")[0]+".wav"
        pcm2wav(file,newfile)
