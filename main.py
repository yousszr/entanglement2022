
from codecs import xmlcharrefreplace_errors
from os import system
import sys
import itertools
from collections import OrderedDict
from operator import itemgetter    
# generate random integer values
from random import seed
from random import randint
import numpy as np


class Object:
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __str__(self):
        return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2) 
        
C=0
Clients=[]
ingredients={}
ingredientslikes={}
ingredientsdlikes={}


def parseInput(file):
    global C
    global Clients
    lines = []
    with open(file) as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        
        if(count==1):
          count+=1
              
        
        elif(count==2):
          count=1
        
        if(count==0):
          count=+1

        
         
def object_score(object):
    finalscore=0
        
    return finalscore
        

def ObjectsUpdate(object): 
    new_list=[]
    return new_list
   
def all_score(ingredients):
    
    score=0

    return score

def output(objects):
    sourceFile = open(sys.argv[2], 'w')
    sourceFile.write("{} ".format(str(len(objects)))+ " ".join(list(objects)))
    sourceFile.close()
    

if __name__ == "__main__":

    parseInput(sys.argv[1])
    objects=[]
    not_finished=False
    while(not_finished):
        
        if(True):        #Pulisco la lista di ingredienti da quelli scelti
           newscore=[]
           if(newscore>scores):
             output(objects)
             scores=newscore
         
           Objects=ObjectsUpdate(fingredients) # aggiorna la lista dei clietni,
           print("SCORE --> "+ str(scores))

        else:
            
            not_finished=False
    

 
