# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path

#rename file
FileName = 'day04.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList

def req(p):
  valid=['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
  for i,e in enumerate(p):
    if i%2==0:
      if not e in valid:
        return(False)
      valid.remove(e)
  if len(valid)>1:
    return(False)
  elif len(valid)==1:
    if valid[0]=='cid':
      return(True)
  else:
    return(True)

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)

  passport=[]
  newP=[]
  for l in line:
    if l=="":
      if req(newP):
        passport.append(newP)
      newP=[]

    else:
      entries=l.split()
      for entry in entries:
        key,value=entry.split(':')
        newP.extend([key,value])

  if req(newP):
    passport.append(newP)
  print("part1",len(passport))

  validPassport=0
  for pa in passport:
    validPass=True
    for i,l in enumerate(pa):
      if i%2==0:
        key,code=pa[i:i+2]
        if key=="byr":
          check=False
          if code.isdigit():
            if 1920 <= int(code)<=2002:
              check=True
          validPass = validPass and check
        elif key=="iyr":
          check=False
          if code.isdigit():
            if 2010 <= int(code)<=2020:
              check=True
          validPass = validPass and check
        elif key=="eyr":
          check=False
          if code.isdigit():
            if 2020 <= int(code)<=2030:
              check=True
          validPass = validPass and check
        elif key=="hgt":
          check=False
          if code[:-2].isdigit():
            c=int(code[:-2])
            unit=code[-2:]
            if unit=="cm":
              if 150 <= c<=193:
                check=True
            elif unit=="in":
              if 59 <= c<=76:
                check=True
          validPass = validPass and check
        elif key=="hcl":
          check=False
          if len(code)==7:
            if code[0]=="#":
              count=0
              for digit in code[1:]:
                if ord('0') <= ord(digit)<=ord('9'):
                  count+=1
                if ord('a') <= ord(digit)<=ord('f'):
                  count+=1
              if count==6:
                check=True
          validPass = validPass and check
        elif key=="ecl":
          color=["amb","blu","brn","gry","grn","hzl","oth"]
          if not code in color:
            validPass=False
        elif key=="pid":
          count=0
          for digit in code:
            if ord('0') <= ord(digit)<=ord('9'):
              count+=1
          if count!=9:
            validPass=False
        else:
          if not key=="cid":
            validPass=False
    if validPass:
      validPassport+=1
  print("part2",validPassport)

test01()