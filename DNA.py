#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 07:38:39 2019

@author: axl
"""
import random

class DNA:
    def __init__(self,nGenes):
        self.genes = []
        self.nGenes = nGenes
        self.randomGenes()
        self.fitness = 0
        
    def randomGenes(self):
        for num in range(self.nGenes):
            numAscii = random.randint(64,122)
            if numAscii == 64:
                numAscii = 32
            self.genes.append(chr(numAscii))
    
    def calcFitness(self,target):
        skorFitness = 0
        for nGen in range(len(self.genes)):
            if self.genes[nGen] == target[nGen]:
                skorFitness=skorFitness+1
        self.fitness = skorFitness
        
    def mutate(self,mutasiRate):
        #print("sblm mutasi : {0}".format(self.genes))
        for num in self.genes:
            if random.random()<mutasiRate:
         #       print("termutasi")
                randi = random.randint(0,self.nGenes-1)
                self.genes[randi] = chr(random.randint(32,126))
        #print("stlh mutasi : {0}".format(self.genes))        