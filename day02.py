# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
import time

#rename file
FileName = 'day02.txt'
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
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)

  start=time.time()
  valid=0
  for l in line:
    low,high=getIntValues(l)
    num,c,password=l.split()
    char=c[0]
    count=password.count(char)
    if low<=count and high>=count:
      valid+=1

  print("Part1",valid,time.time()-start)


  start=time.time()
  valid=0
  for l in line:
    low,high=getIntValues(l)
    num,c,password=l.split()
    char=c[0]
    if (password[low-1]==char) ^ (password[high-1]==char):
      valid+=1

  print("Part2",valid,time.time()-start)

test01()