# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

from collections import defaultdict
import time

def test01():
  start=[0,1,5,10,3,12,19]
  spoken=start[::-1]

  for index in range(len(start),2020):
    if spoken.count(spoken[0])==1:
      age = 0
    else:
      age=spoken[1:].index(spoken[0])+1
    spoken.insert(0,age)
  print("part1",age)


  startTime = time.time()
  latest=defaultdict()
  previous=defaultdict()

  for index,number in enumerate(start):
    latest[number]=index
    previous[number]=index

  repeat=False
  for index in range(len(start),30000000):
    if repeat:
      age = latest[age]-previous[age]
      if age in latest:
        previous[age]=latest[age]
      else:
        repeat=False
    else:
      age=0
      previous[age]=latest[age]
      repeat=True

    latest[age]=index
  print("part2",age,"Elapsed",time.time()-startTime)








test01()