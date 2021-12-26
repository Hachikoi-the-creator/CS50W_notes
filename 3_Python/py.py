"""Collections
List []: nice & easy
Tuple (): Inmutable elements, can repeat
x = set() : Mutable, but cannot repeat values
Dictionary : nice & easy
"""
# CLASSES re-make
import math
class Flight():
    # default value of 0
    def __init__(self, cap = 0):
        self.cap = cap
        self.persons = []
        
    def addPerson(self, name:str):
        # check if seats available
        if (self.cap - len(self.persons) <= 0):
            return False
        else:
            self.persons.append(name)
            return True

        

newFlight = Flight(5)
ppl_List = ["jhon", "jane", "Dir", "Doc", "joseph", "Jojo" , "Doc", "joseph", "Jojo"]

for i in ppl_List:
    if newFlight.addPerson(i): 
        print(f"{i} Added to the flight!")
    else: 
        print(f"{i} Could not enter the flight")

print(newFlight.persons)

# More Classes, 'cuz why not






