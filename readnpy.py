"""
python readnpy.py -i npy文件路径
可选参数:
-head n 打印前n行
-tail n 打印尾部n行
-row n 打印第n行(行数从0开始计算)
-col n 打印第n列(列数从0开始计算)
-txt txt目录路径 转换成txt文件
"""
import numpy as np
import argparse
import os
parser = argparse.ArgumentParser(prog='read npyfile')
parser.add_argument('-i', '--input', type=str, required=True,help="path/to/load/npyfile")
parser.add_argument('-head', '--head', type=int, help="read headline")
parser.add_argument('-tail', '--tail', type=int, help="read tailline")
parser.add_argument('-row', '--row', type=int, help="read rowline")
parser.add_argument('-col', '--col', type=int, help="read colline")
parser.add_argument("-txt", "--txt", type=str, help="path/to/save/txtfile")
opt = parser.parse_args()


data=np.load(opt.input)
print(data)

if opt.head is not None:
    print(data[:opt.head])
if opt.tail is not None:
    print(data[-opt.tail:])
if opt.row is not None:
    print(data[opt.row])
if opt.col is not None:
    print(data[:,opt.col])


if opt.txt is not None:
   name=os.path.basename(opt.input).replace("npy","txt")
   np.savetxt(os.path.join(opt.txt,name),data,fmt="%s")