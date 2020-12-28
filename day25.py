# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import time

#rename file
FileName = 'day25.txt'
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
  card,door=list(map(int,line))

  start=time.time()

  loop=0
  val =1
  subject = 7
  mod = 20201227
  while True:
    val*=subject
    val%=mod
    loop+=1
    if val == card:
      key = pow(door,loop,mod)
      break
    if val == door:
      key = pow(card,loop,mod)
      break
  print("solution",key)
  print("time",time.time()-start)



test01()