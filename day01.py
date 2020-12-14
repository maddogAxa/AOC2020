# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import time

#rename file
FileName = 'day01.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

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
  start=time.time()
  found=False
  for i in range(len(n)):
    for j in range(i+1,len(n)):
      if n[i]+n[j]==2020:
        print("part1",n[i]*n[j],"Elapsed Time",time.time()-start)
        found=True
        break
    if found:
      break

  sN=set(n)
  start=time.time()
  found=False
  for i in range(len(n)):
    for j in range(i+1,len(n)):
      if 2020-(n[i]+n[j]) in sN:
        found=True
        print("part2",n[i]*n[j]*(2020-(n[i]+n[j])),"Elapsed Time",time.time()-start)
        break
    if found:
      break

  start=time.time()
  found=False
  for e in n:
    if 2020-e in sN:
      if e==1010:
        if n.count(e)>1:
          print("part1",e*(2020-e),"Elapsed Time",time.time()-start)
          break
      else:
        print("part1",e*(2020-e),"Elapsed Time",time.time()-start)
        break

test01()