#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 05:21:35 2019

@author: axl
"""
import random
arr = []
arr.append([1,2,3,1,2])
arr.append([2,5,10,5,6])
arr.append([9,222,31,121,12])
arr.append([0,9,5,1,3])
print("sblm mutasi : {0}".format(arr))
for num in range(len(arr)):
    for num2 in range(len(arr[num])):
       randi = random.randint(0,len(arr)-1)
       arr[num][num2] = random.randint(32,126)
print("stlh mutasi : {0}".format(arr))  