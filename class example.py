import datetime
import random
import pandas as pd
class bank(object):
    def __init__(self, name, tax_num, num_branches):
        self.name = name
        self.tax_num = tax_num
        self.num_branch = num_branches
        self.list = [1,2,3]
    def __str__(self):
        return f"{self.name} is a bank with {self.num_branches} branches"
    def fetch(self):
        for i in self.list:
            yield i
class inflow(object):
    def __intit__(self):
        self.volume = 0
        self.date = None
    def set_volume(self,val):
        self.volume += val
    def get_volume(self):
        return volume
class branch(object):
    pass
class location(object):
    '''assumes the world in which these locations exists is 2d'''
    def __init__(self,x,y,unit_factor):
        self.x = x * unit_factor
        self.y = y * unit_factor
    def reset(self,x,y,unit_factor):
        self.x = x * unit_factor
        self.y = y * unit_factor
    def move(self, deltaX, deltaY, unit_factor):
        self.x = self.x + deltaX*unit_factor
        self.y = self.y + deltaY*unit_factor
        return self
    def dist(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    def __str__(self):
        return f" x : {self.x}, y :{self.y}"
    def __lt__(self,other):
        return self.dist(origin) < other.dist(origin)
origin = location(0,0,1)

x = 2
def f(x):
    x +=2
f(x)
print(x)
    

        
        
