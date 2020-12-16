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
FileName = 'day16.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getIntValues(l):
  return(list(map(int,(re.findall(r'\d+', l)))))

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList

def test01():
  data=[]
  if(os.path.exists(FileName)):
    data=getData(FileName)

  positions=[]
  ranges=[]
  myticket=[]
  samples=[]
  types = 0
  for line in data:
    if not line=="":
      val=getIntValues(line)
      if "your ticket" in line:
        types=1
      elif "nearby tickets" in line:
        types=2
      else:
        if types==0:
          ranges.append(val)
          positions.append(line)
        if types==1:
          myticket=val
        if types==2:
          samples.append(val)

  errorRate = 0
  validTickets=[]
  for ticket in samples:
    isValid = True
    for val in ticket:
      inRange=False
      for mn1,ma1,mn2,ma2 in ranges:
        if mn1 <= val <= ma1 or mn2 <= val <= ma2:
          inRange=True
          break
      if not inRange:
        errorRate+=val
      isValid &= inRange
    if isValid:
      validTickets.append(ticket)
  print("Part1", errorRate)

  invalidField=defaultdict(list)
  allValid = set(list(range(len(ranges))))
  for ticket in validTickets:
    for field,val in enumerate(ticket):

      possible=set([])
      for index, rng in enumerate(ranges):
        mn1,ma1,mn2,ma2 = rng
        if mn1 <= val <= ma1 or mn2 <= val <= ma2:
          possible.add(index)


      invalid=list(allValid-possible)
      invalidField[field].extend(invalid)

  validPos=defaultdict(int)
  while(len(validPos)<len(ranges)):
    for i in range(len(ranges)):
      invalid=set(invalidField[i])
      valid=list(allValid-invalid)
      if len(valid)==1:
        validPos[i]=valid[0]
        allValid.remove(valid[0])

  depart=1
  for i in validPos:
    if "departure" in positions[validPos[i]]:
      depart*=myticket[i]

  print("Part2",depart)


test01()