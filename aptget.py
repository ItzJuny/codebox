"""
    实验室没办法使用apt-get 安装，但是wget可以使用，所以每次apt-get install xxx失败之后，
        使用apt --fix-broken install会生成一些deb文件，把这些保存成file。

    Usage: python aptget.py -i file -d path
            会生成download.sh和install.sh，执行就好了。
            
    file: 为无法下载的文字文件，例如
        E: 无法下载 http://mirrors.ustc.edu.cn/ubuntu/pool/main/g/gcc-9/libgfortran-9-dev_9.3.0-17ubuntu1~20.04_amd64.deb  文件尺寸不符(479 != 684348)。您使用的镜像正在同步中？ [IP: 218.104.71.170 80]
        Hashes of expected file:
            - SHA512:390a43e997f23ade0a74d6544ce1302671946ffe2fe7e38bbc8cf75d55c2f1ca3e92d61c86af956b9cb3631e91e4c5d289daf5339ca3fb64e669d38fe20dbe07
            - SHA256:5aec287c044d808259957759dcc63371c6c8d285ed5e5f8277ce98851b87e048
            - SHA1:b89c7b9d48c7047afed5f931e96ed54d4064bd72 [weak]
            - MD5Sum:ffc98e6999efa225a38ccad3110c05ff [weak]
            - Filesize:684348 [weak]

    path: 下载安装路径

"""
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser(prog='download deb')
parser.add_argument('-i','--input', type=str, help="path/to/load/file")
parser.add_argument('-d','--download', type=str, help="path/to/save/downloadfiles")
opt = parser.parse_args()

lines=open(opt.input,encoding='utf-8')
urls=[]
names=[]

for line in lines:
    if ".deb" in line:
        start=line.find("http")
        end=line.find(".deb")
        url=line[start:end+4]
        name=os.path.basename(url)
        urls.append(url)
        names.append(name)
lines.close()
"""url for download"""
f1=open("download.sh",'w')
for url in urls:
    f1.write("wget %s -P %s\n"%(url,opt.download))
f1.close()
"""name for install"""
f2=open("install.sh",'w')
for name in names:
    f2.write("dpkg -i %s\n"%(os.path.join(opt.download,name)))
f2.close()
