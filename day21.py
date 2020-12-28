# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:08:35 2019

@author: henri
"""

import os.path
from collections import defaultdict
#rename file
FileName = 'day21.txt'
if(os.path.exists("input.txt")):
  os.rename('input.txt', FileName)

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

  #generate food list with ingredients
  #generate allergens dict, where allergen points to food index
  food=[]
  allergens=defaultdict(list)
  for foodIndex,l in enumerate(line):
    p=l.split(" (contains ")
    include =p[1].split()
    food.append(p[0].split())
    for allergen in include:
      allergens[allergen[:-1]].append(foodIndex)

  #generate appear dict where allergen point to ingredients that are common for all foods
  appear=defaultdict(list)
  for allergen in allergens:
    for foodIndex in allergens[allergen]:
      if allergen in appear:
        ingredientSet=set(food[foodIndex])
        common=ingredientSet -( ingredientSet - set(appear[allergen]) )
        appear[allergen]=list(common)
      else:
        appear[allergen]=food[foodIndex]

  #generate ingredient set that holds allergen
  allergenIngredient=set([])
  for allergen in appear:
    allergenIngredient.update(set(appear[allergen]))

  #counts the ingredients that cannot hold an allergen
  noAllergen=0
  for ingredients in food:
    for ingredient in ingredients:
      if not ingredient in allergenIngredient:
        noAllergen+=1
  print("part1",noAllergen)


  #generate a convert dict where ingredient holds a list of possible allergens
  convert=defaultdict(list)
  for ingredient in allergenIngredient:
    for allergen in appear:
      if ingredient in appear[allergen]:
        convert[ingredient].append(allergen)


  #update convert list where each ingredient holds only one allergent
  while True:
    updated=False
    #check each ingredient
    for ingredientA in convert:
      #if ingredient holds only one allergen
      if len(convert[ingredientA])==1:
        #remove that allergen from other ingredients
        for ingredientB in convert:
          if len(convert[ingredientB])>1 and convert[ingredientA][0] in convert[ingredientB]:
            convert[ingredientB].remove(convert[ingredientA][0])
            #we have updated the ingredient list
            updated=True
        #if we removed an allergent, do not look for more
        if updated:
          break
    #if we have not updated the list, we must have found all
    if not updated:
      break
  #generate allergen list and sort it
  allergentList=[]
  for ingredient in convert:
    allergentList.append(convert[ingredient])
  allergentList.sort()

  #get ingredients for each allergen
  solution=""
  for allergen in allergentList:
    for ingredient in convert:
      if convert[ingredient]==allergen:
        solution+=ingredient+","
  print("part2",solution[:-1])



test01()