# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]
from itertools import islice
from collections import defaultdict
import time
#rename file
FileName = 'day23.txt'
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


def getFirst(cup,c,setC):
  a=cup.popleft()
  if a in setC:
    cup.extendleft(c[a])
    del c[a]
    setC.remove(a)
  return a


def test01():
  line="496138527"
  line=list(line)
  n=list(map(int,line))
  t=deque()
  for a in n:
    t.append(a)
  for a in range(len(t)+1,10**6+1):
    t.append(a)
  print(n)
  start=time.time()
  j=-1
  t.rotate(-1)
  pp=defaultdict(list)

  for i in range(10**2):

    val=t[-1]-1


    a=t.popleft()
    b=t.popleft()
    c=t.popleft()



    sss=set([a,b,c,0])
    while val in sss:
      val-=1
      if val < 0:
        val=max(t)


    pp[val]=[a,b,c]
    j=t.index(val)
    t.rotate(-1-j)
    t.appendleft(c)
    t.appendleft(b)
    t.appendleft(a)
    t.rotate(j)
  j=t.index(1)
  t.rotate(-j-1)
  print(t[6])
  v=t[0]*t[1]
  print(v,time.time()-start)


  del pp[3]

  print()

  rounds = 10**7
  maxN=10**6
  cup = deque()
  for a in n:
    cup.append(a)
  for a in range(len(cup)+1,10**6+1):
    cup.append(a)


  c=defaultdict(list)
  setC=set([])

  for r in range(rounds):
    if r
    val = getFirst(cup,c,setC)
    cup.append(val)
    val-=1
    pickUp=[getFirst(cup,c,setC),getFirst(cup,c,setC),getFirst(cup,c,setC)]
    while val==0 or val in pickUp:
      val-=1
      if val<=0:
        val=maxN
    pickUp=pickUp[::-1]
    if val in setC:
      c[val].extend(pickUp)
    else:
      setC.add(val)
      c[val]=pickUp
  while len(setC):
    while not cup[0] in c:
      cup.rotate(-1)
    a=getFirst(cup,c,setC)
    cup.append(a)
  idx=cup.index(1)
  cup.rotate(-idx)
  print(cup[1]*cup[2])


test01()