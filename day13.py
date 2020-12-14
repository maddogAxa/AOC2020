# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]
import math
#rename file
FileName = 'day13.txt'
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

def ff(val,idx,step,startIdx,index,idd,delay):
  found=False
  ch=False
  print(startIdx)
  for a in range(0,idd,step):
    m=index+a
    if m%val[1][startIdx]==delay[startIdx]:
      print(step*val[1][startIdx]-m)
      if( val[1][startIdx]*step-m)<=0:
        return(False)
      if startIdx<len(delay)-1:
        if ch:
          found=ff(val,idx,step,startIdx+1,m,idd,delay)
        else:
          found=ff(val,idx,step*val[1][startIdx],startIdx+1,m,idd*val[1][startIdx+1],delay)
        if found :
          break
        else:
          if not ch:
            ch=True
            step=step*val[1][startIdx]
            idd*=val[1][startIdx+1]
      else:
        found = True
        break
  return(found)

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  val=[]
  for l in line:
    val.append(getIntValues(l))

  startMinute,busId=val
  timeStamp=startMinute[0]

  startTime=[]
  for bId in busId:
    #find delay fromTime stamp to depart
    delayFromBus = timeStamp%bId
    delayToNextBus = (bId-delayFromBus)%bId
    startTime.append(delayToNextBus)
  mn=min(startTime)
  bId = busId[startTime.index(mn)]
  print("part1",bId*mn)



  delay=[]
  l=line[1].split(',')
  for Id in busId:
    delay.append(l.index(str(Id)))

  #swap delay to show minutes when first is 0

  for i,d in enumerate(delay[1:],start=1):
    delay[i]=(busId[i]-d)%busId[i]

  #run through delays, for each step, take the solution for previous
  step=1
  end=1
  offset=0
  for j,d in enumerate(delay):
    end*=busId[j]
    for i in range(offset,end,step):
      if i%busId[j]==d%busId[j]:
        #offset is the found index in the cycle
        offset=i
        #set step to cycle size
        step=end
        break
  print("Part2",offset)

test01()