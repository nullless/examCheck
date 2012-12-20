# -*- encoding: gb2312 -*-
'''
Created on 2012-12-19

@author: fishWin7
'''
from hashlib import md5
import os
 
def md5File(name):
    m = md5()
    cFile = open(name, 'rb') #二进制读取
    m.update(cFile.read())
    cFile.close()
    return m.hexdigest()

def loopFile(path):
    path = path+'rightAnswer/'
    li = []
    for ansFile in os.listdir(path):
        if os.path.isfile(os.path.join(path,ansFile))==True:
            print ansFile
            li.append(ansFile+' ^ '+md5File(path+ansFile))
    return li

def toTxt(cont,path):
    f = open(path+'md5Ans.txt','w')
    for i in cont:
        k=''.join([str(j) for j in i])
        f.write(k+"\n")
    f.close()

if __name__ == "__main__":
    path = './' #正式使用的时候请取消该注释
    toTxt(loopFile(path),path)
