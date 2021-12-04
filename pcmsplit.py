# # from scipy.io import wavfile
# # sample_rate, samples = wavfile.read(r"F:\DATA\wav\sample7999.wav")
# # print(sample_rate)
    

import os,wave
import numpy as np
pcm_path=r"d:\Users\jun\Pictures\3367\pcm\EN\10s"
samples=16000
seg_time=1
seg_samples=int(seg_time*samples)
seg_pcm_path=os.path.join(r"d:\Users\jun\Pictures\3367\pcm\EN","%.1fs"%seg_time)
os.makedirs(seg_pcm_path,exist_ok=True)
#正常来说,1秒的pcm文件有16000个采样点=8000采样频率*量化位数2*声道数1*时间1.

for dirname, _, filenames in os.walk(pcm_path):
    for filename in filenames:
        file=os.path.join(dirname, filename)
        pcmdata = open(file, 'rb').read()
        print("aaaaaaaaaaa",len(pcmdata))
        print("-----正在分割样本%s-----"%file)
        print("     样本长度为%.1fs"%(len(pcmdata)/samples))
        print("     分割长度为%.1fs,分割样本数量%d个"%(seg_time,len(pcmdata)/seg_samples))
        for i in range(int(len(pcmdata)/seg_samples)):
            #print(i)
            #print(len(pcmdata[i*seg_samples:(i+1)*seg_samples]))
            newdata=pcmdata[i*seg_samples:(i+1)*seg_samples]
            newfilename = "%s_%d.pcm"%(os.path.splitext(filename)[0],i)
            newfile=open(os.path.join(seg_pcm_path, newfilename),'wb')
            newfile.write(newdata)
