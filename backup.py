"""
    @author:
        Jun
    @function：
        备份（从src备份到dst，并且目录与src一致。）
        1. 判断dst中文件是否在src中存在，不存在删除，若存在需md5一致，否则删除。
        2. 判断src中文件是否在dst中存在，存在时需要md5一致，否则都复制一份。
"""
import hashlib
import os
import shutil
import datetime
def get_md5(filename):
    if not os.path.isfile(filename):
        print(filename+ "is not File")
        return None
    myhash = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            value = f.read(8096)
            if not value:
                break
            myhash.update(value)
    return myhash.hexdigest()

srcpath=r"C:\Users\Wu-Junyan\Desktop\huh"
dstpath=r"I:\huh"

# 判断dst中文件是否在src中存在，不存在删除，若存在需md5一致，否则删除。
print("----------------------处理备份文件夹------------------------------")
for i,j,k in os.walk(dstpath):
    # 文件夹
    for mpath in j:
        dstmpath=os.path.join(i,mpath)
        srcmpath=dstmpath.replace(dstpath,srcpath)
        if not os.path.exists(srcmpath):
            print("处理多余文件夹:",srcmpath)
            shutil.rmtree(dstmpath)
    for file in k:
        dstfile=os.path.join(i,file)
        srcfile=dstfile.replace(dstpath,srcpath)
        if not os.path.exists(srcfile) or get_md5(dstfile) !=get_md5(srcfile):
            print("处理md5不一致文件:",srcfile)
            os.remove(dstfile)
print("-----------------------备份源文件夹------------------------------")
# # 判断src中文件是否在dst中存在，存在时需要md5一致，否则都复制一份。
for i,j,k in os.walk(srcpath):
    # 文件夹
    for mpath in j:
        srcmpath=os.path.join(i,mpath)
        dstmpath=srcmpath.replace(srcpath,dstpath)
        print(srcmpath,dstmpath)
        if not os.path.exists(dstmpath):
            os.makedirs(dstmpath,exist_ok=True)
            print("备份文件夹:",dstmpath)
    for file in k:
        srcfile=os.path.join(i,file)
        dstfile=dstfile.replace(srcpath,dstpath)
        if os.path.exists(dstfile) :
            if get_md5(dstfile) != get_md5(srcfile):
                os.remove(dstfile)
                shutil.copy(srcfile,dstfile)
                print("备份md5不一致文件:",dstfile)
        else:
            shutil.copy(srcfile,dstfile)
            print("备份不存在文件:",dstfile)
