# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path

#rename file
FileName = 'day18.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList

def getNumber(inp,mult,add,value):
  if inp.isdigit():
    if mult:
      value*=int(inp)
      mult=False
    elif add:
      value+=int(inp)
      add=False
    else:
      value=int(inp)
  else:
    if inp=='+':
      add=True
    if inp=='*':
      mult=True
  return(mult,add,value)

def interpret(l):
  index=0
  sums=0
  mult=False
  adds=False
  while index<len(l):
    char=l[index]
    index+=1
    if char=='(':
      val,delta=interpret(l[index:])
      index+=delta
      char=str(val)
    elif char==')':
      return(sums,index)
    mult,adds,sums=getNumber(char,mult,adds,sums)
  return(sums,index)

def interpretOrder(l,prevMult):
  index=0
  sums=0
  mult=False
  adds=False
  while index<len(l):
    char=l[index]
    index+=1
    if char=='(':
      val,delta=interpretOrder(l[index:],False)
      index+=delta
      char=str(val)
    elif char==')':
      if prevMult:
        return(sums,index-1)
      return(sums,index)
    mult,adds,sums=getNumber(char,mult,adds,sums)
    if mult:
      if prevMult:
        return(sums,index-1)
      else:
        val,delta=interpretOrder(l[index:],True)
        index+=delta
        char=str(val)
        mult,adds,sums=getNumber(char,mult,adds,sums)
  return(sums,index)


def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  sums=0
  sumsOrder=0
  for l in line:
    p,v=interpret(l)
    sums+=p
    p,v=interpretOrder(l,False)
    sumsOrder+=p
  print("part1",sums)
  print("part2",sumsOrder)


test01()