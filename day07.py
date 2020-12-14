# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]

#rename file
FileName = 'day07.txt'
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

def findInside(TopBag,BagsInside,searchBag,counted):
  count=0
  for i,bags in enumerate(BagsInside):
    for bag in bags:
      if searchBag == bag:
        if not TopBag[i] in counted:
          counted.add(TopBag[i])
          count+=1
          count+=findInside(TopBag,BagsInside,TopBag[i],counted)
  return(count)


def numberBags(TopBag,BagsInside,InsideCount,searchBag,multi):
  count=0
  for i,bag in enumerate(TopBag):
    if searchBag == bag:
      for j,insideBag in enumerate(BagsInside[i]):
        count+=multi*InsideCount[i][j]
        count+=numberBags(TopBag,BagsInside,InsideCount,insideBag,multi*InsideCount[i][j])
  return(count)


def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)

  TopBag=[]
  BagsInside=[]
  InsideCount=[]

  for l in line:
    top,inside=l.split("contain")

    top=top.split()
    TopBag.append(top[0]+" "+top[1])

    check=inside.split()
    bagList=[]
    countList=[]
    for i,w in enumerate(check):
      if "bag" in w:
        p=check[i-2]+" "+check[i-1]
        if not p in "no other":
          bagList.append(p)
          countList.append(int(check[i-3]))
    InsideCount.append(countList)
    BagsInside.append(bagList)


  print("Part1",findInside(TopBag,BagsInside,"shiny gold",set([])))
  print("Part2",numberBags(TopBag,BagsInside,InsideCount,"shiny gold",1))



test01()