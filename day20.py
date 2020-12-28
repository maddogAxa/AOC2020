# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import defaultdict

#rename file
FileName = 'day20.txt'
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

def exists(x,y,maps,seaPos):
  for dx,dy in seaPos:
    if y+dy<len(maps) and x+dx<len(maps[0]):
      if maps[y+dy][x+dx]!="#":
        return(False)
    else:
      return(False)
  return(True)

def tileMatch(edge,tile):
  if tile[0]==edge:
    return(True)
  if tile[0]==edge[::-1]:
    return(True)
  if tile[-1]==edge:
    return(True)
  if tile[-1]==edge[::-1]:
    return(True)

  tileLeft=""
  tileRight=""
  for row in tile:
    tileLeft+=row[0]
    tileRight+=row[-1]
  if edge==tileLeft:
    return(True)
  if edge==tileRight:
    return(True)
  if edge==tileLeft[::-1]:
    return(True)
  if edge==tileRight[::-1]:
     return(True)
  return(False)


def rotateToBottomEdge(edgeBottom,tileToRotate):
  rotated=[]
  if tileToRotate[0]==edgeBottom:
    return(tileToRotate)
  if tileToRotate[0]==edgeBottom[::-1]:
    for row in tileToRotate:
      rotated.append(row[::-1])
    return(rotated)
  if tileToRotate[-1]==edgeBottom:
    for i in range(len(tileToRotate)-1,-1,-1):
      rotated.append(tileToRotate[i])
    return(rotated)
  if tileToRotate[-1]==edgeBottom[::-1]:
    for i in range(len(tileToRotate)-1,-1,-1):
      rotated.append(tileToRotate[i][::-1])
    return(rotated)

  for i in range(10):
    rotated.append("")
  for e in tileToRotate:
    for i,p in enumerate(e):
      rotated[i]+=p

  if edgeBottom==rotated[0]:
    return(rotated)
  if edgeBottom==rotated[-1]:
    q=[]
    for i in range(len(rotated)-1,-1,-1):
      q.append(rotated[i])
    return(q)
  elif edgeBottom==rotated[0][::-1]:
    q=[]
    for row in rotated:
      q.append(row[::-1])
    return(q)
  elif edgeBottom==rotated[-1][::-1]:
    q=[]
    for i in range(len(rotated)-1,-1,-1):
      q.append(rotated[i][::-1])
    return(q)

def rotateToRightEdge(edgeRight,tileToRotate):
  rotatedTile=[]
  for i in range(len(tileToRotate)):
    rotatedTile.append("")

  if tileToRotate[0]==edgeRight:
    for row in tileToRotate:
      for i,p in enumerate(row):
        rotatedTile[i]+=p
    return(rotatedTile)
  if tileToRotate[0]==edgeRight[::-1]:
    for row in tileToRotate:
      for i,p in enumerate(row):
        rotatedTile[i]+=p[::-1]
    return(rotatedTile)
  if tileToRotate[-1]==edgeRight:
    for row in tileToRotate:
      for i,p in enumerate(row):
        rotatedTile[i]+=p[::-1]
    q=[]
    for i in rotatedTile:
      q.append(i[::-1])
    return(q)
  if tileToRotate[-1]==edgeRight[::-1]:
    for row in tileToRotate:
      for i,p in enumerate(row):
        rotatedTile[i]+=p[::-1]
    q=[]
    for i in range(len(rotatedTile)-1,-1,-1):
      q.append(rotatedTile[i][::-1])
    return(q)
  rotatedTile=[]
  left=""
  right=""
  for row in tileToRotate:
    left+=row[0]
    right+=row[-1]
  if edgeRight==left:
    return(tileToRotate)
  elif edgeRight==right:
    for row in tileToRotate:
      rotatedTile.append(row[::-1])
    return(rotatedTile)
  elif edgeRight==left[::-1]:
    for i in range(len(tileToRotate)-1,-1,-1):
      rotatedTile.append(tileToRotate[i])
    return(rotatedTile)
  elif edgeRight==right[::-1]:
    for i in range(len(tileToRotate)-1,-1,-1):
      rotatedTile.append(tileToRotate[i][::-1])
    return(rotatedTile)


