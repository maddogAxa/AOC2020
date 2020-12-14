# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path

#rename file
FileName = 'day10.txt'
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
  jolts=list(map(int,line))

  jolts.append(0)
  jolts.append(max(jolts)+3)
  jolts.sort()

  diff =[]
  for i,current in enumerate(jolts[1:],start=1):
    diff.append(current-jolts[i-1])
  print("part 1",diff.count(1)*diff.count(3))

  previous=[1]
  for i,current in enumerate(jolts[1:],start=1):
    index=max(0,i-3) #start index must the latest 3 but must start at 0

    arrangements=0
    for j in range(index,i):
      diff=current-jolts[j]
      if diff<=3:
        arrangements+=previous[j-i]
    previous.append(arrangements)
  print("part 2",arrangements)





test01()