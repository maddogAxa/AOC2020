# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]

#rename file
FileName = 'day06.txt'
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

  group=set([])
  count=[]
  for l in line:
    if l=="":
      count.append(len(group))
      group=set([])
    else:
      group.update(l)

  count.append(len(group))
  print("part1",sum(count))


  start = 0
  group=set([])
  count=[]
  for l in line:
    if l=="":
      count.append(len(group))
      group=set([])
      start = 0
    else:
      if start==0:
        group.update(l)
        start=1
      else:
        group&=set(l)

  count.append(len(group))
  print("part2",sum(count))



test01()