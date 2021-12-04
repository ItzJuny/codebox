import os,wave
import numpy as np
pcm_path=r"path/to/pcmfiles"
seg_pcm_path=pcm_path=r"path/to/save/pcmfiles"
os.makedirs(seg_pcm_path,exist_ok=True)

samples=16000
seg_time=1
#正常来说,1秒的pcm文件有16000个采样点=8000采样频率*量化位数2*声道数1*时间1.
seg_samples=int(seg_time*samples)

for dirname, _, filenames in os.walk(pcm_path):
    for filename in filenames:
        file=os.path.join(dirname, filename)
        pcmdata = open(file, 'rb').read()
        #print("len(pcmdata):",len(pcmdata))
        print("-----正在分割样本%s-----"%file)
        print("     样本长度为%.1fs"%(len(pcmdata)/samples))
        print("     分割长度为%.1fs,分割样本数量%d个"%(seg_time,len(pcmdata)/seg_samples))
        for i in range(int(len(pcmdata)/seg_samples)):
            newdata=pcmdata[i*seg_samples:(i+1)*seg_samples]
            newfilename = "%s_%d.pcm"%(os.path.splitext(filename)[0],i)
            newfile=open(os.path.join(seg_pcm_path, newfilename),'wb')
            newfile.write(newdata)
