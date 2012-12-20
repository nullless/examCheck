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
    path = path+'question/'
    li = []
    for ansFile in os.listdir(path):
        if os.path.isfile(os.path.join(path,ansFile))==True:
            li.append([ansFile,md5File(path+ansFile)])
    print li
    return li

def checkAns(ansLi,rightLi):
    resultLi = ['<table border=\"1\">']
    for li in ansLi:
        print li
        print li[0]
        if li in rightLi:
            tmp = '对'
        else:
            tmp = '错'
        resultLi.append(['<tr><td>'+li[0]+'</td>','<td>'+tmp+'</td></tr>'])
    resultLi.append('</table>')
    return resultLi
    
def getLi(path):
    li=[]
    f=file(path+'md5Ans.txt','r')
    for line in f.readlines():
        tmp = line.split(' ^ ')
        tmp[1] = tmp[1][:32]
        li.append(tmp)
    f.close
    print li
    return li

def toHtml(li):
    f = open(path+'result.html','w')
    for i in li:
        k=''.join([str(j) for j in i])
        f.write(k+"\n")
    f.close()

if __name__ == "__main__":
    path = './' #正式使用的时候请取消该注释
    rightLi = getLi(path)
    ansLi = loopFile(path)
    result = checkAns(ansLi,rightLi)
    toHtml(result)
    os.system('result.html')
    
    print os.getcwd()
    
    
