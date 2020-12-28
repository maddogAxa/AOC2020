# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
import re
from collections import defaultdict

#rename file
FileName = 'day19.txt'
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


def generate(rules,ruleToMatch,words):
  newWords=set([])
  for rule in ruleToMatch:
      if 'a' in rule:
        if len(words)>0:
          for word in words:
            word+='a'
            newWords.add(word)
        else:
          newWords=set(['a'])
      elif 'b' in rule:
        if len(words)>0:
          for word in words:
            word+='b'
            newWords.add(word)
        else:
          newWords=set(['b'])
      else:
        followRules=getIntValues(str(rule))
        ruleWords=set([])
        for nextRule in followRules:
          wordsForRule=generate(rules,rules[nextRule],words)
          if len(ruleWords)>0:
            tempWords=set([])
            for tailWord in wordsForRule:
              for word in ruleWords:
                word+=tailWord
                tempWords.add(word)
            ruleWords=tempWords
          else:
            ruleWords=wordsForRule
        newWords.update(ruleWords)
  return(newWords)

def addRule31(toCheck,message,valid,rule31,maxLength):
  for aRule31 in rule31:
    nextCheck=toCheck+aRule31
    if nextCheck==message:
      valid.add(message)
    elif len(nextCheck)<len(message) and len(nextCheck)<maxLength:
      if message[:len(nextCheck)]==nextCheck:
        addRule31(nextCheck,message,valid,rule31,maxLength)


def checking(toCheck,message,rule42,rule31,valid):
  if toCheck==message[:len(toCheck)]:
    for aRule42 in rule42:
      nextCheck=toCheck+aRule42
      if len(message)>len(nextCheck):
        if message[:len(nextCheck)]==nextCheck:
          checking(nextCheck,message,rule42,rule31,valid)
          addRule31(nextCheck,message,valid,rule31,2*len(nextCheck)-len(aRule42))




def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)
  rules=defaultdict()
  messages=set([])
  for l in line:
    if len(l)>0:
      if ':' in l:
        v=l.split(': ')
        if '|' in v[1]:
          q=v[1].split(' | ')
        else:
          if 'a' in v[1]:
            q=['a']
          elif 'b' in v[1]:
            q=['b']
          else:
            q=[v[1]]
        rules[int(v[0])]=q
      else:
        messages.add(l)

  allRules=generate(rules,rules[0],set([]))
  valid=set([])
  for message in messages:
    if message in allRules:
      valid.add(message)
  print("part1",len(valid))


  #for the second part we change rule 8
  #  from 42 to 42 | 8
  #  this means when 8 is used it will be a list of rule 42

  #we change rule 11 too
  #  from 42 | 31 to 42 31 | 42 11 31
  #  this means when 11 is used it will be a list of
  #    a number of rule 42 following by the same number of 31

  #only rule 0 uses rule 8 and 42
  #  namely 8 11

  #so the result is:
  #  X number of rule 42 following by Y number of rule 42 followed by Y number of rule 31

  rule42 = generate(rules,rules[42],set([]))
  rule31 = generate(rules,rules[31],set([]))

  valid=set([])
  for message in messages:
    for toCheck in rule42:
      checking(toCheck,message,rule42,rule31,valid)
  print("part2",len(valid))

test01()