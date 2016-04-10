'''
Created on Apr 10, 2016

@author: chunq
'''

import datetime

class Animal(object):
    def __init__(self, name, time):
        self.name = name
        self.time = time
    
class Dog(Animal):
    pass
    
class Cat(Animal):
    pass
    
class AnimalShelter(object):
    def __init__(self):
        self.dogList = []
        self.catList = []
        
    def enqueue(self, animal):
        animal.time = datetime.datetime.now()
        if isinstance(animal, Dog):
            self.dogList.append(animal)
        elif isinstance(animal, Cat):
            self.catList.append(animal)
        return
    
    def dequeueDog(self):
        if len(self.dogList) > 0:
            return self.dogList.pop()
        return None
    
    def dequeueCat(self):
        if len(self.catList) > 0:
            return self.catList.pop()
        return None
    
    def dequeueAny(self):
        if len(self.catList) > 0 and len(self.dogList) > 0:
            if self.catList[len(self.catList) - 1].time > self.dogList[len(self.dogList) - 1].time:
                return self.catList.pop()
            else:
                return self.dogList.pop()
        elif len(self.catList) > 0:
            return self.catList.pop()
        elif len(self.dogList) > 0:
            return self.dogList.pop()
        return None
    
        
            