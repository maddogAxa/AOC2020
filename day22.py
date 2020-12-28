# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
from collections import deque #pop, append, pop delete end and return its value, [1,2,3,4,5].rotate(-2) = [3,4,5,1,2]

#rename file
FileName = 'day22.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

def getData(filename):
  file = open(filename,"r")
  dataList = file.readlines()
  file.close()
  for index in range(len(dataList)):
    dataList[index]=dataList[index].rstrip('\r\n')
  return dataList


def combat(DeckA,DeckB):
  prevDeckA=set([])
  prevDeckB=set([])
  while True:
    thisDeckA=tuple(DeckA)
    thisDeckB=tuple(DeckB)
    if thisDeckA in prevDeckA and thisDeckB in prevDeckB:
      return(True)
    else:
      prevDeckA.add(thisDeckA)
      prevDeckB.add(thisDeckB)
      cardA=DeckA.popleft()
      cardB=DeckB.popleft()
      if cardA<=len(DeckA) and cardB<=len(DeckB):
        subA=deque()
        subB=deque()
        for i in range(cardA):
          subA.append(DeckA[0])
          DeckA.rotate(-1)
        for i in range(cardB):
          subB.append(DeckB[0])
          DeckB.rotate(-1)
        DeckA.rotate(cardA)
        DeckB.rotate(cardB)

        if combat(subA,subB):
          DeckA.extend([cardA,cardB])
        else:
          DeckB.extend([cardB,cardA])
      else:
        if cardA>cardB:
          DeckA.extend([cardA,cardB])
        else:
          DeckB.extend([cardB,cardA])
      if not DeckA:
        return(False)
      if not DeckB:
        return(True)


def GetDecks(inputs):
  deck=deque()
  for l in inputs:
    if len(l)>0:
      if "Player" in l:
        if len(deck)>0:
          deckA=deck
        deck=deque()
      else:
        deck.append(int(l))
  return(deckA,deck)

def test01():
  line=[]
  if(os.path.exists(FileName)):
    line=getData(FileName)


  deckA,deckB = GetDecks(line)

  while True:
    cardA=deckA.popleft()
    cardB=deckB.popleft()
    if cardA>cardB:
      deckA.extend([cardA,cardB])
    else:
      deckB.extend([cardB,cardA])
    if not deckA:
      winDeck = deckB
      break
    if not deckB:
      winDeck = deckA
      break

  score=0
  multi=0
  while winDeck:
    multi+=1
    score+=multi*winDeck.pop()
  print("Part1",score)



  DeckA,DeckB= GetDecks(line)
  while True:
    if not DeckA:
      winDeck = DeckB
      break
    if not DeckB:
      winDeck = DeckA
      break
    cardA=DeckA.popleft()
    cardB=DeckB.popleft()
    if cardA<=len(DeckA) and cardB<=len(DeckB):
      subA=deque()
      subB=deque()
      for i in range(cardA):
        subA.append(DeckA[0])
        DeckA.rotate(-1)
      for i in range(cardB):
        subB.append(DeckB[0])
        DeckB.rotate(-1)
      DeckA.rotate(cardA)
      DeckB.rotate(cardB)

      if combat(subA,subB):
        DeckA.extend([cardA,cardB])
      else:
        DeckB.extend([cardB,cardA])
    else:
      if cardA>cardB:
        DeckA.extend([cardA,cardB])
      else:
        DeckB.extend([cardB,cardA])

  score=0
  multi=0

  while winDeck:
    multi+=1
    score+=multi*winDeck.pop()
  print("Part2",score)

test01()