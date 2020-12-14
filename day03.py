# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import time

#rename file
FileName = 'day03.txt'
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

  c=0
  d=0
  e=0
  f=0
  g=0
  start=time.time()
  for i,l in enumerate(line):
    if l[i%len(l)]=='#':
      c+=1
    if l[(3*i)%len(l)]=='#':
      d+=1
    if l[(5*i)%len(l)]=='#':
      e+=1
    if l[(7*i)%len(l)]=='#':
      f+=1
    if i%2==0:
      if l[(i//2)%len(l)]=='#':
        g+=1
  print("Part1",d)
  print("Part2",c*d*e*f*g)
  print("elapsed time:",time.time()-start)



test01()