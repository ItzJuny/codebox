import os
import numpy as np 
wavpath="/home/path/to/wav"
savedir="/home/path/to/wavfeat"
# loading wavfiles
wavfiles=[os.path.join(path,i) for i in os.listdir(path) if os.path.splitext(i)[-1]==".wav"]
if not os.path.exists(savedir):
    os.makedirs(savedir,exist_ok=True)

# wav.scp
f=open(os.path.join(savedir,"wav.scp"),"w")
for i in wavfiles:
    f.write("%s %s\n"%(os.path.basename(i),i))
f.close()

# feats.ark(MFCC)
opt="compute-mfcc-feats --use-energy=false scp:%s/wav.scp ark:%s/feats.ark"%(savedir,savedir)
os.system(opt)

# feat.scp(MFCC) feat.ark(MFCC)
opt="copy-feats ark:%s/feats.ark ark,scp:%s/feat.ark,%s/feat.scp"%(savedir,savedir,savedir)
os.system(opt)

# cmvn.scp cmvn.ark(CMVN)
opt="compute-cmvn-stats scp:%s/feat.scp ark,scp:%s/cmvn.ark,%s/cmvn.scp"%(savedir,savedir,savedir)
os.system(opt)

"""
from kaldi_io import read_mat_scp
data = { k:m for k,m in read_mat_scp(path_to_scpdata) }
"""
