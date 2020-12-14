# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]
from collections import defaultdict

#rename file
FileName = 'day14.txt'
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
  #get values
  val=[]
  for l in line:
    val.append(getIntValues(l))


  memory=defaultdict()
  for i,p in enumerate(line):
    l=p.split(" = ")
    if l[0]=="mask":
      bits=l[1][::-1]
    else:
      address,value = val[i]

      for j,b in enumerate(bits):
        if b=='1':
          value|=1<<j
        elif b=='0':
          value&=~(1<<j)
      memory[address]=value

  sums=0
  for adr in memory:
    sums+=memory[adr]
  print("part1",sums)


  memory=defaultdict()
  for i,p in enumerate(line):
    l=p.split(" = ")
    if l[0]=="mask":
      bits=l[1][::-1]
    else:
      address,value = val[i]
      storage=[address]

      for j,b in enumerate(bits):
        pattern=(1<<j)
        if b=='1':
          for l,adr in enumerate(storage):
            storage[l]|=pattern
        elif b=='X':
          storageNew=[]
          for adr in storage:
            adr&=~pattern
            storageNew.append(adr)
            adr|=pattern
            storageNew.append(adr)
          storage=storageNew
      for adr in storage:
        memory[adr]=value

  sums=0
  for adr in memory:
    sums+=memory[adr]
  print("part2",sums)






test01()