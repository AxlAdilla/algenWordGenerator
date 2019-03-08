#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:12:54 2019

@author: axl
"""
from DNA import DNA
import math
#import os
#import time
import random
class Population:
    def __init__(self,target,mutationRate,nPopulation,maxGen):
        self.target = target
        self.mutationRate = mutationRate
        self.nPopulation = nPopulation
        self.populasi = []
        self.matingPool = []
        self.maxGen =maxGen
        self.randomPop()
    
    def display(self):
        for pop in self.populasi:
            print(pop.genes)
    def randomPop(self):
        for num in range(self.nPopulation):
            self.populasi.append(DNA(len(self.target)))
    #def testLoop(self):
    #    while True:
    #        rand = random.randint(0,len(self.populasi)-1)
    #        print(rand)
    #        print(self.populasi[rand].genes)
    #        time.sleep(0.1)
    #        os.system('clear')
    
    def calcFitness(self):
        for pop in self.populasi:
            pop.calcFitness(self.target)
            #print("indv: {0}".format(pop.genes))
            #print("fitness: {0}".format(pop.fitness))
    def calcMaxFitness(self):
        maxFitness = 0;
        for pop in self.populasi:
            if pop.fitness > maxFitness:
                maxFitness = pop.fitness
        return maxFitness
    def selection(self):
        self.matingPool = [];
        
   
        for pop in self.populasi:
            persentase = math.floor(pop.fitness*10)
            #print("max fitness:{2} \n fitness:{1} \n persentase {0} ".format(persentase,pop.fitness,maxFitness))
            for num in range(persentase):
                self.matingPool.append(pop)
            
    def crossOver(self,parent1,parent2,middle):
        child = DNA(len(self.target))
        for num in range(0,len(self.target)):
            if num < middle:
                child.genes[num]=parent1[num]
            else:
                child.genes[num]=parent2[num]
        return child
    
    def generate(self):
        offspring = []
        i = 0
        middle = random.randint(0,len(self.target)-1)
        
        while i<self.nPopulation:
            #for mate in self.matingPool:
              #  print("mating Pool {0} ".format(mate.genes))
            parent1 = self.matingPool[random.randint(0,len(self.matingPool)-1)]
            parent2 = self.matingPool[random.randint(0,len(self.matingPool)-1)]            
            #print("parent 1 {0} parent2 {1}".format(parent1.genes,parent2.genes))
            child = self.crossOver(parent1.genes,parent2.genes,middle)    
            #print("parent 1 crossover {0}".format(child.genes))
            child.mutate(self.mutationRate)
            
            #print("parent 1 mutate {0}".format(child.genes))
            offspring.append(child)
            i = len(offspring)
            #for a in range(0,i):
             #   print("offsprings {0}".format(offspring[a].genes))

        self.populasi = offspring
        for child in self.populasi:
            print("Kata {0}".format(child.genes))
            
    
    def isFinish(self,nowGen):
        #print(nowGen)
        if nowGen >= self.maxGen :
            
            return True
        else :
            for child in self.populasi:
                child.calcFitness(self.target)
                if child.fitness == len(self.target):
                    return True
        return False