# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]

#rename file
FileName = 'day05.txt'
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


def check(f,ma,mn):
  for p in f:
    if p=='F' or p=='L':
      ma=(ma+mn)//2
    else:
      mn=(ma+mn+1)//2
  return(mn)

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  seatId=set([])
  for l in line:
    a=check(l[:-3],127,0)
    b=check(l[-3:],7,0)
    seatId.add(a*8+b)
  print("part1",max(seatId))
  myId = set(list(range(min(seatId),max(seatId))))-seatId
  print("part2",myId)

test01()

def move(cnode,fldht,fldwh):
  for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
    j, i = cnode[0] + dy, cnode[1] + dx
    if 0 <= j < fldht and 0 <= i < fldwh:
      a=0