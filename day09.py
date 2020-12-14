# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]

#rename file
FileName = 'day09.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getIntValues(l):
  return(list(map(int,(re.findall(r'-?\d+', l)))))

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  n=list(map(int,line))

  for j,f in enumerate(n[25:]):
    pre=n[j:j+25]
    found=False
    sN=set(pre)
    for e in pre:
      if f-e in sN:
        if not f-e == e:
          found=True
          break
    if not found:
      print(f,j)
      break

  for i,e in enumerate(n[:j]):
    s=0
    mn=f
    ma=0
    ff=False
    for p in n[i:j]:
      s+=p
      mn=min(p,mn)
      ma=max(p,ma)
      if s==f:
        print(mn+ma)
        ff=True
        break
      if s>f:
        break
    if ff:
      break



test01()