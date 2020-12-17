# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]
from collections import defaultdict
import time
#rename file
FileName = 'day17.txt'
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

def rule(maps,x,y,z,mX,mY,mZ):
  see=0
  isActive=False
  for nz in range(z-1,z+2):
    if 0<=nz<mZ:
      for ny in range(y-1,y+2):
        if 0<=ny<mY:
          for nx in range(x-1,x+2):
            if 0<=nx<mX:
              if z!=nz or x!=nx or y!=ny:
                if maps[nz][ny][nx]=="#":
                  see+=1
              else:
                if maps[nz][ny][nx]=="#":
                  isActive=True

  if isActive:
    if 2<=see<=3:
      return(True)
    else:
      return(False)
  else:
    if 3==see:
      return(True)
    else:
      return(False)

def getNewMap(maps):
  maxZ=len(maps)
  maxY=len(maps[0])
  maxX=len(maps[0][0])
  newMap=[]
  for z in range(-1,maxZ+1):
    nLayer=[]
    for y in range(-1,maxY+1):
      lay=""
      for x in range(-1,maxX+1):
        if rule(maps,x,y,z,maxX,maxY,maxZ):
          lay+="#"
        else:
          lay+="."
      nLayer.append(lay)
    newMap.append(nLayer)
  return(newMap)


def getNewCoor(coordinates):
  see = defaultdict()

  for x,y,z,w in coordinates:
    for a in range(x-1,x+2):
      for b in range(y-1,y+2):
        for c in range(z-1,z+2):
          for d in range(w-1,w+2):
            if (a,b,c,d) in see:
              see[(a,b,c,d)]+=1
            else:
              see[(a,b,c,d)]=1

  activeCoordinates=set([])
  for possible in see:
    if possible in coordinates:
      if 3<=see[possible]<=4:
        activeCoordinates.add(possible)
    else:
      if see[possible]==3:
        activeCoordinates.add(possible)
  return(activeCoordinates)

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)

  maps=[line]

  start=time.time()
  for r in range(6):
    maps=getNewMap(maps)
  active=0
  for layer in maps:
    for l in layer:
      active+=l.count('#')
  print("part1",active,time.time()-start)

  start=time.time()
  coordinates=set([])
  for y,l in enumerate(line):
    for x,b in enumerate(l):
      if b=="#":
        coordinates.add(tuple([x,y,0,0]))
  for loop in range(6):
    coordinates = getNewCoor(coordinates)
  print("part2",len(coordinates),time.time()-start)


test01()