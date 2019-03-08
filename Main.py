#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:13:03 2019

@author: axl
"""
from Population import Population
#from DNA import DNA
import os
import time
if __name__ == "__main__":
    target = 'Hello'
    mutationRate = 0.05
    Populasi = 15
    maxGen = 2000
    newPop = Population(target,mutationRate,Populasi,maxGen)
    #newPop.display()
    #print(len(newPop.populasi))
    #newPop.testLoop()
    nowGen = 0
    while not newPop.isFinish(nowGen):
        
        os.system('clear')
        nowGen=nowGen+1
        print("Target:{0}\nMutation Rate:{1}\nPopulasi:{2}\nMaximal Generasi:{3} ".format(target,mutationRate,Populasi,maxGen))
        print("GENERASI Ke-{0} ".format(nowGen))
        newPop.calcFitness()
        newPop.selection()
        newPop.generate()
        time.sleep(0.08)
        
        
        
    