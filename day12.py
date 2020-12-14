# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re

#rename file
FileName = 'day12.txt'
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

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  instruction=[]
  for l in line:
    value=getIntValues(l)
    instruction.append([l[0],value[0]])

  ship=0
  direction=1
  for action,value in instruction:
    if action=='F':
      ship+=value*direction
    if action=='N':
      ship+=value*1j
    if action=='S':
      ship-=value*1j
    if action=='E':
      ship+=value
    if action=='W':
      ship-=value
    if action=='R':
      turn=value//90
      direction*=(-1j)**turn
    if action=='L':
      turn=value//90
      direction*=(1j)**turn
  print("part1",int(abs(ship.real)+abs(ship.imag)))


  waypoint=10+1j
  ship=0
  for action,value in instruction:
    if action=='F':
      ship+=value*waypoint
    if action=='N':
      waypoint+=value*1j
    if action=='S':
      waypoint-=value*1j
    if action=='E':
      waypoint+=value
    if action=='W':
      waypoint-=value
    if action=='R':
      turn=value//90
      waypoint*=(-1j)**turn
    if action=='L':
      turn=value//90
      waypoint*=(1j)**turn
  print("part2",int(abs(ship.real)+abs(ship.imag)))



test01()