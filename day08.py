# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]

#rename file
FileName = 'day08.txt'
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

def execute(prg,pc,acc):

  op,arg=prg[pc]
  if op=="nop":
    pc+=1
  elif op=="jmp":
    pc+=arg
  elif op=="acc":
    acc[0]+=arg
    pc+=1
  else:
    print("Bug")
  return(pc)

def part1(prg):
  #start state
  acc=[0]
  pc=0
  exe=set([])
  while True:
    if pc in exe:
      print("part1",acc)
      break
    else:
      exe.add(pc)
      pc=execute(prg,pc,acc)

def part2(prg):
  #start state
  acc=[0]
  pc=0
  exe=set([])
  while True:
    if pc in exe:
      return(False)
    if pc<0 or pc>len(prg):
      return(False)
    if pc==len(prg):
      print("part2",acc)
      return(True)
    else:
      exe.add(pc)
      pc=execute(prg,pc,acc)

def test01():

  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  prg=[]
  for l in line:
    arg=getIntValues(l)
    op=l.split()
    prg.append([op[0],arg[0]])
  part1(prg)
  change=0
  while True:
    #prepare
    cpy=[]
    for a in prg:
      cpy.append(a[:])
    for a in range(change,len(cpy)):
      c,p=cpy[a]
      if c=="nop":
        cpy[a][0]='jmp'
        change=a+1
        break
      elif c=="jmp":
        cpy[a][0]='nop'
        change=a+1
        break
    if change==len(cpy):
      print("bug")
      break
    if part2(cpy):
      break


test01()

def move(cnode,fldht,fldwh):
  #for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
  for d, t in ((-1, '<'), (1, '>'), (-1j, '^'), (1j, 'v')):
    j, i = cnode[0] + dy, cnode[1] + dx
    if 0 <= j < fldht and 0 <= i < fldwh:
      a=0