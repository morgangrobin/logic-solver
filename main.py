

# Wizards always need a pointy hat
# The Cleric, Rogue, and Warrior all insist on getting at least one item of each material (Cloth, Leather, Scale, Steel)
# Steel is heavy, folks can only wear one piece of Steel armor at a time. 
# For fairness reasons, each character has exactly 150 gold to spend on their armor.
# Each character has a signature stat that they need to get to 8 points in. Not more though, fairness again!!
# Cant wear more than two items of the same material

#clothing
import random

class Clothing:
    def __init__(self,slot,size):
        #self.name = name
        self.slot = slot
        self.size = size
        self.wearer = None

    def isAssigned(self):
        if self.wearer is None:
            return False
        else:
            return True
        
    def getWearer(self):
        if self.isAssigned():
            return self.wearer
        else:
            return None

class Person:
    def __init__(self, size):
        self.size = size
        self.hat = None
        self.shirt = None
        self.pants = None

smallHat = Clothing("hat","small")
medHat = Clothing("hat","medium")
largeHat = Clothing("hat","large")
sShirt = Clothing("shirt","small")
mShirt = Clothing("shirt","medium")
lShirt = Clothing("shirt","large")
sPants = Clothing("pants","small")
mPants = Clothing("pants","medium")
lPants = Clothing("pants","large")

smallGuy = Person("small")
mediumGuy = Person("medium")
largeGuy = Person("large")

clothes = [smallHat,medHat,largeHat,sShirt,mShirt,lShirt,sPants,mPants,lPants]
random.shuffle(clothes)
guys = [smallGuy,mediumGuy,largeGuy]
random.shuffle(guys)

def sizeMatch(guy,item):
    if(guy.size == item.size):
        return True
    else:
        return False
    
def everybodysWearingSomething(guys):
    for guy in guys:
        if guy.hat is None or guy.shirt is None or guy.pants is None:
            return False
    return True

def slotNotTaken(guy,item):
    if getattr(guy,item.slot) is None:
        return True
    else:
        return False
    
while not everybodysWearingSomething(guys):
    for guy in guys:
        for item in clothes:
            if sizeMatch(guy,item) and slotNotTaken(guy,item):
                print(f'assigning {item.size} {item.slot} to {guy.size} guy')
                setattr(guy,item.slot,item)

print(f'everybody is wearing something')
for guy in guys:
    print(f'guy {guy.size} is wearing a {guy.hat.size} {guy.hat.slot}, a {guy.shirt.size} {guy.shirt.slot}, and {guy.pants.size} {guy.pants.slot}')
                