def getNext(tileToMach,tiles):
  for tile in tiles:
    if tile!=tileToMach:
      if tileMatch(tiles[tileToMach][-1],tiles[tile]):
        tiles[tile]=rotateToBottomEdge(tiles[tileToMach][-1],tiles[tile])
        return(tile)
  print("Error")

def getRight(tileToMach,tiles):
  edgeRight=""
  for row in tiles[tileToMach]:
    edgeRight+=row[-1]

  for tile in tiles:
    if tile != tileToMach:
      if tileMatch(edgeRight,tiles[tile]):
        tiles[tile]=rotateToRightEdge(edgeRight,tiles[tile])
        return(tile)
  print("Error")

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)

  tiles=defaultdict(list)
  for l in line:
    if l>"":
      anyId = getIntValues(l)
      if len(anyId)>0:
        tileId=anyId[0]
      else:
        tiles[tileId].append(l)


  m1=defaultdict(list)
  m2=defaultdict(list)
  m3=defaultdict(list)
  m4=defaultdict(list)


  for tileA in tiles:
    for tileB in tiles:
      if tileA!=tileB:
        if tileMatch(tiles[tileA][0],tiles[tileB]):
          m1[tileA].append(tileB)

    for tileB in tiles:
      if tileA!=tileB:
        if tileMatch(tiles[tileA][-1],tiles[tileB]):
          m2[tileA].append(tileB)

    edgeLeft=""
    edgeRight=""
    for tileRow in tiles[tileA]:
      edgeLeft+=tileRow[0]
      edgeRight+=tileRow[-1]

    for tileB in tiles:
      if tileA!=tileB:
        if tileMatch(edgeLeft,tiles[tileB]):
          m3[tileA].append(tileB)

    for tileB in tiles:
      if tileA!=tileB:
        if tileMatch(edgeRight,tiles[tileB]):
          m4[tileA].append(tileB)




  solution=1
  mapsRow=[]
  for tileId in tiles:
    edgeCount = 0
    p=0
    if tileId in m1:
      edgeCount+=1
    if tileId in m2:
      edgeCount+=1
      p+=1
    if tileId in m3:
      edgeCount+=1
      p+=2
    if tileId in m4:
      edgeCount+=1
      p+=4
    if edgeCount==2:
      if p==5:
        mapsRow.append(tileId)
      solution *= tileId

  print("part1",solution)

  #generate map
  mapTileId=[]
  while len(mapTileId)<12:
    for i in range(11):
      v=getRight(mapsRow[-1],tiles)
      mapsRow.append(v)
      if len(mapsRow)==12:
        mapTileId.append(mapsRow)
        if len(mapTileId)<12:
          mapsRow=[getNext(mapsRow[0],tiles)]

  maps=[]
  for mapRow in mapTileId:
    for tileRow in range(1,9):
      tileMap=""
      for tileId in mapRow:
        tileMap+=tiles[tileId][tileRow][1:-1]
      maps.append(tileMap)

  #rotate map
  tempMap=[]
  for i in range(len(maps)):
    tempMap.append("")
  for e in maps:
    for i,p in enumerate(e):
      tempMap[i]+=p
#  maps=tempMap

  #mirror map
 # for i in range(len(maps)):
 #   maps[i]=maps[i][::-1]

  sea=[]
  sea.append("..................#.")
  sea.append("#....##....##....###")
  sea.append(".#..#..#..#..#..#...")

  for turn in range(8):
    #find coordinates for sea
    seaPos=[]
    for y in range(len(sea)):
      for x in range(len(sea[y])):
        if sea[y][x]=="#":
          seaPos.append([x,y])
    #find number of sea monsters
    seaMonster=0
    for y in range(len(maps)):
      for x in range(len(maps[y])):
        if(exists(x,y,maps,seaPos)):
          seaMonster+=1
    #stop if seamonsters found
    if seaMonster>0:
      break
    #otherwise rotate seamonster
    tempSea=[]
    for i in range(len(sea[0])):
      tempSea.append("")
    for e in sea:
      for i,p in enumerate(e):
        tempSea[i]+=p
    sea=tempSea
    #if not seamonster found on first rotation
    #mirror seamonster
    if turn==3:
      for i in range(len(sea)):
        sea[i]=sea[i][::-1]

  waveCount=0
  for row in maps:
    waveCount+=row.count("#")
  #subtract seamonsters
  for row in sea:
    waveCount-=seaMonster * row.count("#")
  print("part2",waveCount)






test01()