# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
from collections import defaultdict

#rename file
FileName = 'day24.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList

def getPos(line):
  dirs={"e":2,"w":-2,"nw":-1-1j,"sw":-1+1j,"ne":1-1j,"se":1+1j}
  pos=0
  move=""
  for char in line:
    move+=char
    if move in dirs:
      pos+=dirs[move]
      move=""
  return(pos)

def addNewBlack(black,newB,a,tilesAround):
  nearBlack = 0

  delta=[-2,2,-1-1j,-1+1j,1-1j,1+1j]
  for b in delta:
    c=a+b
    if not c in black:
      if c in tilesAround:
        tilesAround[c]+=1
      else:
        tilesAround[c]=1
    else:
      nearBlack+=1
  if 1<=nearBlack<= 2:
    newB.add(a)


def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  black=set([])

  for l in line:
    pos = getPos(l)
    if pos in black:
      black.remove(pos)
    else:
      black.add(pos)
  print("part1:",len(black))

  for r in range(100):
    tilesAround=defaultdict()
    newB=set([])
    for a in black:
      addNewBlack(black,newB,a,tilesAround)
    for tile in tilesAround:
      if tilesAround[tile]==2:
        newB.add(tile)
    black=newB
  print("part2",len(black))





test01()