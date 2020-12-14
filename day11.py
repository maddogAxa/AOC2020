# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import time
#rename file
FileName = 'day11.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList

def ns(seats,new):
  area=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
  changed=False
  for y,row in enumerate(seats):
    for x,seat in enumerate(row):
      if seat!='.':
        taken=0
        for dx,dy in area:
          nx=x+dx
          ny=y+dy
          if 0<=nx<len(row) and 0<=ny<len(seats):
            if seats[ny][nx]=="#":
              taken+=1
        if seat=='L':
          if taken==0:
            new[y][x]='#'
            changed=True
        else:
          if taken>=4:
            new[y][x]='L'
            changed=True
  return(changed)

def newseats(seats,new):
  area=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
  changed=False
  for y,row in enumerate(seats):
    for x,seat in enumerate(row):
      if seat!='.':
        taken=0
        for dx,dy in area:
          nx=x
          ny=y
          while True:
            nx+=dx
            ny+=dy
            if 0<=nx<len(row) and 0<=ny<len(seats):
              if seats[ny][nx]=="#":
                taken+=1
                break
              elif seats[ny][nx]=="L":
                break
            else:
              break
        if seat=='L':
          if taken==0:
            new[y][x]='#'
            changed=True
        else:
          if taken>=5:
            new[y][x]='L'
            changed=True
  return(changed)

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  val=[]
  for l in line:
    val.append(list(l))
  start=time.time()
  while True:
    old=val
    val=[]
    for i in old:
      val.append(i[:])
    if not ns(old,val):
      taken=0
      for row in val:
        taken+=row.count('#')
      print("part 1",taken,time.time()-start)
      break

  val=[]
  for l in line:
    val.append(list(l))
  start=time.time()
  while True:
    old=val
    val=[]
    for i in old:
      val.append(i[:])
    if not newseats(old,val):
      taken=0
      for row in val:
        taken+=row.count('#')
      print("part 2",taken,time.time()-start)
      break

test01()